# Reconciliation with the newly available generalized Euler--adelic draft

**Inspected sibling:** [PR #285](https://github.com/femboy2112/SUCC/pull/285),
head `f36ddfba4525fe6800ce8b08cc6598e7edfdb1ad`, parent main
`e648df3e4fca73ab6b942232b5ca4b310e9cac08`.
The PR appeared during the final live check of this research round, after
the original 18-draft reconnaissance. Its paper, source module and ledger
were read at that commit. This addendum preserves the original start-state
record and supplies the updated context without rewriting history.

## What was already present

EAB-01/03/04/05 already supply the generalized regularized $G$, positive cell
tails, a source-labelled Hurwitz mesh, and the infinite Stieltjes hierarchy.
EAB-07/08 give the genuine finite-prime bound and the explicit cofinal clock
$s=1+1/q$, $X=q^{2q}$, with error at most $1/q$.
EAB-09 supplies the balanced two-pole theta completion. EAB-11 already gives
finite-jet nonidentification through changed positive prime exponents.
Those overlapping classical constructions and prior source observations are
not discoveries attributed to this round.

The original sibling sources remain available at their exact commit:

- [Paper dossier](https://github.com/femboy2112/SUCC/blob/f36ddfba4525fe6800ce8b08cc6598e7edfdb1ad/research/2026-10-24/GENERALIZED_EULER_ADELIC_BOUNDARY.md).
- [Implementation](https://github.com/femboy2112/SUCC/blob/f36ddfba4525fe6800ce8b08cc6598e7edfdb1ad/observational_succ/generalized_euler_adelic.py).
- [EAB claims](https://github.com/femboy2112/SUCC/blob/f36ddfba4525fe6800ce8b08cc6598e7edfdb1ad/docs/CLAIM_SUPPLEMENT_GENERALIZED_EULER_ADELIC.md).

## 1. The two Hurwitz normalizations have an explicit conversion

This round fixes a common counterterm:

$$
G(s,q)=\zeta(s,q)-\frac1{s-1},\qquad G(1,q)=-\psi(q).
$$

The sibling's mesh $h>0$ and chart $q>0$ instead use aligned source cells:

$$
E_{q,h}(s)=h^{-s}\left[\zeta(s,q)-\frac{q^{1-s}}{s-1}\right].
$$

The exact conversion is

$$
E_{q,h}(s)=h^{-s}\left[G(s,q)+\frac{1-q^{1-s}}{s-1}\right],
\qquad E_{q,h}(1)=\frac{G(1,q)+\log q}{h}.
$$

At a finite horizon, writing $E_N^{q,h}$ for its aligned-cell cutoff,

$$
E_N^{q,h}(s)=h^{-s}\left[
B_N(s,q)+\int_1^q x^{-s}\,dx-\int_N^{N+q}x^{-s}\,dx\right].
$$

Thus its mesh/refinement law cannot be transferred into our chart with the
counterterm omitted. The difference is explicit and tends to the displayed
conversion in the right half-plane.

## 2. Compare tail bounds on the same finite object

For the positive successor-cell sum $C_N(s)$, EAB proves

$$
0<G(s)-C_N(s)\le\frac1{2N^s},\qquad s>0.
$$

Our finite Mellin value is $F_N(s)=C_N(s)/s$, so this supplies the alternative
tail $1/(2sN^s)$. The implemented elementary envelope is
$1/[s(N+1)^s]$. Either may be smaller: the EAB bound wins when
$(1+1/N)^s<2$. A later integration can use their minimum. They are
alternative bounds on the same tail, not independent errors to add.

The centered-sawtooth observation has a more substantial consequence.
With $B_N^*=B_N-(1/2)N^{-s}$, the bounded periodic primitive
$P_2=(\{x\}^2-\{x\})/2$ gives

$$
B_N^*(s)-G(s)
=s(s+1)\int_N^\infty P_2(x)x^{-s-2}\,dx.
$$

Its bound $|P_2|\le1/8$, followed by the convex logarithm estimate in this
round, yields the stronger all-degree completed-Li approximation

$$
|\lambda_n^{(N,*)}-\lambda_n|
\le\frac{135}{392}n5^{n-1}N^{-7/4}.
$$

See [Corollary 7.1](EULER_MASCHERONI_COMPLETED_LI.md). The centered
Euler--Maclaurin ingredient is classical and the sibling observation is
credited explicitly. This is a quantitative source approximation theorem,
not a sign theorem. It is paper-only in this branch; production functions
and their validated hashes were left fixed.

## 3. Its completed endpoint is exactly the first Li coefficient

Let $\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$ and write the sibling's
balanced function as

$$
B_{\rm EAB}(s)=\Lambda(s)-\frac1{s-1}+\frac1s.
$$

It obeys

$$
2\xi(s)=1+s(s-1)B_{\rm EAB}(s).
$$

Consequently

$$
B_{\rm EAB}(1)=\frac{\xi'(1)}{\xi(1)}=\lambda_1
=1+\frac\gamma2-\log(2\sqrt\pi).
$$

The positive theta integral already proves this first sign. Our rational
certificate is an executable enclosure of that known value, with extension
to the finite completed coefficient map. This $B_{\rm EAB}$ is not the
unregulated BBP function $B_{\rm BBP}$ whose value at zero is $15/8$.

The EAB finite-prime nullspace control is valid in its stated scope. Its
multiplier is an exponential of an analytic function on $\Re s>0$, hence
zero-free there: it changes the prime exponents and preserves a finite
regular jet, but preserves the original zero locations in that half-plane.
Our additive completed-function counterfeit has a different purpose: it
also retains reflection and real-axis normalization while forcing off-line
anchors, and its failure of ordinary Dirichlet-source authenticity is proved
explicitly. Neither is a counterexample to the genuine RH statement.

## 4. Certified prefixes and normality have different quantifiers

EAB's Basel-based rational square-root intervals certify `3.243` at cutoff 50
and `3.243F` at cutoff 300, using the external classical Basel theorem.
They certify digits of the actual number; they do not estimate the frequency
of every block along all large horizons.

This round instead embeds the unchanged BBP source by finite Lerch
partitions and proves a criterion for its selected character sequence.
The four character windows are genuine finite certificates, and their
nonmonotonicity is a genuine negative control. Their vanishing as the
horizon grows remains unproved. Neither construction replaces that limit
with digit computation or a changed-source ensemble.

## 5. A numerical endpoint defect in the sibling implementation

Read-only calibration reproduced `theta_balanced_completed(-2)` raising
`ValueError: gamma function pole`, although its documented entire function
has $B_{\rm EAB}(-2)=B_{\rm EAB}(3)$. Directly multiplying the Gamma pole
and the trivial zeta zero causes this removable numerical problem. The
theta integral or the already-proved reflection $s\mapsto1-s$ supplies a
regular evaluation at this point.

This is a defect in that optional numerical evaluator, not a failure of
EAB's paper theorem. Its source branch is separate and was not modified by
this review. It should be covered by an exact negative-even endpoint
regression when the sibling is integrated. No passing numerical endpoint
claim is inherited here.

## Integration and validation boundary

The sibling was not merged. Its 12 isolated test groups and hosted checks
retain their own scope; our 7,649-test repository run does not certify code
absent from this branch. At the live reconciliation check the sibling's
main full workflows were still running, while its smaller reviewed checks
had completed successfully. The precise observation is retained in
[the reconciliation receipt](euler_mascheroni_validation/pr285_review.json).
No new runtime dependency on the sibling is introduced.
