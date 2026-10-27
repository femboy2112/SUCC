# Operation First-Primal Recursion: BBP binary shear gates, 3-adic source trident and CRT clock

**October 27, 2026.** **Authority:** paper proofs below use the original four-pole BBP rational source and the zero-infinite-past source theorem of draft PR #321 (`eeb2a48ea1b43967ea385009a3f8ec280b2efa69`). Arithmetic ingredients (Hensel lifting, CRT, finite-character orthogonality, compatible bit gates) are classical; the combination is a source-specific SUCC research result, **not a claim of external academic priority**. Code/tests: `observational_succ/bbp_primal_recursive_geometry.py`, `tests/test_bbp_primal_recursive_geometry.py`. Every claim about π's **real** normality remains **OPEN**.

## 0. Steelman of the author's 0 → 1 → 2 idea, and the independent reverse direction

`0` is the additive origin; `1` is the first successor and multiplicative identity; `2` is the first positive prime and the uniformizer of the 2-adic filtration. In ordinary integers, 2 is **not** a multiplicative unit. The operational distinction is exact: `S(x)=x+1`, `V_2(x)=2x`, `V_2 S=S² V_2`. The SUCC interpretation is to recursively discover how the original BBP time-to-state map acts on every next bit, **not** to assume that its finite mod-16 reflection is globally valid. The author's suggestion to recurse in the *opposite direction* motivates separately testing the next prime 3 on the same four-pole source rather than treating base 16 as an opaque minimal constant.

The original source, frozen archives and `U_0=0` are immutable. Define

$$
r(x)=\frac4{8x-7}-\frac2{8x-4}-\frac1{8x-3}-\frac1{8x-2}
=\frac{A(x)}{D(x)},
$$

$$
A(x)=120x^2-89x+16,
\qquad D(x)=(2x-1)(4x-1)(8x-7)(8x-3).
$$

The canceled form is algebraically identical to all four signed poles for positive integer `x`. The declared negative-time values and `x∈Z_p` extensions are **rational analytic extensions**, not original observations. Distinguish at every stage the **actual BBP state** `U_n`, the **cleared numerator** `A(n)`, and the selected **real fractional phase** `{U_n}`.

## 1. Binary recursion: every output bit is an input bit plus its prior-state correction

Inherited PR #321 constructs

$$
\Phi(x)=\sum_{s\ge0}16^s r(x-s),\quad x\in\mathbb Z_2,
$$

with a source-specific 2-adic zero boundary `Φ(0)=0`, and shows that `Φ(n)=U_n` for each natural time `n`. The inherited exact isometry reads

$$
v_2(\Phi(x)-\Phi(y))=v_2(x-y)\quad(x\ne y).
$$

The finite-bin part also has an **independent fallback** not depending on the logarithmic boundary theorem: for every `k≥1` and `n≥k`, the original recurrence implies `U_n≡Σ_{s<k}16^s r(n-s) (mod 16^k)`, and this finite map is an isometry.

**Theorem BR-1 (classical compatible-map theorem, source-specialized).** Write an arbitrary 2-adic input as `x=Σ_{j≥0}2^j b_j`, and write `Φ(x)=Σ_{j≥0}2^j y_j`, all `b_j,y_j∈{0,1}`. There is exactly one family of Boolean functions

$$
\boxed{y_j=b_j\oplus f_j(b_0,\ldots,b_{j-1})},
\qquad j=0,1,\ldots .
$$

Proof: let `u=x mod 2^j`. The isometry and compatibility imply `Φ(x)≡Φ(u)+2^j b_j (mod 2^{j+1})`, since `Φ(u+2^j)-Φ(u)` has valuation exactly `j`, and higher input bits disappear modulo `2^{j+1}`. Therefore `f_j(u)` is bit `j` of `Φ(u)`; higher inputs cannot affect it. Conversely, given output `y` modulo `2^K`, reconstruct bit `b_j=y_j XOR f_j(b_0,...,b_{j-1})` in increasing order. This is an exact inverse **without** a search through `2^K` histories. Every finite permutation is compatible with refinement from `2^{K+1}` down to `2^K`. QED.

For source-authentic `Φ` the first bit corrections are:

