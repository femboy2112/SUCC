# Seed-Resonance Interferometry and the Differential Null Fiber

**SUCC / Principia Observatoris / BBP Endpoint Coercivity — 2026-11-17**

**Originating hypothesis:** the literal zero seed may conceal observer-relative carrier distinctions; injecting a nonzero seed supplies hidden information that resonates with the difference between source and shifted orbit. This may scramble, attenuate or even cancel an observer’s apparent phase. **Status:** SR-01–09 are elementary/classical exact identities or no-go results in declared source/observer models; SR-10 is a source-selected research contract, **OPEN**. Neither R0 nor base-16 normality of π has been proved.

## 1. Source-translation family; endpoint is not provenance

Retain the four authenticated BBP poles and literal zero seed:

\[
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),\quad
U_0(0)=0,\quad U_{n+1}(0)=16U_n(0)+r(n+1).
\]

With \(x=\pi/16\), the exact original completion is \(Y_n=U_n(0)+T_n=16^nx\), where \(T_{n+1}=16T_n-r(n+1)\). For a **counterfactual** seed \(s\), use the unchanged forcing but \(U_0(s)=s\).

**SR-01 — affine seed transport (EXACT):**

\[
\boxed{U_n(s)=U_n(0)+16^ns,\qquad Y_n(s)=16^n(x+s).}\tag{SR1}
\]

Thus any requested real or irrational endpoint \(y\) can be represented by the *unique* seed \(s=y-x\). This seed explicitly contains the information selecting that endpoint and is not automatically an authenticated original-zero path. The specially chosen \(s=-x\) locks at zero; \(s=q-x\) with rational \(q\) gives an eventually periodic rational orbit. Nonzero seeds **do not generically lock**: every \(s=a/16^m\), with nonzero integer \(a\), gives the *exact same circle phases as the zero seed for all n≥m*.

## 2. Seed resonance and signed contamination

Let \(e(t)=e^{2\pi it}\), \(z_n(s)=e(Y_n(s))\). The relative seed character is

\[
\boxed{\chi_n(s)=z_n(s)/z_n(0)=e(16^ns),\quad
\chi_{n+1}(s)=\chi_n(s)^{16}.}\tag{SR2}
\]

In particular \(z_n(s)/z_n(t)=e(16^n(s-t))\): **every purely relative comparison between two equal-forcing completed copies forgets all four source poles and the original endpoint**. Causal transport alone cannot recover the data it has canceled.

The exact shell response is

\[
\boxed{W_B(x+s)-W_B(x)
=\frac1B\sum_{n=B}^{2B-1}z_n(0)\,[\chi_n(s)-1],}\tag{SR3}
\]
\[
\boxed{|W_B(x+s)-W_B(x)|
\le\frac2B\sum_{n=B}^{2B-1}|\sin(\pi16^ns)|.}\tag{SR4}
\]

**SR-02 — exact kernel (EXACT):** the seed-invisible set for every circle sample in shell \(B\le n<2B\) is precisely \(K_B=16^{-B}\mathbb Z/\mathbb Z\). The union of these sets is dense in the circle. At the same time, \(\partial_s\chi_n(0)=2\pi i16^n\): a large infinitesimal response is entirely compatible with a finite exact wrap returning the sampled phase to one.

### Where the added Gamma observer sees two kinds of resonance

The *additional* adaptive Gamma continuum observer from the prior dossier has \(q(y)=(1-2\pi iy)^{-1}\), \(c(y)=q(y)-q(y/16)^{16}\), \(M_n(y)=q(y)e(16^ny)\), and \(D_{n-1}(y)=c(y)e(16^ny)\). The source-dependent amplitude is part of the instrument; it must not be held fixed when the seed changes.

\[
\boxed{M_n(x+s)-M_n(x)
=z_n(0)[q(x+s)\chi_n(s)-q(x)],}\tag{SR5}
\]
\[
\boxed{D_{n-1}(x+s)-D_{n-1}(x)
=z_n(0)[c(x+s)\chi_n(s)-c(x)].}\tag{SR6}
\]

