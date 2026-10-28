# Prime-7 arithmetic translator: exact local cancellation and its missing real bridge

2026-10-27. Independent read-only research against PR325 commit `95ee2f1fab851afe1517d8ec5a0589885842426f` and local PR327-derived dossiers at `76f37996`. No external novelty claim. Pi normality remains OPEN.

## Verdict and hole contract

There is a genuine new source-specific finite-arithmetic lemma: for the original `r=A/D`, complete additive-character sums modulo `7^L` have square-root cancellation; the regular numerator-mirror character sum vanishes exactly. There is also an exact obstruction: even this favorable oscillating source-character model has normalized A-collision energy **2/7**, independent of depth. Neither statement concerns the selected real phase `e(h U_n)` without an additional bridge.

The exact missing edge is identification/control of the *archimedean character and its cofactor*, not identification of an algebraic correspondence. The weakest assertion actually verified here is local modular cancellation, not a global sufficient condition for normality. The optional translation-defect condition below is a strict sufficient condition for one residue-disk sum, is testable, and has not been proved for the authentic orbit. It is deliberately not promoted to an accepted moonshot reduction.

## 1. Good reduction: verified scope

Write `A=120x^2-89x+16`, `D=(2x-1)(4x-1)(8x-7)(8x-3)`. Exact symbolic calculation gives

* `Res(A,D)=-7372800=-2^15*3^2*5^2`;
* `disc(D)=3774873600=2^24*3^2*5^2`;
* the degree-four homogeneous model `[Y^2 A_h(X,Y):D_h(X,Y)]` has resultant `512^2 Res(A,D)=-2^33*3^2*5^2`.

Silverman's cited AWS notes, section 6 (printed pp.18–20), define good reduction by preservation of degree and give the normalized resultant criterion. Proposition 24 says reduction commutes with evaluation and iteration; Theorem 25 concerns reduction of periodic points of an *iterated rational map*. These justify PR325's displayed-model good-reduction claim, not minimal reduction under arbitrary conjugacy. They do not imply equidistribution of `r(n)` or of `U_n`. The SUCC recurrence is an affine nonautonomous forcing recurrence, not iteration of `r`.

At 7, projective good reduction does **not** make `r` integral on every integer input: four affine residue disks are poles. Those disks remain a positive-density part of the true time orbit. No argument may discard them as an `o(N)` exceptional set.

Primary source: Joseph H. Silverman, *Lecture Notes on Arithmetic Dynamics*, AWS 2010, https://swc-math.github.io/aws/2010/2010SilvermanNotes.pdf .
## 2. Source-specific stationary phase at 7

Modulo 7,

`A=x^2+2x+2`, `D=x^4-2x^3-2x^2-3x`,

and the derivative numerator is

`A'D-AD'=-2(x-1)(x+2)(x^3+x^2+x-2)`.

The regular residue disks are exactly `1,5,6`. Direct evaluation gives:

| residue x | r(x) | r'(x) | r''(x) |
|---|---:|---:|---:|
| 1 | 5 | 0 | 1 |
| 5 | 1 | 0 | 2 |
| 6 | 2 | 1 | 2 |

All entries are modulo 7. Thus there are exactly two nondegenerate critical points on the regular domain.

Let `q=7^L`, `L>=2`, and `7∤a`. Here `e_q(r(x))` ALWAYS means `exp(2πi [r(x)]_q/q)`, with denominator inverted modulo q; it does not mean evaluating the rational number in R and dividing it by q. The following self-contained stationary-phase argument gives

`| sum_{x mod q, 7∤D(x)} e_q(a r(x)) | <= 2 sqrt(q)`.

Each critical disk contributes a Gauss term of magnitude `sqrt(q)`; the noncritical disk 6 contributes zero.

