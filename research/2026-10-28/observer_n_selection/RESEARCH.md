# Operation Observer-N: arithmetic source, observer basis and postselection

**Date:** 2026-10-28. **Parent:** SUCC draft [PR #355](https://github.com/femboy2112/SUCC/pull/355), fixed at `6770de1d20400115031354ef1a797f3328ff892e`. New-to-SUCC observer/source synthesis only; the elementary probability/categorical facts are classical. Academic priority and cognition claims UNVERIFIED. No RH or pi-normality proof.

## 0. Steelman and the actual objects

The hypothesis is that natural-number-shaped, cheaply described or sequentially enumerable outcomes might be sampled earlier by a finite human observer, even if the base arithmetic field is the same across passive frames. The hypothesis concerns an **observer**, not a measured property of humans and not a change in the source distribution by itself. Keep the objects distinct:

1. **Source:** \((X,\mathcal F,P,T,S,V_p,\ldots)\), with arithmetic labels and original transition law.
2. **Passive encoding:** a bimeasurable invertible \(f\) transporting measures \(f_*P\), operations and observables together.
3. **Observer:** a measurement, finite observation filtration \(\mathcal F_j^o\), cost/attention weighting \(w_o\), selection event and acceptance record.
4. **Intervention:** a new dynamical kernel \(\widetilde T\), not merely a different observed marginal.

The natural-number *semiring* \((\mathbb N,+,\times,0,1)\) is initial in unital semirings: a unital morphism is fixed by 1 and hence by every sum of ones. It is not arbitrary as arithmetic. The code, radix, order, complexity prior, and choice of what can be observed are not determined by that algebra.

There is no countably additive uniform probability on all natural numbers: equal singleton mass \(c>0\) has divergent total, while \(c=0\) sums to zero. The *finite* uniform distribution on source grade \(j\) is instead grounded by SUCC's explicitly specified Pólya transition, not by a fictitious global uniform law.

## OBN-01 — finite observer selection reproduces the demon tilt exactly

The inherited authentic prime-power fiber \(\mathcal H_{p^j}\) has a split coordinate \(k=0,\dots,j\) and source law
\[
u_j(k)=1/(j+1).
\]
SUCC's original birth kernel has \(P_j(k,k+1)=(k+1)/(j+2)\), with stay probability \((j+1-k)/(j+2)\). Fix \(a\in(0,1)\), declare an **observer acceptance rule**
\[
P(A\mid K_j=k)=a^k.
\]
Without modifying the native birth kernel, Bayes' formula gives
\[
\boxed{P(K_j=k\mid A)=\frac{a^k}{Z_j}=q_j(k),\qquad Z_j=\sum_{\ell=0}^{j}a^\ell.}
\]
This is **identical** to the real-tilted probability marginal from PR #355, with \(a=p^{-4\varepsilon}\). The success rate and expected attempts are
\[
P(A)=\frac{Z_j}{j+1},\quad E[\text{attempts}]=\frac{j+1}{Z_j}\sim(1-a)(j+1).
\]
A code-cost interpretation \(w_o(k)=e^{-\lambda C_o(k)}\) and \(C_o(k)=k\), \(\lambda=-\log a\), realizes the same law but is only a **declared observer prior**, not an empirical human law. Selection effort is not automatically physical injected energy.

## OBN-02 — identical terminal observations can conceal different paths

At \(j=2\), native Pólya histories have \(P(K_1=1,K_2=1)=1/6\) and \(P(K_1=1,K_2=2)=1/3\). Selecting *whole source trajectories only by their terminal* \(K_2\), accepting with probability \(a^{K_2}\), gives
\[
P(K_1=1\mid A_2)=\frac{a+2a^2}{2(1+a+a^2)}.
\]
The **persistently modified birth process** in PR #355 instead has
\[
\widetilde P(K_1=1)=\frac{a}{1+a}.
\]
Both yield exactly the same terminal law \(q_2\), but the two-time discrepancy is
\[
\boxed{\frac{a}{1+a}-\frac{a+2a^2}{2(1+a+a^2)}
=\frac{a(1-a)}{2(1+a)(1+a+a^2)}>0.}
\]
For \(a=1/4\) these probabilities are \(1/7\) versus \(1/5\). Thus a specified endpoint-only selection protocol is distinguishable from persistent intervention by longitudinal observations.

## OBN-03 — even whole finite histories are postselectable

The full native and controlled history laws \(P^{(j)},Q^{(j)}\) live on \(2^j\) binary birth histories. All their path weights are strictly positive. Let
\[
L_j(\omega)=\frac{Q^{(j)}(\omega)}{P^{(j)}(\omega)},\quad
M_j=\max_\omega L_j(\omega).
\]
Accept a native history \(\omega\) with probability \(L_j(\omega)/M_j\). Conditional on acceptance, the entire finite-history law is exactly \(Q^{(j)}\), with rate \(1/M_j\). It follows that no fixed finite history alone separates **unrestricted history-dependent postselection** from intervention unless the observer protocol and its acceptance records are constrained.

Since \(L_j=E_P[L_{j+1}\mid\mathcal F_j]\), the sequence \(M_j\) is nondecreasing. From PR #355 we have the exact singularity \(Q\perp P\) of the consistent infinite-history laws. If \(M_j\le C\) for all j, then \(Q(Cyl)\le C P(Cyl)\) for all cylinders, extending by the monotone-class theorem to \(Q\ll P\), contradiction. Thus
\[
\boxed{M_j\to\infty,\qquad 1/M_j\to0.}
\]
The **selection rate** must vanish, but no physical Landauer-energy cost has been derived. This proof inherits the source singularity theorem from the PR #355 provenance family; it is not an independent witness to that premise.

## OBN-04 — passive frames, coarse observation and false arithmetic relabeling

For bimeasurable bijection \(f\), the pushforward measures satisfy
\[
D_{\mathrm{KL}}(f_*Q\Vert f_*P)=D_{\mathrm{KL}}(Q\Vert P),\quad
Q\perp P\iff f_*Q\perp f_*P.
\]
For a shared noninjective measurement \(m\), the data-processing inequality yields
\[
D_{\mathrm{KL}}(m_*Q\Vert m_*P)\le D_{\mathrm{KL}}(Q\Vert P).
\]
Conditioning on observer acceptance is **not** a common pushforward: it changes the observed law nonlinearly after normalization.

An arbitrary bijection of underlying labels is not a semiring automorphism. Example: switch \(2\leftrightarrow4\). Then \(f(2\cdot2)=2\ne f(2)f(2)=16\). To call this a passive frame, one must also transport the multiplication \(x\otimes y=f(f^{-1}(x)\cdot f^{-1}(y))\), the prime predicate, source labels and measure. Arbitrarily renaming a composite a prime is not an arithmetic discovery.

The infinite source path space may have uncountably many histories even though each finite observation/description is indexed by natural numbers. Finite enumerability does not entail an intrinsic N-uniform probability over complete histories.

## OBN-05 — local zero locations are not an observer-neutral witness

PR #355's local tilted Fourier character has zeros shifted from the real phase axis to \(\Im z=\log(a)/(2\log p)\). OBN-01 now realizes that **same local off-axis zero character** by selecting snapshots from an unchanged source. Hence an off-axis **local-character** zero does not, on its own, establish a physical intervention or an information pump inside the arithmetic dynamics.

This is **not** a zeta-zero construction. The completed zeta function's genuine nontrivial zeros require an authenticated map from original prime-power Euler data and archimedean gamma/pole completion to the virtual path spectrum. The Gibbs probability \(n^{-s}/\zeta(s)\) exists for real \(s>1\), not as an ordinary probability at the critical line. The earlier off-line-cosh, fake-4, non-Pisot, composite equilibrium and clock-collision controls remain.

## Verdict, source map and next discriminator

**PAPER-PROVED LOCAL:** exactly realized snapshot selection, exact two-time difference, finite whole-history rejection and vanishing acceptance conditional on inherited singularity. **CLASSICAL:** initial semiring, no N-uniform countably additive measure, KL coordinate invariance, data-processing. **REFUTED SHORTCUT:** finite tilted observation implies actual source intervention. **HYPOTHESIS:** human observers prioritize N-shaped descriptions; no measurements collected. **UNVERIFIED:** an RH-grade completed zeta zero-to-source-path spectral map, Weil-positive form or physical Maxwell-demon energy law. RH/pi-normality OPEN.

Sources: SUCC PRs [#352](https://github.com/femboy2112/SUCC/pull/352), [#354](https://github.com/femboy2112/SUCC/pull/354), [#355](https://github.com/femboy2112/SUCC/pull/355) (one source ancestry); [Lorscheid on initial semiring](https://www.lorscheid.org/notes/2018-Blueprints/versions/lecturenotes180405.pdf); [CMU on uniform measures on N](https://www.stat.cmu.edu/tr/tr814/newoldtr814.pdf); [Oxford Pólya/de Finetti](https://www.stats.ox.ac.uk/~steffen/teaching/grad/definetti.pdf); [SIAM data processing](https://epubs.siam.org/doi/full/10.1137/25M180874X); [postselection inference](https://doi.org/10.1146/annurev-statistics-100421-044639). No external prior art is claimed as validating the new SUCC synthesis.
