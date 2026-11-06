# Operation TRIANGLE SEAM × SILVER SOURCE × SIGNED RETURN SPECTRUM

**2026-11-06 | strict research child of [SUCC PR #528](https://github.com/femboy2112/SUCC/pull/528), at parent 45c5d41435fdf94998d81901b0e58b9fa7775106.** Proofs below are local elementary derivations, not independently refereed priority or formal Lean theorems. Base-16 normality of π and the selected original signed Weyl estimate remain **OPEN**.

## 0. Typed authentic source and topology boundary

For positive integers n let

\[
r(n)=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)}
=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
\]

Use literal \(U_0=0\), \(U_{n+1}=16U_n+r(n+1)\), \(C_n=\lfloor U_n\rfloor\), \(x_n=U_n-C_n\). All \(U_n,x_n\) are rationals with **odd reduced denominators** and therefore have well-typed embeddings in \(\mathbb Z_2\). The real circle phase \(x_n\) itself does not have a canonical group reduction modulo \(2^k\). Parent #527 proves the source graph

\[
V(t)=\sum_{j\ge0}16^j r(t-j),\quad
V(0)=0,\quad V(n)=U_n,\quad
v_2(V(s)-V(t))=v_2(s-t)
\]

on \(\mathbb Z_2\). We take that exact source theorem as a **stated inherited hypothesis** throughout; no numerical observation substitutes for its parent proof. Parent #528 proves the initial dyadic clone and exact carry reconstruction.

## 1. TS-01: the co-dual pair-overlap triangle has one exact 2-adic bit defect — PROVED LOCAL

Let \(R=\mathbb Z/2^K\mathbb Z\), \(K\ge1\), and take three *formal* vertices \(P,Q,S\). Define their three pair overlaps

\[
(A,B,D)=(P+Q,\ Q+S,\ S+P).
\]

Its integer matrix \(M=\left(\begin{smallmatrix}1&1&0\\0&1&1\\1&0&1\end{smallmatrix}\right)\) has determinant \(2\) and Smith normal form \({\rm diag}(1,1,2)\). Therefore its image in \(R^3\) consists **exactly** of the triples with \(A+B+D\) even; it has index two, and each allowed edge triple has exactly two vertex preimages. The kernel is precisely

\[
\ker M=\{(0,0,0),\ (2^{K-1},2^{K-1},2^{K-1})\}.
\]

Explicitly \(2P=A+D-B\), \(2Q=A+B-D\), \(2S=B+D-A\). A full \(K\)-bit vertex reconstruction from independent pair edges requires \(K+1\) bits of edge precision. The hidden shift by \(2^{K-1}\) in all vertices leaves every pair edge unchanged modulo \(2^K\).

**Interpretation strictly delimited:** The proposed HARMONIC/GOLDEN/EULER–MASCHERONI co-duality supplies labels for these three *formal* vertices and pairwise interactions. It does NOT supply a canonical embedding of the real numbers \(\gamma\) or \(\varphi^{-1}\) into \(\mathbb Q_2\). The determinant-two statement is universal integer algebra, not evidence that the source dynamically couples those constants.

## 2. TS-02: true BBP seam closes the triangle, but a false seam can spoof modular closure — PROVED LOCAL / repaired negative control

Specialize the formal coordinates to the **well-typed 2-adic rationals** \(P=V(n)=U_n\), \(Q=C_n\), \(S=x_n\). The authentic identity \(P=Q+S\) is exact. Writing \(A=P+Q,\ B=Q+S,\ D=S+P\) gives

\[
\boxed{A+D-3B=2(P-Q-S).}\tag{TS2}
\]

For a source-valid triple the edge constraint \(A+D=3B\) holds. Restricted **to the source plane** \(P=Q+S\), the pair-overlap map is injective even mod \(2^K\): \(P=B,\ Q=A-B,\ S=D-B\).

