# Dual Zero / Rational-Real Cayley Carrier — source-preserving theorem dossier

**Date 2026-11-04.** Research-only add-on to Europa #500 (pinned parent bf103c4a25bbd83b6cfbad1dd77895928300ddd9), with Gamma Prybar #501 as READ-ONLY sibling. PREREGISTRATION.md was committed before the source holdouts. Original signed four-pole BBP forcing, literal U0=0, older source contracts, historical Lean, main and workflows remain UNCHANGED. All claims below are classical mathematical deductions and source-specific compositions, not a normality proof, physical Feynman amplitude, or independently certified scholarly first.

## DZ-01 — two different zeros really are Fourier dual, NOT the same 1

For an odd cyclic source carrier C_M=Z/MZ and basis |a> in C[C_M], define X|a>=|a+1>, Z|a>=exp(2πia/M)|a>. The two character identities exp(2πi 0*a/M)=1 and exp(2πi h*0/M)=1 are different row/column restrictions of ONE bicharacter.

The zero-frequency and zero-phase projectors are

P_F = M^(-1) sum_(j mod M) X^j = |u><u|, u=M^(-1/2) sum_a |a>;
P_0 = M^(-1) sum_(h mod M) Z^h = |0><0|.

The normalized discrete Fourier transform interchanges them. Rank-one algebra proves exactly

tr(P_F P_0)=1/M,
P_F P_0 P_F=P_F/M,
P_0 P_F P_0=P_0/M,
||[P_F,P_0]||_HS^2=2(M-1)/M^2.

The projections do not commute for M>1. This is a finite path/character sum, not a quantum path integral or a statistical conclusion about a single chosen orbit. In particular, as the authentic conductor increases, their *overlap tends to zero*, although both unprojected zero evaluations return scalar 1.

## DZ-02 — the rational/real projective Cayley interval

Define C(t)=(1+it)/(1-it), with C(infinity)=-1. It is an oriented homeomorphism RP^1(R) -> S^1, with inverse t=-i(z-1)/(z+1) for z != -1. For reduced rational t=a/b,

C(a/b)=((b^2-a^2)+2iab)/(a^2+b^2).

This parametrizes all rational-coordinate circle points. No odd p congruent 3 modulo 4 can divide a^2+b^2 when gcd(a,b)=1; if a,b are both odd the only factor 2 in the norm cancels from both coordinates. Thus the reduced coordinate denominators of rational Cayley points are odd and have only splitting primes p=1 mod4. This is the classical Gaussian norm/sum-of-two-squares structure.

The four rational UNIT INTERVAL charts C(u), C(1/u), C(-1/u), C(-u) cover the four oriented quarter arcs, with matching endpoints 1,i,-1,-i,1 (reverse direction for the second and fourth charts). For t>0,

arctan(t)+arctan(1/t)=π/2,
C(1/t)=-C(t)^(-1).

For t<0 the principal arctan sum is -π/2, giving the same projective circle relation. This is exact elementary geometry, not evidence of temporal Weyl decay.

## DZ-03 — the REAL algebraic lift of the ACTUAL rational source

Let x=a/M mod1 be a reduced source phase with odd M>1. Its authentic circle point is ζ=exp(2πia/M), and its CORRECT tangent coordinate is

t(x)=tan(πa/M)=-i(ζ-1)/(ζ+1).

It is real, finite and algebraic. It is NOT generally rational, and crucially it is NOT the original phase number a/M. The inverse C(t(x))=ζ exactly reproduces the selected source character.

The field K=Q(i,ζ)=Q(i,t). Since M is odd, Q(ζ) does not contain i: otherwise it would contain a primitive (4M)th root, impossible because φ(4M)=2φ(M)>φ(M). Hence [K:Q]=2φ(M). Since t is real, [K:Q(t)]=2. Consequently

**[Q(tan(πa/M)):Q]=φ(M), for reduced odd M>1.**

The M=1 origin is t=0 with degree1. This exact tangent degree is classical (Calcut, Rationality and the Tangent Function, Proposition 2). A finite polynomial certificate requiring no π DIGITS is

R_M(T)=(1-iT)^φ(M) Φ_M((1+iT)/(1-iT)) in Z[T],

which is irreducible of degree φ(M) for odd M>1. The original rational numerator a specifies WHICH real root. The polynomial without that orientation is not a selected source.

