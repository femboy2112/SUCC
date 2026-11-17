# PCE: Prime completion defect as observer-relative causal compensation

**Scope and claim status (2026-11-16):** This is an *additive* research program built on the classical genuine-prime Euler product, the Hurwitz-zeta continuation, the author's Prime-Path Nerve draft #660 (head `6ece172c5f7faa22955129374cb93db005316c94`), and Principia observer descent. Mathematical algebra in PCE-01--09 is **EXACT / PROVED PAPER within declared source and chart**. These are classical ingredient identities plus an explicit new-to-SUCC synthesis; no external-priority claim. RH, positive completed Weil form, BBP zero-seed carry escape, and pi base-16 normality remain **OPEN**. The word *energy* below denotes a defined arithmetic interaction/action, not physical energy, thermodynamic entropy, a quantum effect, or a proof of arithmetic randomness.

## Original thesis: a completed zero can contain two nonzero relative motions

The author's statement is interpreted as follows. An ideal full-state *model observer* sees two source-bound presentations of an invariant object with vanishing comparison defect. A partial observer sees the components move differently and must transport the hidden complementary coordinate to reconstruct the same invariant. The missing mixed term is the finite structural encoding of the compensation. The theological name "God" is, if used, an explicitly **idealized all-probes model perspective**, not a mathematical assertion that a physical omniscient intervener exists or a consequence of the formulas. Causal access is observer- and experiment-relative.

**Load-bearing warning:** We do NOT posit that all graphs sharing endpoints have identical arithmetic sources, nor that every coarse observer fails to predict the next observable. The precise comparisons and counterexamples are given below.

## PCE-01. Source-typed genuine-prime and Hurwitz coordinates (EXACT / CLASSICAL)

Fix finite `S` of distinct *actual rational primes*, `Q=prod_(p in S)p` (empty set `Q=1`), and `chi_p(s)=1-p^(-s)`. Define finite Euler coordinate

\[
E_Q(s)=\prod_{p|Q}\chi_p(s)^{-1}.
\]

For `Re(s)>1`, define the complete **complementary restricted-integer source**

\[
R_Q(s)=\sum_{\substack{n\ge1\\(n,Q)=1}}n^{-s}
=Q^{-s}\sum_{\substack{1\le a\le Q\\(a,Q)=1}}\zeta(s,a/Q)
=\zeta(s)\prod_{p|Q}\chi_p(s).
\tag{PCE1}
\]

Each equality is justified by absolute convergence and the actual CRT/reduced-residue sieve in `Re(s)>1`. The finite Hurwitz sum provides a meromorphic continuation for each finite `Q`; by uniqueness, the continued identity remains valid meromorphically. At the point `s=-1` the factors are finite, nonzero and real, giving

\[
R_Q(-1)=-\frac Q2\sum_{\substack{1\le a\le Q\\(a,Q)=1}}B_2(a/Q),\quad
E_Q(-1)=\prod_{p|Q}(1-p)^{-1},\quad
E_Q(-1)R_Q(-1)=\zeta(-1)=-\frac1{12}.
\tag{PCE2}
\]

The Hurwitz specialization is the classical `zeta(-1,a)=-B_2(a)/2`, NIST DLMF 25.11.14; it is not a numerical assignment to the divergent natural-number sum. `Q=1` is legitimate, taking the single coprime class `a=1`. The factorization labels must be genuine primes. A fake Euler factor `6` after primes `2,3` is not the same source.

## PCE-02. Exact two-channel observer transport, with zero global defect (EXACT)

Let `p` be a new genuine prime `p not |Q` and abbreviate `chi=chi_p(s)`. In the regular domain `chi != 0` (in particular `s=-1,2`), insertion acts as

\[
\begin{pmatrix}E_{Qp}\\R_{Qp}\end{pmatrix}
=T_p(s)\begin{pmatrix}E_Q\\R_Q\end{pmatrix},\quad
T_p(s)=\begin{pmatrix}\chi^{-1}&0\\0&\chi\end{pmatrix}.
\tag{PCE3}
\]

