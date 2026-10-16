"""Pinned finite-model translation to existing YEAN declarations.

Generation is not verification. Fresh Lean replay proves the generated mathematical
instance; no function here proves the Python interpreter or an external source.
Only a fixed, reviewed grammar is emitted, never caller-supplied Lean or shell text.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

from .finite_affine_presentation import normalize_word
from .finite_quotient_retract import FiniteQuotientRetract


class BridgeError(ValueError):
    pass


RUNTIME_PINS = {
    "observational_succ/finite_affine_presentation.py": "aa3203171ddcca1f87b33e5199c4209c62f23908e977c47ca12d2c62b8d39167",
    "observational_succ/finite_quotient_retract.py": "0d68dcd920962701c054b43410aa2a885ff99deef4a8825a0f431969b833edd7",
}
LEAN_PINS = {
    "Yean/SUCC/AffineWord.lean": "77bfbe803999a61e72a3cbfeaad804a948f72d641a9ff55e8310e24488157d4b",
    "Yean/SUCC/TwoPoint.lean": "0a46404ac95ccea592d54fe24334391836813801b5a72cd181ed1b2a443d07a4",
    "Yean/SUCC/FiniteRetract.lean": "a2b915ee6034745222a1be6cc4c1607018007b555a78fbc38d6cc7d6d35be308",
    "lean-toolchain": "7dc000621e0046d1aada809e2b7177e64454645cf4c741e9daaf79c99ec2e7a2",
    "lake-manifest.json": "db796b63ff16b3e7b23530173e92cd7b9d8acaf9f8dcacbb3e175a69f076b1f2",
}
SOURCE_OBLIGATIONS = (
    "Declared source identity and epoch match the intended mathematical carrier",
    "Python execution implements the pinned source text in the declared runtime",
    "External source identification, if requested, requires independent evidence",
)


def digest(value) -> str:
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def verify_pins(root: Path, pins: dict[str, str]) -> None:
    root = root.resolve()
    for relative, expected in pins.items():
        path = (root / relative).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise BridgeError("Missing pinned source: " + relative)
        if sha256(path.read_bytes()).hexdigest() != expected:
            raise BridgeError("Pinned source changed: " + relative)


def _source(source_id, epoch):
    if type(source_id) is not str or not source_id.strip() or len(source_id) > 200:
        raise BridgeError("Explicit bounded source identity required")
    if type(epoch) is not int or epoch < 0:
        raise BridgeError("Exact nonnegative source epoch required")


def _packet(kind, source_id, epoch, inputs, outputs, mapping):
    _source(source_id, epoch)
    body = dict(schema="SUCC_YEAN_FINITE_INSTANCE_v1", kind=kind,
                source_id=source_id, epoch=epoch, inputs=inputs, outputs=outputs,
                parameter_mapping=mapping, runtime_pins=RUNTIME_PINS.copy(),
                lean_pins=LEAN_PINS.copy(), source_obligations=list(SOURCE_OBLIGATIONS),
                requested_scope="SERIALIZED_MATHEMATICAL_INSTANCE",
                universal_python_correctness=False, physical_source_authenticated=False)
    return dict(body, digest=digest(body))


def affine_packet(word, *, source_id: str, epoch: int) -> dict:
    """One accepted natural word, with all-input Lean semantics after replay."""
    normal = normalize_word(word)
    # Further bound proof-generation cost; this does not alter the source API.
    if len(word) > 24 or max(normal.multiplier, normal.offset).bit_length() > 256:
        raise BridgeError("Bridge proof budget: <=24 steps and <=256-bit normal form")
    return _packet("AFFINE_NAT_WORD", source_id, epoch,
                   {"word": [[k, n] for k, n in word]},
                   {"slope": normal.multiplier, "offset": normal.offset},
                   {"coefficient_type": "Nat", "S": "Step.shift", "V": "Step.scale",
                    "order": "left-to-right chronological", "prime_gate": "Word.PrimeWord",
                    "composition": "compose f g = f after g"})


def retract_packet(fine: int, coarse: int, *, source_id: str, epoch: int) -> dict:
    """Serialize every matrix column of the admitted rational cyclic operators."""
    retract = FiniteQuotientRetract(fine, coarse, source_id, epoch)
    if fine > 8:
        raise BridgeError("Bridge kernel matrix budget: fine<=8")
    basis = lambda n: [tuple(int(i == j) for i in range(n)) for j in range(n)]
    tables = {name: [[str(v) for v in operation(e)] for e in basis(size)]
              for name, operation, size in (
                  ("pull", retract.pullback, coarse),
                  ("average", retract.average, fine),
                  ("project", retract.project, fine))}
    return _packet("CYCLIC_RATIONAL_RETRACT", source_id, epoch,
                   {"fine": fine, "coarse": coarse, "fiber": retract.multiplicity}, tables,
                   {"coefficient_type": "Rat", "chart": "r+n*t", "fine_type": "Fin(k*n)",
                    "measure": "counting", "pull_adjoint": "fiber sum",
                    "average": "fiber sum divided by k", "table_order": "input column then output row",
                    "hypotheses": ["0<n", "1<k"]})


def replay_packet(packet: dict, *, source_id: str, epoch: int) -> dict:
    """Recompute the fixed entire model; hashes alone never authorize a packet."""
    _source(source_id, epoch)
    if type(packet) is not dict or packet.get("source_id") != source_id or packet.get("epoch") != epoch:
        raise BridgeError("Source/epoch mismatch")
    try:
        inputs = packet["inputs"]
        if packet["kind"] == "AFFINE_NAT_WORD":
            fresh = affine_packet([tuple(s) for s in inputs["word"]], source_id=source_id, epoch=epoch)
        elif packet["kind"] == "CYCLIC_RATIONAL_RETRACT":
            fresh = retract_packet(inputs["fine"], inputs["coarse"], source_id=source_id, epoch=epoch)
        else:
            raise BridgeError("Unsupported mathematical instance")
    except (KeyError, TypeError, ValueError) as exc:
        raise BridgeError("Malformed or inadmissible mathematical instance") from exc
    # Canonical bytes also distinguish bool from int, list from arbitrary objects.
    if json.dumps(packet, sort_keys=True) != json.dumps(fresh, sort_keys=True):
        raise BridgeError("Parameter, normalization, obligation or output mismatch")
    return {"audit": "EXACT_INSTANCE_TRANSLATION_REPLAYED", "packet_digest": packet["digest"],
            "kernel_verification_performed": False, "universal_python_correctness": False,
            "retained_source_obligations": list(SOURCE_OBLIGATIONS)}


def _rat(value: str) -> str:
    q = Fraction(value)
    return f"(({q.numerator} : ℚ) / {q.denominator})"


def _table(columns):
    # Finite functions use natural equality, avoiding any caller syntax injection.
    result = "0"
    for j, col in reversed(list(enumerate(columns))):
        for i, entry in reversed(list(enumerate(col))):
            if Fraction(entry):
                result = f"if j.val = {j} ∧ i.val = {i} then {_rat(entry)} else ({result})"
    return result


def lean_source(packet: dict) -> tuple[str, tuple[str, ...]]:
    replay_packet(packet, source_id=packet["source_id"], epoch=packet["epoch"])
    lines = ["import Yean.SUCC.TwoPoint", "import Yean.SUCC.FiniteRetract",
             "import Mathlib.Tactic.FinCases", "namespace Yean.SUCC.RuntimeInstance",
             "set_option maxRecDepth 8192", "set_option maxHeartbeats 2000000"]
    names = []
    if packet["kind"] == "AFFINE_NAT_WORD":
        word = ", ".join(f".{('shift' if k == 'S' else 'scale')} {n}" for k, n in packet["inputs"]["word"])
        a, b = packet["outputs"]["slope"], packet["outputs"]["offset"]
        lines += [f"def word : Word ℕ := [{word}]",
                  f"theorem normalized : Word.normalize word = (⟨{a}, {b}⟩ : Affine ℕ) := by decide",
                  "theorem prime_admission : Word.PrimeWord word := by",
                  "  norm_num [Word.PrimeWord, word] <;> decide",
                  f"theorem all_inputs (x : ℕ) : Word.run word x = {a} * x + {b} := by",
                  "  rw [← Word.normalize_sound, normalized]", "  rfl"]
        names = ["normalized", "prime_admission", "all_inputs"]
    else:
        n, k, m = (packet["inputs"][s] for s in ("coarse", "fiber", "fine"))
        for key, insize, outsize, operation in (
                ("pull", n, m, f"FiniteRetract.cyclicPull (k := {k})"),
                ("average", m, n, f"FiniteRetract.cyclicAverage (n := {n}) (k := {k})"),
                ("project", m, m, f"FiniteRetract.cyclicProject (n := {n}) (k := {k})")):
            lines += [f"def {key}Table (j : Fin {insize}) (i : Fin {outsize}) : ℚ := {_table(packet['outputs'][key])}",
                      f"theorem {key}_columns (j : Fin {insize}) (i : Fin {outsize}) :",
                      f"    {operation} (fun z => if z = j then 1 else 0) i = {key}Table j i := by",
                      "  fin_cases j <;> fin_cases i <;>",
                      f"    norm_num [{key}Table, FiniteRetract.cyclicProject, FiniteRetract.cyclicPull,",
                      "      FiniteRetract.cyclicAverage, FiniteRetract.cyclicPush, FiniteRetract.push,",
                      "      FiniteRetract.cyclicChart, Fin.sum_univ_succ, finProdFinEquiv] <;> decide"]
            names.append(key + "_columns")
        lines += [f"theorem retraction (f : Fin {n} → ℚ) :",
                  f"    FiniteRetract.cyclicAverage (k := {k}) (FiniteRetract.cyclicPull f) = f :=",
                  f"  FiniteRetract.cyclic_average_pull {n} {k} (by decide) f"]
        names.append("retraction")
    lines += ["end Yean.SUCC.RuntimeInstance", "set_option pp.all true", "set_option pp.universes true"]
    full = tuple("Yean.SUCC.RuntimeInstance." + n for n in names)
    for name in full:
        lines += ["#check @" + name, "#print axioms " + name]
    return "\n".join(lines) + "\n", full
