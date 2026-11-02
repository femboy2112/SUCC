# Operation Prime-Cofactor Non-Conspiracy & Five-Front Theorem-Building Mega-Round (2026-11-02)

**Branch:** `research/prime-cofactor-nonconspiracy-2026-11-02` (stacked on `origin/main` commit `81045770234a114247e43eb08ae5c6d446e9514a`, Operation Main XIX).  
**Executable Oracles:** [`mega_round_engine.py`](mega_round_engine.py), [`independent_oracle.py`](independent_oracle.py), [`PrimeCofactorCore.lean`](PrimeCofactorCore.lean), and [`../../tests/test_prime_cofactor_nonconspiracy.py`](../../tests/test_prime_cofactor_nonconspiracy.py).

---

## 0. Epistemic Firewall & Source Contract

Throughout this document, the **authentic four-pole BBP recurrence** is held strictly invariant:
$$r(n) = \frac{4}{8n-7} - \frac{2}{8n-4} - \frac{1}{8n-3} - \frac{1}{8n-2} = \frac{120n^2 - 89n + 16}{(2n-1)(4n-1)(8n-7)(8n-3)}, \qquad U_0 = 0, \qquad U_{n+1} = 16 U_n + r(n+1),$$
with circle projection $x_n = \{U_n\} \in \mathbb{R}/\mathbb{Z}$ and additive character $e(z) = e^{2\pi i z}$.

> **Firewall Declaration (All OPEN):**
> - Base-16 and base-3 normality of $\pi$: **OPEN**.
> - All-horizon signed Weyl gate $S_N(h) = \sum_{n=1}^N e(h U_n(0)) = o(N)$ for every fixed $h \in \mathbb{Z}\setminus\{0\}$: **OPEN**.
> - Joint prime-cofiber non-conspiracy inequality (`NET-XVII-2` / `SPP-10`): **OPEN** (reformulated here as an exact bilinear DFT/Gauss-sum pairing with unconditional DC-mean suppression, not proved to cancel oscillatory cofiber mode-locking).
> - Riemann Hypothesis (RH), Weil positivity ($\neq$ positive Gram covariance), general Collatz conjecture, and shifted Lonely Runner $n=18..94$: **OPEN**.

---

## Front 1: Exact $p$-Adic Cofiber Recurrence, Midy Complementarity, Bilinear Twisted-Gauss Bound, and Higher-Octave Stroboscope (`PCN-01`..`PCN-04`)

### Theorem 1 (`PCN-01` — Exact $p$-Adic Cofiber Recurrence & Hexadecimal Carry-Digit Law)
- **Status:** `PROVED LOCAL` (paper proof + exact `Fraction` oracle + standalone Lean 4 kernel theorems `primary_step_euclidean`, `primary_carry_lt_sixteen`, `scaled_cofiber_step_identity` in [`PrimeCofactorCore.lean`](PrimeCofactorCore.lean)).
- **Domain & Hypotheses:** Let $p > 5$ be a prime with $p \equiv 1 \pmod 4$. Let
  $$b_p = \begin{cases} (p+7)/8 & \text{if } p \equiv 1 \pmod 8, \\ (p+3)/8 & \text{if } p \equiv 5 \pmod 8 \end{cases}, \qquad J_p = \frac{p+1}{2}, \qquad c_p = \begin{cases} 4 & \text{if } p \equiv 1 \pmod 8, \\ p-1 & \text{if } p \equiv 5 \pmod 8. \end{cases}$$
  For every integer $j$ in the single-pole interval $b_p \le j \le J_p - 1$, define the canonical primary residue and cofiber rational state:
  $$a_{p,j} := \left(c_p 16^{j - b_p}\right) \bmod p \in \{1, \dots, p-1\}, \qquad W_{p,j} := U_j - \frac{a_{p,j}}{p} \in \mathbb{Q}.$$
- **Claim:**
  1. **(Strict $p$-Local Integrality):** For every $b_p \le j \le J_p - 1$, $W_{p,j} \in \mathbb{Z}_{(p)}$ ($p \nmid \operatorname{den}(W_{p,j})$), with birth value
     $$W_{p, b_p} = 16 U_{b_p - 1} + \left(r(b_p) - \frac{\tilde{c}_p}{p}\right) - \mathbf{1}_{p \equiv 5 \pmod 8}, \qquad \tilde{c}_p \in \{4, -1\}.$$
  2. **(Exact Cofiber Recurrence & Hexadecimal Carry-Digit Law):** For every $b_p \le j < J_p - 1$,
     $$\boxed{W_{p, j+1} = 16 W_{p,j} + r(j+1) + \kappa_{p,j}, \qquad \kappa_{p,j} := \frac{16 a_{p,j} - a_{p,j+1}}{p} = \left\lfloor \frac{16 a_{p,j}}{p} \right\rfloor \in \{0, 1, \dots, 15\},}\tag{1.1}$$
     where $\kappa_{p,j}$ is the exact $(j - b_p + 1)$-th hexadecimal digit of the proper fraction $\frac{a_{p, b_p}}{p} \in (0, 1)$.
  3. **(Circle Decoupling Law):** On the circle $\mathbb{R}/\mathbb{Z}$, the integer carry $\kappa_{p,j} \in \mathbb{Z}$ vanishes modulo $1$:
     $$\boxed{W_{p, j+1} \equiv 16 W_{p,j} + r(j+1) \pmod 1 \qquad (b_p \le j < J_p - 1).}\tag{1.2}$$
     That is, after the single punctured step $b_p$, the cofiber circle projection $\{W_{p,j}\}$ evolves under the bare BBP map with zero $p$-dependence across the entire single-pole window.
- **Proof:**
  At $j = b_p$, $p$ divides exactly one pole denominator ($8b_p - 7 = p$ if $p \equiv 1 \pmod 8$, or $8b_p - 3 = p$ if $p \equiv 5 \pmod 8$), and for $b_p < n < J_p = (p+1)/2$, all four pole denominators $8n-7, 2n-1, 8n-3, 4n-1$ are coprime to $p$, so $r(n) \in \mathbb{Z}_{(p)}$. By Euclidean division, $16 a_{p,j} = p\kappa_{p,j} + a_{p, j+1}$ with $\kappa_{p,j} = \lfloor 16 a_{p,j}/p \rfloor \in \{0,\dots,15\}$ since $1 \le a_{p,j} \le p-1$. Subtracting $\frac{a_{p,j+1}}{p} = \frac{16 a_{p,j}}{p} - \kappa_{p,j}$ from $U_{j+1} = 16 U_j + r(j+1)$ yields
  $$W_{p, j+1} = U_{j+1} - \frac{a_{p,j+1}}{p} = 16\left(U_j - \frac{a_{p,j}}{p}\right) + r(j+1) + \kappa_{p,j} = 16 W_{p,j} + r(j+1) + \kappa_{p,j},$$
  preserving $W_{p, j+1} \in \mathbb{Z}_{(p)}$ by induction and reducing modulo $1$ to (1.2). $\blacksquare$

---

### Theorem 1B (`PCN-02` — Midy Hexadecimal Carry-Complementarity & Half-Period $p$-Annihilation)
- **Status:** `PROVED LOCAL` (paper proof + exact `Fraction` oracle + standalone Lean 4 kernel theorems `complementary_div_mod_fifteen`, `midy_hex_carry_complement_fifteen`, `half_period_primary_annihilation` in [`PrimeCofactorCore.lean`](PrimeCofactorCore.lean)).
- **Domain & Hypotheses:** Let $p > 5, p \equiv 1 \pmod 8$ have even multiplicative order $L = \operatorname{ord}_p(16) = 2M$ ($M \ge 1$) with $b_p + M \le J_p - 1$ (e.g., $p = 17, 97, 241, 257$).
- **Claim:** For every $b_p \le j \le J_p - 1 - M$:
  1. **(Complementary Primary Residues & Hex Digits):**
     $$\boxed{a_{p, j+M} = p - a_{p,j}, \qquad \kappa_{p,j} + \kappa_{p, j+M} = 15.}\tag{1.3}$$
  2. **(Exact Half-Period $p$-Primary Annihilation):**
     $$\boxed{U_j + U_{j+M} = W_{p,j} + W_{p, j+M} + 1 \in \mathbb{Z}_{(p)}, \qquad v_p\left(U_j + U_{j+M}\right) \ge 0,}\tag{1.4}$$
     and for every $h \in \mathbb{Z}$, the two half-period character vectors combine into the real-modulated cofiber pair:
     $$\boxed{e(h U_j) + e(h U_{j+M}) = 2\,e\!\left(h\,\frac{W_{p,j} + W_{p,j+M}}{2}\right) \cos\!\left(2\pi h\left(\frac{W_{p,j} - W_{p,j+M}}{2} + \frac{a_{p,j}}{p}\right)\right).}\tag{1.5}$$
