# Classical SUCC: unit-origin multiplication, `1-s` duality, and Hilbert boundary obstructions

**Round:** 2026-10-15 | **Branch:** `research/classical-affine-carrier-2026-10-15` | **Parent:** `03db44203147a7b28d445bb9f970fa71360e78c4`

**Scope:** classical algebra on the actual positive-integer SUCC carrier; elementary CRT; bounded Hilbert-space operators; Mellin transformation. No physical source identification, global Weil positivity, RH proof, new Euler coefficients, or novelty claim. The tests instantiate finite exact cases; the universal results below are justified by the paper proofs, **not** by finite enumeration.

## 0. Recover the source and the author's idea

The **original carrier**, not a toy replacement, is `C=N_{>=1}` with successor `S(n)=n+1` and arithmetic dilations `V_m(n)=mn` for positive integers `m`. For genuine Euler jets one restricts `m` to actual primes and authentic source weights, but the action identities alone hold also at composites. The user insight is that multiplication has to retain the **unit `1`** when represented from an observer's zero-reference frame, and proposes the reflection `1-s` as a natural dual. We test three *different* meanings of a reflection:

1. **Address charts:** `x=n-1` or `u=1-n`. Here `u=-x` is the chart transition; it changes the sign of the quadratic coupling.
2. **Mellin exponent:** `s -> 1-s`. Here the identity is realized by a specific *unitary half-density inversion* on `L²(R_{>0}, dx)`.
3. **Zeta functional equation:** completed `Lambda(s)=Lambda(1-s)`. This requires the authentic global arithmetic/Poisson/Gamma input and does **not** follow from (1) or (2).

The claim of *uniqueness* below is scoped to genuine affine actions with prescribed slopes and the full integer-multiplier monoid. Without those assumptions, `x -> mx` is also a coherent action, but it fixes `0` as an absorbing origin rather than encoding the original monoid's unit at zero.

## 1. C1 — unit-origin formal-group law (CLASSICAL / PROVED PAPER)

Define `tau_+(n)=n-1` and `tau_-(n)=1-n`, both mapping the multiplicative identity `n=1` to the observer origin `0`. Transport ordinary multiplication through the charts:

```
F_+(x,y) = tau_+((x+1)(y+1)) = x+y+xy;
F_-(u,v) = tau_-((1-u)(1-v)) = u+v-uv.
```

For either sign `epsilon=+1` or `-1`, `F_epsilon(a,b)=a+b+epsilon*a*b`. It satisfies `F(a,0)=a`, commutativity, and associativity by the identity

`1+epsilon F_epsilon(a,b)=(1+epsilon*a)(1+epsilon*b)`.

The change of coordinates `u=-x` gives `F_-(-x,-y)=-F_+(x,y)`. These are two coordinate presentations of the **multiplicative formal group**, not an unexplained new formal group. Formal inverses are

`i_+(x)=-x/(1+x)` and `i_-(u)=-u/(1-u)`

as series in `Z[[x]]` and `Z[[u]]` respectively. **Caution:** the actual source subsets `x>=0` and `u<=0` are monoids, not groups closed under inversion. A polynomial identity on all integers does not license negative coordinates as realized source states. Over `Z_p` the formal logarithm is a local analytic linearization with its own convergence and integrality conditions; it does not provide unrestricted division by the observer step or an adelic theorem.

**External attribution:** MIT 18.786 Lecture 32, Example 32.7, `https://math.mit.edu/classes/18.786/2018/LectureNotes32.pdf`, and the formal-group example in `https://www.math.harvard.edu/media/Kim-explicit-local-class-thesis.pdf`. Neither is a claim of scholarly priority for SUCC.

### C2 — arithmetic successor and multiplication in both charts

For `epsilon=+1` (coordinate `n-1`) or `epsilon=-1` (coordinate `1-n`):

```
S^k_epsilon(x) = x + epsilon*k;
V_{m,epsilon}(x) = m*x + epsilon*(m-1)
                 = F_epsilon(x,epsilon*(m-1)).
```