However, when checking an *arbitrary candidate* triple, edge closure modulo \(2^K\) establishes only \(P-Q-S=0\pmod{2^{K-1}}\). In particular, with true \(P=Q+S\), change only \(Q\) by \(2^{K-1}\). The proposed source seam becomes false modulo \(2^K\), yet its edge closure still passes modulo \(2^K\), because the defect was doubled. Checking the edge defect modulo \(2^{K+1}\) is equivalent to verifying the original seam modulo \(2^K\).

**Real failed run:** An initial test incorrectly expected the half-modulus wrong-carry perturbation to break closure at the original precision. It failed; the counterexample and correction are retained in VALIDATION. The distinction between an injective *restricted* map and an edge test that *certifies membership* in its restriction is load-bearing. This is an actual one-bit certificate deficit, not a real Fourier sign.

## 3. TS-03: every positive integer lag has an exact source clone and next-bit flip — PROVED LOCAL

For **any** integer \(q\ge1\), not just powers of two, define \(\ell=v_2(q)\) and the genuine future source block \(S_q(t)=\sum_{j=1}^q16^{q-j}r(t+j)\). The source recurrence and isometry imply

\[
V(t+q)=16^qV(t)+S_q(t),\quad
V(t+q)-V(t)\equiv2^\ell\pmod{2^{\ell+1}}.
\]

Because \(4q\ge\ell+1\), the \(16^qV(t)\) term vanishes modulo \(2^{\ell+1}\). Therefore, for every \(t\in\mathbb Z_2\),

\[
\boxed{S_q(t)\equiv V(t)+2^\ell\pmod{2^{\ell+1}}.}\tag{TS3}
\]

This extends PR #528's \(q=2^k\) identity. For a return-fiber pair whose time lag is \(q=d2^k\), the 2-adic valuation of the **unwrapped rational state difference** is exactly \(k+v_2(d)\). The result holds for other isometric 2-adic graphs too. It does not force a real antiphase.

## 4. TS-04: exact source-carry fractional-bit BORROW rule — PROVED LOCAL

Fix \(k\ge1\), \(Q=2^k\), \(n\ge0\). Put \(\Delta C=C_{n+Q}-C_n\), \(\Delta x=x_{n+Q}-x_n\). By TS3 and the literal source seam,

\[
\Delta C+\Delta x\equiv Q\pmod{2Q}
\quad\text{in }\mathbb Z_2.
\]

Write \(a=[\Delta C]_{2Q}\), \(L=a\bmod Q\), \(t=\lfloor a/Q\rfloor\in\{0,1\}\). Let \(s=\lfloor[\Delta x]_{2Q}/Q\rfloor\in\{0,1\}\), where the rational denominator of \(\Delta x\) is odd. Then direct modular subtraction yields the exact conditional bit law

\[
\boxed{s=t\ \mathsf{XOR}\ {\bf 1}_{L=0}.}\tag{TS4}
\]

When lower carry residues agree (\(L=0\)), the next 2-adic fraction bit flips relative to the carry bit; when they differ, the borrow transports the flipped bit without that complement. These are **2-adic rational bits**, not base-16 digits of the real number π. The real return Fourier character remains uncontrolled by TS4.

## 5. TS-05: authentic harmonic/Gamma source primitive selects a silver-ratio closed form — PROVED LOCAL (classical digamma reduction)

The signed poles have offsets \(\alpha=(1/8,1/2,5/8,3/4)\) and coefficients \(c=(4,-2,-1,-1)\). The digamma recurrence \(\psi(z+1)-\psi(z)=1/z\) gives the exact finite primitive

\[
\Phi_N:=\sum_{n=1}^N r(n)
=\frac18\sum_{a=1}^4 c_a\bigl(\psi(N+\alpha_a)-\psi(\alpha_a)\bigr).
\]

Since \(\sum c_a=0\) and \(\psi(N+\alpha)=\log N+O(N^{-1})\), the first terms cancel in the limit. Gauss's digamma formula at these rational arguments gives, writing \(s=\sqrt2\), \(L=\log(1+s)\),