- **Proof:**
  Since $L = \operatorname{ord}_p(16) = 2M$ is even in $\mathbb{F}_p^\times$, $16^M \equiv -1 \pmod p$, so $a_{p, j+M} \equiv -a_{p,j} \pmod p$, forcing $a_{p, j+M} = p - a_{p,j} \in \{1,\dots,p-1\}$. Dividing $(16 a_{p,j}) + (16 a_{p, j+M}) = 16p$ by $p$ with remainders $a_{p, j+1} + a_{p, j+M+1} = p$ gives $\kappa_{p,j} + \kappa_{p, j+M} = 16 - 1 = 15$. Adding $U_j = W_{p,j} + a_{p,j}/p$ and $U_{j+M} = W_{p, j+M} + (p - a_{p,j})/p$ cancels the $1/p$ poles to $+1 \in \mathbb{Z}$, proving (1.4)–(1.5). $\blacksquare$

---

### Theorems 2 & 3 (`PCN-03` — Bilinear DFT Cofiber-Erosion Identity & Twisted Subgroup Gauss Bound for `NET-XVII-2`)
- **Status:** `PROVED LOCAL` (paper proof + exact numerical/DFT verification in [`mega_round_engine.py`](mega_round_engine.py)).
- **Domain & Hypotheses:** Let $p > 5, p \equiv 1 \pmod 4$ have $L = \operatorname{ord}_p(16)$, coset index $m = (p-1)/L$, and $b_p + L - 1 < J_p$. For $0 \le r < L - 1$, let $\delta_{p, r} := W_{p, b_p + r + 1} - W_{p, b_p + r}$ be the cofiber step increment, $D_{p,h}(r) := e(h\delta_{p,r}) - 1$ (with $D_{p,h}(L-1) := 0$), $\widehat{D}_{p,h}(\ell) = \frac{1}{L}\sum_{r=0}^{L-1} D_{p,h}(r) e(-\ell r / L)$ its discrete Fourier transform on $\mathbb{Z}/L\mathbb{Z}$, and
  $$G_p(\alpha, \ell) := \sum_{r=0}^{L-1} e_p\!\left(\alpha 16^r\right) e\!\left(\frac{\ell r}{L}\right) \qquad (\alpha \in \mathbb{F}_p^\times,\ \ell \in \mathbb{Z}/L\mathbb{Z})$$
  the **twisted subgroup Gauss sum** on $H_p = \langle 16 \rangle \le \mathbb{F}_p^\times$.
- **Claim:**
  1. **(Exact Bilinear Plancherel Identity for `NET-XVII-2`):** The true vs. primary-only step-lag discrepancy $E_p(h) - \widetilde{E}_p(h) := \frac{1}{L-1}\Re\sum_{r=0}^{L-2}\left(e(h(U_{b_p+r+1}-U_{b_p+r})) - e_p(15 c_p h 16^r)\right)$ satisfies:
     $$\boxed{E_p(h) - \widetilde{E}_p(h) = \frac{1}{L-1}\Re \sum_{\ell=0}^{L-1} \widehat{D}_{p,h}(\ell)\,G_p(15 c_p h, \ell), \qquad \sum_{\ell=0}^{L-1} \left|G_p(\alpha, \ell)\right|^2 = L^2.}\tag{1.6}$$
  2. **(Uniform Twisted Subgroup Gauss Bound):** For every $\alpha \in \mathbb{F}_p^\times$ and every harmonic $\ell \in \mathbb{Z}/L\mathbb{Z}$:
     $$\boxed{\left|G_p(\alpha, \ell)\right| \le \sqrt{p} \quad (\forall \ell \in \mathbb{Z}/L\mathbb{Z}), \qquad \left|G_p(\alpha, 0)\right| \le \frac{(m-1)\sqrt{p} + 1}{m} < \sqrt{p}.}\tag{1.7}$$
  3. **(Unconditional DC-Mean Suppression & Mode-Locking Localization):** Letting $\mu_2(h) := \frac{1}{L-1}\sum_{r=0}^{L-2} \sin^2(\pi h \delta_{p,r})$, the $\ell = 0$ (mean) cofiber contribution to $|E_p(h) - \widetilde{E}_p(h)|$ is unconditionally bounded by $\frac{2\sqrt{\mu_2(h)}\left((m-1)\sqrt{p}+1\right)}{m L} = O(\sqrt{p}/L)$, while the oscillatory ($\ell \ne 0$) contribution is bounded by $2\sqrt{\frac{L}{L-1}\mu_2(h)}$.
- **Proof:**
  Since $U_{b_p+r+1} - U_{b_p+r} \equiv \frac{15 c_p 16^r}{p} + \delta_{p,r} \pmod 1$, factoring out $e_p(15 c_p h 16^r)$ and expanding $D_{p,h}(r) = \sum_{\ell=0}^{L-1} \widehat{D}_{p,h}(\ell) e(\ell r / L)$ proves (1.6). Extending the multiplicative character $\psi_\ell(16^r) = e(\ell r / L)$ of $H_p$ to the $m$ characters $\chi_1, \dots, \chi_m$ of $\mathbb{F}_p^\times$ extending $\psi_\ell$ gives $G_p(\alpha, \ell) = \frac{1}{m}\sum_{s=1}^m \overline{\chi_s(\alpha)}\,\tau(\chi_s)$. Since $|\tau(\chi)| = \sqrt{p}$ for every non-trivial character $\chi$ of $\mathbb{F}_p^\times$ and $\tau(\chi_0) = -1$, the triangle inequality gives (1.7). $\blacksquare$

---

### Theorem 4 (`PCN-04` — Higher-Octave $4k$-Checkpoint Quadratic Reciprocity Stroboscope)
- **Status:** `PROVED LOCAL` (paper proof + exact `Fraction` verification in [`mega_round_engine.py`](mega_round_engine.py) + Lean 4 theorems `stroboscope_involution_square`, `stroboscope_fixed_iff_bbp_ratio`, `first_octave_synchronization_47_15` in [`PrimeCofactorCore.lean`](PrimeCofactorCore.lean)).
- **Domain & Hypotheses:** Fix $k \ge 1$ and any prime $p > \max(5, 8k - 2)$ with $p \equiv 1 \pmod 4$. Let $N_p(k) := \frac{(4k-1)p + 1}{4}$, and in octave $l \in \{1, \dots, k\}$, let the four pole-hit steps be $j_l^{(m)} = (l-1)p + h_p^{(m)}$ ($m=1,2,3,4$), where
  $$\left(h_p^{(1)}, h_p^{(2)}, h_p^{(3)}, h_p^{(4)}\right) = \begin{cases} \left(\frac{p+7}{8},\, \frac{p+1}{2},\, \frac{5p+3}{8},\, \frac{3p+1}{4}\right) & \text{if } p \equiv 1 \pmod 8, \\[4pt] \left(\frac{p+3}{8},\, \frac{p+1}{2},\, \frac{5p+7}{8},\, \frac{3p+1}{4}\right) & \text{if } p \equiv 5 \pmod 8. \end{cases}$$
