# ATOM IV — Constructive finite-to-Archimedean Tate phase and CRT multi-observer coherence

**Branch:** research/observer-tate-bijective-descent-2026-10-15. **Source:** rational number field Q, real additive character e^(-2pi i x), local p-adic characters e^(+2pi i {x}_p), and original discrete prime-place arithmetic. All integer/rational receipts are exact; no numerical phase samples, no zero-location information, no sign inference. **RH PROVED: NO.**

## 1. Tate's additive global character from actual finite SUCC arithmetic

Let q=a/b be any reduced rational, b>0. For each genuine prime p dividing b write b=p^k u_p with gcd(u_p,p)=1. The p-adic fractional part of q in [0,1) is
\[
\{q\}_p=\frac{v_p}{p^k},\qquad
v_p\equiv a u_p^{-1}\pmod{p^k},\quad 0\le v_p<p^k.
\]
At all p not dividing b, q∈Z_p and the local additive character is trivial.

**Exact finite-to-real diagonal phase conservation:**
\[
\boxed{
\sum_{p\mid b}\{q\}_p-q\in\mathbb Z
\quad\Longrightarrow\quad
e^{-2\pi i q}\prod_p e^{2\pi i\{q\}_p}=1
\qquad\forall q\in\mathbb Q.
}\tag{ATOM-IV-PRODUCT}
\]
**Proof directly by Chinese remainders:** multiply the finite fractional sum S by b:
\[
bS=\sum_{p^k\parallel b} v_p(b/p^k).
\]
For a selected modulus p^k, every other term is divisible by p^k. The selected term equals a modulo p^k because v_p is the inverse-unit residue of a/(b/p^k). Thus bS≡a mod every p^k dividing b. The moduli are coprime and multiply to b, so bS−a is an integer multiple of b, i.e. S−q∈Z. No analytic continuation, Poisson summation, Gaussian integral, prime infinity limit, or RH input is used. This is the true mathematical common-basis transport of the p-local and real additive phases; wrong real orientation breaks it.

**Example:** q=1/6. The local p=2 fractional part is 1/2; p=3 part is 2/3; S=7/6 and S−q=1. Reversing the real sign instead yields S+q=4/3, not an integer. Omitting the actual p=3 place gives 1/2−1/6=1/3, also not an integer. These are separate exact source-mutation controls.

**What this proves:** a coherent finite arithmetic source fixes the global additive character's relative finite/real phase convention, and the global character is trivial on the diagonally embedded Q. It is an actual Tate compatibility ingredient, not a mere similarity between finite and Archimedean phases. This does NOT construct the real Gaussian or full adelic Poisson theorem, and it does not constrain zeros.

## 2. Two and three real-prime observers: dual CRT frequency transport

For coprime moduli a,b (in the source-specific code these are powers of TWO distinct genuine primes), let N=ab and identify
\[
\mathbb Z/N\cong\mathbb Z/a\times\mathbb Z/b
\]
by residue reduction. The CRT idempotents are
\(e_a=b(b^{-1}\bmod a)\), \(e_b=a(a^{-1}\bmod b)\).
Therefore the global additive character transported to the two locally modeled observers satisfies
\[
\chi_{N,k}(x)=
\chi_{a,k(b^{-1}\bmod a)}(x\bmod a)\,
\chi_{b,k(a^{-1}\bmod b)}(x\bmod b).
\tag{ATOM-IV-CRT2}
\]
The inverse factors are not optional. For a=2,b=3, N=6, k=1 the correct local frequency indices are (1,2), NOT the naïve (1,1). Taking a non-symmetric 3-residue input provides an exact cyclotomic counterexample to the naïve gluing.

More generally, for pairwise coprime m_1,...,m_d, with N=product m_j, the unique source-canonical dual label at the j-th observer is
\[
k_j=k\big((N/m_j)^{-1}\bmod m_j\big)\pmod {m_j}.
\]
For a pure-tensor finite source function \(f(x)=\prod_j f_j(x\bmod m_j)\), CRT and Haar counting show
\[
\boxed{\mathcal F_N f(k)=\prod_j\mathcal F_{m_j}f_j(k_j).}
\tag{ATOM-IV-CRTn}
\]
The right side is evaluated in one common cyclotomic field via the canonical root embeddings. This **tensor-natural Fourier theorem** follows exactly from the CRT bijection x↔(x_j), its inverse x=sum_j e_j x_j, and independence of the finite counting Haar product.

The new code checks every global Fourier coefficient by (i) direct exact Q(zeta_N) cyclotomic Fourier and (ii) the separately transported local Fourier product, including all 2-place configurations for p=2,3,5 with p-power exponents, and the 3-place cube p=(2,3,5), N=30, under all three orderings. Source ambiguity is rejected at duplicate primes, composites acting as fake primitive places, malformed/floating values and noncoprime factorizations. Joint modulus N=6 or 30 is a lawful observation carrier, **not** a new primitive Euler local place.

## 3. Implications for recursive SUCC and RH proof design

Finite observer models can be fused in one canonical additive Fourier model when they carry correct CRT-dual phase. The interobserver map is a natural, source-derived morphism. The rational diagonal character then couples all finite nontrivial local phases to the real place with a fixed sign, giving a legitimate arithmetic source-interface invariant.

**This is a hard boundary, not a sign mechanism.** Additive Fourier self-duality and the product character do not imply multiplicative Euler-source positivity. Tate's global Poisson formula, local epsilon factors for all multiplicative characters, full Weil quadratic pairing and all-test Hilbert positivity remain separate. A candidate positive Weil Hilbert factor must preserve these transport identities AND prove a source-specific quadratic inequality that survives all new cross-terms.

The immediate next instrument is to assemble restricted adelic pure tensors with a genuine real Schwartz source, check invariance under all CRT grouping maps and the global additive character, then establish diagonal Poisson from controlled source sums. A second, RH-facing team must supply the missing PSD growth/Schur law for the original Weil test algebra, not infer it from these successful Fourier squares.

**Verdict: CLASSICAL/PROVED additive phase and CRT tensor transport, implemented as exact source algorithms; full Tate + RH still UNVERIFIED.**
