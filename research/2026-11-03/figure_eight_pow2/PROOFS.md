# SUCC figure-eight at powers of two: exact 16-step jets, Hensel source root, two-stage gluing

2026-11-03. RESEARCH ONLY. Pinned parent PR #482 at 5599ebd35bda64ad817e1b30d5aaa486e7049b35. Main E² chiral source, main original 2-adic particular isometry, original Gamma seam and read-only sibling PR #481 are credited as antecedents. The previous unpushed eight-step boundary theorem and eight tests were audited and reproduced locally. Immutable signed original four BBP poles and literal U_0=0 retained. Base-16 π normality remains OPEN.

## F8-01. All coherent powers of two in the E² microclock

The historical four-rational-dimensional E² source successor and involution are

\[
\mathcal T=\mathrm{diag}(G,H),\quad
G=\tfrac12\begin{pmatrix}1&-1\\1&1\end{pmatrix},\quad
H=\begin{pmatrix}0&1\\1/2&0\end{pmatrix},\quad
J=\mathrm{diag}(I_2,-I_2).
\]

The already-established identities are \(\mathcal T^4=-J/4\), \(\mathcal T^8=I/16\). Squaring repeatedly yields for EVERY integer \(k\ge3\)

\[
\boxed{\mathcal T^{2^k}=16^{-2^{k-3}}I_4.}\tag{F8-01}
\]

At four microsteps a relative chirality sign appears; eight restores the common orientation at amplitude 1/16; sixteen is \(I/256\), with NO NEW primitive chirality. Two microsteps have \(\mathcal T^2=\mathrm{diag}(\tfrac12\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix},I_2/2)\).

CRITICAL TWO-CLOCK PASSPORT: ONE BBP arithmetic source index spans EIGHT microsteps. Sixteen *microsteps* realize only the first TWO source-index Mellin terms. The distinct arithmetic *index n=16* occurs in a 128-microstep truncation. Do not conflate them.

## F8-02. A rigorous 8, 16, 32, ... microstep finite/global first-jet hierarchy

The authentic eight-source impulse shell is
\(P(t)=4-2t^3-t^4-t^5\), corresponding to \(c=(4,0,0,-2,-1,-1,0,0)\). For B complete eight-tap blocks, the finite impulse polynomial and original full transfer are

\[
P_B(t)=P(t)\sum_{j=0}^{B-1}(t^8/16)^j
=(1-(t^8/16)^B)F(t),\quad
F(t)=\frac{P(t)}{1-t^8/16}.
\]