- **Claim:**
  1. **(Universal Octave Checkpoint Law):** Let $C_l^{(m)} := 16^{j_l^{(4)} - j_l^{(m)}} a_{p, j_l^{(m)}} \bmod p$ be the primary residue at the $m$-th hit of octave $l$ referenced to the octave checkpoint $j_l^{(4)} = \frac{(4l-1)p + 1}{4}$, and let $r^{(m)}(l)$ be the cumulative $m$-pole forcing at index $l$. Then **for both $p \equiv 1 \pmod 8$ and $p \equiv 5 \pmod 8$, and for every octave $1 \le l \le k$ and every hit $m \in \{1, 2, 3, 4\}$**:
     $$\boxed{C_l^{(m)} \equiv 16 U_{l-1} + r^{(m)}(l) \pmod p, \qquad C_l^{(4)} \equiv U_l \pmod p.}\tag{1.8}$$
     In instantaneous (unshifted) coordinates $a_{p, j_l^{(m)}} \bmod p$, the four hits in octave $l$ equal $\left(C_l^{(1)}, C_l^{(2)}, C_l^{(3)}, U_l\right)$ for $p \equiv 1 \pmod 8$ and $\left(-\frac{1}{4}C_l^{(1)}, C_l^{(2)}, -4 C_l^{(3)}, U_l\right) \pmod p$ for $p \equiv 5 \pmod 8$.
  2. **(Higher-Octave Pole Cancellation Criterion & $p=73, k=4$ Resonance Witness):** For every $1 \le l \le k$, $v_p\big(U_{j_l^{(4)}}\big) \ge 0$ if and only if $p \mid \operatorname{num}(U_l)$. In particular, at $k=4$, $\operatorname{num}(U_4) = 1428806141948 = 2^2 \cdot 3 \cdot 73 \cdot 1631057239$, so $p = 73 > 30$ has $v_{73}(U_{55}) = v_{73}(U_{128}) = v_{73}(U_{201}) = -1$ at octaves $l=1,2,3$, and **exact $73$-adic pole cancellation $v_{73}(U_{274}) = 0$** at octave $l=4$!
- **Proof:**
  Since $p > 8k - 2$, $p^2 > 8 N_p(k)$, so every multiple $q p$ dividing a pole denominator has $v_p = 1$. For $p \equiv 1 \pmod 8$, $2^{(p-1)/2} \equiv 1 \pmod p$, so $16^{j_l^{(4)} - j_l^{(m)}} \equiv (1, 1, 1, 1) \pmod p$ and the four hits in octave $l$ have denominators $((8l-7)p, (8l-4)p, (8l-3)p, (8l-2)p)$ with weights $(4, -2, -1, -1)$, adding $r^{(m)}(l)$ to $16^p U_{j_{l-1}^{(4)}} \equiv 16 U_{l-1} \pmod p$. For $p \equiv 5 \pmod 8$, $2^{(p-1)/2} \equiv -1 \pmod p$, so $16^{j_l^{(4)} - j_l^{(m)}} \equiv (-4, 1, -1/4, 1) \pmod p$, while the 1st and 3rd hits occur at $8j_l^{(1)} - 3 = (8l-7)p$ (weight $-1$) and $8j_l^{(3)} - 7 = (8l-3)p$ (weight $+4$). Multiplying $(-4)\cdot \frac{-1}{8l-7} = +\frac{4}{8l-7}$ and $(-\frac{1}{4})\cdot \frac{+4}{8l-3} = -\frac{1}{8l-3}$ restores the exact cumulative forcing $r^{(m)}(l) \pmod p$ at every hit $m=1,2,3,4$! $\blacksquare$

---

## Front 2: Parametric Effective Diophantine Thresholds & Universal Radix-$B$ Coercivity (`PCN-05`..`PCN-08`)

### Theorem 2A (`PCN-05` & `PCN-06` — Parametric Effective Thresholds $J_0(C, \mu)$ and $J_2(C, \mu)$)
- **Status:** `PROVED LOCAL` (paper proof + exact `Fraction` oracle in [`mega_round_engine.py`](mega_round_engine.py) + Lean 4 theorem `two_step_direct_and_decimal_hex_enclosure` in [`PrimeCofactorCore.lean`](PrimeCofactorCore.lean)).
- **Domain & Hypotheses:** Suppose $\pi$ satisfies the effective Diophantine inequality $|\pi - p/q| \ge C q^{-\mu}$ for all integers $p, q$ with $q \ge q_0 \ge 1$, where $0 < C \le 1$ and $2 \le \mu < \frac{16384}{2051} \approx 7.988298$.
- **Claim:**
  1. **(Closed-Form Threshold Functions $\Phi_{\mathrm{strict}}(C, \mu)$ and $\Phi_{\mathrm{band}}(C, \mu)$):** Define
     $$\boxed{\Phi_{\mathrm{strict}}(C, \mu) := \frac{2048\log_{16}(1/C) + 2048\mu + 1024}{16384 - 2051\mu}, \qquad \Phi_{\mathrm{band}}(C, \mu) := \frac{2048\log_{16}(1/C) - 1024(\mu - 1)}{16384 - 2051\mu},}\tag{2.1}$$
     and for any integer $j$, set $\lfloor x \rfloor_{\mathrm{strict}} + 1 := \lfloor x \rfloor + 1$ (the smallest integer strictly greater than $x$). Then the Stage `#304` and Stage `#321` (`GlobalSigned.lean`) all-$N$ logarithmic saving bounds hold unconditionally for all $j \ge J_0(C, \mu) := \max\big(2, \lfloor \Phi_{\mathrm{strict}}(C, \mu) \rfloor + 1\big)$ and $j \ge J_2^{\mathrm{strict}}(C, \mu) := \max\big(4, \lfloor \Phi_{\mathrm{strict}}(C, \mu) \rfloor + 1\big)$ respectively. Moreover, if finite-band non-vanishing is certified through block $J_{\mathrm{cert}} \ge 3$ and $\lfloor \Phi_{\mathrm{band}}(C, \mu) \rfloor + 1 \le J_{\mathrm{cert}} + 1$, then $J_2^{\mathrm{band}}(C, \mu) = 4$.
  2. **(Discharge of the Stage `#304` / `#321` Unit-Constant Threshold Debt):** Under the unit-constant hypothesis $C = 1$ ($\log_{16}(1/C) = 0$) for any $\mu \in [2, 15/2]$:
     - Since $\Phi_{\mathrm{band}}(1, \mu) = -\frac{1024(\mu-1)}{16384 - 2051\mu} < 0 < 2$, combining with the already-committed finite-band certificates on $j \in \{2, 3\}$ (`test_pi_selected_phase_forge.py` / `test_global_branch_coercivity.py`) discharges $J_0^{\mathrm{band}}(1, \mu) = 2$ and $J_2^{\mathrm{band}}(1, \mu) = 4$.
     - Without any finite-band certificate beyond $j \ge 2$, $\Phi_{\mathrm{strict}}(1, 15/2) = \frac{32768}{2003} \approx 16.3595 \implies J_2^{\mathrm{strict}}(1, 15/2) = 17$, and at Salikhov's $\mu = 7.6063$, $\Phi_{\mathrm{strict}}(1, 7.6063) = \frac{166017024}{7834787} \approx 21.1897 \implies J_2^{\mathrm{strict}}(1, 7.6063) = 22$.
  3. **(Exact Rational Decimal-to-Hexadecimal Enclosure):** Since $10^6 = 1{,}000{,}000 < 1{,}048{,}576 = 16^5$, for any decimal constant $C \ge 10^{-K}$ ($K \ge 0$), $\log_{16}(1/C) \le \frac{5}{6}K \in \mathbb{Q}$.
