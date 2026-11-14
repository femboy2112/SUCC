# Kernel replay and labelled descent

Lean 4.14.0 compiled Fable’s 753-line weighted ancestral source. Its verifier
reproduced the archived 18-export receipt byte for byte, including successful
positive controls and rejected negative controls for both the selected-source
ghost and may/must distinction. The fresh receipt SHA-256 is
`855999980febd68bf0fdd36d0c31acf4bebd50341ffb052a461ea56aa46e0b3c`.

The larger audit queried every explicitly named top-level structure,
inductive type, definition and theorem in the actual three source modules.
For Fable this covers 63 names, including all 45 named theorems. All 63
returned an empty axiom dependency list. The word “axioms” here describes
Lean’s transitive declaration dependencies. The theorem types explicitly
take the operations and laws of a `LaxQuantale` as hypotheses. Generated
recursors and structure projections were not counted as additional named
source declarations.

| Module | Named declarations queried | Results of `#print axioms` |
|---|---:|---|
| Fable’s `ObservatorisQuantale` | 63 | All empty |
| SUCC’s inherited `FutureSafeForgetting` | 13 | `finite_trace_preserved`, `availability_reflected` and `quotient_path_lifts_from_each_representative` use `propext`. The other ten lists are empty. |
| `ObserverBridge` | 6 | `endpointExact_and_wordLift` inherits `propext` from the whole-word lift. All five other lists are empty. |

Read the exact types, axiom lists and compiler diagnostics in
[compiler.log](compiler.log). The machine-readable source hashes and per-name
dependencies are in [audit.json](audit.json). The inherited verifier’s complete
replay is [fable_kernel.json](fable_kernel.json).

## What the bridge proves

Take any SUCC partial deterministic source and quotient systems with an actual
`FutureSafeForgetting.Descends` witness. Choose any predicate on action/cost
pairs. Forget the labels of legal edges satisfying that predicate to obtain a
Boolean relation on source states. Then the existential quotient of that
relation is exact at every selected start in Fable’s `propQ` sense.

The proof passes through the two actual Lean modules. Given a source edge
and a second state in its source-report fibre, the descent square projects
that edge to the target system. The inherited one-step lifting theorem lifts
the same action and cost at the second state. The edge filter accepts that
lift. Fable’s `star_propQ_iff` turns the one-step path into a Boolean closure
witness. Fable’s `exact_iff_edgeRealised` then gives all-start endpoint
exactness. This construction permits filters such as “cost ≤ B and action
belongs to menu M” whenever those predicates have been supplied. The
endpoint theorem applies to the filtered unlabelled relation. The stronger
ordered-word and ordered-cost conclusion uses SUCC’s labelled descent law
directly. Its proof retains the standard Lean axiom `propext`.

There is a separate axiom-free answer to the handoff’s question about unit
laws. Use predicates on `Bool` ordered by inclusion, pointwise union for all
suprema, and the constantly true predicate for the designated unit. Define
the product by $(P\otimes Q)(i)=P(i)\land(\exists j, Q(j))$. Lean checks all
fields of Fable’s `LaxQuantale`. For $Q=\{\mathrm{true}\}$ the product
$1\otimes Q$ is the entire Boolean set, and its inclusion into $Q$ fails
at `false`. Thus the stated Fable instance requires both right-unit
inequalities and only the left-unit inequality $Q\le1\otimes Q$. A
two-sided left identity is a genuinely stronger requirement even after
quotienting predicates by mutual inclusion. An explicit proof of the
missing inequality’s negation compiled. Replacing the negated statement
by the positive one rejected the same proof with a type mismatch. See
[ObserverBridge.lean](ObserverBridge.lean).

For the arbitrary preorder the handoff’s displayed equality between
endpoint values denotes two inequalities. Literal equality additionally
requires antisymmetry or passage to the preorder quotient. Its idempotence
conclusion has the same interpretation. The supremum operation is
idempotent up to that equivalence. Multiplication itself may retain path
order, as it does for languages of action words.

The replay certifies the encoded theorems and their explicit hypotheses.
Single-copy experiment availability, physical source adequacy, Fable’s
other paper theorems, arithmetic cancellation and the external historical
independence of the two research runs need their own evidence.

## Reproduce

The source modules were checked from the integration tree rooted at
`670919f53322246936393b2f994d54957fe41057` with Fable parent
`5b7470c677135600c39f817064695308b86756f9` and Astra parent
`f9efa624da06a28e1a8ac99a56499acd11197928`. The source hashes in
`audit.json` bind the local execution exactly. The original Fable module
is byte-identical to its integrated copy.

The compiler came from the official
[Lean v4.14.0 Linux release](https://github.com/leanprover/lean4/releases/download/v4.14.0/lean-4.14.0-linux.tar.zst).
The archive’s SHA-256,
`320f18e7d58271d95fced740522b5a5ed41b85b2af5bf0e8ab9a8dbc380e450a`,
matched the value already pinned in the repository’s
[Duck π workflow](../../../../.github/workflows/duck-pi-proof.yml).
The executable reported Lean compiler commit `410fab728470`.

From the repository root, with this compiler on PATH, run

~~~sh
python research/2026-11-14/tenacious_d/lean/replay.py --lean lean --out /tmp/tenacious-lean-replay
diff -u research/2026-11-14/tenacious_d/lean/audit.json /tmp/tenacious-lean-replay/audit.json
diff -u research/2026-11-14/tenacious_d/lean/compiler.log /tmp/tenacious-lean-replay/compiler.log
~~~

The replay compiles each imported source to fresh temporary objects. Its
negative control requires a type error and its positive counterpart must
compile silently. During development, Lean rejected an import placed
after a module docstring and caught an omitted explicit predicate argument
in the supremum proof. Both source errors were corrected before the
recorded run.
