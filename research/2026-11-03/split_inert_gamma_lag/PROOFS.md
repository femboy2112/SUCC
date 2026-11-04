# OPERATION GAMMA × SPLIT/INERT — original selected BBP source, mixed-character compensation and joint prime clocks

**2026-11-03 · RESEARCH ONLY · paper proofs; π base-16 normality OPEN.**

Pinned parent **SUCC PR #484** `057a68c4b4e01439e76c2050c28309a4858b9dc2`; first child preregistration commit `2235c5e00dcdfcbb96d5a9eee7709cd25f67848c`. Original four signed Mellin terms, literal `U0=0`, all canonical files, main, Lean, workflows and archives unchanged. This contribution extends but does not reclassify the results of #474/#476/#481/#484 and the staged Euler-Gamma × Gaussian odd-cofactor dossier from the immediately preceding SUCC conversation. External classical inputs are identified. No academic priority for PNT-AP, Fejér, Dirichlet characters, digamma or Tate theory is claimed.

## Immutable source and notation

For **every integer n>=1**,

    r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
    U_0=0, U_n=16 U_(n-1)+r(n).

The ORIGINAL zero-seeded canonical H/G source channels from PR #481 are

    r_H(n)=-1/(4n-3)-1/[4(2n-1)]-1/[4(4n-1)]-1/(32n),
    r_G(n)=r(n)-r_H(n),
    U_0^H=U_0^G=0, U_n^a=16U_(n-1)^a+r_a(n), U_n=U_n^H+U_n^G.

Let `e(x)=exp(2πix)` and `||x||` be circle distance to the nearest integer. The original completion identity, **inherited**, is `U_n=16^n(π/16)-T_n` with `0<T_n<1/(64n²)` for n>=1. The original scalar Mellin index and the transfer-coefficient index are distinct. The source states in this document are **unwrapped** unless `{...}` is written.

The H/G source-sector projection is a rational **linear** operation; the separate *Gaussian prime-class* splitting on the exact odd conductor is a **different** CRT decomposition. Neither gives independent random variables. Do not conflate the two!

## GL-01 — Exact geometric mixture behind the H-channel Gamma tail (PROVED)

The inherited source-specific real continuation has, for **all real s>0**,

    T_H(s)=sum_(j>=1)16^-j r_H(s+j)<0,
    -T_H(s)=integral_(0,infinity) exp(-st) Q_H(t) dt,
    Q_H(t)=1/[32(2 exp(t/4)-1)].

Expanding the **absolutely convergent positive geometric series** gives, for all t>=0,

    Q_H(t)=(1/32) sum_(j>=1)2^-j exp(-j t/4).

Tonelli then gives the exact formula

    -T_H(s)=(1/32) sum_(j>=1)2^-j /(s+j/4).           (GL-1)

The weights sum to 1, with first moment 2 and second moment 6. They form an actual geometric distribution over the SOURCE kernel's discrete shifts; this is not a random model for π's digits.

Define the *rational principal harmonic counterterm* and positive remainder

    R_H(s) = T_H(s)+1/(32s)
           = (1/32) sum_(j>=1)2^-j [1/s-1/(s+j/4)].

Every bracket is strictly positive for s>0. Consequently

    0<R_H(s)<1/(64s²),                                 (GL-2)

because `1/s-1/(s+a)=a/[s(s+a)]<a/s²`, and `E[j]=2`. This is a UNIFORM all-real-s bound, not a fitted asymptotic. Its expansion begins

    R_H(s)=1/(64s²)-3/(256s³)+O(s^-4).

Proof: expand the positive resolvent at s=infinity, using the finite geometric moments. A direct kernel certificate is: for y=exp(t/4)>=1,

    -Q_H'(t) = y/[64(2y-1)^2] <=1/64,

since `(2y-1)^2-y=(y-1)(4y-1)>=0`. Hence `0<1/32-Q_H(t)<=t/64`, and its Laplace transform is again R_H. In particular R_H is strictly completely monotone (all alternating derivatives positive), a source-specific consequence of a positive kernel. We do not infer any real Fourier equidistribution from it.

**Exact rational finite oracle:** truncating (GL-1) after J terms has a positive omitted tail smaller than `2^-J/(32s)`. No numerical π or analytic continuation is needed for this enclosure.

## GL-02 — All-character, all-prefix Gamma-compensated SOURCE transport (PROVED)

The inherited exact real channel constants are

    α_H= -log(2)/8, α_G=π/16+log(2)/8,
    U_n^H=16^n α_H-T_H(n), U_n^G=16^n α_G-T_G(n),
    T_G(n)=T_n-T_H(n).

For **arbitrary integers h,k**, set `λ=k-h` and `θ_(h,k)=kπ/16+λ log(2)/8`. Then algebra gives for every n>=1

    h U_n^H+k U_n^G
      =16^n θ_(h,k)-k T_n+λ T_H(n).

