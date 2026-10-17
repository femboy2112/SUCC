# THE FOUR-BODY BREAKOUT: COMPLETE FOUR-MOMENT PRIMITIVE-DUAL QUOTIENT, PARITY-SPLIT BESSEL COERCIVITY, AND CERTIFIED DERIVATIVE GRAM

**Branch:** `research/deepseek-pdq-megaswarm-2026-10-16` (extending `research/dual-variational-schur-source-gates-2026-10-16`, PR #150, child of PR #149)  
**Source Authority:** Original Suzuki signed completed Weil operator (`0cc8510b71d178fc79e8d410a86d8b6014cf9178`), $a = 1/2$, genuine prime-2 wavefront $((2,2),)$, one real $\Gamma_{\mathbb{R}}$, both completed poles, $C_\infty$ contact.  
**Nontrivial Zeta-Zero Coordinates Used:** `False`  
**Four-Mode Schur Sign $S_4 = A_4 - R_4$:** `OPEN` (`AMBIGUOUS`)  
**Riemann Hypothesis Proved:** `NO` (`RH_proved: False`)

---

## 1. Executive Summary & Quantitative Progress

On the first-window mean-zero derivative carrier $H = L_0^2(-1/2, 1/2)$ with low subspace $F_4 = \operatorname{span}\{P_1(2t), \dots, P_4(2t)\}$ and high projection $Q_4 = I - P_{F_4}$, the primitive-dual quotient theorem (`PDQ-01`, `PDQ-02`) identifies the inverse-Neumann $K = V^*V = (-\Delta_N)^{-1}$ dual energy of the high residual $Q_4 h_x$ ($h_x = G(x - Ux)$) with the unprojected polynomial quotient:
$$\sup_{w \in Q_4 H \setminus \{0\}} \frac{|\langle Q_4 h_x, w\rangle|^2}{\langle Kw, w\rangle} = \|(I - \Pi_{\le 3}) h_x'\|_{L^2(-1/2, 1/2)}^2 = H'_{xx} - (E^* P^{-1} E)_{xx}.$$

In PR #150, only the two endpoint-vanishing combinations $\phi_e(t) = t^2 - 1/4, \phi_o(t) = t(t^2 - 1/4)$ were subtracted (`30 c_1^T c_1 + 210 c_2^T c_2`), while the derivative energy $H'$ was bounded by the coarse global Young inequality $\|g'\|_{L^1}^2 N_U < (11/40)^2 N_U$ and divided by the global coercivity constant $\kappa = 1/50$.

In this campaign, we execute a hostile audit of PR #150 and deliver five interconnected breakthroughs (Wave I Moonshots A–E) together with six independent structural theorems and countermodels (Wave II Agents G–L):

| Quantity | PR #149 / #150 Baseline | This Campaign (`PDQ-07`..`PDQ-14`) | Improvement Factor |
|---|---|---|---|
| Authenticated polynomial moment channels | $2$ ($\phi_e, \phi_o$) | **$4$** ($\phi_e, \phi_o, \psi_e = \frac{1}{2}u_3', \psi_o = \frac{1}{2}u_4'$) | Complete $\mathcal{P}_{\le 3}$ |
| Odd-mode-1 subtracted moment energy $(E^* P^{-1} E)_{11}$ | $3.783 \times 10^{-7}$ ($30 c_{1,1}^2$) | **$2.346 \times 10^{-5}$** ($30 c_{1,1}^2 + \frac{1}{24}M_{3,1}^2$) | **$62.0\times$ larger subtraction** |
| High-sector coercivity $\kappa_{\mathrm{odd}}$ on $Q_4 H_{\mathrm{odd}}$ | $1/50 = 0.020$ | **$63/500 = 0.126$** | **$6.3\times$ stronger** |
| High-sector coercivity $\kappa_{\mathrm{even}}$ on $Q_4 H_{\mathrm{even}}$ | $1/50 = 0.020$ | **$153/500 = 0.306$** | **$15.3\times$ stronger** |
| Certified $U=0$ odd-sector $\lambda_{\min}(S_4^{\mathrm{lower}})$ | $-1.260304$ | **$-0.029142$** | **$43.2\times$ closer to $0$** |
| Certified $U=0$ even-sector $\lambda_{\min}(S_4^{\mathrm{lower}})$ | $-0.756015$ | **$-0.015150$** | **$49.9\times$ closer to $0$** |

---

## 2. Moonshot A — Hostile Audit of PR #150 & Complete Source-Certified 4-Moment Quotient (`PDQ-04`, `PDQ-07`)

### 2.1 Four Concrete Defects Found and Fixed in PR #150's 2-Moment Implementation
1. **Cross-Parity Error Contamination (`four_schur_dual_quotient.py:210-215`)**: `vanishing_boundary_moment_lower` subtracted `weight * ((1/t)-1) * radius2` from all four diagonal entries $I_4$, even though row 0 ($c_1$, weight $30$) is supported strictly on odd modes $\{0, 2\}$ and row 1 ($c_2$, weight $210$) is supported strictly on even modes $\{1, 3\}$. At $U=0, J=64$, the weight-$210$ even error penalty contaminated the odd block and made `source_dual_boundary_lower_bracket` strictly worse than the unsubtracted `source_dual_U_lower_bracket` on modes 1 and 3 (by $-3.73\times 10^{-5}$ and $-4.61\times 10^{-5}$).
2. **Missing Reflection-Parity Zeroing on Omitted Gamma Row Error (`certified_four_schur_trial.py:435-440`)**: When `(jj - i) % 2 == 1`, $\langle P_{jj+1}, (G - G_J) v_i \rangle = 0$ identically by reflection parity, yet `omitted_gamma_row_error` was added to `row_err[i]`.
3. **Coarse $\ell^1$ Sum vs $L^2$ Cauchy–Schwarz (`certified_four_schur_trial.py:436-438`)**: Used $\tau_J \sum_k |V_{k,i}|$ instead of the exact Cauchy–Schwarz bound $\tau_J \|P_{jj+1}\|_{L^2} \|v_i\|_{L^2} = \tau_J \sqrt{\frac{(W_{L^2})_{ii}}{2jj+3}}$.
4. **Hardcoded $\eta = 1/2$ Signal Loss (`four_schur_dual_quotient.py:181, 214`)**: Hardcoding $\eta = 1/2$ discarded $50\%$ of the positive rank-one moment subtraction $m_k^T m_k$ even when interval error $e_k \sim 10^{-14}$. Our new `_sector_rank_one_lower` bounds $|c_i c_j - m_i m_j| \le |m_i| e_j + e_i |m_j| + e_i e_j =: \Delta_{ij}$ strictly on the active parity sector $S$, retaining $100\%$ of $m_k^T m_k$ at zero error and preventing cross-parity leakage.

### 2.2 Theorem A.1 (Complete Orthogonal 4-Moment Decomposition of $E^* P^{-1} E$)
Let $u_k(t) = P_k(2t)$ on $I = (-1/2, 1/2)$. The polynomial space $\mathcal{P}_{\le 3}(I)$ admits two canonical $L^2$-orthogonal decompositions:
1. **Shifted-Legendre Basis $\{P_0(2t), P_1(2t), P_2(2t), P_3(2t)\}$**:
   With $L_{m,i} = \langle P_m(2t), h_i'(t) \rangle_{L^2(I)}$ ($m=0,1,2,3$) and $M_{k,i} = \langle u_k', h_i' \rangle_{L^2(I)}$ ($k=1,2,3,4$):
   $$L_0 = E_0 = \frac{1}{2}M_1, \quad L_1 = 2E_1 = \frac{1}{6}M_2, \quad L_2 = E_0 - 6c_1 = \frac{M_3 - M_1}{10}, \quad L_3 = 2E_1 - 10c_2 = \frac{M_4 - M_2}{14},$$
   and
   $$E^* P^{-1} E = L_0^T L_0 + 3 L_1^T L_1 + 5 L_2^T L_2 + 7 L_3^T L_3.$$
2. **Interior Endpoint-Vanishing Plus Boundary-Flux Decomposition**:
   $$\mathcal{P}_{\le 3}(I) = \operatorname{span}\{\phi_e, \phi_o\} \oplus^{\perp_{L^2}} \operatorname{span}\{\psi_e, \psi_o\},$$
   where $\phi_e(t) = t^2 - 1/4 = -(V u_1)(t)$, $\phi_o(t) = t(t^2 - 1/4) = -\frac{1}{2}(V u_2)(t)$ vanish at $\pm 1/2$, and $\psi_e(t) = \frac{1}{2}u_3'(t) = 30t^2 - \frac{3}{2}$, $\psi_o(t) = \frac{1}{2}u_4'(t) = 140t^3 - 15t$ satisfy $\langle \phi_e, \psi_e \rangle = -\langle V u_1, \frac{1}{2}u_3' \rangle = \frac{1}{2}\langle u_1, u_3 \rangle = 0$ and $\langle \phi_o, \psi_o \rangle = \frac{1}{4}\langle u_2, u_4 \rangle = 0$, with $\|\psi_e\|_2^2 = 6, \|\psi_o\|_2^2 = 10$. Consequently:
   $$\boxed{E^* P^{-1} E = 30 c_1^T c_1 + 210 c_2^T c_2 + \frac{1}{24} M_3^T M_3 + \frac{1}{40} M_4^T M_4,}$$
   and the monomial moments $E_{j,i} = \int_{-1/2}^{1/2} t^j h_i'(t)\,dt$ are recovered via
   $$E_0 = \frac{1}{2}M_1, \quad E_1 = \frac{1}{12}M_2, \quad E_2 = \frac{1}{40}M_1 + \frac{1}{60}M_3, \quad E_3 = \frac{1}{112}M_2 + \frac{1}{280}M_4.$$

At $U=0, J=64$, the boundary channel $\frac{1}{24}M_{3,1}^2 \approx 2.308 \times 10^{-5}$ is **$61.0\times$ larger** than the interior channel $30 c_{1,1}^2 \approx 3.783 \times 10^{-7}$, bringing the total odd-mode-1 subtracted moment energy to $2.346 \times 10^{-5}$ ($25.8\%$ of the true derivative energy $H'_{11} \approx 9.081 \times 10^{-5}$).

---

## 3. Moonshot C — Parity-Split High-Sector Bessel Coercivity (`PDQ-08`)

### Theorem C.1 (Parity-Split High Coercivity on $Q_4 H = Q_4 H_{\mathrm{odd}} \oplus Q_4 H_{\mathrm{even}}$)
Both the signed Suzuki operator $G$ and the inverse-Neumann operator $K = V^*V = (-\Delta_N)^{-1}$ commute with reflection $(Rf)(t) = f(-t)$, while the primitive map $V: L_0^2(-1/2, 1/2) \to H_0^1(-1/2, 1/2)$ anticommutes with $R$ ($R V = -V R$). Therefore $D_4 = D_{4,\mathrm{odd}} \oplus D_{4,\mathrm{even}}$ and $Q_4 K Q_4 = K_{\mathrm{odd}} \oplus K_{\mathrm{even}}$ block-diagonalize across parity:
1. **Odd High Derivative Sector ($w \in Q_4 H_{\mathrm{odd}}$, coupling to $(P_1, P_3)$)**:
   The primitive $f = Vw \in H_0^1(-1/2, 1/2) \cap \mathcal{V}_4$ is **EVEN**, so $\langle f, \sinh(t/2) \rangle = 0$ identically (zero negative pole leakage) and $\langle f, P_{2k+1}(2t) \rangle = 0$ for all $k \ge 0$. Hence only **even spherical Bessel modes** $\ell \in \{4, 6, 8, \dots\}$ contribute to the low-frequency Fourier leakage. At $\Omega = 16, J = 256$:
   $$\boxed{D_{4,\mathrm{odd}} \succeq \frac{63}{500} K_{\mathrm{odd}} = 0.126\, K_{\mathrm{odd}} \quad \left(\frac{1}{\kappa_{\mathrm{odd}}} = \frac{500}{63} \approx 7.9365 \text{ vs.\ } 50\right).}$$
2. **Even High Derivative Sector ($w \in Q_4 H_{\mathrm{even}}$, coupling to $(P_2, P_4)$)**:
   The primitive $f = Vw \in H_0^1(-1/2, 1/2) \cap \mathcal{V}_4$ is **ODD**, so $\langle f, P_{2k}(2t) \rangle = 0$ for all $k \ge 0$ — in particular $\langle f, P_4(2t) \rangle = 0$ automatically! Thus $f \in \mathcal{V}_5$ has **five** vanishing polynomial moments ($0..4$), and only **odd spherical Bessel modes** $\ell \in \{5, 7, 9, \dots\}$ contribute. At $\Omega = 18, J = 256$:
   $$\boxed{D_{4,\mathrm{even}} \succeq \frac{153}{500} K_{\mathrm{even}} = 0.306\, K_{\mathrm{even}} \quad \left(\frac{1}{\kappa_{\mathrm{even}}} = \frac{500}{153} \approx 3.2680 \text{ vs.\ } 50\right).}$$
3. **Global Coercivity on $Q_4 H$**:
   $$D_4 \succeq \min(\kappa_{\mathrm{odd}}, \kappa_{\mathrm{even}}) Q_4 K Q_4 = \frac{63}{500} Q_4 K Q_4 > \frac{1}{8} Q_4 K Q_4.$$

---

## 4. Moonshot B — Certified Differentiated Convolution Energy $H'_{ij} = \langle h_i', h_j' \rangle$ (`PDQ-09`)

### 4.1 Comparison of Routes B1, B2, B3
- **Route B1 (Real-Space Midpoint-Lipschitz Integration)**: Evaluates $(G_J v_i)'(x)$ at the positive-half midpoints $x_q = \frac{2q+1}{2\cdot\mathrm{grid}}$ using exact 90-digit rational intervals for the two poles, contact primitive, prime-2 hinge, and $J$ Gamma rungs (`authentic_suzuki_mode_derivative_point`), and integrates $(G_J v_i)'(x)(G_J v_j)'(x)$ over all cells using reflection symmetry and the proved total-variation Lipschitz bound $L_i = V_J \sum_{m=1}^{\mathrm{rank}} |V_{m-1, i}|$ ($V_J = 16 + 8\sum_{j<J}\frac{1}{4j+1}$).
- **Route B2 (Frequency-Space Plancherel)**: Strictly leaky because whole-line Plancherel integrates $|(g_J' * v_i)(x)|^2$ over $[-1, 1]$ rather than $[-1/2, 1/2]$, losing interior cancellation against the exterior wings $|x| \in (1/2, 1)$, and suffers $O(\Omega^{-1})$ high-frequency tail decay because $v_i(\pm 1/2) \ne 0$.
- **Route B3 (Sharpened $O(J^{-3/2})$ Polynomial Integration-by-Parts Gamma Tail)**:
  For a polynomial trial $v_i \in L_0^2(-1/2, 1/2)$, integration by parts on each omitted Gamma rung $j \ge J$ ($\alpha_j = \frac{4j+1}{2}, c_j = \frac{4}{(4j+1)^2}$) gives
  $$\frac{d}{dx}(E_{\alpha_j} v_i)(x) = (E_{\alpha_j} v_i')(x) + v_i(-1/2) e^{-\alpha_j(x+1/2)} - v_i(1/2) e^{-\alpha_j(1/2-x)}.$$
  Since $\|E_{\alpha_j}\|_{L^2 \to L^2} \le \frac{2}{\alpha_j} = \frac{4}{4j+1}$ and $\|e^{-\alpha_j(1/2 \pm x)}\|_{L^2(-1/2,1/2)} \le \frac{1}{\sqrt{2\alpha_j}} = \frac{1}{\sqrt{4j+1}}$, summing over $j \ge J$ ($d = 4J+1$) yields:
  $$\boxed{\|((G - G_J) v_i)'\|_{L^2(-1/2,1/2)} \le 2 \|v_i'\|_{L^2}\left(\frac{1}{d^2} + \frac{8}{d^3}\right) + \bigl(|v_i(1/2)| + |v_i(-1/2)|\bigr)\left(\frac{2}{3 d^{3/2}} + \frac{4}{d^{5/2}}\right),}$$
  improving the $O(J^{-1})$ Young tail $\eta_J = \frac{2}{d} + \frac{8}{d^2}$ by **$5.7\times$** at $J=20$ ($0.00263$ vs $0.01496$ on mode 1).

Combining Routes B1 + B3 with Moonshots A and C in `CertifiedDerivativeEnergyTrial` tightens the certified $U=0$ $S_4$ lower bracket minimum eigenvalues from $(-1.260304, -0.756015)$ to **$(-0.029142, -0.015150)$** at $J_{\mathrm{deriv}}=20, \mathrm{grid}=256$.

---

## 5. Moonshot D — Exact Obstruction to Nested $30 \to 4$ Young-Bracket Transport (`PDQ-10`)

### Theorem D.1 (`source_30mode_middle_block_obstruction_certificate`)
By Haynsworth transitivity (`CFS-06`), $S_4 = \operatorname{Short}_{F_4}(S_{30})$. The variational monotone-transport argument $\operatorname{Short}_{F_4}(L_{30}) \preceq S_4$ (`PDQ-06`) uses, as a **sufficient hypothesis**, that the discarded 26-mode middle block $L_{30}|_{5..30}$ of the *computed Young lower bracket* $L_{30}$ be strictly positive definite. (This is sufficient, **not** necessary — a non-PD middle block merely removes the guarantee; it does not force the transport to fail. And the obstruction is to the computed Young **bracket** $L_{30}$, not to the true complement $S_{30}$, whose modes 5..30 do carry the inherited source coercivity $D_4 \succeq K/50$.) For the 30-mode Young lower bracket $L_{30}(\kappa_{30}) = A_{30} - \frac{(11/40)^2}{\kappa_{30}} W_{L^2, 30}$, since $\|G\|_{\mathrm{op}} \le \|g\|_{L^1(-1,1)} \le \|g'\|_{L^1(-1,1)} < \frac{11}{40}$, we have $A_{30} \prec \frac{11}{40} W_{L^2, 30}$, and therefore:
$$L_{30}(\kappa_{30})\big|_{5..30} \prec \left(\frac{11}{40} - \frac{121}{1600 \kappa_{30}}\right) W_{L^2, 5..30} = -\frac{26191}{14760} W_{L^2, 5..30} \prec 0 \quad (\text{at } \kappa_{30} = 369/10000),$$
and $\prec -\frac{187}{200} W_{L^2, 5..30} \prec 0$ at $\kappa_{30} = 1/16$. Structurally, $G$ is compact on $L_0^2(-1/2, 1/2)$ so $(A_{30})_{mm}/W_{mm} = O(m^{-2})$ ($\approx 0.00397$ at $m=5$ down to $\approx 0.00075$ at $m=30$), whereas the unprojected Young penalty subtracts an $O(1)$ multiple of $W_{mm}$.

---

## 6. Wave II Independent Moonshots (`PDQ-11`..`PDQ-14`)

1. **Agent L — Hodge–Legendre Cochain Isomorphism (`PDQ-11`, `hodge_legendre_endpoint_free_gram`, `general_endpoint_free_moment_lower`)**:
   For every cut $m \ge 2$ on $I = (-a, a)$, the polynomial space $\mathcal{P}_{\le m-1}(I)$ decomposes $L^2$-orthogonally as
   $$\mathcal{P}_{\le m-1}(I) = V(F_{m-2}) \oplus^{\perp_{L^2}} \operatorname{span}\{L_{m-1}', L_m'\},$$
   where $\phi_k(t) = (V L_k)(t) = \frac{a}{2k+1}(P_{k+1}(t/a) - P_{k-1}(t/a))$ ($k=1,\dots,m-2$) vanish at $\pm a$ and have $L^2(I)$ Gram matrix identically equal to the tridiagonal inverse-Neumann submatrix $K_a^{[1..m-2]}$. At $m=4, a=1/2$, $K_{1/2}^{[1..2]} = \operatorname{diag}(1/30, 1/210)$, explaining the weights $(30, 210)$. At $m=5, a=1/2$, $(K_{1/2}^{[1..3]})^{-1}$ couples modes 1 and 3 with exact odd block $\begin{pmatrix} 168/5 & 252/5 \\ 252/5 & 3528/5 \end{pmatrix}$.
2. **Agent J — Observer Interior/Boundary Synergy & Cross-Gauge No-Ghost Gluing (`PDQ-12`, `observer_interior_boundary_synergy_certificate`, `cross_contact_gauge_no_ghost_countermodel`)**:
   On $h(t) = P_3(2t)$ ($\|h'\|_2^2 = 24$), the interior observer $\mathcal{O}_{\mathrm{int}}(c_1, c_2)$ sees $0$ and the boundary observer $\mathcal{O}_{\mathrm{bdry}}(E_0)$ sees $4$, whereas their join $\mathcal{O}_{\mathrm{int}} \vee \mathcal{O}_{\mathrm{bdry}}$ recovers $M_3 = 12(E_0 - 5c_1) = 24$ and captures $100\%$ of $\|h'\|_2^2 = 24$ ($24 > 0 + 4$). Conversely, stitching $c_1$ from contact gauge $c=1$ with $E_0$ from gauge $c=-1$ on $K_{1/2} u_1$ fabricates a ghost moment $M_{3,\mathrm{ghost}} = -4$ with apparent energy $7/10 > 1/30 = \|h'\|_2^2$, violating Bessel's inequality.
3. **Agent K — Tate/Connes Single-Moment Contact Rigidity (`PDQ-13`, `single_moment_contact_rigidity_certificate`)**:
   While off-identity prime wavefronts are blind to $W_c = W + c\delta_0$ ($G_{a,c} = G_a + c K_a$), the identity $(K_a u)' = -Vu$ diagonalizes the mixed derivative pairing $M_{k,i}(K_a) = \langle u_k', (K_a u_i)' \rangle = \frac{2a}{2k+1}\delta_{k,i}$. Thus all off-diagonal moments $M_{k,i}$ ($k \ne i$, including $M_{3,1}, M_{4,2}$) are strict contact-gauge invariants, and $c = \frac{3}{2a}(M_{1,1}(G_{a,c}) - M_{1,1}(G_a))$ is uniquely pinned by a single moment.
4. **Agent G — SUCC × FUCC Categorical Arithmetic (`PDQ-14`, `fucc_fractional_gamma_braid_certificate`, `fucc_self_carry_braid_certificate`, `fucc_succ_functoriality_obstructions`)**:
   Proves the affine braid step-cocycle $\Omega_p(n) = D_p(n+1)/D_p(n)$ and Gauss–Legendre $p$-torsion factorization of $D_p(n) = (pn)!/(n!)^p$, the Frobenius scale invariance $c_p(p, p^k n) = s_p(n)$ and Kummer step-valuation law $\Delta_S c_p(p, n) = 1 - (p-1)v_p(n+1)$, and three exact functoriality obstructions (carry defect, factorial non-additivity, and composite $n=6$ single-prime slice leakage).
5. **Agent H — Finite Spectral Resonance (`PDQ-14`, `odd_bubble_offline_pair_certificate`, `even_sector_small_window_submersion_certificate`, `delayed_detection_aliasing_countermodels`)**:
   Establishes that the off-critical quadruplet $\{\frac{1}{2}\pm\Delta\pm i\gamma\}$ contributes the **indefinite** real form $Z = 4\operatorname{Re}\!\big((Lf_{\mathrm{even}})(z)^2 - (Lf_{\mathrm{odd}})(z)^2\big)$, $z=\Delta+i\gamma$ (a real-part-of-a-**square**, *not* a modulus-square), of overall inertia $(2,2)$. **CORRECTION:** neither reflection-parity sector is sign-definite — the earlier "every even test $\ge 0$ / every odd test $\le 0$" claim is **refuted** (an interval-certified even bump gives $4\operatorname{Re}(E^2)<0$; the named default odd bubble gives $+9.3\times10^{-5}>0$ at $\gamma=14$). The $(2,2)$ split is the **real-vs-imaginary transform** axis $\{\operatorname{Re}E,\operatorname{Im}O\}$ (+) / $\{\operatorname{Im}E,\operatorname{Re}O\}$ (−), each parity sector being $(1,1)$; off-critical indefiniteness is precisely the obstruction a spectral RH attack must confront (on-line $|F|^2$ positivity does not persist). Also: a bandwidth-$T$ even-sector non-resolution bound ($O(a^7\Delta^2\gamma^2)$ signal below *this certificate's* $\delta_a(T)$ error allowance — instrument-relative, **not** universal undetectability; the signal re-emerges at larger $T$), and three aliasing countermodels including the strictly negative fourth cumulant $\kappa_4 = -4\Delta^2\gamma^2 < 0$.
6. **Agent I — SUCC × YEAN Division-Free Proof Capsules (`PDQ-14`, `build_rational_ldlt_schur_capsule`, `verify_rational_ldlt_schur_capsule`)**:
   Implements `SUCC_YEAN_RATIONAL_SCHUR_CAPSULE_v1`, checking $P M P^T = L D L^T$ and Schur complement certificates $X D_{\mathrm{high}} = B, A - X B^T = S$ using pure ring additions/multiplications (zero division in the verifier), enforcing canonical FQID resolution via `CLAIM_NAMESPACE_REGISTRY.json`, and separating finite matrix verification from infinite-dimensional analytic premises.
