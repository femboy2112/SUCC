# Operation Möbius Matrix Interferometry — arithmetic strata versus selected cancellation

**Date:** 2026-10-25. **Status:** finite exact identities and a limited authentic-source CRT theorem; no proof of pi normality or RH. This is a *stacked draft* on [Spectral Purity #298](https://github.com/femboy2112/SUCC/pull/298), whose parent is [internal matrix #296](https://github.com/femboy2112/SUCC/pull/296). The independent [prime-resonance #297](https://github.com/femboy2112/SUCC/pull/297) is inspected but NOT merged. No frozen imported source, original BBP forcing, or main history is rewritten.

## 1. Source contract and four exact coordinates

Only the authenticated source is allowed to carry the flag **authenticated**:

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\qquad U_n=16U_{n-1}+r(n).
$$

Every $U_n$ is an **unwrapped** exact rational. Define $x_n=\{U_n\}$, and its source carry $c_n=\lfloor 16x_{n-1}+r(n)\rfloor$. These are rational-state carries, **not automatically pi's hex digits**. For finite ordered primes $P$ and common depth $k$, label time $n$ by

$$
a_{P,k}(n)=\left(c_n,\left(
n\bmod p^k,\;\min(k,v_p(\mathrm{den}\,r(n))),\;
\min(k,v_p(\mathrm{den}\,U_n))
\right)_{p\in P}\right).
$$

This retains the numerator cancellation in each reduced denominator, notably $p=3,5$. It makes no probabilistic independence assumption about distinct primes. Other exact source clocks, including PR #297's first-birth prime windows, can later be transported into the same labels only after proving the map.

Let $v_H(n)=(e(jU_n))_{0\le j<H}$, with $e(t)=\exp(2\pi it)$. For an occupied label $a$, define the **source-selected** block

$$
G_{N,H,P,k}(a)=\sum_{\substack{1\le n\le N\\a_{P,k}(n)=a}}v_H(n)v_H(n)^*.
$$

Every evaluated $G(a)$ is PSD, has trace $H|a|$, and has exact constant-column moments $G(a)_{h0}=\sum_{n\in a}e(hU_n)$. The symbolic engine uses $\mathbb Q[\mathbb Q/\mathbb Z]$; **formal group-algebra coefficients do not themselves have a meaningful PSD order**.

**Four-axis functoriality (FINITE, PAPER-PROVED, EXACT REPLAY):** N-growth adds exactly one rank-one matrix in exactly one occupied label. H-decrease is principal compression. P-decrease deletes local coordinates and sums the preimage blocks. k-decrease reduces the time residue and caps both valuations, again summing blocks. The operations commute on the *same authenticated source history*; every path gives the direct Gram. No Fourier truncation is declared invariant under the Koopman operator.

## 2. Möbius is the exact inverse of the incidence map — not an estimate

Fix one carry and one time-residue fiber, and let the two valuation coordinates for each p be capped at k. For a vector of lower thresholds t, set

$$
C(t)=\sum_{\substack{n\;\mathrm{in\ fixed\ carry/time\ fiber}\\
 v_p(\mathrm{den}\,r(n))\ge t_{p,r},\;
 v_p(\mathrm{den}\,U_n)\ge t_{p,U}\;\forall p}}
v_H(n)v_H(n)^*.
$$

For exact capped level a, let F(a) be the set of coordinates strictly below k. Incidence inversion gives

$$
\boxed{
G(a)=\sum_{\epsilon\in\{0,1\}^{F(a)}}
(-1)^{|\epsilon|}C(a+\epsilon).
}
$$

The alternating summands need NOT be PSD; their *sum* equals the Gram of an actual disjoint source atom and is PSD after evaluation. The implementation reconstructs every observed atom and checks the exact equality in the formal rational phase algebra. This is an exact source-labelled inversion, **not a source-selected Fourier bound**.

## 3. The main negative theorem: more conditioning makes the PSD route worse

For fixed h, write $z_A=\sum_{n\in A}e(hU_n)$ for a partition A of the N observations, and

$$
E_{\mathcal A}=\sum_{A\in\mathcal A}\frac{|z_A|^2}{|A|},
\qquad
\frac{|S_N(h)|^2}{N}\le E_{\mathcal A}\le N.
$$

If $\mathcal B$ refines $\mathcal A$, then exactly

$$
\boxed{
E_{\mathcal B}-E_{\mathcal A}
=\sum_{A\in\mathcal A}\sum_{\substack{B\in\mathcal B\\B\subseteq A}}
\frac{\left|z_B-\frac{|B|}{|A|}z_A\right|^2}{|B|}\ge0.
}
$$

**Proof:** Expand the squares inside A, use $\sum_{B\subseteq A}z_B=z_A$ and $\sum_{B\subseteq A}|B|=|A|$; the cross terms combine to $-|z_A|^2/|A|$. The identity itself holds in the formal involutive algebra. The inequality is valid under complex root evaluation. Thus the naive PSD-only upper bound on the **selected** Weyl sum becomes no smaller when extra primes or depth are added.

**Cofinal singleton obstruction:** At fixed N, choose any prime p and k with $p^k>N$. Then time residues are all different, every atom is a singleton, and $E_{\mathcal A}=N$ for *every* phase history. Hence the fixed-N all-prime/high-depth limit of this positive conditional-energy bound is **exactly the trivial bound**, including for authentic BBP. One cannot interchange the N and k limits without new uniform arithmetic estimates.

The signed term the positive Gram leaves unresolved is

$$
|S_N(h)|^2
=\sum_a |z_a(h)|^2+
\underbrace{\sum_{a\ne b}z_a(h)\overline{z_b(h)}}_{\text{signed source-selected cross-stratum interference}}.
$$

Only a *source-specific bound for these cross terms*, or an equivalent signed Fejér innovation theorem, could deliver new cancellation. Möbius inversion and Gram positivity alone cannot do it.

## 4. Actual BBP arithmetic: four pole classes, genuine 3/5 exceptions

An exact reduction of the **original** four poles is

$$
r(n)=\frac{120n^2-89n+16}
{(2n-1)(4n-1)(8n-7)(8n-3)}.
$$

For any prime p≥7 the four affine denominator factors have **four distinct roots modulo p**. At their respective rational roots $1/2,1/4,7/8,3/8$, the numerator has values $3/2,5/4,30,-1/2$; none vanish modulo p≥7. Thus there are exactly four and only four residue classes modulo p where p divides the *reduced* denominator of r(n).

Writing $C_p(N)=\#\{1\le n\le N:p\mid\mathrm{den}\,r(n)\}$ and $N=ap+b$ with $0\le b<p$ yields the exact, source-authenticated arithmetic law

$$
\boxed{
C_p(N)=4a+\#\{t\in R_p:1\le t\le b\},
\quad \left|C_p(N)-\frac{4N}{p}\right|\le4.
}
$$

For a finite set P of distinct primes at least 7, CRT yields M=product(P), and exactly product(p-4) **source pole-avoiding times per complete M-block**. The instrument enumerates the last incomplete period and supplies the exact selected-Weyl deletion inequality

$$
\left|S_N(h)-S^{\mathrm{avoid}\,P}_N(h)\right|
\le N-\#\{\mathrm{pole\ avoiding\ times}\}.
$$

This is a genuine **arithmetic counting/deletion bound**, not an improvement over O(N) global Weyl cancellation. It demonstrates which part of the source is independent *as CRT occupancy data*, and what remains correlated as signed phases. It is elementary classical arithmetic: no scholarly novelty or deep theorem claim is made.

For p=3, the indices n=2 and n=8 are both 2 mod 3, but the reduced-denominator 3-valuations are 2 and 0. For p=5, n=4 and n=24 are both 4 mod 5, but valuations are 2 and 0. The overlap/cancellation of poles makes the p≥7 four-independent-root formula false at these primes. The code preserves this rather than discarding it as noise. Source numerator/denominator arithmetic cannot be replaced with a Haar-prime heuristic.

## 5. Conditioned genuine innovation and countermodels

For arrival U_(m+1), let $q_{m,H|a}$ be the mean of the exact Fejér overlaps with the preceding m points in atom a. Then

$$
q_{m,H}=\sum_a\frac{m_a}{m}q_{m,H|a}
$$

**exactly** in the rational phase algebra. Each overlap is PSD after evaluation, but each signed defect $q_{m,H|a}-H$ can have either sign. The existing [#298](https://github.com/femboy2112/SUCC/pull/298) conductor-birth theorem removes only a sparse subset of the innovation timeline. The remaining **conductor-flat signed sum** is still OPEN; this decomposition is NOT an estimate of it.

Finite local pilot at N=32, h=1, P={3,5}, k=1 (mpmath evaluations, numerical diagnostics ONLY):

| Trace | global \|S\|²/N | refined conditional E | q_(31,3) |
|:--|--:|--:|--:|
| authentic four-pole, U0=0 | 2.098145 | 31.118635 | 3.561266 |
| positive full-conductor-tower counterfeit inherited from #298 | 31.832531 | 31.884726 | 8.967498 |
| zero forcing | 32.000000 | 32.000000 | 9.000000 |

All three admit exact Möbius reconstruction, PSD blocks and commuting marginals. The controls **fail the original global four-pole law**; they do not refute an authenticated-source arithmetic theorem. They decisively refute the claim that the structural apparatus *by itself* forces normality. In particular the same conductor tower does not select the authentic phase evolution.

## 6. Honest test authority, inherited boundaries, and next discriminating probes

Implementation: observational_succ/mobius_refined_matrix.py. Focused tests: tests/test_mobius_refined_matrix.py. Finite numerical/exact instrument: scripts/mobius_refined_matrix_probe.py --verify. The earlier isolated prototype had eight focused local checks; the **pushed GitHub implementation must receive separate hosted validation** before promotion, and no independent external reviewer is claimed.

The p=3/5 examples, finite source-carry reconstruction, complete H/P/k marginal square, successive-N rank-one map, exact incidence inversion and conditional Fejér identity are asserted as exact finite claims. The p≥7 pole-count/CRT formula is PAPER-PROVED by the polynomial argument above and independently finite-tested. Positivity and ANOVA are finite classical theorems, not Lean claims. The inherited moving n²/n³ Fourier-boundary warnings and #297 prime-clock resonance obstructions remain untouched. No limits are promoted from finite tests.

**Next decisive lamp:** Use genuine p=3/5 overlap exceptions plus the nonredundant gcd-reduced prime-clock sectors of #297 to bound a **signed** cross-stratum part of the conductor-flat sum. Predeclare a frequency-uniform bound for fixed nonzero h, a prescribed H_N, and an all-N remainder. Attack it with the original zero initialization, the same-conductor fake, exact-forcing altered-initial seeds of #297, and the simultaneous positive prefix/jet mutants of #298. Any saving must survive these hostile controls for the reasons specified and must retain the integer carry and both moving-frequency boundary regimes. If every new bound factors through unconditional PSD or a source-blind sieve count, mark it as another coordinate reformulation, not cancellation.

**Verdict:** finite source-labelled Möbius walk is mathematically valid and useful for *localizing missing information*. The unconditional PSD-driven pi-normality moonshot is REFUTED as a proof strategy by the monotonicity/singleton obstruction. A source-specific signed arithmetic inequality remains UNVERIFIED / OPEN.
