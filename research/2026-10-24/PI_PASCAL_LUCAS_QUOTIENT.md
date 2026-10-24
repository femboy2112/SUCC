# Operation Pascal Quotient: Lucas incidence, coherent prime operators, and lost carry information

**Date:** 2026-10-24. **Proposed ancestry:** SUCC draft #273 at `8d89711db77fea81920321d32f831eed3dec1e68`, inheriting draft #272 at `6e8fa8b77886b13f1f533ed8083fd88c849d14b3`. **Research-only.**

**Authority:** elementary paper proofs, classical Lucas's theorem, independent exact-integer controls; no new Lean kernel authority, no independent external mathematical refereeing. **Pi normality, authentic real half retention, the 1/16 carry-frequency bound, and same-law tripling remain OPEN.**

## 1. Source of the question and immediate resolution

Two familiar formulas both produce `3^m`:

$$
\sum_{j=0}^m {m\choose j}2^j=3^m,\qquad
\#\{(n,k):0\le k\le n<2^m,\;{n\choose k}\text{ odd}\}=3^m.
$$

The tempting proposal is to quotient the *non-weight-two* forms out of the weighted-binomial forms. The unambiguous combinatorial reading has an important correction: **there are no leftover cells. Both formulas are two enumerations of the same finite incidence object.** Set

$$
\mathcal L_{2,m}=\{(n,k):0\le n,k<2^m,\;k_i\le n_i\text{ at every binary place }i\}.
$$

Lucas's theorem identifies `L_{2,m}` exactly with the odd cells. At each place `(n_i,k_i)` is one of `(0,0),(1,0),(1,1)`. A word in these three symbols is simultaneously (i) a pair of nested subsets `B subseteq A subseteq [m]`, and (ii) a ternary word with digit `d_i=n_i+k_i`. The map

$$
\Psi_m(n,k)=\sum_{i=0}^{m-1}(n_i+k_i)3^i
$$

is a canonical digit-order-preserving bijection `L_{2,m} -> {0,...,3^m-1}` with inverse `0 -> (0,0)`, `1 -> (1,0)`, `2 -> (1,1)` digitwise. The weighted sum first chooses `A` of size `j` and then chooses `B subseteq A`; the odd-cell count first enumerates all pairs. Consequently, subtracting the two totals or identifying the two sets *under Psi* gives zero residual. There is no canonical set of 'non-weight-two' parity cells to remove. The nontrivial alternative is an **observable quotient**, whose discarded fiber carries information.

### Bivariate exact refinement

With `a=|A|=s_2(n)` and `b=|B|=s_2(k)`, the common enumerator is

$$
\boxed{\sum_{(n,k)\in\mathcal L_{2,m}}u^{s_2(n)}v^{s_2(k)}
=(1+u+uv)^m
=\sum_{a=0}^m{m\choose a}u^a(1+v)^a.}
$$

The coefficient of `u^a v^b` is `{m\choose a}{a\choose b}`. Setting `v=1` is precisely the weight `2^a`. Thus the weight-two structure is already implicit in each parity cell, and is recovered by forgetting `B` while counting its fibers. This is a combinatorial identity, not a claim about the source of pi's binary digits.

## 2. An exact commutative quotient of Pascal operators

Let `V_m=Q^{P([m])}`, functions on all subsets of `[m]`. Define the Boolean incidence/zeta transform

$$
(Z_mf)(A)=\sum_{B\subseteq A}f(B),\qquad
Z_m=\begin{pmatrix}1&0\\1&1\end{pmatrix}^{\otimes m}.
$$

The integer entries of `Z_m`, indexed by the binary numbers `n,k`, are `1` exactly when `{n\choose k}` is odd. **This is the support of Pascal modulo 2, not the unrestricted integer Pascal matrix.**

Define the rank-average map `P_m:V_m -> Q^{m+1}` by

$$
(P_mf)(r)=\frac1{{m\choose r}}\sum_{|A|=r}f(A).
$$

Define `T_m` on rank functions by `(T_mg)(r)=sum_{j<=r}{r\choose j}g(j)`.

**PLQ-02 (PROVED PAPER): exact intertwining.** For every rational `f`,

$$
\boxed{P_mZ_m=T_mP_m.}
$$

*Proof.* First symmetrize `f` over `S_m`. The zeta operator is equivariant for coordinate permutations, so symmetrization commutes with it. On a symmetric function `f(B)=g(|B|)`, each `A` of size `r` contains `{r\choose j}` subsets of size `j`; hence `(Z_m f)(A)=sum_{j<=r}{r\choose j}g(j)`. Composing gives the stated equality for arbitrary `f`. Alternatively count incidences `B subseteq A` across fixed ranks and use `{m\choose r}{r\choose j}={m\choose j}{m-j\choose r-j}`. QED.

