# BBP computational graph: algebraic resonance, holonomic closure, and the statistical fixed-point seam

**Research stage:** local source-first exploration, November 10, 2026.  
**Upstream:** `femboy2112/SUCC`, draft PR #579 at `c3923bb35fed371fcd290ce65b8c36f378f92f28` (not merged), based on audited Main XXII.  
**Authority:** exact polynomial, rational, and operator identities derived below. The BBP quartic reduction itself is classical, present in the original Bailey–Borwein–Plouffe paper; no discovery or priority claim. No proof of hexadecimal normality or parity balance.

## Purpose: read the graph, not merely its final value

The present source-first fold constructs:

```text
four genuine BBP poles --> moment polynomial P(x) --> G_z fixed point K_z(x)
             |                                        |
             |  holonomic differential system        | sampled Mellin M
             v                                        v
  ordinary generating function Phi(z) <---------- indexed tail fixed point B(n)
             |                                        |
             | z=1/16                                | original U_0=0, completed tail
             +---------------------> alpha=pi/16 <---+
                                         |
                                   x -> 16x mod 1
                                         |
                            Abel orbit fixed point mu_rho
                                         |
                    rho -> 1: invariant measure SELECTION
                                         |
                        full fixed-h Weyl decay [OPEN]
```

The source fold is a uniform contraction. The **statistical** fixed-point equation becomes noncontractive at the boundary. Keep those two distinct.

## R-01 — exact source polynomial resonance (paper proof)

Let

```math
P(x)=4-2x^3-x^4-x^5=(1-x)(x^2+2)(x^2+2x+2),\quad K_z(x)=\frac{P(x)}{1-zx^8}.
```

The resultants are **exact**:

```math
\operatorname{Res}_x(P(x),1-zx^8)=(1-z)(1-16z)^4.
```

Proof: the five roots of P are x=1, x=±i√2, and x=-1±i. The latter four have x^8=16 and x=1 has x^8=1. Since P's leading coefficient is -1 and the second polynomial has degree 8, its resultant is precisely the product of `(1-z*x_root^8)` over the five roots. Distinctness follows from the displayed factorization.

Consequently, for real 0<z<1 the numerator and denominator have a common root **only at z=1/16**, with gcd

```math
\gcd(P,1-x^8/16)=(x^2+2)(x^2+2x+2)
```

up to a unit. At the authentic BBP parameter:

```math
K(x)=K_{1/16}(x)=\frac{16(1-x)}{(2-x^2)((x-1)^2+1)}.
```

This cancels two quadratic factors of `16-x^8` and leaves the real-quadratic factor `2-x^2` and Gaussian factor `(x-1)^2+1`. The resulting quartic-integral form is **classical BBP 1997**, not new. Source: Bailey, Borwein & Plouffe, *On the Rapid Computation of Various Polylogarithmic Constants*, Mathematics of Computation 66 (1997), eqs. (1.2)-(1.4), https://www.pi314.net/ref/BaileyBorweinPlouffe.pdf.

The exact primitive

```math
\Phi_*(x)=4\arctan(x-1)+2\log\frac{2-x^2}{(x-1)^2+1}
```

satisfies `Phi_*'(x)=K(x)`; `Phi_*(0)=-pi`, `Phi_*(1)=0`. The log ratio is 1 at both endpoints, and pi comes from the angular displacement. This does NOT imply anything about hexadecimal digit frequencies.

**Typed limitation:** the resultant vanishes in *parameterized algebraic geometry*. It does not make the Banach fixed-point operator degenerate: `G_z(f)=P+zx^8f` remains a strict contraction for `0<z<1`.

## R-02 — exact four-channel holonomic differential shortcut (paper proof)

For |z|<1, define

```math
\mathcal A(z)=\sum_{n\ge0}R(n)z^n=\int_0^1\frac{P(x)}{1-zx^8}\,dx,
\quad R(n)=\frac4{8n+1}-\frac2{8n+4}-\frac1{8n+5}-\frac1{8n+6}.
```

Let `theta=z*d/dz`, and let `L_a=8theta+a`, a in `{1,4,5,6}`. For the individual pole series `J_a(z)=sum_{n>=0} z^n/(8n+a)`, coefficient comparison proves `L_a J_a=1/(1-z)`. Since the `L_a` commute, a direct rational calculation gives

```math
\boxed{\left[\prod_{a\in\{1,4,5,6\}}(8\theta+a)\right]\mathcal A(z)
=\frac{8(16z^2+177z+47)}{(1-z)^3}.}
```