The *full* observer measures the quadratic pairing `B(E,R)=ER`. It sees

\[
B(T_p(E,R))=B(E,R)=\zeta(s),\qquad
\mathcal Z_{Q\to Qp}:=E_{Qp}R_{Qp}-E_QR_Q=0.
\tag{PCE4}
\]

There are simultaneously two independent, exact zero identities:

\[
\chi E_{Qp}-E_Q=0,\qquad R_{Qp}-\chi R_Q=0.
\tag{PCE5}
\]

The nonzero component motions are `Delta E=E_(Qp)-E_Q` and `Delta R=R_(Qp)-R_Q`. Thus the *objective/model-global zero* and the *subjective/component-relative nonzero movements* are different readouts of one typed arrow, not contradictory assertions. A model point with complete state and the correct source laws is called a **full observer** here; an abstract all-interventions oracle is not physically established.

## PCE-03. The missing mixed term is an exact interaction certificate (EXACT)

The quadratic pairing cannot be linearized across a finite prime step without paying the mixed term:

\[
\boxed{R_Q\Delta E+E_Q\Delta R+\Delta E\Delta R=0.}\tag{PCE6}
\]

For the nonzero base product, the normalized interaction is

\[
\boxed{\mathcal M_p(s):=\frac{\Delta E\Delta R}{E_QR_Q}
=(\chi^{-1}-1)(\chi-1)
=2-\chi-\chi^{-1}
=-\frac{p^{-2s}}{1-p^{-s}}.}\tag{PCE7}
\]

The normalized linear residual is exactly `-M_p(s)`. At two reflected points,

\[
\boxed{\mathcal M_p(-1)=\frac{p^2}{p-1}>0,\quad
\mathcal M_p(2)=-\frac1{p^2(p^2-1)}<0.}\tag{PCE8}
\]

For primes `2,3,5,7`, `M_p(-1)` is respectively `4, 9/2, 25/4, 49/6`. These are exact rational values. The interaction is nonzero for *every* genuine prime and is unchanged by a single fixed chart rescaling `(E,R)->(cE,c^(-1)R)` with `c != 0`. It is not invariant under arbitrary stage-by-stage rescaling: a changing gauge contributes its own transport.

**Falsifying the naive observer:** Omitting `Delta E Delta R` changes a correct zero statement into the false assertion `R Delta E+E Delta R=0`. At `Q=1,p=2,s=-1`, that omitted linear term is `1/3`, while the mixed term is `-1/3`. This exact rational contradiction is the hostile receipt for any linear-only compensation formula.

## PCE-04. A signed O(1,1) geometry at negative one (EXACT)

At `s=-1`, set `u=(E_Q+R_Q)/2`, `v=(E_Q-R_Q)/2`. Then

\[
\boxed{u^2-v^2=E_QR_Q=-1/12.}\tag{PCE9}
\]

For an inserted prime `p`, write the real rapidity `t_p=log(p-1)`. Since `chi_p(-1)=-(p-1)`, its coordinate change is

\[
\boxed{\binom{u'}{v'}=-\begin{pmatrix}
\cosh t_p&-\sinh t_p\\-\sinh t_p&\cosh t_p
\end{pmatrix}\binom{u}{v}.}\tag{PCE10}
\]

It belongs to real `O(1,1)` and preserves the split quadratic form. This is the *presentation-space* hyperbolic geometry of the canonical Euler/Hurwitz coordinates, **not physical Lorentz invariance, spacetime dynamics or Einstein field equations**. The extra minus sign is a central orientation/sign flip at each negative-one prime insertion; at `p=2` the rapidity is zero but the sign flip persists.

The mixed interaction also has the exact hyperbolic representation

\[
\boxed{\mathcal M_p(-1)=4\cosh^2(t_p/2).}\tag{PCE11}
\]

This positive quantity is an **observer-relative prime-step mixed-compensation coefficient**. For a finite prime path `S`, the declared additive path action