EXACT source example: the primal zero-seeded first state Y1=109/35 has phase 4/35. Its actual tangent t=tan(4π/35) has degree φ(35)=24. Mistakenly applying C to the rational number 4/35 produces (1209+280i)/1241, with 1241=17*73, an entirely different circle point. This is an explicit no-oracle/source-map discriminator.

## DZ-04 — an all-time algebraic degree lower bound, then 6N / 8N

Both original four-pole and prime-character angular projected source states have ODD reduced phase denominators D_N. All prime factors in D_N arise from the rational forcing factors at indices ≤N and are ≤8N (possible fixed powers of 2 cancel because the source phase has odd denominator). Thus for N>=1,

0 ≤ log(D_N/φ(D_N)) = sum_(p|D_N) log(p/(p-1))
  ≤ sum_(p|D_N) 1/(p-1) ≤ H_(8N-1) ≤ 1+log(8N).

So the **exact uniform all-N bound** is D_N/(8eN) ≤ φ(D_N) ≤ D_N. By the classical tangent degree theorem, the source-selected R/tangent phase has algebraic degree φ(D_N). Combined with the prior paper-proved, not externally refereed, SUCC #497/#499 results log D_N^U=(6+o(1))N and log D_N^Y=(8+o(1))N, this yields

log deg_Q tan(πU_N)=(6+o(1))N,
log deg_Q tan(πY_N)=(8+o(1))N.

At the MINIMAL instantaneous finite circle C_D the negative logarithm of the two-zero projector overlap is log D, so its growth exponent matches the real tangent coordinate's algebraic-degree exponent. This is arithmetic complexity, NOT digit entropy, Haar mixing or a physical probability. Use source cumulative LCM M_N for nested chronological conductor arrows; D_N need not be nested.

## DZ-05 — reciprocal arctan is a 2-primary carrier change

For reduced x=a/M with M odd, the reciprocal tangent 1/t corresponds to the REAL circle phase x'=(1/2-x) mod1. Its reduced denominator is exactly 2M because M-2a is odd and coprime to M. Therefore reciprocal arctan gluing cannot act INSIDE the original odd-denominator source subcategory: it requires a declared 2-primary extension, retaining the old rational numerator, odd conductor and source carry.

