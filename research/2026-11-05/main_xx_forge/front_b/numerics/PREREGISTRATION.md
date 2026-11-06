# PREREGISTRATION - Front B carry-transport probe (written BEFORE any computation)

Author of instrument: Daniel Bernoulli (experimentalist). Date: 2026-11-05.
Scratch directory only. No git. Python = scratchpad venv (mpmath 1.3.0, pure-python backend, numpy 2.5.4, sympy 1.14.0). Every mpmath use is inside a local `mp.workdps(...)`.

Source (immutable): r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2), U_0=0, U_n=16U_{n-1}+r(n), x_n={U_n}. Seed s: U_n(s)=U_n(0)+16^n s.
S_k(n)=sum_{j=1..k}16^{k-j} r(n+j). T_n=sum_{j>=1}16^{-j} r(n+j).
Repo definitions (HS-01/HS-08): d=m+k; theta={16^d x_n}; delta={16^m S_k(n)}; b=1[theta+delta>=1]; J_{A,m,k}(s)=(1/A) sum_{n=A}^{2A-1}(b-delta).
ADMISSIBLE(A,m,k): S_d(n)<1 for every n in [A,2A).

## What is being tested (orchestrator's claims, unverified)
- CB-1 (rational form): if S_d(n)<1 then b = 1[ S_m(n+k) <= x_{n+d} < S_d(n) ] and delta = S_d(n)-S_m(n+k).
- CB-1g (gauge form): alpha=s+pi/16, z_j={16^j alpha}; b = 1[16^m T_{n+k} <= z_{n+d} < 16^d T_n], delta = 16^d T_n - 16^m T_{n+k}.
- CB-3 (countermodel): non-normal alpha with J_{A,m,k}->0 over all admissible triples.

## Exp 0/1 - calibration (must pass before anything enters the record)
r(1)=47/15 exactly; r(n)>0 for n<=10^5 (plus the 3-line analytic argument); U_n/16^n vs pi/16 and U_n+T_n = 16^{n-1} pi (rigorous interval for T_n, pi only as external reference); 64 n^2 T_n -> 1; 16T_n - T_{n+1} = r(n+1) inside the rigorous interval; small hand-checkable case (A=2, m=k=1) computed by hand-in-Fractions and by both oracles; mutation sensitivity of the detector (negated forcing MUST show mismatches).

## Exp 2 - CB-1 exact check (two independent implementations)
Oracle A: Python Fractions, repo definitions (theta via 16^d x_n mod 1, delta via 16^m S_k(n) mod 1), x_n by Fraction recurrence; claim side from Fraction S_d, S_m, x_{n+d}.
Oracle B (oracle_b.py): pure big-integer arithmetic over a common denominator D=lcm(all pole denominators, seed denominator), numerators N_n=16N_{n-1}+R_n, repo definition by integer mod, claim by integer interval test. No Fraction objects.
Epochs A in {64, 173, 347, 691, 1024, 4096}; every n in [A,2A); every (m,k) with m,k>=1, d=m+k from 2 up to dmax(A) (largest d with S_d(n)<1 for all n in window) PLUS the first inadmissible d=dmax+1 as a boundary control (reported separately, mismatches there are NOT a falsification, but are reported exactly and classified by sign/size of S_m, S_d).
Seeds: s in {0, 1/5, 1/3, 3/7, 5/17} (rational, exact); coherent s*=-pi/16 and irrational seeds via the gauge route in Exp 3/4.
FALSIFIER of CB-1: any single (n,m,k,seed) with S_d(n)<1 where claimed b or claimed delta differs from the repo-definition b or delta, in EITHER oracle, or any cross-oracle disagreement. (Mechanical derivation expected: the identity should hold for any seed and any forcing with 0<=S_m, S_d<1; this is a prediction, not a proof by this instrument.)
Boundary: also report the n in each window with S_d(n) closest below 1 (minimum margin 1-S_d) and confirm the identity there.
Mutants (same two oracles): M1 first pole 4->5 (positive forcing); M2 constant forcing r=1/1000 ("unforced plus constant"); M3 unforced r=0 (degenerate, empty interval); M4 NEGATED forcing r->-r (detector control: mismatches EXPECTED, positivity violated); M5 sign-alternating forcing (-1)^n r(n) (positivity of S_m, not of r, is what matters). Epochs for mutants: A in {64,173,347,691,1024} (4096 if time). Prediction: M1,M2,M3 -> 0 mismatches (CB-1 generic for positive forcing); M4,M5 -> mismatches>0 only where S_m<0 or S_d outside [0,1) fails. Mismatches are classified.