The **exact first-order susceptibility** separates radial transport from instrument gain:

\[
\boxed{\left.\partial_s D_{n-1}(x+s)\right|_{s=0}
=2\pi i\,z_n(0)\big[16^nc(x)+q(x)^2-q(x/16)^{17}\big].}\tag{SR7}
\]

A dyadic seed \(s=a/16^m\) is completely invisible in *integer-time* circle measurements for n≥m, yet \(q(x+s)\ne q(x)\) for s≠0; the newly declared fractional-time Gamma readout detects the **real lift**. This is a stronger instrument, **not information secretly present in the original discrete BBP orbit**. At \(s=-x\), the Gamma defect coefficient is \(c(0)=0\), displaying the tuned lock.

## 3. The mathematical meaning of a zero-looking update

Literal \(0J=0\) in an ordinary algebra. A nonzero *projected-null* carrier update instead satisfies \(P(h)=0\) with \(h\ne0\). A complementary algebraic representation is the complex dual-number ring \(\mathbb C[\varepsilon]/(\varepsilon^2)\): the seed \(s=\varepsilon v\) has zero ordinary base value but a nonzero first jet,

\[
\boxed{e(16^n\varepsilon v)=1+2\pi i16^n\varepsilon v.}\tag{SR8}
\]

**SR-03 (EXACT formal jet):** the base evaluation \(\varepsilon\mapsto0\) erases the tangent; a higher-resolution tangent probe reveals it. This is an illustrative *mathematical* realization of observer-relative zero, not a nontrivial literal multiplication by zero or a physical infinitesimal.

Keep distinct: literal source zero; hidden state in \(\ker P\); finite-shell seed alias; expectation zero under a declared probability distribution; and two causally different histories that induce identical accessible future states. An analytic germ with all derivatives zero at a point is locally zero; no all-orders hidden analytic signal is inferred without a non-injective projection.

## 4. Haar seed noise, 17-factor causal resonance, and a strong no-go

Introduce a **counterfactual random seed** \(S\sim\mathrm{Haar}(\mathbb R/\mathbb Z)\), independent of fixed source \(x\). Put \(A_n=e(16^nS)\), \(Z_n=e(16^n(x+S))\). Character orthogonality on the circle yields, for integers \(k_j\),

\[
\boxed{\mathbb E_S\prod_j A_{n_j}^{k_j}
=\mathbf1_{\{\sum_jk_j16^{n_j}=0\}}.}\tag{SR9}
\]

So the individual and two-time moments appear noise-like:

\[
\boxed{\mathbb E_SZ_n=0,\quad
\mathbb E_S(Z_n\overline Z_m)=\mathbf1_{\{n=m\}},\quad
\mathbb E_S(Z_n^{16}\overline Z_{n+1})=1.}\tag{SR10}
\]

**SR-04 (CLASSICAL/EXACT):** ordinary first means and off-diagonal two-time correlations vanish, while a **17-factor adjacent-clock resonance** is identically one. A nontrivial two-clock character relation \(k16^n+\ell16^{n+1}=0\) has minimal nonzero degree \(|k|+|\ell|=17\). The original process is not actually independent: \(Z_{n+1}=Z_n^{16}\) deterministically. If the observer is permitted to lift its features to \(Z_n^{16}\), the relation becomes a second-order correlation in that *enlarged observable algebra*. Observation order is toolkit-relative.

For the randomized-seed Weyl shell,

\[
\boxed{\mathbb E_SW_B(x+S)=0,\qquad
\mathbb E_S|W_B(x+S)|^2=1/B.}\tag{SR11}
\]

**SR-05 (STRONG NO-GO):** since \(x+S\) is exactly Haar-uniform **regardless of x**, the probability distribution of the *entire infinite shifted orbit* is independent of the original source x. No statistic of these unlabelled masks alone, at any correlation order, can identify which x generated it. The 17-factor resonance authenticates the radix transition, **not the literal zero seed**. The Haar expectation (SR11) is not a bound for the fixed point S=0; it cannot be substituted into the π normality problem.

