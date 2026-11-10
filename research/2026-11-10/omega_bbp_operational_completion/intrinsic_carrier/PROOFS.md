# Proof contracts, edge formulas, and hostile controls

## T1. Arithmetic Toeplitz–Cuntz packet

**Domain.** `H=ℓ²(N_{≥1})`, basis `e_n`; for integer `p>=2`, let `S e_n=e_{n+1}` and `V_p e_n=e_{pn}`. These are isometries, with `V_p S=S^p V_p`. Set `T_{p,a}=S^a V_p`, `0<=a<p`. Each image is exactly `span{e_{pm+a}:m>=1}`; they are disjoint for distinct `a`, giving `T_{p,a}*T_{p,b}=δ_ab I`. Their orthogonal sum is `span{e_n:n>=p}`. Thus `Σ T_{p,a}T_{p,a}*=I-E_{<p}` with boundary rank `p−1`. The unitary *coordinate* lift `H≅C^{p-1}⊕(H⊗C^p)` is the inverse of the stated basis bijection, not the lossy low-pass postselection.

`W_p=(1/√p)Σ T_{p,a}` is isometric. Its range is the direct sum of uniform vectors `u=(1,...,1)/√p` on each block; `B_p=W_pW_p*` has local matrix `J_p/p`. `Q_p=V_p V_p*` has local matrix `E_{00}`. Therefore `C_p=[B_p,Q_p]` is real skew; only matrix entries `(C_p)_{a0}=1/p` and `(C_p)_{0a}=−1/p`, `a>=1`, are nonzero. The Hermitian operator is `H_p=iC_p`. The 2D invariant span of `e_0` and `w=(Σ_{a>=1}e_a)/√(p−1)` has matrix `sqrt(p−1)/p` times `σ_y` (with the stated basis orientation). Its orthogonal complement is null. Consequently `||H_p||=sqrt(p−1)/p`, `H_p³=((p−1)/p²)H_p`, and `Tr_block(H_p²)=2(p−1)/p²`.

**Negative:** for composites the same identities hold. The projections `Q_p` are all diagonal (divisibility); hence `[Q_p,Q_q]=0` for all `p,q`. No pure divisibility commutator generates an intrinsic chiral oscillator. Complex conjugation sends `H_p→−H_p`, so a nonzero `H_p` cannot be nonnegative.

## T2. Ω₄/Ω₅ infinite-carrier decomposition

`B_2` averages blocks `(2,3),(4,5),(6,7),...`; `B_3` averages `(3,4,5),(6,7,8),(9,10,11),...`. The span of `1,...,5` is invariant under both, and for every `m>=1`, the span of `6m,...,6m+5` is invariant. Thus `[B_2,B_3]` is their orthogonal direct sum. On the boundary, `B_3` is the projection onto `v=(e_3+e_4+e_5)/√3` and `||B_2 v||²=5/6`; the unique nonzero principal angle has `sinθ cosθ=√((5/6)(1/6))=√5/6`. The boundary skew commutator has characteristic polynomial `λ³(λ²+5/36)` and the Hermitian `i` multiple has eigenvalues `0,0,0,±√5/6`. On each bulk six-cell window the rank-two commutator is exactly the chronological `[P_2,P_3]` of [Ω₄×Ω₅ Haar](../OMEGA_HAAR_WAVELET.md), with `C³=−(2/9)C` and eigenvalues `±i√2/3`, four zeros. Sympy exact matrix tests independently recover both characteristic polynomials. No source forcing is needed to construct this bulk operator; genuine BBP excitation is a separate input.

## T3. Thermal zeta covariance, with no RH promotion

Define `H_0 e_n=(log n)e_n` on its diagonal self-adjoint domain. Then `e^{itH_0}V_p e^{−itH_0}=p^{it}V_p`. For `β>1`, `e^{−βH_0}` is trace-class, with trace `ζ(β)`. By T1, diagonal entries of `H_p²` in block `(pm,...,pm+p−1)` are `(p−1)/p²` at `pm` and `1/p²` at each other entry. Hence

```
Tr(exp(-beta H0)*Hp²)
 = p^-2 * [ (p-1) sum_m (pm)^-beta + sum_m sum_{a=1}^{p-1} (pm+a)^-beta]
 = p^-2 * [ (p-1)p^-beta zeta(beta)
            +(1-p^-beta)zeta(beta) - sum_{a=1}^{p-1} a^-beta]
 = p^-2 * [zeta(beta)*(1+(p-2)p^-beta) - H_{p-1}^{(beta)}].
```

The first equality is an **absolutely convergent positive trace formula for β>1**. For `p=2`, `H_2²=(I−|1><1|)/4` and thus the normalized expectation is `(1−1/ζ(β))/4`, a vacuum-probability identity. For *every* real diagonal Gibbs density, `Tr(ρ H_p)=0`. The expectation's weak/nonzero property is not a Weil signed explicit formula, and the trace expression's analytic continuation, if written formally, does **not** continue a positive Gibbs state to Re β<=1.

