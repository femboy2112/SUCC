# Green–Tao meets synchronized SUCC prime clocks

**2026-10-19 · Research stacked on PPC #185, itself stacked on RAD/RIS #184.**
Claims are *classical/paper-derived*, *external theorems*, *finite exact observations*, or *unverified hypotheses* as separately labeled below. Academic priority not established. ABC OPEN; RH OPEN; original signed Suzuki S4 OPEN.

## GTC-01 — Exact wheel size and synchronized support (CLASSICAL)

Choose a finite nonempty set Q of distinct genuine prime clocks. Define W=prod(q in Q)q; SUCC advances a q-clock by n mod q and its target is phase 1. The Chinese remainder theorem gives

\[
 \forall q\in Q,\ p\bmod q=1
 \iff p\equiv1\bmod W
 \iff \boxed{p=1+Wt,\quad t\ge1}.
\]

When the endpoint p is prime, p>=W+1 and

\[
 \boxed{\log(p-1)=\sum_{q\in Q}\log q+\log t}.
\]

For q_j=a+jh, j=0,...,k-1, a genuine k-prime arithmetic progression, the fully aligned endpoint has

\[
 \boxed{p=1+t\prod_{j=0}^{k-1}(a+jh)},\qquad
 a^k\le W\le(a+(k-1)h)^k.
\]

This quantitatively answers why synchronized endpoints are large: periods multiply. The variable t is the wheel multiplier, *not necessarily RIS(p-1)* unless Q is the entire distinct-prime support of p-1.

**Specific source:** p=870871 is independently certified prime and

\[
 p-1=870870=2\cdot3\cdot5\cdot7\cdot11\cdot13\cdot29.
\]

These seven clocks make W=870870, t=1, rad(p-1)=870870, ris(p-1)=1. The support contains two distinct prime-clock 3-term progressions (3,5,7) and (3,7,11), but this shape does not independently imply p prime. Here phi(W)=161280 and W/phi(W)=870870/161280≈5.39974.

## GTC-02 — Exact W-tricked prime source and the analytic boundary (EXTERNAL PNT-AP)

Let Lambda_P(m)=log(m) when m is prime and 0 otherwise. With **fixed** W and reduced residue 1 mod W, put

\[
 f_{W,1}(n)=\frac{\phi(W)}{W}\Lambda_P(Wn+1).
\]

The external prime number theorem in arithmetic progressions entails

\[
 \frac1N\sum_{n\le N} f_{W,1}(n)\longrightarrow1,\qquad
 \#\{p\le x:p\equiv1\bmod W\}\sim\frac{\operatorname{Li}(x)}{\phi(W)}.
\]

Consequently the limiting fraction **among all primes** in the fixed class is 1/phi(W), while relative enrichment **among integers 1+Wt** is W/phi(W)=prod_{q in Q}(1-1/q)^(-1) in the asymptotic comparison. This is the standard W-trick, not a probability certificate for the single integer W+1. For p≈W, including 870871, fixed-W asymptotics provide no controlled finite error. If W grows with x, no uniform modulus theorem is imported here.

A normalized one-point prime mean is NOT a proof of multi-point prime arithmetic progressions. Green–Tao's transference and pseudorandom majorants are independent external proof machinery.

## GTC-03 — A faithful and fully transported finite Fourier phase (PROVED LOCAL)

Fix the canonical orientation S:n→n+1 and the phase-1 origin. For each q in Q, choose the standard character chi_q(n)=exp(2πi(n-1)/q). Their product is

\[
 \Phi_Q(n)=\prod_{q\in Q}\chi_q(n)
 =\exp(2\pi i\, h_Q(n-1)/W),\quad
 h_Q=\sum_{q\in Q}W/q.
\]

For each q dividing W, h_Q mod q equals W/q mod q and is nonzero. Since W is squarefree, gcd(h_Q,W)=1. Thus Phi is a *faithful* cyclic W-character and

\[
 \boxed{\Phi_Q(n)=1\iff W\mid n-1},\qquad
 \boxed{1_{W\mid n-1}=\frac1W\sum_{j=0}^{W-1}\Phi_Q(n)^j}.
\]

SUCC rotates the character by the **declared primitive root** exp(2πi h_Q/W). The executable does not compare floating phases: it keeps exact integer label (h_Q(n-1) mod W). There are W distinct phases and the minimal separation in the complex plane is 2sin(π/W). A source observer needs at least ceil(log₂ W) bits to identify an arbitrary state uniquely; one complex-valued diagram does not grant infinite free resolution.