$$
\boxed{f_0=f_1=0,\qquad f_2=b_1,\qquad
f_3=b_1\lor b_2=b_1\oplus b_2\oplus b_1b_2.}
$$

The full first hexadecimal layer is

$$
\boxed{\Phi(x)\equiv2(x\bmod2)-x\pmod{16}}.
$$

This formula is valid for all 2-adic `x`: the source rational function gives `r(x)≡2(x mod2)-x mod16` on the 16 finite input classes, and the higher window terms are multiples of 16. At the first level `Φ₄²=id`; this **does not extend** to mod 32: exact source values are `Φ₅(2)=30`, `Φ₅(30)=18≠2`.

The first previously unresolved binary correction is nontrivial. Its uniquely determined mod-2 algebraic normal form is

$$
\begin{aligned}
f_4={}&b_1\oplus b_0b_1\oplus b_1b_2\oplus b_3
\oplus b_1b_3\oplus b_2b_3\oplus b_1b_2b_3.
\end{aligned}
$$

The code computes **every further `f_j` automatically** up to a declared finite resource budget, then computes its unique algebraic normal form by the Boolean Möbius transform. For time residue representatives beyond the inherited PR #321 exact-Fraction adapter budget, an independent modular evaluation of the identical canceled four-pole polynomial is used and crosschecked against the original pole formula at large indices. The source-specific values through bit 7 were checked exactly, not extrapolated to a guessed closed form. Although the ANF may require exponentially many monomials, inversion itself uses one evaluation per bit.

**Theorem BR-2 (conjugated successor/odometer).** Let `Φ_K` be the reduction modulo `2^K` and set

$$
T_K=\Phi_K\circ(x\mapsto x+1)\circ\Phi_K^{-1}.
$$

Then `T_K` is a single cycle on all `2^K` states, compatible across all levels. At modulus 16 only,

$$
T_4(y)=\begin{cases}y+1,&y\text{ even},\\y-3,&y\text{ odd},\end{cases}\pmod{16}.
$$

This is a source-derived coordinate change on the ordinary 2-adic adding machine, **not an ergodicity or mixing theorem for the real circle**. It agrees with the corresponding classical compatible-map/T-function picture.

## 2. The reverse prime: 3-adic numerator permutation and four genuine punctures

**Theorem TR-1 (paper-proved).** The *denominator-cleared numerator* `A(x)` is a bijective 3-adic isometry:

$$
\boxed{v_3(A(x)-A(y))=v_3(x-y),\quad x,y\in\mathbb Z_3,\ x\ne y.}
$$

Indeed

$$
A(x)-A(y)=(x-y)[120(x+y)-89],
$$

and `120(x+y)-89≡1 mod3`, a 3-adic unit for every `x,y`. Thus `A` permutes every residue ring `Z/3^L Z`, and Hensel lifting computes its unique inverse one ternary digit at a time. In particular `A(x)≡x+1 mod3`. **This is not a 3-adic isometry statement for the actual quotient `r=A/D` or the original state `U_n`.**

The denominator `D(x)` vanishes modulo 3 at at least one factor for **every** residue class `x mod3`. Its four rational poles

$$
\frac12,\ \frac14,\ \frac78,\ \frac38
$$

all lie in `Z_3` and are genuine (their numerator values are respectively `3/2`, `5/4`, `30`, `-1/2`, all nonzero in `Q_3`). Their exact residues as rational-function poles are

$$
-\frac14,\ -\frac18,\ \frac12,\ -\frac18,
$$

with **signed sum zero**. This is inherited BBP four-pole residue cancellation in a different carrier: globally the pole residues neutralize the `1/x` term, but **locally none of the singularities disappears**. The distinction mirrors Seinfeld's provenance-aware zero: a zero total is not a zero labelled source.

**Theorem TR-2 (paper-proved 3-adic nonconvergence).** For every `x∈Z_3`, the naive reverse-past series

$$\sum_{s\ge0}16^s r(x-s)$$

fails to converge in `Q_3` (if a term hits a pole exactly, it is undefined). Proof: choose positive, strictly increasing integers `s_j` such that `x-s_j≡3/8 (mod3^j)`. Such choices exist because nonnegative integers are dense in `Z_3`; choose them in successively higher congruence blocks. For large `j`, `x-s_j≡0 mod3`, so `A(x-s_j)` and each denominator factor other than `8(x-s_j)-3` are units. Hence

