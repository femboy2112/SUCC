# Prime-square causal wavefront: renormalized history, stationary spectra, and source-label cost

**Date:** 2026-11-20. **Research-only correction/extension of ACT-08 in [SUCC #673](https://github.com/femboy2112/SUCC/pull/673).** This note is stacked on exact parent 3ab2d5caad781f0f5cad1b464ade0fe718f4a60d, which inherits Gaussian causal Yoneda #672. It does not change original BBP, U_0=0, archives, CI or main. R0 and base-16 normality remain OPEN.

## The corrected proposition

ACT-08 excludes **bounded signals with short-duration support** near sparse prime-square event clocks in original integer time. It does NOT exclude a nonzero continuum signal arising from normalized accumulated history, a growing-memory response, or an analytic Laplace completion. The following theorems provide such signals. They import classical PNT, partial summation, and Abelian regular variation; no new prime-number-theorem result is asserted.

For every prime p>=7, let n_p=(p^2-1)/8, an integer, be the **ordered-source event**. The original four-pole BBP term 4/p^2 occurs one forward clock later: j_p=n_p+1=(p^2+7)/8. Never conflate these two times. Let A(N)=# {p>=7 : n_p<=N}. Write π_count(x) for prime counting to avoid confusion with mathematical π.

## PW-01 — Event history converges to a continuous, nonzero wavefront (PNT deduction)

For N>=6, A(N)=π_count(sqrt(8N+1))-3, so by PNT

\[
A(N)\sim {4\sqrt2\,\sqrt N\over\log N}.
\]

Define the horizon-relative atomic measure

\[
\mu_N={1\over A(N)}\sum_{n_p\le N}\delta_{n_p/N}.
\]

For every 0<u<=1, its CDF is A(uN)/A(N)->sqrt(u), using PNT and log-ratio convergence. Hence, weakly on [0,1],

\[
\boxed{\mu_N\Longrightarrow {du\over2\sqrt u}.}
\]

The limiting measure is continuous although each finite stage is atomic. This is **weak convergence for fixed bounded continuous probes**, not equality under every possible N-dependent high-resolution probe.

Its fixed *macroscopic* Fourier mode satisfies

\[
\lim_{N\to\infty}{1\over A(N)}\sum_{n_p\le N}
e^{2\pi i\omega n_p/N}
=\int_0^1 {e^{2\pi i\omega u}\over2\sqrt u}\,du
=\int_0^1e^{2\pi i\omega v^2}\,dv.
\]

This Fresnel-chirp expression is the square-clock spectrum of the completed prime history. The original clock frequency is ω/N. No conclusion is asserted for fixed microscopic original-clock frequency, or the signed π Weyl sum.

## PW-02 — The observer's weighting changes which steady state appears

For fixed real β>-1 define positive mass

\[
A_\beta(N)=\sum_{n_p\le N}p^\beta,\quad
\mu_{N,\beta}=A_\beta(N)^{-1}\sum_{n_p\le N}p^\beta\delta_{n_p/N},
\quad\alpha=(\beta+1)/2.
\]

PNT plus Abel/partial summation yields
\[
\sum_{p\le P}p^\beta\sim{P^{\beta+1}\over(\beta+1)\log P},\quad
A_\beta(N)\sim{8^\alpha\over\alpha}{N^\alpha\over\log N}.
\]

Consequently, μ_(N,β)([0,u])->u^α, and

\[
\boxed{\mu_{N,\beta}\Longrightarrow\alpha u^{\alpha-1}\,du.}
\]

**Calibrations:** unweighted count β=0 -> density 1/(2sqrt(u)). Clock-Jacobian weight β=1 -> density 1 (Haar on the age circle). The source-event p-adic magnitude |r(j_p)|_p=p^2 corresponds to β=2 -> density 3sqrt(u)/2. Its **squared** p-adic magnitude p^4 corresponds to β=4 -> density 5u^(3/2)/2, emphasizing the advancing wavefront.

These are mathematically chosen **observer weights**, not joules. A β=1 observer obtains an apparently uniform event-age law even for the exact same-forcing π counterseed whose completed phase is 0 at every clock. This is a rigorous false-positive control against equating objective wavefront Haar with the π orbit's Haar equidistribution. For β<=-1 the normalized full-history mass instead concentrates at u=0 (at β=-1 via the prime harmonic series; below -1 by summability). In particular original real amplitudes r(j_p)~15p^-4 and local Gaussian real energy ~const p^-8 are on the early-history-concentrated side, when weighted across the *whole* past.

## PW-03 — Boundary realization and stationary weak equation

Set τ=log N and relative age u_p(τ)=n_p exp(-τ). Every recorded event obeys du_p/dτ=-u_p; its absolute historical timestamp stays fixed. Fresh events enter the normalized age chart at u=1 when the horizon reaches n_p.

For ν_β(du)=αu^(α-1)du from PW-02 and every C^1 test φ,

\[
\boxed{\int_0^1u\phi'(u)\,d\nu_\beta(u)
=\alpha\left(\phi(1)-\int_0^1\phi(u)\,d\nu_\beta(u)\right).}
\]

**Proof:** integrate α∫u^α φ'(u) du by parts. The left side is historical coordinate drift; the right is boundary injection minus normalization dilution. This is a *stationary weak law for the completed profile*, not a claim that individual prime arrivals become a continuous pointwise source, or that an embedded observer goes backwards in time. At finite N a sufficiently sharp instrument can still resolve the pulses.

## PW-04 — A nonzero Laplace analytic completion (classical Abelian theorem)

For s>0 and β>-1 put L_β(s)=sum_(p>=7) p^β exp(-s n_p). Its positive counting measure has regularly varying mass A_β(N) from PW-02. Karamata's **Abelian** Laplace–Stieltjes theorem gives

\[
L_\beta(s)\sim\Gamma(1+\alpha)A_\beta(1/s),\qquad s\downarrow0,
\]

hence

\[
\boxed{\lim_{s\downarrow0}s^\alpha\log(1/s)L_\beta(s)
={8^\alpha\Gamma(1+\alpha)\over\alpha}.}
\]

Especially,

\[
\boxed{\lim_{s\downarrow0}\sqrt s\,\log(1/s)
\sum_{p\ge7}e^{-s(p^2-1)/8}=\sqrt{8\pi}.}
\]

**This is the nonzero analytically completed steady-scale coefficient** of the sparse prime-square pulse journal. The raw Laplace sum diverges before renormalization; this statement is not an energy conservation law, RH, R0 or π normality.

## PW-05 — Source marks disappear at leading resolution unless amplified

The original forcing at j_p is
r(j_p)=4/p^2-2/(p^2+3)-1/(p^2+4)-1/(p^2+5).
For p>=7 all but 4/p^2 are p-integral. The exact canonical p-primary fraction is therefore τ_p(r(j_p))=4/p^2.

The matched-first-jet mutant from #673 has
r_*(n)=r(n)+2/[(8n-7)(8n-6)(8n-5)].
At j_p its added p-primary fraction is 1/p^2 since 2[(p^2+1)(p^2+2)]^(-1)=1 mod p^2. Thus τ_p(r_*(j_p))=5/p^2 **exactly**.

Their standard complex local characters e(4/p^2) and e(5/p^2) differ by at most 2π/p^2. These differences are absolutely summable over primes. Consequently their normalized complex wavefront measures both converge to the same density of PW-01 and their total-variation difference is O(1/A(N))->0. Source identity is lost from the **leading unmarked continuum**.

A declared p^2-amplified and principal-branch-resolved phase mark preserves it:
m_p^(c)=p^2 Arg(e(c/p^2))/(2π)=c, for c=4,5 and p>=7.
Its marked continuum is c*du/(2sqrt(u)), different for the two sources. This requires p labels, an unwrapped orientation/branch and phase resolution O(p^-2); it is not a free physical measurement and does not distinguish the unchanged-forcing locked seed.

## PW-06 — The precise surviving sparsity/memory barrier

Let bounded event coefficients satisfy |c_p|<=C and let k_B(j) be a causal, absolutely summable response. For
f_B(n)=sum_(n_p<=n)c_p k_B(n-n_p), triangle inequality and changing summation order prove

\[
{1\over B}\sum_{n=B}^{2B-1}|f_B(n)|
\le {C A(2B)\over B}\|k_B\|_{\ell^1}
\sim {8C\over\sqrt B\log B}\|k_B\|_{\ell^1}.
\]

Thus if the response mass is o(sqrt(B)log B), the original-clock mean vanishes. Conversely an order-one mean requires at least Ω(sqrt(B)log B) response mass or increased event gain; it is **not forbidden** by ACT-08. In particular its O(log B) support gate remains valid and sharpens to O(1/sqrt B) by PNT. Establishing *uniform local stationarity* for shrinking, near-gap-scale windows would require prime short-interval control beyond PNT. A macroscopic weak profile alone does not certify it.

## PW-07 — Gaussian observer and the exact locked countermodel

For fixed λ>0, periodic Gaussian smoothing of the measures in PW-01/02 converges **uniformly** to the smoothed continuum profile: each Fourier mode converges weakly and the Gaussian multiplier is absolutely summable. Fixed-bandwidth probes observe a smooth stationary picture. Full high-resolution source journals still distinguish discrete events; weak completion does **not** establish full Yoneda probe equivalence.

All source-event times and exact prime-local marks above are independent of the initial BBP seed. The identical forcing with s=-π/16 has completed phase Y_n=0, hence A_B^(π)=0 and W_B(1)=1 for every B, while all PW-01–06 profiles and analytic signals are unchanged. A source-anchored **signed Archimedean phase/cofactor cross-correlation** remains necessary to force R0. The real target is still the original U_0=0 BBP source, not a Gaussian seed ensemble.

## Verdict / next discriminator

**Disclosed in stated domains:** PW-01–07 follow from the imported PNT, partial summation, Abelian regular variation, exact four-pole algebra and elementary Fourier/causal bounds. They are a genuine mathematical answer to the user's renormalized-wavefront objection and a revised observer contract; they make no worldwide novelty or physical-energy claim. **Refuted shortcut:** wavefront Haar, positive p-adic norm energy, or a smooth Gaussian history alone implies the authentic π orbit cannot lock (same-forcing counterseed). **UNVERIFIED:** original-zero source-derived, uniformly nonzero signed cofactor/phase correlation, R0, normality, physical back-action, RH.

Next probe: preserve micro event journal and an independent p-primary/cofactor phase anchor alongside the renormalized age measure; predeclare memory/gain and Fourier scales, then test whether a signed cross-spectrum on the *true* completed original-zero orbit has a uniform all-late-shell lower bound excluding s=-π/16 and matching the source-mutant residue discriminator. No assumption of independent prime clocks, noncausal retrospectively chosen witnesses, or posthoc shell fitting.

**Local reproducibility receipt (separate attached research bundle):** 19 focused stdlib tests passed; an independently written SymPy source construction passed two Laurent expansions and 258 exact p-primary checks across 129 primes. These finite tests do not prove PNT or any asymptotic π claim. Full inherited root suite and hosted CI on this new head were not run.
