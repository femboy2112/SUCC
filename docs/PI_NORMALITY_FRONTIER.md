# π base-16 normality — Main XXIII frontier

Maintained 2026-11-10. **π base-16 normality, original-zero hexadecimal parity
balance and parity words, and RH are OPEN.** This is the Main XXIII integration
candidate. See its [audit](SUCC_MAIN_XXIII_INTEGRATION_AUDIT_2026-11-10.md),
[tool atlas](MAIN_XXIII_TOOL_ATLAS.md), and
[Main XXII snapshot](archive/PI_NORMALITY_FRONTIER_MAIN_XXII_2026-11-09.md).

## 1. Authenticated original source

```math
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
```

```math
U_0=0,\qquad U_n=16U_{n-1}+r(n).
```

Put $`C_n=\lfloor U_n\rfloor`$, $`\kappa_n=C_n-16C_{n-1}`$ and
$`T_n=\sum_{j\ge1}16^{-j}r(n+j)`$. Then
$`U_n+T_n=16^{n-1}\pi`$. Preserve literal carries, including 16, before reducing any
coordinate. For seed $`s`$, the same forcing gives
$`U_n(s)+T_n=16^n(s+\pi/16)`$; that seed dependence is decisive.

Canonical implementations: [rational source](../observational_succ/duck_bbp.py),
[integer carrier](../observational_succ/integer_bbp_carrier.py),
[selected orbit](../observational_succ/selected_orbit.py). The critical-carry bit in
`selected_orbit` is a different observable from the integer carry above.
[Import provenance](../provenance/IMPORT_MANIFEST.json) authenticates the original imported
files; the integration manifest authenticates the research heads separately.

## 2. Strongest established tools and their authority

| Result | Status and actual content | Boundary / source |
|---|---|---|
| Green completion | PROVED PAPER; exact identity above with rigorous tail enclosures | Transport to π; no mean-decay estimate. [source contract](PI_FRONTIER_CONTRACT.md) |
| Absolute Fourier loss | PROVED PAPER under the stated classical imports; logarithmic loss from maximal reinforcement | Not sublinear signed cancellation. [selected-phase synthesis](../research/2026-10-25/PI_SELECTED_PHASE_FORGE.md) |
| #544 carry observer | PROVED PAPER; bounded continuous $`\Phi_h`$ on the integer-lift 16-adic carrier, with $`O_h(\log A/A)`$ comparison to the authentic epoch Weyl mean | Signed mean decay remains Weyl-equivalent and OPEN. [proof](../research/2026-11-08/chronology_carry/crucible/EXPLICIT_INNOVATION.md) |
| #554 balanced prime | CONDITIONAL TRANSFER with declared classical PNT/AP, exponential-sum and completion inputs; local nonzero-frequency estimate | Fixed-Gram claim needs $`p\nmid h`$. No real-complement estimate. [balanced epoch](../research/2026-11-08/three_channel_prime_tomography/BALANCED_EPOCH.md) |
| #565 recursive Haar | PROVED PAPER; sharp interval-W1 descent retaining sixteen children and the entire future tail | Its zero-seed symmetry-defect premise is OPEN; see the supplement for the precise projector |
| #571 successor junction | PROVED PAPER; signed high/low word junctions and endpoint-corrected transport inequalities | Positive finite collision energy is not a signed estimate. [proof](../research/2026-11-09/tenacious_d_haar/PROOFS.md) |
| #572 complete CRT parity | PROVED PAPER; exact prime-power/real winding factorization | Cannot omit old prime powers or the section. [proof](../research/2026-11-09/pi_parity_pressure/PROOFS.md) |
| #574 two-fiber certificate | PROVED LOCAL finite algebra; sharp error and precision constants | No asymptotic contrast estimate. [proof](../research/2026-11-09/aphex_two_fiber_haar/PROOFS.md) |
| #561 source digits | EXACT FINITE certificate: integer enclosures for a 40,960-digit prefix | A finite prefix cannot prove normality. [proof](../research/2026-11-08/lambert_entropy_forge/THEOREMS.md) |

The new analytic results are paper proofs. The four #544 Lean identities have integer-coordinate
scope; they do not formalize signed cancellation. Current execution status belongs to the
integration audit, not inherited research test counts.

## 3. Sufficient but unproved normality criteria

For $`e(x)=\exp(2\pi i x)`$, define
$`c_A(h)=A^{-1}\sum_{n=A}^{2A-1}e(hU_n)`$.
Vanishing for every fixed nonzero integer $`h`$ and all integer epochs $`A\to\infty`$
is equivalent to base-16 normality, by Weyl and the Green-tail comparison.

