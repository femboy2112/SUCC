# SUCC x Suzuki finite-interval Weil form: the finite->global program

**RH PROVED: no.**

Provenance: branch research/suzuki-weil-finite-to-global-2026-10-13, based on the dsv4 fifth-wave substrate (/home/leah/succ_lab/SUZUKI_BLAST), branch dated 2026-10-13; blast executed 2026-10-14. Four bearings (A positivity, B spectral, C normalization/firewall, D Nyman-Beurling), each adversarially re-derived by an independent crucible. Only crucible-survived findings are kept. Finding C5 is dropped (see section 8).

Labels: Disclosed / Corroborated / Observed / Conjectured / Refuted. Most numbers below are mpmath at 25-60 digits, not interval arithmetic, so they are Observed or Corroborated and are not AGENTS.md section 8 certificates. The exceptions are exact Fraction/sympy results, marked as such.

## 1. Overview and the verified Suzuki boundary

Source: Suzuki, arXiv:2606.09096 v3, "Weil's quadratic form via the screw function".

- Thm 1.3 (proved, no RH): lambda_a is continuous in a>0.
- Corollary (Yoshida): RH <=> Q_W^a is nondegenerate for every a>0.
- Thm 1.5 (proved): the zeros of W(a,theta;z) are all real.
- Cor 1.6 / eq 1.12: conjectural. Suzuki himself says it "does not appear to provide a simple route".

Net result of this program, in four sentences:

1. The finite-interval layer is a zero-free construction.
2. The finite-to-global passage is not a topology problem.
3. Everything with RH content sits in two places: the quantifier "for all a", and the eq 1.12 limit target, which is xi itself.
4. SUCC's source-indexed finite machinery reproduces the Nyman-Beurling wall and does not go around it.