More generally, a predeclared probability distribution \(\mu\) over seeds supplies a frequency transfer function \(\widehat\mu(k)=\int e(ks)d\mu(s)\):

\[
\mathbb E_\mu Z_n=z_n(0)\widehat\mu(16^n),\quad
\mathbb E_\mu(Z_n\overline Z_m)
=z_n(0)\overline{z_m(0)}\,\widehat\mu(16^n-16^m).\tag{SR12}
\]

This identifies precisely when **seed uncertainty**, rather than source statistics, nulls or contaminates an observation. A finite uniform mask on \(\mathbb Z/16^M\mathbb Z\) reproduces the Fourier orthogonality on clocks n<M but aliases all clocks n≥M. It is a finite calibration, not an identification of random masks with the deterministic BBP trajectory.

## 5. Higher-order source memory can still be seed-blind

Define the original-source calibrated channel \(C_n(s)=e(-U_n(0))Z_n=e(T_n+16^ns)\). The forcing survives in a signed higher-order comparison:

\[
\boxed{C_{n+1}(s)\,\overline{C_n(s)}^{16}=e(-r(n+1)).}\tag{SR13}
\]

**SR-06 (SOURCE-EXACT):** this corrects the universal raw orbit identity \(Z_{n+1}\overline Z_n^{16}=1\) by retaining the actual BBP source forcing. Yet (SR13) holds for *every* seed s—including \(s=-x\). It can certify the forcing law but **cannot certify the initial condition**. Our next instrument must transport source and literal zero-seed provenance together.

### Distinct causal histories with the same entire future

Pick a clock k≥1 and insert a one-time real impulse a at that update, with initial seed zero:

\[
\widetilde U_0=0,\qquad
\widetilde U_n=16\widetilde U_{n-1}+r(n)+a\mathbf1_{\{n=k\}}.
\]

Compare to unchanged forcing and initial seed \(s=a/16^k\). Then

\[
\boxed{\widetilde U_n=U_n(0)\ (n<k),\qquad
\widetilde U_n=U_n(a/16^k)\ (n\ge k).}\tag{SR14}
\]

**SR-07 (CLASSICAL CAUSAL-PROVENANCE NO-GO):** no deterministic observer restricted to the **full real states from k onward**, no matter how elaborate its future higher-order probes, can determine which of these two causal histories occurred. Historical states or the authenticated forcing/initial-seed passport separate them. The impulse is an adversarial *changed-source* model, not a claim about the original four-pole forcing.

## 6. The dense null subgroup creates a discontinuous observation wall

Let \(G=\bigcup_{m\ge0}16^{-m}\mathbb Z/\mathbb Z\). It is dense in the circle, and every \(g\in G\) alters only finitely many radix-16 circle samples. Therefore eventual-shell predicates such as R0 are invariant under shifts by G.

**SR-08 (PROVED PAPER; dense-invariance lemma):** every nonconstant real-valued function invariant under a dense subgroup G of circle translations is *nowhere continuous*. Proof: if f were continuous at y, for arbitrary x choose g_j∈G with x+g_j→y. Then f(x)=f(x+g_j)→f(y), forcing f to be constant. The R0 indicator is nonconstant: it fails at x=0 and holds at x=1/15, whose radix-16 orbit is a fixed nonunit phase. Thus the R0 indicator is nowhere continuous with respect to ordinary endpoint distance.

This is a rigorous moving-horizon limitation on continuous endpoint-only classifiers, not an undecidability theorem for the source-authenticated π problem. A source-aware arithmetic proof might decide the specific x despite this topological obstruction.

## 7. The open original-zero arithmetic problem remains

The original source terminal norm

\[
\boxed{\mathcal R_B(0)=\frac1B\sum_{j=1}^B
\left\|\frac{U_{2B}(0)}{16^j}\right\|_{\mathbb T}^2,\quad
\liminf_{B\to\infty}\mathcal R_B(0)>0\iff\mathrm{R0}}\tag{SR15}
\]

