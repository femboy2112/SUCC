# Operation Gaussian Restoration — the canonical observational BBP source algebra

**2026-11-03. Research-only, paper derivations and exact rational/symbolic checks.**
Intended additive child of draft PR #479 at pinned `61bab5cb354e6143fd2fd7ce229ef1b8e9902538`. Root provenance: already-integrated `observational_succ/bbp_quadratic_atoms.py` and `research/2026-10-26/BBP_TWO_QUADRATIC_ATOMS.md` (original two quadratic atoms, rational filter, eight-step return, exact angular/radial channels). We do NOT claim academic priority for classical minimal realization, CRT, trace, Frobenius algebras, BBP or Mellin moments. This is a typed assembly and source-specific exact extension of the existing SUCC construction. Main, frozen source, Lean/formal, production, license, workflows and historical proof contracts remain unchanged.

Original source is **immutable**:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

Four displayed denominator terms are the Mellin moment labels, *not* literal four complex poles of the reduced rational transfer. The one selected real Weyl target remains `S_N(h)=sum_(n<=N)exp(2*pi*i*h*U_n)=o(N)` for every fixed nonzero integer h. This bound, the mesoscopic logarithmic collision bound and π base-16 normality are **OPEN**.

## GR-01. What the scalar transfer actually identifies (INHERITED exact source, NEW typed reconstruction)

Put

\[
P(t)=4-2t^3-t^4-t^5,\quad D_8(t)=1-t^8/16,
\quad D_{\rm min}(t)=(1-t^2/2)(1-t+t^2/2).
\]

The original integer-indexed BBP formula is `pi=int_0^1 P(t)/D8(t) dt`, with exact rational factorization

\[
K(t)=\frac{P(t)}{D_8(t)}=\frac{4(1-t)}{D_{\rm min}(t)}
=\sum_{m\ge0}c_mt^m.
\]

The original scalar impulse has first eight terms
`(c_0,...,c_7)=(4,0,0,-2,-1,-1,0,0)` and exact eight-shell return
`c_(m+8)=c_m/16`. Everything here is inherited from the October 26 source.

A `4x4` exact Hankel minor of the impulse is

```
[ 4,  0,  0, -2]
[ 0,  0, -2, -1]
[ 0, -2, -1, -1]
[-2, -1, -1,  0]
```

with determinant **4**. Since the reduced denominator has degree four and is coprime to the numerator, the infinite Hankel rank is exactly four. Therefore ordinary rational reachable+observable linear realizations of this *complete transfer* have state dimension four, and all minimal ones are uniquely isomorphic as pointed input/output systems. This is a standard Kalman/Hankel minimal-realization result, not a claim of a unique physical, nonlinear, or quantum source.

**Categorical construction (future-observation congruence, not heuristic).** Let the free rational successor-history space be `Q[s]`, let the linear functional `Lambda(s^m)=c_m`, and set

\[
I=\{f(s)\in\mathbb Q[s]:\Lambda(s^k f(s))=0\ \forall k\ge0\}.
\]

`I` is a shift-invariant ideal, the actual future-observational indistinguishability congruence. The exact recurrence `D_min K=4(1-t)` shows that

\[
m(s)=s^4-s^3+s/2-1/4\in I.
\]

No nonzero polynomial of degree less than four belongs to `I`, by the nonzero Hankel determinant; Euclidean division then gives `I=(m)`. Consequently the **canonical minimal realization** is

\[
\boxed{\mathcal A=\mathbb Q[s]/(m(s)),\quad u=[s],\quad b=[1],\quad \ell([f])=\Lambda(f).}
\]

The operation is a real quotient by equal future observables (a concrete SUCC/Yoneda-style observability quotient). It does *not* freely add hidden states. If another reachable-observable rational realization has the same all-time impulse, the map `[f(s)] -> f(A')b'` is well-defined by observability, bijective by reachability, and intertwines the successor, input and output. Its action on `[1]` is forced; thus the pointed minimal realization is unique up to unique pointed isomorphism.

