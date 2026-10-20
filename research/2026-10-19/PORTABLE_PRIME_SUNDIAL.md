# The portable prime sundial: a source-indexed rational SUCC carrier

**Date:** 2026-10-19. **Parent:** SUCC Academic Main V, main commit `455600a2e013895c36238a3a97e0f470fd7ba197`. **Branch:** `research/portable-prime-sundial-rational-succ-2026-10-19`.  
**Status:** elementary integer/projective/CRT mathematics (PROVED PAPER), exact finite implementations (TESTED MODEL), and a possible categorical/observer interface (HYPOTHESIS). **Academic novelty unverified. ABC OPEN. RH OPEN. Signed Suzuki S4 OPEN.**

## Abstract

The proposed portable sundial is **not** a physical clock and is **not** merely a
fraction. It is a source-retaining state `(a,b;u,v)`: two integer arms with
independently chosen SUCC units, their ratio report, and their genuine-prime
congruence clocks. The analogy is that an arithmetic system contains both a
movable pointer (the ratio) and a collection of local prime-power dial faces.
Transporting the instrument must preserve the frame, its units, and the
provenance of the arithmetic source.

The central object is one integer

\[
D=ub-va.
\]

This **same** number determines the direction and size of the ratio's real
diagonal drift and bounds every numerator/denominator cancellation in that
diagonal orbit. At prime powers coprime to both step units, it also controls
whether the two modular zero-clocks can coincide. This real/local coincidence
is classical algebra; the explicit source-indexed packaging is new to SUCC.

The mathematical reward is not the name "sundial": it is a pair of exact
local-to-global interfaces with positive and negative certificates.

## 1. Domain and the four different objects being compared

Let `a,b,u,v` be **positive integers** and `k,l in N`. Define

\[
A_k=a+ku,\qquad B_l=b+lv,\qquad F(k,l)=\frac{A_k}{B_l}.
\]

The original source frame is the typed quadruple `(a,b;u,v)`, not the reduced
rational `a/b`. The two actions

\[
S_A:(k,l)\mapsto(k+1,l),\qquad
S_B:(k,l)\mapsto(k,l+1)
\]

**commute as actions** on the independent carrier `N^2`. The report
`F(k,l)` nevertheless couples them:

\[
\begin{aligned}
\Delta_A F(k,l)&=\frac{u}{B_l},\\
\Delta_B F(k,l)&=-\frac{v A_k}{B_l(B_l+v)},\\
\boxed{\Delta_A\Delta_BF(k,l)}
&=\boxed{-\frac{uv}{B_l(B_l+v)}}.
\end{aligned}
\]

No noncommutative source operation or quantum effect is implied. The mixed
difference is just the discrete response to two commuting operations after
passing through a nonlinear ratio observable.

There are four distinct levels:

1. **Source carrier** `(A_k,B_l)` with retained units `(u,v)`.
2. **Rational report** `F(k,l)`, which may erase source distinctions.
3. **Clock observations** `A_k mod p^r` and `B_l mod p^r` for genuine primes.
4. **Original-source certificate** that the arithmetical charts truly arise
   from the intended original carrier; a label alone never proves this.

## 2. Sundial determinant theorem: one real and arithmetic invariant

Define the oriented cross-difference

\[
D(k,l)=uB_l-vA_k.
\]

**PS-01 (CLASSICAL / PROVED ELEMENTARY).** For all `k,l in N`,

\[
\boxed{D(k,l)=D_0+uv(l-k)},\qquad D_0=ub-va.
\]

Consequently on the diagonal `(k,l)=(n,n)`,

\[
\boxed{D(n,n)=D_0}\quad\text{for every }n\ge0.
\]

*Proof.* Expand `u(b+lv)-v(a+ku)`. The mixed `uvn` terms cancel
along the diagonal. Nothing infinite is assumed.

**PS-02 (CLASSICAL / PROVED ELEMENTARY — Archimedean pointer).**

Write `F_n=F(n,n)`, `B_n=b+nv`. Then

\[
\boxed{F_{n+1}-F_n=\frac{D_0}{B_n(B_n+v)}},
\qquad
\boxed{F_n-\frac uv=-\frac{D_0}{vB_n}}.
\]

