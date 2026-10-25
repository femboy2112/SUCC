# The SUCC π Gearbox Atlas

*Coherent Main X (2026-10-24). A map of how the 2026-10-24 π-frontier branches
mesh on one authenticated source — and the exact gear that is still missing.*

This Atlas is navigational. Every box is a mathematical object or map that lives
in the repository; every arrow is a transport with a **status label**; and the
whole point of the map is to show precisely where a *proved* square stops and an
*open* statistical estimate begins. Nothing here claims π normality. π normality,
its logical independence, RH, and absolute/decimal normality all remain **OPEN**.

Status labels used throughout:

- **EXACT** — proved by exact integer/rational algebra (and machine-checked by a
  finite test over a stated range).
- **FINITE** — a finite numerical certificate only; *not* a proof of any
  asymptotic or universal statement.
- **CONDITIONAL** — a classical implication (e.g. van der Corput, Weyl) whose
  hypothesis is an as-yet-unproved source estimate.
- **OPEN** — the missing theorem.

---

## 0. The one source

Everything turns on a single external clock and a single internal program.

$$(\mathbb{N},0,S),\qquad S(n)=n+1.$$

$$U_0=0,\qquad U_{n+1}=16\,U_n+r(n+1),\qquad
r(n)=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)}.$$

Equivalently $r(n)=\dfrac{4}{8n-7}-\dfrac{2}{8n-4}-\dfrac{1}{8n-3}-\dfrac{1}{8n-2}$,
and $\alpha=\pi/16=\lim_{n\to\infty}U_n/16^{n}$. The denominator is always odd;
$U_n$ is an exact rational with odd denominator — the integer **lift** that every
observer quotient below throws away some of.

**Do not alter** the source law, the time indexing, the initial state $U_0=0$, the
exact integer lift, or the source-specific sign information. These are the shafts
the gears turn on.

---

## 1. One source, two carriers (the hub)