**Correction to the repo boundary note** (SUZUKI_2606_09096_FRONTIER.md line 10, "kernel built from the zeros, not zero-independent"). This is true of the explicit-formula representation k(t)=sum e^{-i gamma t}=-g''. It is false of the construction. Eq (1.3) defines g from primes (n<=e^{|t|}), pole terms and digamma/Lerch Gamma terms, with no zero position. The zeros enter only through (a) the representation, (b) the eq 1.12 target xi/(xi+xi'), and (c) the section 7 de Branges machinery, which assumes RH. [C1, Disclosed; A7, Disclosed]

## 2. Route A: positivity and the compression topology (nodes P03/P05/P06/P07)

**T1 (window exhaustion, Disclosed, with Weil's criterion as cited input).** Let Q be ONE a-independent Hermitian form on D=Cc^inf(R) and V_a=Cc^inf(-a,a). Define lambda_a=inf over V_a of Q(v)/||v||^2, which is Suzuki's lowest eigenvalue by his Cor 1.2. The hypotheses are:
- (H1) V_a is contained in V_b for a<b;
- (H2) Q^a is Q restricted to V_a, with the same Q for every a;
- (H3) the union of the V_a equals D, by exact compact-support containment.

Then the following are equivalent:
- lambda_a>=0 for all a;
- lim lambda_a>=0;
- Q>=0 on Cc^inf(R);
- RH (Weil).

The proof uses no boundedness, no strong density and no limit. The screw/bounded-operator form is G_a=P_a G P_a on L2_0(-a,a). RH <=> G_a>=0 for all a, and the tower G_a=P_a G_b P_a is an exact compression tower. The B-02 strong-density machinery is overkill here. T1 is Weil+Yoshida restated and adds no RH information. [A1]

**Lemma M (monotonicity and inertia, Disclosed).**
- lambda_a is non-increasing in a. With Thm 1.3 and Thm 1.4 (lambda_a -> +inf as a->0+), define a_*=sup{a: lambda_a>0}. Then RH <=> a_*=inf.
- If RH fails, then lambda_{a_*}=0 with a nonzero null vector, and lambda_a<=0 for all a>=a_*.
- The inertia n_-(a) is a finite, non-decreasing integer.
- Continuity of lambda_k for k>=2 is not proved by Suzuki and is not used. [A2]

**Thm 1.3 gives no uniformity (Disclosed).** Continuity only upgrades Weil's criterion to nondegeneracy, because a failure must pass through an exact zero. It gives no lower bound on a_* and no extrapolation from a window (0,a0] to larger a. [A3]

**Exact countermodels showing which hypotheses are load-bearing** (negative controls, no RH content):
- CM1 (Disclosed, exact Fractions/sympy). Take A_M=I-2|1_[M,M+1]><1_[M,M+1]| on nested L2(-a,a). Then lambda_a^(M)=1-2*clip(a-M,0,1). It is continuous, non-increasing and positive for a<M+1/2, crosses 0 at a=M+1/2, and equals -1 for a>=M+1. For fixed a0 and M>a0 the compression equals that of I, and A_M -> I strongly. Verified: closed form vs sympy exact eigenvalue at all 15 grid points (M=2, m=3); world table for M=1,5,25; lambda_{7/2}^(M)=1 for M=4..60. [A4]
- CM2 (Disclosed, sympy exact). On L2(0,inf) with exhaustion Cc^inf(0,a) (L2-dense), take q_R=int|u'|^2-alpha|u(0)|^2. It equals q_D on H^1_0, so every compression is PSD, yet u=e^{-alpha x} has Rayleigh quotient -alpha^2. The right topology is form-norm density, not L2 density. The Robin-pathology-defused reading for the Weil form is only Observed/Conjectured. [A5]
- Shift-manufactured positivity (Disclosed). T_a=A_a-lambda is positive for any lambda<lambda_a whether or not RH holds, and Thm 1.5 uses only finitely many primes. So real-rootedness of W at finite a is source-blind. [A10]

**Direction of finite evidence (Disclosed).** Finite Gram matrices give only upper bounds on lambda_a (Rayleigh-Ritz; exact CM3 check: Ritz minima 3.0, -0.236068, -0.236068 are all >= the true minimum -0.236068). A finite PSD Gram cannot certify lambda_a>=0 even at one a. A finite non-PSD Gram, with interval arithmetic and sampled-test density, refutes RH. So not-RH is a Sigma_1 event and RH is Pi_1. A rigorous single-a lower bound needs a Temple/Weinstein complement estimate with a certified gap, which is a new obligation not yet built. [A6]

**Source sensitivity of finite screw-Gram (Observed, mpmath 30 dps, not interval).** The 8-point matrix K_ij=g(x_i-x_j)-g(x_i)-g(x_j)+g(0) at points {+-(A/4)k, k=1..4} has these minimum eigenvalues:

| Source | A=1 | A=2 | A=3 |
|---|---|---|---|
| true g | 0.0266489 | 0.0270045 | 0.0236721 |
| primes only (prime powers dropped) | -0.145647 | -2.74783 | -6.4206 |
| fake composite impulse at 6 | -0.102052 | -2.96429 | -6.50034 |
| Lambda->log n for all n | -0.370501 | -21.5095 | -179.354 |
| Gamma linear term removed | -0.0393805 | -0.0078849 | +0.076309 (undetected at A=3) |
| Gamma linear term sign-flipped | positive | positive | positive (not detected) |

Detection is one-sided: mutants that add positive screw mass pass PSD checks undetected. So the identification of a SUCC object with Q_W must be proved, not tested (section 6 firewall). [A9]

**Transcription audit (Observed).**
- g(0)=0, A=(log 2pi+gamma-1)/2=0.70754636565544..., and the small-t remainder tends to -7/8.
- Q_W(v)=W(v*~v) agrees with -int g f'' to ~1e-13 on three Gaussians (the bearing-A run; not re-run to completion by the crucible).
- This is an internal consistency check of the paper's formulas, not independent evidence that the paper's W is the true Weil functional. [A7]

**Cost of the all-a quantifier (Observed, float64, not interval).** The pole and prime terms of g cancel to ~1e-5 relative accuracy at t=14, with individual terms reaching 4e3. The cancellation is of von Koch type, so an a-uniform proof carries RH-strength prime-side information (classical equivalence, cited, not derived). [A8]

**SUCC completion spec (Conjectured; each item is an undischarged typed obligation).** [A11]
- C1: source-first identification of the SUCC Gram with Q_W|V_a, with mutant failures.
- C2: restriction-map consistency.
- C3: exhaustion, which is automatic from the causal finite horizon.
- C4: a Pi_1-strength inequality with prime/pole cancellation uniform in a.
- C5: non-circularity, meaning no passage through sum_gamma |v^(gamma)|^2.
- Without C4 the honest output is Sigma_1: refutation witnesses and certified single-a lower bounds. P06 collapses to P07 under C1-C3.

## 3. Route B: Nyman-Beurling / Baez-Duarte (independent of Suzuki; N01-N07)

Setup: r_n(x)=(k mod n)/n on the reciprocal cell k=floor(1/x), with L2 weights 1/(k(k+1)).

**D1 (Disclosed).** E_N* is a constrained distance (SUCC span, A(1)=0), not the classical d_N^2. With D_N the classical L2(0,inf) distance:
- D_N <= E_N* <= (log 2pi - gamma) D_N, and log 2pi - gamma = 1.26066140151....
- The proof sets g'=g-A(1)rho_1 and applies Cauchy-Schwarz with kappa=log 2pi-gamma-1.
- Hence E_N*->0 <=> D_N->0 <=> RH (classical BD criterion, cited).
- **This corrects FANOUT_SYNTHESIS sec.3/4 ("E_N* is the classical d_N^2").** The crucible's Plancherel route gave d_2^2~0.290, not 0.307.

**Certified finite values (Corroborated).** Four routes agree; the crucible re-derived the values with an arithmetically independent Gram and a structurally independent Plancherel route.
- U_N <= D_N <= E_N*, all non-increasing in N.
- E_2*=1-log 2=0.306852819440054690582767879; D_2=0.289964573742202731811200583.
- E_3*=0.0957477839277540266143081193 (closed form with the pi*sqrt3 class-number term).
- E_30*=0.0145567335769969923509342799; D_30=0.0145301104741372508696171843; U_30=0.0142067381065618179233355537.
- Ratio E/D falls from 1.0582 (N=2) to 1.0018 (N=30).
- Interval widths in the original run were <=1e-47. The crucible reproduced the centre values, not the widths. Rigor is conditional on the DLMF 5.11 remainder lemma. [D2]

**N05 is RH-equivalent (Disclosed).** Any proof of N05 is a proof of RH, so zero-independence is automatic and uninformative. [D3]

**Source-first interpolant (Observed).**
- Exact identity: for K<k<=2K+1, 1-F_K(k)=(K+1) m_K+M(k)-M(K), with m_K=sum_{n<=K} mu(n)/n and M the Mertens function. The interpolant is exact (residual 0) on every cell k<=K.
- Checked in exact Fractions on 1677 cells (K=2..40), 0 mismatches. The re-run test_D4 in this program independently re-derives the formula.
- Weighted-ell2 residual lower bounds (partial sums to k=20000): K=13 >=0.0329967; K=30 >=0.0367454; K=60 >=0.0377467; K=100 >=0.0376880; K=200 >=0.0368854; K=400 >=0.0378740.
- A plateau near 0.037 for all K is a random-walk heuristic only. [D4]

**Zero-independent Mobius sources (Observed; N=3..30).**
- Plain truncation -mu(n) fluctuates with M(N): 0.2144 (N=3), 0.0486 (N=5), 0.0374 (N=7), 0.0712 (N=30).
- The Riesz-weighted BCF version gives 0.32449 at N=30, about 22 times D_30. [D5]

**LCM blackout (Observed).** The ZCR-06 bound 1/L^2 is 1.84e-25 at N=30, versus E_30*=0.0146. It stays PROVED_LOCAL but is vacuous as the NB barrier. [D6]

**Baez-Duarte c_k (Observed).** c_0=0.607927101854, c_1=-0.316011301068, c_100=-0.00147737763416, c_800=-2.56536314203e-5. Over this range c_k~-16.42/k^2 is dominated by the trivial-zero term. The Rice explicit formula reproduces c_k numerically; its derivation is not made rigorous. Zeros are used only as a hostile cross-check, never as inputs. [D7]

**Verdict (Conjectured status of N05 itself).** SUCC adds exact small facts and a reformulation, not a route around the wall. [D8]

## 4. Route C: spectral realization and eq 1.12 (nodes S02-S11)

Instrument: an exact lag-lattice toy. D(s)=1+p^{-s} with ell=2, Gamma=pi(Z+1/2), Toeplitz classes, built with mpmath interval arithmetic. It is calibrated against an independent closed form and an independent zero-side Galerkin (agreement 5e-6 to 7e-4, float only). [B1, Corroborated]

**Results in the toy.**
- For a<b=ell/2: Spec(D_{a,theta})={(pi k+atan(tanh a * tan(theta/2)))/a}, a lattice of spacing pi/a, never Gamma. The closed form solves the boundary condition to ~1e-40 (test_toy).
- Nyquist a=b, theta=pi: W=c*cos z and Spec=Gamma exactly. The eq 1.12 analogue is exact at the single critical width. [B2, Disclosed in toy]
- For a>b: as tau->0+, W0=lim tau*W vanishes on all of Gamma for every theta (the identity B_n(-1)=0 holds symbolically for n=2..5). This needs ker A_a != 0, which is the RH-failure regime. The remaining zeros are theta-dependent. [B3, Disclosed in toy]
- Density budget: real zero counts 7, 13, 19, 31, 44 against 2aX/pi = 6.37, 12.73, 19.10, 31.83, 44.56 for a = 1/2, 1, 3/2, 5/2, 7/2. Spec does not converge to Gamma in Hausdorff distance. [B4, Observed]
- UHP limit with intrinsic normalization, a>b: R_a -> constant 1, with error ~0.42/N for a=N (N*err = 0.4935, 0.4587, 0.4343, 0.4231, 0.4177 at N=4..64) and ~0.80/N for a=N+1/2. The Gamma target sits 0.3853 away and is not reached. [B7, Observed]
- Bearing C's independent toy confirms the same flattening: the limit is the constant 1 independent of mu, with max|R-1|~1/a and the distance to the toy target saturating at 0.3484. Both toys are lag-lattice combs on the same Gamma, so this is corroboration of a shared structure, not two independent mechanisms. [C6, Observed]
- Beyond the critical width the toy is outside the Suzuki class: Q(psi(x)+psi(x-2))=0 exactly, so lambda_a jumps 2->0 and Thm 1.3 coercivity fails. [C6]

**General-xi obstructions.**
- Jensen window (Disclosed, classical inputs: Jensen, Paley-Wiener, Riemann-von Mangoldt main term, no zero positions). W has type <= a, so N_W(r) <= (2a/pi) r+O(log r), while N_Gamma(r)~(r/pi)(log(r/2pi)-2). No fixed finite-interval spectrum contains all of Gamma. The crossing scale is r*(a)=307.357, 2489.14, 18673.5, 138329.0 for a=1..4 (asymptotic 2*pi*e^{2a+2}). The constants are uncontrolled, so these are scales, not thresholds. [B5]
- Lemma V / vacuity of the phi-clause (Disclosed, derived independently in B6 and C2).
  - W_a is zero-free in the UHP by Thm 1.5. For arbitrary analytic phi, "exists phi with e^phi W_a -> T=Xi/(Xi+iXi') locally uniformly" is equivalent to T zero-free in the UHP, which is equivalent to RH.
  - The trivial phi=log T-log W_a works under RH. Hurwitz gives the converse. Under RH, Im(Xi'/Xi)<0 in the UHP, so E=Xi+iXi' is zero-free there.
  - Winding numbers (Observed): 0, 0, 7 for W_a, (1+X)/W_a, (1-2X)/W_a.
  - Cor 1.6 as printed is therefore a tautological reformulation of RH. The only content is a target-free constraint on phi.
- Reality of W(a,theta;z) is source-blind (Observed). A nonreal-pair "fake" form (Gamma_fake=pi(k+1/2)+-i ln2/2, with eig C_2={-1/4,9/4}, C_3(1,0,-1)=-9/8*(1,0,-1) exactly) has the identical W for a<=b. Once T is made positive it is real-rooted anyway. With tau=-1/2 the reality fails (5 real roots, UHP winding 5), so positivity is load-bearing. [B8]
- theta=pi is the zero-free parity choice: v_-=R v_+ gives W(-z)=-e^{i theta}W(z) iff e^{2i theta}=1, with theta=pi even. [C3, Disclosed]
- The section 7 normalization phi=-log E_a with lambda=0 is RH-presupposing: (7.7) needs real gamma, the paper assumes RH at the start of section 7, and its own text says (1.12) needs lambda=0 for large a, which is equivalent to RH. [C7, Disclosed]
- Left-edge boundary-layer mechanism: e^{iaz}W is dominated by the left-edge layer, so phi~iaz+c(a). [C8, Conjectured]
- PR#59 reconciliation (Observed): the unit-modulus modes e_gamma 1_(-a,a) have L2 mass 1/(2*pi*N)->0 but Q-energy share exactly 1 (Fractions, N=1,2,3,4,6,12). The PR#59 no-go is about L2(0,1) and does not touch Suzuki's H(A_inf). The carrier -> H_W identification is the missing section 6 step, still unverified. [B9]
- Gram/Mobius link is only an analogy: no exact relation to GRAM_MOBIUS T1-T4. [B10, Conjectured]

## 5. Zero-independence classification (bearing C; ZF = zero-free construction, ZD = zero-dependent, RH = RH-presupposing)

| Object | Defined from | Verdict |
|---|---|---|
| Lambda(n), g of eq 1.3 | primes, psi(1/4), log pi, Lerch, e^{t/2}+e^{-t/2}-2 | ZF (carries full Gamma/pole source data; burden on A08/A09/H03/H10/P03) |
| k(t)=sum e^{-i gamma t}=-g'' | zeros, or g via explicit formula (cited) | ZD as written; ZF content |
| G_a, B_a, A_a (Friedrichs), Q_W^a, lambda_a, continuity | g | ZF |
| lambda(a)<lambda_a | certified finite lower bound on lambda_a | ZF per fixed a; needs a rigorous bound, which the paper does not supply |
| lambda(a)=0 for large a | A_a>0 | RH (equivalent) |
| T_a, H(T_a), D_a, v_pm, W(a,theta;z), real roots | g, lambda | ZF (only finitely many primes at fixed a) |
| theta(a)=pi | parity | ZF |
| theta(a) tuned to T | target | ZD |
| phi=iaz+c(a), c from ||v_pm||=1 | support endpoint, norm | ZF |
| phi=-log E_a | de Branges function of H(A_a^) | RH |
| phi_triv=log T-log W | target | ZD and tautological |
| Target xi/(xi+xi'), E=xi+xi' | zeta | ZD (output, not input) |
| Gamma, m_gamma, U, F_gamma, B=H(E) | zeros | ZD, RH-conditional |
| Hurwitz step | xi | uses the zero set as output only |
| Section 7.7 criterion | S_x, g-kernel | ZF positive-realization problem (Route A/P05 in disguise) |

Verdict: compliant finite-interval inputs, RH-strength output, RH-presupposing de Branges machinery. "The kernel is built from the zeros" is Refuted as a statement about the construction. "The section 7 mechanization is a zero-independent proof route" is Refuted as mechanized. "No zero-independent proof of 1.12 can exist" is NOT shown (Conjectured, no obstruction receipt). The section 8 Fredholm route (first-kind equations with kernel g(x-y)+lambda N(x,y)) is the open possibility. [C1, C9, C10]

## 6. Consolidated ledger

Disclosed (proof within declared boundary; cited inputs named):
- T1 window exhaustion; Lemma M monotonicity/inertia; Thm 1.3 gives no uniformity; CM1; CM2; Ritz upper-bound direction; shift-manufactured positivity; firewall map of Q_W^a.
- Finite-interval layer is zero-free by definition.
- Lemma V (phi-clause <=> RH), derived twice.
- Jensen window for general xi; theta=pi parity.
- Section 7 mechanization is RH-presupposing.
- E_N* comparability D_N <= E_N* <= (log 2pi-gamma) D_N.
- N05 is RH-equivalent.
- Toy: Nyquist identity; anchor W0|Gamma=0 (needs ker A_a).

Corroborated: calibrated toy engine; U_N <= D_N <= E_N* table (N<=30).

Observed:
- g transcription and Q_W=W to ~1e-13 on three Gaussians.
- Prime/pole cancellation table.
- Screw-Gram one-sided source sensitivity.
- Toy density budget; constant UHP limit; fake-form source-blindness.
- Q-topology normalizability.
- Source-first interpolant error formula (exact) and ell2 plateau 0.033-0.038 (lower bounds).
- Mobius sources; LCM vacuity; BD c_k.

Conjectured: SUCC completion spec C1-C5; left-edge boundary layer; no-zero-independent-proof-of-1.12 not shown; Gram/Mobius link; N05 itself.

Refuted: "the kernel is built from the zeros so the Suzuki finite layer is not zero-independent"; "section 7 de Branges machinery is a zero-independent route"; "E_N* is the classical d_N^2" as an identity (true only up to factor 1.2607); Spec(D_{a,theta}) -> Gamma as a->inf (false in the toy, impossible for xi); Cor 1.6 as printed is informative (vacuous).

## 7. Firewall status

Intact.

Intact across all survived work. (1) No survived finding consumes a nontrivial zero position as a construction input. The Suzuki finite-interval layer is built from primes, digamma and Lerch terms (eq 1.3). In bearing A the zeros appear only in a flagged post-hoc validation. In bearing B the Jensen window uses only the smooth Riemann-von Mangoldt law. In bearing D, zetazero appears only as a hostile cross-check of the Rice identity and never feeds a coefficient. (2) No finite Gram PSD is passed off as a completed-Weil-positive form. A6 and A9 prove the opposite: finite Gram evidence gives only upper bounds on lambda_a, and detection of wrong sources is one-sided. The carrier -> H_W identification (B9) and the SUCC Gram -> Q_W|V_a identification (A11/C1) remain explicitly unverified. (3) Section 5 is respected: no finite enumeration is used as a universal proof, and the only universal step in T1 is that every test function has compact support. (4) Section 8 is respected: every numeric claim is labelled Observed or Corroborated unless exact (Fractions/sympy). No interval-arithmetic certificate was independently re-derived in this synthesis, and the crucibles reproduced centre values, not enclosure widths. (5) Section 7: the Suzuki finite layer is compliant, but the eq 1.12 target (xi itself) and the section 7 de Branges mechanization are zero-dependent or RH-presupposing and are classified as such; "refuted as zero-independent" is reported as an honest result. No node is promoted without an independent proof, Sigma_1-not-Pi_2 stands, and RH is not proved.

## 8. Dropped, open, next

**Dropped by the crucible.**
- C5 headline, "the target xi/(xi+xi') is not a function of the zero set alone", is false. F(z)=xi(1/2-iz) is even, real and of genus 0, so it is determined by its zeros up to a constant that cancels in T. In the toy, the calibration c is the zero spacing pi/c.
- What survives of C5 is the exact algebra, labelled Observed and not as a finding: the translation normalization phi=iaz yields (1+e^{2icz})/2, whereas the de Branges target is cos(cz)/(cos(cz)-ic sin(cz)); these differ for c != 1. This is a statement about the normalization, not about zero-determinacy.

**Open obligations (sharpest first).**
- Sigma_1 side: interval-certified lower bound on lambda_a at fixed a (Temple/Weinstein with a certified gap, interval arithmetic on g of eq 1.3).
- A target-free, non-vacuous constraint on phi.
- A Galerkin/enclosure test on a log-density Gamma proxy with A_a>0 for all a.

**All open obligations.**
- Sigma_1 side (A6, A11/C4): build and interval-certify (mpmath.iv, rigorous digamma/Lerch/prime sums) a Temple/Weinstein-type lower bound on lambda_a at fixed a, with a certified gap to the next eigenvalue of A_a. This yields certified 'no counterexample below horizon a' statements. No such certificate exists.
- sigma-identification (A11 C1, P03/P05/S11): source-first derivation that a SUCC finite-horizon Gram on a declared probe menu equals Q_W|V_a, with real Lambda/Gamma/pole/conductor/half-density/phase and failing fake-composite, non-Euler, wrong-half-density and wrong-Gamma mutants. A9 shows wrong-sign-Gamma mutants pass finite PSD, so the identification must be proved, not tested.
- All-a Pi_1 inequality (A11 C4/C5): a proof of Q_W>=0 on Cc^inf(R) from prime/arch data with explicit pole/prime cancellation uniform in a, not passing through sum_gamma |v^(gamma)|^2 or the de Branges identification. This is RH.
- Eq 1.12 (B6/C2/C8): a target-free, non-vacuous constraint class on phi (for example phi=iaz+c(a) with c from ||v_pm||=1), plus a proof or refutation of the restricted statement. The free-phi version is equivalent to RH and carries no content.
- Regime gap (B nag, boundary): no exactly solvable toy reproduces the RH-true regime (A_a>0 for all a, with log-density Gamma). B3/B7/C6 must not be transplanted. A Galerkin/enclosure computation on a log-density Gamma proxy is needed.
- Sharp threshold for Thm 1.5 reality in tau (B nag): indefinite T at tau=1/5, 1/10 still gave full real spectra, so T>0 is sufficient but not necessarily sharp. Toy artifact or a weaker hypothesis is unknown.
- Unconditional status of the de Branges property of H(A_a^) without RH (C7/C10): neither proved nor refuted. The section 8 first-kind Fredholm route is untested.
- Route B N05: a zero-independent L2 approximation sequence with a rigorous norm bound ->0. This is RH-equivalent, so no independent progress is expected.
- Documentation: correct FANOUT_SYNTHESIS sec.3/4 ('E_N* is the classical d_N^2') to the comparability statement, and correct the SUZUKI_2606_09096_FRONTIER.md line 10 phrasing to separate the representation from the construction.
- Interval certification of every numeric currently labelled Observed (Q_W=W identity, screw-Gram mutant table, A8 cancellation table, toy UHP-limit scans). Continuity of lambda_k for k>=2 is not proved. Rice formula and Jensen constants are not made rigorous.
- Convene sibling Ricks for: (a) mutant controls (fake composite, non-Euler) run through the Thm 1.5 construction at fixed a; (b) the closability/L2-embedding of the global Q_W on Cc^inf(R) needed for H(A_inf).

**Next experiment.** Build the first certified Sigma_1 instrument: an interval-arithmetic (mpmath.iv) Temple/Weinstein lower bound on lambda_a for a small, fixed a, say a in {1/2, 1}. Discretize Suzuki's A_a on a Galerkin basis with an exactly computed Gram from eq (1.3), using the g already transcribed and tested here. Obtain an upper bound on lambda_a from Rayleigh-Ritz, a rigorous residual norm, and a certified lower bound on the next eigenvalue. This yields a rigorous lambda_a > 0 at that horizon. Control it with the primes-only and fake-6 mutants, which must certify negative as in A9. It would be the first thing in this program that moves beyond observed finite numerics and fits SUCC's Sigma_1 verifier stance. It also supplies the 'lambda(a)<lambda_a certified by a finite computation' that the Thm 1.5 construction needs (C9 table), and it avoids the all-a quantifier, which every bearing identified as equivalent to RH.