## GR-02. Exact CRT: the forced rational algebra is a product of two quadratic fields

The polynomial factors over Q as

\[
m(s)=(s^2-1/2)(s^2-s+1/2),\quad
\mathcal A\cong\mathbb Q(\sqrt2)\times\mathbb Q(i).
\]

Both factors are irreducible and coprime. This is a **direct product of algebras**, corresponding to the **direct sum/biproduct of two distinct two-state modules**. It is NOT the tensor product `Q(sqrt2) tensor_Q Q(i) = Q(sqrt2,i)`, which is a four-dimensional FIELD and has no nontrivial idempotents. Equal dimension does not mean equal source objects.

Choose a convenient presentation `u=(1/sqrt2,(1+i)/2)` in the two factors. The value `u^8=1/16` holds in both. The splitting field over Q is `Q(i,sqrt2)=Q(zeta_8)`; this is where an actual eighth-root-of-unity description becomes available. After scalar extension from Q to Q(sqrt2), set `v=sqrt2*u`; then `v^8=1`, `v^4 !=1`. Thus it is a faithful order-eight action of the abstract cyclic group C8 on the extended state. The Galois group of Q(zeta_8)/Q is C2 x C2; do **not** confuse it with the order-eight unit group.

The eight-step return alone DOES NOT determine the selected factors: `s^8-1/16` has FOUR distinct rational quadratic factors, and a scalar eight-step clock is compatible with several unrelated readouts and factor selections. The *complete* K(t) is needed to reconstruct this precise algebra.

## GR-03. Half-clock central involution restores the discarded sector label

The intrinsic, Q-rational endomorphism

\[
\boxed{C=4u^4,\quad C^2=1,\quad C\ne1}
\]

is +1 on Q(sqrt2) and -1 on Q(i). Therefore the canonical mutually orthogonal primitive central idempotents are

\[
\boxed{e_H=(1+C)/2=1-u+2u^3,\quad e_G=(1-C)/2=u-2u^3.}
\]

They sum to 1, square to themselves, and multiply to zero. On the Gaussian sector the Q-linear complex structure

\[
\boxed{j_G=2u^2 e_G=(2u-1)e_G,\qquad j_G^2=-e_G}
\]

is source-internal. Its sign as a *chosen complex embedding* is not recoverable from real trace data; conjugating the embedding sends i to -i while retaining the same rational transfer. The **abstract pointed algebra** is canonical; a preferred clockwise orientation in an external complex chart is not.

## GR-04. The scalar source determines a nondegenerate Frobenius trace

There is a unique trace weight, in Q[s]/(m),

\[
\boxed{w=-8u^3+2u^2+2u-1=-2u\,e_H+2e_G,}
\]

such that for all m>=0

\[
\boxed{c_m=\ell(u^m)=\operatorname{Tr}_{\mathcal A/\mathbb Q}(w u^m)
=\operatorname{Tr}_{\mathbb Q(\sqrt2)/\mathbb Q}(-2u_H^{m+1})
+\operatorname{Tr}_{\mathbb Q(i)/\mathbb Q}(2u_G^m).}
\]

Explicit partial fractions independently give

\[
K_H(t)=-\frac{2t}{1-t^2/2},\qquad
K_G(t)=\frac{4-2t}{1-t+t^2/2},\qquad K=K_H+K_G.
\]

The form `B(a,b)=ell(ab)` is symmetric, associative and nondegenerate, since its basis matrix IS the 4x4 Hankel matrix (det=4). Thus `(A,1,ell,u)` is a **pointed commutative semisimple Frobenius Q-algebra**. The trace weight is a unit; its Frobenius handle is exactly

`mu Delta(1) = w^(-1) = -1/2 + u/2 + u^2 - 3u^3`,

verified both by an exact inverse Gram matrix and by multiplication. This is algebraic gluing data; a 2D-TQFT interpretation is optional and does not authenticate physical/quantum states.