Independent coefficient certificate: for every n>=0,

```math
\left[\prod_a(8n+a)\right]R(n)=8(120n^2+151n+47).
```

Thus the *infinite source summation* has a finite-rank differential-operator description as well as the source-specific analytic fixed-point root. This is a **holonomic/G-function-type form**; Lagarias (2001) already identified G-function connections in this normality program. It is not a digit-frequency theorem. Source: https://doi.org/10.1080/10586458.2001.10504456.

## R-03 — an opposite structural result: infinite radix-16 decimation rank

Define `r_k(n)=R(16^k n)` for k>=0, viewed as rational functions of n. Its simple poles are

```math
-\frac{a}{8\cdot16^k},\quad a\in\{1,4,5,6\}.
```

These pole sets are pairwise disjoint: equality between levels k>j would require `a=16^(k-j)b`, impossible when `1<=a,b<=6`. Hence the rational functions `{r_k : k>=0}` are linearly independent over C, by evaluating any finite linear combination at the unique pole belonging to its last nonzero term.

**Conclusion:** the source has *finite differential/holonomic closure* but *infinite-dimensional linear closure under repeated index decimation*. A finite-state clock may still compute it using an unbounded integer register; the theorem rules out only finite-dimensional linear span of these decimated rational functions. This graph contrast is a concrete criterion for where a proposed “finite algebraic shortcut” must transport information between distinct bases.

## R-04 — the second fixed point and the critical boundary

Let `alpha = A(1/16)/16 = pi/16`, `T(x)={16x}`, and, for 0<rho<1,

```math
\mu_\rho=(1-\rho)\sum_{n\ge0}\rho^n\delta_{T^n\alpha}.
```

Then

```math
\boxed{\mu_\rho=(1-\rho)\delta_\alpha+\rho T_*\mu_\rho.}
```

The right-hand side is a contraction with factor rho on finite signed measures in total variation, so for each rho<1 the probability solution is unique. At rho=1 the equation loses this contraction: it only demands `T_*mu=mu`, admitting Haar and infinitely many non-Haar invariant measures. Every weak limit of `mu_rho` as rho approaches 1 is T-invariant; source-selected uniqueness of the Haar boundary is not provided.

On Fourier characters `e_h(t)=exp(2 pi i h t)` we get the **frequency-tree fixed point**

```math
m_\rho(h)=(1-\rho)e_h(\alpha)+\rho m_\rho(16h).
```

A source-specific estimate making `m_rho(h)->0` at rho↑1 for each fixed h≠0 would yield the corresponding normality target (with the standard positive-sequence Tauberian passage from Abel means to Cesaro means). **The new opportunity is to seek a genuinely independent identity on the source-selected Fourier branch at rho=1**, not merely a new parameterization of `m_rho`.

**Hostile control:** take alpha=1/255. Then T has a two-cycle `{1/255,16/255}` and the uniquely defined finite-rho fixed point is exactly

```math
\mu_\rho=\frac1{1+\rho}\delta_{1/255}+\frac{\rho}{1+\rho}\delta_{16/255}.
```

As rho↑1 it approaches a non-Haar invariant measure, and the Fourier mode h=255 equals 1 at every rho. Thus **uniqueness of every finite-resolution fixed point does not enforce Haar at the infinite boundary**.

## R-05 — resonance plus positivity *and quadratic decay* still do not enforce normality

Let `D4=(2-x^2)((x-1)^2+1)` and define

```math
J(x)=\log\frac{2-x^2}{(x-1)^2+1},\qquad
K_{\mathrm{fake}}(x)=2(1-x)+\frac1{10}\big(4x-2+J'(x)\big).
```

It has the exact rational simplification

```math
K_{\mathrm{fake}}(x)=\frac{(1-x)H(x)}{5(2-x^2)((x-1)^2+1)},
\quad H(x)=38-34x-x^2+17x^3-8x^4.
```

For x in [0,1], `H(x)>=38-34x-x²>=3` because `17x³-8x⁴>=0`; hence the kernel is strictly positive for 0<=x<1 and vanishes at x=1. Its integral is exactly **1**: the integral of `2(1-x)` is 1, that of `4x-2` is zero, and `J(1)-J(0)=0`.

Define the polynomial source

```math
P_{\mathrm{fake}}(x)=(1-x^8/16)K_{\mathrm{fake}}(x)
=\frac{(1-x)(x^2+2)(x^2+2x+2)H(x)}{80}.
```