Thus if `D_0>0`, the pointer increases strictly toward `u/v`; if
`D_0<0`, it decreases strictly toward `u/v`; if `D_0=0`, it
is constant. These are exact signed identities, not asymptotic fits.
For `D_0 != 0` convergence is `O(1/n)`.

**PS-03 (CLASSICAL / PROVED ELEMENTARY — prime cancellation).**

For every `n`,

\[
\boxed{g_n:=\gcd(a+nu,b+nv)\mid D_0}.
\]

*Proof.* `g_n` divides both integers; it therefore divides their
integer linear combination `uB_n-vA_n=D_0`.

When `D_0!=0`, `g_n<=|D_0|`, and for each prime `p`,

\[
v_p(g_n)\le v_p(D_0).
\]

This is a **one-way bound**. A prime dividing `D_0` need not cancel,
because the step units can be noninvertible at that prime.

**PS-04 (CLASSICAL / PROVED ELEMENTARY — degenerate fork).**
If `D_0=0`, put `g=gcd(u,v)`, `u=g u'`, `v=g v'`,
`gcd(u',v')=1`. The equality `ub=va` forces a unique positive
integer `t` such that `a=t u'`, `b=t v'`. Hence

\[
\boxed{\gcd(a+nu,b+nv)=t+ng}.
\]

The ratio is stationary, yet the common factor grows linearly.
This is the decisive counterexample to asserting any universal finite
gcd bound without `D_0!=0`.

These four statements tie the real pointer and the integer cancellation
structure to the **same conserved cross-difference**.

## 3. Source-relative prime-power dial faces

Fix a genuine prime `p`, depth `r>=1`, and `M=p^r`.

We need the exact congruence

\[
a+ku\equiv0\pmod M.
\]

Put `t=min(r,v_p(u))`. The set of allowed `k` is empty unless
`p^t|a`; otherwise it is precisely **one residue class modulo**
`p^{r-t}`. The modulus is 1 if every nonnegative time qualifies.
The same theorem applies to `b+lv`.

**PS-05 (CLASSICAL / PROVED ELEMENTARY — partial nonunit clock).**
Along an offset diagonal `l=k+d`, solve

\[
a+ku\equiv b+(k+d)v\equiv0\pmod{p^r}.
\]

Each arm contributes one residue class or none; the intersection is
nonempty exactly when those classes agree modulo their smaller period.
The periods are powers of the same prime and hence nested.

The resulting report contains source- and unit-basis-labelled
`numerator_class`, `denominator_class`, `diagonal_class`,
counts of grid and diagonal solutions modulo `p^r`, and an optional
phase only when both units are invertible modulo `p^r`.

**Negative control.** Take `(a,b;u,v)=(1,2;2,2)`. Then `D_0=2`,
so `2|D_0`, but `1+2k` is never even. A claimed clock asserting
"p divides determinant, therefore cancellation at p is attained"
would be false. The exact nonunit clock correctly returns no
numerator solution at `p=2`.

### The local prime phase

If `p\nmid uv`, both step units are invertible modulo `p^r`
There are unique zero-times

\[
k_p=-a\,u^{-1},\qquad l_p=-b\,v^{-1}\pmod{p^r}.
\]

Define the **relative sundial phase**

\[
\boxed{\delta_{p,r}=l_p-k_p
\equiv-\frac{D_0}{uv}\pmod{p^r}}.
\]

The division means multiplication by an actual unit inverse in the
residue ring. It is **not defined by this formula** if `p|uv`.

**PS-06 (CLASSICAL / PROVED ELEMENTARY — diagonal clock test).**

For `p\nmid uv`,

\[
\exists n:\;p^r\mid A_n, p^r\mid B_n
\quad\Longleftrightarrow\quad
\boxed{p^r\mid D_0}.
\]

In that case the successful time is exactly
`n=-a u^{-1} mod p^r` (one residue class).
This proves **sufficiency** for invertible-unit primes, strengthening
the general necessary condition of PS-03.

## 4. The portable prime wheel and simultaneous time certificate

Let `W=prod_i p_i^{r_i}` for finitely many distinct genuine primes,
and assume `gcd(uv,W)=1`.

Each local dial has `delta_i=-D_0(uv)^{-1} mod p_i^{r_i}`.
The Chinese remainder theorem encodes the readings into one clock:

\[
\boxed{
\delta_W=-D_0(uv)^{-1}\pmod W,
\quad
k_W=-a u^{-1}\pmod W,
\quad
l_W=-b v^{-1}\pmod W.
}
\]

**PS-07 (CLASSICAL / PROVED ELEMENTARY — portable arithmetic sundial).**
The `p_i^{r_i}` local relative phases glue to the unique
`delta_W=l_W-k_W` modulo `W`. Choosing the nonnegative representatives
`k=k_W` and `l=k+delta_W` gives an actual pair `(k,l)` for which

\[
\boxed{W\mid A_k\quad\text{and}\quad W\mid B_l}.
\]

The requirement `l-kequivdelta_W mod W` is source-compatible.
The original diagonal `l=k` is generally **not** compatible with it.

With `(a,b;u,v)=(1,2;1,1)`, a factorial-style wheel
`W=2^3cdot3cdot5=120` yields

\[
\delta_W=119,\quad k_W=119,\quad l_W=118,\quad
(k,l)=(119,238).
\]

The actual arms are `A_{119}=120`, `B_{238}=240`.
The ratio at the original `(0,0)` was `1/2`, and no prime
distribution theorem was needed for this **constructed arithmetic
synchronization**.

A finite wheel does not determine a physical clock, a globally unique
source, the prime number theorem, or an infinite all-prime clock.

### Arbitrary units and offsets

For nonunit moduli the `phase_wheel` interface refuses to invent
a phase. Instead `crt_synchronize` combines the exact *partial*
congruence classes of the offset-diagonal observer; different prime
periods are coprime, so compatible local solutions glue by ordinary CRT.
A suitable nonnegative time is constructed if and only if each local
constraint is satisfiable.

## 5. Sharp prime-to-unit cancellation theorem

Let `D_0 != 0` and let `M` be the **largest positive divisor
of `|D_0|` coprime to `uv`** (remove all prime powers sharing
a prime with `uv`).

**PS-08 (CLASSICAL / PROVED ELEMENTARY — sharp attainable sector).**

There exists an explicit nonnegative diagonal time `n` for which

\[
\boxed{M\mid \gcd(A_n,B_n)}.
\]

*Proof.* Because `gcd(u,M)=1`, choose
`n=-a u^{-1} mod M` (or `n=0` if `M=1`).
Then `M|A_n`. The determinant law implies `M|uB_n`
because `M|D_0`. Invertibility of `u` implies `M|B_n`.
Thus `M|gcd(A_n,B_n)`.

Example: `(a,b;u,v)=(1,20;3,5)`, `D_0=55`,
`uv=15`, `M=11`, `n=7` gives arms
`22,55`, whose gcd is 11.

This sharpens the naive rule "cancellation primes lie in D" by
exhibiting a jointly attainable sector and explaining exactly where
the proof breaks for unit-dividing primes.

## 6. Radical-unit frame: when arithmetic births change the dial

Define `r_a=rad(a)`, `t_a=ris(a)=a/r_a`, and likewise
`r_b,t_b`. Choose the **initial RAD units** `u=r_a,v=r_b`.

Then

\[
A_k=r_a(t_a+k),\qquad B_l=r_b(t_b+l),
\]

and the conserved diagonal determinant is

\[
\boxed{D_0=r_ar_b(t_b-t_a)}.
\]

This is the earlier proposed RIS-coordinate time, but the
original RAD units are only a **frame**. They are not necessarily
the RADs of the later integer states.

Define the exact prime-birth factor

\[
J_r(m)=\prod_{\substack{p\mid m\\p\nmid r}}p.
\]

**PS-09 (CLASSICAL / PROVED ELEMENTARY — RAD/RIS update).**

\[
\boxed{
rad(A_k)=r_aJ_{r_a}(t_a+k),\quad
ris(A_k)=\frac{t_a+k}{J_{r_a}(t_a+k)}
}
\]

and analogously for `B_l`. Proof: the prime support of a product
`rm` is the union of the supports of `r` and `m`, and
`r` is squarefree.