## GR-05. A two-time-sample decoder recovers each hidden mode from original scalar impulses

As `C=4u^4`, if `c_m^H=ell(e_H u^m)` and `c_m^G=ell(e_G u^m)`, then

`c_m = c_m^H+c_m^G` and `4 c_(m+4) = c_m^H-c_m^G`.

Therefore **for every integer m>=0**, not just fitted finite samples:

\[
\boxed{c_m^H=\frac{c_m+4c_{m+4}}2,\qquad
c_m^G=\frac{c_m-4c_{m+4}}2.}
\]

The original first eight scalar taps `(4,0,0,-2,-1,-1,0,0)` split exactly into

```
H: ( 0, -2, 0, -1,  0, -1/2, 0, -1/4)
G: ( 4,  2, 0, -1, -1, -1/2, 0,  1/4)
--------------------------------------
P: ( 4,  0, 0, -2, -1, -1, 0,  0)
```

This establishes a **discriminating temporal probe**: observing only the eight-step scalar return loses the sign C, but observing the full temporal impulse (including lag +4) recovers C and its two spectral source channels. Time index m here is the generating-function coefficient index, NOT the original BBP recurrence time n. Confusing these two indices would be an invalid proof transfer.

## GR-06. The Mellin observer restores exactly the FOUR signed BBP forcing terms

Each sector has its own eight-tap polynomial `P_H`, `P_G` from GR-05. They add to `P=4-2t^3-t^4-t^5` EXACTLY. Define the typed Mellin observer **on P, not on K**:

\[
\mathcal M(P)(n)=\int_0^1 t^{8(n-1)}P(t)\,dt
=\sum_{j=0}^7\frac{c_j}{8(n-1)+j+1},\quad n\ge1.
\]

Then `M(P)(n)=r(n)` exactly, with ALL four original signs/poles and no source replacement. By contrast `int t^(8(n-1))*K(t)dt` is a weighted sum of *future* r(n+k) terms, NOT r(n). The distinction is essential.

The projectors split the forcing into the canonical rational components

\[
\boxed{r_H(n)=\frac{-1}{4n-3}-\frac1{4(2n-1)}-\frac1{4(4n-1)}-\frac1{32n},}\tag{6.1}
\]

and `r_G(n)=r(n)-r_H(n)` (also obtained from P_G), for every positive integer n. Both arise by exact Mellin integration of their channel polynomials; their sum is the original unmodified source. Define separate ZERO-SEEDED rational states `U_n^a=16U_{n-1}^a+r_a(n)` for `a=H,G`. Then

\[
\boxed{U_n=U_n^H+U_n^G,\qquad e(hU_n)=e(hU_n^H)e(hU_n^G).}
\]

The products are actual selected time-aligned phases, not statistically independent Gaussian and real random variables. Proving a signed cross-channel correlation saving is just as hard as proving the original Weyl gate unless additional source-specific estimates are derived.

## GR-07. Exact hidden-log cancellation and sharper source decay

Real integration of the two canonical channel transfers gives

\[
\boxed{\int_0^1 K_H(t)dt=-2\log2,\quad
\int_0^1 K_G(t)dt=\pi+2\log2.}
\]

The logarithmic boundary contributions cancel; the surviving complete original integral is π. For source moments, expansion at large real n gives

\[
r_H(n)=-\frac{15}{32n}-\frac{17}{64n^2}+O(n^{-3}),
\]

\[
r_G(n)=+\frac{15}{32n}+\frac1{2n^2}+O(n^{-3}),
\]

and the sum is

\[
\boxed{r(n)=\frac{15}{64n^2}+O(n^{-3}).}
\]

Thus the n^(-1) source components cancel and produce the original n^(-2) forcing responsible for the summable real Gamma tail/Koopman Ward error. This is **source-specific LINEAR cancellation**, not selected real Weyl cancellation. It is categorically meaningful because the two components are the canonical projectors GR-03, not an arbitrary hand-picked partial fraction split.