\[
\mathscr A_{-1}(S)=\sum_{p\in S}\mathcal M_p(-1)>0
\tag{PCE12}
\]

is a concrete finite arithmetic measure of cumulative compensation, independent of insertion order. It is not a conserved physical energy and does not give a lower bound on BBP carry escape. At `s=2`, `chi_p(2)>0` yields an unsigned boost, and `M_p(2)<0`; positivity is **basis/end-point relative**.

## PCE-05. Full prime-path transport is FLAT; no fabricated curvature (EXACT / CRUCIBLE)

For distinct new authentic primes `p,q`,

\[
\boxed{T_p(s)T_q(s)=T_q(s)T_p(s).}\tag{PCE13}
\]

Every prime-insertion square has exact trivial holonomy. The full transport along any ordering of a fixed finite set is path-independent. The positive action in PCE12 records nonzero *motion/compensation cost*, NOT curvature, nonabelian commutator, or quantum phase. This distinction is central: shared endpoints alone would not make arbitrary source paths equivalent, but here the actual multiplicative prime maps explicitly commute.

A **partial observation** may nevertheless fail to descend. On the full hyperbola `ER=-1/12`, take `h(E,R)=E+R`. The distinct states `(1,-1/12)` and `(-1/12,1)` have the same h and the same invariant product. For `p=3`, `T_3=diag(-1/2,-2)`. Their next sums are `-1/3` and `-47/24`, different. Hence there is no well-defined map on *all h-fibers* that predicts the next h from h alone. This is Principia CG-02's observer-descent obstruction in a nonlinear state-domain example. These two states belong to the declared extended hyperbola, NOT necessarily to the finite-Euler reachable prime sequence.

**Countercontrol:** the Euler-only observer `h(E,R)=E`, *provided it knows the inserted p and the chart*, DOES have a closed update `E -> chi^(-1) E`. An assertion that every subjective observer loses causal information is REFUTED. What is hidden depends on its readout, source passport and probes. The full observer's zero invariant neither implies zero component motion nor universal nonzero projected curvature.

## PCE-06. A finite jet register exactly stores derivative compensation (EXACT)

The transport is a meromorphic identity in `s`, not merely a scalar equality at one point. Differentiation yields

\[
\begin{aligned}
E_{Qp}'&=\chi^{-1}E_Q'-\chi'\chi^{-2}E_Q,\\
R_{Qp}'&=\chi R_Q'+\chi'R_Q,
\qquad\chi'=p^{-s}\log p.
\end{aligned}\tag{PCE14}
\]

For `j>=1`, `chi^(j)=(-1)^(j+1)(log p)^j p^(-s)`, so all finite k-jets are updated by Leibniz's finite triangular recurrence. In particular,

