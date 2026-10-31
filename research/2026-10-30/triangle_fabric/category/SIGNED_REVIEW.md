# Complementary signed-front review

Reviewed `../signed/SIGNED_FABRIC.md` at SHA256
`abc117a4dbfc2b9b95af87f0d8a3a58abc109354ebbdedd8c23b8bf6dfdf6167`.
This is another same-model agent, not an independent external referee.

No substantive error found in SF-01–04.

* SF-01: checked source indexing, the identity
  U_n^F=F(16)U_n+16^n q_0−q_n, and the rational period moduloQ. The converse
  coboundary implication uses a rational initial value and decay; those
  hypotheses are stated. Injectivity follows from the full-support moment
  measure. The quotient classification is not normality proof.
* SF-02/03: checked positive definiteness, the sign-changing-root proof,
  the uniform15^(−N−M) product bound, exact prefix matching, first omitted
  residual, jet orders and minimal degree. The minimality is explicitly
  restricted to polynomial shift filters.
* SF-04: checked the sign in the resolvent error, dyadic convex mixing,
  zero-seed tail identity and coherence onset. The series constants in
  inequalities15/16 follow from integrating at A−1 and π<4.
* The finite-data obstruction preserves positivity, arbitrary finite source
  prefix, finite kernel jets, and zero seed. It does not retain the exact
  original four-pole source at every index, which remains the crucial type
  boundary. Rational-affine normality is classical input, not newly proved.

Fresh checks executed by `review_signed.py`, without importing the signed
implementation: SymPy matrix inversion plus polynomial division at
(N,M)=(2,5),(4,3),(6,2),(9,4); all minimal degrees, positive Gram determinants,
exact prefix/jet constraints and20 telescoping values passed. Rational Machin
intervals (240 arctangent terms at1/5,80 at1/239) fit inside the norm-based
error enclosure for all four cases. This rotates the π-calibration route
away from the signed front's BBP interval.

Two additional dyadic mixtures (N,M)=(3,4),(6,2) passed exact rational boundary,
integer radix onset and positive-tail checks. Their denominator exponents
are57 and81, giving onset16 and22. The full exact values, hashes and raw
command output are in `receipts/signed-review.json` and
`receipts/signed-review-run.{json,log}`.

The mathematical derivations remain paper proofs. These extra finite checks
are implementation validation, not a proof of their unrestricted quantifiers.

Post-review clarification checked: the signed dossier explicitly restricts
complete monotonicity to the real clock a=8n−7>0. Its revised SHA256 is
`4f90a1d0f62f553c95549416580899ddd8324c58a05fc0d8d8e723b6eb932b9d`.
This narrows wording without changing the formulas or the checks above; the
raw execution receipt correctly retains the earlier hash.
