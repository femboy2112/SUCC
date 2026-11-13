# Quantum Yang–Mills existence × SUCC

**2026-11-13 research round.** Main XXV base:
`db9fb4b84672050efa79b13377f1e73364598a14`.

**Continuation: existing SUCC quantum structures.** The new
[quantum graph/Haar dossier](qm_graph_bridge/README.md) gives a literal unitary
map from the existing successor carrier to central SU(2) characters, a finite
constructive Wilson-state algorithm with proved error, actual typed-source
and measurement graph adapters, source-weighted Haar reconstruction, and the
prime-mode Fock connection. It records 40 additional exact tests and the
remaining finite-lattice/continuum interfaces. The expanded focused set passed
76 tests; the full repository rerun passed 13,126 tests with the project import
path supplied. See the continuation's [validation](qm_graph_bridge/VALIDATION.md).

## Verdict

**The reported breakthrough is real in a precise, substantial sense:** the
Yang–Mills working group's November 10 assessment endorses OpenAI's public
construction of a four-dimensional quantum field theory as a scaling limit
of Wilson lattice gauge theory, in its stated nonabelian compact simple-group
class. Its source, formal checks, independent statement adapters and assessment
are public. **The construction does not prove a mass gap or uniqueness of the
infinite-volume limit.** The full Millennium problem remains open.

This is the current published expert assessment, not a claim that this SUCC
round independently rechecked the complete proof. The committee itself
distinguishes machine verification from its ongoing work to understand the
construction. We inspected the primary definitions and verification records,
replayed artifact integrity, reproduced bounded mathematical ingredients, and
developed a concrete SUCC transfer interface.

Primary sources:

- [OpenAI announcement, October 26](https://openai.com/index/building-scientific-understanding-with-academic-communities/).
- [Committee announcement, November 9](https://www.kitp.ucsb.edu/sites/default/files/3rd-Statement-About-Quantum-YangMills-Theory_Nov-9.pdf).
- [Assessment and checks, pinned revision](https://github.com/yang-mills-group/YM/tree/55ba9fc36293b3f4d52c6b1f813169a0be76ee98).
- [Assessment PDF](https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/docs/assessment-1.pdf).
- [Original submission, pinned revision](https://github.com/yang-mills-group/OpenAI-YM-20261028/tree/3456e5e75cf8d4cd558955a5c7638fba2d68f464).
- [Clay's problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf).

No specific Facebook post was supplied, so this identifies the matching primary
result without claiming to have authenticated that particular post.

## 1. What changed in the external mathematics

The formal input is a closed matrix subgroup of U(m) with nonabelian simple
real Lie algebra. One Wilson lattice family is selected before requested
volume-extraction sequences. Its source-bound correlations have a continuum
limit along the construction's chosen spacing sequence at suitable fixed
physical volumes. An infinite-volume subsequence is then selected. The mixed
limiting hierarchy is decomposed into components, each reconstructed into a
Wightman quantum theory.

The construction is a statement about correlation functions and reconstructed
fields. It does not provide every possible formulation of Yang–Mills theory.
In particular, the assessment leaves a continuum probability measure on a
field configuration space, Wilson-loop construction and an area law as further
questions. Its OPE truncation is by field degree, not an assertion of complete
perturbative loop matching.

Each selected component has its own unique invariant vacuum. That does not
identify different components or limits. A physical mass gap would require a
strictly positive lower bound on nonzero excitation energies, and is absent
from the result.

The independent scalar OS adapter uses the selected centered stress trace and
Schwartz tests flat on coincidence diagonals. It is not an independent
all-field check on unrestricted Euclidean contact terms. The broader source
construction has additional reconstruction/contact results, with their own
stated domains. The audit preserves those distinctions.

See [UPSTREAM_AUDIT.md](UPSTREAM_AUDIT.md) for the complete scope and provenance.

We also traced a native analytic theorem, `YM.FullVolume.genuine`, beyond the
public interface. For each fixed field list, finite difference list and positive
physical separation, it bounds renormalized lattice correlations uniformly in
all volumes and sufficiently fine cutoffs. Its inputs include source-specific
reflection/chessboard estimates, controlled replicated insertion costs, and a
preliminary extracted field table. Convergence still needs a separate Cauchy
input. This is difficult analytic machinery; the finite reproduction below does
not reproduce it. [RG_IMPORT_MAP.md](RG_IMPORT_MAP.md) records the exact types,
dependencies and missing arithmetic adapters.

## 2. How SUCC can use it now

| Opportunity | Concrete result in this round | Remaining obligation |
|---|---|---|
| Use a rigorous nonabelian field-theory carrier | Identified the actual source, observable, limit and reconstruction interfaces | An application must instantiate those interfaces and preserve their domains |
| Reproduce a finite Wilson ingredient | Exact SU(2) Haar moments, positive Wilson approximants, a proved factorial error budget | Four-dimensional renormalization and the volume limit are not reproduced by this slice |
| Translate observer-state reconstruction | Proved the source-preserving GNS isometry and its reflection/dynamics conditions | Construct the actual source/state map, not just matching vocabulary |
| Compare phases without discarding coherence | Reproduced the common-coefficient OPE difference lemma; proved target-reader factorization and its stability bound | Derive a common expansion and quantitative reader for the authentic arithmetic source |
| Improve proof acceptance | Inspected the combined theorem tying every clause to one family, table and final witness | Apply equally strong source/witness binding to future SUCC analytic claims |

The external existence theorem does not by itself settle a SUCC arithmetic
problem. It gives a genuine mathematical object and a source-bound construction
architecture that can guide new work.

## 3. The constructive reproduction: one SU(2) Wilson plaquette

For the holonomy U of one square plaquette, put x=Tr(U)/2. Product Haar
integration reduces its Wilson law to

\[
 d\nu(x)=\frac2\pi\sqrt{1-x^2}\,dx,\qquad
 L_\beta(f)=\frac{\int f(x)e^{\beta x}d\nu(x)}{\int e^{\beta x}d\nu(x)}.
\]

We re-derived

\[
 \int x^{2k}d\nu(x)=\frac{\binom{2k}{k}}{4^k(k+1)},
 \qquad \int x^{2k+1}d\nu(x)=0,
\]

both by beta integration and by an independent moment recurrence. Even Taylor
truncations of the exponential are strictly positive on the whole real line.
They therefore define exact rational positive states for rational beta and
polynomial observables. The proof supplies, for |f|<=M,

\[
 |L_\beta(f)-L_{\beta,K}(f)|
 \le 2M\,3^{2\lceil|\beta|\rceil}
       \frac{|\beta|^{2K+1}}{(2K+1)!}.
\]

This is a genuine reconstruction with a proved approximation limit for its
declared finite source. It is useful for testing SUCC observable-state adapters.
It is not the ultraviolet or infinite-volume limit of four-dimensional QFT.

The calibration includes a sharp failed mutation: replacing the positive even
truncation with the odd weight 1+3x preserves normalization but makes the
square observable (1-x)^2 have expectation -1/4. Thus the instrument can
reject a false positivity claim rather than merely reproduce a positive example.

See [WILSON_REFLECTION_SLICE.md](WILSON_REFLECTION_SLICE.md).

## 4. The most useful bridge: retain invisible coherence, bound visible error

The inspected upstream theorem `YMReview.OPE.phase_difference` uses one
coefficient family for all phases. Subtracting two expansions gives the
difference expansion with twice the remainder. We reproduced that argument.

We then made the SUCC transfer target more precise. Suppose the **same**
source-bound affine relation holds for all candidate state readings x_s:

\[
 x_s=A_r x_s+b_r+R_r(s),\qquad \|R_r(s)\|\le\epsilon_r.
\]

Let L be the observable readout needed by the theorem. If a bounded linear
reader B_r satisfies

\[
 L=B_r(I-A_r),
\]

then

\[
 \boxed{\|L(x_s-x_t)\|\le2\|B_r\|\epsilon_r.}
\]

In finite dimensions such a reader exists exactly when
`ker(I-A_r)` is contained in `ker L`. A persistent coherent direction may
remain if the target is insensitive to it. Even a noncontracting oscillation
can admit a stable reader. Full contraction is a sufficient special case,
not a requirement imposed on normality or gauge equivalence.

The exact solver returns a reader and its norm, or rejects a target-visible
kernel. It distinguishes:

- A=diag(1,1/2), L=(0,1): the first direction persists; B=(0,2) still reads
  the target from the residual.
- The same A with L=(1,0): no such reader exists; the surviving direction
  changes the target.
- A=-I: B=I/2 is valid although A's powers do not decay.
- A_N=1-1/N and residuals +/-1/(2N): errors tend to zero while reader norms
  grow like N, allowing a persistent unit difference.

The criterion is classical linear algebra put into a calibrated proof interface.
It does not prove an arithmetic estimate. For any limit argument, the product
`||B_r|| epsilon_r` must tend to zero, the target identification must be fixed
or transported by a proved map, and the reference value must be identified.
The source OPE alone is not a closed return equation of this form.

See [TRANSFER_THEOREMS.md](TRANSFER_THEOREMS.md).

## 5. What this diagnoses in SUCC's actual frontier

Main XXV authenticates the original four-pole BBP source and literal zero seed.
Sibling [#611](https://github.com/femboy2112/SUCC/pull/611) and
[#612](https://github.com/femboy2112/SUCC/pull/612) show how complete fixed-lag
observables can characterize normality and distinguish lawful gauge changes
from arbitrary samplewise rephasing. The present work preserves that correction:
normality does not require arbitrary moving-lag correlation maxima to vanish.

Applying the new reader to the actual radix-invariance relations diagnoses
their missing information. For an invariant law,

\[
 \widehat\mu(h)=\widehat\mu(16h)=\cdots.
\]

A constant Fourier channel survives those relations and is visible to the
normality target. The invariant atom at zero and Haar measure both satisfy
the relations while taking different values in that channel. The reader
correctly refuses to infer cancellation. Adding a zero boundary condition
makes the finite system solvable, but that boundary estimate is a new
mathematical obligation; it is not supplied by invariance or by a gauge label.

The next worthwhile attack is an actual source-conditioned carry/block
expansion, with common coefficients and boundary terms fixed before looking
at the desired response. It must produce a target reader whose norm times
the proved residual tends to zero, on a complete observable family. It must
also identify the reference law as Haar. This is the exact missing edge;
no new signed saving for the original BBP source was proved here.

The source transport was nevertheless quantified explicitly. If M_(B,h) is
the full-shell signed average of e(h U_n), then for B>=1 and d>=0,

\[
 |M_{B,h}-M_{B,16^dh}|
 \le\frac{2d}{B}+\frac{\pi|h|(1+16^d)}{32B^2}.
\]

This follows from the exact completed radix orbit and the positive four-pole
tail. It transfers an estimate between two readings; it does not establish
the estimate at either end. The proof is YT-08 in the transfer dossier.

[SUCC_CROSSWALK.md](SUCC_CROSSWALK.md) maps the existing holonomy, GNS, TFD,
pinbed and fresh gauge branches at their pinned revisions.

## 6. What was checked, and what was not

The upstream integrity replay checked 9,508 submitted files, 43 review
modules and four normalized whole-declaration OS correspondences. It passed.
This establishes artifact identity/source correspondence, not a new local
Lean proof replay. The exact receipt and a reading manifest covering 24 core
files plus 14 native RG files are preserved.

The initial round's two focused suites contain 36 exact finite tests. The Wilson and
phase-transfer probes include positive, negative, singular/null and mutation
controls. The local report records these and the required SUCC gates separately
from upstream historical kernel results.

All 36 initial tests and the provenance, foundations and ordinal gates passed.
The initial complete repository suite ran 13,086 tests with one subprocess import
error, reproduced on unchanged main. All 11 tests in the affected suite passed
when the project import path was supplied. The full raw run remains recorded
as an error; the diagnosis and unmodified logs are included in the local report.
The quantum/Haar continuation subsequently reran the full suite with that
precondition satisfied: **13,126 tests passed**, including the 40 additions.

- [Local validation and command scope](LOCAL_VALIDATION.md)
- [Exact finite probe receipt](probe_receipt.json)
- [Upstream reading/hashing manifest: 24 core files and 14 native RG files](upstream_manifest.json)
- [Unmodified fresh upstream integrity receipt](upstream_integrity_receipt.json)
- [Claim ledger](CLAIM_LEDGER.md)
- [Hole contract](HOLE_CONTRACT.md)

From the SUCC repository root:

```sh
python -m unittest discover -s tests -p 'test_ym_*.py' -v
python scripts/yang_mills_succ_probe.py
```

The test pattern now selects all Yang–Mills suites, including the continuation.
These finite probes accompany the
paper proofs; they do not execute a continuum infinity.

For a full upstream replay, use its exact pinned toolchains and runner as
documented in [UPSTREAM_AUDIT.md](UPSTREAM_AUDIT.md). The published reference
build used about 52 GiB for its source/dependency/build tree and about three
hours on the recorded machine, with additional verification tools. That
resource report is not a prediction for another machine. This round did not
perform the full Lean build or Comparator replay.

## 7. Research decision

Use the result as an externally constructed QFT carrier, a precise source-bound
reconstruction blueprint, and a source of explicit comparison lemmas. Continue
with target-sensitive observable readers instead of demanding decay in every
coordinate. The next promotion requires an actual arithmetic operator and
residual estimate, or a separately executed full upstream formal replay.

**π normality, RH, Goldbach, and the Yang–Mills mass gap remain OPEN in SUCC.**
The push is an additive research dossier and reproducible mathematical slice,
not a claim to have solved those problems or independently reproduced the
complete four-dimensional existence proof.