The Fourier transform is exact: exp(2πi h x')=(-1)^h conjugate(exp(2πi h x)). A global reciprocal reflection preserves the MODULUS of every Weyl coefficient and every circle tent/collision energy. The parity (-1)^h here is a circle character, NOT the multiplicative χ_-4(p) prime-class character of the Gaussian primal. This distinction is load-bearing.

## DZ-06 — exact finite Fourier compatibility under conductor growth

If M|M'=kM, embed |a> in C_M as |ka> in C_M'. With the + Fourier convention,

(F_M f)(h)=M^(-1/2)sum_a exp(2πiha/M)f(a),

the genuine Fourier-refinement law is

(F_M' iota f)(h)=sqrt(M/M') (F_M f)(h modM).

There are k aliased frequency copies. The old normalized uniform state is mapped to a subgroup-uniform state, NOT the new full Haar vector. Source conductor refinement does not give a natural selected Haar time orbit. The full UNIFORM ensemble on C_M has a weak Haar limit as M grows, but source-selected rational phases are a different object.

## DZ-07 — the primal angular BBP kernel is exactly quarter-Haar Jacobian

On RP^1(R), C(t)=exp(2i arctan(t)). The pullback of normalized real-circle Haar is the Cauchy reference density dt/(π(1+t^2)); the projective infinity point has no atom. Each of the four unit-interval charts carries probability 1/4. Because the authenticated prime-character angular primal has kernel K_ang(t)=4/(1+t^2) after t=1-source_x,

K_ang(t)dt/π = 4 dt/[π(1+t^2)] on 0≤t≤1

is EXACTLY the reference Haar measure CONDITIONED on its first quarter arc. This is a genuine source scalar/angular integral identification, NOT source time equidistribution. A uniform t-grid is not quarter-Haar: its mean is 1/2 rather than 2log(2)/π<1/2.

## DZ-08 — exact real-projective source dynamics, algebraic forcing and negative controls

Let x_n={U_n} or {Y_n}, source forcing r(n+1), and t_n=tan(πx_n), s_n=tan(πr(n+1)). These are algebraic real numbers with source-authenticated cyclotomic root choices. Define A16+i B16=(1+it)^16, i.e.

A16(t)=sum_(j=0)^8 (-1)^j binom(16,2j)t^(2j),
B16(t)=sum_(j=0)^7 (-1)^j binom(16,2j+1)t^(2j+1).

The ORIGINAL affine circle recurrence has the exact projective rational update

t_(n+1)=[B16(t_n)+s_n A16(t_n)]/[A16(t_n)-s_n B16(t_n)],

including ∞ when the projective denominator vanishes. The coefficients in t are integers and the ONLY external parameter is the exact source-defined algebraic forcing s_n. The original UNWRAPPED integer/rational state and its literal carries remain parallel data; this circle quotient does not discard their source provenance.

This map preserves the Cauchy REFERENCE probability measure because it is conjugate to ×16 followed by a circle rotation. But preserving Cauchy does NOT select Cauchy: the unforced nonnormal fixed orbits x=1/3,1/5,1/15 have algebraic irrational tangent coordinates with minimal polynomials dividing B16(t)-t A16(t). Thus every uniformity claim based solely on this rational/projective naturality is refuted.

**Endogenous source falsifier:** the genuine zero-seeded RADIAL projection Z_N=U_N-Y_N from #499 satisfies 0<Z_N<1/(32N+16), while #500 reports log den(Z_N)=(8+o(1))N. Hence its real tangent algebraic degree grows like exp((8+o(1))N), and its two-zero projector overlap decays similarly, YET Z_N→0 and its real-circle empirical measure approaches the point mass δ0. Therefore even the same source's own high-degree real coordinates and vanishing zero-projector overlaps do NOT imply angular mixing.

## DZ-09 — equivalence to a real Cauchy observational normality gate (OPEN)

For the chosen ZERO-SEEDED angular time trajectory, ν_A=A^(-1)sum_(A≤n<2A) δ_(tan πY_n) is a measure on RP^1(R). By the Cayley homeomorphism, ν_A tends weakly to dt/[π(1+t^2)] iff its selected nontrivial circle Weyl coefficients

A^(-1) sum_(A≤n<2A) C(t_n)^h → 0, for each fixed h!=0.

The same original/primal full-prefix normality equivalence is inherited from #499 and SUCC's earlier source bridge. THIS IS AN EQUIVALENT REFORMULATION, NOT A NEW SIGNED SAVING. The Cauchy measure has no finite first absolute moment: any polynomial-moment argument on bare R must state its truncation, while bounded continuous tests on compact RP^1 are legitimate.

## Validation, source map and limits

A complete source/test/receipt package is attached to the conversation as SUCC_Dual_Zero_Rational_Real_Cayley_2026-11-04.zip. Its isolated staged tests: 30 new exact-source and symbolic regressions + 26 inherited primal regressions = 56 PASS; deterministic exact source receipt and compileall PASS. Includes independent integer-LCM vs Fraction original/primal states through n=61; integer cyclotomic character orthogonality; rational Cayley Pythagorean/split-prime checks; SymPy tangent minimal polynomials; genuine radial source controls; 16-multiple tangent polynomial, reciprocal 2M, and irrational fixed-point regressions. Same reasoning/source provenance, not blind independent referee. The full new file payload is separately attached; not claimed committed until byte re-fetch confirms it.

**NOT CLAIMED:** native complete SUCC checkout tests on THIS child, full provenance/foundations/ordinal, new compiled Lean theorem, independently established world academic priority, selected J=o(K), fixed-h signed Weyl decay, π base16 normality, beta GRH, zeta RH or physical quantum interference. 

**NEXT:** Seek a source-specific signed estimate on the actual angular phase amplitudes which fails for the radial null, periodic 1/5, altered-seed and CRT-cofactor mutants. A new 2-primary carrier or exact Cauchy reference without such an inequality does not close normality.

**Classical references:** J. S. Calcut, Rationality and the Tangent Function, Proposition 2 (https://www2.oberlin.edu/faculty/jcalcut/tanpap.pdf); NIST DLMF §4.24 tangent addition (https://dlmf.nist.gov/4.24). Earlier SUCC #497/#499/#500 theorem lineage and parallel #501 microscopic signed probes are named source dependencies, not independent new sources.