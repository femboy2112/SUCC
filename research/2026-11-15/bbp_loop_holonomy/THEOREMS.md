# OPERATION BBP — causal return holonomy, Archimedean phase excitation, and source passports

**2026-11-15. Research-only.** This note is an additive continuation of SUCC draft [#646](https://github.com/femboy2112/SUCC/pull/646), and inherits the original four signed poles, real BBP identification, and literal `U_0=0`. **Base-16 normality of pi, R0, signed all-shell saving, quantum Higgs production and physical energy quantization remain unproved.** The new tests certify finite exact arithmetic, not the infinite real limit. Existing source provenance is unchanged.

## 0. Hypothesis, source, carrier, and refusal of free energy

User's strongest operational idea: a low-resolution carrier may return to the same 2-adic state after a finite causal loop, while the source-selected Euclidean-circle phase fails to return. The unresolved coupling must then appear as a *quantifiable defect*; source-conditioned phase response, measured coherently across time, might be more revealing than a positive Gram norm. A discrete higher-register winding could supply a quantized **phase label**, although it does not itself license a quantum-particle or thermodynamic interpretation.

Let

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}
=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)},
\quad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]

The *unreduced* \(U_n\in\mathbb Q\cap\mathbb Z_2\) retains integer winding. For the real completion, define

\[
x=\pi/16,\qquad T_n=\sum_{j\ge1}16^{-j}r(n+j)>0,\qquad
z_n=\{U_n+T_n\}=\{16^n x\}.
\]

The classical real BBP identity and pi irrationality are imported, not re-proved. SUCC's original source Green estimates give \(T_n<r(n+1)/15\), and for n>=1 the stronger \(T_n<1/(64n^2)\). All rational phase estimates below use the former bound without a pi-digit file. Set \(e(t)=\exp(2\pi i t)\), \(\|t\|=\min_{m\in\mathbb Z}|t-m|\), and \(|2^a v|_2=2^{-a}|v|_2\).

## LH-01 — closed 2-adic loop, nonzero source-specific higher-register holonomy (PAPER-PROVED; no BC-0 dependence)

For any integer \(k\ge1\), let \(q=16^k\). For all \(n\ge k+1\),

\[
\boxed{U_{n+q}\equiv U_n\pmod q,\qquad
J_{n,k}:=\frac{U_{n+q}-U_n}{q}\pmod{16}
=\begin{cases}11,&n\equiv0,1\pmod4,\\3,&n\equiv2,3\pmod4.\end{cases}}\tag{LH1}
\]

In particular, \(J_{n,k}\) is an odd 2-adic unit, hence

\[
\boxed{v_2(U_{n+q}-U_n)=4k,\qquad |U_{n+q}-U_n|_2=q^{-1}.}\tag{LH2}
\]

**Finite original-source proof, independent of the unreviewed infinite 2-adic zero anchor.** The original rational forcing is defined throughout \(\mathbb Z_2\) since its rational denominator is odd for every 2-adic input. The exact zero-seeded history is

\[
U_n=\sum_{j=0}^{n-1}16^j r(n-j).
\]

For \(n\ge k+1\), truncate both \(U_n\) and \(U_{n+q}\) after \(j=k\), modulo \(16q=16^{k+1}\). Their difference is

\[
U_{n+q}-U_n\equiv\sum_{j=0}^k16^j[r(n+q-j)-r(n-j)]\pmod{16q}.
\]

Each bracket is divisible by \(q\) in \(\mathbb Z_2\), because the rational forcing is 2-adically 1-Lipschitz. After division by \(q\) modulo 16, all terms with \(j\ge1\) vanish. For a rational function with 2-adic integral coefficients and odd denominator, the difference quotient satisfies

\[
\frac{r(t+q)-r(t)}q\equiv r'(t)\pmod {16}\qquad(q\equiv0\pmod{16}).
\]

Write \(P=120t^2-89t+16\), \(D=(2t-1)(4t-1)(8t-7)(8t-3)\), and \(L=P'D-PD'\). The explicit polynomial certificate in `audit_algebra.py` verifies, **coefficientwise in** \(u\),