$$v_3(r(x-s_j))=-v_3(8(x-s_j)-3)\le-j.$$

Since `16` is a 3-adic **unit**, multiplying by `16^{s_j}` does not diminish this term; its 3-adic norm tends to infinity along the subsequence. In particular the summands do not tend to zero. The same construction is executable with exact rational indices `x` and all finite depths. **Simply reversing the 2-adic recursion into 3-adics is refuted; regularization, a different operator or local punctured-domain theory is necessary.**

## 3. An exact 3-adic 'WTF detector': alignment at 3, splitting at 9

Compare the authentic source forms

$$A(x),\qquad L_1(x)=2x-1,\qquad L_2(x)=8x-7.$$

All three have a single, simple zero at `x≡2 mod3`. For uniform `x mod3`, this triple shared-input coincidence occurs with probability `1/3`, whereas independent-input sampling of their three individual zero events gives `1/27`. The **descriptive**, not inferential, agreement ratio is `9`.

At the next precision the zero classes are **distinct**:

| Form | Zero mod 3 | Zero mod 9 |
|---|---:|---:|
| `A(x)` | 2 | **8** |
| `2x−1` | 2 | **5** |
| `8x−7` | 2 | **2** |

Therefore the triple shared-input coincidence probability is exactly **zero modulo `3^L` for every `L≥2`**, whereas each form has a unique 3-adic zero path. The independently sampled zero-event baseline is `3^{-3L}`. The ratio falls from `9` to `0` upon refinement. This is a rigorously source-derived example of an apparently compelling coarse coherence that **cannot** persist as a single coherent 3-adic trajectory. It directly supports the global calibration principle: an arithmetic coincidence must survive higher-precision continuation before gaining evidence weight.

This is **not** a claim that three arithmetic constraints are statistically independent, that this descriptive ratio is a p-value, or that this trident creates real π Fourier cancellation.

## 4. A complete joint 2×3 primal-clock theorem

Let `k,L≥1`, `m_2=16^k`, `m_3=3^L` and `M=m_2m_3`. Define the pair of **distinctly typed** source-observable maps

$$
\boxed{C_{k,L}(n)=([U_n]_{16^k},\ [A(n)]_{3^L}).}
$$

The first coordinate is the authentic BBP **2-adic rational-state code**. The second is the **3-adic denominator-cleared source numerator**; replacing it by `[U_n]_{3^L}` would be false because the actual rational states need not be 3-adically integral.

**Theorem CRT-1 (paper-proved, all k,L).** For every consecutive time block `[t,t+M)` with `t≥0`, `C_{k,L}` visits each member of

$$ (\mathbb Z/16^k\mathbb Z)\times(\mathbb Z/3^L\mathbb Z) $$

**exactly once**. This uses the inherited all-time zero boundary of PR #321. Independently of that boundary proof, the theorem holds for `t≥k` by the *finite* source-window identity from PR #320.

Proof: `U_n mod16^k=Φ_k(n)` and `A(n) mod3^L` are individually compatible bijections of their respective residue rings. Given an arbitrary target pair `(a,b)`, let `n_2=Φ_k^{-1}(a) mod16^k` be found from the binary gate recursion and `n_3=A_L^{-1}(b) mod3^L` be found by ternary Hensel lifting. The two moduli are coprime, so CRT gives exactly one `n modM` with `n≡n_2 mod16^k` and `n≡n_3 mod3^L`. Explicitly,

$$
\boxed{n=n_2+16^k\big[(n_3-n_2)(16^k)^{-1}\bmod3^L\big].}
$$

It recovers the unique time index associated to each residue pair, proving the theorem. QED.

Consequently, for any integers `u,v`, the complete-period arithmetic additive-character sum is **exactly**

$$
\boxed{
\sum_{n=t}^{t+M-1}
\exp\!\left(2\pi i\left[
\frac{u[U_n]_{16^k}}{16^k}+\frac{v A(n)}{3^L}
\right]\right)
=\begin{cases}
M,&16^k\mid u\ \text{and}\ 3^L\mid v,\\
0,&\text{otherwise}.
\end{cases}}
$$