**Proof.** On disk 6, translating by q/7 changes the source residue by q/7, so summing each seven-point translation orbit gives zero. On either critical disk, Hensel lifting gives its unique critical point c. The integral Taylor expansion and square-root coordinate from [the local Morse lemma](PI_FULL_SOURCE_DELAY_RECONSTRUCTION.md#2-local-exact-counting-lemma) give an isometric bijection t↔w of 7Z_7 with r(c+t)=r(c)+b w², b a unit. Consequently the disk sum is exactly

$$e_q(a r(c))\,7G_{7^{L-2}}(ab),\qquad G_m(v)=\sum_{j\bmod m}e_m(vj^2).$$

Use G_1=1 at L=2. For odd m and unit v, the invertible change (j,k)↦(j−k,j+k) gives |G_m(v)|²=Σ_{s,t mod m}e_m(vst)=m by character orthogonality. Each critical disk therefore has magnitude √q. The triangle inequality over the two disks proves the bound. Every Taylor coefficient used here is 7-integral because the chart denominator is a unit. This proof needs no uninspected external theorem.

 This is a theorem for the actual four-pole rational function, rather than a heuristic drift claim. It supplies a growing saving for a different, precisely defined observable.

A primary theorem checked directly is Bag–Baier–Haldar, *Multiple exponential sums and their applications to quadratic congruences*, arXiv:2311.17706v5 (2025), Theorem 1, specialized to one variable and derivative content zero. Its explicit domain excludes denominator zeros mod p; noncritical disks vanish and nonsingular critical disks have the displayed Gauss evaluation. https://arxiv.org/pdf/2311.17706 .

## 3. Exact regular mirror cancellation

Put `c=89/120` in Z_7 and `F(x)=r(x)-r(c-x)`. Modulo 7 the mirror is `x↦5-x`. Pole residues are `{0,2,3,4}` and their mirrors are `{5,3,2,1}`. Therefore **both denominators are units only on disk x≡6 mod7**. On this disk,

`F'(x)=r'(x)+r'(c-x) ≡2 mod7`.

For every `L>=2` and `7∤a`,

`sum_{x mod 7^L, x≡6 mod7} e_{7^L}(a F(x)) = 0`.

An elementary proof avoids any literature theorem. Translation by `q/7` preserves the disk and changes F modulo q by `2q/7`. Partition the disk into 7-element translation orbits and sum the nontrivial seventh roots of unity. Taylor's quadratic error is divisible by q because `2L-2>=L`. The rational Taylor coefficients are 7-integral on this disk.

This is exact denominator-induced oscillation on the regular mirror. It does not encompass the other six residue disks, and it does not encode `e(h(U_n-U_m))` for time pairs satisfying the numerator congruence.

## 4. A-collision energy stays 2/7 even in the favorable local model

Define the periodic local-character observable

`w_x = 1_{7∤D(x)} e_q(a r(x))`, with `q=7^L`, `L>=2`, `7∤a`.

Then exactly

`sum_{b modq} | sum_{x modq, A(x)=b modq} w_x |^2 = 2q/7`.

Proof:

1. In regular disk 1, A' is a unit. Every A-fiber represented there has exactly one regular root in disk1; its mirror root is in pole disk4. There are q/7 such singleton fibers. Likewise disk5 gives q/7 singleton fibers, with removed pole partners in disk0. The two sets of A-values are disjoint modulo7.
2. Every remaining regular input is in disk6, where A'≡0. Translation `x↦x+q/7` preserves each A-fiber modulo q, while `r(x+q/7)-r(x)≡q/7 modq`. Every such fiber sum vanishes by nontrivial seventh-root orthogonality.

Consequently, on any integer number of periods `N=mq`, the PR325-style normalized energy of w is exactly **2/7**, whereas its normalized scalar sum has magnitude at most `2/sqrt(q)`. Taking `N=q^2` even gives `q=o(N)`.

Scope: this is a triangular family of modular observables, with zero weights on excluded pole disks, not a new fixed normal real or an authentic replacement for `e(hU_n)`. It is nevertheless an exact source-specific calibration showing that a theorem yielding scalar cancellation need not make the chosen A-energy decay.

## 5. The square-collision weighted tree

For p>=7, complete the square by `t=240x-89`, so `480A(x)+241=t^2`. For a value b modulo `p^L`, set `s=480b+241` and let `m_L(b)` be the A-fiber cardinality. Then:

* If `s=0 mod p^L`, `m_L(b)=p^floor(L/2)`.
* If `v_p(s)=2j<L` and its unit part is a quadratic residue, `m_L(b)=2p^j`.
* Otherwise `m_L(b)=0`.

The natural pushforward probability is `m_L(b)/p^L`; it is not uniform. The corresponding empirical conditional-expectation norm uses weights equal to actual bin sizes. The PR325 energy instead multiplies the unweighted bin-square sum by `p^L/N^2` and on complete periods weights a bin by an extra factor equal to its fiber multiplicity. For arbitrary samples the exact extra factor is q times that bin count divided by N.

There is an even stronger elementary monotonicity fact than the endpoint-qualified statement in the PR327 CRT dossier. At fixed N define `S_{L,b}=sum_{n<N,A(n)=b modp^L}z_n`. For ALL N and ALL complex phases,

`C_{L+1}-C_L = (p^L/N^2) sum_{b modp^L} sum_{0<=i<j<p} |S_{L+1,b+i p^L}-S_{L+1,b+j p^L}|^2 >=0`.

Empty child bins are included. No balance assumption or error term is needed. The same algebra applies to ordinary time-residue E_M whenever M divides M'. This follows from `p sum_i|u_i|^2-|sum_i u_i|^2=sum_{i<j}|u_i-u_j|^2`.

For coherent phases and a complete period, `C_L=1+L(1-1/p)`, from the known pair count. Thus the ramified tree itself creates no decreasing energy mechanism.

## 6. Why these theorems do not estimate the real phase

The original source gives the exact real-circle identity

`e(h(U_n-16U_{n-1})) = e(h r(n)) -> 1`.

Indeed `r(n)=O(n^-2)`. Thus this very same rational source is maximally coherent in its real one-step echo, while its complete modular additive characters have square-root cancellation. This is an authentic source counterexample to an automatic transfer principle; no changed seed is needed.

For a rational u=A/B with `7∤B`, let `R=[A B^{-1}]_q` and `K=(B R-A)/q∈Z`. Exact arithmetic gives

`u/q = R/q - K/B`, hence `e(h u/q)=e_q(hR) e_B(-hK)`.

The omitted cofactor character can exactly undo the modular cancellation. For the unscaled real character, `u=R-qK/B`, so `e(hu)=e_B(-hqK)`; the integer residue R vanishes from the real character entirely. Knowing R and its good-reduction distribution does not control this quotient/cofactor.

The standard genuine local/global factorization is also exact: if the reduced denominator of u is `7^v d`, `(7,d)=1`, choose `s=d^{-1} mod7^v` and `t=(7^v)^{-1} modd`; then

`e(h u)=e_{7^v}(h A s) e_d(h A t)`.

An estimate for one local factor cannot ignore correlation with the complementary one. In particular, when v=0 the genuine 7-local factor of e(hu) is trivial, despite the nontrivial artificial character `e_q([u]_q)`.

Milićević's p-adic exponent-pair theorem does not repair this: the paper explicitly treats sums of periodic functions `e(f(m)/p^n)` built from specified p-adic analytic phases. It does not identify the real SUCC phase with one of them. Primary source: https://arxiv.org/pdf/1407.4100 , introduction equation (4), Definition 1 and the periodicity statement immediately after it (PDF pp.2–3,11–12).

## 7. Exact testable transfer defect, and novelty boundary

On each complete q-block, cyclically translate indices by `q/7`, writing the permutation as τ. On the mirror-regular disk6 put `lambda=e(2a/7)`. For any array z,

`|sum_{n≡6 mod7} z_n| <= (1/|1-lambda|) sum_{n≡6 mod7} |z_{τ(n)}-lambda z_n|`.

This follows by summing the defect and using that τ is a permutation. Thus an `o(N)` authentic-source bound for this absolute defect would transfer the modular cancellation on that disk. The bound is NOT established. It is stronger than mean cancellation, and generic random-looking phases need not satisfy it. Replacing the absolute defect by its signed sum simply recovers the original selected sum and pays no novelty tax.

The cheapest discriminating probe is to compute this defect (with exact phase error bounds) for the true U and the changed-seed coherent control, not merely inspect D-asymmetry or modular histograms. A failure at positive density kills this specific local phase-matching bridge. Even success would leave the six other disks and the selected zero boundary to handle; there is no claim that this alone proves normality.

## Finite validation and earned claims

Independent exact integer checks at L=1,2,3,4 gave A-pair counts 13,133,1225,10633, matching `q+L*6q/7`. Mirror-character vanishing was checked exactly for L=2,3,4 by uniform cyclotomic coefficient counts, not floating cancellation. The 2/7 energy identity was likewise checked by verifying every regular singleton fiber and every central fiber's sevenfold character balance at L=2,3,4.

Earned classification: **genuine local arithmetic proof steps + refutation of automatic modular-to-real transfer; no selected real growth saving**. The principal reusable object is the exact source-specific stationary-phase model and its nondecaying A-energy calibration. All cited theorem hypotheses and excluded pole sets are explicit.