## Exp 3 - CB-1g gauge check
T_n rigorous from rationals only: backward recurrence T_n=(T_{n+1}+r(n+1))/16 in fixed point 2^400 with outward rounding from the bracket [0,1/10] at N0=nmax+120. z_{n+d} computed (i) from mpmath pi hex digits (labelled GAUGE VERIFICATION ONLY; independent integer Chudnovsky for >= 2^13 digits as second route), (ii) from x_{n+d}+T_{n+d} mod 1 using the exact oracle-B x. Membership vs the exact b; minimum endpoint margin; max |z(i)-z(ii)| in bits. Seeds: s=0 (alpha=pi/16) for all six epochs, all admissible triples. Also check separately whether 16^d T_n >= 1 can occur inside an admissible triple (wrap risk for CB-1g; exposure is noted explicitly since S_d<1 does not imply 16^d T_n<1).
FALSIFIER of CB-1g: any membership/b mismatch, or any delta mismatch beyond the rigorous interval width, in an admissible triple. A wrap case (16^dT_n>=1 with S_d<1) with mismatch is a finding that restricts the claim.

## Exp 4 - exact J values
s=0: exact J_{A,m,k}(0) (Fractions via oracle B integers; printed decimal with exact sign) for the six epochs, all admissible triples. Coherent s*=-pi/16: b===0 and J=-avg delta (verified by repo definition at high-precision mp for A in {64,173,347,691}, and by the rigorous-T route for all epochs). Rational seed s=1/5 (16=1 mod 5, orbit rotation): J reported. No prediction other than that J(1/5) need not equal J(0).

## Exp 5 - CB-3 countermodel
Construction exactly as specified by orchestrator: tau_j=16^{floor(log16(64j^2))}/(64j^2); p(tau)=uniform off [0.3,0.7]; inside: u+delta*phi(tau)*w_perp + c*g (delta=0.02, phi a C-infinity bump supported on [0.3,0.7] with max 1, w=e_1-e_2 with the component along the gradient g=dF/dp projected out inside the 14-dim subspace {dp_0=0, sum dp=0}, then 1-D Newton/root in c so F_{p(tau)}(tau)=tau). Fine grid construction at mp 60 dps (residual target <=1e-30); production laws p(tau_j) for all j<=2^18 by vectorised float64 Newton (residual reported, cross-checked to the mp solver on a grid and on random tau_j).
Digits: numpy default_rng, seeds 20261105, 1, 2 (preregistered), plus supplementary seeds 3..12 (labelled supplementary) for slope/null-sd statistics. Sweep A=2^10..2^17 (to 2^15 if runtime forces; stated). For every A: all admissible (m,k): empirical J (gauge form, rigorous T, exact fallback for ambiguous float comparisons), max_triples |J|, plus the EXACT expectation of J under the CB-3 measure (digit-product measure with position-dependent laws; deterministic bias, no sampling noise). Fit log|J| vs log A slope (max-over-triples and RMS-over-seeds).
Witnesses (prefix [1,N), N=2A): single-digit frequencies, freq(1)-freq(2), max_a|freq_a-1/16|, sum_a freq(aa)-1/16 (adjacent equal pairs), each both empirical and exact-expected. Comparators: true pi digits (same gauge machinery; digits of pi up to as many as runtime permits) and iid-uniform digits.
Expectation to test: |J|~A^{-1/2} (slope about -0.5), witnesses bounded away from 0. FALSIFIED-AS-STATED if slope clearly not negative, or if exact-expected bias does not tend to 0, or if the witnesses can be driven to 0 along the sweep (liminf over A is reported).

## Exp 6 - second-order selected carry statistic
J2_{A,l}=(1/A) sum_n [b_n b_{n+l} - Leb(I_n cap T^{-l} I_{n+l})], I_n=[16^m T_{n+k},16^d T_n), T(z)={16z}, l in {1,2,3}. Representative triple per A: (m,k)=(1,dmax-1) and also the balanced split; closed-form Leb via the counting function (cell structure). Computed for true seed (pi digits), CB-3 (3 preregistered seeds + supplementary), iid-uniform digits (null), and coherent (b===0 so J2=-avg Leb). Also the exact CB-3 expectation of J2 (inclusion-exclusion over the joint CDF). Question answered with data: ratio of exact expected J2 bias to the null sampling sd, versus the same ratio for first-order J.

## Does-not-cover (declared in advance)
No proof; all agreement is evidence with stated case counts. No statement about pi normality. CB-3 sweeps are finite (A<=2^17), digit laws are not shown to be extendable to a proof of J->0 beyond the measured bias and sd.
