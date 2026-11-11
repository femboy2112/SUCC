# Zero-Anchored Identity Kernel — definitions, theorems, and proof contracts

**Status:** `PROVED PAPER` for explicit rational and classical categorical statements with stated imports. `OBSERVED FINITE` for tests and numeric displays. `OPEN` for any pi normality / signed decay inference. Nonnovelty note: BBP, π irrationality, Dedekind cuts, Farey/Stern–Brocot, 16-fold shift Weyl criterion, and real-line Wasserstein identities are classical; the present contribution is a source-locked compiler architecture and executable exact controls.

## ZI-01. Unique source-selected root and effective modulus (PROVED PAPER)

For n>=1 preserve the four signed poles verbatim:

```
r(n)=4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2).
```

Let `P_0=0`, `P_n=sum_(j=1)^n 16^-j r(j)`, and `x=sum_(j>=1)16^-j r(j)`. Classical BBP states `16x=pi`. The source has the positive moment representation

```
r(n)=int_0^1 t^(8n-8) (1-t)(t^2+2)(t^2+2t+2) dt.
```

Thus `r(n)>r(n+1)>0`. For every `n>=0`,

```
P_n < x < H_n := P_n+r(n+1)/(15*16^n)
0 < H_n-P_n <= (47/225)*16^(-n) < 16^(-n).
```

**Proof:** the positive remainder is `sum_(j>n)16^-j r(j)`. Monotonicity gives it strictly below `r(n+1)sum_(j>n)16^-j=r(n+1)/(15*16^n)`. The n=1 source value is `47/15` and decreases strictly, proving the width constant. The lower endpoints increase; the upper endpoints decrease, because `H_(n+1)-H_n =16^(-(n+1))*(r(n+2)-r(n+1))/15<0`. Nested compact closures have intersection exactly `{x}` because widths ->0. For any rational epsilon>0 choose n with `16^-n<epsilon`: this is finite and gives a strict rational enclosure of required width. No pi-value oracle is needed. ∎

The separate circle-beta source at depth k uses `W_0=1`, `W_(j+1)=W_j*(j+1)/(2j+3)`, `S_k=2 sum_(j<k)W_j`, and interval `[(S_k+3W_k)/16,(S_k+4W_k)/16]`. From the Euclidean arclength theorem established on #595, this strictly encloses `pi/16`. Their intersection is a smaller interval for the same x. **Finite intersection is not an independent proof that the two limiting definitions agree**; equality uses classical geometric π and the BBP identity, declared as imports. If two independently *proved* enclosure names have distinct limits, their finite intervals must eventually become disjoint.

## ZI-02. The origin equalizer and symbolic counterseed (PROVED PAPER)

Define `M=Q+Q*x`, regarded as a rational vector space whose coordinates `(a,b)` denote `a+b*x`. Because `x` is irrational, `(a,b)->a+b*x` is injective. The `s`-seeded source recurrence is

```
U_0(s)=s,
U_(n+1)(s)=16 U_n(s)+r(n+1),
U_n(s)=16^n(s+P_n),
Z_n(s):=16^-n U_n(s)-P_n=s.
```

All equations are exact in `M` and can be proved by induction, retaining the entire real/unwrapped state. The origin-selected natural section is the **unique** recurrence solution in this source fiber with `Z_0=0`, equivalently with `Z_n=0` at any clock. Every other seed is excluded algebraically. The source completion identity is

```
T_n=16^n(x-P_n),   0<T_n<r(n+1)/15,
U_n(s)+T_n=16^n(x+s).
```

The coherent same-forcing counterseed `s=-x` is `(0,-1)` and gives completed phase zero at all n, yet `Z_n=(0,-1)!=0`. The rational counterseed `s=1/16` is `(1/16,0)` and is rejected despite later phase aliasing. `zero_anchor.py` refuses to issue an authenticated `PhaseCertificate` for either. ∎

**Scope:** the finite equality test is on M, not arbitrary computably named real seeds, for which zero equality is generally undecidable. We require an exact type and its proof contract; an arbitrary two-number tuple without source provenance is not a proof of `pi/16`.

## ZI-03. Complete classification of eventual phase aliases in M (PROVED PAPER)

