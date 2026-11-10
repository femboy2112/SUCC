# Publication fetch: balanced three-channel epoch

Fetched main remains `43a607818907120d4cdab73d240f5b4d7700b63f`.
New read-only branch `research/three-channel-balanced-epoch-2026-11-08` is
pinned at `90711d2e9dc73020acbc4cde1ad058b62ef54a4d`, draft PR554.
Its actual `BALANCED_EPOCH.md`, claim ledger, `balanced_prime_clock.py` and
`test_balanced_prime_clock.py` were inspected. No merge or source import.
Branch tests were read, not executed here. This is a scoped mathematical audit,
not blanket certification of its imports or implementation.

## Useful connection

BEC-01 observes that a p~4A clock misses the channel4/channel5 split during
the actual epoch, making its three-channel Gram singular. This does not
invalidate PR544's scalar clock or claim that scalar cancellation was proved.
The balanced p~(12/5)A clock crosses all four stages in macroscopic proportions
(1/5,3/10,3/10,1/5). Its incomplete-period Gauss completion correctly retains
both the complete-cycle mean and a square-root/log remainder. This supplies
local marginal information for a different, properly time-labelled observer.

It does not bound the real complement or the new integer-lift innovation.
The latter depends on C_n=floor(U_n) and the next literal carry, not merely
on the three p-primary phase coordinates. BEC-08's p-invisible source controls
remain a useful audit of any proposed map between these two observations.

## Two precise proof qualifications at this pin

1. The BEC-05 Gram formula with limiting smallest eigenvalue1/2 requires
   **p not dividing h**. Its general Fourier/resonance formula already handles
   arbitrary h, but this specialized Gram sentence must retain the hypothesis.
   For h=0, or h=p, every channel phase is1 and the Gram is the all-ones matrix,
   with eigenvalues3,0,0. This is an exact counterexample to the unrestricted
   Gram statement. Fixed nonzero h satisfies the needed condition eventually.

2. BEC-08 defines

       B_A=2^-80 + 16^-10/[15(2A+11)^2] + 1/[15(A+1)^2]

   and asserts B_A->0. The displayed bound actually tends to2^-80. This is a
   gap in the claimed *uniform* vanishing estimate; the intended Weyl-mean
   conclusion is repairable without changing the dyadic seeds.

   Write alpha_N=sum_(j<=N)16^-j r(j), N=2A+10, and
   s_A=-floor(2^(8A+80) alpha_N)/2^(8A+80). The original Green identity and
   the existing tail bound give

       |U_n(s_A)| <= 16^n 2^(-8A-80)
           +16^(n-N)/[15(N+1)^2]+1/[15(n+1)^2].

   Sum this inequality over n=A,...,2A-1 **before** taking its maximum.
   Since sum 16^n <16^(2A)/15,

   \[
   {1\over A}\sum_{n=A}^{2A-1}|U_n(s_A)|
   \le {2^{-80}\over15A}
     +{16^{-10}\over225A(2A+11)^2}
     +{1\over15(A+1)^2}\longrightarrow0.
   \]

   Therefore |W_A(h;s_A)-1| is at most2 pi |h| times this vanishing bound.
   The construction's actual intended hostile Weyl conclusion survives with
   an averaged proof. If uniform-in-n convergence is desired instead, let
   the additional rounding-bit margin tend to infinity with A. Neither repair
   turns these horizon-dependent nonzero seeds into the authentic zero source.

These are read-only integration notes. The complete inequality above is the
reviewable proposed repair; the sibling branch was not edited. The claim that
the displayed B_A tends to zero is refuted by its explicit constant term,
not by an experiment on pi digits.

Pi base16 normality: OPEN. RH: OPEN.
