# Operation Maxwell Demon: source-relative information cost and local zero migration

**2026-10-28.** This is a research-only child of [draft PR #354](https://github.com/femboy2112/SUCC/pull/354), pinned to commit 6adf1a74e3d85355ee94f0087b27e2c3b7f125d8. The authentic source is the OLZF-04 prime-power factorization fiber, its marked uniform state and PCR-02 Pólya stochastic birth law. This appendix neither changes them nor claims RH, pi normality, a physical Maxwell demon, or new academic priority.

## 1. Precise conjecture and source contract

The intuition being tested is that the base arithmetic field is invariant under *passive source-faithful frame transport*, whereas a nonzero real tilt changes relative path probabilities. Persistent real reweighting is hypothesized to require a control/selection absent from native arithmetic. We quantify *information*, not thermodynamic work. We distinguish (i) path probabilities, (ii) a pure-state amplitude, (iii) a Fourier-character zero, and (iv) a zeta zero. No map among these types is assumed without proof.

For fixed genuine prime p, depth j>=0, and L=log p, let the paths of p^j have coordinates k=0,...,j. The marked source vector has uniform amplitudes. Its source law is

$$u_j(k)=\frac{1}{j+1},\qquad
P_j(k,k+1)=\frac{k+1}{j+2},\quad P_j(k,k)=\frac{j+1-k}{j+2}.$$

This is the original SUCC/PCR probability transition, not a newly inserted dynamics.

## 2. SDB-01: the authentic Pólya infinite source

Direct substitution yields u_j P_j=u_(j+1). The process K_j starts at K_0=0, has increments in {0,1}, and (K_j+1)/(j+2) is a bounded martingale. The classical two-color Pólya-urn theorem identifies its almost-sure limit:

$$\boxed{\frac{K_j}{j}\longrightarrow U\sim\operatorname{Uniform}[0,1]\quad P\text{-a.s.}}$$

In particular P(U=0)=P(U=1)=0. This is a theorem about the declared native stochastic process, not about the Riemann zeros. See the external Pólya-urn sources at the end.

## 3. SDB-02: fixed real tilt and finite-source fidelity

The source imbalance operator is D|k>=(2k-j)L|k>. For epsilon>0, normalize exp(-epsilon D) applied to the original marked pure vector and take squared coordinate amplitudes:

$$a=e^{-4\varepsilon L}\in(0,1),\qquad
q_j(k)=\frac{a^k}{Z_j},\quad
Z_j=\frac{1-a^{j+1}}{1-a}.$$

Negative epsilon is obtained by reversing k and j-k. Each q_j has strictly positive weights on every finite path: **finite-depth absolute continuity is not infinite-history equivalence**.

Its expected occupation is

$$E_{q_j}K_j=\frac a{1-a}-\frac{(j+1)a^{j+1}}{1-a^{j+1}}\le\frac a{1-a}.$$

The squared Bhattacharyya/Hellinger affinity of q_j with the source law is exactly

$$F_j=\frac{\big(\sum_{k=0}^j a^{k/2}\big)^2}
{(j+1)\sum_{k=0}^j a^k}
\sim \frac{1+\sqrt a}{(1-\sqrt a)(j+1)}\longrightarrow0.$$

The prior PR #354 derived the same expression from normalized pure-state overlap. The *overlap* tends to zero; neither probability distribution loses its normalization.

## 4. SDB-03: explicit changed kernel and mutually singular histories

There exists a consistent modified birth process whose marginals are precisely q_j at every grade. Its k->k+1 transition is

$$\boxed{\widetilde P_j(k,k+1)=
\frac{a^{j+1-k}(1-a^{k+1})}{1-a^{j+2}}; \quad
\widetilde P_j(k,k)=1-\widetilde P_j(k,k+1).}$$

**Derivation.** The tilted cumulative distribution is Q_j(k)=(1-a^{k+1})/(1-a^{j+1}). The edge flux required to move from q_j to q_(j+1) is Q_j(k)-Q_(j+1)(k). Divide by q_j(k), simplify, and recover the displayed transition. It lies in [0,1]. The exact row equations then give q_j tilde-P_j=q_(j+1). This kernel is not P_j when a!=1 (already distinguishable at j=0).

Let Q be the resulting infinite path-history law. Under Q, K_j is nondecreasing and E_Q K_j is bounded independently of j by a/(1-a), so monotone convergence gives a finite K_infinity Q-almost surely. Therefore K_j/j ->0 Q-a.s. Under the unmodified native law P, K_j/j ->U with U in (0,1) P-a.s. The event {lim K_j/j=0} has Q mass 1 and P mass 0:

$$\boxed{Q\perp P\quad\text{on the full infinite path space}.}$$

Each finite marginal q_j and u_j nevertheless has identical full finite support. This is an **exact source-relative selection obstruction**, not a claim about a physical controller or zeta-zero realization.

## 5. SDB-04: the orientation of the information cost matters

Write H_geom(a)=-log(1-a)-[a/(1-a)] log a. From q_j(k)=a^k/Z_j,

$$D(q_j\|u_j)=\log\frac{j+1}{Z_j}+
(\log a)\,E_{q_j}K_j
=\log(j+1)-H_{\rm geom}(a)+o(1).$$

In the reverse direction,

$$D(u_j\|q_j)=\log\frac{Z_j}{j+1}-\frac j2\log a
=\frac{j|\log a|}{2}-\log(j+1)-\log(1-a)+o(1).$$

The first grows **logarithmically**; the second grows **linearly**. For a=p^(-4 epsilon), the latter linear coefficient is 2 epsilon log p. These are different information divergences, not a measured work expenditure. Data processing gives D(Q_(0:j)||P_(0:j)) >=D(q_j||u_j), so a full tilted history cannot have a uniformly finite information divergence from the source. This is consistent with and weaker than the path-space singularity. Physical energy needs a specified temperature, substrate and work protocol; the claim of constant additive work per step is unproved.

## 6. SDB-05: exact circle-to-line migration of local-character roots

For z complex, define the **local path-character** of the tilted probability state:

$$\chi_{j,a}(z)=\sum_{k=0}^j q_j(k)e^{iz(2k-j)L}
=\frac{e^{-ijzL}}{Z_j}
\frac{1-(a e^{2izL})^{j+1}}{1-ae^{2izL}},$$

with removable singularities filled by the finite sum. For j>=1, its zeros have ae^(2izL)=exp(2 pi i h/(j+1)) for h=1,...,j, modulo z-period pi/L. Thus every nontrivial zero satisfies

$$\boxed{\operatorname{Im}z=\frac{\log a}{2L}=-2\varepsilon.}$$

When a=1 the zeros lie on the real phase axis. Within this *specified local geometrically tilted family*, off-axis Fourier-character zeros are exactly accompanied by source reweighting; that reweighting is incompatible with native Pólya transport across all depths. This is a direct operational circle-to-line dictionary, but **z is not the zeta spectral parameter and these are not zeta zeros**.

## 7. SDB-06: controls—analytic zeros do not require a demon

A single static two-path positive source, w exp(izL)+(1-w)exp(-izL), has off-real zeros whenever 0<w<1 and w!=1/2:

$$\operatorname{Re}z=\frac{(2n+1)\pi}{2L},\qquad
\operatorname{Im}z=\frac{\log(w/(1-w))}{2L}.$$

No ongoing real-world energy intervention is needed merely for this analytic function to exist. Therefore the general slogan “off-line analytic zeros require constant added energy” is **REFUTED** without stronger assumptions about source, dynamics and spectral representation. Similarly, vanishing of a unitary phase correlation does not mean the underlying state lost norm.

In the genuine local zeta Euler factor, p^(-s j) tends to zero for fixed p and Re(s)>0. The j->infinity unweighted uniform fiber cannot simply be exchanged for analytic continuation of the completed global zeta function. Prime-specific charge labels must remain: the PR #352 exact beta_11^7=beta_29^5 collision shows why. Its non-Pisot and fake-4 controls also show that sharing the nontrivial zero divisor does not authenticate the source. PR #354's positive cosh off-line control remains mandatory.

## 8. The exact missing RH bridge

**Conditional only.** If every genuine nontrivial zero rho of the completed zeta function were represented by a source-faithful, projectively consistent path family of the above tilted form with epsilon=Re(rho)-1/2, AND the authentic completed arithmetic forced uniformly finite full-history relative entropy or a source-derived positive bounded two-sided dynamics for all these zero modes, the preceding theorem would force epsilon=0.

Neither the zero-to-path map nor its source-derived entropy bound or positive spectral pairing is presently constructed. Asserting that off-line zeros must be demon-controlled **before proving the map** would assume the missing result. The required bridge must recover original prime-power coefficients, source labels, Gamma/pole contribution, test-function domains and global Weil positivity while rejecting the biased-character, positive-cosh, fake-4 and non-Pisot controls.

**Claim status:** SDB-01 classical; SDB-02 through SDB-05 paper-proved locally with exact tests; SDB-06 refuted generic shortcut with explicit counterexample; SDB-RH unverified. RH and pi normality OPEN.

## Provenance and independent checks

- Original inherited SUCC formulas: PR #352 prime-Pisot dossier; PR #354 circle-line source stability; OLZF-04 and PCR-02 source dossiers pinned in those PRs. Same provenance family, not multiple independent authorities.
- Classical two-color Pólya urn with uniform asymptotic proportion: https://staff.math.su.se/daniel.ahlberg/notes-urns.pdf and https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_%28Siegrist%29/12%3A_Finite_Sampling_Models/12.08%3A_Polya%27s_Urn_Process
- KL chain rule and data processing: https://people.lids.mit.edu/yp/homepage/data/itbook-export.pdf
- Conditioned Markov processes/context: https://doi.org/10.1017/S0962492923000016
- Exact rational standard-library tests and an independent SymPy oracle accompany this dossier. Neither uses zeta-zero coordinates; neither constitutes peer review or a Lean proof.
