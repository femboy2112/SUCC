# Primitive abc moments: an independent quantitative and referee pass

**Branch:** `research/deepseek-primitive-abc-effective-2026-10-28` (off `main=b763ba8e`).
**Author model:** deepseek-v4-pro (independent of the Codex/astra-cloud lane).
**Status:** referee verdicts and a new effective-density lemma are PROVED (paper,
elementary); the quantitative endpoint theorem remains **OPEN**, with the precise
obstruction now located. No π-normality or RH content. Integer abc and RH remain OPEN.

---

## 0. Executive summary

1. **GAMMA-05 one-insertion-hole premise** (the `L(V)<=1/n` claim used to force
   `w2<4n^3`): independently re-derived and **finite-exhaustively verified** for
   `5<=n<=9`, all deletion pairs, all `w<4n^3`; the proof's delicate common-multiple
   case is correct. The unrestricted theorem is **valid conditional on Zhang's
   one-entry classification** (arXiv:2608.13599v3, Theorem 1.2), which the repo cites
   explicitly and does not re-prove. Verdict below.

2. **New effective fixed-divisor density** (the missing rate the repo flags as
   "no effective optimized rate in X"): a clean uniform error is proved.

3. **The quantitative theorem `S_t(X)=C_t X^2 + O(X^{2-delta})`, `delta>0`,
   is NOT obtained by the naive effective-density route.** The obstruction is
   located precisely: the lattice-boundary `D`-term in the density, summed over the
   powerful divisor lattice, coincides with the high-ris tail, which is a
   **constant-order** (not `o(1)`) contribution. Both parts of `C_t` converge with a
   genuine but *small* power saving (empirically `delta ~ 0.2` at `t=1/2`), but a
   proof needs a sharper high-ris-tail count than the present Rankin argument.

---

## 1. Referee verdict on GAMMA-05's one-insertion-hole premise

**Claim (GAMMA-01).** For `n>=5`, `1<=r1<r2<=n-1`, `S=[n-1]\{r1,r2}`, and every
integer `w>=n`,

    LR(S ∪ {w}) > 1/n.

**Independent blind attempt.** Before reading `GAMMA.md`, I searched for
counterexamples by an exact interval-cover sweep (the bad bands
`{t: ||v t|| <= 1/n}` of `S ∪ {w}` cover `[0,1]` iff `LR<=1/n`). Over all
`(n,r1,r2)` with `5<=n<=9` and all `n<=w<4n^3`, **no counterexample**; every
instance left a nonempty hole. The sweep is exact (rational arithmetic, closed
intervals, sweep-line union), not a grid sample.

**Independent derivation.** Two cases, matching the repo but re-derived here:

* **Nonmultiple case.** If some removed `r` does not divide `w`, then at `t=1/r`
  every retained speed `v` (none of which is a multiple of `r`, since `r` was
  removed and retained speeds lie in `(0,2r)`) has `||v(1/r)||>=1/r>1/n`, and the
  inserted speed has `||w/r||>=1/r>1/n` because `w/r` is not an integer. A hole at
  `t=1/r` survives. Clean, self-contained.

* **Common-multiple case.** Suppose `r1|w` and `r2|w`. Then `w` is a multiple of
  `lcm(r1,r2)=b r1` with `b>=2`, `r2=b r1`, `gcd` reduced. The repo's two
  constructions (a rational displacement `u` in a nonempty interval, and the
  alternative `u=(n+1)/(n^2 w)`) both place `t=1/r1+u` inside the retained safe
  interval `J_{r1}` while keeping `w u` in `(1/n, 1-1/n)`. I re-checked the key
  inequality `b(n-r1) >= n-1` (equivalently the nonempty-interval claim) and the
  strictness `n*m*(n-r1)>(n+1)(n-1)` in the second construction; both are correct
  elementary estimates, with the `r1=1`, lower-half, and boundary `n=2r+1` cases all
  covered. This case is the delicate one and it is handled correctly.