\[
\boxed{E_{Qp}'R_{Qp}+E_{Qp}R_{Qp}'
=E_Q'R_Q+E_QR_Q'=\zeta'(s).}\tag{PCE15}
\]

At `s=-1` the exact formal jet lives in a finite module over the rational ring generated by the finitely many symbols `log p` and the original `zeta'(-1)`. The verifier implements first jets with rational coefficient maps, *never* replacing each log by a floating estimate. This is an explicit finite structural encoding of the compensation across arbitrary finite prime insertion sequences. For each finite k the jet register is finite, but its raw symbolic/source label size grows with prime count; this is not a single fixed-memory automaton for all primes and all complex s.

The genuine zeta reflection identifies the invariant first derivative with the positive prime-power current:

\[
\boxed{\frac{\zeta'(-1)}{\zeta(-1)}
=\gamma-1+\log(2\pi)-\frac{\zeta'(2)}{\zeta(2)}
=\gamma-1+\log(2\pi)+\sum_p\frac{\log p}{p^2-1}.}\tag{PCE16}
\]

The final prime sum is absolutely convergent. The equality imports the authentic zeta functional equation and its true Euler source, not a BBP-derived proof of those facts. Equally, `xi(-1)=xi(2)=pi/6=(8/3) x_BBP` uses the **imported classical BBP identity**, with `x_BBP=pi/16` from the literal four-pole source and zero seed. An equality of completed values/derivatives is not a time-ordered BBP carry theorem.

## PCE-07. Analytic continuation first is legal if the compensation register survives (EXACT)

For a growing finite authentic prime sequence `Q_k`:

- On `Re(s)>1`, the restricted source `R_(Q_k)(s)` tends to `1`, because its coefficients are the coprime projectors `1_((n,Q_k)=1)` and tend pointwise to `1_(n=1)`, and dominated convergence applies.
- Continuing each **finite** `R_(Q_k)` to `s=-1` instead gives `R_(Q_k)(-1)=(-1/12)prod_(p|Q_k)(1-p)`, whose absolute value grows unboundedly. Simultaneously `E_(Q_k)(-1)` tends to zero in absolute value and its sign flips at every added prime.
- Their product is `-1/12` at **every finite stage**.

Therefore the two completion orders do not commute as *uncompensated one-coordinate limits*. The exactly transportable finite state is `(E_Q,R_Q)` plus desired signed/jet/source metadata, not `R_Q(-1)` alone. An infinite collection of growing finite registers is legitimate; its separate component limits have no finite value from which one may reconstruct the endpoint by ordinary multiplication. The nonuniform boundary is **diagnosed** by the finite coefficients `chi_p`, their signs and logarithmic derivatives; it has not been made uniformly convergent by renaming it.

At `s=-1`, the log-magnitude increments are exactly `±log(p-1)`, the Euler and residue signs each reverse, and `M_p=p²/(p-1)`. These finite entries are the explicit structural encoding sought in the thesis. No infinite divergent Euler product at -1 is asserted to converge p-adically in one common field, or to equal the analytically continued zeta there.

## PCE-08. CRT automata authenticate the local atoms, not every global theorem (EXACT)

At a candidate integer `n>=2`, take the finite source inventory `S(n)={p genuine prime:p<=sqrt(n)}`. Its path-nerve signed face sum is `1` iff `n` is prime; the finite CRT projector implements the same predicate. As `n` changes, the required finite automaton/CRT domain can grow. This is a correct effective procedure, not a fixed finite automaton with a constant number of states recognizing all primes.

**Fake-6 mutant:** after primes 2 and 3, checking `6|n` is redundant in the divisor projector, whereas appending an independent factor `(1-6^(-s))^(-1)` changes the Euler coordinate. So the phase/product presentation needs *prime-factor labels and multiplicities*, not only yes/no sieve output. The elementary distinction is tested exactly. A source-labelled prime path is a lawful factorization route; two arbitrary parallel graph edges need not be prime states.

## PCE-09. An actual common-clock signed CRT × BBP joining (EXACT IDENTITY / OPEN POSITIVE BOUND)

Retain exactly the source from Main XXVI:

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\ U_n=16U_{n-1}+r(n),\ C_n=\lfloor U_n\rfloor.
\]

Set `sigma(C_n)=+1` for residues `0,3 mod4` and `-1` for `1,2`. Let `rho_Q(n)=1_((n,Q)=1)` be the *same-time* authentic CRT prime projector. On each integer shell define

\[
A_{B,Q}=\frac1B\sum_{n=B}^{2B-1}\rho_Q(n),\qquad
J_{B,Q}=\frac1B\sum_{n=B}^{2B-1}\rho_Q(n)\sigma(C_n).
\tag{PCE17}
\]

The exact source-tied signed *difference* is

\[
\boxed{A_{B,Q}-J_{B,Q}
=\frac2B\sum_{n=B}^{2B-1}\rho_Q(n)\mathbf1_{\{C_n\bmod4\in\{1,2\}\}},
\quad 0\le A-J\le2d_B.}\tag{PCE18}
\]

In terms of actual Ramanujan coefficients `c_Q(h)`, the unaveraged signed joining is also

\[
\boxed{J_{B,Q}=\frac1{BQ}\sum_{h\bmod Q}c_Q(h)
\sum_{n=B}^{2B-1}\sigma(C_n)e^{-2\pi ihn/Q}.}\tag{PCE19}
\]

No independent CRT clock was invented: both observations use the same integer `n`. A fixed-Q uniform all-late-shell margin `A-J>=2delta>0` would imply original positive selected carry density `d_B>=delta` and therefore Main XXVI's R0. That margin is **OPEN**, and PCE18 itself is merely a nonnegative counting identity. The full prime accumulator, Gamma transport or a finite positive action PCE12 does **not** produce that margin.

For an inserted prime `p not|Q`, the directly observed temporal prime update is

\[
\boxed{J_{B,Qp}-J_{B,Q}
=-\frac1B\sum_{n=B}^{2B-1}\rho_Q(n)\mathbf1_{p|n}\sigma(C_n).}\tag{PCE20}
\]

This is an explicit **source-chosen signed joining** between prime-path insertion and the true zero-seed BBP carry. It is a mathematically valid next object to investigate, unlike a factorized product of unrelated marginals. The function `rho_Q` is seed-blind; the *joined* statistic is seed-attached. The coherent changed seed `s=-pi/16` has `U_n=-T_n`, `C_n=-1`, `sigma=1`, and consequently `A-J=0` for every shell and every Q. Rational finite-shadow changed seeds may suppress the selected events on any prescribed finite horizon. Both controls prohibit promoting PCE18 into a generic positivity statement.

**Inventory saturation control:** if `Q` includes every prime up to `2B-1`, then `rho_Q(n)=0` for every `n in[B,2B)` with `B>=2`; the joined statistic vanishes regardless of BBP carries. Thus one must fix a nontrivial prime cutoff/conditional normalization *before* claiming a positive source constraint. An infinite sieve uncritically inserted into a fixed finite-time shell loses the information the question needs.

**Coboundary control:** changing `r` by `g(n)-16g(n-1)`, `g(0)=0`, and changing `T` by `-g(n)` can preserve the completed real pi orbit while changing `C_n`. PCE17 is explicitly original-source-presentation-dependent, and gauge transport must be specified before comparing signed carry statistics. The same *completed* circle is not enough to identify integer-winding observations.

### The original BBP forcing has an authenticated Gamma successor chart

Define the explicit source-pole Gamma quotient (where its arguments avoid poles)

\[
H(t)=\frac{\Gamma(t+\tfrac18)^4}{\Gamma(t+\tfrac12)^2\Gamma(t+\tfrac58)\Gamma(t+\tfrac34)}.
\]

Gamma's exact successor recurrence gives

\[
\frac{H(t+1)}{H(t)}=
\frac{(t+\tfrac18)^4}{(t+\tfrac12)^2(t+\tfrac58)(t+\tfrac34)},\quad
\boxed{r(n)=\frac18\left.\frac{d}{dt}\log\frac{H(t+1)}{H(t)}\right|_{t=n-1}.}\tag{PCE21}
\]

The latter equality is the literal original four-pole forcing, verified by differentiating the logarithm of the displayed rational quotient. It is a lawful **source-time** Gamma representation. It does not turn the Euler-prime insertion operator `T_p` into the actual BBP time shift, nor does it identify the prime-specific split-signature action with a physical Gamma field. The two paths meet at the true completed scalar `pi`, but a common *signed chronological* square remains unproved.

## PCE-10. Reflection and the RH/normality firewall (EXACT CONTACT / OPEN GLOBAL GOAL)

For the genuine zeta source,

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)=\xi(1-s).
\]