It shares the **same fourfold gcd** `(x²+2)(x²+2x+2)` with `1-x^8/16`; the remaining factor `H` has no common root at the other four denominator poles (exact polynomial gcd tested). The fake moment forcing `R_fake(n)=int_0^1 x^(8n) P_fake(x) dx` is rational and strictly positive; because `P_fake(1)=0` with a nonzero first-order zero it is `Theta(n^-2)`. Its analytic fixed-point equation is contractive for 0<z<1, the selected sum is 1, and the *zero-seeded* base-16 circle orbit is identically 0, hence nonnormal.

**Refuted:** fourfold parameter resonance + positive rational source + vanishing endpoint + quadratic moment decay + unique bounded fixed point + literal zero seed imply normality. **Not refuted:** the exact original **four signed poles and their coefficients**, which the mutant does not preserve (its polynomial has degree 9 and more source moments). The control deliberately attacks a weaker structural inference, not the authentic source.

## R-06 — exact source-root oscillator boundary identity (with a no-gain receipt)

Let `H(x)=Phi_*(x)+pi`, so `H(0)=0`, `H(1)=pi`, and `H'(x)=K(x)>0` for `0<=x<1`. For every real t≠0, the fundamental theorem of calculus yields

```math
\boxed{\int_0^1 K(x)e^{itH(x)}\,dx=\frac{e^{it\pi}-1}{it}.}
```

At the digit-orbit frequencies `t_n=2*pi*h*16^n`, for each nonzero integer h this becomes the **exact source-derived pin**

```math
\boxed{e^{2\pi i h16^n\pi}=1+2\pi i h16^n
\int_0^1 K(x)e^{2\pi i h16^nH(x)}\,dx.}
```

The integral has bound `<=2/|t_n|=O(16^-n)`. **This is not a signed saving of the orbit Weyl sum**: multiplying by `t_n` in the displayed identity exactly restores the order-one boundary phase. More fundamentally, substituting `y=H(x)` converts `K(x)dx` to the uniform Lebesgue measure `dy` on `[0,pi]`—the source-specific geometry disappears under this particular probe. A useful next pin must use a different, authenticated signed weight (e.g. separate four-pole channels, source-carry phase, or a tested nontrivial cofactor), and establish a gain **after** frequency multiplication. This is an exact diagnostic of a tempting false shortcut.

## Interpretation / next verdict-changing probe

The exact graph has at least three distinct interfaces:

1. **Algebraic pole cancelation** at z=1/16 (fourfold resultant root), with the classical angular/log primitive.
2. **Finite holonomic source action** in z, alongside **infinite radix-16 decimation span** in n.
3. **Critical invariant-measure selector** at rho↑1, where the finite contraction gap disappears.

The research target is a **new cross-interface constraint** derived from the exact source coefficients and the marked zero seed, which eliminates non-Haar boundary measures. A potentially sufficient form is a source-derived signed coboundary

```math
e(h16^n\alpha)=\Psi_h(n+1)-\Psi_h(n)+\varepsilon_{h,n},
```

with a *constructively bounded* `Psi_h(N)=o(N)` and `sum_{n<N} epsilon_{h,n}=o(N)`, proved independently of the desired Weyl bound. Do not define `Psi` as the unknown Weyl partial sum and call it a theorem. Alternatively, prove an independent source-selected half-turn/Haar defect estimate from the exact carry and future-tail graph of PR #579.

**Next falsifier:** derive any proposed Fourier gain also for `P_fake`, or for the original BBP forcing with a coherent wrong seed. If it survives these controls without a source-specific distinction, it cannot establish original-zero normality.

**Status ledger:** R-01 classical exact factor/resultant; R-02 exact holonomic operator; R-03 proved pole-space independence; R-04 classical measure-resolvent identity and non-Haar boundary control; R-05 explicit positive hostile polynomial; R-06 exact oscillator boundary identity with no signed gain; source-selected Fourier/Haar gain **UNVERIFIED**; original-zero parity, pi hexadecimal normality and RH **OPEN**.

**Local validation:** companion `bbp_graph_shapes_probe.py` verified 21 assertion families, including 400 exact source coefficient identities, 25 pairwise disjoint decimation pole sets, algebraic resultants/gcds, symbolic primitive, and hostile rational fixed points. SymPy used for symbolic checks; no independent kernel proof or full SUCC suite claimed. No GitHub changes from this local exploration.