For Q=(2,3,5,7,11,13,29): W=870870, h_Q mod W=329629, gcd=1; the label carries 20 bits of finite state discrimination. This is genuine finite Fourier transport—not a quantum, Weil, or RH phase.

## GTC-04 — Necessary local divisibility of prime-progression steps (PROVED LOCAL)

Let ℓ≥2 and suppose

\[
 p_j=1+W(t+jd),\qquad j=0,\ldots,\ell-1,
\]

are all primes **strictly larger than ℓ**. If r≤ℓ is prime but r does not divide W, then r must divide d. Otherwise Wd is invertible modulo r, and among ℓ consecutive progression terms at least one is divisible by r, impossible since that prime endpoint exceeds r.

Put

\[
 \boxed{D_{\ell,W}=\prod_{\substack{r\le\ell\\r\text{ prime}\\r\nmid W}}r.}
\]

The exact necessary gate is D_{\ell,W}|d. Equivalently, the endpoint difference Δ=Wd must be divisible by lcm(W,prod_{r≤ℓ prime}r). **This is necessary, not sufficient** for primality.

An instructive exception: the five clock primes (5,11,17,23,29) form an AP with difference 6, even though 5 does not divide 6. This does not violate the theorem because the first term is the prime 5 itself, whereas the endpoint theorem explicitly assumes every term is larger than ℓ.

## GTC-05 — Local singular-series factors, NOT the prime-tuples conjecture

For fixed W, ℓ,d and the varying t, the linear forms L_j(t)=1+W(t+jd) have an exactly computable number ν_r of local forbidden t residues modulo each prime r:

\[
 \nu_r=\begin{cases}
 0,&r\mid W,\\
 1,&r\nmid W,\ r\mid d,\\
 \min(\ell,r),&r\nmid Wd.
 \end{cases}
\]

The Hardy–Littlewood **local** factor is

\[
 \boxed{\beta_r=\frac{1-\nu_r/r}{(1-1/r)^\ell}}.
\]

At all sufficiently large r not dividing Wd, β_r=1+O(r^(-2)); the Euler product has a convergent positive value exactly if there is no locally forbidden r. This is equivalent here to D_{\ell,W}|d. A positive factor/product does **not** establish the number of prime values of the fixed-d forms, or even their infinitude for ℓ≥2. That would require a major open prime-tuple result. An independent test enumerates all t mod r and checks ν_r against the formula, with deliberately forbidden d=1 controls.

## GTC-06 — A two-sided prime arithmetic-progression theorem (CLASSICAL COROLLARY, EXTERNAL Green–Tao + PNT-AP)

**Theorem.** For any k,ℓ≥2 there exist k primes q_i in an arithmetic progression and ℓ primes p_j in another arithmetic progression such that every p_j exceeds the q_i and

\[
 \boxed{p_j\bmod q_i=1\quad\text{for all }i,j.}
\]

Indeed, apply Green–Tao to choose any k-term prime arithmetic progression Q. Put W=prod Q. By the fixed-modulus PNT-AP, the subset A of primes p≡1 mod W has relative prime density 1/phi(W)>0. The **positive-relative-density subset** version of Green–Tao then gives infinitely many ℓ-term arithmetic progressions of primes entirely inside A. Choose one far enough above max Q. Their common difference is necessarily a multiple of W.

This proof **uses Green–Tao as an external theorem**, not a reconstructed Green–Tao proof. It does not fix the endpoint step in advance, quantify its least occurrence, or give uniformity as W grows with p. It also does not solve any RH, ABC or signed completed Weil positivity problem.

## GTC-07/08 — Concrete finite prime-grid witnesses and source-audited minimality

All the entries below are genuine primes verified by complete bounded trial division, not plausible primes inferred from residue tests. Every endpoint reads 1 on every declared clock.

| Prime clock AP | W | Prime endpoint AP | Δ | t-start,d | Number of phase-1 contacts |
|---|---:|---|---:|---|---:|
| 3,5,7 | 105 | 211,421,631 | 210 | 2,2 | 9 |
| 5,11,17,23 | 21505 | 989231,1118261,1247291,1376321 | 129030 | 46,6 | 16 |
| 5,11,17,23,29 | 623645 | 228254071,269414641,310575211,351735781,392896351 | 41160570 | 366,66 | 25 |

The 5×5 witness is

\[
 q_i=5+6i,\quad
 p_j=1+623645(366+66j),\qquad i,j=0,\ldots,4.
\]

