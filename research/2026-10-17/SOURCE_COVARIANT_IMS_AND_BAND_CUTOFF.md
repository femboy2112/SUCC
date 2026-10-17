# SOURCE-COVARIANT IMS: ARITHMETIC FUCC SHIFTS, GAMMA PARTITIONS, AND NEGATIVE-WITNESS BANDWIDTH

**Status:** PAPER DERIVED (classical functional-analysis and arithmetic reductions applied to the unmodified SUCC signed source); exact finite rational controls, optional SHA-pinned original-source packet. This is **not a proof of first-window `S4` positivity, Weil positivity, or RH**. Academic novelty unverified. No nontrivial zeta zeros are inputs. Original SUCC source blob `0cc8510b71d178fc79e8d410a86d8b6014cf9178` retained, **not edited**. Branch stacks on the gamma-edge companion PR #154 at `e9e09201b4414ed6e5e98183bde1b150ef74fdb2`; the sibling #155 piecewise integrator is inspected but not treated as ancestry.

## 0. Steelman and crucible

Proposed intuition: a lawful primitive is not free to choose the global arithmetic source. Finite SUCC operations occur inside a carrier bearing genuine multiplicative FUCC structure; therefore each primitive is subject to source-specific correlations and cannot be decomposed without interaction costs. The rigorous version is **source-covariant action and gluing**, not compulsory nonzero prime correlation in every test.

Three disjoint claims must be distinguished:

1. Every `F in H0^1(I)` has a well-defined genuine prime-power lag correlation `Re<F,T_(log n)F>` and nonnegative Gamma energy; this is a statement of the **operator** acting on `F`.
2. Not every `F` has a nonzero correlation at every prime lag: a smooth bump supported in an interval of diameter smaller than `log2` has no prime-2 self-overlap. The source still prescribes its (zero) reading.
3. A partition of unity produces source-determined Gamma, arithmetic prime-lag, and pole interface terms. They are signed bilinear contributions, not independently positive errors or arbitrary new Euler places.

## 1. Exact first-principles original-source primitive representation [SCIMS-01]

Fix `0<a<=1` where the imported original archive certifies the complete prime tape. Let `I=(-a,a)`. Take `F in Cc^infty(I;C)`, zero-extended to `R`; put `u=F'` (mean-zero), or extend the form identities to the appropriate `H0^1(I)` domain. Let `C=C_infinity = gamma_E + pi/2 + 3 log2 + log(pi)` be the authentic completed contact constant. For every genuine prime power `n=p^k` with `b_n=log n<2a`, put `w_n = Lambda(n)/sqrt(n)=log(p)/sqrt(p^k)`. The archived signed Suzuki screw kernel is, for `0<=r<=2a`,

```
g(r) = -8(cosh(r/2)-1) + (C/2)*r
       + sum_(genuine p^k, b_n<2a) w_n*(r-b_n)_+
       - sum_(j>=0) 4/(4j+1)^2*(1-exp(-(4j+1)*r/2)).
```

The finite-radius sum over prime powers is genuinely **finite**, with multiplicativity provenance and no fake `n=6` impulse. Set `d_j=4j+1`, `alpha_j=d_j/2`, `J(r)=sum_(j>=0)exp(-alpha_j r)=exp(-r/2)/(1-exp(-2r))`. The original quadratic form `Q_a(F')=int_I int_I g(|x-y|)F'(x)conj(F'(y))dxdy`, with signs as in original `source_weil_hierarchy.py`, becomes

```
Q_a(F') =  (1/2) int_R int_R J(|x-y|)|F(x)-F(y)|^2 dxdy
            - C * ||F||_2^2
            - 2 sum_(n=p^k, b_n<2a) w_n Re int_R F(x) conj(F(x+b_n)) dx
            + 2 |int_I F(x) cosh(x/2) dx|^2
            - 2 |int_I F(x) sinh(x/2) dx|^2.        (1)
```

**Proof and normalization:** twice integrate by parts in distributions: `Q_a(F')=-<g''*F,F>`. The Gamma rung satisfies `-g_j''=4/d_j delta_0 - exp(-alpha_j|r|)`, yielding the positive nonlocal jump energy; nonnegative monotone sum over `j` is legitimate on smooth compact primitives. The contact `(C/2)|r|` has second derivative `C delta_0`; hence it contributes `-C||F||²`. The authentic prime hinge `( |r|-b )_+` has distributional second derivative `delta_b+delta_-b`, hence *exactly* the `-2w Re` logarithmic translation correlation. Finally `-8(cosh(r/2)-1)` gives `-g''=2cosh(r/2)`; the identity `cosh((x-y)/2)=cosh(x/2)cosh(y/2)-sinh(x/2)sinh(y/2)` yields the **two completed polar terms with correct signs**. No zero coordinate occurs anywhere in the reconstruction. Only the complete source sum has an RH-relevant sign, not any individual positive Gamma term.