The reflected endpoints `s=-1` and `s=2` give `xi(-1)=xi(2)=pi/6=8 x_BBP/3`. The finite compensated coordinate `E_Q R_Q=ζ(s)` is transported by the actual completed Gamma/pole multiplier before comparison. This retains both the prime and Archimedean source structures; it does not imply Weil's globally nonnegative quadratic form or zeros confined to the critical line. The split-signature boost is not by itself a positivity proof, and the signed action `M_p(-1)>0` is not a density of the BBP carry residues.

A genuine theorem advancing R0 requires a new zero-ancestry-dependent **all-shell** bound, e.g. `liminf_(B->infty)(A_(B,Q)-J_(B,Q))>0` for some predetermined fixed Q, or an independently established *source-sensitive* inequality after a declared time/refinement/Gamma transport. Controls: fake composite six, arbitrary paths, signed-jet truncation, wrong chronological seed, finite rational shadows, polynomial coboundary with corrected tail, completion-order swap, and saturating prime inventory. A proof using only scalar `xi(-1)=xi(2)` is insufficient.

## PCE-11. Fictitious-force calibration: flat ambient transport, nonzero subjective inertial response (EXACT / SOURCE-TYPED ANALOGY)

**Motivation and scope.** The author identifies the constrained observer's apparent causal energy with a *fictitious force*, such as centrifugal force in a rotating frame. This is a productive and mathematically testable distinction: a nontrivial connection coefficient or observer-relative acceleration need not imply intrinsic curvature. This section supplies exact source-labelled prime maps and an explicit calculation of the information lost by projecting between steps. The models below are **presentation-space coordinate dynamics**, not physical noninertial motion, literal centrifugal force, gravitational curvature, a proof of local causal thermodynamics, or a new pi-normality estimate.