## GR-08. Local 2-adic descent: separately singular channels glue into an integral source

Because the linear factors `4n−3`, `2n−1`, and `4n−1` in (6.1) are odd in Z_2 (with the explicitly displayed powers of 2 kept separate), the term `-1/(32n)` is strictly of smallest valuation. Therefore for EVERY positive integer n,

\[
\boxed{v_2(r_H(n))=-5-v_2(n).}
\]

The full original r(n) has an odd denominator and is 2-integral. Since `r_G=r-r_H`, the ultrametric law gives

\[
\boxed{v_2(r_G(n))=-5-v_2(n),\qquad r_H(n)+r_G(n)=r(n)\in\mathbb Z_2.}
\]

Moreover, at the 2-adic source-index chart `t=0` the meromorphic germs are

\[
r_H(t)=-1/(32t)+5/6+O(t),\quad
r_G(t)=+1/(32t)-1/14+O(t),\quad
r(t)=16/21+O(t).
\]

The opposite principal parts cancel AND the regular pieces cancel their negative 2-adic powers. The total analytic function has 2-adic integral coefficients locally because its ORIGINAL denominator is odd everywhere on Z_2. This recovers, at the source level, the analytic 2-adic forcing underlying the previously-proved `observational_succ/bbp_two_adic.py` isometry. It does not prove real-circle near-collision bounds.

**Typed gluing:** Let `M` be the ADDITIVE GROUP of declared meromorphic rational source functions on the Z_2 index disk (allowing the zero-index pole), let `R` be its ADDITIVE SUBGROUP of analytic Z_2-valued rational source functions, and let `q:M->M/R` be the quotient in the category of abelian groups. Crucially `R` is NOT a Q_2-linear subspace: scaling by 1/2 can destroy integrality. Then the source pair lies in the equalizer / fiber relation

\[
\boxed{\mathcal G=\{(f_H,f_G)\in M\oplus M:q(f_H)+q(f_G)=0\},}
\]

and the sum map `G -> R` is well-defined. Beware: simply canceling the formal pole coefficient is too weak; a counterexample is `f_H=-1/(32t)+1/4`, `f_G=1/(32t)`, whose sum is still nonintegral. The complete defect class and all 2-adic residue data must be retained. In particular separate channel mod-2^k evaluations are NOT legal before gluing, because their reduced denominators contain 2; the original sum is integral.

## GR-09. A sharp source-selection counterexample within the SAME unit algebra

Only `u^8=1/16`, the two quadratic atoms, positive scalar return, initial coefficient c0=4 and the simple endpoint derivative are NOT enough to force the original π source. Define for rational epsilon>0

\[
\boxed{P_\varepsilon(t)=P(t)+\varepsilon\,t(1-t)^2 D_{\rm cancel}(t).}
\]

It retains all four rational quadratic return factors, the canceled sector `D_cancel`, the leading `c0=4`, the value `P(1)=0` and `P'(1)=-15`; it changes the higher source readout and preserves the same eighth-step scalar return. Its integral is

\[
\boxed{\int_0^1\frac{P_\varepsilon(t)}{1-t^8/16}dt
=\pi+\frac{67\varepsilon}{480}\ne\pi.}
\]

The added term is positive on (0,1); `P_epsilon` is positive there if P is positive. This is an explicit changed-source counterfeit, not evidence against the original FULL numerator/source. The full original K(t), including its numerator, uniquely selects w and the original four Mellin terms in the declared minimal category. The scalar eighth return by itself does not.

Likewise the unchanged exact original K, sector projections and forcing law can be paired with the DIFFERENT real initial seed `s=1/5-pi/16`; the completed point is the nonnormal x=1/5 fixed point of ×16. Hence arguments depending only on the unit algebra, original forcing and return but ignoring literal U0=0 are refuted.

