# Quantitative selector protocol (before implementation/measurement)

Parent source/research1990b051; new selection changes only the observer's
prime, never the BBP source. Let b(p)=bit_length(p), and fix integer C>=1.
Choose largest p<=4A, p=1mod8, with m=ord_p16, m^3>p and m^2 b(p)^(2C)>p.
Candidate theorem: for any fixed0<B<2C, 4A-p=O(A/log^B A), proved by the
finite product order sieve and quantitative fixed-modulus PNT/AP.
Cochrane--Pinner Theorem1.1 supplies the exact uniform local bound delta^8
<=min(1,p^4/m^8,(256/9)p^2/m^5,(256/9)p/m^3), with no fitted exponent.
New asymptotic consequences are derived on paper, never inferred from tests.

Exact finite grid: C=1,2,3; all integer A=5,...,300 compare selector against
an independent sieve/direct-multiplication order algorithm. Prime/cube
checks use p=17,41,73,89,97,137,193,233,281,353,617,769,1009,1217 and every
nonzero coefficient (one representative per subgroup coset is sufficient,
but multiplicative invariance must be checked exactly). Outward interval
averages raised to the eighth power must not contradict the analytic cap.
The finite order sieve: X=64,128,256,512,1024,2048, Y=1,2,3,5,8,13,21;
verify every odd prime <=X of order<=Y divides product_(j<=Y)(16^j-1).
Derive the counting inequality analytically; do not fit its asymptotics.

Audit exact source local phases and the gluing formula on A=97,307,613,1229
for C=2. Reuse previous source receipts only if the selectors coincide;
otherwise compute literal rational source states. This is observer selection
and algebraic verification, not a new independent source dataset.
Retain all failures, code hashes and thresholds. No effective starting epoch
for the PNT asymptotic is claimed. Pi base16 normality OPEN; RH OPEN.