For `12/18`, both RAD units initially equal 6, while the RIS values
are 2 and 3. Two diagonal RAD-unit steps produce `24/30`:
`rad(24)=6,ris(24)=4`, but `rad(30)=30,ris(30)=1`.
Prime 5 is a **denominator birth**; it does not cancel, because
`D_0=36` contains only primes 2 and 3.

A RAD unit is a source label. Silently updating the unit as primes
are born would produce a DIFFERENT dynamical law and requires its
own explicitly typed frame change.

## 7. Portability laws — what is preserved, and what is not

**PS-10 (CLASSICAL / PROVED ELEMENTARY — frame transformations).**

1. **Homogeneous rescaling** `(a,b;u,v) -> (ma,mb;mu,mv)`
   for `m>0` preserves **every rational report** `F(k,l)`
   and the rational clock-origin difference
   `alpha-\beta=a/u-b/v`; it multiplies `D_0` by `m^2`
   and every common gcd by `m`.
   It does NOT preserve raw `p`-adic occupation numbers for
   primes dividing `m`. Prime wheel phases remain identical when
   `gcd(m,W)=1`, with the necessary inverse-unit hypotheses.
2. **Independent origin shift** `a'=a+hu,b'=b+jv` for
   `h,j>=0` represents the same carrier from a later chart:
   `F'_{k,l}=F_{k+h,l+j}`.
   The phase transforms **covariantly** as
   `delta'=delta+h-j`. The determinant changes by
   `D'_0=D_0+uv(j-h)`. Calling it an invariant under
   unequal chart shifts is incorrect.
3. **Premature rational reduction loses dynamics.** The two
   frames `(1,2;1,1)` and `(2,4;1,1)` both initially
   report `1/2`, but after one diagonal step report `2/3`
   and `3/5`. Their determinants are 1 and 2.
   In contrast `(1,2;1,1)` and `(2,4;2,2)`
   are full homothetic frames and have identical ratio trajectories.

This is a source-level counterexample to assuming a deterministic
future ratio on the quotient `(a,b;u,v) -> a/b` without an
observational-fiber-compatibility proof. Compare the existing
`formal/EODCS_CausalDescent.lean`,
`formal/MetaChoiceRelationalDescent.lean`, and the source-ghost gates.

The word **portable** means these lawful transformations and their
source/basis witness maps are **known and checked**, not that one can
freely throw away information or that every rational representation
is interchangeable.

## 7A. Three-shadow theorem: a portable sundial needs three rational probes

For each full source frame, consider the *three canonical mathematical
measurements*:

\[
q_{00}=F(0,0)=\frac ab,\qquad
q_{10}=F(1,0)=\frac{a+u}{b},\qquad
q_{01}=F(0,1)=\frac{a}{b+v}.
\]

**PS-13 (CLASSICAL / PROVED ELEMENTARY — finite projective reconstruction).**
Assuming positive integer a,b,u,v, define

\[
x=q_{00},\qquad
y=q_{10}-q_{00},\qquad
z=\frac{q_{00}}{q_{01}}-1.
\]

Then

\[
\boxed{x=\frac ab,\quad y=\frac ub,\quad z=\frac vb},
\qquad
\boxed{F(k,l)=\frac{x+ky}{1+lz}}\quad(k,l\ge0).
\]

*Proof.* Direct substitution: q10−q00=u/b, and
q00/q01−1=(b+v)/b−1=v/b; divide both A_k and B_l by b.

**Corollary (exact indistinguishability classification).**
Two positive integer sundial frames have identical F(k,l) for every
(k,l) in N² **if and only if** all their four coordinates are
proportional by the *same positive rational scale*. Equality of these
three canonical rational probes is both necessary and sufficient for
the whole infinite two-dimensional report family.

*Proof.* Sufficiency is the displayed formula. Necessity follows from
equality at (0,0),(1,0),(0,1), which forces equality of the normalized
triples (a/b,u/b,v/b). Put m=b'/b to obtain
(a',b',u',v')=m(a,b,u,v).

This is a **finite mathematical model-identification theorem**, not a
claim of observing infinitely many physical future events.