The explicit prime-indexed operator family `K_σ=Σ_{p prime}(log p)p^(−σ)H_p` converges absolutely in operator norm if `Re σ>1/2`, because `||H_p||<=p^-1/2` and the majorant `Σ_{n>=2}(log n)n^(−(Reσ+1/2))` converges. This is a *sufficient* bounded-holomorphic region, not a zero-free half-plane result for ζ. On `c_00(N_{≥1})` only `p<=max supp(v)` act, giving a locally finite densely defined operator for all coefficients; self-adjoint closure on the critical boundary is **UNVERIFIED**. For real σ>1/2 the norm-limit is bounded self-adjoint. The edge time-transport formula is `(pm+a)/(pm)` to the power `it`; this is exact but does not contain the completed Archimedean Γ or prime powers from Weil's formula.

## T4. Nonunique finite reverse root, even with positivity and a shared endpoint zero

On `x∈[0,1]` set `t=x^8`, `dν(x)=(1−x)dx`, and `μ_k=∫t^k dν=1/[(8k+1)(8k+2)]`. For any `N>=0`, the `(N+1)x(N+1)` Hankel Gram `G=(μ_{i+j})_{i,j<=N}` is positive definite: the integral of the square of a nonzero polynomial in `t` is strictly positive because `dν>0` on `(0,1)`. Thus there is a unique monic `q_N(t)=t^(N+1)+Σ_{j=0}^N c_jt^j` orthogonal to `t^0,...,t^N`, with rational coefficients; the roots of a positive-weight orthogonal polynomial lie in the open support interval `(0,1)`, so `q_N(16)>0`. Put `ε=1/Σ_{j=0}^{N+1}|c_j|`, with leading coefficient one, and note `|ε q_N(t)|<=1` on `[0,1]`.

The canonical source is `P(x)=(1−x)M(x)` with `M(x)=(x²+2)(x²+2x+2)>=4`. Hence `Pε(x)=(1−x)(M(x)+ε q_N(x^8))` is nonnegative and strictly positive for `x<1`, with the same endpoint cancellation. For each `0<=n<=N`,

```
int_0^1 x^(8n) (Pε(x)-P(x)) dx
 = ε int_0^1 t^n q_N(t) dν(x) = 0.
```

**Completion difference.** Let `Π(P)=∫_0^1P(x)/(1−x^8/16) dx`. Since `(q_N(16)-q_N(t))/(16−t)` is a polynomial of degree `N`, orthogonality gives

```
q_N(16) int q_N(t)/(16−t) dν
   = int q_N(t)^2/(16−t) dν > 0.
```

Therefore `Π(Pε)−Π(P) = 16ε/q_N(16) *∫ q_N(t)^2/(16−t) dν`. Because `15<16−t<16` for almost all x in (0,1), the exact rational `D_N=∫q_N(t)^2dν>0` yields

```
0 < εD_N/q_N(16) < Π(Pε)-Π(P) < (16/15)*εD_N/q_N(16).
```

This is not a mutation of the **authentic** four-pole source: it is an adversarial different BBP-type rational source, with additional pole shifts determined by the polynomial degree. It refutes a *finite-moment-only* reconstruction claim, not a source-locked theorem that knows all four poles.

### Exact first example

`N=0`, `μ_0=1/2`, `μ_1=1/90`, so `q_0(t)=t−1/45`, `ε=45/46`. The initial moment is identical, while the infinite sums differ by a strictly positive quantity between 0.0001849684664 and 0.0001972996976. The independent high-precision quadrature gives approximately 0.0001905264841237519187413, within the rational interval. **The rational interval is the certificate**; the numerical quadrature is merely a cross-check.

## T5. Clock, parity bundle, source/oracle firewall

For the authentic source use `R(j)=4/(8j+1)-2/(8j+4)-1/(8j+5)-1/(8j+6)`. `P_L=Σ_{j<L}16^{−j−1}R(j)→π/16`. The strict bound from [quantum bridge](../quantum_bridge/README.md) is `16^n(P∞−P_L)<16^(n−L)/[(8L+1)(8L+2)]`. A finite circuit approximating real continuous characters has a separately quantified phase budget; a digit boundary or arbitrary growing frequency is not paid by smooth phase Lipschitz alone. The full inverse label is a retained wire, not spontaneously recovered after partial trace.

For even `p` the cyclic digit group `Z/pZ` has a nontrivial real character `k↦(−1)^k`; for odd p, it does not (since a one-step cyclic wrap would demand `(-1)^p=1`). The 16-branch parity Möbius monodromy is a property of an inverse-digit **representation**, not universal arithmetic orientation or a physical Berry phase.

**No-seed-blind-decay theorem:** a circuit or observable prepared solely from the source forcing and not from the initial seed has identical input for all seeds. All later seed-blind unitaries/measurements have identical output statistics. Yet the coherent completed wrong seed `s=−π/16` has every completed phase zero and all parity signs +1, whereas the zero-seed π digit balance is the target. Thus any proof scheme that purports to infer original-zero parity *solely* from a seed-blind state statistic is invalid. Including the actual marked zero boundary is necessary, but not sufficient.

## Reproduction notes

`intrinsic_carrier.py` uses `Fraction` matrices and source arithmetic. `finite_alias.py` solves exact Gram systems with handwritten Fraction elimination. `test_intrinsic_carrier.py` and `test_finite_alias.py` calibrate these two independent constructions with hostile composite, wrong-seed and pole/moment controls. The separate `independent_carrier_audit.py` reconstructs projections and a first orthogonal perturbation directly in SymPy/MPMath, avoiding the production helper functions. These are **not externally blind peer review**. Native full-suite/CI not executed in this round.
