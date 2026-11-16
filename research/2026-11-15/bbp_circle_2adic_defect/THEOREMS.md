# BBP × circle × 2-adic carrier: the source-attached defect transport

**2026-11-15 — DRAFT RESEARCH, zero seed unchanged.**  This dossier responds to the proposal that hidden causal structure survives a change of basis as a *structured transport defect*. Source-specific exact results are separated from classical Monna-map / Fourier facts, finite numerical certificates, and open arithmetic estimates. **No proof of R0 or base-16 normality of pi is claimed.**

## 0. Typed source and the four distinct coordinates

The fixed, original four-pole forcing is

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)}.
\]

The original recurrence is \(U_0=0\), \(U_{n+1}=16U_n+r(n+1)\). Put \(x=\pi/16\), \(T_n=\sum_{j\ge1}16^{-j}r(n+j)\), \(u_n=\{U_n\}\), \(z_n=\{U_n+T_n\}=\{16^n x\}\). The classical BBP identity identifying \(x\) with geometric pi is an explicit imported dependency. The circle/line observer independently defines geometric pi from Euclidean arclength \(\pi=4\int_0^1(1+t^2)^{-1}dt\), but is NOT a new derivation of the BBP identity or normality. The authentic source has \(0<T_n<1/(64n^2)\) (for \(n\ge1\), inherited in #644) and \(T_n=1/(64n^2)+O(n^{-3})\) (from its four-pole asymptotics).

**Do not identify these different objects:**

1. \(U_n\) in \(\mathbb Q\cap\mathbb Z_2\), with its full *unreduced* integer carry, is the **arithmetic 2-adic state**.
2. \(u_n\in\mathbb R/\mathbb Z\) is the **rational real circle phase**.
3. \(z_n\in\mathbb R/\mathbb Z\) is the **completed zero-seeded pi phase**.
4. \(\rho(z_n)\in\mathbb Z_2\) is the **symbolic digit-reversal code of the real phase**, NOT the arithmetic 2-adic state \(U_n\).

At \(n=1\), \(U_1=47/15\), hence \(U_1\equiv1\pmod{16}\), but its first real hexadecimal digit is \(\lfloor16\{U_1\}\rfloor=2\). This exact counterexample kills an otherwise tempting identification before any large-scale asymptotics.

## 1. BBP forcing is a 2-adic isometry (source algebra; proved)

Write \(r(t)=P(t)/D(t)\), with \(P(t)=120t^2-89t+16\) and \(D(t)=(2t-1)(4t-1)(8t-7)(8t-3)\). Every denominator factor is odd throughout \(\mathbb Z_2\). In \(\mathbb F_2[t]\), \(P(t)\equiv t\), \(D(t)\equiv1\). Moreover the divided difference \((P(t)-P(s))/(t-s)\equiv1\pmod2\); since all nonconstant coefficients of \(D\) are even, \((D(t)-D(s))/(t-s)\equiv0\pmod2\). Consequently

\[
\frac{r(t)-r(s)}{t-s}
=\frac{[(P(t)-P(s))/(t-s)]D(s)-P(s)[(D(t)-D(s))/(t-s)]}{D(t)D(s)}
\in1+2\mathbb Z_2,
\]

for \(t\ne s\), and therefore \(|r(t)-r(s)|_2=|t-s|_2\). The earlier SUCC 2-adic forcing work, including #610, is prior provenance; academic originality is not asserted.

## 2. The 2-adic backward source clock is an isometry and an odometer conjugacy (proved)

Define a **2-adic extension**, not a modification of real source values, by

\[
F(t)=\sum_{j=0}^{\infty}16^j r(t-j),\qquad t\in\mathbb Z_2.
\tag{BC-1}
\]

It converges uniformly in \(\mathbb Z_2\), because every summand is 2-adically integral. Its difference quotient is

\[
\frac{F(t)-F(s)}{t-s}
=\frac{r(t)-r(s)}{t-s}+16\sum_{j\ge1}16^{j-1}
\frac{r(t-j)-r(s-j)}{t-s}\in1+2\mathbb Z_2.
\]

Thus \(F\) is an **isometric bijection of \(\mathbb Z_2\)**: at every modulus \(2^m\) it induces an injective, hence surjective, finite map. The source-induced odometer \(\mathcal S_F=F\circ(t\mapsto t+1)\circ F^{-1}\) is a genuine conjugate of successor. The identity

\[
F(t+1)=16F(t)+r(t+1)
\tag{BC-2}
\]

shows that this autonomous odometer has exactly the original affine forcing *when the source index is recovered by \(F^{-1}\)*. This is a **mathematical conjugacy**, not a claim that \(U_n\)'s real phase is equidistributed.

The original zero-seeded state satisfies, exactly in \(\mathbb Z_2\),

\[
\boxed{F(n)-U_n=16^n F(0).}\tag{BC-3}
\]

Indeed both sides follow from the recurrence and the initial difference \(F(0)-U_0=F(0)\). Modulo \(q=16^k\), \(F(n)\) needs only its last \(k\) taps:

\[
F(n)\equiv\sum_{j=0}^{k-1}16^j r(n-j)\pmod{16^k}.
\]

The original zero seed has a stronger source-specific identity proved in §2a below: **\(F(0)=0\)** in \(\mathbb Z_2\). Consequently the exact source-time identity is

\[
\boxed{U_n=F(n)\text{ in }\mathbb Z_2\qquad\text{for every }n\ge0.}\tag{BC-3a}
\]

Because \(F\) is an isometric bijection, **every** complete consecutive block of \(q=16^k\) original zero-seeded BBP states, including the block starting at the literal origin, has the exact permutation property

\[
\boxed{\{U_n\bmod16^k:n=B,\ldots,B+16^k-1\}=\mathbb Z/16^k\mathbb Z}
\quad(B\ge0,k\ge1),\tag{BC-4}
\]

with every residue appearing **once**. More generally the same holds modulo \(2^m\) for all \(m\ge1\). Every nontrivial finite arithmetic 2-adic character has identically zero average over these complete blocks. This is an **exact source-specific finite-clock equidistribution theorem**; it is **NOT** the real-circle equidistribution or normality of \(\pi\).

### 2a. The original source annihilates its own 2-adic backward origin (new source-specific paper proof; independent review pending)

Write the *different*, original BBP source **weight polynomial**

\[
Q(z)=4-2z^3-z^4-z^5=(1-z)(z^2+2)(z^2+2z+2).
\]

Do not confuse \(Q(z)\) with the quadratic numerator \(P(t)\) in §1. Work in the finite extension \(K=\mathbb Q_2(\sqrt 2,i)\), containing all eight roots \(\alpha\) of \(\alpha^8=16\). They all have 2-adic valuation \(v_2(\alpha)=1/2>0\). The convergent 2-adic logarithm
\(\log_2(1-\alpha)=-\sum_{m\ge1}\alpha^m/m\)
therefore exists for all eight roots. Normalized roots-of-unity filtering gives

\[
\sum_{\alpha^8=16}\alpha^\ell=\begin{cases}8\cdot16^{\ell/8}&8\mid\ell,\\0&8\nmid\ell.\end{cases}
\]

For every integer \(j\ge0\), the declared 2-adic extension of the *same rational forcing* satisfies

\[
r(-j)=-\frac4{8j+7}+\frac2{8j+4}+\frac1{8j+3}+\frac1{8j+2}.
\]

Substitute \(zQ(z)=4z-2z^4-z^5-z^6\) into the finite root-filter sum and expand each logarithm. The four surviving degrees, \(8j+7,8j+4,8j+3,8j+2\), reconstruct **exactly** the four original signed poles with their original coefficients. The expansions converge rapidly in \(K\), permitting interchange of sums. Therefore

\[
\boxed{F(0)=\sum_{j=0}^\infty16^jr(-j)
=\frac1{128}\sum_{\alpha^8=16}\alpha Q(\alpha)\log_2(1-\alpha).}\tag{BC-0a}
\]

Now enumerate all eight roots, with no unaccounted term:

* At \(\alpha=\pm i\sqrt2\) and \(\alpha=-1\pm i\), \(Q(\alpha)=0\).
* At \(\alpha=1\pm i\), \(1-\alpha=\mp i\) is a fourth root of unity. Its **2-adic** logarithm is zero, because the logarithm is a homomorphism on \(1+\mathfrak m_K\) and a characteristic-zero additive group has no torsion. The corresponding coefficient \(Q(\alpha)\) need not vanish.
* At \(\alpha=\pm\sqrt2\), direct substitution gives \(\alpha Q(\alpha)=-16\) for **both** signs. Their combined contribution is \(-16[\log_2(1-\sqrt2)+\log_2(1+\sqrt2)]\). Both arguments belong to \(1+\mathfrak m_K\), their product is \(-1\), and \(\log_2(-1)=0\). Hence their sum vanishes.

Every source-root contribution is zero or cancels in a declared pair, proving

\[
\boxed{F(0)=0\quad\text{in }\mathbb Z_2.}\tag{BC-0}
\]

Together with (BC-3), this proves (BC-3a)/(BC-4) **without** finite-precision extrapolation. The earlier independent modular check \(F(0)\equiv0\pmod{16^{256}}\) now serves as a finite sanity check, *not* the proof. This is a paper derivation, not Lean-verified and not externally refereed. The BBP source weight polynomial factorization already appears in SUCC #430; this research makes no academic priority claim for the factorization, 2-adic log, or root-of-unity filter.

### 2b. Exact arithmetic-real denominator/carry attachment (source coupling, proved)

Let \(d_n>0\) be the **reduced, odd** denominator of the original \(U_n\), \(a_n=d_nU_n\in\mathbb Z\), \(m_n=\lfloor U_n\rfloor\), and \(b_n=a_n-d_nm_n\in\{0,\ldots,d_n-1\}\). The **same rational number** has two observations:

\[
\boxed{U_n\bmod q\;\equiv\;m_n+b_nd_n^{-1}\pmod q,\qquad
z_n=\left\{\frac{b_n}{d_n}+T_n\right\}\in\mathbb R/\mathbb Z,\quad q=16^k.}\tag{DC-0}
\]

The modular inverse \(d_n^{-1}\pmod q\) exists because all denominators are odd. Thus the ordinary integer winding \(m_n\), the original odd denominator \(d_n\), and the same numerator remainder \(b_n\) jointly specify the arithmetic 2-adic observation and the rational real-circle phase; the BBP Green tail completes the real observation. **This is the authenticated bridge.** Projecting away \(d_n\) or \(m_n\) generally destroys this phase coupling, even if the marginal 2-adic register visits every address. A source-coupled proof must use a nontrivial constraint on this **joint** data, not only the perfect 2-adic permutation law.

### 2c. The actual 2-adic `−1 → 0` source path and exact finite defect valuation (new corollary)

The origin theorem has a stronger negative-index consequence *inside the declared 2-adic analytic extension*; it is not a claim that the physical BBP real-time source has negative epochs. For each positive integer \(m\), iterate the exact same affine law \(F(t+1)=16F(t)+r(t+1)\) forward from \(t=-m\) to \(t=0\). The zero anchor gives

\[
\boxed{0=16^m F(-m)+\sum_{j=0}^{m-1}16^j r(-j),\qquad
F(-m)=-16^{-m}\sum_{j=0}^{m-1}16^j r(-j).}\tag{BC-5}
\]

Thus the entire **negative source-time orbit consists of rational 2-adic integers**, computable by finite original-formula rational arithmetic. At the first neighboring state, \(r(0)=16/21\), hence

\[
\boxed{F(-1)=-\frac1{21},\quad 16F(-1)+r(0)=0=F(0),\quad
\mathcal S_F(-1/21)=0.}\tag{BC-6}
\]

Here \(-1\) is the **2-adic source-time index**, and \(-1/21\) is its **2-adic carrier value**. These are distinct objects. The two values are one causal successor apart, even though their standard 2-adic metric distance is one. This is an exact, nontrivial source-coupled realization of the user's `−1 → 0` observation, without claiming a continuous path in totally disconnected \(\mathbb Z_2\) or a physical time reversal.

Finally, the already proved isometry plus \(F(0)=0\) yields
\(v_2(F(-m))=v_2(m)\), and consequently the **sharp valuation identity**

\[
\boxed{v_2\!\left(\sum_{j=0}^{m-1}16^j r(-j)\right)
=4m+v_2(m)\qquad\text{for every integer }m\ge1.}\tag{BC-7}
\]

No asymptotic extrapolation is involved: (BC-7) is a deductive consequence of (BC-0) and isometry. It implies an entire infinite family of exact rational-source 2-adic divisibility certificates, and it provides independent finite adversarial witnesses for any faulty anchor or sign convention. It does **not** imply the real Fourier orbit is normal.

## 3. Monna/digit-reversal circle quotient and its exact defects (classical structure, new source application)

For \(a=\sum_{j\ge1}d_j16^{j-1}\in\mathbb Z_2\), \(0\le d_j\le15\), define the radix-16 Monna map to the circle

\[
\Pi(a)=\sum_{j\ge1}d_j16^{-j}\pmod1.
\tag{CM-1}
\]

It is continuous and onto, but not injective; it pushes normalized 2-adic Haar measure to circle Lebesgue measure. A circle radix-boundary has two symbolic 2-adic codes. Specifically, at a boundary whose two real expansions first differ at digit \(m\),

\[
(d_1\cdots d_{m-1}\,c\,15\,15\cdots),\qquad
(d_1\cdots d_{m-1}\,(c+1)\,0\,0\cdots),
\]

its **two 2-adic codes differ by exactly \(17\cdot16^{m-1}\)**, using the indicated orientation. At the global circle seam the words \(15^\infty\) and \(0^\infty\) correspond to \(-1\) and \(0\) in \(\mathbb Z_2\), even though \(\Pi(-1)=\Pi(0)=0\). This is the operationally short \(-1\to0\) successor that the circle quotient identifies. General finite-level real-prefix increments are **not** the arithmetic 2-adic successor; see §4.

No continuous right-inverse \(\sigma:\mathbb T\to\mathbb Z_2\) exists because the circle is connected and \(\mathbb Z_2\) is totally disconnected. This is an actual *topological* transport obstruction: a measurable/pointwise digit section is available off the radix seam but no globally continuous inverse observer frame is available.

The standard Monna map is prior mathematics; see `PROVENANCE.md` for literature, including diaphony and modern transport examples. No academic novelty is claimed for (CM-1) itself.

## 4. An exact **source-selected** circle carry and its 2-adic code gap (proved)

Let \(q=16^k\), \(u_n=\{U_n\}\), and suppose \(qT_n<1\). The uncompleted and completed circle prefix registers satisfy

\[
A_{n,k}=\lfloor qu_n\rfloor,\quad
A'_{n,k}=\lfloor q(u_n+T_n)\rfloor\bmod q,\quad
D_{n,k}=\lfloor q(u_n+T_n)\rfloor-\lfloor qu_n\rfloor.
\]

Then

\[
\boxed{D_{n,k}=\mathbf1_{\{qu_n\}+qT_n\ge1}\in\{0,1\},
\quad A'_{n,k}\equiv A_{n,k}+D_{n,k}\pmod q.}\tag{CD-1}
\]

This is an exact arithmetic/circle-metric seam law. Let \(R_k\) reverse the \(k\) hex digits of the integer prefix. If \(D=1\) and \(A=q-1\), then \(R_k(A')-R_k(A)\equiv1\pmod q\): the global \(-1\to0\) seam. Otherwise, if \(m\) is the **one-based location of the first real digit changed** by the carry, the 2-adic code gap is

\[
\boxed{R_k(A')-R_k(A)\equiv17\cdot16^{m-1}\pmod{16^k}.}\tag{CD-2}
\]

The \(16\)-adic valuation of the gap is exactly \(m-1\). This follows by adding one to the ordinary real prefix and explicitly reversing its trailing chain of hexadecimal F digits. No claim that this symbolic code equals \(U_n\bmod q\) is allowed: they are different coordinate systems.

**Critical source scale.** Since \(T_n\sim1/(64n^2)\), the source lift \(qT_n\) is order one at \(q\asymp n^2\), or \(k\sim2\log_{16}n+3/2\). The deterministic choice \(k(B)=\max\{k\ge1:16^k\le32B^2\}\) ensures \(qT_n<1/2\) on every authentic shell \([B,2B)\) for \(B\ge8\). This is *also* the scale at which the Fourier-grid approximation error \(O_h(q^{-1})\) and the real source Green error \(O_h(B^{-2})\) have matching order for each fixed \(h\). Unlike a fixed-depth Haar norm, the selected critical depth grows with the source clock.

The seam indicator at fixed \(n,k\) is a periodic union of real arcs of length \(T_n\). Under uniform **external** circle measure its mean is \(qT_n\), and its only nonzero Fourier frequencies are multiples of \(q\): for \(j\ne0\),

\[
\widehat D_{q,T_n}(jq)=\frac{e^{2\pi i j qT_n}-1}{2\pi i j};
\quad\widehat D_{q,T_n}(\ell)=0\;(q\nmid\ell).
\tag{CD-3}
\]

The actual phases \(u_n\) are **not** sampled from uniform circle measure. The signed empirical deviation of seam hits from \(qT_n\) is an open source-selected high-frequency correlation; averaging (CD-3) as if the \(u_n\) were iid would be circular.

## 5. Unitary change of observer basis: circle Fourier \(\leftrightarrow\) reversed 2-adic Fourier (proved)

Let \(q=16^k\), \(R_k(a)\) radix digit reversal, and \(e(y)=\exp(2\pi i y)\). Define

\[
\boxed{M^{(k)}_{h,t}=\frac1q\sum_{a=0}^{q-1}e\left(\frac{hR_k(a)-ta}{q}\right),
\quad 0\le h,t<q.}\tag{FT-1}
\]

This is a **unitary matrix**: it is the usual finite DFT of the permutation obtained by reversing digits. It factors into independent digit sums,

\[
M^{(k)}_{h,t}=\prod_{j=1}^k\left[\frac1{16}\sum_{d=0}^{15}
 e\left(d\left(\frac{h}{16^j}-\frac{t16^{j-1}}q\right)\right)\right].
\tag{FT-2}
\]

For a source empirical distribution of *completed real* prefix registers \(A'_{n,k}\), let
\(P_{B,k}(t)=B^{-1}\sum_{n=B}^{2B-1}e(tR_k(A'_{n,k})/q)\). Then the circle-grid Fourier coefficient obeys the **exact transport**

\[
\boxed{C_{B,k}(h):=\frac1B\sum_{n=B}^{2B-1}e(hA'_{n,k}/q)
=\sum_{t=0}^{q-1}M^{(k)}_{h,t}P_{B,k}(t).}\tag{FT-3}
\]

Parseval preserves the **full finite Gram norm** across the two bases; low-mode truncations need not preserve it. For every fixed \(h\), the completed real Weyl mean satisfies

\[
\boxed{|W_B^\pi(h)-C_{B,k}(h)|\le2\pi|h|/16^k.}\tag{FT-4}
\]

**Source-selected signed seam interface:** define the analogous \(C^U_{B,k}\) from \(A_{n,k}\). If \(qT_n<1\) throughout the shell, then

\[
\boxed{C_{B,k}(h)-C^U_{B,k}(h)
=(e(h/q)-1)\frac1B\sum_{n=B}^{2B-1}D_{n,k}e(hA_{n,k}/q).}\tag{FT-5}
\]

This is the operational missing-detail response, *exactly* retaining the original signed phases and actual source-selected seam hits. For a fixed low \(h\) it is \(O(h/q)\) even if many carries occur. At moving \(h=q/2\), it becomes the **exact signed parity-interferometer**

\[
\boxed{C_{B,k}(q/2)-C^U_{B,k}(q/2)
=-\frac2B\sum_{n=B}^{2B-1}D_{n,k}(-1)^{A_{n,k}}.}\tag{FT-6}
\]

This distinguishes an invisible low-frequency deviation from an order-one moving-frequency seam signal. It does **not** show the signed right-hand side is small, nor that it controls fixed-frequency Weyl sums. Moving-frequency defects do not automatically imply base-16 normality.

At critical \(q\asymp B^2\), naive full-register energy **cannot** tend to zero: every empirical distribution of at most \(B\) samples obeys

\[
\sum_{t=1}^{q-1}|P_{B,k}(t)|^2=q\sum_a p_a^2-1\ge q/B-1.
\tag{FT-7}
\]

Thus a high-depth positive norm is dominated by an unavoidable sampling floor even for an ideal distinct grid. The meaningful target must preserve signed, selected low-mode projections and their interference/transport; merely transferring a positive norm is insufficient. This overlaps SUCC #572's collision-pressure warning and #644's all-depth Haar calibration.

## 6. Coherent wrong-seed and other hostile controls (proved)

The same-forcing coherent seed \(s=-x=-\pi/16\) has the **exact** unwrapped state \(U_n(s)=-T_n\), and completed real phase \(z_n(s)=0\). At every \(k,n\) with \(qT_n<1\), the uncompleted real prefix is \(q-1\), the completed prefix is \(0\), and \(D_{n,k}=1\) on **every** time step. Thus the counterseed realizes the **maximal and perfectly coherent \(-1\to0\) global seam**, despite being nonnormal. The counterseed does not have an odd-denominator rational state, so no claim about arithmetic \(U_n(s)\in\mathbb Z_2\) is made. This kills the proposed generic implication "large coherent seam -> normality" and makes the original zero anchor indispensable.

The rational seed \(s=1/16\) is a different control: \(U_n(s)-U_n(0)=16^{n-1}\) for \(n\ge1\), so its later real circle phases are identical. The original source passport \(16^{-n}U_n(s)-P_n=s\) still discriminates the seeds; at any fixed 2-adic precision, their integer-state differences eventually become invisible because they gain four powers of 2 per time step. This illustrates finite-toolkit identity loss; it is not a new pi-normality implication.

**A stronger falsifier of shortcut claims:** The unconditional **all-block** arithmetic 2-adic permutation law (BC-4) holds alongside the open real π question; "2-adic uniformity -> real normality" is not a theorem. The map from real hex prefixes to the actual rational \(U_n\bmod q\) is not digit reversal, and the relation must retain its full source/carry and odd-denominator information. Dropping the pairing is exactly an invalid change of frame.

## 7. A typed next arithmetic gate, not a promised proof

A candidate source-coupled joint observable is

\[
J_{B,k}(h,t)=\frac1B\sum_{n=B}^{2B-1}
 e\left(\frac{hA'_{n,k}-t(U_n\bmod q)}{q}\right),
\quad q=16^k,
\tag{N-1}
\]

with the \(U_n\bmod q\) factor taken from **arithmetic \(\mathbb Z_2\)**, not the reversed-code variable used in (FT-3). Its \(t=0\) marginal reconstructs real Weyl phases, while \(h=0\) late-window marginal is explicitly periodic/permutation-controlled. A **new nontrivial source-selected signed bound** must constrain the *joint* modes, their phase alignment or conditional defects. A marginal uniformity statement is provably insufficient. In particular, any proposed estimator from the exact odometer of §2 must pass the coherent counterseed, seed passport and independent residual checks before it can imply even R0.

### 7a. Exact finite source-clock anti-aliasing and a mixed-norm no-go

The new BC-0 source anchor upgrades the arithmetic clock to \(U_n\bmod q=F(n)\bmod q\) **for every nonnegative** \(n\). Since \(F\) is an isometry, the arithmetic residues \(a_n=U_n\bmod q\) are pairwise different whenever source indices \(n\) lie in any contiguous epoch of length \(B\le q=16^k\). In particular, at the **critical real Green scale** \(q\asymp B^2\), the original arithmetic register has *zero collisions* across the entire source shell. This anti-aliasing statement is exact and holds without any real equidistribution hypothesis.

For any real phases \(z_n\) (in particular the original completed \(z_n=\{16^n\pi/16\}\)), form a full mixed character bank
\[
\mathcal J_{B,q}(h,t)=\frac1B\sum_{n=B}^{2B-1}
 e\left(hz_n-\frac{t a_n}{q}\right),\quad t=0,\ldots,q-1.
\]

Finite character orthogonality and the exact source arithmetic noncollision prove
\[
\boxed{\sum_{t=0}^{q-1}|\mathcal J_{B,q}(h,t)|^2
=\frac{q}{B}\quad(B\le q),\qquad
\mathcal J_{B,q}(h,0)=W_B^\pi(h).}\tag{N-2}
\]

Thus \(\sum_{t\ne0}|\mathcal J|^2=q/B-|W_B^\pi(h)|^2\). **The huge positive energy outside the zero frequency is guaranteed even for coherent \(z_n\equiv0\)**; it does not prove π normality or R0. The exact joint carrier-inherited information is in **where** this norm lies, its phase orientation and source-selected conditional defects, not the raw aggregate. In particular, the normalized share of \(t=0\) tends to zero automatically as \(q/B\to\infty\), even if \(W_B(h)=1\) forever. A claim that this vanishing normalized share establishes real Fourier decay is therefore **REFUTED** by the coherent null control.

Possible discriminating avenues: prove a non-product joining/conditional covariance bound for (N-1) from the *original* four-pole rational source; derive a source-specific estimate on (FT-5)/(FT-6) controlling fixed \(h\) rather than merely moving \(h\); and explicitly test whether the π Euclidean circle arclength/BBP identity constrains the odd-prime cofactor winding left invisible by the 2-adic marginal. None is established here.

### Claim ledger

| ID | Statement | Status |
|---|---|---|
| BC-1/2 | 2-adic analytic source extension, isometric bijection and odometer conjugacy | **PROVED PAPER**, exact finite controls |
| BC-3/4 | Exact zero-source anchor coupling \(F(n)=U_n\); all-block arithmetic register permutation | **PROVED PAPER**, modular controls |
| BC-5/6/7 | Rational negative-index carrier path, exact \(-1/21\) predecessor and sharp 2-adic valuation \(4m+v_2(m)\) | **PROVED PAPER**, exact rational controls |
| BC-0 | Infinite 2-adic anchor via root filter and 2-adic logarithms | **PROVED PAPER**, review / Lean pending |
| DC-0 | Exact odd-denominator + integer-winding bridge between arithmetic and real observations | **PROVED PAPER**, rational controls |
| CM-1 | Monna map, seam fibres, no continuous circle section | **CLASSICAL**, specialized explicit digit proof |
| CD-1/2/3 | Source circle carry, digit-reversal gap, seam Fourier coefficients | **PROVED PAPER**, exact finite controls |
| FT-1..6 | Finite unitary basis transport and signed real/carry discrepancy | **PROVED PAPER**, numerical Fourier checks |
| FT-7 | Critical-depth full-register energy floor | **CLASSICAL**, exact algebra |
| N-1/2 | Mixed source-selected join; exact high-depth noncollision/Parseval no-go | **PROVED FINITE**, no signed asymptotic saving |
| R0 / pi normality | Source-signed all-shell bound | **OPEN** |

No external blind peer review or Lean kernel proof was performed. The local exact modular/permutation tests, root/Green interval computations, independent DFT and finite shell witnesses are documented in `VALIDATION.md`.