**Authentic finite source oracle:** `authenticated_first_prime_window_packet()` calls the original frozen source hash checker, verifies `((2,2),)` is the only active prime-power source at `a=1/2`, and checks `C<43/8`, `(log2)/sqrt2<1/2` by exact source intervals. The paper statement extends beyond the archive's `a<=1` only if the classical all-prime source formula is separately imported, not through this finite tape code.

**Exact polynomial calibration, independently derived:** for `a=1/2`, `u=P_1(2t)=2t`, `F(t)=t²-1/4`, and a rational `0<b<1`,

```
int F(t) F(t+b) dt = (1-b)^3*(1+3b+b²)/30,
int int (|x-y|-b)_+ (2x)(2y) dxdy = -2*(1-b)^3*(1+3b+b²)/30.
```

The latter also follows directly from `rho_11(r)=2(r-1)(2r²+2r-1)/3` integrated against `(r-b)` on `[b,1]`. This is an exact symbolic/rational bridge to `suzuki_legendre_source.prime_hinge_integral_polynomial`. Multiplying by the genuinely source-authenticated `w2=(log2)/sqrt2` recovers the original prime-2 sign. This calibration is **not** the full signed source.

## 2. The source action SUCC→FUCC [SCIMS-02]

In integer carrier coordinates, `S e_n=e_(n+1)` and `V_p e_n=e_(pn)` obey `V_p S = S^p V_p`. Define the *distribution-valued* logarithmic placement `Phi:c_00(N)->D'(R)`, `Phi(e_n)=delta_(log n)`. Then, on finitely supported arithmetic vectors,

```
Phi V_p = T_(log p) Phi,
Phi S(e_n) = delta_(log(n+1)),
log(n+1)-log n = log(1+1/n).
```

This is a genuine algebraic intertwining of **FUCC** with translation by `log p`, but **not** a Hilbert-space unitary equivalence or a claim that additive SUCC is constant-velocity translation in logarithmic time. The source's prime lag in (1) is defined independently by its actual von Mangoldt tape; the two descriptions are compatible, not circular derivations of zeta from the affine braid.

## 3. Exact original-source arithmetic IMS localization [SCIMS-03]

Take a finite real-valued smooth partition-of-square family `{chi_j}` on `R`, with `sum_j chi_j(x)^2=1` for all `x`. Every `chi_j F` remains a lawful smooth compact primitive. Write `Q_Gamma`, `Q_n`, `Q_contact`, `Q_pole` for the four parts of (1) and define the scalar jump defect

```
D_chi(x,y) = sum_j [chi_j(x)-chi_j(y)]².
```

Expanding the positive nonlocal squares **exactly** gives

```
sum_j Q_Gamma((chi_j F)') - Q_Gamma(F')
    = (1/2) int int J(|x-y|) Re(F(x)conj(F(y))) D_chi(x,y) dxdy.  (2)
```

For each real prime-power lag `b_n=log n`, expanding the genuine source correlation yields

```
sum_j Q_n((chi_j F)') - Q_n(F')
    = w_n Re int F(x)conj(F(x+b_n)) D_chi(x,x+b_n) dx.        (3)
```

**The crucial source-specific interface is exactly** `D_chi(x,x+log n)`: the square of the commutator amplitude for the genuine FUCC logarithmic translation. It is not an invented boundary force. Equation (2) is the nonlocal IMS/carré-du-champ algebra; (3) is its arithmetic-shift companion. These *corrections are not generally nonnegative*, because they contain signed relative phases `Re(F(x)conj(F(y)))`. Contact localizes exactly, `sum_j Q_contact((chi_j F)')=Q_contact(F')`.

Polar reassembly **must retain global source correlations**. Let `P(F)=2(|<F,cosh>|²-|<F,sinh>|²)` and define `D_pole(F,chi)=P(F)-sum_j P(chi_jF)`, with its completely explicit rank-two original-source moments. Combining all channels,

```
Q_a(F') = sum_j Q_a((chi_j F)') - D_Gamma(F,chi)
          - sum_(genuine p^k) D_n(F,chi) + D_pole(F,chi).     (4)
```

No diagrammatic gluing without these three correction families proves a signed result. The local contact cancels, but Gamma, prime and pole have nontrivial source-specific inter-chart interactions. A finite `Fraction` analogue in `source_covariant_ims.finite_ims` verifies every sign and channel, including examples where omitting the polar term forges a result. **This is a discrete model checking an algebraic identity**, not source identification of the discretized matrix.