## GR-10. Where 2,3,5,13 actually enter, without importing RH

The integral polynomial `4m(s)=4s^4-4s^3+2s-1` has discriminant `-2^11`. The minimal linear source algebra's discriminant identifies only the prime 2 as exceptional for this model. In contrast the original indexed Mellin forcing `r(n)=N(n)/D(n)` has

\[
\operatorname{Res}(N,D)=-2^{15}3^25^2,\quad
\operatorname{Disc}(D)=2^{24}3^25^2.
\]

Thus 3 and 5 appear at the **Mellin/indexed source map**, not as extra bad primes of the minimal rational linear algebra. The finite identity at p=13, `F_13^×=<16> x <5> ~=C3 x C4`, is an exact *different finite field quotient*; it does not force 13 into the minimal transfer's exceptional discriminant and is not an unconditional real phase saving. No Riemann zeros, RH or zeta critical-zero trajectories are premises of any theorem above.

## GR-11. The next admissible genuinely new Weyl estimate

An exact source-aligned phase splitting exists:

\[
\frac1N\sum_{n=1}^N e(hU_n)
=\frac1N\sum_{n=1}^N e(hU_n^H)e(hU_n^G).
\]

This is an identity, not decay. A useful theorem would have to prove a source-selected, all-prefix **joint** estimate for the product, e.g. the original logarithmic-mesh bound from #476 `E_(A,m_A)=o(log m_A)` with `m_A~log A`, or a lower-level non-conspiracy bound on the exact cross-carry constraint that genuinely implies it. A marginal Haar or Galois-average theorem for either channel is insufficient; the 2-adic cancellation shows they are structurally coupled.

**Next discriminating probe:** derive an exact (not fitted) count of intervals where the two sector real carries have anomalously aligned fractional parts, with simultaneous original n and original zero seeds. Compare (a) original, (b) sector-shuffled temporal controls, (c) the rational positive `P_epsilon` mutant, (d) same original forcing but coherent wrong initial seed, and (e) local 2-adic quotient applied illegally before gluing (must reject). A proof candidate must predict a different unbounded-family bound for the authentic selected source and withstand holdouts. If it does not, classify as a representation identity.

### Claim ledger

- **Disclosed (paper, exact algebra):** GR-01 Hankel observational quotient; GR-02 finite étale CRT and order-eight extension; GR-03 central involution/idempotents/complex structure; GR-04 nondegenerate Frobenius trace/readout; GR-05 all-n four-step sector recovery; GR-06 all-n original Mellin forcing recovery; GR-07 exact log cancellation / source asymptotics; GR-08 2-adic pole and integrality descent; GR-09 explicit changed-source counterexample; GR-10 source-map distinction. No new Lean compilation claimed.
- **Observed:** specified finite code/holdout executions, always with explicit scope and hashes; same-reasoner independent algorithms do NOT amount to blind referee corroboration.
- **Conjectured/UNVERIFIED:** an actual new original selected cross-sector real carry/collision inequality. Existing pi normality gate still OPEN.
- **Refuted within stated scope:** uniqueness from eight-step return alone; tensor identification of algebra factors; 2-adic integral reduction of separate nonintegral sector sources; automatic real cancellation from exact Gaussian-unit trace or from local carrier Haar.

### External mathematical provenance (classical)

- Exact original two-atom rational BBP transfer and angular/radial decomposition: SUCC `research/2026-10-26/BBP_TWO_QUADRATIC_ATOMS.md`; classical BBP derivation of Bailey/Borwein/Plouffe and later source analyses.
- Ho/Kalman minimal realization: standard reachable-observable realization and Hankel-rank theorem; see original external references in SUCC and https://doi.org/10.1016/S0377-0427(00)00341-1 (standard results, not source-specific proof of normality).
- Chinese remainder theorem, finite étale algebra trace, semisimple commutative Frobenius pairing, rational canonical form, 2-adic ultrametric law: classical algebra.