Every finite shell has \(P_B(1)=0\) because \(P(1)=0\). Since \(P'(1)=-15\), direct differentiation gives the ALL-B EXACT theorem

\[
\boxed{P_B'(1)=-16(1-16^{-B}),\qquad
F'(1)-P_B'(1)=-16^{1-B}.}\tag{F8-02}
\]

The second endpoint jet, with no fitted coefficients, is

\[
\boxed{P_B''(1)=-44\sum_{j=0}^{B-1}16^{-j}
-240\sum_{j=0}^{B-1}j16^{-j}\longrightarrow-64=F''(1).}\tag{F8-03}
\]

For \(2^k\) microsteps, \(B=2^{k-3}\). At sixteen microsteps \(B=2\), so \(P_2'(1)=-255/16\), first-jet gap \(-1/16\). At 32 microsteps B=4 the gap is \(-1/4096\); at 64 B=8 it is \(-1/268435456\). This rapidly shrinking boundary *jet* is exact source algebra, not temporal signed Fourier decay.

Mellin integration of the signed first-shell coefficients gives EXACTLY the source's finite completion

\[
\boxed{
\alpha_B=\frac1{16}\int_0^1P_B(t)\,dt
=\sum_{n=1}^{B}16^{-n}r(n),\quad
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
}\tag{F8-04}
\]

The inherited positive Gamma tail yields
\[
0<\alpha-\alpha_B=16^{-B}T_B
\le\frac{16^{-B}}{(8B+1)(8B+2)},\qquad\alpha=\pi/16.
\]

The individual inherited chiral source-tail asymptotics are
\(\alpha_+-\alpha_{+,B}
=16^{-B}(1/(32B)+O(B^{-2}))\) and
\(\alpha_--\alpha_{-,B}
=16^{-B}(-1/(32B)+O(B^{-2}))\).
Their first-order terms cancel, leaving
\(\alpha-\alpha_B=16^{-B}(1/(64B^2)+O(B^{-3}))\).
This is the previously derived real positive boundary cancellation; it is not a new proof of Weyl cancellation. A mutated impulse shell with its first coefficient increased by 1 has nonzero endpoint mass, destroying the leading-order cancellation.

At arithmetic index B=16, the corresponding full source completion uses **128** microsteps and has a first-jet gap \(-16^{-15}\), as opposed to the \(-1/16\) gap at sixteen *microsteps*.

## F8-03. The authentic four-pole numerator has a unique 2-adic zero address

Exact recombination of the original signed four-pole source gives

\[
\boxed{
r(n)=\frac{Q(n)}{D(n)},\quad
Q(n)=120n^2-89n+16,\quad
D(n)=(2n-1)(4n-1)(8n-7)(8n-3).
}\tag{F8-05}
\]

Every \(D(n)\) is an odd 2-adic unit, including for all \(n\in\mathbb Z_2\). Moreover
\[
Q(n)\equiv n\pmod2,\qquad
Q'(n)=240n-89\equiv1\pmod2,\qquad
Q(x)-Q(y)=(x-y)(120(x+y)-89).
\]

The latter factor is ALWAYS odd. Classical simple-root Hensel lifting therefore supplies exactly ONE root \(\zeta\in\mathbb Z_2\). For every ordinary integer n (indeed every \(n\in\mathbb Z_2\)):

\[
\boxed{v_2(r(n))=v_2(Q(n))=v_2(n-\zeta).}\tag{F8-06}
\]

The root is identified constructively by the unique compatible residues \(a_k=\zeta\bmod2^k\): begin \(a_1=0\), then
\[
\boxed{a_{k+1}
=a_k+2^k\big(Q(a_k)/2^k\bmod2\big).}\tag{F8-07}
\]

Exactly checked residues:

| Modulus | Unique original source root residue |
|---|---:|
| \(2^4\) | 0 |
| \(2^5\) | 16 |
| \(2^7\) | **16** |
| \(2^8\) | **144** |
| \(2^{10}\) | 656 |
| \(2^{12}\) | 1680 |
| \(2^{16}\) | 13968 |
| \(2^{24}\) | 3487376 |
| \(2^{32}\) | 2486515344 |

Thus **n=16 matches the unique zero through SEVEN binary digits but fails on the eighth**: \(Q(16)=29312=2^7\cdot229\). The numerator discriminant is exactly \(241\equiv1\pmod8\). The two algebraic roots \((89\pm\sqrt{241})/240\) are both real, but only one is integral over \(\mathbb Z_2\), namely \(\zeta\) with \(v_2(\zeta)=4\); the other has \(v_2=-3\) by Vieta's product \(2/15\). This is LOCAL algebraic branch selection, not a source-imposed real phase.

The main-inherited 2-adic source isometry is stronger than a simple numerological congruence. The new explicit address gives the exact exceptional-set census:

\[
\boxed{\{n\in\mathbb Z: v_2(r(n))\ge m\}
=\{n:n\equiv a_m\pmod{2^m}\}.}\tag{F8-08}
\]

Any interval containing L consecutive integers has either \(\lfloor L/2^m\rfloor\) or \(\lceil L/2^m\rceil\) such indices. For a dyadic epoch \([A,2A)\), \(A=2^j\), there are EXACTLY \(2^{j-m}\) when \(m\le j\), and at most one when \(m>j\). Hence high-valuation source exceptions are sparse, in a proved arithmetic sense. Deleting at most one time from an A-long source epoch changes normalized fixed-h Weyl means by at most \(1/A\) and ordered near-pair counts by at most \(2A-1\); it does NOT bound the remaining bulk.

## F8-04. TWO separate gluing stages at the original time indices n=2^k

The original on-main \(\mathbb Z_2\) particular solution theorem says
\[
\mathcal F(n)=\sum_{j\ge0}16^j r(n-j),\quad
\mathcal F(0)=0,\quad
U_n=\mathcal F(n),\quad
v_2(U_n)=v_2(n)\qquad(n\ge1).
\]
The unique-root and isometry results of the older source are credited. Parallel read-only PR #481 proves for both authentic chiral channels
\[
\boxed{v_2(r_+(n))=v_2(r_-(n))=-5-v_2(n).}\tag{F8-09}
\]

For \(n=2^k\), an elementary valuation comparison in the ORIGINAL numerator \(Q\) now yields

\[
\boxed{
v_2(r(2^k))=
\begin{cases}
k,&0\le k\le3,\\
7,&k=4\;(n=16),\\
4,&k\ge5.
\end{cases}}\tag{F8-10}
\]

For \(k\le3\), \(-89\,2^k\) is the uniquely minimal 2-adic term; at k=4 directly \(Q(16)=2^7\cdot229\); for k≥5 the constant 16 is uniquely minimal.

**First, chiral-source gluing:** Each channel has valuation \(-5-k\), and the full original forcing has valuation F8-10. The number of gained binary valuations is \(5+k+v_2(r(2^k))\), exceptionally **16** at n=16 and \(k+9\) for all k≥5.

**Second, causal-memory gluing:** For k≥5, n−1 is odd, so the old selected-source theorem gives \(v_2(16U_{n-1})=4\). Simultaneously F8-10 gives \(v_2(r(n))=4\). The EXACT original recurrence \(U_n=16U_{n-1}+r(n)\) therefore proves

\[
\boxed{v_2(16U_{2^k-1})=v_2(r(2^k))=4,\quad
v_2(U_{2^k})=k.}\tag{F8-11}
\]

This is **k−4 extra cancellation bits** at a *second*, causally coupled interface. At index 16, by contrast, forcing has valuation 7 and memory has valuation 4, so \(v_2(U_{16})=4\): the exceptional source-value cancellation does NOT itself propagate as extra state cancellation.

| Original n | Each lane \(v_2\) | Combined forcing \(v_2\) | First gain | Selected state \(v_2\) | Second gain |
|---:|---:|---:|---:|---:|---:|
| 8 | −8 | 3 | 11 | 3 | 0 |
| **16** | **−9** | **7** | **16** | 4 | 0 |
| 32 | −10 | 4 | 14 | 5 | 1 |
| 64 | −11 | 4 | 15 | 6 | 2 |
| 128 | −12 | 4 | 16 | 7 | 3 |
| 256 | −13 | 4 | 17 | 8 | 4 |
| 8192 | −18 | 4 | 22 | 13 | 9 |
| 32768 | −20 | 4 | 24 | 15 | 11 |

These are real statements about the authentic BBP source in **2-adic arithmetic**, not real-circle phase cancellation.

## F8-05. Steelman, hostile control, and missing real-place arrow

The figure-eight source and two coherent gluing interfaces are now exactly represented, but they live in DIFFERENT observation categories: (a) E² eight-microstep signed chiral/source Mellin integral, (b) rare high-valuation 2-adic source-index roots, and (c) the chronologically selected real \(e(hU_n)\). There is currently NO declared signed phase-preserving transport from (a)/(b) to (c). A source 2-adic isometry or a positive Gamma finite/global error bound does not imply Haar measure.

For every finite B, the same **unchanged four signed original poles** and chiral/Gamma boundary accept the rational changed real seed \(s_B=1/5-\alpha_B\). Its completed finite orbit satisfies
\[
U_n(s_B)+R_{n,B}=16^n/5\equiv1/5\pmod1,\qquad 0\le n\le B.
\]
Globally \(s=1/5-\alpha\) yields a coherent nonnormal completed fixed point. This REFUTES source-only boundary cancellation implying real π normality. The original marked \(U_0=0\) is retained throughout our positive source claims; the changed seed is an explicitly labelled negative control.

**NEXT real discriminator:** The inherited #475/#476 sufficient all-prefix condition is a source-selected dyadic mesoscopic collision bound \(E_{A,M_A}=o(\log M_A)\), e.g. explicit \(M_A\asymp\log A\). The Hensel census may remove a genuinely tiny exceptional set from each epoch; it does NOT control real near-pairs in the remaining bulk. The actual next theorem must bind original full Archimedean cofactor/carry dynamics to a signed loss and reject the coherent changed-seed control. Do not call a mere 16-step identity the long-missing signed inequality.

## Status and provenance

**PAPER DERIVED:** F8-01–11 under their explicitly attributed original E²/2-adic/Gamma premises; power-2 microclock classification, complete finite source endpoint jets, unique root and source-specific root addresses, the precise exceptional-set census, exact power-index valuation profile, and two-stage gluing deduction. Classical Hensel lemma is from standard p-adic theory (Keith Conrad / Vanderbilt Hensel notes), not claimed new.

**FINITE OBSERVED:** Previously 8/8 original eight-step tests and 25/25 new independent-path local tests passed, plus fresh preregistered original n=8192/16384/32768 modular holdouts and symbolic exact derivative/discriminant checks. They do not convert finite runs into universal theorems; proofs above are algebraic.

**REFUTED:** a new primitive chirality at microstep 16; equating sixteen microsteps with BBP index 16; using source-only gluing or 2-adic high precision as evidence of real selected π normality.

**UNVERIFIED:** genuine marked-zero-seed all-scale real signed Weyl saving/near-collision inequality; base-16 π normality and RH remain OPEN. No independent peer review or new compiled Lean theorem is claimed.