**Proof:** directly conjugate `n -> n+k` and `n -> mn`. The source relation survives:

`V_m S^k = S^(m*k) V_m`.

Its value is *an equality of destination maps*, not a scalar Hilbert operator commutator. On the ket representation `e_n -> e_{n+1}` and `e_n -> e_{mn}`, the difference of noncommuting orderings is the difference of **basis vectors**, not automatically the scalar `(1-m)`.

**Mutation:** replacing `V_{m,+}(x)` by `mx` gives `V_m(0)=0` although true multiplication sends the represented source unit `n=1` to `n=m`, i.e. `x=m-1`. The alternate action is coherent on an abstract zero-anchored multiplicative monoid but is **not** the conjugated arithmetic source.

## 2. C3 — the affine cocycle is rigid (PROVED PAPER)

Let `R` be any unital commutative ring, or an additive abelian group on which multiplication by integers is defined. Suppose every positive integer `m` acts affinely by `A_m(x)=mx+c(m)` and the action respects `A_m A_n=A_{mn}`. Then

`c(mn) = m c(n)+c(m)`.

Because `2m=m2`, compare the two expansions:

`2 c(m)+c(2) = m c(2)+c(m)`.

Subtract `c(m)` and `c(2)` to get **for every `m>=1`**:

`c(m)=(m-1)c(2)`.

Conversely this formula satisfies the complete cocycle identity. No division by `m-1`, cancellation in `R` of a nonunit, primality of `m`, or field structure is used. Prescribing `c(2)=+1` forces the positive chart; `c(2)=-1` forces the reflected chart. This is a conditional uniqueness theorem, not a statement that every possible source representation must be affine.

**Mutant:** `c(1)=0,c(2)=1,c(3)=4,c(6)=5` disagrees already with `c(3)=(3-1)c(2)=2`. Finite checks of a candidate table never establish the full quantifier; the algebraic proof does.

## 3. C4 — exact CRT, actual first witnesses, and observation horizons (CLASSICAL / PROVED PAPER)

Let `R(a,m)={a+km:k in N_0}`, with `a>=0,m>=1`. Intersections satisfy the generalized Chinese remainder criterion. For two rays `R(a,m)` and `R(b,n)`, the intersection is empty **iff**

`a != b (mod gcd(m,n))`.

If compatible, their intersection is another nonnegative ray of step `lcm(m,n)`, beginning at the *least* simultaneous solution `w>=max(a,b)`. The standard modular inverse on the reduced coprime moduli constructs the residue, and moving into the actual ray intersection requires advancing beyond both starting addresses. Consequently

`max(a,b)<=w<max(a,b)+lcm(m,n)`.

The same result iterates across finitely many rays. Compatible congruences have **global** solutions, but this does not imply a witness at a prescribed finite observation horizon `H`.

**Concrete complete certificate:**

```
A=1+2*N_0,  B=2+3*N_0,  C=3+5*N_0;
first(A cap B)=5, first(A cap C)=3, first(B cap C)=8;
first(A cap B cap C)=23; triple step=lcm(2,3,5)=30.
```

At horizon `H=9` an observer can witness *all three pairwise intersections* but none of the triple intersection. By `H=23` the first global intersection becomes accessible. Algebraic compatibility, mathematical existence and observed finite access have distinct types. This is **not** a no-go for CRT gluing: it is a no-go for upgrading compatibility to *visibility at the same horizon*. The independent test oracle enumerates bounded genuine source addresses rather than calling the CRT implementation to check itself.

## 4. C5 — algebraic modular quotients need not be bounded Hilbert quotients (PROVED PAPER)

The residue map `q_N:n -> n mod N` is a perfectly lawful quotient of the **set-theoretic** SUCC shift and integer dilation actions. A tempting ket-level linearization on finitely supported vectors is

`J_N:e_n in ell²(N_0) -> e_(n mod N) in C^N`.