\[
L(4u+j)-c_jD(4u+j)^2\equiv0\pmod{16},\quad
(c_0,c_1,c_2,c_3)=(11,11,3,3).
\]

Since \(D\) is odd, \(r'(t)=L/D^2\equiv c_{t\bmod4}\pmod{16}\). This proves LH1. It is a genuine **nontrivial lift** of a loop closed in the quotient \(\mathbb Z_2/q\mathbb Z_2\) to the next level \(\mathbb Z_2/(16q)\mathbb Z_2\). The phase orientation is exactly

\[
\boxed{\omega^{J_{n,k}}=\omega^3(-1)^{\lfloor n/2\rfloor},\quad\omega=e^{2\pi i/16}.}\tag{LH3}
\]

**Seed firewall:** The high-depth loop jet is also unchanged by any *2-adically integral rational seed* because \(16^n s\) vanishes modulo \(16q\) for \(n\ge k+1\). It identifies the original forcing, **not** by itself the selected zero seed or the real pi phase. The combined real-circle observer below must keep the original zero-source passport. If one accepts the independent BC-0 root/log paper proof in #646, LH1 extends to all \(n\ge0\); this extension is not required for the theorem above.

## LH-02 — sharp carrier-loop / circle-phase mismatch (CLASSICAL; universal expanding circle)

Let \(b\ge2\) and \(y\in\mathbb R/\mathbb Z\) have **no terminating radix-b iterate**, meaning \(b^m y\ne0\pmod1\) for every integer \(m\ge0\). This includes every irrational \(y\). Then for each \(n_0\ge0\) there is \(n\ge n_0\) such that

\[
\boxed{\|b^n y\|\ge\frac1{b+1}.}\tag{LH4}
\]

**Proof.** Suppose \(\|b^n y\|<1/(b+1)\) for every \(n\ge n_0\). Let \(v_n\in(-1/(b+1),1/(b+1))\) be the centered representatives. Since \(v_{n+1}\equiv b v_n\pmod1\), the difference \(bv_n-v_{n+1}\) is an integer of absolute value \(<(b+1)/(b+1)=1\), hence is zero. Then \(v_{n+j}=b^jv_n\) for all j; boundedness forces \(v_n=0\), so \(b^{n_0}y=0\pmod1\), contradicting the nontermination hypothesis. Sharpness: \(y=1/(b+1)\) alternates exactly between \(\pm1/(b+1)\). QED.

For **original BBP** set \(b=16\), \(x=\pi/16\) (irrational) and \(y_q=(16^q-1)x\). Because \(y_q\ne0\pmod1\) for every integer \(q\ge1\), LH4 implies for every q and every starting observation n0 a time \(n\ge n_0\) with

\[
\boxed{\|z_{n+q}-z_n\|\ge1/17,\qquad
|e(z_{n+q})-e(z_n)|^2\ge 4\sin^2(\pi/17)>0.}\tag{LH5}
\]

A terminating rational, e.g. \(y=1/16\), is an essential excluded control: after one step its entire future orbit is zero and no late pulse exists. The real metric threshold is **universal for irrational radix-16 expanding orbits**; the original BBP specificity is the simultaneous closed 2-adic source loop LH1. This is a guaranteed *eventually observed pulse*, not a positive lower time-density, an average, a normality theorem, or a physical particle detection.

## LH-03 — quantitatively singular observation transport (PROVED from LH-01 + LH-02)

For each \(k\ge1\), q=16^k, take \(n_0=k+1\) in LH5. At the selected time n, LH2 and LH5 hold together. Hence

\[
\boxed{\sup_{n\ge k+1}\frac{\|z_{n+q}-z_n\|}{|U_{n+q}-U_n|_2}\ge\frac q{17},}\tag{LH6}
\]

and

\[
\boxed{\sup_{n\ge k+1}
\frac{|e(z_{n+q})-e(z_n)|^2}{|U_{n+q}-U_n|_2^2}
\ge 4q^2\sin^2(\pi/17).}\tag{LH7}
\]

Thus a circle observation of the exact original arithmetic carrier on this forward history cannot obey any global uniform Lipschitz or positive-Hoelder modulus as a map from the 2-adic metric to the real circle metric. In fact **no continuous map** \(g:\mathbb Z_2\to\mathbb T\) can agree with \(g(U_n)=z_n\) at all sufficiently late n: uniform continuity would make all q-return separations small for sufficiently large q, contradicting LH5 arbitrarily late. This conclusion does not require BC-0, since LH1 applies at sufficiently late times.

**Classification for the pure integer clock.** A circle orbit \(n\mapsto\{16^n x\}\) admits a continuous extension \(g:\mathbb Z_2\to\mathbb T\) if and only if \((16^{16^k}-1)x\in\mathbb Z\) for some k, equivalently its exact orbit is periodic with a period dividing a power of two. Necessity is the above small-return argument plus LH4; sufficiency defines the locally constant map \(g(t)=\{16^{t\bmod 16^k}x\}\). The real pi orbit is irrational and cannot admit such a continuous extension.

**What is not shown:** a physical divergence in joules, an energy eigenvalue, infinite physically extractable work, a positive mean excitation density, or Weyl saving.

## LH-04 — a bounded *detection horizon* from a genuine pi arithmetic input (CLASSICAL IMPORT; non-effective onset)

Published Zeilberger–Zudilin (2020) proves the irrationality measure \(\mu(\pi)\le7.103205334137\ldots\) (https://doi.org/10.2140/moscow.2020.9.407). The same exponent applies to \(x=\pi/16\). For any \(a>\mu(\pi)-1\), there exists a constant \(c_a>0\), **not extracted by this note**, such that

\[
\|M x\|\ge c_a M^{-a}\qquad\text{for all integers }M\ge1.
\]

Fix \(q\ge1\) and the initial observation \(n_0\). Put \(M=16^{n_0}(16^q-1)\). If no LH5 pulse occurs in the next L steps, the no-integer-winding proof forces \(\|Mx\|<16^{-L}/17\). The Diophantine inequality contradicts this as soon as

\[
L>a(q+n_0)+C_a,
\]

where the finite constant \(C_a\) only depends on \(x,a\). Therefore

\[
\boxed{\exists n:\quad n_0\le n\le n_0+\lceil a(q+n_0)+C_a\rceil,\quad
\|z_{n+q}-z_n\|\ge1/17.}\tag{LH8}
\]

For example \(a=6.2\) is admissible using the imported numerical bound, and \(n_0=k+1\) gives a time-horizon \(6.2\,16^k+7.2(k+1)+O(1)\). **This is an existence bound with a non-effective additive constant, not a practical numerical schedule or an asymptotic density result.** A generic irrational number of infinite irrationality measure does not inherit this linear-in-q horizon.

## LH-05 — full odd-prime CRT phase passport closes the *real* rational loop (CLASSICAL; source-attached)

The original \(U_n=m_n+b_n/d_n\), where \(m_n\in\mathbb Z\), \(d_n\) odd, \(0\le b_n<d_n\), and gcd(b_n,d_n)=1 when b_n is nonzero. Its denominator divides an lcm of the original source denominators through n; hence each prime divisor of \(d_n\) is odd and \(\le8n\). For each \(p^{v_{p,n}}\Vert d_n\), set

\[
k_{p,n}\equiv b_n\big(d_n/p^{v_{p,n}}\big)^{-1}\pmod{p^{v_{p,n}}},
\qquad 0\le k_{p,n}<p^{v_{p,n}}.
\]

CRT gives the **exact integer winding** \(L_n\in\mathbb Z\):

\[
\boxed{\frac{b_n}{d_n}=\sum_{p^{v}\Vert d_n}\frac{k_{p,n}}{p^v}-L_n.}\tag{LH9}
\]

Consequently

\[
\boxed{e(z_n)=e(T_n)\prod_{p^{v}\Vert d_n}e(k_{p,n}/p^v).}\tag{LH10}
\]

For q=16^k, the real return-loop phase is the **time-correlated global odd-prime product**

\[
\boxed{\Phi_{n,q}=e(z_{n+q}-z_n)
=e(T_{n+q}-T_n)\prod_{p\text{ odd}}
 e\!\left(\frac{k_{p,n+q}}{p^{v_{p,n+q}}}-\frac{k_{p,n}}{p^{v_{p,n}}}\right),}\tag{LH11}
\]

where absent prime terms are zero. This product is finite at every source time; it is not a product of independently sampled prime laws. The *arithmetic 2-adic register* is separately

\[
U_n\pmod q\equiv m_n+b_n d_n^{-1}\pmod q.
\]

**All of the following are load-bearing and distinct:** the original forcing pole genealogy, the unreduced integer carry m, the odd conductor, the prime-local CRT residues, the CRT winding L, the real future Green tail, and the literal zero seed. The preceding two formulas are not a proof of cancellation; they are an authenticated, arithmetic source decomposition of the exact circle holonomy. They identify the missing candidate: a signed bound on the *correlated full prime product* (not an independent-prime approximation).

## LH-06 — a phase-labelled, two-time return interferometer (EXACT source instrument)

With q=16^k, \(n\ge k+1\), \(\omega=e(1/16)\), define

\[
\boxed{\mathfrak A_{n,k}=\omega^{J_{n,k}}(\Phi_{n,q}-1),\quad
\mathfrak E_{n,k}=|\mathfrak A_{n,k}|^2=|e(z_{n+q})-e(z_n)|^2.}\tag{LH12}
\]

This combines (a) the **quantized source lifting character** \(\omega^{11}\) or \(\omega^3\), (b) two times n and n+q chosen by the closed coarse carrier clock, (c) the actual zero-selected real circle metric, and (d) the full odd-prime + Green phase passport. LH5 gives a nonzero observable excursion at arbitrarily late source times at every k; LH7 gives the scale-amplified response.

A detector that records only \(|\mathfrak A|^2\) discards the source phase. A detector that averages only \(\omega^{J}\Phi\) produces a **false negative for the coherent wrong seed**, because the phase \(\omega^{J}\) averages to zero over four source-time classes even when \(\Phi\equiv1\). A valid interferometer therefore retains **both** the unweighted complex reference \(\Phi\) and the mod-4 source-labelled quadratures. For a shell B divisible by 4, their sums and differences reconstruct the separate source-time sectors exactly. This is real two-time phase correlation, not a positive Gram norm claiming automatic arithmetic randomness.

**Normality relation (conditional).** For every fixed q,h nonzero, if x is base-16 normal then \(B^{-1}\sum_{n=B}^{2B-1}\Phi_{n,q}^h\to0\), since \(\Phi^h=e(h(16^q-1)16^n x)\), and each mod-4 source sector separately tends to zero (progression normality). The converse for one fixed q,h is NOT asserted, and none of these signed limits is proved for original pi. Moving q, high modes, and selected stopping times demand separate uniformity estimates; they cannot be inferred from fixed-parameter normality.

## LH-07 — finite original-pi and hostile receipts (CERTIFIED FINITE, not an asymptotic claim)

The standalone `loop_probe.py` uses the exact four-pole source in `fractions.Fraction`, retaining **unreduced rational lifts for 2-adic calculations**. Its original-source T_n enclosures are exact rational intervals. It independently checks both source-clock jet and circle-distance lower bound at these preregistered finite cases:

| Carrier clock period q | Index n (n>=k+1) | Rigorous real-circle distance lower bound (decimal approximation) | Jet mod 16 |
|---|---:|---:|---:|
| 16 | 2 | > 0.07174716 | 3 |
| 256 | 3 | > 0.09991618 | 3 |

Both exceed 1/17. `FINITE_REPORT.json` saves the **full exact rational lower bounds**, source bracket widths, source fingerprint, source/CRT passports and failure calibrations; these decimals are explanatory approximations only. The coherent same-forcing wrong *real* seed s=-x gives \(z_n=0\) and \(\mathfrak E=0\) at every n,k, but violates the authentic zero-seed passport. The rational periodic source point \(x=1/(16^q-1)\) likewise gives \(\Phi=1\), and the rational point \(x=1/[17(16^q-1)]\) saturates the 1/17 universal threshold. A nonnormal irrational Liouville-type source point may have the same guaranteed intermittent excursions as pi, so **the pulse is not sufficient for normality**. Mutating the original 4/(8n−7) pole to 3/(8n−7) breaks the all-depth original zeroed return signature already modulo 16.

### Two failures deliberately recorded during construction

1. The first attempted comparison of 2-adic residue to the *real-reduced* state was false: reducing modulo 1 loses integer winding m_n. Repair: compare only the **unreduced rational U_n** to its 2-adic residue. The control is retained as `test_unreduced_winding_is_load_bearing`.
2. A preliminary mutant-test helper assumed the changed pole would preserve the original q-loop closure. It does not. Repair: explicitly test that the mutant fails closure, rather than making a jet division on a nonexistent mutant loop. Both corrections preceded the final PASS receipt.

## Conjecture, obstruction and the next verdict-changing probe

**CONJECTURED — source-driven phase transduction.** The original source's full odd-prime/CRT/real-tail history, conditioned on the 2-adic lifted return orientation, may yield a *nontrivial signed time-density bound* on loop excitation and eventually a fixed-mode Weyl saving. The exact energy burst established above is a **necessary geometric response** for all irrational x, not the sought normality estimate. The finite carrier holonomy is original-four-pole specific but (at late n) seed blind. Neither can singly force normality.

**Next discriminating proof gate:** derive an arithmetic estimate for an original-zero **full-history signed covariance** of \(\omega^{J_{n,k}}\), \(\Phi_{n,q}\), and the full original odd-prime CRT product with the real Green tail—at fixed frequency and with all-epoch/shell quantifiers. Preserve an unweighted coherent reference and test wrong seed, odd-prime matched mutant, rational periodic, Liouville irrational, and newly specified source-time shells. A proof of positive collision intensity, a high-frequency selected pulse, or a finite Monte Carlo success count is not a proof of pi normality or even the Main XXV R0 target.

### Primary/source provenance

- SUCC original `observational_succ/duck_bbp.py`; Main XXV `docs/PI_NORMALITY_FRONTIER.md`, `docs/PI_FRONTIER_CONTRACT.md` and the frozen `provenance/IMPORT_MANIFEST.json` (not modified).
- SUCC draft [#646](https://github.com/femboy2112/SUCC/pull/646) BC-0..BC-7 and TT-01..TT-05; the inherited zero-anchor paper proof is explicitly **not required** for LH1..LH7 on late epochs.
- SUCC draft [#572](https://github.com/femboy2112/SUCC/pull/572): prior odd-prime cofactor/carry real-parity pressure and complement-covariance obstructions. LH9–LH11 are classical CRT source passports, not a claim of a new adelic product theorem.
- Doron Zeilberger and Wadim Zudilin, *The irrationality measure of pi is at most 7.103205334137...*, Moscow Journal of Combinatorics and Number Theory 9 (2020), 407–419, https://doi.org/10.2140/moscow.2020.9.407. The published inequality is imported; no effective constant is derived here.
- Paul Garrett, *Adele groups, p-adic groups, solenoids*, https://www-users.cse.umn.edu/~garrett/m/mfms/notes_2013-14/12_1_adeles.pdf (historical background, not an independent proof of BBP coupling).

**Claim-status boundary:** LH1, LH2, LH3, LH5, LH6 exact paper derivations with explicit hypotheses; LH4 imported number-theoretic fact plus derivation; finite source checks certified in rational arithmetic; original-zero signed all-shell real saving, R0 and pi-normality **OPEN**. No results here are a quantum Higgs process, physical energy quantization or independent blind peer review.