## 4. Arithmetic no-go: no globally prime-transparent nonconstant continuous partition [SCIMS-04]

A spatial chart commuting with a genuine FUCC translation must satisfy `chi(x+log p)=chi(x)` for all `x`; then its arithmetic IMS defect for that prime vanishes identically. For the one-prime system `p=2`, nonconstant smooth `log2`-periodic charts exist, e.g. `cos(2 pi x/log2), sin(2 pi x/log2)`. But once both genuine primes 2 and 3 have arrived, invariance under both cannot persist nontrivially:

```
chi(x+log2)=chi(x)=chi(x+log3) for all x
    ==> chi is constant.
```

Proof: `log2/log3` is irrational, since `log2/log3=m/n` would give `2^n=3^m` with nonzero integers, contrary to unique prime factorization. Two incommensurable periods generate a dense subgroup of `R`. Continuity propagates invariance to its closure, all real translations, and hence `chi(x)=chi(0)` globally. The same applies chartwise to a partition-of-square family.

**Exact scope:** this is global invariance of continuous charts under both translations, **not** that every test has nonzero p=2 or p=3 correlation, nor that no spatial partition exists. At smaller support, some shifts do not connect support points. At the first window `a=1/2`, p3 is not active; the no-go becomes pertinent when `2a>log3`. Its mathematical content is that *nontrivial observer localization cannot erase every globally active FUCC interface by mere recharting*.

## 5. Gamma logarithmic multiplier and unconditional fixed-radius Gårding bound [SCIMS-05]

With unitary Fourier transform on `R`, the genuine Gamma jump form has symbol

```
m_Gamma(xi)=sum_(j>=0) 4 xi² /[(4j+1)(xi²+(4j+1)²/4)] >=0.
```

For `|xi|>=1`, every `d_j=4j+1<=|xi|` contributes at least `16/(5d_j)`. If `N=floor((|xi|-1)/4)`, the finite harmonic sum obeys

```
  m_Gamma(xi) >= (16/5)sum_(j=0)^N 1/(4j+1)
              >= (4/5) log(4N+5) >= (4/5)log|xi|.        (5)
```

This is a **rigorous pointwise source-derived high-frequency floor**; exact rational checks compare the finite prefix for rational `xi`. It is stronger than simply knowing Gamma is positive but says nothing about the low-frequency sign. The original prime-lag correlations satisfy `|<F,T_bF>|<=||F||²`. The source polar positive cosh channel is retained, while the only negative polar channel obeys `-2|<F,sinh>|²>=-2(sinh(a)-a)||F||²`. Consequently define

```
B_a = C + 2 sum_(genuine prime powers n, log n<2a) Lambda(n)/sqrt(n)
          + 2(sinh(a)-a).
```

Then the exact complete original signed source satisfies

```
Q_a(F') >= int_R m_Gamma(xi)|hat F(xi)|² dxi - B_a ||F||².    (6)
```

For any `R>=1` and Fourier low-pass projector `P_R`, this gives

```
Q_a(F') >= [(4/5)log R] * (||F||²-||P_R F||²) - B_a||F||².  (7)
```

This is a fixed-radius **frequency-observability inequality**: whenever `[(4/5)log R] >= 2 B_a`, any **strictly negative actual-source witness** satisfies

```
||P_R F||² > (1/2)||F||².                                  (8)
```

The theorem is unconditional *as an implication* from the original signed source formula and its established Gamma positivity, NOT an assertion of a negative direction, nor RH. It does not require candidate zero positions. At any fixed finite a, the arithmetic source supplies finitely many active true prime-power atoms, so B_a is finite. As a grows, B_a may grow without bound; (8) does **not** give a single uniform Fourier cutoff valid for all radii.

### Exact first-prime certificate: R = 2^24

At `a=1/2`, only the genuine prime2 wavefront is active. The pinned archive's exact intervals prove `C<43/8` and `w2=log2/sqrt2<1/2`. Independently, since `sinh(1/2)-1/2 <= (1/2)^3/[6(1-(1/2)^2)]=1/36`, we have `2(sinh(1/2)-1/2)<1/16`. Thus

```
B_(1/2) < 43/8 + 1 + 1/16 = 103/16.
```

The elementary atanh series proves `log2>2*(1/3+1/81+1/1215)=842/1215>69/100`. Take `R=2^24`; by (5),

```
m_Gamma(xi) >= (4/5)*log R
             > (4/5)*24*(69/100) = 1656/125 = 13.248
             > 103/8 = 2*(103/16) > 2 B_(1/2)
```