**Canonical minimal integer representative.** From exact positive
Fractions x,y,z, choose b equal to the least common multiple of their
three denominators. Then a=bx,u=by,v=bz are integers. The resulting
frame is primitive as a four-tuple: a common factor dividing all four
would permit a smaller positive b, contradicting its minimality.
This construction is a projective *representative*, **not** evidence
of the original integer scale. It is implemented by
\`reconstruct_three_shadows\`, with floats and invalid data rejected.

**Sharpness for the three canonical probes.** Every proper two-element
subset of the specified triple can fail to distinguish source frames:

| Observed probes | Base frame | Different frame | Hidden change |
|---|---|---|---|
| (0,0),(1,0) | (1,2;1,1) | (1,2;1,2) | denominator unit |
| (0,0),(0,1) | (1,2;1,1) | (1,2;2,1) | numerator unit |
| (1,0),(0,1) | (1,2;1,1) | (2,3;1,3) | initial ratio |

In each row the observed two ratios agree exactly but the full
ratio dynamics differ. This proves **minimality for that canonical
set**, not a universal minimum over arbitrary adaptive probes or
other mathematical observation languages.

**Recoverable phase, nonrecoverable prime occupation.**
These three probes determine the projective clock origin difference

\[
\alpha-\beta=\frac au-\frac bv=\frac{x}{y}-\frac1z.
\]

When p does not divide the units, this rational phase has a valid
mod-p^r interpretation. But a homogeneous scale can multiply every
integer source arm by p while preserving every rational ratio report,
changing the original p-adic occupation counts. Thus the three
shadows do NOT authenticate the true scale or prime valuation of the
original source.

**Counterfactual-access firewall.** The construction assumes the
mathematical observer can compare *three reports from the same
underlying frame*, including independent one-step paths. A physical
source which cannot be reset, duplicated, or legitimately queried
along both forks may not provide those measurements. No amount of
algebra on formal counterfactual reports grants such access.
Compare SUCC's source-relative proof-access and EODCS causal
descent contracts.

**PS-14 (CLASSICAL/TESTED — observation insufficiency).**
The ratio q00 alone and each proper subset of the canonical three
readings fail to identify the full frame; original *absolute integer
scale* and physical source identity remain inaccessible even from
all rational reports without additional source data. The exact
finite adversarial tests cover all three omitted-probe directions
and a full homothetic gauge.

## 8. Steelman → crucible → verdict

| ID | Statement | Status | Hostile control / next falsifier |
|---|---|---|---|
| PSD-01 | 2D independent SUCC actions commute while ratio finite differences couple | CLASSICAL / PROVED PAPER | finite exhaustive grid oracle, wrong mixed-sign mutation |
| PSD-02 | Diagonal determinant governs exact ratio drift | CLASSICAL / PROVED PAPER | exact difference checks including negative D |
| PSD-03 | Diagonal gcd divides D; if D!=0 only primes of D cancel | CLASSICAL / PROVED PAPER | D=0 stationary family refutes unconditional bounded gcd |
| PSD-04 | D=0 gives gcd=t+ng | CLASSICAL / PROVED PAPER | stationary family (6,10;3,5) |
| PSD-05 | Nonunit p-power arm roots are empty or one p-power residue class | CLASSICAL / PROVED PAPER | (1,2;2,2), p=2 refutes p|D sufficiency |
| PSD-06 | Invertible-unit p-power common cancellation iff p^r|D | CLASSICAL / PROVED PAPER | independent brute-force modular root sets |
| PSD-07 | CRT-wheel phase is -D/(uv) mod W and yields explicit independent k,l witness | CLASSICAL / PROVED PAPER | nonunit wheel refused; orientation and source labels |
| PSD-08 | Largest prime-to-uv divisor M of nonzero |D| is attained in some diagonal gcd | CLASSICAL / PROVED PAPER | exact M=11,n=7; exhaustive small frames |
| PSD-09 | RAD frame new-support factor J gives exact later RAD/RIS | CLASSICAL / PROVED PAPER | 12/18→24/30, new denominator prime 5 |
| PSD-10 | Full rescale preserves rational path; rebase shifts phase; fraction-only quotient loses SUCC future | CLASSICAL / PROVED PAPER | 1/2=2/4 but 2/3 !=3/5 next |
| PSD-11 | A source-indexed all-prime/adelic sundial exists, or is physically measurable | UNVERIFIED | finitely many prime-clock readings do not authenticate the source |
| PSD-12 | Sundial yields ABC exceptional-set improvement or signed-Weil/RH positivity | UNVERIFIED | requires new primitive a+b=c correlations / completed signed-form equality |

No proof-status promotion follows from the local exhaustive checks. A finite
algorithm using actual integer arithmetic can encode prime clocks but does
**not** thereby construct the natural numbers from nothing, authenticate a
physical observer, or prove a new arithmetic distribution theorem.

## 9. Reproducible finite evidence

Module `observational_succ/portable_prime_sundial.py`.

- Exact oracle tests: `tests/test_portable_prime_sundial.py`, 20 methods, including
  625 four-parameter frames for two-dimensional identities, 256 frames for
  modular brute-force crosschecks, nested nonunit prime clocks, RAD births,
  chart origin shifts, homogeneous gauge, falsifying source aliases and three-shadow source-gauge counterexamples.
- Stable frozen receipt: `research/2026-10-19/PORTABLE_SUNDIAL_FINITE_RECEIPT.json`.
- Generator: `python -m scripts.portable_prime_sundial_probe`.
- Dedicated CI: `.github/workflows/portable-prime-sundial.yml`, with genuine
  GitHub `main` checkout provenance and Python 3.10/3.13 matrix.
- Kernel calibration: `formal/PortablePrimeSundial.lean` is independent of
  all frozen original EODCS sources; where added, its status becomes
  LEAN KERNEL VERIFIED only after a successful pinned Lean run.

The exact JSON probes 256 bounded integer frames × 4 prime-power windows,
for 1,024 recorded diagonal reads (306 satisfiable); two malformed
fake/invertibility controls are independently rejected.
These numbers are **finite**, not an infinity certificate.

## 10. Research targets beyond this round

**Moonshot A — a source-indexed projective rational SUCC category.**
Objects should retain the unit basis and typed original carrier; morphisms
are validated homogeneous scalings, chart shifts, and source-realized clock
refinements. Prove composition/naturality and characterize exactly which
quotient reports admit deterministic descent. Distinguish mathematical
equivalence from source-authorized access.

**Moonshot B — local-to-global phase/precision tower.** Over a growing sequence
of prime-power wheels, characterize when a compatible phase family comes from
one rational offset `alpha-beta`, from a profinite point, or from an
unjustified phantom point. Do not confuse the first-digit primorial completion
with the full factorial profinite completion. The law `delta=-D/(uv)`
lives in `Z_p` only at primes where both units are invertible.

**Moonshot C — primitive ABC slot-coupling.** Extend the dial to three
source slots constrained by `a+b=c`. Keep exact clock coincidences
`v_p(a),v_p(b),v_p(c)`, the RAD/RIS birth operators and the honest
primitive coprimality law. Investigate whether cancellation restrictions
provide **uniform** high-occupation control beyond the one-variable
moment bound. The `t<1/2` Cauchy–Schwarz result in draft PR #196 is a
separate bound; rational SUNdial fraction transitions do not produce
BBLT's exceptional-counting 3/5 exponent by numerology.

**Moonshot D — genuine source geometry and positivity.** Only after explicit
operator equality on an appropriate signed test space may one compare these
arithmetic clocks to Weil/Suzuki geometry. Never infer the completed
signed form from a nonnegative discrete kernel or the exact cancellation
divisor `D`. RH, ABC and signed `S4` remain open.

## Prior research and attribution

- Project source arithmetic: `observational_succ/rad_ris_transport.py`,
  `prime_phase_clocks.py`, `clock_factorial_duality.py`,
  `prime_clock_yoneda.py`, and `unit_prime_succ.py` on Academic Main V.
- Project source-representation firewalls:
  `formal/EODCS_CausalDescent.lean`,
  `formal/MetaChoiceRelationalDescent.lean`,
  `docs/OBSERVER_PROOF_ACCESS.md`, and Academic Main V's audit.
- Classical mathematics involved: Bézout and gcd divisibility,
  finite differences of a fractional-linear map, modular linear
  congruences, the Chinese remainder theorem and (p)-adic units.

**Attribution:** The portable-sundial analogy and source-indexed arithmetic
research direction come from the author's SUCC program. The elementary
determinant, CRT, gcd and projective formulas are classical. The typed
finite implementation and adversarial verification are new to this repo
round; publication priority is not established.