Earlier sufficient gates remain available: critical Fejér energy
$`C^x_{A,A}=o(\log A)`$, the fixed golden-aperture energy tending to zero,
and the joint log-stationarity/source-lattice criteria (LS) and (H2*).
The [archived frontier](archive/PI_NORMALITY_FRONTIER_MAIN_XXI_2026-11-09.md)
retains their exact hypotheses and references. None is proved for the selected zero seed.
#561's growing-word entropy premise is stronger than normality; full-conductor empirical
Haar is an impossible finite-window target. Do not substitute either for an easier theorem.

## 4. One-digit parity and the complete signed complement

Use the #572 source-clock sign $`s_n=(-1)^{\lfloor U_n+T_n\rfloor}`$.
For $`n\ge2`$ this is the parity of the $(n-1)$st fractional hexadecimal digit.
The complete CRT ledger gives

```math
s_n=(-1)^{n+\sum_m k_{m,n}+\ell_n+\varepsilon_n}=a_nb_n,
\qquad a_n=(-1)^{k_{p_A,n}}.
```

Here $`m`$ ranges over the full prime-power coordinates, $`k_{m,n}`$ are their
normalized CRT numerators, $`\ell_n`$ is the global CRT winding, and
$`\varepsilon_n`$ pays the real future-tail digit boundary. The complementary sign
$`b_n`$ retains the parity clock, all other prime powers, winding and tail.
The selected simple-pole prime is balanced at $`p_A\sim12A/5`$.

The circle observable $`f(t)=(-1)^{\lfloor16\{t\}\rfloor}`$ instead satisfies
$`f(U_n+T_n)=s_{n+1}`$. Its epoch mean differs from the source-clock mean by
$`(s_{2A}-s_A)/A`$, of magnitude at most $`2/A`$. Their limiting balance targets
agree; their finite tables require this explicit endpoint correction. This
repairs the earlier entrypoint's missing one-step index shift; PPP-02 already
stated the source-clock convention correctly.

**Digit parity is the h=8 character of the discrete digit group.** It is a step function
of a real phase, not the single real-circle character $`e(8x)`$.
Its real Fourier expansion has infinitely many frequencies; at jumps the symmetric series
converges to the midpoint. Irrational completed π phases avoid those rational jump points.

## 5. Two-fiber Haar / Aphex calibration

For the uniform epoch average, with both source-sign fibers nonempty, put
$`m_A=\mathbb E_A[a]`$, $`u_\pm(A)=\mathbb E_A[b\mid a=\pm1]`$ and
$`t_A=(u_++u_-)/2`$. Then the fitted coefficient is exactly

```math
\beta_A^*=\frac{u_+(A)-u_-(A)}2
=\frac{\mathrm{Cov}_A(a,b)}{1-m_A^2},\qquad
P_A:=\mathbb E_A[s]=\beta_A^*+m_At_A.
```

