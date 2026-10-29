# SUCC — The cototient dual of the harmonic/golden/Pascal Gamma triangle

**2026-10-29. Research only.** Proposed stacked child of SUCC draft PR #372 (`44912760eca39069ef5b980a492a1feabc9f6149`) and its #370/#369/#367 ancestors; read-only sibling #371 (`e418e465b7b0669997d8c67fcbcbd48c1df1681f`). Merged `main` observed at `ac7303b2e0e2ec16e3b1d88d186324e1fae65ea5`. No original four-pole forcing, U_0=0, historical proof registry, other branch, or main edits. π-normality and RH OPEN. The finite grade law is a declared mathematical Pascal observation on the *authentic source*, not a claim that π digits are random.

## 1. Three distinct uses of totient, typed

1. **Arithmetic:** φ(q)=#{a mod q:gcd(a,q)=1}; cototient `barφ(q)=q-φ(q)` (classical). This is a *count of equally weighted residue labels*.
2. **Source-graded:** J≥0 has Oily endpoint law w_j=(j+1)/2^(j+2). Set χ_q(j)=1_[gcd(j,q)=1], P_q=E χ_q(J), Q_q=1-P_q. These are *nonuniform probabilities*, generally not φ(q)/q.
3. **Carry-character:** for the actual integer carry κ, sum additive characters over unit or nonunit frequency labels mod q. This is a *Fourier transform of an integer carry*, not a selection of the Oily grade. Maintain this distinction.

For q>1, χ_q(0)=0. The complement includes grade zero and its original Gamma-rank-two contrast Ω_OM=φ_golden^(-1)-γ. At q=16, P_q=4/9, Q_q=5/9, despite classical φ(16)/16=1/2. Grade zero has unconditional mass 1/4 and conditional cototient mass (1/4)/(5/9)=9/20 exactly.

## 2. Exact complementary Oily generating functions

Let z be a formal variable or |z|≤1. For q=2^m,m≥1, primitive grades are odd. The unconditioned grade PGF and its two projected parts are

G(z)=1/(2-z)^2,

A(z)=E[z^J 1_(J odd)]=4z/(4-z²)^2,

B(z)=E[z^J 1_(J even)]=(4+z²)/(4-z²)^2.

They obey G=A+B, A(1)=4/9, B(1)=5/9, and the exact intertwinement `(4+z²)A(z)=4zB(z)`. The q=1 complement is zero, so never normalize it as a probability.

The limiting **coupled** Pascal–Poisson–Gamma law inherited from #372 is

P(J=j,Y∈dy)=y^(j+1)e^(-2y)/j! dy,  Z=2Y,  Z|J=j ~ Gamma(j+2,1),

and `E[z^J e^{-tZ}]=(2-z+2t)^(-2)`. Write

K_T(z,t)=E[z^J e^{-tZ} χ_16(J)] = (1+t)^(-2) A(z/(1+t)),
K_C(z,t)=E[z^J e^{-tZ}(1-χ_16(J))] = (1+t)^(-2)B(z/(1+t)).

After setting z=1, the normalized conditional densities of **Y**, not Z, are

f_T(y)=(9/8)y(e^(-y)-e^(-3y)),
f_C(y)=(9/10)y(e^(-y)+e^(-3y)).

These are nonnegative and integrate to one. The original Oily packet compiler has a *different joint* (grade, boundary) law despite the same endpoint grade marginal: do not transfer conditional-rank theorems to that law without an explicit map.

## 3. Exactly where γ lives in the sector differential

Let λ=(sqrt(5)-1)/2, and `F(Z)=log Z-exp(-λ Z)`. The conditional mean at grade j is

D(j+2)=H_(j+1)-γ-λ^(j+2).

For q=16 the exact sector means are

D_T = 1+log2+log3/8-γ-(9sqrt(5)/2-99/10) ≈ 1.09095215299287252639,
D_C = 1+log2-log3/10-γ-(207/25-18sqrt(5)/5) ≈ 0.77591500579084438674.

Therefore **γ cancels exactly in their normalized contrast**:

Δ_16=D_T-D_C = 909/50-81sqrt(5)/10+(9/40)log3
  ≈0.31503714720202813965 >0.

The unconditioned mean is `(4/9)D_T+(5/9)D_C = 4/5+log2-γ`.
The selection susceptibility of F under exponential event tilt `dP_θ/dP ∝ e^(θχ_16)` is

`(d/dθ)E_θ F|_(θ=0)=Cov(χ_16,F)=(4/9)(5/9)Δ_16
 = 202/45-2sqrt(5)+log3/18 ≈0.07778694992642670115`.

No γ survives in this centered observable. In the **unnormalized** signed balance `E[(2χ_16-1)F]`, γ has coefficient `-γ(4/9-5/9)=+γ/9`. That term is not invariant under additive shifts F→F+c; it measures unequal sector masses, not an intrinsic interaction.

The original Ω_OM occurs **inside** the cototient distribution at j=0 with exact conditional probability 9/20, whereas it is absent from the totient sector. This is a genuine reference anchoring, not a coefficient of the centered differential.