### Flat prime transport as a removable full-frame connection

At `s=-1`, define `K=[[0,-1],[-1,0]]`, `K^2=I`, and `B(t)=exp(t K)=[[cosh(t),-sinh(t)],[-sinh(t),cosh(t)]]`. As in PCE-04, insertion of a genuine prime `p` is `T_p=-B(t_p)` with `t_p=log(p-1)`. For a finite set of `k` inserted primes, the **entire** action is

\[
T_{p_k}\cdots T_{p_1}=(-1)^k B(\tau_S),\qquad \tau_S=\sum_{j=1}^k\log(p_j-1). \tag{PCE22}
\]

The proof uses `K^2=I`, commutation of exponentials of the same matrix, and the central sign `-I`. The coordinate velocity in a declared *continuous auxiliary* interpolation `z(t)=B(\tau(t))z_0` is `dz/dt=\dot\tau Kz`; its second derivative is `d²z/dt²=(\ddot\tau K+\dot\tau² I)z`. A moving frame `\tilde z=B(-\tau)z` removes this apparent motion: `d\tilde z/dt=0`. Equivalently the matrix-valued connection `\mathcal A=K\,d\tau` is pure gauge, with `d\mathcal A+\mathcal A\wedge\mathcal A=0`. The two-prime insertion square is exactly flat, as already proved in PCE-05.

The factor `(-1)^k` is **discrete**. It cannot be silently interpolated within the identity component of `O(1,1)`, so the above smooth demonstration treats only the boost part and retains the sign as a separate `Z/2` orientation label. Choosing a smooth `\tau(t)` is an auxiliary chart, not an authenticated sub-integer prime-insertion clock. Also, `K²=+I` here; a literal rotating-frame centrifugal term instead comes from a spatial rotation generator `J²=-I`. The analogy concerns *coordinate-dependent fictitious terms*, not an equality of these two forces.

### Exactly where forgetting creates a force-like defect

Declare the coarse observer `P(u,v)=u` and an explicit linear reinjection `J(u)=(u,0)`, so `PJ=I`. Compare **retaining** full memory through two distinct prime insertions with **discarding** the hidden coordinate after the first step:

\[
\boxed{\begin{aligned}
\mathscr D_{p,q}&=PT_qT_pJ-(PT_qJ)(PT_pJ)\\
&=PT_q(I-JP)T_pJ\\
&=\sinh(t_p)\sinh(t_q)\,I.\end{aligned}}\tag{PCE23}
\]

This is the exact compression/hidden-fiber term of the type already studied in SUCC's observer-compression defect laws. It can be nonzero despite **zero ambient curvature**, since `PT_qT_pJ` and the compressed product are *different operations*. In particular, for authentic primes `p=3,q=5`,