The map `P_m` is surjective, and

$$
\boxed{0\longrightarrow K_m\longrightarrow V_m\overset{P_m}{\longrightarrow}\mathbb Q^{m+1}\longrightarrow0,\qquad
\dim K_m=2^m-(m+1).}
$$

The kernel `K_m` is invariant under `Z_m`; the induced operator on `V_m/K_m` is exactly the truncated binomial successor `T_m`. For `m=4`, this loses `11` vector-space dimensions of positional information. **Neither `11` nor `16` is a frequency bound on pi**. Applying `Z_m` to the all-ones vector yields `(Z_m 1)(A)=2^{|A|}` and pairing with all-ones gives `3^m`. Therefore the two constructions are the same operator viewed before and after quotient.

A nonzero hostile kernel element at `m=2` is `f({0})=+1, f({1})=-1`, with `f(empty)=f({0,1})=0`. It has `P_2 f=0`; `P_2Z_2f=0` too. Both positions matter even when *all rank-averaged transforms* are blind to their difference.

## 3. Prime-specific generalization: a coherent tensor tower

For prime `p` define the digit-pair alphabet

$$
\mathcal A_p=\{(a,b):0\le b\le a<p\},\quad
L_p=|\mathcal A_p|=p(p+1)/2.
$$

Define `V_{p,m}=Q^{\{0,\ldots,p^m-1\}}` and its **support** zeta operator

$$
Z_{p,m}=J_p^{\otimes m},\qquad
(J_p)_{a,b}=\begin{cases}1&b\le a,\\0&b>a.\end{cases}
$$

Lucas's theorem implies `Z_{p,m}[n,k]=1` iff `{n\choose k}` is nonzero mod `p`. The support count and row count are