is inherited from [Endpoint Coercivity](../../2026-11-16/defect_window_tomography/ENDPOINT_COERCIVITY_REPORT.md). The pointwise weaker floor \(\mathcal R_B(0)\ge1/(16711680B^5)\) is another **OPEN** source-specific arithmetic premise, not achieved by Haar averaging or a relative-only seed response.

**SR-09 — REFUTED inference:** the source-independent character (SR2), the seed ensemble moments (SR9–11), and the seed-independent forced cocycle (SR13) all survive the locked counterseed. Their existence cannot alone imply π escape from locking.

**SR-10 — next verdict-changing probe (OPEN):** construct an **asymmetric** arithmetic correlation retaining the literal seed \(U_0=0\), the selected integer winding, four poles and odd-denominator/cofactor chronology, and a source-passport-aware clock comparison. Predeclare its signed prediction on a withheld source window and a nontrivial all-late-shell estimate relating it to \(\mathcal R_B(0)\). Kill it first with \(s=-x\), finite dyadic aliases, the per-shell winding erasure construction, sparse irrational controls and the pre-/post-k causal impulse rival. Never promote statistical noise of a randomized seed to statistics of deterministic π digits.

### Claim ledger and provenance

| ID | Status | What survives |
|---|---|---|
| SR-01–02 | **PROVED PAPER** | Source-affine seed torsor, dyadic nulls, Fourier/Gamma resonance and signed contamination |
| SR-03 | **PROVED PAPER / formal algebra** | Dual-number zero-base/nonzero-tangent separation |
| SR-04 | **CLASSICAL/PROVED PAPER** | Haar null low moments, deterministic 17-factor resonance and mean-square 1/B |
| SR-05 | **NO-GO / EXACT** | The entire Haar-shifted process loses the original source label |
| SR-06 | **SOURCE-EXACT** | Original forcing in corrected high-order cocycle, but no seed selector |
| SR-07 | **HOSTILE EXACT** | Original seed shift versus later impulse, indistinguishable after k |
| SR-08 | **CLASSICAL/PROVED PAPER** | Dense tail aliases force the nonconstant R0 indicator nowhere continuous |
| SR-09 | **REFUTED** | Generic seeded resonance or virtual zero ambiguity does not force R0 |
| SR-10 | **UNVERIFIED / OPEN** | Source-selected signed winding estimate, R0 and π normality |

**Linked SUCC sources:** [Causal clock synchronization](CAUSAL_CLOCK_SYNCHRONIZATION.md), [Moving-frame chart](../../2026-11-16/defect_window_tomography/MOVING_FRAME_THIRD_LAW_INTERFEROMETRY.md), [Gamma microscope](../../2026-11-16/defect_window_tomography/ADAPTIVE_GAMMA_ICE_CLIMB.md), [Source-aware higher-order boundary](../../2026-11-16/defect_window_tomography/MOVABLE_BOUNDARY_ORDER_LIFT.md), [Original source phase](../../../docs/MAIN_XXVI_SOURCE_PHASE_INTERFACE.md), [Principia observation quotient](../../../docs/principia_observatoris/02_causality_geometry.md). Shared forcing provenance is not blind independent source confirmation.

**External classical checks:** [Warwick Tate's Thesis notes — Haar character orthogonality](https://warwick.ac.uk/fac/sci/maths/people/staff/sheth/tate/tateweek4.pdf); [Walkden Ergodic Theory — radix shift](https://personalpages.manchester.ac.uk/staff/charles.walkden/ergodic-theory/ergodic_theory.pdf).

**Focused validation:** [tests/test_seed_resonance.py](../../../tests/test_seed_resonance.py) includes exact rational finite-group moment and source-history controls. [Validation receipt](SEED_RESONANCE_VALIDATION.md) records the executed run, source-gain derivative check, limits and deliberately unrun root gates.
