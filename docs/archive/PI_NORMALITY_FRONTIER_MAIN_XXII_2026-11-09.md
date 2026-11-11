# π base-16 normality — Main XXII frontier

Maintained 2026-11-09. **π base-16 normality: OPEN. Original-zero hexadecimal parity
balance: OPEN. Riemann hypothesis: OPEN.** This page replaces the previous entrypoint;
its [Main XXI version](archive/PI_NORMALITY_FRONTIER_MAIN_XXI_2026-11-09.md) and every
primary dossier remain historical evidence. See the [integration audit](SUCC_MAIN_XXII_INTEGRATION_AUDIT_2026-11-09.md)
and [claim supplement](CLAIM_SUPPLEMENT_MAIN_XXII.md) for review boundaries.

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

Let $`s_n=(-1)^{d_n}`$ for the completed real hexadecimal digit
$`d_n=\lfloor16\{U_n+T_n\}\rfloor`$. The #572 complete CRT ledger gives

```math
s_n=(-1)^{n+\sum_m k_{m,n}+\ell_n+\varepsilon_n}=a_nb_n,
\qquad a_n=(-1)^{k_{p_A,n}}.
```

Here $`m`$ ranges over the full prime-power coordinates, $`k_{m,n}`$ are their
normalized CRT numerators, $`\ell_n`$ is the global CRT winding, and
$`\varepsilon_n`$ pays the real future-tail digit boundary. The complementary sign
$`b_n`$ retains the parity clock, all other prime powers, winding and tail.
The selected simple-pole prime is balanced at $`p_A\sim12A/5`$.

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

Prove, for the **literal original zero seed** and all sufficiently large integer epochs,
$`u_+(A)-u_-(A)\to0`$, retaining all prime powers, global winding, the original forcing,
and real-tail boundary payments. A proof needs an input that rejects PPP-08's p-integral
control, whose contrast is exactly 2. No finite fitted covariance can pay this quantifier.
This would establish hexadecimal **parity balance only**, strictly weaker than full normality.

The [next-round protocol](MAIN_XXII_NEXT_ROUND.md) fixes a fresh experiment and the exact
proof obligation. Other digit characters and future word depths follow only after a
defensible parity advance. More equivalent Fourier identities do not change this verdict.

## 9. Independent RH program

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
