# Positive analytic-source perturbations with an empty prescribed terminal wall block

Status: **PROVED PAPER, source-changing hostile theorem**. This is not a new inequality for the literal original source. It rules out a locally uniform coercivity bridge based only on continuous Mellin/Gamma source geometry, even when every moment degree and every weighted pole-orbit obstruction is retained. No claim of external priority.

## 1. Objects and exact construction

Let r(n) be the literal original four-pole BBP forcing, Q(t)=4-2t^3-t^4-t^5, K(t)=Q(t)/(16-t^8), U_0=0, U_n=16U_(n-1)+r(n), and P_n=16^(-n)U_n. Fix any integer M>=1. Set

\[
h_M(n)=r(n+M)-r(n+M+1),\qquad
g_M(n)=16h_M(n)-h_M(n+1).
\]

For every integer B>=1 define the **exact rational** parameters

\[
q_B=16^{-B}\lceil16^B P_{2B}\rceil,\quad
\delta_B=q_B-P_{2B}\in[0,16^{-B}),\quad
\epsilon_B=\delta_B/h_M(1),
\]

and the changed forcing

\[
f_B(n)=r(n)+\epsilon_Bg_M(n),\quad
V_0=0,\quad V_n=16V_{n-1}+f_B(n).
\]

All data are computed from finite rational source sums. No digits of a floating-point pi value or uncomputed tail are used to choose the perturbation. The forcing f_B is **different** from r unless delta_B=0. No replacement of the original source is proposed.

## 2. Positivity, complete monotonicity, and full moment-tower stability

The exact Mellin formulas give

\[
h_M(n)=\int_0^1t^{8n-8}t^{8M}Q(t)(1-t^8)\,dt>0,
\]

\[
f_B(n)=\int_0^1t^{8n-8}Q(t)
\left[1+\epsilon_Bt^{8M}(16-t^8)(1-t^8)\right]dt.
\]

The integrand is positive for 0<t<1 and n>=1. Differentiating with respect to real n inserts powers of 8 log(t); the integrals are absolutely convergent on n>=1. Thus f_B is positive, strictly decreasing, and completely monotone on [1,infinity). In particular this construction preserves more than positivity and monotonicity.

Since h_M(n)=15/(32n^3)+O(n^-4),

\[
g_M(n)=225/(32n^3)+O(n^{-4}),\qquad
f_B(n)=15/(64n^2)+O_B(n^{-3}).
\]

The exact leading BBP coefficient is unchanged.

The completed Mellin density becomes

\[
K_B(t)=K(t)+\epsilon_Bt^{8M}Q(t)(1-t^8)
=K(t)[1+\epsilon_B A_M(t)],
\]

where A_M(t)=t^(8M)(16-t^8)(1-t^8) satisfies 0<=A_M(t)<=16 on [0,1]. Consequently, for the u=-log(t) measures dnu=e^(-u)K(e^(-u))du and dnu_B=e^(-u)K_B(e^(-u))du,

\[
d\nu\le d\nu_B\le(1+16\epsilon_B)d\nu.
\]

This gives the **simultaneous all-degree Loewner bounds**

\[
H_m\preceq H_{m,B}\preceq(1+16\epsilon_B)H_m
\quad\text{for every integer }m\ge0,
\]

where H_m and H_(m,B) are the complete Hankel moment matrices in powers of u. Proof: integrate |p(u)|^2 for every polynomial p. In fact the same comparison holds for every measurable square-integrable function. Each entire infinite positive-moment tower is relatively 1+O_M(16^-B) close to the authentic one. This is not a finite-moment fitting statement.

Moreover ||nu_B-nu||_(TV)=epsilon_B h_M(1)=delta_B<16^-B, since the difference measure is positive.

## 3. Original residues and all shift-orbit obstructions survive

Expand the perturbation:

\[
g_M(n)=16r(n+M)-17r(n+M+1)+r(n+M+2).
\]

Because M>=1, all added poles are to the left of the four original poles. Their residues at 7/8,1/2,3/8,1/4 remain exactly (1/2,-1/4,-1/8,-1/8). The construction does add deeper poles; it does not preserve the exact four-pole inventory.

On a pole orbit alpha-Z with original residue R_alpha, the added residues at depths M,M+1,M+2 are epsilon_B R_alpha(16,-17,1). Their weighted sum is

\[
\epsilon_B R_\alpha16^{M+1}(1-17+16)=0.
\]

Thus **every weighted simple pole-orbit obstruction** remains exactly that of r. The perturbation is a rational coboundary, so this equality is consistent with the inherited obstruction theorem. These invariants cannot detect it; the full rational source function detects it immediately.

## 4. The same Gamma regularizer and almost all exact activation channels

Use r_w(n) with the original four shifted denominators and define

\[
H_M(w)=r_w(M+1)-r_w(M+2).
\]

Absolute convergence of the weighted source sum, or direct telescoping, gives

\[
\mathcal B_B(w)=\mathcal B(w)+\epsilon_B H_M(w).
\]

Let A={1,4,5,6}, D(w)=prod_(a in A)1/Gamma((w+a)/8), and E=D B/D(0), as in #657. The SAME D regularizes the changed source: E_B=E+epsilon_B D H_M/D(0) is entire. The additional rational term has poles only at the eight channels w=-a-8M and w=-a-8(M+1). Therefore

\[
\mathcal E_B(-a-8j)=\mathcal E(-a-8j)
\quad\text{for every }a\in A,\ j\notin\{M,M+1\}.
\]