For fixed Q=(5,11,17,23,29) and the explicit bound t_last≤630, the final largest prime 392896351 is the **minimum possible greatest endpoint of any five-term verified prime AP** of this wheel, as an exhaustive finite search over every locally allowed d and positive start t confirms. This does not assert a globally minimal prime pattern without its fixed source and bound. The independently implemented tests compare the full finite search to a different loop orientation and prime oracle.

Importantly p_0-1=W×366 is squarefree, while p_1-1=W×432 has 2⁴·3³. Both endpoints have the SAME declared five phase-1 clocks but different additional support and multiplicity (RAD/RIS). This is precisely the source-information boundary in the earlier RRT results.

## GTC-11 — Constant RAD and arithmetic RIS are equivalent to a squarefree primorial support condition

This is a strict strengthening of the unconstrained Green–Tao progressions. Fix length ℓ≥2, a positive integer R, and ask that the *whole* RAD/RIS chart of the ℓ consecutive predecessors R,2R,...,ℓR remain on one support fiber:

\[
 \operatorname{rad}(jR)=R,\quad
 \operatorname{ris}(jR)=j,\qquad j=1,\ldots,\ell.
\]

**Theorem (elementary, exact).** Writing M_ℓ=prod_{q≤ℓ, q prime}q, the following are equivalent:

1. rad(jR)=R for all 1≤j≤ℓ.
2. R is squarefree and M_ℓ divides R.

**Proof:** j=1 in (1) implies rad(R)=R, so R squarefree. For each prime q≤ℓ choose j=q; the equality rad(qR)=R forces q|R. Thus M_ℓ|R. Conversely if R is squarefree and includes every prime≤ℓ, then each 1≤j≤ℓ has prime support contained in that of R; rad(jR)=R and (jR)/rad(jR)=j. QED.

Now if **every p_j=1+jR is itself prime**, the AP of endpoints p_1,...,p_ℓ has constant RAD(p_j−1)=R and RIS(p_j−1)=j exactly. These are truly *flat support / linearly increasing depth* SUCC prime ladders. Their difference is R, so

\[
 \boxed{p_j=1+j\,\mathrm{RAD}(p_j-1),\qquad \mathrm{RIS}(p_j-1)=j.}
\]

If a prescribed prime-clock AP Q also must be synchronized in every p_j, the necessary support size is

\[
 \boxed{\operatorname{lcm}(W,M_\ell)\mid R,\qquad R\text{ squarefree}},
\]

where W=prod Q. This is much stronger than p_j≡1 mod W: it fixes the entire predecessor radical, not merely the selected clock residues.

## GTC-12 — Verified flat-RAD ladders of lengths 3, 4 and 5

The following are exact prime sequences checked by an independent primality oracle and full factorization of every predecessor:

| R | Verified prime ladder p_j=1+jR | Common RAD of p_j−1 | RIS values |
|---:|---|---:|---|
| 210 | 211,421,631 | 210 | 1,2,3 |
| 330 | 331,661,991,1321 | 330 | 1,2,3,4 |
| 247710 | 247711,495421,743131,990841,1238551 | 247710 | 1,2,3,4,5 |

An even more structured **5×5 clock-AP × prime-AP configuration with constant radical** uses clock primes Q=(5,11,17,23,29), a genuine five-term prime AP with difference 6, and

\[
 R=71533328790
  =2\cdot3\cdot5\cdot7\cdot11\cdot17\cdot23\cdot29\cdot2731.
\]

All factors are genuine distinct primes, and R is divisible by M_5=30 and by W=623645. Then all five numbers

\[
 \boxed{71533328791,\quad143066657581,\quad214599986371,\quad
 286133315161,\quad357666643951}
\]

are genuine primes, with common difference R. Every one of the 25 Q-clock readings is 1 **and** every predecessor has the **same full radical R** with RIS respectively 1,2,3,4,5. Complete trial division establishes each finite primality result. The wheel minimal support for these prescribed Q and ℓ=5 is lcm(W,M_5)=3741870. This example has R=3741870×19117. The extra factor 19117=7×2731 illustrates the *additional arithmetic search cost* not forced by the support lower bound.

Bounded least-R calibrations (not global theorems of least primes): the first squarefree R≥M_4 with p_j=1+jR all prime for j≤4 is R=330; for length 5, the first squarefree R≥M_5 giving all five primes is R=247710, by an exhaustive finite search with exact trial-factor and independent direct primality checks. These are finite observations, not evidence that all lengths succeed.

## GTC-13 — Green–Tao does not solve anchored flat-RAD ladders