Substitute `T_H(n)=-1/(32n)+R_H(n)` and apply (GL-2) and original `0<T_n<1/(64n²)`:

    |h U_n^H+k U_n^G+λ/(32n)-16^n θ_(h,k)|
        < (|k|+|λ|)/(64n²).                          (GL-3)

This inequality is for real unwrapped numbers; no exponentials and no wrapping ambiguity in its proof. Because `|e(x)-e(y)|<=2π|x-y|` and `sum_(n>=1)n^-2<2`, it immediately implies **for every N>=1**:

    |sum_(n=1)^N e(h U_n^H+k U_n^G+λ/(32n))
      -sum_(n=1)^N e(16^n θ_(h,k))|
        <π(|k|+|λ|)/16.                               (GL-4)

The normalized sums differ by O_(h,k)(1/N). The phase counterterm is an EXACT rational number, computable directly from the source frequency labels and original time n. Without this counterterm the elementary comparison is O_(h,k)(log N) due to the genuine O(1/n) H-channel tail.

**Diagonal firewall:** if h=k, λ=0 and θ=hπ/16, this is just the inherited original π trajectory transport; no improvement in selected Weyl cancellation occurs. For offdiagonal h!=k, the completed source is the ×16 orbit of the specific irrational linear form `kπ/16+(k-h)log2/8`. No proof of base-16 normality of that linear form is asserted. Kronecker's additive-time rotation theorem is not an ×16 theorem, and no generic Haar or channel-independence statement enters (GL-4).

## GL-03 — Euler–Mascheroni is the exact long-horizon phase slip (PROVED)

For fixed h,k and λ=k-h, define the ABSOLUTELY convergent real constant

    E_(h,k)=sum_(n>=1)[-k T_n+λ R_H(n)].

For n>N, the bound in GL-3 gives

    |sum_(n>N)[-kT_n+λR_H(n)]| < (|k|+|λ|)/(64N).

The source-completed UNCORRECTED phase difference is

    h U_n^H+k U_n^G-16^n θ_(h,k)
      =-λ/(32n) -k T_n+λ R_H(n).

Summing and using `0<H_N-logN-γ<1/(2N)` proves for **every N>=1**:

    |sum_(n=1)^N[h U_n^H+k U_n^G-16^n θ_(h,k)]
      +(λ/32)log N - (E_(h,k)-λγ/32)|
      < (|k|+2|λ|)/(64N).                            (GL-5)

This realizes Euler–Mascheroni as an exact *finite-to-infinite normalization constant for the cumulative phase slippage* between the canonical H/G carrier and its completed geometric orbits. It is a statement about an ordered REAL **sum of unwrapped phase differences**, not an estimate on exponential sums or an empirical π digit frequency. The diagonal λ=0 has no logarithmic/Euler slip, reflecting the exact source-sector cancellation.

No zeta critical zeros or analytic continuation are used in (GL-1)–(GL-5).

## GL-04 — NEW exact inert-prime birth and FALSE long-window counterexample (PROVED)

Let `p=4k-1>5` be a prime, so p≡3 (mod 4); k≥2. In the ORIGINAL four-pole r(n), the FIRST p-denominator occurs at n=k, from

    -1/(8k-2)=-1/(2p).

The other original source denominators have no p pole for `1<=n<k`. Its NEXT p-denominator occurs at the integer

    b'_p=ceil(3k/2).

More precisely, if k is odd (p≡3 mod 8) then n=(3k+1)/2 and `8n-7=3p`, adding residue `+4/3` to `p*r(n)` modulo p. If k is even (p≡7 mod 8), then n=3k/2 and `8n-3=3p`, adding residue `-1/3`. Earlier candidates for the other pole denominators require at least 4p, 6p or 7p as appropriate, so no smaller second event exists. All coefficients are p-units at birth and all relevant p-adic denominators have valuation exactly -1.

Therefore the authentic ZERO-SEEDED source has the clean local prime chart

    U_n = [(-1/2)*16^(n-k) mod p]/p + C_(p,n),
    C_(p,n) in Z_(p),   k <= n < ceil(3k/2).         (GL-6)

Here `-1/2 mod p` is the unique class in {0,...,p-1}. This is an exact rational real-embedding identity, not a Galois average. The original `p=47,k=12,n=18` refutes the tempting, false extension of the clean window to `[k,2k)` (also `p=43,k=11,n=17`). **This repaired error is retained as a hostile regression**, not suppressed.

The companion inherited #474 split-prime window: for `q=8j+1` prime, q>5,

    U_n = [4*16^(n-j-1) mod q]/q + C_(q,n),
    C_(q,n) in Z_(q), j+1 <= n <=4j.                (GL-7)

The coefficients and windows are ORIGINAL SOURCE-specific. They do not infer selected real cancellation.