$$
\boxed{\#\mathcal L_{p,m}=L_p^m,\qquad
\#\{k:{n\choose k}\not\equiv0\pmod p\}=\prod_i(n_i+1).}
$$

An explicit base-`L_p` address uses digit code `c_p(a,b)=a(a+1)/2+b`. It bijects the prime-Lucas cells and the words in `L_p` symbols, respecting *prefix extension*:

$$
\Psi_{p,m+1}(n+ap^m,k+bp^m)=\Psi_{p,m}(n,k)+c_p(a,b)L_p^m.
$$

It is **not generally a homomorphism of p-adic additive groups**. In particular `L_2=3`, `L_3=6`, `L_5=15`. The identity `L_p=p+1` holds only at `p=2`, so extrapolating the same 'p becomes p+1' statement to every prime is false.

Coordinate permutations form `S_m` for each `p`. Quotient by the digit-histogram `h=(h_0,...,h_{p-1})`, `sum h_a=m`, of the *source index* `n`; the quotient has dimension `{m+p-1\choose p-1}`. The induced operator has coefficients

$$
[\mathbf x^{\mathbf b}]\prod_{a=0}^{p-1}(x_0+\cdots+x_a)^{h_a}
$$

from output histogram `h` to input histogram `b`. The quotient is **exactly intertwined** with `Z_{p,m}`, by the same permutation-equivariance argument. At `p=2` the quotient reduces to the binomial transform. This supplies a coherent prime-indexed family of finite operator quotients, not a canonical map of actual p-adic arithmetic across different primes.

### Important prime-phase obstruction (p=3 immediately fails)

For `p>2`, the *residue* of a surviving Pascal cell need not be `1`. Define

$$
(C_{p,m})_{n,k}\equiv{n\choose k}\pmod p,\quad
C_{p,m}=B_p^{\otimes m}\text{ in }\mathbb F_p,\quad
(B_p)_{a,b}={a\choose b}\pmod p.
$$

The support operator `Z_{p,m}` **forgets nontrivial residue units**: `C_{2,m}=Z_{2,m} mod 2` but `C_{3,1}[2,1]=2=-1 mod 3` while `Z_{3,1}[2,1]=1`. Thus prime-base transfer based on support counts alone loses phase/sign information already at a single digit. Neither a real source phase nor a selected carry history can be reconstructed from these support counts in general.

## 4. Two independently measurable transfer obstructions

### 4.1 Uniform prime-base inclusion: exponentially vanishing overlap

For `p<q`, include digit pairs with `a<p` from `A_p` into `A_q`. On these principal coordinates the **support** incidence operators agree exactly. But `A_q` contains extra states. The uniform law on `A_q^m` and the pushforward of uniform `A_p^m` have total-variation distance

$$
\boxed{\mathrm{TV}_{p\hookrightarrow q}(m)=1-\left(\frac{L_p}{L_q}\right)^m.}
$$

*Proof.* The image contains `L_p^m` of the `L_q^m` equally likely states. On the image the embedded law has mass `L_p^{-m}` per state, greater than the full law's `L_q^{-m}`. Total variation is `1` minus full-law mass of the image. QED.

At `p=2, q=3`, `L_2/L_3=1/2`, so the overlap at four digit positions is `1/16` and the variation distance is `15/16`. **This is a support-overlap identity, not the real-circle four-gate probability required for pi normality.** It is a positive/negative control for confusing geometric fractions with selected-source statistics.

### 4.2 Ternary SUCC does not descend through digit histograms

The ternary address `Psi_m` makes addition `a -> a+1 mod 3^m` into a well-defined transformation on *full* Lucas pairs. However it does NOT descend to the rank quotient or even the complete digit-histogram quotient: at depth 2, ternary words `(0,1)` and `(1,0)` (least significant digit first) have identical histograms; their successor words `(1,1)` and `(2,0)` have different histograms. Thus no deterministic map of the quotient can make the SUCC diagram commute. This is an exact **non-congruence** counterexample. It does not bar a lifted successor carrying positional state.

The full depth-compatible digital map gives a homeomorphism between `Z_3` and the closed digitwise Lucas-pair subset of `Z_2 x Z_2`. If the first differing digit is `j`, their p-adic ultrametrics satisfy

$$
 d_{2,\mathrm{pair}}=2^{-j}=\bigl(3^{-j}\bigr)^{\log 2/\log 3}.
$$

This is a precise snowflake/Hölder transfer of **digit topology**, not of additive dynamics, arithmetic measures, or pi's real orbit. For distinct primes, a continuous additive group homomorphism `Z_p -> Z_q` must be zero: `p^n -> 0` in `Z_p`, but `|p^n a|_q=|a|_q` for nonzero `a` in `Z_q`. This is a sharp boundary between topological coding and additive arithmetic.

## 5. Quantified four-bit information deficit: a hostile distribution

Fix `m>=4`. Sample binary `n` uniformly in `{0,...,2^m-1}` and let `k=0`. Every `(n,0)` is a valid odd Pascal cell, but this distribution **is not** the uniform distribution on all odd Pascal cells and is not the authenticated BBP source. Define the four-bit gate

$$
G(n)=\mathbf1_{n\bmod16=0},\qquad\mathbb EG=1/16.
$$

Let `R=s_2(n)` be the rank, and estimate `G` using only `R`. The optimal mean-squared estimator is

$$
\widehat G(R)=\mathbb E(G\mid R)=\frac{{m-R\choose4}}{{m\choose4}}.
$$

The **exact irrecoverable conditional error** is

$$
\boxed{\mathcal E_m=\inf_{g}\mathbb E\bigl(G-g(R)\bigr)^2
=\frac1{16}-\frac1{{m\choose4}}\sum_{s=0}^{4}
{4\choose s}{m-4\choose4-s}2^{-(8-s)}.}
$$

Use `{a\choose b}=0` outside the range `0<=b<=a`.

*Proof.* Conditional on `R`, the zero-bit positions form a uniform `(m-R)`-subset; all first four are zero with the stated hypergeometric probability. Its squared expectation can be computed by selecting two independent four-subsets `S,T` of `[m]`: the probability that both are all zero is `2^{-|S\cup T|}`. Count `|S\cap T|=s` via `{m\choose4}{4\choose s}{m-4\choose4-s}`, divide by `{m\choose4}^2`, and subtract from `E[G^2]=1/16`. QED.

In particular `E_4=0` (the rank knows whether all four bits are zero), `E_5=1/40`, and `E_m -> 15/256` as `m -> infinity` (the rank fraction concentrates at `1/2`, while `G` retains Bernoulli variance `(1/16)(15/16)`). Finite cases were checked independently by enumerating every binary `n`; the limit is a paper consequence of concentration.

A stronger **pointwise** obstruction is available: for `m>=5` choose `n=2^4` and `n'=1`, both rank one and `k=0`. They have opposite four-bit gate values. Consequently any rank-only predictor has worst-case absolute error at least `1/2`, a bound attained by the constant `1/2` predictor. The quotient cannot determine the gate even when all exact binomial identities remain true.

## 6. Source-faithful interpretation and the real pi-normality contract

For a measure `mu` on length-m Lucas states, let `P` average observables under coordinate permutations and let `mu_sym` be its symmetrized measure. For any bounded observable `G`, the exact identity is

$$
\boxed{\mathbb E_{\mu}G-\mathbb E_{\mu}(PG)
=\mathbb E_{\mu}(G-PG).}
$$

For `0<=G<=1`, the magnitude is at most `TV(mu,mu_sym)`; this bound is sharp. At depth five, the synthetic point source `mu=delta_{n=16,k=0}` has rank-one symmetrization supported uniformly on the five one-bit positions. The four-bit gate has `E_mu G=1`, `E_mu(PG)=1/5`, and `TV(mu,mu_sym)=4/5`, so equality holds. This source is **not** pi. The right side is **the selected positional-fiber term**. Even perfect rank data leave it unbounded without source information; uniform/Haar averages can annihilate it without controlling its value along the authentic BBP history. One may retain the full fiber with a source-labelled state rather than quotienting it away.

The existing authenticated BBP recurrence is `U_0=0`, `U_n=16U_{n-1}+r(n)`, `y_n={U_n}`, with fixed four-pole forcing `r` (drafts #272–273). Nothing in the Lucas tensor system, the p-adic coding homeomorphism, the exact TV overlap, or the synthetic four-bit probability provides an authenticated factor from `(U_n,carry_n)` into our Lucas-pair process. **Such a map must be defined, proved to preserve the literal integer lift and the selected real-circle gate, and then shown to have controlled nonsymmetric fiber correlations.**

A worthwhile conditional research program is to seek maps `C_{p,m}` from BBP source histories to Lucas-digit states, together with an actual gate `G` and a signed source-correlation estimate

$$
\left|\frac1N\sum_{n<N}\Bigl(G(C_{p,m}(U_n))-PG(C_{p,m}(U_n))\Bigr)\right|\longrightarrow0
$$

with an *independently proved* term relating `G(C_{p,m}(U_n))` to the original selected four-bit carry. There is no constructed map or such bound yet. Mere symmetrization of the model is not sufficient; it replaces the source. Equally, the existing signed Fourier jet `J_R` from sibling #271 remains an unbounded selected-source term. Our finite quotient theorem does not discharge it.

### Strong adversarial controls and verdict

- **Mutation A: numerical-only quotient.** `3^m-3^m=0`, so any alleged positive leftover count is REFUTED. Repair: retain the nontrivial kernel of the rank projection, not a difference of cardinalities.
- **Mutation B: assume prime support preserves residues.** `p=3`, `(a,b)=(2,1)` gives `2 != 1 mod 3`. REFUTED.
- **Mutation C: assume rank/histogram determines successor.** The two depth-two ternary words above disprove it. REFUTED.
- **Mutation D: assume four-bit count 1/16 passes to the authentic BBP orbit.** NO authentication or frequency probe exists; UNVERIFIED (not a counterexample to pi).
- **Mutation E: read support-overlap 1/16 as real-circle frequency.** Different sample spaces and measures; typed contradiction, REFUTED.
- **Survivor:** prime-indexed Lucas support tensor tower, rational symmetric quotients, explicit loss fibers, and source-indexed conditional transfer contracts. PROVED PAPER with exact finite tests; scholarly novelty UNVERIFIED.

### Next verdict-changing probe

Use the authenticated source from #272 and selector machinery from #273 to construct **one explicit source-labelled, integer-carry-preserving observable into the Lucas full fiber**. Check whether its four-bit gate matches the original circle carry at each of a frozen set of windows, using genuine BBP rational intervals, and supply an adversarial altered-source control with the same rank histogram. If the representation fails, retain that failure; if it succeeds, a genuinely new source-specific bound on its nonsymmetric correlation is needed. In either case, the target is the authentic selected real carry, not another unweighted count.

## 7. Provenance, reproducibility and authority

Inherited source: #272 `PI_PASCAL_SYNTHESIS.md` (authentic BBP Pascal valuations, source filters, and source-height bounds); #273 `PI_PATH_SELECTION_SYNTHESIS.md` (exact source selection and path limitation); separate sibling #271 `PASCAL_CARRY_INTERFEROMETRY.md` (selected Walsh/Fourier jet). No existing source code or frozen archives were changed here.

Classical inputs: Lucas's theorem (1878), e.g. [Mathlib's formal Lucas statement](https://teorth.github.io/analysis/docs/Mathlib/Data/Nat/Choose/Lucas.html), and the elementary permutation-equivariant Boolean-lattice zeta transform. The tensor/support/symmetric-quotient results are direct derivations, **not claims of novel discovery or independent formalization**.

Reproduce new finite probes:

```sh
python -m unittest discover -s tests -p 'test_pascal_lucas_quotient.py' -v
python scripts/pascal_lucas_quotient_probe.py
```

The new module is `observational_succ/pascal_lucas_quotient.py`; the new tests and probe are independent code paths where indicated. Claims PLQ-01--14 are recorded in `docs/CLAIM_SUPPLEMENT_PASCAL_LUCAS_QUOTIENT.md`. Full repository gates and hosted CI must be reported **separately** from this focused result.