\[
\begin{aligned}
\psi(1/8)&=-\gamma-4\log2-\frac{\pi}{2}(1+s)-sL,\\
\psi(1/2)&=-\gamma-2\log2,\\
\psi(5/8)&=-\gamma-4\log2-\frac{\pi}{2}(1-s)+sL,\\
\psi(3/4)&=-\gamma-3\log2+\frac{\pi}{2}.
\end{aligned}
\]

Substitution and exact cancellation of all \(\gamma\) terms yields

\[
\boxed{\sum_{n=1}^{\infty}r(n)=\frac{4+5\sqrt2}{16}\pi
+\frac58\log2+\frac{5\sqrt2}{8}\log(1+\sqrt2).}\tag{TS5}
\]

This equals \(3.3860476195971917219364\ldots\). The silver ratio \(1+\sqrt2\) is a Pisot unit (root of \(X^2-2X-1\)); its conjugate \(1-\sqrt2\) has magnitude below 1. The **original pole conductor 8** directly generates the \(\mathbb Q(\sqrt2)\) closed form; golden \(\varphi\) is an auxiliary Pascal/Pisot selection, NOT deduced uniquely from these poles. The real \(\gamma\) has been canceled, not identified with a 2-adic constant. Different regularizations may expose it elsewhere.

**Rigorous tail:** For all n≥2, \(0<r(n)<1/n^2\). Indeed \(A(n)>0,D(n)>0\); for \(t=n-2\ge0\),

\[
D(n)-n^2A(n)=392t^4+2201t^3+4494t^2+3902t+1185>0.
\]

Therefore \(0<\Phi_\infty-\Phi_N<1/N\) for every \(N\ge2\) by the integral bound for \(\sum_{n>N}n^{-2}\). The transcendental expression is proved from the digamma identity; floating finite evaluations are only diagnostics.

## 6. TS-06: the prior return energy's 2-adic labels only permute clock fibers — PROVED LOCAL no-go

With \(Q=2^k\), \(N=QM\), original state \(V\), and \(F_n=e^{2\pi ihU_n}\), the PR #528 energy is

\[
R_{Q,M}(h)=\frac1Q\sum_{j=0}^{Q-1}\left|\frac1M\sum_{t=0}^{M-1}F_{j+tQ}\right|^2.
\]

Because \(V\) is an isometry, \(V(n)\equiv V(m)\pmod Q\iff n\equiv m\pmod Q\). Thus indexing fibers instead by \(V(n)\bmod Q\) **only permutes their labels**. For *any sequence* \(F_n\), and any bijective state relabeling of the \(Q\) clock residues, the energy stays exactly the same.

The inequality \(|W_{QM}(h)|^2\le R_{Q,M}(h)\) is valid, but the equal-weight partition contributes no original-source signed saving on its own. Source effects enter only through the actual real values \(F_n\), or through a newly defined nontrivial source-dependent observable. This is a rigorous audit of the purported return-fiber advantage.

## 7. TS-07: exact Haar-SEED null spectrum, for arbitrary forcing — PROVED LOCAL

Fix any integer \(b\ge2\), arbitrary real forcing \(r_1,r_2,\ldots\), and the recurrence \(U_n(s)=b^ns+a_n\) with \(a_n\) independent of seed \(s\). For \(h\ne0\), \(Q,M\ge1\), define \(R_{Q,M}^{(s)}(h)\) by the preceding energy formula, replacing \(16\) by \(b\). If **only the seed** \(s\) is sampled uniformly modulo one, then

\[
\boxed{\mathbb E_s R_{Q,M}^{(s)}(h)=\frac1M,\qquad
\operatorname{Var}_s R_{Q,M}^{(s)}(h)=\frac{M-1}{Q M^3}.}\tag{TS7}
\]

