# Exact Gauss-unit probes: declarations before execution

Parent: PR400, `2b0628f52e9d88993c2e3ffa30b9748adfb781f0`.
The code and tests in this directory are not yet executed at this declaration.

1. **GG-01 candidate.** For an odd prime, q=p^ord_8(p), a primitive
   g in F_q and chi(g)=zeta_8^(-1), set
   G_d=sum_(x!=0) chi(x)^d zeta_p^Tr(x). Claim
   G_1 G_5 G_6 / G_4^3 = chi(2)^2, hence for every even integer t the
   full weighted product for c+t(1,-3,1,1) equals that for c=(4,-2,-1,-1).
   Predict exact agreement for positive t=2^(k+2) controls at every odd
   prime, despite the actual p13 birth distinguishing these sources.
   PASS: a quadratic Davenport-Hasse proof with all normalizations checked
   and direct exact finite-field identities. FAIL: any nonzero coefficient
   in the exact difference. No finite sample promotes the universal claim.
2. **GG-02 candidate.** The complete unit in Gross-Koblitz is
   product_(d,i) Gamma_p(<p^i d/8>)^c_d. Compute it modulo p^3, not just
   its valuation, and check its appropriate power against the exact
   cyclotomic Gauss product under a declared p-adic embedding. The root
   normalization is supplied by the classical GK formula, not guessed
   from a complex branch. A power check alone is insufficient to certify
   the root choice independently.
3. **GG-03 candidate.** Algebraic expressions over Q in these fixed-p
   Gauss sums lie in Q(zeta_(8p)); any exact cofiber whose root-of-unity
   order contains an odd prime ell!=p cannot equal such an expression.
   PASS: a ramification or elementary cyclotomic field proof and exact
   original-zero-seed witnesses. This refutes direct identities only;
   embeddings, analytic maps, extra conductor fields and approximate
   estimates are not ruled out.
4. Discovery primes: 13,19,73. Fresh calibration primes: 17,29,43,47;
   optional extra 7,23,31,41,53,59,71,89. Every residue class mod8 must
   occur. Two separate field-enumeration routes and independent Morita
   factorial/block calculations must agree. Original p19 disappearances
   and p73,k4 cancellation must be reproduced by rational arithmetic.

The aim is an actual signed-phase bridge. A universal source-identification
obstruction is a useful failure of a proposed bridge, not a normality
theorem or a nonnormality claim for the positive mutants.