Consequently $`|P_A-\beta_A^*|\le|m_A|`$ with sharp constant 1.
At fixed exact prime labels, mean absolute complement error $`\epsilon`$ changes the
detail by at most $`\epsilon/(1-|m_A|)`$, also sharply.
[#573](../research/2026-11-09/aphex_haar_feedback/PROOFS.md) and
[#574](../research/2026-11-09/aphex_two_fiber_haar/PROOFS.md) prove the calibration;
fitting uses observed real-complement data and is retrospective.

The inherited #554 all-nonzero-frequency estimate $`\mathcal E_A`$ gives, conditionally,

```math
|m_A|\le p_A^{-1}+(2+\log p_A)\mathcal E_A=o(1).
```

Retain every hypothesis and the uniformity needed for this Fourier-l1 transfer.
**This pays the prime marginal, not the Archimedean conditional contrast.**
Conditional on that imported estimate, parity balance is equivalent to
$`\beta_A^*\to0`$. The latter is OPEN. Binary conditional Haar is distinct from #565's
full sixteen-child future-conditioned projector and from local prime Haar.

## 6. Complete-source wrong-seed controls

The irrational mathematical seed $`s_*=-\pi/16`$ gives the coherent completed orbit zero;
it preserves forcing but does not define rational p-adic coordinates. #572 supplies the
separate mandatory **rational p-integral, odd-denominator, epoch-dependent** control
$`s_A`$: source-only rational prefix construction, unchanged forcing, identical selected
p-primary history and parity clock, all real digits zero over the certified epoch.
For its populated fibers, $`b=a`$, $`u_+=1`$, $`u_-=-1`$, contrast 2,
$`\beta^*=1`$, $`P=1`$ and minimum Aphex fitting loss zero.

Any seed-blind descent, forcing-only Gamma invariant, local-prime marginal argument or
low-loss criterion must confront this control. It does not refute a genuinely zero-seed
selective theorem. [Exact construction PPP-08](../research/2026-11-09/pi_parity_pressure/PROOFS.md).

## 7. Positive pressure and failed shortcuts

| Shortcut | Falsifying receipt / boundary |
|---|---|
| Local prime Haar implies real Haar | PPP-07: even global CRT representatives have biased parity with arbitrarily uniform fixed local marginals |
| Perfect learning implies normality | PPP-08 / TFH-03: coherent same-forcing control, zero loss, parity 1 |
| Fine-scale collision growth is anti-normality | Universal $`N`$-sample floor $`E_k\ge16^k/N-1`$; #571/#572 separate floor from excess collisions |
| Pair eigenvalues determine Haar | #567 nilpotent doubly stochastic perturbation: Haar eigenvalues, nonzero pair defect |
| Gamma detects a defect, so it contracts it | #569 coercivity only compares two defects; source-only finite parts survive wrong seeds |
| Spatial 2-adic Haar implies real temporal Haar | #566 preserves spatial Haar with a non-Haar temporal word law |
| More representation accuracy proves decay | #544 and #549 compare signed statistics without bounding their common value |

The [historical frontier](archive/PI_NORMALITY_FRONTIER_MAIN_XXI_2026-11-09.md) preserves
additional carry, Galois, seed-ensemble, collision and refinement countermodels.
The [typed Gamma table](MAIN_XXII_GAMMA_OBSERVABLES.md) prevents identification of distinct
Mellin, q-Gamma, Euler–Mascheroni and 16×16 matrix objects.

## 8. Next source-selected theorem

For every fixed odd integer $`k`$, show that the literal zero-seed orbit satisfies

```math
\frac{1}{A}\sum_{n=A}^{2A-1} e(8k\,16^{n-1}\pi)\longrightarrow 0
\qquad (A\to\infty,\; A\in\mathbb N).
```

Put $`y_n=\{8\cdot16^{n-1}\pi\}`$. The limit gives half-turn symmetry
of each stationary subsequential law of $`y_n`$. This symmetry excludes
atoms on radix cuts, then flips the first parity while preserving the
complete future. Thus every fixed length-$`d`$ parity word has limiting
epoch frequency $`2^{-d}`$. The
[proof and finite Fejér boundary payment](../research/2026-11-10/main_xxiii/PARITY_BOUNDARY.md)
give the boundary step and explicit constants.

This route also has a narrower independent goal. Under the #554 prime marginal
estimate, decay of the two-fiber contrast in §5 gives one-digit parity balance.
Neither route has its source-selected signed estimate. Any proof must fail
on PPP-08 and the coherent seed $`-\pi/16`$. Finite-moment and low-residue
tests alone also admit [positive zero-seed dyadic mutants](../research/2026-11-10/main_xxiii/MELLIN_AUTHENTICATION.md).
The four-pole support and endpoint cancellation, together with three
exact Mellin values, exclude those mutants.

## 9. Causal-weld audit and Cayley source-observer follow-up

The [follow-up dossier](../research/2026-11-09/cayley_source_observer/README.md)
is based on causal-weld PR #576 at `afabc458323ef2e3a20ce2bae77239c4190819c5`.
Its [errata](../research/2026-11-09/cayley_source_observer/ERRATA.md) withdraw
capture-unsafe lambda reduction, invented omega redex addresses, finite-prefix
cofinality certification, a purported arithmetic embedding that substituted time
iteration for dilation, and unsupported sharp/uniform estimates. The revised
implementations and hostile regressions have deliberately restricted contracts;
full faithful C-monoid/source compilation remains **UNVERIFIED**.

A constructive intermediate result is now available: the
[faithful affine source-clock action](../research/2026-11-09/cayley_source_observer/AFFINE_SOURCE_ACTION.md)
on indexed rational states. Its successor is the authentic BBP step, and
its clock dilation sends n to pn while preserving the complete source seed
fiber. It satisfies the affine relation with exact source-functor naturality.
All forcing sequences admit analogous abstract conjugacies, so the source
and Archimedean observer must remain attached; the action laws imply no
selected signed cancellation.

The [Cayley proofs](../research/2026-11-09/cayley_source_observer/CAYLEY_PROOFS.md)
transport continuous circle observables to the real projective line, including
infinity. The normalized reciprocal-pi density is the classical Cauchy measure
$`dx/[\pi(1+x^2)]`$, not a source-selected cancellation law. For a source horizon
$`L\to\infty`$, time bound $`N\le L`$ and whole frequency band $`|h|\le H`$,
uniform finite-to-completed transport holds exactly when
$`H16^{N-L}/L^2\to0`$. Averaging the epoch $`A\le n<2A`$ at a **common** horizon
$`L=2A`$ is more forgiving: a clipped geometric bound tends to zero whenever
$`\log(1+H_A)=o(A)`$. The finite signed mean itself still needs an estimate.

The [boundary proofs](../research/2026-11-09/cayley_source_observer/BOUNDARY_PROOFS.md)
pay source precision, Fejer truncation, arithmetic evaluation and digit-boundary
mass separately. They also isolate a sufficient **binary future fairness** gate:

```math
\forall k\in2\mathbb Z+1,\qquad
\frac1A\sum_{n=A}^{2A-1}e\!\left(8k(U_n+T_n)\right)\longrightarrow0.
```

For consecutive orbit laws, their stationary weak limits then have half-turn
symmetry after folding by eight. This forces vanishing shrinking-boundary mass
and fair frequencies for every fixed parity word. It is strictly weaker than
hexadecimal normality: the invariant law with independent fair digits 0 and 1
satisfies the gate and is not Haar. It is stronger than fair parity words alone;
a dependent digit countermodel proves the distinction. This is a **conditional
paper theorem**, and the displayed hypothesis is **OPEN for the original zero
seed**. It is another sufficient route, not a necessary condition for one-digit
parity balance or a replacement for the less demanding contrast target in §5.

The new real half-turn contrast and the prime-conditioned complement in §5 are
different objects. Their [source map and next obligation](../research/2026-11-09/cayley_source_observer/NEXT.md)
retain that distinction and the coherent wrong-seed controls. The exact finite
certificates validate the observer and its budgets; they supply no asymptotic
signed saving.

## 10. Source-first clocks and reversible readout

The [inverse-beta BBP root](../research/2026-11-10/omega_bbp_operational_completion/INVERSE_BETA_BBP_ROOT.md)
folds the actual four-pole source, selects the bounded arithmetic solution,
and intertwines it with a continuous Mellin fixed point. The finite moment
observer is non-identifying in the unrestricted positive source class.
The [six-step diamond](../research/2026-11-10/omega_bbp_operational_completion/OMEGA_HAAR_WAVELET.md)
identifies two exact chronological groupings. Inserting lossy two- and
three-cell averages creates the noncommuting Haar projections and their
rank-two oscillator. The inverse-fiber parity character lives in the
Möbius line bundle. These operations leave the signed zero-seed bound open.

The [quantum dagger model](../research/2026-11-10/omega_bbp_operational_completion/quantum_bridge/README.md)
supplies finite unitary and phase precision results. A separate
[reversible BBP circuit](../research/2026-11-10/main_xxiii/REVERSIBLE_BBP_ORACLE.md)
implements exact finite classical-basis arithmetic, with explicit register
widths, gate counts and inverse checks. A typed source-to-lambda compiler
and a scalable quantum phase implementation remain unverified.

## 11. Independent RH program

The [intrinsic arithmetic Hamiltonians](../research/2026-11-10/omega_bbp_operational_completion/intrinsic_carrier/PROOFS.md)
give self-adjoint star blocks on the positive-integer carrier. The
[prime field endpoint audit](../research/2026-11-10/main_xxiii/HAMILTONIAN_ENDPOINT.md)
addresses operator domains. The Gibbs generator $`H_0\lvert n\rangle=\log(n)\lvert n\rangle`$
is a different operator. The signed completed Weil identification is open.

[#550](../research/2026-11-08/xi_cayley_prime_pinbed/PROOFS.md) retains the genuine
Euler/Gamma source, horodisk of convergence and conditional Jensen certificate.
[#553](../research/2026-11-08/theta_extruded_interference/PROOFS.md) retains completed
theta/Gamma moment identities and the unresolved signed Li/Weil positivity seam.
Finite Schur positivity, positive Fourier kernels and Pascal moment inequalities do not
prove completed Weil positivity. Positive Pascal fake sources can have off-critical roots.
No nontrivial zero locations are construction inputs. **RH remains OPEN** and is not a
step in the π proof chain. See [RH handoff](RH_HANDOFF.md).

[Research history and primary dossiers](RESEARCH_HISTORY.md) ·
[Main XXI audit](SUCC_MAIN_XXI_INTEGRATION_AUDIT_2026-11-07.md) ·
[Main XXII audit](SUCC_MAIN_XXII_INTEGRATION_AUDIT_2026-11-09.md)
