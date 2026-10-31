# A finite prefix can match every band and still have maximal band growth

Status: **PROVED LOCAL**, using A03 in
[the analytic dossier](analytic/ANALYTIC_TRANSPORT.md). This is a sharpened
application of the positive rational-boundary countermodels, not a new
obstruction to the authentic source itself. It changes the source after the
specified prefix, keeps the exact zero seed, and does not claim to match the
completed real states on that prefix.

## Declaration before the additional probe

For each integer d>=1, take the d-atom Gaussian source from A03. Predict:

* PASS: its rational recurrence matches the authentic U_n for 0<=n<=2d;
  all finite-band energies of those rational states therefore match exactly,
  simultaneously for every integer H>=1.
* PASS: its rational boundary alpha_d=P/D in lowest terms, positive future
  tail and finite tail budget imply F_(H_N,N) grows proportionally to H_N
  for every H_N tending to infinity with H_N=o(N).
* FAIL: a disagreement in the matched prefix, a failed tail identity, or a
  mistaken transfer of the statement to completed digits or to the original
  four-pole law at every time.
* AMBIGUOUS: any finite sample which has not reached the denominator-dependent
  asymptotic range. A large denominator is not evidence against the theorem.

Probe degrees are 1,2,3,5,8, with degree8 held out from the smaller cases.
Verify 40 further rational source terms at each degree, the exact tail budget
and the fixed-frequency coherence budget. The proof, rather than a finite
fit, supplies the all-horizon conclusion. Rational prime-frame observations
and high source derivatives are not asserted to match those of the original.

## F1. All bands agree on the declared finite rational-state prefix

Write r_d(n)=sum_i w_i x_i^(n-1), with 0<x_i<1 and w_i>0, for the Gaussian
source. A03 proves r_d(n)=r(n) for 1<=n<=2d, and proves all r_d(n) rational
by the orthogonal-polynomial recurrence. The recurrence with U_0=0 therefore
gives U_n^(d)=U_n for 0<=n<=2d. For every integer N in [1,2d] and every H>=1,

    F_(H,N)(U^(d)) = F_(H,N)(U).

This is identity of the actual finite exponential sums, not an approximation
or equality of prime marginals. The completed y_n differ because they include
different future tails. Exact agreement of the finite rational states must
not be silently relabeled as exact agreement of completed digit cylinders.

## F2. Every fixed Gaussian shadow fails the moving-band certificate

Fix d. A03 gives a rational completed boundary alpha_d=R_d(16)=P/D and

    U_n^(d)+T_n^(d)=16^n P/D,
    B_d=sum_(n>=1) T_n^(d)=[R_d(1)-16R_d(16)]/15 < infinity.

Let y_n be the completed states modulo one. They lie in the D-point grid.
The Fejer kernel K_H is nonnegative and K_H(0)=H. If c_j counts these N
states in grid cell j, the two-time formula gives

    F_(H,N)(y) >= H sum_j c_j^2/N^2 >= H/D.

No period completion, residue equidistribution or lower bound on the order
of 16 modulo D is used. The Hilbert feature map from PR415 has Lipschitz
constant L_H=2pi sqrt(H(H^2-1)/6). Applying its triangle inequality to the
actual tails gives

    sqrt(F_(H,N)(U^(d)))
      >= sqrt(H/D) - 2pi B_d sqrt(H(H^2-1)/6)/N.       (F2)

Use zero as a lower bound if the displayed right side is negative. For
H_N tending to infinity with H_N=o(N), its error divided by sqrt(H_N)
tends to zero. Thus eventually

    H_N/(4D) <= F_(H_N,N)(U^(d)) <= H_N,
    log F_(H_N,N)(U^(d))/log H_N -> 1.

In particular the subexponential-in-depth criterion with
H_N=16^floor(log_16(N)/3)/2 fails. For this control,
log F_(H_N,N)/floor(log_16(N)/3) tends to log16, not zero.
The threshold may be extremely large and depends on d; d is fixed before
N tends to infinity. Interchanging those quantifiers would invalidate the
argument.

For completeness, h=D makes e(h16^nP/D)=1 at every n, and

    |sum_(n=1)^N e(D U_n^(d))-N| <= 2pi D B_d.

Hence the exact prefix match coexists with fixed-frequency coherence. This
does not contradict pi normality: the shadow has a different infinite source.

## What has been ruled out

For any prescribed finite prefix length, there is a positive, completely
monotone, rational-valued zero-seed source with exactly the same rational
states and all their finite-band energies, yet with the opposite asymptotic
band verdict. No rule based only on such a prefix can certify the missing
asymptotic property uniformly over that source class. A theorem using the
entire authentic four-pole law remains possible and is the required target.

The source-moment identity, nonnegative Fejer kernel, and Hilbert transport
are shared premises. The new probe is a cross-front integration check, not
an independent mathematical authority or a second proof of normality.