- **Proof:**
  On block $I_j = [m_j, 8m_j]$ ($m_j = 8^j$), the periodic rational branch denominator is $Q_j = |h P_j(16)|(16^p - 1)16^{m_j}$ with $p = |h|L_j \le 8^{j-1}$. Using $|P_j(16)| < \frac{5}{28} 16^{8^j}$ and $(8m_j + 1)^2 > 64\cdot 16^{(3/2)j}$, the condition that the BBP tail plus branch-approximation error is strictly smaller than $C Q_j^{-\mu}$ reduces upon taking $\log_{16}$ to
  $$\left(8 - \frac{2051}{2048}\mu\right) 8^j > \log_{16}(1/C) + (\mu + 1/2) \quad (\text{strict}), \qquad \left(8 - \frac{2051}{2048}\mu\right) 8^j > \log_{16}(1/C) - \frac{\mu - 1}{2} \quad (\text{band}).$$
  Using $8^j \ge 8j$ for $j \ge 1$ and multiplying by $256$ yields (2.1). $\blacksquare$

---

### Theorem 2B (`PCN-07` & `PCN-08` — Variational Duality of Universal Radix-$B$ Coercivity)
- **Status:** `PROVED LOCAL` (paper proof + exact `Fraction` oracle + Lean 4 kernel theorems `universal_radix_square_gap`, `universal_radix_total_weight`, `radix_weight_minimality_gap`, `pairwise_radix_square_gap`, `adjacent_branch_norm_unification`, `two_step_direct_and_decimal_hex_enclosure` in [`PrimeCofactorCore.lean`](PrimeCofactorCore.lean)).
- **Domain & Hypotheses:** Let $B \ge 2$ be any integer radix, $a, b \in \mathbb{R}$ (or $\mathbb{Z}$), and $\alpha > 0$.
- **Claim:**
  1. **(Trajectory-Summed $\ell_1$-Variational Minimum $\Lambda_{\mathrm{sum}}(B) = (B+1)^2$):** In the family of valid one-step radix-$B$ transport bounds $(a + B b)^2 \le u(\alpha) a^2 + v(\alpha) b^2$ with $u(\alpha) = 1 + \alpha$ and $v(\alpha) = B^2(1 + 1/\alpha)$, the trajectory-summed weight $W_B(\alpha) := u(\alpha) + v(\alpha)$ satisfies the exact identity
     $$\boxed{W_B(\alpha) - (B+1)^2 = \frac{(\alpha - B)^2}{\alpha} \ge 0,}\tag{2.2}$$
     uniquely minimized at $\alpha^* = B$, where $u^*(B) = B+1$, $v^*(B) = B(B+1)$, $\Lambda_{\mathrm{sum}}(B) = (B+1)^2$, and
     $$\boxed{(B+1)a^2 + B(B+1)b^2 - (a + B b)^2 = B(a - b)^2.}\tag{2.3}$$
     At $B = 16$, $(u^*, v^*, \Lambda_{\mathrm{sum}}) = (17, 272, 289)$, recovering `formal/GlobalSigned.lean`.
  2. **(Pairwise $\ell_\infty$-Balanced Minimum $\Lambda_{\mathrm{pair}}(B) = B^2 + 1$ & Operator Norm Unification):** Minimizing $\max(u(\alpha), v(\alpha))$ uniquely forces $\alpha^{**} = B^2$, where $u(\alpha^{**}) = v(\alpha^{**}) = B^2 + 1 =: \Lambda_{\mathrm{pair}}(B)$ ($257$ at $B=16$), with exact Lagrangian identity
     $$\boxed{(B^2 + 1)(a^2 + b^2) - (a - B b)^2 = (B a + b)^2,}\tag{2.4}$$
     and the squared Frobenius norm of the `#311` adjacent-branch operator matrix $\mathcal{M}_B = \begin{pmatrix} 1 & -(B+1) & B \\ 1 & 0 & 0 \end{pmatrix}$ unifies the two constants:
     $$\boxed{\|\mathcal{M}_B\|_F^2 - 1 = 1^2 + (B+1)^2 + B^2 = \Lambda_{\mathrm{pair}}(B) + \Lambda_{\mathrm{sum}}(B) \qquad (257 + 289 = 546 \text{ at } B=16).}\tag{2.5}$$
  3. **(Direct $k$-Step vs. Iterated 1-Step Transport Theorem):** For every step span $k \ge 2$ and radix $B \ge 2$, direct $k$-step radix-$B^k$ transport $\Lambda_{\mathrm{sum}}(B^k) = (B^k + 1)^2$ strictly beats iterated 1-step transport $(B+1)^2 \left(\frac{B^k - 1}{B - 1}\right)^2$ by the exact positive integer gap:
     $$\boxed{(B+1)^2 \left(\frac{B^k - 1}{B - 1}\right)^2 - (B^k + 1)^2 = \frac{4(B^k - B)(B^{k+1} - 1)}{(B - 1)^2} > 0 \qquad (\text{at } B=16, k=2:\ 83521 - 66049 = 17472).}\tag{2.6}$$
- **Proof:**
  All four polynomial identities (2.2)–(2.6) hold over $\mathbb{Z}$ by direct ring expansion and are kernel-certified in [`PrimeCofactorCore.lean`](PrimeCofactorCore.lean). $\blacksquare$

---

## Front 3: All-Order Laurent Clock Dyadic Collapse, Gevrey-1 Super-Asymptotics, Two-Sided Fejér Repair, and Zero-Seed Discriminators (`PCN-09`..`PCN-12`)

### Theorem 3A (`PCN-09` & `PCN-10` — Aurifeuillian Dyadic Denominator Collapse, Strict Alternating Remainder Sandwich, and Gevrey-1 Optimal Truncation $d_*(n)$)
- **Status:** `PROVED LOCAL` (paper proof + 3-way independent exact `Fraction` / Stirling / Eulerian verification in [`mega_round_engine.py`](mega_round_engine.py) & [`independent_oracle.py`](independent_oracle.py) + Lean 4 theorems `laurent_pole_dominance_all_orders`, `laurent_egf_aurifeuillian_at_one`, `laurent_dyadic_numerators_first_six` in [`PrimeCofactorCore.lean`](PrimeCofactorCore.lean)).
- **Domain & Hypotheses:** For $d \ge 1, k \ge 1, n > 0$, let $F_{n,k} = \sum_{j=1}^k 16^{k-j} r(n+j)$, $F^{[d]}_{n,k} = \sum_{m=1}^{d-1} \frac{16^k c_{m,k}}{n^{m+1}}$, $R^{[d]}_{n,k} = F_{n,k} - F^{[d]}_{n,k}$, $c_{d,k} = \sum_{j=1}^k 16^{-j} \sum_{a=1}^4 \frac{w_a}{8}(p_a - j)^d$, and $c_d = \lim_{k\to\infty} c_{d,k}$.
- **Claim:**
  1. **(Aurifeuillian $15$-Cancellation & Odd-Integer Dyadic Numerator Law):** The Exponential Generating Function $\mathcal{C}(z) = \sum_{d=0}^\infty c_d \frac{z^d}{d!} = \frac{4e^{7z/8} - 2e^{4z/8} - e^{3z/8} - e^{2z/8}}{8(16e^z - 1)}$ factors in $t = e^{z/8}$ via the shared Aurifeuillian divisor $P_{\mathrm{aur}}(t) = (2t^2+1)(2t^2+2t+1)$ (which equals $3 \times 5 = 15$ at $t=1$):
     $$\boxed{\mathcal{C}(z) = \frac{t^2(t-1)P_{\mathrm{aur}}(t)}{8(2t^2-1)(2t^2-2t+1)P_{\mathrm{aur}}(t)} = \frac{1}{32}\left(\frac{2t-1}{2t^2-2t+1} - \frac{1}{2t^2-1}\right), \qquad t = e^{z/8}.}\tag{3.1}$$
     Consequently, all factors of $3$ and $5$ cancel identically across the four BBP poles: for every $d \ge 1$, $\tilde{c}_d := 8^{d+1} c_d \in 2\mathbb{Z} + 1$ is an **odd integer** ($\operatorname{den}(c_d) = 8^{d+1}$ in lowest terms), satisfying the exact integer recurrence
     $$\boxed{\tilde{c}_d = (3^d - 2^d) - \sum_{m=1}^{d-1} \binom{d}{m}\left(2 - 4\cdot 3^{d-m} + 4\cdot 4^{d-m}\right)\tilde{c}_m.}\tag{3.2}$$
  2. **(Strict Alternating Sign & Stieltjes Remainder Sandwich):** For every $n > 0, k \ge 1, d \ge 1$, $(-1)^{d+1} R^{[d]}_{n,k} > 0$, and $R^{[d]}_{n,k}$ is strictly bracketed by:
     $$\boxed{\max\!\left(0,\, \frac{|c_{d,k}|}{n^{d+1}} - \frac{|c_{d+1,k}|}{n^{d+2}}\right) < 16^{-k}\left|R^{[d]}_{n,k}\right| < \frac{|c_{d,k}|}{n^{d+1}} < \frac{|c_d|}{n^{d+1}}.}\tag{3.3}$$
  3. **(Gevrey-1 Factorial Growth & Super-Asymptotic Optimal Truncation $d_*(n)$):** The Borel transform $\mathcal{C}(z)$ has nearest simple pole at $z_0 = -\ln 16$ with residue $-\frac{1}{8}$ (and vanishing residues at $z_m = -\ln 16 + 2\pi i m$ for $m \equiv 2, 3, 5, 6 \pmod 8$), giving the exact factorial asymptotic
     $$\boxed{c_d = (-1)^{d+1}\frac{d!}{8(\ln 16)^{d+1}}\left(1 + \delta_d\right), \qquad |\delta_d| \le 4\left(1 + \frac{4\pi^2}{(\ln 16)^2}\right)^{-(d+1)/2}.}\tag{3.4}$$
     Thus the formal all-order Laurent series is **Gevrey-1 divergent**, and truncating at the **optimal super-asymptotic order** $d_*(n) := \lfloor n \ln 16 \rfloor$ minimizes $\frac{|c_d|}{n^{d+1}}$ and achieves an exponentially small remainder for all $k \ge 1$:
     $$\boxed{16^{-k}\left|R^{[d_*(n)]}_{n,k}\right| < \frac{|c_{d_*(n)}|}{n^{d_*(n)+1}} = O\!\left(n^{-1/2} 16^{-n}\right).}\tag{3.5}$$