Two seeds `s,t in M` give equal **completed circle phases** at every clock `n>=N` if and only if `16^N(s-t) in Z`. For the difference `s-t=a+b*x`, the irrationality of x shows this holds only if `b=0` and `16^N a in Z`. Therefore the least alias clock is `ceil(v_2(denominator(a))/4)` if the reduced rational denominator of a is a power of 2, and no finite alias clock exists otherwise. Every fixed `N` equivalence class loses the rational group `16^-N Z`; the unwrapped `Z_n` recovery always retains the original seed.

This gives an exact separation between *finite later phase equivalence*, *seed identity*, and *source identity*. The map `s->Z_n(s)` is faithful on the whole declared module, not merely on a finite empirical sample. ∎

## ZI-04. Source-faithful affine arrows (PROVED PAPER)

For integers `a>=1,b>=0`, define the indexed source-state arrow

```
A_(a,b)(n,U_n(s))=(an+b,U_(an+b)(s)).
```

Then

```
A_(a,b) o A_(c,d)=A_(ac,ad+b),
D_p=A_(p,0),  S=A_(1,1),  D_p S=S^p D_p,
Z_(an+b)(U_(an+b)(s))=Z_n(U_n(s))=s.
```

The first law holds because both sides have clock `ac*n+ad+b` and preserve s; the other laws follow. It is *not* the map `U->pU`, and the clock and source cannot be erased without changing the claimed functor. This is the explicit representation already motivated in SUCC #579, now extended to the two-dimensional rational-affine seed module. ∎

## ZI-05. Complete rational-probe fingerprint (PROVED PAPER, classical inputs)

Define the rational subterminal presheaf `Y_x(q)={*}` iff `q<x`. Each rational q differs from the irrational x, and the interval widths tend to zero. Thus for every rational q, finite source refinement decides whether `q<x`. The natural-family inclusion relation faithfully recovers x among all real cuts, by density of rationals. It is *not* ordinary Yoneda representability inside Q: x is not an object of Q. It is the restriction of the real-order representable `Hom_R(-,x)` along Q -> R.

At every finite source depth n the interval `(P_n,H_n)` is a *proof object*; arrows are refinement. The limit in the information order of compact real intervals is the singleton `[x,x]`. The source and geometric interval names have a coherent common refinement by intersection. The source label, zero section, rational cut and finite phase operations together comprise the proposed **identity kernel**. Any false rational candidate is separated at finite depth; no uniform rational-query runtime bound or arbitrary computable-real equality algorithm is asserted.

## ZI-06. Zero-locked phase, integer winding and digit certificates (PROVED PAPER)

For n>=0, let `k_n=floor(16^n*x)` and `theta_n=16^n*x-k_n`. Because x is irrational, `16^n*x` is never an integer or a hexadecimal boundary. Hence strict rational source refinement eventually produces an interval `(l_n,u_n)` strictly inside the correct phase and first-digit chart, together with the exact integer carry k_n:

```
0<l_n<theta_n<u_n<1,
[floor(16*l_n)]=[floor(16*u_n)],
16^n*x=U_n(0)+T_n=k_n+theta_n,
T_n in (16^n*(P_L-P_n), 16^n*(H_L-P_n)).
```

No rational floor is ever inferred from an interval still crossing an integer/radix boundary. Increasing L also certifies any fixed hexadecimal word prefix. This is a finite procedure for any fixed n or word length, not a claim about the statistical frequency of the word over all n.

## ZI-07. Quantitative source-to-Weyl and source-to-joining transport (PROVED PAPER)

For `e(t)=exp(2*pi*i*t)` and integer `h!=0`, `W_(N,h)(x)=(1/N)sum_(0<=n<N)e(h*16^n*x)`. Let `m_L=(P_L+H_L)/2` and `w_L=H_L-P_L`. Since `|e(a)-e(b)|<=2pi*|a-b|`, `pi<4`, and `|x-m_L|<w_L/2`, the geometric sum gives

```
|W_(N,h)(x)-W_(N,h)(m_L)|
  < [4|h|(16^N-1)/(15N)]*w_L
  = 4|h|r(L+1)(16^N-1)/(225N*16^L).
```