on `|xi|>=R`. This is a strict **all-rational source conditional-implication certificate**. The runtime source gate checks the exact protected source blob, prime2 activation, and these source upper bounds; the analytic steps are in this paper.

**Therefore if any actual negative first-window test exists, its primitive has more than half its L2 spectral mass in `|xi|<=16,777,216`.** The existing weighted-Bessel high-coercivity theorem already gives a much stronger *negative-index* bound (<=4) at this one radius; our result is about a different **Fourier-observation channel**, and must not be promoted as a stronger index estimate.

## 6. Finite observer readout and fixed-radius negative index [SCIMS-06]

Let `R=2^24`, `N=2R²=2^49`, `h=1/R`, `xi_j=-R+(j+1/2)h` for `j=0,...,N-1`. All xi_j are **rational**. For the unitary Fourier transform of any supported `F in L2(-1/2,1/2)`, Cauchy–Schwarz gives

```
|hat F(xi)| <= sqrt(1/(2pi)) ||F||,
|hat F'(xi)| <= (1/2)*sqrt(1/(2pi)) ||F||,
|d/dxi |hat F(xi)|²| <= (1/(2pi))||F||².
```

The midpoint quadrature error is at most `N*h²*L/4 = (1/(4pi))||F||² < (1/12)||F||²`, since `pi>3`. Consequently (8) implies for any strictly negative original-source direction

```
h * sum_(j=0)^(N-1) |hat F(xi_j)|² > (5/12)||F||² > (1/3)||F||².   (9)
```

These are **finitely many explicit mathematical Fourier readouts**; existence of physical measurement access to all of them is not claimed. The count is deliberately enormous. The certificate itself is short because no 2^49 individual samples are executed here. Finite sampling of an unknown F cannot on its own certify the signed energy Q_a(F') or produce a hidden negative vector. It only proves any such negative vector would necessarily generate a strong footprint in the chosen finite observation channel.

For fixed radius a and suitable R with `(4/5)log R>=2 B_a`, every negative-definite subspace E of the original signed test form has all its L2(F)-unit vectors satisfying (8). If `{F_i}` is an L2-orthonormal basis of E, then

```
dim(E)/2 < sum_i ||P_R F_i||² <= Tr(1_I P_R 1_I) = 2aR/pi.
```

The positive compact time-frequency concentration operator has explicit trace `2aR/pi` (factor it through the Hilbert–Schmidt truncated Fourier transform). Thus

```
negative_index(Q_a) < 4 a R / pi.                           (10)
```

This proves a finite negative index for **each fixed finite radius under the source formula**; it is not a global RH sign theorem. At a=1/2 this crude estimate is weaker than the inherited WB4 `negative_index<=4`; it may be useful as a general arithmetic radius-dependent spectral horizon when stronger Bessel estimates have not been established. Infinite time-bandwidth resolution at all a remains open.

## 7. Consequential next mathematical test [SCIMS-07, OPEN]

The user's proposed 'carrier resonance' becomes a concrete program:

1. Construct **source-generated FUCC-covariant partitions** using genuine `log p` lag translations, not arbitrary freely postulated sensor capabilities.
2. Prove operator-valued source-localization inequalities using the *actual signed* prime corrections (3), Gamma correction (2), and the **two completed polar moments**; never omit or posit positive cross terms.
3. Use `p=2,3` incommensurability to prove a quantitative lower bound on unavoidable partition commutators under a *specified localization constraint* (e.g. finite width or prescribed transfer fidelity), rather than only the qualitative common-period no-go.
4. Attempt a quantitative full-source **nonlocal IMS** estimate, with the true prime-powered source weight, whose localization error is smaller than the Gamma logarithmic compensation plus independently audited low-bulk sector. For the original `a=1/2` Schur short, source-specific matrix control and an effective high residual still remain necessary.
5. Independently audit the first-window low-frequency witness bound, e.g. optimize the huge `2^24` R by using exact multiplier/source constants and polar rank-two structure, and compare with existing WB4's much sharper four-low-mode negative-index gate.

**No sign theorem is asserted.** Uniformity in a, effective measurement access, proof of RH and academic priority remain open. None of (1)–(10) reads nontrivial zero locations.

**External analogues:** nonlocal Dirichlet forms and IMS localization are established classical machinery (e.g. Barlow–Bass–Chen–Kassmann 2006; discrete IMS in spectral-analysis literature). The prime-lag correction and finite-band budget are source-specific applications and not claimed novel mathematical concepts. Canonical source: M. Suzuki, 'Weil's quadratic form via the screw function', arXiv:2606.09096v3, formula (1.3). Verify all source assumptions in the pinned SUCC bridge before using it.