- **Proof:**
  See Front 3 proof derivation above: polynomial expansion in $t = e^{z/8}$ establishes (3.1); Hurwitz-ring inversion modulo $2$ proves $\tilde{c}_d \equiv 3^d - 2^d \equiv 1 \pmod 2$ and (3.2); strict monotonicity of $t \mapsto \frac{t^d}{n+t}$ on $t > 0$ proves $(-1)^{d+1} R^{[d]}_{n,k} > 0$ and the Stieltjes sandwich (3.3); and Cauchy's residue theorem on $\mathcal{C}(z) z^{-(d+1)}$ together with Stirling's formula at $d_*(n) = \lfloor n \ln 16 \rfloor$ establishes (3.4)–(3.5). $\blacksquare$

---

### Theorem 3B (`PCN-11` — Two-Sided Symmetrized Fejér Identity & Curvature Defect Dichotomy)
- **Status:** `PROVED LOCAL` (paper proof + exact/numerical verification in [`mega_round_engine.py`](mega_round_engine.py)).
- **Domain & Hypotheses:** For $s \in \mathbb{R}$, $N \ge K \ge 2$, $d \ge 1$, $h \in \mathbb{Z}\setminus\{0\}$, let $L^C_{N,K}(h;s)$ and $L^{[d]}_{N,K}(h;s)$ be the true and order-$d$ compensated one-sided Cesàro-Fejér lag scores.
- **Claim:**
  1. **(Two-Sided Fejér Repair of `SZB-02`):** Restoring the $k=0$ diagonal self-correlation weight $\frac{1}{K}$ yields the exact identity
     $$\boxed{\frac{1}{K} + L^{[d]}_{N,K}(h; s) = B_{N,K}(h; s) + \left(L^{[d]}_{N,K}(h; s) - L^C_{N,K}(h; s)\right), \qquad B_{N,K}(h; s) := \frac{1}{N K^2}\sum_{m=1}^{N+K-1}\left|\sum_{j=0}^{K-1} z_{m-j}(s)\right|^2 \ge 0.}\tag{3.6}$$
     This explains why the one-sided score $L^{[d]}_{N,K}(h; 0) = B_{N,K}(h; 0) - \frac{1}{K} + o(1)$ in `SZB-02` takes small negative values in $[-\frac{1}{K}, 0)$ when $B_{N,K}(h; 0) < \frac{1}{K}$, whereas the two-sided score $\frac{1}{K} + L^{[d]}_{N,K}(h; 0)$ is strictly positive across all tested configurations.
  2. **(Curvature Defect Dichotomy: $s_* = -\pi/16$ vs. $U_0 = 0$):** On the counterseed $s_* = -\pi/16$, $\Delta^{[d]}_{N,K}(h; s_*) := L^C_{N,K}(h; s_*) - L^{[d]}_{N,K}(h; s_*) = \frac{4}{KN}\sum_{k=1}^{K-1}(1-k/K)\sum_{n=1}^{N-k}\sin^2(\pi h R^{[d]}_{n,k}) + O_h(1/N)$ is coherently positive of second order, whereas on $U_0 = 0$ it is modulated by $\cos(2\pi h \Delta x_{n,k})$ and $\sin(2\pi h \Delta x_{n,k})$.
- **Proof:**
  Expanding $\sum_{m} |\sum_{j=0}^{K-1} z_{m-j}|^2 = K N + 2\Re\sum_{k=1}^{K-1}(K-k) C_{h,k}(N;s)$ and applying the trigonometric addition formula to $2\pi h(U_{n+k}(s)-U_n(s) - R^{[d]}_{n,k})$ yields (3.6) and the dichotomy. $\blacksquare$

---

### Theorem 3C (`PCN-12` — Exact Finite-Horizon Zero-Seed vs. Counterseed Discriminators)
- **Status:** `PROVED LOCAL` (paper proof + exact `Fraction` verification in [`mega_round_engine.py`](mega_round_engine.py)).
- **Domain & Hypotheses:** Compare the literal zero-seed orbit $U_n(0) \in \mathbb{Q}$ against any irrational same-forcing counterseed orbit $U_n(q - \pi/16) = 16^n q - T_n$ ($q \in \mathbb{Q}$, and specifically $s_* = -\pi/16$ where $q = 0$).
- **Claim:**
  1. **(Backward Telescopic Recurrence Identity):** For every $n \ge 1$ and $s \in \mathbb{R}$, $16^{-n} U_n(s) - \sum_{j=1}^n 16^{-j} r(j) = s$, which vanishes **if and only if** $s = 0$.
  2. **(Finite-Window Unwrapped & Circle Discriminators):** Both the unwrapped increment excess $\mathcal{I}^\Delta_{n_1,n_2}(s) := \sum_{n=n_1}^{n_2} \max\big(0, U_{n+1}(s) - U_n(s) - \frac{16}{(8n+1)^3}\big)$ and the circle carry-and-distance excess $\mathcal{I}^{\mathbb{T}}_{n_1,n_2}(s) := \sum_{n=n_1}^{n_2} c_n(s)^2 + \sum_{n=n_1}^{n_2} \max\big(0, \|U_n(s)\|_{\mathbb{Z}} - \frac{1}{(8n+1)^2}\big)$ **vanish identically ($\equiv 0$) on $s_* = -\pi/16$ for every window $1 \le n_1 \le n_2$**, and are **strictly positive on $U_0 = 0$** ($\mathcal{I}^\Delta_{n,n}(0) > 46$ for all $n \ge 1$, and $\mathcal{I}^{\mathbb{T}}_{1,n}(0) \ge \frac{11044}{1215} > 9$ for all $n \ge 1$).
  3. **(Active Prime Denominator Support):** Every prime $p > 5$ with $p \equiv 1 \pmod 4$ and $2n < p < 8n$ satisfies $v_p(U_n(0)) = -1$, forcing $\log \operatorname{den}(U_n(0)) \ge 3n + o(n)$.