All integer starts `t≥0` are allowed with PR #321's boundary. For a prefix of `N` observations with a nontrivial `(u,v)`, the absolute character mean is at most `((N mod M)/N)`; completed `M` blocks cancel. Under a uniformly sampled time `n mod M`, the pair of finite arithmetic coordinates is exactly product-Haar. This is a **finite clock identity**, not independent stochastic trajectories through time or an equidistribution statement about the real-circle phases `{U_n}`.

**EXACT FINITE RECEIPTS:** all `M=48,144,768,2304` pairs were enumerated independently; constructive CRT inverse paths were verified on held-out higher moduli. Finite modular checks on the original source ensure the 2-adic code agrees with the *actual* zero-seed rational recurrence for authentic indices. The all-level proof is independent of brute-force enumeration.

## 5. Hostile controls and the precise π frontier

- **Finite reflection trap:** the mod16 map is an involution; already at mod32, `Φ(Φ(2))=18`, not 2. Never extrapolate the minimal-atom reflection to an infinite involution.
- **3-adic continuation trap:** the unregularized source has four genuine poles in `Z_3`, and its backwards weighted sum diverges for every 3-adic center. The 3-adic bijection is the numerator `A`, not the BBP source `r` and not `U`.
- **Coincidence inflation trap:** the exact three-form mod3 match ratio is 9, yet its triple intersection is empty mod9. Refinement (and independence of constraints) must be established.
- **CRT false inference:** the joint arithmetic Haar law is compatible with deterministic phase-bias in the real circle. PR #320 already gives a zero-seeded, 2-adically isometric, positive-forcing, real-nonnormal mutant. The extra numerator coordinate provides a source-derived arithmetic label; neither its marginal nor the CRT permutation alone supplies the missing complex cancellation.
- **Proof authority:** the paper proofs below establish exact first-prime arithmetic statements. A source-specific signed `o(N)` real-Weyl estimate or RH proof is **not established**. All finite test/oracle claims explicitly retain negative authority flags.

The actual base-16 π-normality requirement remains

$$
\boxed{\forall h\in\mathbb Z\setminus\{0\},\qquad
S_N(h)=\sum_{n=1}^N\exp(2\pi ihU_n)=o(N).}
$$

For a fixed pair of precision levels define the *new* real/adic conditional signed sums

$$
B_{a,b;N}(h)=\sum_{\substack{1\le n\le N\\[U_n]_{16^k}=a\\[A(n)]_{3^L}=b}}
\exp(2\pi ihU_n).
$$

Their indexing is completely solved by CRT, but **bounding their magnitudes or signed cross-bin interactions is NOT solved**. In particular, a true source-specific inequality must use the full signed four-pole forcing and original zero selector in a way that rejects PR #320's counterfeit and the changed-seed phase-coherent orbit. Source marginals and purely symbolic reindexing cannot prove the displayed Weyl estimate.

**Research priority:** obtain a genuinely new signed conditional correlation bound, ideally improving Astra PR #319's `N-(\log_8N)/14+O_h(1)` absolute-loss order, not merely its coefficient. Translate (if valid) PR #319 periodic/mixed-lag observers into the CRT bins with correct frequency and boundary/error budgets. Full solenoid Haar is a stronger hypothesis than π normality and must not silently replace the actual target.

## 6. Reproduction and literature grounding

Implementation is strictly standard-library `Fraction`, integer modular inverses, 2-adic bit gates, exact Hensel lifts and CRT. It calls PR #321's `stationary_window`, itself imported from original four-pole `authentic_r`; no π digits or nontrivial zeros are used as inputs. The local focused suite was exercised with a documented temporary test-only shim for this one native import, which is never committed. Native combined-repository tests and CI remain a separate gate. No new Lean kernel authority is claimed. Receipt hashes cover this module, its tests and the inherited PR #321 core, with deliberate mutation rejection.

Classical sources for Hensel lifting include the [University of Chicago expository proof](https://math.uchicago.edu/~may/VIGRE/VIGRE2011/REUPapers/Herwig.pdf) and [Aitken–Lemmermeyer](https://public.csusm.edu/aitken_html/m372/diophantine.pdf). The compatible 2-adic triangular bit description follows directly from the isometry proof and is not asserted as a newly discovered general theorem. Source-authentic formulas, code, tests and adversarial controls are the new work within this program.