At `L=N+s`, this is `<4|h|r(N+s+1)/(225N*16^s)`. Epoch means over n in `[A,2A)` have the analogous bound `4|h|(16^(2A)-16^A)*w_L/(15A)`. Source forcing alone generates the rational states `U_n(0)`, with

```
|(1/N) sum e(h*U_n(0)) - W_(N,h)(x)|
   < [8|h|/(15N)] sum_(n=0)^(N-1) r(n+1).
```

For `h=0`, all these character-comparison differences are exactly zero. For #593, the proper 2:3 mixed Fourier phase uses `alpha=pi=16x`, coefficient `K_l=16^(3l-1)-16^(2l-1)` of alpha, hence the coefficient of x is `16^(3l)-16^(2l)`. Each finite ratio-fiber epoch has error `<4|h|w_L*mean_(l in J_A)(16^(3l)-16^(2l))` between x and m_L. **This is a valid transport cost, not a bound on the magnitude of the authentic signed statistic.** No extra prime-power/CRT or seed/carry information is inferred by changing coordinates. ∎

## ZI-08. Branch-aware rational Haar/SIGNED overlap budget (PROVED PAPER)

Let `mu_N=(1/N)sum_(n<N)delta_(theta_n)` and `T(z)={16z}`. Let `B_a(y)=(a+y)/16`, `C=(1/16)sum_(a=0)^15 (B_a)_*` and `Q=C T_*`. For every atomic phase z, `(Q delta_z)` equals the uniform law on `z+a/16 mod1` for a in 0..15. Let `D_N=W_1(mu_N,Q mu_N)` in the *ordinary interval metric* on `[0,1]`. For adjacent equal windows of length M define

```
Omega_M = (D_(M,early)+D_(M,late))/2 - D_(2M).
```

The identity `Omega_M>=0` is SUCC #591's exact signed CDF overlap (not a positive-covariance theorem). Take certified phase intervals `(l_n,u_n)` *each contained in one open digit chart* `(d_n/16,(d_n+1)/16)`. Let `m_n=(l_n+u_n)/2`, `epsilon_n=(u_n-l_n)/2`, and define `hat D`, `hat Omega` using these **rational midpoint atoms**.

Because all sixteen translations by multiples of 1/16 remain within the same affine/wrap branch on each certified interval, the relevant translation maps are 1-Lipschitz *on that interval*. Coupling each real phase with its midpoint yields:

```
|D_N-hat D_N| <= 2/N sum_(n<N) epsilon_n.
|Omega_M-hat Omega_M|
  <= (eta_early+eta_late)/2 + eta_entire,
eta_early=2/M sum_(n<M)epsilon_n,
eta_late=2/M sum_(M<=n<2M)epsilon_n,
eta_entire=1/M sum_(n<2M)epsilon_n.
```

All quantities on the right are **exact rationals**. The middle statistic is calculated as a rational CDF integral, not via floating point, arbitrary source mutation or an unverified character table. `Omega_M` belongs to the genuine zero-seed π orbit because the phase intervals are certified from its original BBP source. For any finite M, chart refinement terminates by irrationality and convergence. The returned interval has lower bound `max(0,hat Omega-error)` and upper bound `hat Omega+error`.

**The seam control matters:** without a fixed digit chart, `z->(z+a/16) mod 1` can jump in the ordinary interval metric; a global W1 Lipschitz claim is false. `test_haar_branch_seam_is_not_globally_lipschitz` provides an exact rational counterexample.

**Remaining proof debt:** no estimate of `Omega_M` at every large M or of source-selected signed Weyl means follows from the finite output. In particular we do NOT claim `Omega_M/D_M` has a positive uniform lower bound, that `D_N` is monotone, or that π is normal.

## ZI-09. The required next discriminator (OPEN)

The proposed source-locked data object can be plugged into the #591 inequality `D_(2M)=(D_early+D_late)/2-Omega_M` and the #593 mixed-joining observer, preserving literal source/zero, prime-power and real winding semantics. A meaningful next theorem would bound the **selected signed** overlap or a full odd/every nonzero Fourier family with a quantified all-large-epoch error, ruling out coherent counterseeds and positive source mimics. The same infrastructure reconstructs nonnormal computable irrationals when its original-source passport is removed, so *reconstruction alone cannot deliver that theorem*. No weakening of the normality gate is silently promoted.