- **Proof:**
  For $s_* = -\pi/16$, $U_n(s_*) = -T_n \in (-(8n+1)^{-2}, 0)$ has nearest integer $0$, circle carry $c_n(s_*) = 0$, and $0 < U_{n+1}(s_*) - U_n(s_*) = T_n - T_{n+1} < \frac{16}{(8n+1)^3}$, so both invariants vanish term-by-term. On $U_0 = 0$, $U_{n+1}(0) - U_n(0) > 47\cdot 16^{n-1} > \frac{16}{(8n+1)^3}$ and at $n=1$, $U_1(0) = \frac{47}{15} = 3 + \frac{2}{15}$ gives $c_1(0) = 3$ and $\|U_1(0)\|_{\mathbb{Z}} - \frac{1}{81} = \frac{49}{405} > 0$. $\blacksquare$

---

## Front 4: Exact Prime-Power Birth Law, Stratified Spill-Censored Non-Vacuous Transport, and 4-Bit Walsh–Fourier Codec (`PCN-13`..`PCN-15`)

### Theorem 4A (`PCN-13` & `PCN-14` — Exact Three-Progression Prime-Power Birth Law & Non-Vacuous Spill-Censored Transport)
- **Status:** `PROVED LOCAL` (paper proof + exact `Fraction` verification in [`mega_round_engine.py`](mega_round_engine.py) & [`independent_oracle.py`](independent_oracle.py)).
- **Domain & Hypotheses:** Let $Q_n = \operatorname{lcm}_{1\le t\le n} \operatorname{den}(r(t))$ be the cumulative BBP conductor, and decompose the literal carry $c_t = \lfloor U_t \rfloor - 16\lfloor U_{t-1} \rfloor$ for $t \ge 2$ into $c_t = d_{t-1} + s_t^{(1)}$, where $d_{t-1} = \lfloor 16\{U_{t-1}\} \rfloor \in \{0,\dots,15\}$ is the circle hex digit and $s_t^{(1)} = \lfloor \{16 U_{t-1}\} + r(t) \rfloor \in \{0, 1\}$ is the binary forcing spill.
- **Claim:**
  1. **(`PCN-13` — Exact Three-Progression Prime-Power Birth Law):** The pole denominator $2n - 1$ (from $8n - 4$) is **completely redundant** for conductor births: an index $n \ge 1$ is a conductor-birth step ($Q_n > Q_{n-1}$) **if and only if** at least one of the three linear forms $\{8n - 7,\, 8n - 3,\, 4n - 1\}$ is an odd prime power $p^a \ge 3$, with unique birth step $n_{\mathrm{birth}}(p^a) = (p^a+7)/8$ ($p^a \equiv 1 \pmod 8$), $(p^a+3)/8$ ($p^a \equiv 5 \pmod 8$), or $(p^a+1)/4$ ($p^a \equiv 3 \pmod 4$).
  2. **(`PCN-14` — Stratified Spill-Censored Non-Vacuous Transport):** Partitioning $[2, N+1]$ into the dyadic-square refractory shells $I_m = \{k \in [2, N+1] : L_1(k) = \lfloor \log_{16}(4(k-1)^2) \rfloor = m\}$ ($I_0 = \{2\}$ and $I_m = [2^{2m-1}+1, \min(N+1, 2^{2m+1})]$ for $m \ge 1$) bounds the total number of spills in $[2, N+1]$ by
     $$\boxed{K_{N,1} \le K_{N,1}^{\mathrm{strat}} := 1 + \sum_{m \ge 1} \left\lceil \frac{|I_m|}{m + 1} \right\rceil \sim \frac{2N}{\log_2 N},}\tag{4.1}$$
     and with the modular spill kernel $A_h^{\mathrm{spill}} = \sum_{j=1}^{L_h-1} \min(2, \frac{44}{7}\|h/16^j\|_{\mathbb{Z}}) + \frac{44h}{105\cdot 16^{L_h-1}}$ and $B_h^{\mathrm{spill}} = \sum_{j=1}^{L_h-1} j\min(2, \frac{44}{7}\|h/16^j\|_{\mathbb{Z}}) + \frac{44h(15L_h+1)}{1575\cdot 16^{L_h-1}}$ ($L_h = \min\{L \ge 1 : 7\cdot 16^L \ge 22h\}$), the carry-to-digit transport error satisfies
     $$\boxed{\left|a_{N,h}(Y) - a_{N,h}(Y^{\mathrm{digit}})\right| \le \varepsilon_{N,h}^{\mathrm{spill}} := \frac{A_h^{\mathrm{spill}} K_{N,1}^{\mathrm{strat}} + B_h^{\mathrm{spill}}}{N} < 1}\tag{4.2}$$
     across **every** benchmark horizon $N \in \{2^8, 2^{12}, 2^{16}, 2^{32}, 2^{64}, 2^{128}, 2^{256}\}$! At the three canonical frontier horizons $N = 2^{16}, 2^{64}, 2^{256}$ (`PI_SELECTED_CATEGORICAL_FRONTIER.md` §3.1), the maximum mode error drops from the vacuous **`6.1335 / 3.8846 / 1.2520`** of `bbp_sparse_carry_transport.py` down to the strictly sub-unitary **`0.42750 / 0.14537 / 0.04893`** (and at $h=1$: **`0.05090 / 0.01297 / 0.00327`**).
  3. **(Midpoint-Centered Tail-Truncation Reduction):** Centering the nonnegative tail $Z_n - Z_n^{(J)} \in [0, \tau_J]$ at $\frac{1}{2}\tau_J$ leaves $|a_{N,h}(Z^{(J)})|$ and $R_{N,H}(Z^{(J)})$ invariant while reducing `truncation_root_error_squared` by the exact rational factor $\frac{2401}{484} \approx 4.9607\times$ on $Y^{\mathrm{flat}}$ and $\frac{153664}{27225} \approx 5.6442\times$ on $Y^{\mathrm{digit}}$.
- **Proof:**
  See Front 4 proof derivations of Theorems 4A.1, 4A.2, and 4A.3 above. $\blacksquare$

---

### Theorem 4B (`PCN-15` — Exact 4-Block Unitary Fourier–Walsh Decomposition on $\mathbb{Z}/16\mathbb{Z}$)
- **Status:** `PROVED LOCAL` (paper proof + exact verification in [`mega_round_engine.py`](mega_round_engine.py) & [`independent_oracle.py`](independent_oracle.py)).
- **Domain & Hypotheses:** Let $H_N(k) = \#\{1 \le n \le N : d_n = k\}$ ($0 \le k \le 15$) be the 16-cell hexadecimal digit histogram, $M_A(N) = \sum_{k=0}^{15} H_N(k) w_A(k)$ ($A \subseteq \{1,2,3,4\}$) the 16 Walsh moments, and $D_N(h) = \sum_{k=0}^{15} H_N(k) \zeta_{16}^{h k}$ ($h \in \mathbb{Z}/16\mathbb{Z}$) the 16 Discrete Fourier modes.
- **Claim:**
  1. **(Exact Dyadic Shell Selection Rule & 4-Block Unitary Decomposition):** The change-of-basis matrix $\mathcal{T}_{h, A} = \frac{1}{16}\prod_{i\in A}(1 - \zeta_{16}^{h 2^{i-1}})\prod_{i\notin A}(1 + \zeta_{16}^{h 2^{i-1}})$ satisfies
     $$\boxed{\mathcal{T}_{h, A} \ne 0 \quad \Longleftrightarrow \quad \max(A) = 4 - v_2(h) \qquad (1 \le h \le 15,\ \varnothing \ne A \subseteq \{1,2,3,4\}),}\tag{4.3}$$
     decomposing the $15 \times 15$ non-trivial transform into four decoupled unitary blocks $\mathcal{T} = \mathcal{T}^{(1)} \oplus \mathcal{T}^{(2)} \oplus \mathcal{T}^{(3)} \oplus \mathcal{T}^{(4)}$ of dimensions $1 \times 1$, $2 \times 2$, $4 \times 4$, and $8 \times 8$ ($1 + 2 + 4 + 8 = 15$), with exact shell-wise integer Parseval conservation:
     $$\boxed{\sum_{\substack{1 \le h \le 15 \\ v_2(h) = 4 - r}} \left|D_N(h)\right|^2 = \sum_{\substack{A \subseteq \{1,2,3,4\} \\ \max(A) = r}} M_A(N)^2 \in \mathbb{Z}_{\ge 0} \qquad (r = 1, 2, 3, 4).}\tag{4.4}$$
  2. **(Carry-vs-Digit Odometer Defect Bound):** For every subset $A \subseteq \{1,2,3,4\}$, $\frac{1}{N}|\widetilde{M}_A(N) - M_A(N)| \le \frac{2 K_{N,1}}{N} \le \frac{2 K_{N,1}^{\mathrm{strat}}}{N}$ (and on the authentic BBP prefix $1 \le n \le 1000$, $K_{1000,1} = 0$, so $\widetilde{M}_A(N) = M_A(N)$ identically!).