The ordinary Green–Tao AP model uses two independent integer variables a,d and forms a+jd. Our stronger flat RAD problem fixes a=1 and varies only R in the one-variable linear forms L_j(R)=1+jR. For distinct i,j, these forms are affinely dependent; in fact

\[
 \boxed{L_j(R)-1=\frac ji\bigl(L_i(R)-1\bigr).}
\]

The main finite-complexity machinery for linear equations in primes does **not** cover this degeneracy: see Green–Tao, *Linear Equations in Primes*, Annals of Mathematics 171 (2010), 1753–1850, https://annals.math.princeton.edu/2010/171-3/p08, and Tao's lecture https://terrytao.wordpress.com/2010/06/05/254b-lecture-notes-7-the-transference-principle-and-linear-equations-in-primes/ . The corresponding infinitude assertion would be a special case of the currently open Dickson / Hardy–Littlewood prime-tuple conjecture for the variable R restricted to multiples of M_ℓ, with no prime/power exceptions hidden in the proof. Even for ℓ=2, the two forms 1+R and 1+2R are an unproved infinite prime-pair pattern; finite witnesses prove nothing about infinitude.

**Discriminating negative control:** R=210 is squarefree, includes primes 2 and 3 and so gives flat RAD for j≤4, but the fourth proposed prime 1+4·210=841=29² is composite. Thus the support criterion alone does *not* force primality, and merely citing Green–Tao is not a proof of the stronger ladder hypothesis.

**Frontier:** use the two-variable W-tricked rectangle as the solved classical comparison, and the one-variable anchored ladder as an honestly UNVERIFIED strengthened arithmetic conjecture; characterize which additional source correlations would be needed to bridge them without assuming prime-tuple theorems. This explicit split is the primary mathematical diagnostic produced by this round.

## GTC-14 — An unconditional infinite prime-rich constant-RAD fiber theorem (EXTERNAL generalized Maynard–Tao + elementary proof)

There is a rigorous intermediate result between (a) Green–Tao's arbitrary length *two-variable* progressions and (b) the open claim that **all** first ℓ anchored positions 1+jR are prime.

**Theorem (classical corollary, external Maynard–Tao generalized admissible affine-forms sieve).** Let Q be any fixed finite set of genuine primes, and m≥2. There exists an integer K≥m such that for **infinitely many positive integers R** one has:

1. R is divisible by every q∈Q and by every prime≤K.
2. Every j=1,...,K has **the same** radical:
   \(\operatorname{rad}(jR)=\operatorname{rad}(R)\) and
   \(\operatorname{ris}(jR)=j\operatorname{ris}(R)\).
3. At least m distinct indices j∈{1,...,K} make \(p_j=1+jR\) a genuine prime. Every such endpoint is phase 1 at each declared Q clock.

The chosen indices need **not** be consecutive or constitute a prime AP; R need **not** be squarefree. There is no claim that all K terms are prime or that RIS steps by 1.

**Proof.** Take K large enough that the generalized Maynard–Tao theorem holds for **any admissible K-tuple of affine-linear forms** with different positive leading coefficients. Let M_K=prod_{r≤K, r prime}r and A=lcm(M_K,prod_{q∈Q}q), a fixed positive integer. The K forms

\[
 L_j(t)=1+jAt,\qquad j=1,\ldots,K
\]

are distinct and admissible: for every prime r, the residue t=0 mod r makes **all** L_j(t)=1 mod r, so no prime r divides the product for every t. Maynard–Tao (external) therefore guarantees **infinitely many** positive t for which at least m of these K forms have prime values. Put R=At. Since every prime dividing j≤K also divides A, \(\operatorname{supp}(jR)=\operatorname{supp}(R)\), so rad(jR)=rad(R); the RIS identity follows on dividing jR by this radical. All q∈Q divide R, so each prime endpoint 1+jR reads 1 in every q-clock. Since A is fixed, infinitely many distinct t give infinitely many distinct R. QED, conditional only on the already established named external Maynard–Tao theorem, not a new hypothesis.

