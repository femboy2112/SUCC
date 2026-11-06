# AV-07: a source-specific *linear* upper ceiling on the finite escape depth

**Research continuation, 2026-11-04; paper proof / exact finite tests.** This sharpens the purely finite AV-04 release statement. It remains far too weak for base-16 normality.

Let \(M_A=\mathrm{lcm}(1,2,\dots,16A)\), \(D_A=\mathrm{lcm}\{\mathrm{den}(\{U_n\}):A\le n<2A\}\), and \(q\ge2\) an integer. Then for **every** integer \(A\ge2\),
\[
\boxed{D_A\mid 15 M_A.}\tag{AV-10}
\]
Hence the exact residual tent at width \(16^Lq\) is supported only on **exactly coinciding pairs** once
\[
\boxed{L\ge\left\lceil\max\left(0,\log_{16}(15M_A/q)\right)\right\rceil.}\tag{AV-11}
\]
This is an explicit source-derived finite cutoff, not an estimate of how much pair energy persists before that cutoff.

### Proof of the denominator envelope

The original source collapses to
\[
r(n)=\frac{120n^2-89n+16}{a_n b_n c_n d_n},\quad
(a_n,b_n,c_n,d_n)=(2n-1,4n-1,8n-7,8n-3).
\]
All four factors are odd and at most \(16A\) for \(1\le n<2A\). The only possible pairwise common prime factors obey:
\[
\gcd(a_n,c_n)\mid3,\qquad
\gcd(b_n,c_n)\mid5.
\]
Every other pair among \(a_n,b_n,c_n,d_n\) is coprime: subtract the appropriate integer multiple to obtain 1, or 4 for the two odd \(8n\) factors. Thus for every prime \(p>5\), the \(p\)-adic exponent in \(a_nb_nc_nd_n\) is the exponent in a *single* one of these four factors, hence at most \(v_p(M_A)\). For \(p=3,5\), at most two factors contribute and their minimum exponent is at most one; the sum is therefore at most \(v_p(M_A)+1\). Consequently \(a_nb_nc_nd_n\mid15M_A\), and so does the reduced denominator of \(r(n)\).

Starting from \(U_0=0\), multiplication by the integer 16 and addition of rationals whose denominators divide \(15M_A\) preserve that denominator divisibility through every \(U_n\) with \(n<2A\). Hence \(D_A\mid15M_A\). For any rational nonzero gap between such phases, its circular distance is at least \(1/D_A\ge1/(15M_A)\); once \(16^Lq\ge15M_A\), the tent is zero. This proves AV-10/11.

### Quantitative ceiling and the actual open problem

The classical prime number theorem gives \(\log M_A=\psi(16A)=16A+o(A)\). Thus on the selected \(q_A=O(\log A)\) schedule,
\[
\boxed{L_A\le(16/\log16+o(1))\,A.}\tag{AV-12}
\]
This does **not** assert that the true \(D_A\) requires linear depth, only that this unconditional denominator estimate guarantees release by that depth. SUCC's current sufficient normality criterion examines \(K_A\asymp\log\log A\), much shallower. The gap is real as an *unpaid proof obligation*: a quantitative source-selected **early escape distribution**, not a merely finite eventual release, is required.

Exact Fraction tests for \(A=2,4,8,12,24,40\) verify that the original common conductor divides \(15M_A\) and that every tested original phase does too. This is corroboration, not a substitute for the general proof. Prior source-height results (e.g. #472) are acknowledged; no mathematical novelty is claimed. The \(15\) envelope may be improvable by source cancellation, and improving the constant alone will not bridge the linear-versus-loglog scale deficit.

**Status:** proved source-specific divisor/finite cutoff under the original zero-seed contract. Signed Weyl, real nearpair savings, π normality and RH remain OPEN.