- **Proof:**
  See Front 4 proof derivation of Theorem 4B above. $\blacksquare$

---

## Front 5: Odd-Order & Half-Degree Cyclotomic Law for $p \equiv 5 \pmod 8$, Cyclotomic Order-Threshold Sieve, and Index-$k$ Census (`PCN-16`..`PCN-18`)

### Theorem 5A (`PCN-16` — Odd-Order & Half-Degree Cyclotomic Divisor Law for $p \equiv 5 \pmod 8$)
- **Status:** `PROVED LOCAL` (paper proof + 2-way Möbius / polynomial-division verification in [`mega_round_engine.py`](mega_round_engine.py) & [`independent_oracle.py`](independent_oracle.py) + Lean 4 theorem `p_mod8_five_quarter_odd` in [`PrimeCofactorCore.lean`](PrimeCofactorCore.lean)).
- **Domain & Hypotheses:** Let $p \equiv 5 \pmod 8$ be any prime, $L = \operatorname{ord}_p(16)$, and $k = \frac{p-1}{4L}$.
- **Claim:**
  1. **(Strict Oddness of $L$ and $k$, and $2$-Adic Valuation Match):** Because $p - 1 \equiv 4 \pmod 8$, the quarter-group order $\frac{p-1}{4}$ is strictly odd. Since $16 = 2^4$ generates the index-4 subgroup $(\mathbb{F}_p^\times)^4$ of order $\frac{p-1}{4}$, both $L = \operatorname{ord}_p(16)$ and the subgroup index $k = \frac{p-1}{4L}$ are **strictly odd integers**, and $\operatorname{ord}_p(2) = 4L$ has exact 2-adic valuation $v_2(\operatorname{ord}_p(2)) = 2 = v_2(p-1)$.
  2. **(Half-Period Sign Inversion & Half-Degree Cyclotomic Divisibility):** For every prime $p \equiv 5 \pmod 8$:
     $$\boxed{4^L \equiv -1 \pmod p, \qquad p \;\Big|\; \Phi_{2L}(4) = \Phi_{4L}(2) = \prod_{d \mid L} \left(4^d + 1\right)^{\mu(L/d)},}\tag{5.1}$$
     where $\Phi_{2L}(4)$ has degree $\varphi(2L) = \varphi(L)$ in $4$ and satisfies the tight logarithmic bound
     $$\boxed{\log \Phi_{2L}(4) < (2\log 2)\varphi(L) + \frac{1}{3} \qquad (\forall \text{ odd } L \ge 3),}\tag{5.2}$$
     cutting the naive cyclotomic exponent $\log(16^L - 1) = (4\log 2)L$ by at least a factor of $2$ (and by a factor of $3$ whenever $3 \mid L$, where $\varphi(L)/L \le 2/3$).
- **Proof:**
  For $p \equiv 5 \pmod 8$, Euler's criterion gives $2^{(p-1)/2} \equiv \left(\frac{2}{p}\right) = -1 \pmod p$. Since $\frac{p-1}{2} = 2kL$ with $k$ odd, $(4^L)^k = 2^{2kL} \equiv -1 \pmod p$, forcing $4^L \equiv -1 \pmod p$. Thus $\operatorname{ord}_p(4) = 2L$, so $p \mid \Phi_{2L}(4)$. Since $L$ is odd, $\mu(2d) = -\mu(d)$ yields $\Phi_{2L}(x) = \prod_{d\mid L}(x^d + 1)^{\mu(L/d)}$, and $\sum_{d\mid L} \mu(L/d)\log(1 + 4^{-d}) < 4^{-1} + 4^{-3}/(1 - 4^{-2}) < 1/3$ gives (5.2). $\blacksquare$

---

### Theorem 5B (`PCN-17` — Cyclotomic Order-Threshold Sieve Theorem at the Critical $\sqrt{p}$ Scale)
- **Status:** `PROVED LOCAL` (paper proof + exact verification in [`mega_round_engine.py`](mega_round_engine.py)).
- **Domain & Hypotheses:** Let $\mathcal{P}_N^{(5)} = \{2N < p < 8N : p \equiv 5 \pmod 8\}$, $\mathcal{P}_N = \{2N < p < 8N : p \equiv 1 \pmod 4\}$, and for any threshold $L_0 \ge 1$, let $\mathcal{E}(L_0) := \{p > 5 \text{ prime} : p \equiv 1 \pmod 4 \text{ and } \operatorname{ord}_p(16) \le L_0\}$ and $\mathcal{E}_5(L_0) := \{p \in \mathcal{E}(L_0) : p \equiv 5 \pmod 8\}$.
- **Claim:**
  1. **(Unconditional Cyclotomic Log-Weight Bounds):** For every $L_0 \ge 3$,
     $$\boxed{\sum_{p \in \mathcal{E}_5(L_0)} \log p \le \frac{4\log 2}{\pi^2} L_0^2 + O(L_0 \log L_0), \qquad \sum_{p \in \mathcal{E}(L_0)} \log p \le \frac{12\log 2}{\pi^2} L_0^2 + O(L_0 \log L_0).}\tag{5.3}$$
  2. **($100\%$ Full-Mass Corollary for $L_0(N) = o(\sqrt{N})$):** Since $\sum_{p \in \mathcal{P}_N} \log p = 3N + o(N)$ and $\sum_{p \in \mathcal{P}_N^{(5)}} \log p = \frac{3}{2}N + o(N)$ (`SPP-02`), for **every** growth schedule $L_0(N) = o(\sqrt{N})$ (including all polylogarithmic and $N^{1/2 - \varepsilon}$ windows), **$100\%$ of the prime-conductor mass in $\mathcal{P}_N$ unconditionally satisfies $\operatorname{ord}_p(16) > L_0(N)$**:
     $$\boxed{\sum_{\substack{p \in \mathcal{P}_N \\ \operatorname{ord}_p(16) > L_0(N)}} \log p = 3N + o(N).}\tag{5.4}$$
  3. **(Unconditional Positive Density at the Critical Gauss Scale $L > c\sqrt{p}$):** For every constant $0 < c < c_{\mathrm{shell}} := \sqrt{\frac{3\pi^2}{64\log 2}} \approx 0.816973$ (and up to $c_{\mathrm{dyadic}} := \sqrt{\frac{\pi^2}{16\log 2}} \approx 0.943359$ on dyadic shells $[X, 2X]$), a strictly positive proportion $\ge 1 - \frac{64\log 2}{3\pi^2} c^2 - o(1) > 0$ of the prime mass in $\mathcal{P}_N^{(5)}$ unconditionally satisfies $\operatorname{ord}_p(16) > c\sqrt{p}$ (where the Theorem 3 twisted Gauss ratio is $\frac{\sqrt{p}}{L} < \frac{1}{c}$).