**Provenance and precise hypothesis.** The **general linear forms** extension is essential: the coefficients jA are unequal. Tao explicitly confirms that fixed unequal coefficients are permitted in [MathOverflow, *Does the Maynard–Tao theorem apply to general tuples of linear forms?*](https://mathoverflow.net/questions/162741/does-the-maynard-tao-theorem-apply-to-general-tuples-of-linear-forms), and a published precise formulation is Lemma 2 in [*Solutions of φ(n)=φ(n+k) and σ(n)=σ(n+k)*, International Mathematics Research Notices](https://academic.oup.com/imrn/article/2022/5/3561/5896974). The underlying sieve comes from Maynard, [*Small gaps between primes*, Annals 181 (2015)](https://annals.math.princeton.edu/2015/181-1/p07). The original theorem requires a sufficiently large K depending on m; no specific effective K or finite first R is claimed here.

**Finite source instrumentation.** The code constructs the typed affine family for bounded K and A and checks the local non-divisibility witness t≡0 mod each tested prime. It also checks the exact RAD/RIS fiber at selected finite t. For Q=(5,11,17,23,29), K=5, A=3741870: t=1 gives **zero** prime endpoints despite full local admissibility, while t=19117 gives the earlier five-prime flat-RAD witness. Those are finite outcomes; we do **not** claim Maynard's theorem guarantees 5 primes from K=5.

**Verdict:** genuinely **unconditional infinite existence of arbitrarily prime-rich constant-RAD fibers**, imported as a proven Maynard–Tao consequence; **all-K anchored prime ladders remain a Dickson-type open target**. This distinction is stronger and more informative than declaring the entire one-variable pathway impossible or solved.

## GTC-09/10 — Crucible, failure receipts, and the next discriminatory probe

- **Composite fully locked candidate:** 30030+1=30031=59×509. No wheel phase certifies primality.
- **Locally forbidden fixed step:** for W=623645, ℓ=5, d=1 forces an endpoint divisible by 2 or 3; exact ν_r produces zero singular factor.
- **Locally admissible but composite:** choosing d divisible by 6 only removes small local obstructions; it does not force all five endpoint values prime.
- **Fake q source:** nonprime, reordered, duplicate or oversized clock sources are rejected by typed inputs, not silently treated as independent prime phases.
- **Fake probability:** finite positive local singular-series product is a diagnostic, not a truth probability, a proved prime-tuple asymptotic, or Green–Tao's proof.
- **Wrong analytic quantifiers:** prime equidistribution with fixed W is not a valid uniform theorem for an adversarial sequence W(x) comparable to x.
- **ABC firewall:** the primitive triple 1+(p−1)=p always has quality <1, even at perfectly synchronized primes. These clocks do not supply any epsilon-uniform ABC inequality.
- **RH firewall:** the positive phase Fourier idempotent and local Euler factors are not source-authenticated completed Weil/Suzuki positivity. The original signed S4 obstruction remains OPEN.

**Verdict-changing research probes:** (a) frozen-clock windows versus changing W(x), with independently proved error terms; (b) analytic estimation of actual multilinear W-tricked prime correlations using source-faithful transference, not an assumed positive covariance; (c) matched non-Euler or composite-clock mutations of any proposed source-derived inequality; (d) derive a nontrivial uniform additive-multiplicative inequality for primitive ABC triples that survives the 1+(p−1)=p null case. RH- and ABC-strength claims remain UNVERIFIED.

## Reproduction and external provenance

Code: observational_succ/green_tao_clock_ap.py; exact independent oracles: tests/test_green_tao_clock_ap.py; repeatable source JSON: scripts/green_tao_clock_ap_probe.py; claim register: docs/CLAIM_SUPPLEMENT_GREEN_TAO_CLOCK_AP.md.

Commands:

~~~sh
python -m unittest discover -s tests -p 'test_green_tao_clock_ap.py' -v
python scripts/green_tao_clock_ap_probe.py
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
~~~

Primary external sources:
- Ben Green and Terence Tao, *The primes contain arbitrarily long arithmetic progressions*, Annals of Mathematics 167 (2008), 481–547, https://annals.math.princeton.edu/2008/167-2/p03 . The positive relative density subset theorem is necessary for GTC-06.
- Terence Tao, *Linear equations in primes*, https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-142-tao7-higher-book-05june2012.pdf . External source for normalized W-trick and transference scope.
- Terence Tao, *The prime tuples conjecture, sieve theory, and the work of Goldston–Pintz–Yıldırım, Motohashi–Pintz, and Zhang* (2013), https://terrytao.wordpress.com/2013/06/03/the-prime-tuples-conjecture-sieve-theory-and-the-work-of-goldston-pintz-yildirim-motohashi-pintz-and-zhang/ . Singularity factors and the **conjectural** fixed-step limit.
- Terence Tao, *Narrow progressions in the primes* (2014), https://terrytao.wordpress.com/2014/09/04/narrow-progressions-in-the-primes/ . Why a variable-step theorem is different from the stronger fixed-step question.
- Dirichlet's theorem, fixed-modulus PNT-AP, CRT, Fourier character orthogonality and Bertrand are external classical dependencies. No sampled finite experiment is presented as a universal proof.