| Box | Module | Representation of $U_n$ |
|---|---|---|
| $\mathbb{N}$-successor carrier (#281) | `bbp_natural_carrier.py` | state $(n,a,t)$, $U_n=a/(2t+1)$, product denominator, unreduced |
| integer odd-conductor carrier (#282) | `integer_bbp_carrier.py` | state $(n,Q,N)$, $U_n=N/Q$, with $Q$ the lcm of the reduced forcing denominators |

**Commuting square (EXACT).** Both carriers run the *same* recurrence from the
*same* initial state, so for every $n$ their unwrapped rationals coincide:

$$\frac{a_n}{2t_n+1}\;=\;\frac{N_n}{Q_n}\;=\;U_n.$$

Machine-checked for $n=0,\dots,59$ in
`tests/test_gearbox_source_integration.py::SingleSourceTwoCarriers`. The two
reduced forcing representations agree as exact rationals and keep the denominator
odd. This is the reconciliation the integration demanded: the two integer hosts
are two charts of **one** source, not two sources.

---

## 2. Observer quotients (the gear train)

Each observer is a **declared map out of the source**, not a free-standing
distribution. The repeated discipline: `observe ∘ step = local_step ∘ observe`
(the observer factors through the one clock). Where that square is proved it is
proved *exactly*; where only a finite table exists it is labelled FINITE.

| Observer | Module(s) | Square proved | Label |
|---|---|---|---|
| dyadic 2-adic view $U_n \bmod 2^k$ | `bbp_natural_carrier`, `bbp_two_adic` | `dyadic_observer_step` commutes with the machine; cross-carrier reduction identical | **EXACT** |
| real-circle phase $\{16^{n-1}\pi\}$ and certified hex digit | both carriers | certified digit matches an **independent Machin oracle** (π and π/16) | **EXACT / FINITE** |
| odd-prime CRT phases ($p\ge7$: four pole classes/depth) | `pi_joint_prime_carrier` | local Haar character $1-4p^{-(v_p(h)+1)}-4p^{-(v_p(h)+2)}$; CRT independence over full periods; $p=3,5$ Hensel exceptions | **EXACT** |
| Pascal source differences / weighted charts | `pi_pascal_source`, `pascal_rank_process` | dyadic refinement $P_{k+4}\le P_k/16+15N/16$; signed Pascal differences | **EXACT (own domain)** |
| Lucas-support quotient | `pascal_lucas_quotient` | Boolean-incidence/binomial rank quotient; ordered carry retained | **EXACT** |
| four-bit Walsh gates | `pascal_carry_interferometry` | 16-cell Walsh inversion $16Z-Q_0=\sum_{A\ne\varnothing}M_A$ | **EXACT** |
| twisted-pair Galois | `bbp_twisted_pair` | relative Galois differential; contragredient orientation; source-anchor decoder | **EXACT** |
| harmonic mirror $x\mapsto x/(1+x)$ | `harmonic_mirror_succ`, `pi_harmonic_lag` | four $J^{8}$ reciprocal rays; harmonic cocycle; positive Fejér lag bound (budget $88/1575$) | **EXACT / CONDITIONAL** |
| Euler–Mascheroni boundary / adelic flux | `euler_mascheroni_succ`, `euler_bbp_regulator`, `generalized_euler_adelic` | exact finite cutoff, regulator tail, two-domain projection/flux identity | **EXACT** |

The cross-carrier and dyadic/real-circle squares in the first two rows are the
ones machine-checked in the new integration suite. The rest are proved in their
own branch suites (632 focused tests green on the combined tree) and are exact
*in their stated domain*.

---

## 3. The missing gear (where every square stops)

Here is the entire point of the map. Lay the proved squares end to end and ask
what they deliver about the digits of π. The honest answer:

> Every proved transport above is either **exact finite algebra**, a **finite
> certificate**, or a **conditional criterion** whose hypothesis is a statement
> about the *selected signed* source sum. Not one of them discharges that
> hypothesis.

Concretely, normality of the base-16 expansion needs, for each fixed nonzero
integer $h$, cancellation of a **source-selected signed exponential sum** driven
by the authentic $U_n$ (equivalently the complementary source $w_t$), with a
power saving over the trivial bound. The gears transmit force perfectly *on their
own shafts*:

- the dyadic refinement contracts, **but in its own 2-adic metric** — it is not a
  statement about real-circle $1/16$ digit frequencies;
- the Pascal/Lucas $1/16$ overlap is a combinatorial support, **not** a BBP digit
  frequency;
- the positive harmonic Fejér mixture gives an exact lag bound, **but** the naive
  signed $1/k$ kernel is already negative at angle $\pi$ for $K=4$ — positivity
  alone does not supply the selected cancellation;
- the joint-prime completion has the noncommuting-limit boundary
  $\lim_{\text{prime}}\lim_{\text{time}}=1\ne 0=\lim_{\text{time}}\lim_{\text{prime}}$
  (EXACT) — i.e. independent prime-observer averaging is a proven *failure* mode,
  not a proof of cancellation of the authentic history $U_n$;
- observer *completeness* (all 16 factorial cells) is **not** a proof of uniform
  statistics — the hostile holdouts in #283 show full combination without stable
  improvement.

The missing gear is a single asymptotic estimate on the selected signed temporal
distribution. It has four candidate shapes, written out with quantifiers and the
exact logical debt each would discharge, in the companion
[π Frontier Contract](PI_FRONTIER_CONTRACT.md).

---

## 4. What is *not* on this map (kept separate on purpose)

- **RH / Gamma / Tate / Weil.** The Euler–Mascheroni/Li/completed-boundary work
  (#285–#287) reuses the boundary accounting but is a **separate** frontier: no
  finite Γ-jet authenticates ζ, no finite Li bound proves all-degree Li
  positivity, no positive graph/Hilbert kernel identifies the signed Weil form.
  See the RH handoff; RH remains **OPEN**.
- **Alternative bases.** Base-3 measure rigidity and the rational-base $11/10$
  algebra are preserved as *separate* research; no cross-base normality transfer
  is assumed, and primes below 16 are not assumed to suffice.
- **Lean authority.** None of the 2026-10-24 π families add Lean kernel authority;
  the finite certificates are finite certificates.

---

## 5. How to read the code from here

Start at the hub (`bbp_natural_carrier.py` / `integer_bbp_carrier.py`), confirm
the one-source square with `tests/test_gearbox_source_integration.py`, then walk
out along any observer row above into its module and its branch supplement. The
claim identities for each observer family are in
`docs/CLAIM_NAMESPACE_REGISTRY.json` (56 namespaces; dotted FQIDs disambiguate the
six registered bare-prefix collisions). The precise open estimate you are trying
to close is in the [π Frontier Contract](PI_FRONTIER_CONTRACT.md).