Proof: expanding the square, the diagonal has \(QM\) terms divided by \(QM^2\), yielding \(1/M\). Every off-diagonal seed character has frequency \(h(b^p-b^q)\ne0\), hence Haar integral zero. For the variance, every **oriented nonzero difference** of two distinct powers of \(b\) has a unique ordered pair \((p,q)\): its sign determines orientation, its \(b\)-adic valuation gives the smaller exponent because \(b\nmid b^d-1\), and its magnitude identifies the larger exponent. Consequently the off-diagonal frequencies are pairwise distinct. Parseval gives precisely \(QM(M-1)/(Q^2M^4)\), even when the offsets \(a_n\) come from an arbitrary forcing.

This is an **ensemble** calibration, not a theorem for the single zero-seeded π orbit. It shows that first and second seed-Haar moments of this return energy are forcing-independent. In particular, simply matching the ensemble null cannot fingerprint the original source.

## 8. TS-08: dyadic signed shell decomposition and hostile shadow — PROVED LOCAL identity / OPEN saving

For \(Q=2^k\), split positive return lag \(d=1,\ldots,M-1\) by \(a=v_2(d)\). Expansion of the energy gives

\[
\boxed{
R_{Q,M}(h)=\frac1M+
\frac{2}{QM^2}\sum_{a\ge0}\ \sum_{\substack{1\le d<M\\v_2(d)=a}}
\Re\sum_{j=0}^{Q-1}\sum_{t=0}^{M-1-d}
e^{2\pi ih(U_{j+(t+d)Q}-U_{j+tQ})}.}\tag{TS8}
\]

Only finitely many shells appear. Every term in shell \(a\) has the authentic 2-adic state-difference valuation exactly \(k+a\), by TS3. **Shell contributions are signed real numbers**, and can be negative; a next-bit flip does not prescribe their sign. To prove real Weyl decay using this gate, a *new original-zero-seed bound on the sum of signed shells* must be established for sufficiently dense horizons and every fixed nonzero \(h\).

Hostile countermodel: \(H(n)=n/(2n-1)^4\) is the 2-adic isometric, literal-zero, real-decaying rational shadow from PR #527. Its 2-adic valuation shell hierarchy is identical; its real fractions tend to 0. For *any* choices \(Q,M\) with \(N=QM\to\infty\), the Cesàro mean of \(|e^{2\pi ihH(n)}-1|\) tends to 0, and

\[
|R_{Q,M}^{H}(h)-1|
\le\frac2N\sum_{n=0}^{N-1}|e^{2\pi ihH(n)}-1|\longrightarrow0.
\]

(The inequality uses the within-fiber triangle bound and \(|\,|A|^2-1|\le2|A-1|\) for \(|A|\le1\).) Hence the 2-adic shells alone cannot imply real signed saving. This is a genuine source countermodel, not the authentic π source.

## 9. Verdict and source dependencies

**PROVED LOCAL:** TS1–TS8 mathematical identities, conditional on inherited #527 source isometry/zero where invoked. **OBSERVED-FINITE:** independent exact rational controls, full small-modulus triangle enumeration, finite signed shell samples and optional SymPy audit. **REFUTED:** unrestricted triangle closure as a K-bit seam verifier; 2-adic state fiber labels as an independent source-sensitive energy; universal 2-adic bit-flip ⇒ real Haar inference. **OPEN:** source-selected \(R_{Q,M}^{U_0=0}(h)\to0\) (or \(W_N(h)\to0\)) along a dense enough sequence for all nonzero \(h\); therefore π normality remains open. No RH proof or quantum claim.

**Known literature, not world-priority claims:** Bailey & Crandall (2001), *On the Random Character of Fundamental Constant Expansions*, https://doi.org/10.1080/10586458.2001.10504441 ; Lagarias (2001), *On the Normality of Arithmetical Constants*, https://doi.org/10.1080/10586458.2001.10504456 (broad orbit bridge may hold without normality); classical Gauss digamma identity https://mathworld.wolfram.com/GausssDigammaTheorem.html . Parent SUCC #527/#528 supplies the source and carry framework, not external independent certification.
