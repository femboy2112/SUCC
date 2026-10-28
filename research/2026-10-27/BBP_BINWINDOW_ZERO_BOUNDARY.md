# Operation Goldbach–Seinfeld Bin Window: the authentic BBP 2-adic zero boundary and canonical odometer

**Research date:** 2026-10-27. **Source:** original `femboy2112/SUCC` four-pole BBP source, zero seed, stacked from research PR #320 `5ea12570aec86c3a8b555e927c10337804568a62`. **Status:** `PAPER-PROVED` source-specific 2-adic theorem, `EXACT FINITE` implementation and holdouts, **real-circle base-16 π normality OPEN**. No outside academic-priority claim. No immutable imported theorem, original source file, main branch, or historical archive modified.

## 0. Steelman the proposed Goldbach–Seinfeld sliding window

The author's proposal is to treat the natural-number line as a compatible hierarchy of finite arithmetic bins rather than merely a list traversed one element at a time. The time `n` indexes a *window of forms* attached to original source indices `a=n-s`. As the window slides, the same source value can appear in different observation slots, multiplied by `16^s`. The proposed “Goldbach-shaped” operation is **additive index incidence** `a+s=n`; unlike Goldbach's conjecture this involves all available natural indices, not a theorem that two primes sum to a prescribed integer. Nontrivial number theory enters through the actual source map, not this bijective reindexing.

For precision `16^k`, if `n>=k`, the authenticated recurrence has the exact finite identity

$$
U_n=\sum_{a=1}^n16^{n-a}r(a),\qquad
U_n\equiv\sum_{s=0}^{k-1}16^s r(n-s)
=\sum_{a=n-k+1}^n16^{n-a}r(a)\pmod{16^k}.
$$

The pair `(a,s)` lies on the diagonal `a+s=n`. Across a finite time interval `[L,H)`, double counting gives the exact identity

$$
\sum_{n=L}^{H-1}\sum_{s=0}^{k-1}16^s r(n-s)
=\sum_a r(a)\sum_{\substack{0\le s<k\\ L\le a+s<H}}16^s.
$$

An interior index `a` appears exactly `k` times, with differently weighted contributions. **Reindexing alone is not an independence or real-Fourier cancellation theorem.** The first genuinely source-dependent step is to ask whether the finite bin maps patch into a coherent global function.

## 1. Original BBP source extends 2-adically

The unchanged four signed poles cancel to the rational function

$$
r(x)=\frac{4}{8x-7}-\frac2{8x-4}-\frac1{8x-3}-\frac1{8x-2}
=\frac{120x^2-89x+16}{(2x-1)(4x-1)(8x-7)(8x-3)}.
$$

At positive integers this is literally the authenticated source. For `x∈Z_2` **we separately declare its rational analytic extension**; negative arguments are *not* claimed to be experimentally observed negative-time forcing events. All denominator factors are odd 2-adic units.

The `PAPER-PROVED` isometry inherited from PR #320 is

$$
v_2(r(x)-r(y))=v_2(x-y)\qquad(x\ne y,\ x,y\in Z_2).
$$

Indeed the numerator difference divided by `x-y` is `120(x+y)-89`, odd; denominator differences divided by `x-y` are even. All denominators are units.

## 2. A canonical infinite-past window

Because `|16|_2=1/16`, define

$$
\boxed{\Phi(x)=\sum_{s=0}^{\infty}16^s r(x-s),\qquad x\in\mathbb Z_2.}
$$

This converges uniformly on `Z_2`. It is a source-defined continuous function and satisfies

$$
\boxed{\Phi(x+1)=16\Phi(x)+r(x+1).}
$$

This is **not** an ordinary real convergent sum for negative-time terms; the completion and convergence are explicitly 2-adic. At the original boundary `x=0` it has an apparent constant

$$C_{\rm past}=\Phi(0)=\sum_{s\ge0}16^s r(-s).$$

**Theorem BW-1 (PAPER-PROVED, original-source 2-adic cancellation).**

$$\boxed{C_{\rm past}=0\ \text{exactly in }\mathbb Q_2.}$$

### Proof of the source-specific zero (not a numerical extrapolation)

At nonnegative integers `s`, using the original four rational poles,

$$r(-s)=-\frac4{8s+7}+\frac2{8s+4}+\frac1{8s+3}+\frac1{8s+2}.$$

Let `R(t)` be the 2-adically convergent generating function

$$
R(t)=\frac{-4t^6+2t^3+t^2+t}{1-16t^8}
=\frac{t(t-1)}{(2t^2-1)(2t^2-2t+1)}.
$$