\[
\boxed{\mathscr D_{3,5}=\sinh(\log2)\sinh(\log4)=\tfrac34\cdot\tfrac{15}{8}=\tfrac{45}{32}.}\tag{PCE24}
\]

For `p=2`, `t_p=0`, the defect is zero even though the full prime insertion flips the sign. Thus not every prime step causes this kind of hidden-fiber defect. Since the full transporter is abelian, the displayed scalar gap is symmetric under `p,q` interchange; it is **not** a nonzero prime-order commutator.

**Calibration firewall:** The linear section `J(u)=(u,0)` is not constrained to the actual source hyperbola `u²-v²=-1/12`; indeed no real point on that hyperbola has `v=0`. Thus the `45/32` value is an exact **ambient observer-compression calibration**, not a measured value on the canonical prime orbit and not an intrinsic scalar of the original Euler product. The source-restricted non-descent witness in PCE-05 already uses two legitimate points of the same hyperbola. A physical or fully source-authenticated observer requires a source-valid section (possibly nonlinear), access prior, and disturbance model before a projected inertial *cost* can be assigned.

### No curvature or positivity promotion

A full observer's identity `ER=\zeta(-1)` is unchanged; a constrained observer's failure to transport observations through an intermediate coarse quotient is a real and computable defect. In mathematical terminology it is closer to a **noninertial/compression artifact** than to ambient intrinsic curvature. Neither `\mathscr D_{p,q}` nor the earlier mixed coefficient `\mathcal M_p` is invariant under arbitrary changes of observer, and neither is an actual force acting on BBP dynamics. At `s=-1`, the gamma/carry and Weil-positive research debts remain unpaid. Any proposed generalization claiming curved ambient prime transport must exhibit a nonzero source-derived path commutator or curvature tensor, which the present commuting genuine-prime maps **refute**.

**Independent falsifiers:** direct exact 2×2 rational matrix multiplication; `p=2` zero-gap; `p=3,q=5` gap `45/32`; arbitrary prime ordering; same-source hyperbola pair with equal coarse observation but different next value; wrong section or projection; and a naive identification of this signed `O(1,1)` boost with SO(2) centrifugal dynamics.

## Source records and independent witnesses

- Main XXVI pinned `main@81be6b897ae980b801a3b9de9e22ef81e8360bfb`; its `docs/PI_NORMALITY_FRONTIER.md`, `docs/MAIN_XXVI_SOURCE_PHASE_INTERFACE.md`, `docs/principia_observatoris/02_causality_geometry.md` (CG-02/CG-05/CG-08).
- Prime-Path Nerve draft #660 pinned `6ece172c5f7faa22955129374cb93db005316c94` (PPN-01--06). This dossier is independently additive and does not rewrite #660's claims.
- Generalized Euler--Adelic Boundary EAB-07, EAB-11; `research/2026-10-24/GENERALIZED_EULER_ADELIC_BOUNDARY.md`.
- Finite positive Pascal construction: `research/2026-11-14/causal_suspension_gamma_zeta/THEOREMS.md` PSV-05; negative-order/tower: `research/2026-11-15/causal_negative_orders/THEOREMS.md` CN-09.
- Actual prime/Weil source distinction: `docs/CLAIM_SUPPLEMENT_COMPLETED_WEIL.md`, `docs/CLAIM_SUPPLEMENT_CIRCLE_GAMMA_PRIME_DIGITS.md`.
- Primary analytic formulae: [NIST DLMF Hurwitz special value §25.11.14](https://dlmf.nist.gov/25.11.E14); [completed-zeta reflection §25.4.3--4](https://dlmf.nist.gov/25.4); [Euler product/prime powers §25.2](https://dlmf.nist.gov/25.2).
- Exact arithmetic `prime_compensation.py`, `test_prime_compensation.py`; genuinely separate SymPy/Fourier oracle `independent_audit.py`. Tool passes are finite implementations of algebra, not independent proof of RH/normality or external priority.