## GL-05 — Simultaneous split/inert clean clocks and full-window exact nonrepeat (PROVED using classical PNT-AP)

Fix a rational real `1<c<3/2` and let `A` range over sufficiently large positive integers (dyadic A is allowed). Put `I_(A,c)=[A,ceil(cA))∩Z`. Define two disjoint families of ORIGINAL prime clocks

    P_+(A) = {p=8j+1 prime : ceil(A/2) <= j <= A-1},
    P_-(A,c) = {p=4k-1 prime : ceil(2cA/3) <= k <= A}.

For EVERY n∈I, every p in P_+ satisfies its clean window GL-7, and every q in P_- satisfies GL-6. This requires the SECOND inert pole at ceil(3k/2) and is why the interval cannot naively be as long as [A,3A/2).

There is an exact joint source-selected decomposition

    U_n = sum_(p in P_+) a_(p,n)/p + sum_(q in P_-) b_(q,n)/q + C_n,

where `C_n` has reduced denominator coprime to EVERY selected prime, `a_p=4*16^(n-j-1) mod p`, `b_q=(-1/2)*16^(n-k) mod q`. No class factor is averaged away.

**Classical external input:** fixed-modulus prime-number theorem in arithmetic progressions (PNT-AP), in the weighted form `theta(x;Q,a)=x/φ(Q)+o(x)` for Q=4,8. It yields

    sum_(p in P_+)log p = A+o(A),
    sum_(q in P_-)log q = (2-4c/3)A+o(A),
    log(product_(all selected primes) p)=(3-4c/3)A+o(A).     (GL-8)

For any distinct n,m∈I and integer h with `0<|h|<=A`, a hypothetical equality `e(hU_n)=e(hU_m)` implies for EACH selected prime `p` that `p|16^|n-m|-1`: all selected primes exceed |h| and the local coefficient is a p-unit. Therefore their PRODUCT divides `16^d-1`, where `1<=d<=ceil(cA)-A-1`. But `log(16^d-1) < (c-1)A log16+O(1)`.

Define the explicit critical window length

    c_*=(3+log16)/(4/3+log16)=1.405917755892234...

For **every fixed 1<c<c_*** we have `3-4c/3 > (c-1)log16`, contradicting the product divisibility for ALL sufficiently large A. Thus

    e(hU_n) != e(hU_m)
    for all distinct n,m∈I_(A,c), ALL integers 0<|h|<=A.  (GL-9)

This is **UNCONDITIONAL** given the classical PNT-AP, with an existential (not effective in this dossier) onset. It is a source-authentic selected **exact nonrepeat** result, stronger than one-prime or short-lag exclusion on this specific subwindow. It provides NO lower bound on circle distance of size 1/logA or 1/m_A; exact distinctness is much weaker than quantitative nonconcentration. It uses NO RH or zeta critical-zero positions.

Concrete robust choice c=4/3: joint weighted prime mass coefficient `11/9`, maximal radix lag coefficient `(log16)/3`; strict gap `δ=11/9-(log16)/3≈0.298026... > 2/9`, by the elementary inequality `log16<3` (since `exp(3/4)>1+3/4+(3/4)^2/2>2`).

## GL-06 — Uniform GALOIS-averaged nonalias savings across the entire subwindow (PROVED; selected real remains OPEN)

For `p∈P_+∪P_-` and a nonzero lag d=|n-m|, the p-primary difference coefficient is a p-unit times `(16^d-1)`, since the source coefficients GL-6/GL-7 are pure powers of 16 throughout I. The classical average over p-Galois automorphisms `ζ_p -> ζ_p^v` (v∈Fp*) produces Ramanujan factors

    K_p(d)=1 if p|(16^d-1), otherwise -1/(p-1).

The **joint** Galois average of pairwise phase characters is the product K(d)=∏_p K_p(d). This is an average over a DIFFERENT set of embeddings, not the actual selected real embedding v_p=1.

For every `d<=ceil(cA)-A-1`, the number of alias primes is at most

    #{p selected: p|(16^d-1)}
        <= d log16 / log(min_selected_prime)
        <= [(c-1)log16+o(1)]A/logA.

By PNT-AP the number of ALL selected primes is `[(3-4c/3)+o(1)]A/log A`. Thus for each `c<c_*` there are at least

    [δ_c+o(1)] A/log A nonalias primes,
    δ_c=3-4c/3-(c-1)log16 > 0,

uniformly across EVERY nonzero lag in I. All selected p are Θ(A), hence

    |K(d)| <= exp[-(δ_c+o(1))A],                      (GL-10)

uniformly in 1<=d<=|I|-1, and for all integer `0<|h|<=A`. This **improves the range of the averaged clock decorrelation**, using both the split and the corrected inert prime families; no Galois average is mistaken for a source-selected real bound. Our exact finite oracle computes alias counts with modular exponentiation, not assumed randomness.