On the closed 2-adic unit disc, the termwise antiderivative `J_0(t)` of the power-series expansion of `R(t)`, normalized by `J_0(0)=0`, converges at `t=1`: the `16^s` powers overpower the denominators `8s+j`. By construction,

$$J_0(1)=\sum_{s\ge0}16^s r(-s)=C_{\rm past}.$$

Put `A(t)=1-2t+2t²`, `B(t)=1-2t²`; elementary rational algebra gives

$$
R(t)=\frac18\left(\frac{A'(t)}{A(t)}-\frac{B'(t)}{B(t)}\right)+\frac1{4A(t)}.
$$

Work in `K=Q_2(i)`, let `α=1+i`, `β=1-i`, so `A=(1-αt)(1-βt)` and `α-β=2i`. Both `α` and `β` have strictly positive 2-adic valuation `1/2`; all the logarithm series below converge uniformly on the closed unit disc. Define

$$
\begin{aligned}
J(t)={}&\frac18\left[
\log(1-\alpha t)+\log(1-\beta t)-\log(1-2t^2)
\right]\\
&+\frac{\log(1-\beta t)-\log(1-\alpha t)}{4(\alpha-\beta)}.
\end{aligned}
$$

Direct differentiation verifies `J'=R` and `J(0)=0`. Therefore the formal power-series coefficients of `J` and `J_0` agree, so `C_past=J(1)`. At `t=1`, the three logarithm arguments are, respectively, `-i`, `i`, and `-1`. All are roots of unity. Their convergent 2-adic logarithms vanish (e.g. `4 log(i)=log(i^4)=0` in characteristic zero). Consequently `J(1)=0`, as claimed. **This proof uses the complete authentic four-pole source and does not replace any real arctangent value by a 2-adic value.** QED.

**Finite certificates:** for each `k>=1`, the rational partial sum `C_k=Σ_(s<k)16^s r(-s)` satisfies `C_k≡0 mod16^k`. The exact implementation corroborates this at 48 independently constructed precisions, but that finite check is not the source of the all-`k` claim.

## 3. All-time coherent bins and the new boundary upgrade

The authentic real-rational zero-seeded states obey

$$
U_n=\sum_{s=0}^{n-1}16^s r(n-s),\qquad U_0=0.
$$

Comparing this with the full 2-adic window (for ordinary `n>=0`) yields the **exact** identity in `Q_2`

$$
\Phi(n)-U_n
=\sum_{s=n}^{\infty}16^s r(n-s)
=16^n\sum_{j\ge0}16^j r(-j)
=16^n C_{\rm past}=0.
$$

**Theorem BW-2 (PAPER-PROVED):**

$$\boxed{\Phi(n)=U_n\quad\forall n\in\mathbb N_0,\text{ in }\mathbb Z_2.}$$

This removes the `n>=k` startup restriction of the previously proved finite-window theorem #320. For **every** `n>=0`, `k>=1`, including `n<k`,

$$\boxed{[U_n]_{16^k}=\left[\sum_{s=0}^{k-1}16^s r(n-s)\right]_{16^k}.}$$

The apparent negative-time part when `n<k` is the source-labelled *Seinfeld zero witness*

$$
Z_{n,k}=\sum_{s=n}^{k-1}16^s r(n-s)
=16^n\sum_{t=0}^{k-n-1}16^t r(-t)
\equiv0\pmod{16^k}.
$$

As a rational number `Z_(n,k)` is generally **nonzero**. Its source history remains labelled, but it evaluates to zero in the stated finite residue carrier. The vanishing depends on BW-1, not on generic Fourier averaging. It does not add a statistically independent constraint, nor assert negative-time physical history.

## 4. Isometric bijection and the odometer (no burn-in)

Write `Φ(x)=r(x)+16g(x)`, where `g(x)=Σ_(s>=1)16^(s-1)r(x-s)` is 1-Lipschitz. Then

$$\frac{\Phi(x)-\Phi(y)}{x-y}=\underbrace{\frac{r(x)-r(y)}{x-y}}_{\text{2-adic unit}}
+\underbrace{16\frac{g(x)-g(y)}{x-y}}_{\in16\mathbb Z_2}
$$

is a unit. Hence

$$\boxed{v_2(\Phi(x)-\Phi(y))=v_2(x-y)\qquad(x\ne y).}$$

At every modulus `16^k`, `Φ` induces an injection on a finite set of `16^k` elements and thus a bijection; completeness makes it an isometric homeomorphism of `Z_2`. The original states inherit exact distance preservation for **all times**, including the initial state:

$$\boxed{v_2(U_n-U_m)=v_2(n-m)\quad\forall m\ne n\in\mathbb N_0.}$$

**Corollary BW-3 (PAPER-PROVED):** for each `k>=1`, **every** set of `16^k` consecutive original time indices beginning at `0` or later maps via the original state `U_n mod16^k` to all `16^k` residues exactly once. There is no initial time cutoff. Every fixed nontrivial finite 2-adic Fourier character has exact complete-period cancellation. This result is stronger in startup scope than PR #320; it does *not* strengthen its real-circle selected Weyl estimate.

Define an observable-state successor operation

$$\boxed{\mathcal T(y)=\Phi\big(\Phi^{-1}(y)+1\big)
=16y+r\big(\Phi^{-1}(y)+1\big).}$$

It is conjugate by `Φ` to the adding machine `n→n+1` on `Z_2`. For every `k`, its reduction modulo `16^k` is **one complete cycle**. Thus the source-compatible infinite hierarchy of finite bins is one 2-adic odometer, with `Φ(0)=0` and `U_n=\mathcal T^n(0)`. The map `Φ` is the unique continuous extension of the original time-indexed states because `N_0` is dense in `Z_2`.

### Explicit first hexadecimal bin map

A direct computation in `Z/16Z`, using the complete rational source with unit denominators, gives

$$\boxed{[U_n]_{16}=[r(n)]_{16}=\begin{cases}-n,&n\text{ even},\\2-n,&n\text{ odd} .\end{cases}}$$

It is an involutive permutation. In particular `[U_n]_2=[n]_2` identically: time parity and source-state parity are **perfectly dependent** even though each marginal is exactly balanced. This is a concrete global-calibration guard against inferring independent Gaussian/carry variables from Haar-distributed 2-adic marginals.

## 5. Hostile mutant and boundary discrimination

Reuse PR #320's explicitly **NON-BBP** source

$$T_n^*=\frac{n+1}{(2n+1)(4n+1)(8n+1)},\quad
r^*(n)=16T^*(n-1)-T^*(n),\quad U_n^*=16^n-T_n^*.$$

It is positive at positive times, has odd denominator, correct `15/(64n²)` leading forcing, zero physical seed, and the same all-level 2-adic time equidistribution after a finite cutoff. Its canonical 2-adic infinite-past window, however, telescopes:

$$
\Phi^*(x)=\sum_{s\ge0}16^sr^*(x-s)=-T^*(x),
\qquad\boxed{\Phi^*(0)=-1\ne0.}
$$

Thus

$$U_n^*=\Phi^*(n)+16^n,
$$

explaining **why** the earlier fake passed every fixed-precision sufficiently-late clock test while failing the new source-specific zero boundary. Its real Fourier average still tends to one, not zero. This strengthens the source discriminator without showing that `C_past=0` plus isometry implies normality for every possible forcing. No such universal implication is claimed.

## 6. What this earns toward π, and what remains unpaid

- **Earned:** a source-exact, all-time isometric identification of the natural time bin tree with the 2-adic arithmetic-state bin tree. No probabilistic path averaging, unknown startup threshold, or unverified limit exchange. The exact zero boundary is proven by 2-adic logarithms of torsion and distinguishes the specific existing nonnormal control.
- **Earned:** a source-faithful, continuous extension `Φ` which transforms the time successor into an autonomous state operation `\mathcal T`, giving the proposed SUCC “values as operations” interpretation mathematical content.
- **Not earned:** the selected real-circle signed bound `\sum_{n<=N}e(hU_n)=o(N)` for fixed nonzero integer `h`, and hence base-16 normality of π. The real phase at `U_1=47/15` is `2/15`, whereas its 2-adic mod-16 code gives `1/16`. These are different characters of different locally compact groups. Exchanging them would be a false Fourier transport.
- **Potential next actual theorem:** prove source-specific **real versus 2-adic mixed character** decorrelation beyond exact adic marginal cancellation; or use the canonical source-induced odometer to derive a genuinely nontrivial anti-concentration/real-circle Fourier bound not shared by nearby sources. Exact bin permutations, compatibility, and source-zero boundary alone are *not* the signed estimate.

**Proof policy:** carry original four signed poles and exact zero seed throughout. Adversarial controls include source mutant `U^*`, same-forcing changed seed `V_n=-T_n`, low-order moment twins, fixed-period sparse-digit controls, periodic/mixed-lag aliases and noncartesian Seinfeld branch averaging. New source zero `C_past=0` is a real theorem in `Q_2`; do not call it a real integral of a divergent expression or a normality proof.
