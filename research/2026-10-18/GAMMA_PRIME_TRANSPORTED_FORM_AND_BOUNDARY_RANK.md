# SUCC — Transported form covariance, source-boundary curvature and two parity packets

**Prompt correction:** “It shouldn't commute. Its form should, but its values shouldn't.” This is a new exact mathematical bridge between original Suzuki first-prime/Gamma source structures, not an RH proof. Child of Gamma packets PR #168, frozen original signed Suzuki source blob `0cc8510b71d178fc79e8d410a86d8b6014cf9178`. Status: **PAPER PROVED** on its stated bounded one-rung operators; independent exact rational finite-model controls and separate Lean algebraic shape theorem. **Full Gamma/high Schur S4 and RH remain OPEN.**

## 1. Form transported vs values failing to commute (TBF-01)

On full H=L²(R), let T_b f(x)=f(x-b) and E_α f(x)=integral_R exp(-α|x-y|) f(y)dy for α>0. The convolution kernel depends only on x−y; `[T_b,E_α]=0` for all b. Let I=(-a,a), P=1_I, Q=1−P, S_b=T_b+T_−b. On H_I=P H set A_b=P S_b P and E_α,I=P E_α P. In full-line zero-extension notation:

```
[A_b,E_α,I] = P E_α Q S_b P − P S_b Q E_α P.    (1)
```

Proof: Insert P=1−Q in the middle of both operator products. The remaining interior-independent difference is P[S_b,E_α]P=0. The failure of same-window commutation therefore factors **entirely through the exterior observation carrier**.

If the WHOLE observation interval is transported from I to I+b with the translation unitary U_b, then
```
E_α,I+b U_b = U_b E_α,I.                         (2)
```
This naturality square commutes EXACTLY. It is different from demanding `[A_b,E_α,I]=0` after fixing the old window. Values may change, but the defining shape law is transported coherently.

## 2. An exact four-feature continuum boundary commutator (TBF-02)

For a=1/2 and genuine b=log2, a<b<2a. Define disjoint first-prime edge regions
```
L=(-a,a-b), C=(a-b,b-a), R=(b-a,a).
```
The kernel of D=[A_b,E_α,I] is (all x,y in I):
```
D(x,y) =
(1_R(x)-1_L(y)) exp(-α|x-y-b|)
+(1_L(x)-1_R(y)) exp(-α|x-y+b|).
```
On the support of the first nonzero coefficient, x−b≤y. On the support of the second, x+b≥y. Hence the absolute values **factor exactly** rather than approximately. Put
```
h₊(x)=exp(αx), h₋(x)=exp(-αx),
r₊(x)=1_R(x) h₊(x), l₋(x)=1_L(x) h₋(x).
```
Then as a genuine L²(I) bounded operator,
```
D=e^(−αb)[ r₊⊗h₋ − h₋⊗r₊ + l₋⊗h₊ − h₊⊗l₋ ].   (3)
```
Here `u⊗v` maps f↦u∫_I vf and the original OU kernel carries no fictitious normalization. D is skew-adjoint, with rank ≤4.

It actually has **rank exactly four**: on the nonempty center C, h₊ and h₋ are linearly independent for α>0; r₊ and l₋ vanish on C and have disjoint nonempty supports R and L. Thus the four features are linearly independent. The rank-four coefficient matrix of the two skew wedges is invertible, and their Gram matrix is invertible; hence the induced operator has rank 4.

The original Gamma rung equals a scalar identity minus E_α with α=(4j+1)/2, so its commutator with A_b is the NEGATIVE of (3). The identity scalar part commutes. This does NOT establish a rank-four property for the entire infinite Gamma sum: α varies, yielding growing feature spans and unbounded-form/domain issues.

## 3. Exactly two rank-two parity packets per authentic Gamma rung (TBF-03)

Let J f(x)=f(-x). The original reflection satisfies J A_b=A_b J and J E_α,I=E_α,I J. Under J, r₊↔l₋ and h₊↔h₋. Define
```
u_even=r₊+l₋,  v_even=h₋+h₊,
u_odd =r₊−l₋,  v_odd =h₋−h₊.
```
Both pairs have declared reflection parity. For u∧v := u⊗v−v⊗u,
```
D=(e^(−αb)/2)[u_even∧v_even + u_odd∧v_odd].      (4)
```
Since each pair is independent (one vanishes on C, one does not), its wedge has **rank two**. The even and odd images and inputs are mutually orthogonal, so there is no cross-parity coupling. This yields **two exact 2D boundary transmission packets** per OU rung.

**Research interpretation:** The full-line law is form-covariant, the single-window values are not path-independent, and their disagreement is explicitly source-edge mediated. Thus noncommutation is not a generic obstruction to compensated packet analysis. It prohibits simultaneous exact diagonalization but provides a surprisingly small, structured, source-authentic correction to analyze.

## 4. Independent exact checks and source discipline (TBF-04)

The stdlib Fraction implementation `observational_succ/transported_gamma_boundary.py` tests the same algebra in a DIFFERENT lattice model:
```
E[i,j]=q^|i−j|, A[i,j]=[i=j+k]+[i+k=j], 0<q<1.
```
It computes [A,E] by independent matrix multiplication, and a second matrix by explicitly summing paths through outside cells `z<0` or `z≥n`. It separately computes (3) via feature outer products and (4) via parity wedges. It then verifies all entries, skew symmetry, rank=(4,2,2) using exact rational row elimination, for several window sizes and q. No source floating-point mesh or conjectural equality between `q` and `exp(-αΔ)`.

The source adapter independently checks original SHA, genuine n=2/half-density activation, and certified `1/2<log2<1`. `formal/GammaBoundaryShapeTransport.lean` proves ONLY simultaneous shift invariance of an arbitrary difference kernel and an explicit one-argument value change, on Lean 4.14 core. Neither rational model nor Lean lemma is misrepresented as a formal proof of infinite-dimensional OU operator rank.

## 5. Falsifiers and next RH-facing experiment

Controls reject malformed finite geometry, non-rational or q∉(0,1) spectral decay, mismatched source, wrong prime activity; they compare independent exterior and feature routes. A fixed-window fake assumption D=0 fails. A four-feature formula with wrong wedge sign fails. Pinned historical source files are unchanged. Zero coordinates are not used.

**Next decisive source probe:** bound the sum of authentic two-dimensional boundary transmissions over all real Gamma rungs with a tail bound uniform in the actual original high-response domain. Then compare the resulting correlated even/odd boundary compensator against the existing SOURCE-FOUR `S4=A4−R4` lower, including true prime2, contact, Gamma and both completed poles. If the source-tail does not provide a usable operator bound, preserve the failure: four per-rung channels do not imply four global channels. This is a proposed source-specific avenue toward the still-unproved S4 positivity, not a shortcut to all-radius Weil positivity.

## Claim ledger

| ID | Verdict |
|---|---|
| TBF-01 full-line commutation + source-transport intertwining | CLASSICAL / PAPER PROVED |
| TBF-02 continuum single OU rung fixed-window commutator rank exactly four | PAPER PROVED, exact rational finite controls |
| TBF-03 two reflection-parity rank-two packets per rung | PAPER PROVED, exact rational finite controls |
| TBF-04 source hypotheses and SHA | AUTHENTICATED ORIGINAL SOURCE via fail-closed adapter |
| Infinite Gamma-sum rank four or summable uniform edge interaction | OPEN |
| Original S4/Weil positivity/RH | OPEN |

No merges, tags, releases, source rewrites or priority claims.