The remaining eight values differ by the explicitly signed residues ±epsilon_B c_a D'(w)/D(0). Choosing M beyond any fixed observed activation depth preserves every activation value below that depth, while retaining all but eight of the entire infinite lattice.

For every fixed compact C in the complex plane, D H_M is entire and bounded on C. Hence

\[
\sup_C|\mathcal E_B-\mathcal E|
\le\frac{16^{-B}}{h_M(1)}\sup_C|D H_M/D(0)|.
\]

Thus the changed completions and all finite derivative jets converge locally uniformly to the original at a geometric rate. This is exact local analytic convergence, not merely a match of finitely many numeric samples.

## 5. Empty terminal domain-wall block and exact Borwein failure at the chosen shell

Telescoping the recurrence from the literal zero seed gives, for every n>=0,

\[
V_n-U_n=\epsilon_B[16^n h_M(1)-h_M(n+1)].
\]

Set a_B=epsilon_B h_M(2B+1). Then

\[
\boxed{V_{2B}=16^{2B}q_B-a_B,\qquad 0\le a_B<16^{-B}.}
\]

The integer 16^(2B) q_B is divisible by 16^B. If a_B>0, floor(V_(2B)) has its last B hexadecimal digits all F. If a_B=0 they are all 0. Thus

\[
\boxed{D_B(f_B)=J_B(f_B)=0.}
\]

Every backward probe has circle distance a_B/16^k; this is below 1/2. Therefore the exact norm is

\[
\boxed{
\mathcal R_B(f_B)
=\frac{a_B^2(1-256^{-B})}{255 B}
<\frac{16^{-2B}}{255B}.
}
\]

For the two-pulse leakage L(theta)=162/289 (||theta||-1/18)_+^2, every backward probe lies in the zero region. Hence

\[
\boxed{\widehat J_B^{(f_B)}(0)=0.}
\]

The origin sweep is far from its Haar mean. Since L(1/2)=32/289 and Lip(L)=144/289,

\[
\sup_\alpha|\widehat J_B^{(f_B)}(\alpha)-256/7803|
\ge\frac{608}{7803}-\frac{144a_B(1-16^{-B})}{4335B}.
\]

This lower bound exceeds 3/40 for every B>=1 by a_B<16^-B.

The completed endpoint is x_B=x+delta_B=q_B+(x-P_(2B)). On the selected shell B<=n<2B, its actual circle phase is T_(2B)/16^(2B-n). Thus the actual completed shell also lies in the Borwein zero region. The terminal F-block and the completed 0-block differ by the positive tail carry; neither contains a domain wall. This comparison uses the changed source's own positive tail T_n+epsilon_B h_M(n+1).

## 6. What is refuted, and what is not

For every fixed M, the one-parameter family r+epsilon g_M contains a sequence of rational positive zero-seeded sources f_B tending to r. They retain the original four residues, every weighted shift-orbit obstruction, the leading tail order, the Gamma regularizer, all but eight pole-lattice values, and simultaneous all-degree moment-form comparison. Nevertheless their prescribed B-shell norm collapses exponentially and their anchored Borwein response is exactly zero.

This **refutes a locally uniform source-neighborhood coercivity theorem** based only on these stable analytic properties: no neighborhood of r in the exhibited relative-density/locally-uniform-entire topology can have constants eta>0,B0 for which all sources in that neighborhood have R_B>=eta for every B>=B0.

It does **not** exhibit one fixed source f with arbitrarily late empty shells; f_B changes with B. It does not refute original-source R0, full normality, or an exact-source arithmetic proof. No normality conclusion is drawn from perturbing the source. Exact knowledge of r immediately rejects every nonzero perturbation.

The precise unpaid bridge is an arithmetic inequality on the isolated source r and its literal zero-selected history. Uniform positivity, near-isometry of the entire moment tower, and locally uniform entire continuation cannot supply that inequality by a stability argument with a locally uniform onset time.

## 7. Ancillary exact bridge and its boundary

For the original Mellin family, B(8n)=T_n follows directly from K's geometric expansion. Therefore

\[
U_n=16^n B(0)-B(8n).
\]

This is a valid analytic-source-to-real-state intertwiner, but exponentiating it merely reproduces the signed orbit. If B(0) has absolute error e, its n-th phase error can be as large as 2 pi 16^n e before wrap. Positive moment reconstruction therefore needs exponentially fine mass precision for long circle horizons. The f_B construction is an exact zero-seeded source witness for this instability and identifies which source passport information must remain exact.

## Provenance and verification boundary

Read main at 81be6b897ae980b801a3b9de9e22ef81e8360bfb; #657 at 7e406514ffdd1dac932cdfa6a0e1bf12b8059ebf: ORDINAL_MELLIN_GAMMA_OBSERVER_ASCENT.md, BBP_IMPULSE_MELLIN_FILTER.md, BBP_POLE_SHIFT_CRUCIBLE.md, BBP_TWO_FORMULA_LOCKED_COUNTERMODEL.md. Read #658 at cf46c9dac20b2ac58675ac7f98937e488307cbf7: gamma_carry_tower/THEOREMS.md. All are under research/2026-11-17/causal_clock_scrambling/ except the stated #658 path research/2026-11-16/gamma_carry_tower/.

The new proof uses elementary rational telescoping, positive integrals and the inherited reciprocal-Gamma zero set; no new imported asymptotic theorem. Same-model derivation plus distinct exact code is not an independent mathematical referee. The finite probe is gamma_source_probe.py. It tests direct chronological states, independently integrated kernel polynomials, exact residues, empty walls, exact norms, Borwein bounds and a coefficient mutation. Its finite scope is recorded separately by the parent operation.