### Finite original-source theorem: same γ cancellation at every n

Retain the ORIGINAL four poles `Q(x)=4-2e^(-3x)-e^(-4x)-e^(-5x)` and `a=8n-7`, `μ_a(dx)=e^(-ax)Q(x)dx/R(a)` with `R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5)`. Given X=x, draw the DECLARED `J_n~Bin(n,1-e^(-8x))`. For E∈{J_n odd,J_n even}, its likelihood is

`L_E(x)=[1±(2e^(-8x)-1)^n]/2` (minus for odd),

and the unnormalized density `e^(-ax)Q(x)L_E(x)` is a finite signed *exponential representation of a positive function*, `sum_ell b_ell e^(-c_ell x)` with c_ell>0 and exact rational b_ell. Put `W_E=sum b_ell/c_ell>0`. Then for Re s>-1,

`E[X^s|E]=Gamma(1+s) [sum b_ell c_ell^(-1-s)]/W_E`.

The logarithmic derivative at s=0 gives exactly

`E[log(2a X)|E]=log(2a)-γ-[sum (b_ell/c_ell) log c_ell]/W_E`,

and the exponential part is

`E[e^(-2aλ X)|E]=[sum b_ell/(c_ell+2aλ)]/W_E`.

Thus **for each finite n**, both normalized sector contrasts have precisely the same `-γ` additive term; their difference is γ-free. This uses the genuine four-pole source and the declared finite Pascal observation; no asymptotic approximation is needed. Coefficient signs in the exponential expansion are not probabilities. Exact b_ell are generated and tested in `cototient_dual_probe.py`; independent direct quadrature is in `independent_cototient_oracle.py`.

## 4. Cototient retains a stable, present-state signed inverse

For any bounded sequence |z_n|≤1, let S be the forward shift `(Sz)_n=z_(n+1)`. The endpoint projected sequence `Σ_T=A(S)z`, `Σ_C=B(S)z` satisfies

`(4-S²)^2 Σ_T=4Sz`,
`(4-S²)^2 Σ_C=(4+S²)z`.

The totient operator starts at grade one and only directly recovers the *shifted* original input. The cototient operator has constant coefficient w_0=1/4 and a **stable bounded inverse**:

`z=(4+S²)^(-1)(4-S²)^2 Σ_C`,
`(4+S²)^(-1)=Σ_(k>=0)(-1)^k S^(2k)/4^(k+1)`.

The last series converges in ℓ∞ operator norm, with norm ≤1/3 for the reciprocal factor; combining factors gives inverse norm ≤25/3.

For finite original Pascal weights `q_n(j)` from #370, define `Θ_n^C=Σ_(0≤j≤n,j even)q_n(j)z_(n+j)`. Inherited `TV(q_n,w)≤22/n` for n≥3 gives

`|16Θ_n^C-8Θ_(n+2)^C+Θ_(n+4)^C-4z_n-z_(n+2)|≤1100/n`.

Consequently applying the *same stable infinite inverse* to the finite-source readout reconstructs z_n to within `1100/(3n)` (for n≥3), uniformly in every |z|≤1. This includes the authentic zero-seeded phase but also the coherent counterseed and constant sequences. **It is a representation theorem, not decay of Fourier means.**

For stationary normalized primitive and cototient filters, their respective shifts have mean 7/3 and 26/15. Every bounded sequence therefore satisfies a primitive-minus-cototient **Cesàro** comparison bounded by `122/(15N)`; adding finite source convergence contributes O(log N/N). Thus simple filtered time-average differences vanish for all bounded sequences, whether normal or not. They cannot be used as a π normality criterion.

## 5. Complementary Fourier shells of the ACTUAL integer carry

For q>1 and integer κ, the primitive character sum is Ramanujan's

`c_q(κ)=Σ_(a mod q,gcd(a,q)=1) exp(2π i a κ/q)
       =Σ_(d|gcd(q,κ)) d μ_arith(q/d)`.

Its **cototient character dual** is

`c_q^perp(κ)=Σ_(a mod q,gcd(a,q)>1) exp(2π i a κ/q)
             =q·1_(q|κ)-c_q(κ)`.

For q=p^m this collapses to `c_(p^m)^perp(κ)=p^(m-1)·1_(p^(m-1)|κ)`; in particular,

`c_16(κ)=16·1_(16|κ)-8·1_(8|κ)`, `c_16^perp(κ)=8·1_(8|κ)`,
`c_16-c_16^perp=-16·1_(κ ≡ 8 mod 16)`.

This isolates a **highest-bit carry contrast** only when lower 3 bits vanish. It is NOT the same arithmetic operation as selecting even packet grade. The coherent same-forcing changed seed `U_0=-π/16` has all late literal carries 15 in the inherited #371 result; both aggregated carry shells vanish for 15. Hence the two shells alone fail the changed-seed falsifier. Retain all 16 carry bins/Walsh masks and signed absolute phases, rather than interpreting two collapsed Fourier shells as a source authentication.