For the restriction to `H` source basis vectors, compute `J_N J_N*` on `C^N`: it is diagonal with entries equal to the numbers of source addresses in each residue fiber. Hence

`||J_{N,H}||² = ceil(H/N)` (for `H>=1`).

This grows without bound for fixed `N`. Explicitly, the vector `v_K=sum_(j=0)^(K-1) e_(jN)` has input norm squared `K`, output squared norm `K²`, so the squared amplification is `K`. The infinite linearization has **no bounded extension** from the densely defined `c_00` domain to `ell²`.

In fact its algebraic kernel is dense. For any integer `K>=1`,

`w_K=e_0-(1/K)sum_(j=1)^K e_(jN)`

has `J_N w_K=0` but `||w_K-e_0||²=1/K ->0`. Translating the construction to every source basis vector shows closure(ker J_N)=ell². Thus the naive modular quotient is not a nontrivial continuous Hilbert quotient in this topology.

### C6 — stronger finite-unitary intertwiner no-go (PROVED PAPER)

Let `S` be the unilateral ket shift on `ell²(N_0)` and `C` the cyclic shift on `C^N`. **Any bounded linear `T:ell²(N_0)->C^N` satisfying `TS=CT` must vanish.** Indeed `e_n` converges weakly to zero; bounded `T` sends it to a weakly null sequence; in finite dimensions weak convergence implies norm convergence. But `Te_n=C^n Te_0` has constant norm, because `C` is unitary. Therefore `Te_0=0`, and intertwining implies `Te_n=0` for every `n`, so `T=0`.

This is not a proof that the set quotient fails, nor that all quantum/statistical observations fail. It is a **no-go for a particular bounded Hilbert linear intertwining interface**. Finite quotients, nonlinear or classical reports, changes of measure, alternate embeddings, or weaker topologies require separately declared maps and costs. In particular, a normalized `H`-dependent quotient need not assemble compatibly into a single bounded map as `H->infinity`.

## 5. C7 — the *analytic* `1-s` reflection needs the half-density (CLASSICAL / PROVED PAPER)

On `L²(R_{>0},dx)` define for `a>0`

`(D_a f)(x)=sqrt(a) f(ax)`, and `(Jf)(x)=x^(-1) f(1/x)`.

Then `D_a` and `J` are unitary, `J²=I`, and `J D_a J=D_(1/a)`. These assertions follow by substitution `y=ax` or `y=1/x`, with `dx=dy/y²` in the second case. Note that **plain inversion** `f(x)->f(1/x)` is not unitary for `dx`: for `f=1_[1,2]`, input norm squared is `1` but the plain-inversion output norm squared is `1/2`; correct `J` restores norm squared `1`.

For compactly supported test `f` bounded away from `0`, define the Mellin transform

`M f(s)=integral_0^infinity f(x) x^(s-1) dx`.

A change of variables gives

`M(Jf)(s)=M f(1-s)` and `M(D_a f)(s)=a^(1/2-s)M f(s)`.

Write `x=e^u`, `g(u)=e^(u/2) f(e^u)`. Then `||g||_(L²(du))=||f||_(L²(dx))`, `D_(e^h)` becomes `g(u)->g(u+h)`, and `J` becomes **parity** `g(u)->g(-u)`. On `s=1/2+it`, the Mellin transform is the Fourier transform (up to sign and normalization) of `g`; this explains why `1/2` is the natural `L²(dx)` line for *this choice of measure and half-density*.

**Crucial scope firewall:** There is a unitary operator implementing a reflection on arbitrary `f`, but most `f` are not themselves `J`-invariant. Neither the identity `M(Jf)(s)=M f(1-s)` nor the simple address involution `n->1-n` proves `Lambda(s)=Lambda(1-s)` for the authentic zeta source. Tate-style zeta completion additionally requires genuine local Euler/Gamma data and Poisson/Fourier duality. And a completed functional equation, even when proved, does not imply RH.