**Sharp source-map firewall:** the complementary selected C_n can be changed (in a source mutant) to coherently counteract the fractional clock phases while remaining p-integral. The actual original C_n is NOT bounded by GL-10. Consequently neither exact GL-9 nor averaged GL-10 discharges SUCC #476's selected real near-pair energy `E_(A,m_A)=o(log m_A)`. The entire Archimedean cofactor/carry correlation is still unpaid.

## GL-07 — Character-class obstruction: chi_-4 is multiplicative, not an additive Gaussian parity map (PROVED)

The original real phase lives in the additive torsion group `Q/Z = ⊕_p Q_p/Z_p`. The partition into p≡1 and p≡3 mod4 splits its odd-primary DIRECT SUM into two additive subgroups, but **does not produce an additive sign χ_-4:Q/Z→{±1}**.

Indeed, Q/Z is divisible: for any x there is y with x=2y. Every group homomorphism into C2 must satisfy `f(x)=f(y)^2=1` and is therefore trivial. The nontrivial quadratic Dirichlet character χ_-4 is instead a multiplicative character on the integers coprime to four. Treating it as an additive parity observable of the actual source fractions is a type error. Gaussian prime splitting indexes legitimate p-primary factors; it cannot by itself force anti-phase pairing.

## GL-08 — Exact next real signed-lag gate, and why standard theorems cannot be invoked blindly

For the actual selected epoch I=[A,2A), q_n^+,q_n^- from the **FULL** odd conductor (not just the passport primes), define z_n(h)=e(hq_n^+)e(hq_n^-)=e(hU_n). For every 1<=R<=A a standard zero-extended van der Corput/Cauchy calculation gives

    |sum_(n∈I)z_n(h)|²
    <=(A+R-1)/R² * [R A + 2 sum_(d=1)^(R-1)(R-d)
                         Re sum_(n=A)^(2A-1-d) z_(n+d)(h)conj(z_n(h))]. (GL-11)

Proof: zero-extend the A samples, average R translates, and apply Cauchy to the A+R-1 translated windows; expansion yields the exact diagonal RA and original **selected, time-correlated** offdiagonal sums. This is classical, not a new saving.

A new route must derive a quantitatively NEGATIVE or small **joint** lag average with original odd C_n, source index, real integer carries and literal U0=0, sufficient to make the inherited Fejér energy `E_(A,m_A)=o(log m_A)` for an explicit m_A~logA. The usual large sieve of Montgomery–Vaughan demands demonstrated separation of the actual *real sampling points* and averages over stated evaluation parameters. GL-9 establishes exact nonrepeat but no lower separation δ of order 1/m_A; GL-10 is on a Galois average, not one source-selected point. Inserting either into a large sieve bound without this missing hypothesis is invalid.

A hypothetical source-derived inequality that discards the cofactor and treats the split/inert character means as independent is REFUTED by prior original finite covariance probes and a p-free cofactor-locking control. The same original forcing with changed seed can preserve local polynomial/Gamma structure but change the actual real phase. Finite tests cannot replace the missing unbounded selected inequality.

## Status ledger and externally checked sources

- GL-01..03: PAPER PROVED exact conditional on the previously authenticated original source/Γ completion; finite oracle supports, not independent external referee. New all-character compensation and explicit Euler slip reduce logarithmic source transport to bounded total error but do NOT prove the pure orbit sums small.
- GL-04: PAPER PROVED source exact inert injection/window; the tempting [k,2k) is **REFUTED** with p=47 and p=43.
- GL-05..06: PAPER PROVED source-specific with standard fixed-modulus PNT-AP as a classical external input. GL-09 exact nonrepeat; GL-10 only Galois-averaged pair savings. Selected real near-pair estimate UNVERIFIED.
- GL-07: elementary classical algebra; no additive χ_-4 parity.
- GL-08: classical van der Corput; the required selected source signed lag/covariance remains UNVERIFIED.
- π base-16 normality, RH, and GR physical interpretation remain OPEN.

Primary antecedents: NIST DLMF §5.9.13 for digamma/Gamma kernel (https://dlmf.nist.gov/5.9); Alex Kontorovich et al. public formal PNT-AP blueprint (https://alexkontorovich.github.io/PrimeNumberTheoremAnd/blueprint/corollaries-chapter.html); Montgomery–Vaughan, *The Large Sieve*, Mathematika 20 (1973) 119–134; Bailey–Crandall *On the Random Character of Fundamental Constant Expansions*, Experimental Mathematics 10 (2001) 175–190; Lagarias *On the Normality of Arithmetical Constants*, Experimental Mathematics 10 (2001) 355–368. Parent source #474/#476/#481/#484 and attached EGO research archive are shared-provenance mathematics, not independent witnesses.
