# Prospective prime-epoch checks

Root proposed the aligned clean prime epoch and elementary order-count/Bourgain–
Konyagin route after the earlier finite-adic shadow receipts. The following rows
are fixed before running the new source/cycle/covariance oracle.

Exact clean-epoch holdout primes: 577,641,881,1201,1601. All are to be checked
for primality, class1 mod8, predicted birth/next pole, and exact principal-part
cycle counts. The p=641 row deliberately has sqrt(p)/ord(16)>1; a Gauss bound
alone must not be mislabeled a saving. No finite test certifies BK's asymptotics.

Dense good-prime selector controls: A=37,73,137,257,521. Compute the largest
p<=4A in class1 mod8 with ord_p(16)^3>p, exactly; check source correspondence,
interval overlap and total-variation gluing weights by explicit interval sums.

Aligned hostile covariance controls: p=137,281,521, A=(p-1)/4+1,
L=(p-1)/4, J=3,K=9,eta=1/2^20. Apply AR1 with P=(3,5,7,p). Preserve every
p-principal part but certify Re(W)>near1 and
Re(Cov)>=the rational AR1 lower bound-ceil(sqrt(p))/ord_p(16).
These are signed lower certificates, not complex floating-point observations.

Rejected cases: composite/class-mismatched primes, counting h divisible byp as
an oscillatory character, silently dropping the endpoint shift, and using the
finite Gauss bound as a uniform BK certificate.