**Attribution:** NIST DLMF `1.14(iv), `https://dlmf.nist.gov/1.14.iv` (Mellin convention); Terence Tao, *Tate's proof of the functional equation*, `https://terrytao.wordpress.com/2008/07/27/tates-proof-of-the-functional-equation/` (extra Poisson/adele source bridge). This note supplies its own elementary substitution proof for the involution.

## 6. Source-typed acceptance contract for sibling finite-to-global branches

| Interface | Valid classical fact | Evidence not licensed by it |
| --- | --- | --- |
| `n>=1`, `S(n)=n+1`, `V_m(n)=mn` | True source action identity `V_mS^k=S^(mk)V_m` | Euler primality or actual coefficients from covariance alone |
| Unit-origin chart `n->n-1` | Genuine formal group `x+y+xy`, affine cocycle `m-1` | Arbitrary coordinate changes admitted as source equivalences |
| Reflected chart `n->1-n` | Dual law `u+v-uv`, cocycle `1-m` | Literal equality with the analytic Mellin variable `s` |
| Finite CRT ray data | Exact compatibility, global first witness, explicit visibility budget | A witnessed global event before its actual horizon |
| `q_N` on finite state spaces | Lawful deterministic SUCC/FUCC factor | Bounded linear quotient between counting-measure Hilbert completions |
| `D_a,J` with `L²(dx)` half-density | Unitary dilation/reflection, correct `s->1-s` Mellin transform | Full Euler/Gamma source or completed zeta functional equation |
| Authentic Tate/Suzuki source | May be layered on top **with separate proof** | Any RH-strength global positivity inferred from C1–C7 |

## 7. Controls and reproducibility

- **Exact source checks:** both address charts across positive integer products; SUCC/FUCC semidirect law; composite `m=6` intentionally accepted as a multiplier but never claimed as Euler prime.
- **Adversarial:** zero-fixed dilation incorrectly substituted for the translated source; counterfeit `c(3)`; negative source addresses; incompatible CRT congruences; horizon below first triple witness; naive half-density-free inversion.
- **Independent oracle:** pairwise CRT intersections exhaustively enumerated over a finite family; residue-fiber operator norm recomputed from direct address counts; exact log-coordinate packet inner products use Fraction interval overlap.
- **No circular certification:** numerical tests establish only tested examples. Formal-group, cocycle, CRT, Hilbert no-go and Mellin claims use the separate derivations above.

```
python -m unittest discover -s tests -p 'test_classical_unit_origin.py' -v
python scripts/classical_unit_origin_probe.py --verify
python scripts/verify_provenance.py
```

Read `docs/CLAIM_SUPPLEMENT_CLASSICAL_UNIT_ORIGIN.md`, `observational_succ/classical_unit_origin.py`, `tests/test_classical_unit_origin.py`, and the SHA/JSON reproducibility receipt. Dedicated Python 3.10/3.13 CI is configured. Exact-head CI status must be checked rather than presumed.

## 8. Next verdict-changing mathematical probes

1. **Measure-compatible cylinder morphisms:** construct source-consistent conditional expectation on a *specified probability space*, distinguish normalized counting laws on finite clocks from a genuine projective Haar system, and check conditional expectations commute with the declared SUCC/FUCC actions. Avoid claiming the impossible `J_N` Hilbert map.
2. **Formal-group to Tate interface:** explicitly derive a test-space functor transporting the local multiplicative-group Haar measure `d^x` and the chosen Mellin normalization, retaining additive Fourier/Gamma and prime-power weights. Test a real source and a non-Euler mutant under identical rules.
3. **Uniform analytic tail:** quantify whether finite original-source positive operators converge in a topology strong enough for the *complete* Weil distribution, without presuming sign or importing zero locations. The classical C1–C7 results do not supply this bound.

**Verdict:** the classical address, formal group, CRT and Mellin structures are exact; naive finite Hilbert quotient gluing is refuted in a precisely typed sense. The real completed arithmetic source-to-positive-Hilbert-factor identification is **UNVERIFIED** and remains the other teams' open task.