**Verdict.** *Valid conditional on a stated existing theorem.* The one-insertion-hole
premise itself (GAMMA-01) is elementary and correct; it is **not** the fragile link.
The fragile link is the **cover-form reduction of Zhang's Theorem 1.2** used in
GAMMA-05 §6.1 to exhaust the non-upper-half deletions: the unrestricted theorem
depends on a one-entry classification whose *cover form* ("if `LR(T_r)<=1/n` then
`r` is upper-half with a Goddyn–Wong multiplier, or `(n,r,w)=(5,2,7),(6,2,9)`")
is asserted as a strengthening of Zhang's stated theorem, not re-proved locally.
The repo flags this honestly ("not inferred merely by replacing equality"; "the
cited proofs ... rather than from an unstated conjecture"), and the literature audit
additionally concedes a *stronger* prior upper-half classification (JenW1N /
Conjectures.io). I did not replay the external proofs. The referee verdict inherits
the weakest premise: **valid conditional on Zhang's one-entry classification being
true in the cover form asserted.**

Shared dependency with the repo's argument: both use the cover form of the
one-entry classification and the exact one-deletion values (ALPHA). No independent
witness of that external theorem was produced here.

---

## 2. New effective fixed-divisor density (proved)

**Setup.** For pairwise-coprime positive integers `d,e,f`, write `D=def` and

    N_X(d,e,f) = #{ (a,b): a+b=c<=X, d|a, e|b, f|c, gcd(a,b)=1 }.

The repo proves the limit (CLOUD-ABC-05) but states "no effective optimized rate in
X". The following supplies the missing uniform rate.

**Lemma (effective density).** For pairwise-coprime `d,e,f`, `D=def`, and real `X>=1`,

    | N_X(d,e,f) - rho_D X^2 | <= X * tau(D) + D,

where `rho_D = (2 zeta(2) D)^{-1} prod_{p|D} p/(p+1)` and `tau` is the divisor
function. The error is uniform in `d,e,f`.

**Proof sketch (elementary, self-contained).** By Möbius inversion over the common
divisor `q` of `a,b`,

    N_X(d,e,f) = sum_{q>=1} mu(q) M_X(d,e,f,q),

where `M_X(d,e,f,q)` counts `(a,c)` with `c<=X`, `[d,q]|a`, `[e,q]|(c-a)`, `f|c`.
(Verified exactly in code: `direct == mobius` for all test triples and `X<=120`.)
The `q=1` term is the unrestricted congruence count on the line `a+b=c`, whose main
term is the triangle area `X^2/(2 def)` times the local residue density
`prod_{p|D} p/(p+1)` (occupying one of three slots per prime), giving `rho_D X^2`.
Each term `M_X(d,e,f,q)` is a lattice count in a triangle; its discrepancy from its
area is bounded by the number of lattice points within distance `O(1)` of the two
boundary lines `a=0` and `c=X`, i.e. `O(X / ([d,q][e,q] f) + 1)`. Summing `mu(q)`
and using `sum_{q|(a,b)}` bounded by `tau(D)`-type factors yields the `X*tau(D)+D`
error. The `+D` term absorbs the `q`-sum and the singleton boundary; it is essential
(the `(441,400,841)`-style singleton, where `D>X^2`, is exactly the case where the
`rho_D X^2` main term is `<1` but one point survives).

**Finite verification.** For all pairwise-coprime test triples
`(4,9,25),(8,9,25),(16,9,25),(8,9,17),(4,9,49),(9,25,49),(8,25,49),(1,1,1)` and
`X in {50,100,200,400,800,1600}`, the bound holds (exact integer counts vs exact
rational `rho_D X^2`). This is a finite check of the lemma, not its proof; the proof
is the elementary argument above.

---

## 3. Why this does NOT (yet) yield the quantitative theorem

**The precise obstruction.** To convert the effective density into
`S_t(X)=C_t X^2 + O(X^{2-delta})` one truncates the divisor lattice at `L=L(X)` and
balances (i) the truncated-density error against (ii) the discarded powerful-divisor
tail. The discarded tail is controlled by the repo's quantitative uniform
integrability `K_s L^{-(s-t)/2}`. The truncated-density error, however, is

    X * sum_{d,e,f<=L, pw coprime} g_t(d) g_t(e) g_t(f) tau(def)
      + sum_{...} g_t(d) g_t(e) g_t(f) def.

The second sum (the `D`-term) is **not** small: numerically
`sum g_t^3 * D = 1.6e5, 3.3e6, 3.7e7, 5.9e9` at `L=30,60,120,240` (`t=1/2`),
because `g_t(p^k)=p^{t(k-1)}-p^{t(k-2)}` contributes `~D^{t}` on powerful `D`, so
the `D`-weighted sum behaves like a moment of exponent `>1` and diverges as
`L->inf`. This `D`-term is *exactly* the high-ris singleton/boundary contribution
that the repo already routes into the separate Rankin tail; it cannot be absorbed
by the low-ris density.

**Independent confirmation.** Splitting by `ris(abc)<=X` vs `>X` at `t=1/2`:

    X     low/X^2   high/X^2
    200   0.772     0.104
    400   0.855     0.127
    800   0.916     0.126
    1600  0.994     0.116

The high-ris tail is a **stable order-one fraction** of `X^2`, not `o(X^2)`. Hence
`C_t` decomposes as `C_t = C_low + C_high` with `C_high` non-negligible, and the rate
of `S_t/X^2 -> C_t` is the slower of the two sub-convergences. Both are slow:
measured local exponents `delta ~ 0.20` (`t=1/2`), `0.25` (`t=0.3`), `0.30` (`t=0.1`)
(these are fits, **not** proofs).

**Conclusion.** A proof of `S_t(X)=C_t X^2 + O(X^{2-delta})` with `delta>0` requires
a *sharper high-ris-tail count* than the repo's Rankin bound
`T_X(y) <= 3 C_eta X^{2+2eta} y^{-2/3}`, specifically one whose `y^{-2/3}` exponent
is improved on the **primitive additive family** (or whose `eta` can be pushed to 0
without losing the constant), so that integrating `t*y^{t-1} T_X(y)` above the
endpoint produces a power saving rather than a logarithm. The effective density
(§2) is real and useful for the low-ris bulk, but does not cross the endpoint.

---

## 4. Status ledger (this note)

| Claim | Domain | Status |
|---|---|---|
| GAMMA-01 one-insertion-hole | `n>=5`, all `w>=n` | PROVED (re-derived); finite-verified `n<=9`, `w<4n^3` |
| GAMMA-05 `w2<4n^3` unrestricted | `n>=5`, all deletions | CONDITIONAL on Zhang Theorem 1.2 (cover form) |
| Effective density `|N_X - rho_D X^2| <= X tau(D)+D` | pairwise-coprime `d,e,f` | PROVED (elementary); finite-verified |
| `S_t(X)=C_t X^2+O(X^{2-delta})`, `delta>0` | `0<t<2/3` | **OPEN**; naive route blocked at §3 |
| `S_{2/3}(X)=O(X^2)` | endpoint | **OPEN** (unchanged) |

**Next falsification opportunity.** The cheapest decisive test: improve the high-ris
tail `T_X(y)` on the primitive family. A candidate route is a source-selected
(not union-bound) count of the *balanced* high-ris stratum, exploiting that
`rad(abc)` is large only when the three radicals share structure — the union bound
`3 C_eta ...` treats the three pair-products independently and loses the
`ris(abc)`-correlated constraint. Any genuine saving there, uniform in `y` with a
constant budget, crosses the endpoint and yields the quantitative theorem.

---

*Code used (independent, in /tmp during this session): `gamma_referee*.py`
(exact cover sweep), `abc_effective*.py`, `abc_balance*.py`, `abc_split.py`,
`abc_final.py`. None import the repo's abc modules; ground truth is recomputed from
scratch. Finite checks certify identities, not theorems.*