- **Proof:**
  Every $p \in \mathcal{E}_5(L_0)$ divides $\prod_{\substack{3 \le L \le L_0 \\ L \text{ odd}}} \Phi_{2L}(4)$, whose logarithm is bounded by $(2\log 2)\sum_{\substack{L \le L_0 \\ L \text{ odd}}} \varphi(L) + \frac{L_0}{6} = \frac{4\log 2}{\pi^2} L_0^2 + O(L_0 \log L_0)$ since $\sum_{\substack{L \le x \\ L \text{ odd}}} \varphi(L) = \frac{2}{\pi^2} x^2 + O(x\log x)$. Similarly, every $p \in \mathcal{E}(L_0)$ divides $\prod_{L \le L_0} \Phi_L(16)$, whose logarithm is $(4\log 2)\sum_{L \le L_0} \varphi(L) + O(L_0) = \frac{12\log 2}{\pi^2} L_0^2 + O(L_0\log L_0)$. Setting $L_0 = c\sqrt{8N}$ on $\mathcal{P}_N^{(5)}$ gives $\frac{4\log 2}{\pi^2}(8 c^2 N) / (\frac{3}{2}N) = \frac{64\log 2}{3\pi^2} c^2 < 1$ for $c < c_{\mathrm{shell}}$. $\blacksquare$

---

### Theorem 5C (`PCN-18` — Exact Index-$k$ Small-Order Equivalence & Complete Census $13 \le p < 10000$)
- **Status:** `PROVED LOCAL` (paper proof + complete census in [`mega_round_engine.py`](mega_round_engine.py) + Lean 4 kernel theorem `small_order_index_k_iff` in [`PrimeCofactorCore.lean`](PrimeCofactorCore.lean)).
- **Domain & Hypotheses:** Let $p \equiv 5 \pmod 8$ be prime with $L = \operatorname{ord}_p(16)$ and odd index $k = \frac{p-1}{4L} \ge 1$.
- **Claim:**
  1. **(Exact Index-$k$ Equivalence):**
     $$\boxed{L \le \sqrt{p} \quad \Longleftrightarrow \quad L^2 \le 4kL + 1 \quad \Longleftrightarrow \quad L \le 4k - 1.}\tag{5.5}$$
  2. **(Unconditional Uniqueness for $k=1$ and $k=3$):**
     - At $k = 1$ ($p = 4L + 1$, where $16$ generates the entire quarter-group $(\mathbb{F}_p^\times)^4$): $p = 13$ ($L = 3$) is the **unique prime in all of $\mathbb{N}$** with $L \le \sqrt{p}$; every prime $p = 4L + 1 > 13$ has $L = \frac{p-1}{4} > \sqrt{p}$.
     - At $k = 3$ ($p = 12L + 1$): among the odd candidates $L \in \{3, 5, 7, 9, 11\}$, only $L = 9$ yields a prime ($p = 109$), so **$p = 109$ is the unique $k=3$ prime in all of $\mathbb{N}$** with $L \le \sqrt{p}$.
  3. **(Complete Census Across $13 \le p < 10000$):** Among all $608$ primes $13 \le p < 10000$ with $p \equiv 1 \pmod 4$:
     - $302 / 313$ ($96.49\%$) of $p \equiv 5 \pmod 8$ primes satisfy $L > \sqrt{p}$ (only $11$ exceptions: $p \in \{13, 109, 397, 1013, 1429, 1613, 3061, 3541, 5581, 8101, 8317\}$).
     - $267 / 295$ ($90.51\%$) of $p \equiv 1 \pmod 8$ primes satisfy $L > \sqrt{p}$ ($28$ exceptions).
     - In total, **$569 / 608$ ($93.59\%$)** satisfy $L > \sqrt{p}$.
- **Proof:**
  Since $L \ge 3$ is odd and $4k$ is even, $L \le 4k - 1 \implies L^2 \le (4k-1)L < 4kL + 1 = p$, while $L \ge 4k + 1 \implies L^2 \ge (4k+1)L = 4kL + L > 4kL + 1 = p$, proving (5.5) (kernel-verified in `small_order_index_k_iff`). At $k=1$, $3 \le L \le 3$ forces $L = 3$ ($p = 13$). At $k=3$, $3 \le L \le 11$ gives $p = 12L + 1 \in \{37, 61, 85, 109, 133\}$, where $85=5\times 17$ and $133=7\times 19$ are composite, while $\operatorname{ord}_{37}(16) = 9$ ($k=1$) and $\operatorname{ord}_{61}(16) = 15$ ($k=1$), leaving $p = 109$ ($L=9, k=3$) as the unique solution. $\blacksquare$

---

## 6. Adversarial Countermodels & Next Falsification Opportunities

| Countermodel / Control | What It Tests | Observed Behavior (Certified in `independent_oracle.py`) |
|---|---|---|
| **Coherent Counterseed $s_* = -\pi/16$** | Same 4-pole BBP recurrence $U_{n+1} = 16U_n + r(n+1)$ with real initial state $s_* = -\pi/16$ (`U_n(s_*) = -T_n`) | Passes all seed-uniform Laurent clock bounds up to $(d+1)\log_{16} N$; fails at $c \in (d+1, d+2)$ with positive gap $(1 - (d+1)/c)^2$; vanishes identically ($\equiv 0$) on both Theorem 3C zero-seed discriminators $\mathcal{I}^\Delta$ and $\mathcal{I}^{\mathbb{T}}$. |
| **Mutant Pole Vector $(5, -2, -1, -1)$** | Violates BBP ratio $A + 4C = 0$ (`5 + 4(-1) = 1 != 0`) | Breaks stroboscopic involution fixed point $J_4(v) = 4v$ (`PrimeCofactorCore.lean::bbp_stroboscope_fixed_and_mutant_broken`) and destroys the $15$-cancellation in the Laurent EGF $\mathcal{C}(z)$. |
| **Period-4 Fermat Prime $p = 257$** | $L = \operatorname{ord}_{257}(16) = 4 = 2M$ ($p \equiv 1 \pmod 8$) | Full-period primary character sum $G_{257}(15c_p h, 0) = 0$ vanishes identically for odd $h$, whereas true step-lag average $E_{257}(1) = -0.507420 \ne 0$ due to cofiber carry increments $\delta_{257, r}$. |
| **Higher-Octave Stroboscope Resonance ($p = 73, k = 4$)** | $73 \mid \operatorname{num}(U_4) = 1428806141948$ | $v_{73}(U_{55}) = v_{73}(U_{128}) = v_{73}(U_{201}) = -1$ at octaves $l=1,2,3$, but $v_{73}(U_{274}) = 0 \ge 0$ at octave $l=4$ (`higher_octave_stroboscope_certificate(73, 4)`), refuting naive multi-octave pole persistence without checking $p \nmid \operatorname{num}(U_k)$. |

### Next Falsification & Frontier Opportunities
1. **Oscillatory ($\ell \ne 0$) Cofiber Mode-Locking Bound (`NET-XVII-2`):** Theorems 2 & 3 unconditionally suppress the $\ell = 0$ (mean) cofiber erosion by $O(\sqrt{p}/L)$ and reduce `NET-XVII-2` to bounding the bilinear correlation $\sum_{\ell \ne 0} \widehat{D}_{p,h}(\ell) G_p(15c_p h, \ell)$ on the $100\%$-mass set of primes where $L = \operatorname{ord}_p(16) > L_0(N)$ (Theorem 5B). The next falsifiable probe is whether $\max_{\ell \ne 0} |\widehat{D}_{p,h}(\ell)|$ decays with $L$ across large-order primes in $\mathcal{P}_N$.
2. **Selected Zero-Seed Curvature Cancellation at Critical Scale $(d+1)\log_{16} N$:** Theorem 3B isolates the exact oscillatory zero-seed curvature defect $\Delta^{[d],\pi}_{N,K}(h; 0)$ versus the coherently positive counterseed defect $\mathcal{Q}^{[d]}_{N,K}(h) > 0$. Combining the Theorem 3C zero-seed circle carry invariant $c_n(0)$ with the Theorem 4A.2 stratified spill bound provides a direct finite-horizon filter for testing whether zero-selected phase cancellation persists past the seed-uniform clock barrier.