## 6. The rank-shift totient/cototient square has twin-prime-style finite CRT factors

The Pascal–Gamma joint assigns rank `r=j+2`. Grade primitivity `χ_q(j)` and **rank primitivity** `χ_q(j+2)` are generally distinct arithmetic tests. At modulus q=2 they coincide; at odd primes they can disagree.

For every prime p>2, no residue j can have both p|j and p|(j+2). Thus the **double cototient** cell has zero mass for a single odd prime. For general q, CRT yields the exact count

`#{j mod q: gcd(j,q)=gcd(j+2,q)=1}
 = q·∏_(p|q)[1-1/p for p=2; 1-2/p for odd p]`.

This has the familiar **local twin-prime sieve admissibility factors**; this is finite arithmetic and NOT a twin prime proof. The source-weighted analog requires the exact *nonuniform* residue weights

`W_(q,r)(z)=(z/2)^r/4 · [(r+1)/(1-t)+q t/(1-t)^2], t=(z/2)^q, 0≤r<q`.

At q=3 the four (grade primitive?, rank primitive?) cells are

`P_(00)=0, P_(01)=20/49, P_(10)=17/49, P_(11)=12/49`.

The missing cell forbids a complete 2×2 interaction contrast. At q=6 all four cells are present:

`P_(00)=5/9; P_(01)=172/1323; P_(10)=352/1323; P_(11)=64/1323`.

Using the same F(Z)=log Z-exp(-λ Z), high-precision (non-interval) evaluation of all four conditional expectations gives an **explicit completed factorial interaction**

`E[F|11]-E[F|10]-E[F|01]+E[F|00]
 ≈0.40896091785703939962`.

Truncating the j-sum at 170 has an absolute unnormalized moment-tail bound below 1e-47; the exact sector masses are rational and positive. This is a source-defined arithmetic selection interaction, not non-Abelian quantum physics or signed π cancellation.

## 7. A second (global arithmetic) γ differential: Dirichlet finite parts

The ordinary arithmetic totient/cototient functions have Dirichlet generating series for Re s>2:

`T(s)=Σ_(n≥1)φ(n)/n^s=ζ(s-1)/ζ(s)`,
`C(s)=Σ_(n≥1)(n-φ(n))/n^s=ζ(s-1)(1-1/ζ(s))`.

Writing ε=s-2, `ζ(1+ε)=1/ε+γ+O(ε)`, and expanding `1/ζ(2+ε)`, the **finite parts** at s=2 are

`FP T = γ/ζ(2) - ζ'(2)/ζ(2)^2`,
`FP C = γ(1-1/ζ(2)) + ζ'(2)/ζ(2)^2`.

Therefore

`FP(T-C)=γ(2/ζ(2)-1)-2ζ'(2)/ζ(2)^2`.

This γ genuinely survives the *globally specified Dirichlet regularization*. It is a different comparison from the normalized Oily grade-sector difference, where γ cancels. Ordinary totient/cototient arithmetic by itself does NOT select φ_golden^(-1): that marker enters only through the explicitly retained Oily generating function. Do not conflate these two appearances of Euler's constant.

## 8. Proof authority, remaining question, and decisive controls

The generating functions, finite Mellin factorization, γ cancellation, stable cot inverse, mod-16 Ramanujan/cot Fourier, grade-rank CRT counts, and Dirichlet finite parts have elementary derivations stated here. The finite test code verifies rational identities across many n,q and adversarial bounded sequences. Independent SymPy reduction and direct high-precision source quadrature calibrate the conditional closed form and source-finite event integrals. **No Lean check, hosted CI, full native test suite, external blind review, or new BBP Weyl cancellation theorem is claimed.**

Potential next lamp: retain the full tensor indexed by (grade gcd class, rank gcd class, integer literal carry κ mod16, absolute phase e(hU_(n+j)(0))) under the genuine original recurrence. Compare the q=6 complete factorial and q=3 forbidden cells against the coherent -π/16 counterseed, prime 2/3/5 filters and original-four-pole mutants. The missing proof would have to derive a **noncircular, source- and seed-specific signed carry correlation estimate**, not a static normalized smoothing identity: q=16 complement is invertible for **every bounded sequence** and cannot by itself force normality.

### External mathematical provenance

- Cototient `q-φ(q)`: [Wolfram MathWorld, Cototient](https://mathworld.wolfram.com/Cototient.html).
- Ramanujan sum divisor identity: [NIST DLMF 27.10.4–5](https://dlmf.nist.gov/27.10).
- Totient Dirichlet series: [NIST DLMF 27.4.6](https://dlmf.nist.gov/27.4.E6).
- ζ Laurent constant γ: [NIST DLMF 25.2.4](https://dlmf.nist.gov/25.2.E4).
- Source: SUCC `research/2026-10-26/OILY_TOTIENT_THIRD_SHADOW.md`; #372 `research/2026-10-29/totient_pascal_gamma/PRIMITIVE_GAMMA_TRIANGLE.md`; #370; #371; #367. Claims are scoped to the exact original source and the explicit declared observation models.
