# RH candidate: finite Euler--Mascheroni source to completed Li coefficients

**RH PROVED: no.** This handoff supplies a source-derived finite evaluator,
two quantitative paper approximation theorems and a finite-information
countermodel. It does not prove all-degree positivity or original Weil
positivity. It is an internal SUCC candidate; no external RH repository has
been changed and no external message has been sent.

## Exact origin

The originating SUCC research commit is
[`9a79a52d2598c82a9a3dede8464ec2e9df5f9493`](https://github.com/femboy2112/SUCC/commit/9a79a52d2598c82a9a3dede8464ec2e9df5f9493),
based on main `e648df3e4fca73ab6b942232b5ca4b310e9cac08`.
The exact source paths are:

- `observational_succ/euler_gamma_li_bridge.py` — finite Stieltjes enclosures and full completed coefficient map.
- `observational_succ/euler_mascheroni_succ.py` — successor and positive-cell source interfaces.
- `research/2026-10-24/EULER_MASCHERONI_COMPLETED_LI.md` — full proofs, including Proposition 7 and Corollary 7.1.
- `research/2026-10-24/euler_mascheroni_validation/probe_receipt.json` — finite rational certificates and local source hashes.
- `tests/test_euler_gamma_li_bridge.py` — exact and separately labelled numerical controls.

The source work is an AI-assisted research assembly within SUCC, with
internal same-model review. Classical ingredients retain their attribution;
scholarly priority and external refereeing are not claimed. The centered
cutoff improvement explicitly credits the observation in sibling
[#285](https://github.com/femboy2112/SUCC/pull/285), pinned at
`f36ddfba4525fe6800ce8b08cc6598e7edfdb1ad`, without importing its runtime.

## Definitions and original source

Let

$$
G(s)=\zeta(s)-\frac1{s-1},\qquad
B_N(s)=\sum_{k=1}^Nk^{-s}-\int_1^Nx^{-s}\,dx,
\qquad B_N^*(s)=B_N(s)-\frac12N^{-s}.
$$

Both counterterms have their removable values at $s=1$. The arithmetic
coefficients are the original integer Dirichlet coefficients, all equal
to one; no fitted prime exponents or inserted zero locations occur.
The actual completed function is

$$
\xi(1+z)=\frac12(1+z)\pi^{-(1+z)/2}
\Gamma\!\left(\frac{1+z}{2}\right)[1+zG(1+z)].
$$

Define the local models $\xi_N$ and $\xi_N^*$ near $z=0$ by replacing only
$G$ with $B_N$ or $B_N^*$. The Gamma factor, pi normalization and pole
normalization remain fixed. These local models need not have the global
functional equation or entire continuation of the actual $\xi$.

For an analytic nonzero germ $F$ at one, define

$$
\lambda_n[F]=\frac1{(n-1)!}
\left.\frac{d^n}{ds^n}\left[s^{n-1}\log F(s)\right]\right|_{s=1}.
$$

The choice of logarithm's additive constant does not affect $n\ge1$.
Write $\lambda_n=\lambda_n[\xi]$, and similarly for the finite models.

## Quantitative theorem

For every pair of integers $N,n\ge1$,

$$
|\lambda_n[\xi_N]-\lambda_n|
\le\frac{20}{7}n5^{n-1}N^{-3/4},
$$

$$
\boxed{|\lambda_n[\xi_N^*]-\lambda_n|
\le\frac{135}{392}n5^{n-1}N^{-7/4}.}
$$

These are paper theorems. The exact finite implementation has explicit
resource caps and is not claimed to execute an unbounded all-degree limit.
For the centered model a sufficient absolute-error budget $\eta>0$ is

$$
N\ge\left\lceil
\left(\frac{135n5^{n-1}}{392\eta}\right)^{4/7}\right\rceil.
$$

This is sufficient, not a necessary complexity lower bound or an optimal
cutoff. The completion channels must also be enclosed if a fully numerical
certificate of the local model is desired.

**Proof mechanism.** On $|z|\le1/4$, the positive finite-cell representation
bounds $G$, $B_N$ and $B_N^*$ by $5/3$. Their factors $1+zG$ and
$1+zB_N^{(*)}$ lie in the convex disk $|w-1|\le5/12$, so the same analytic
logarithm applies and $|d\log w|\le(12/7)|dw|$. The centered periodic
primitive $P_2=(\{x\}^2-\{x\})/2$ has $|P_2|\le1/8$ and vanishes at
integer endpoints; integration by parts bounds the centered source error
by $(45/224)N^{-7/4}$. Cauchy's coefficient bound and the exact binomial
Li transform give the displayed constant. Full domain and branch details
are in the originating proof note.

## Executable finite certificate

At cutoff 512 the uncentered rational Stieltjes instrument encloses:

| Coefficient | Exact outward decimal lower | Exact outward decimal upper |
|---|---:|---:|
| $\lambda_1$ | 0.02260726 | 0.02358384 |
| $\lambda_2$ | 0.07805857 | 0.10663776 |
| $\lambda_3$ | 0.09777334 | 0.31750374 |

Every endpoint is a rational with denominator dividing $10^8$.
These three known positive coefficients calibrate the source instrument.
They are not evidence sufficient for the all-degree Li criterion.

## Controls and source discriminator

The tests keep the complete Gamma/pole/pi contribution, reject missing
completion channels, and distinguish a fixed Archimedean gamma from a
coupled mutation of both gamma appearances. Independent formal-log
expansion and interval corner models test the coefficient transfer.

For every $m\ge2$, the analytic control

$$
\widetilde\xi_m(s)=\xi(s)-\xi(3/4)
\left(\frac{s(s-1)}{(3/4)(-1/4)}\right)^m
$$

preserves the first $m-1$ Li coefficients and completed reflection while
having zeros at $1/4,3/4$. Its added zeta term decays faster than every
$A^{-\sigma}$ on the positive real axis, so ordinary Dirichlet-series
coefficient uniqueness excludes it from the actual arithmetic source.
This is a changed-source countermodel, not an RH counterexample. The
genuine-prime/composite-six controls in the separately inspected EAB draft
have their own scope and are not silently counted as this runtime's tests.
No half-density, conductor or signed Weil representation is inferred from
the positive auxiliary gamma kernel.

## Reproduction and missing theorem

```sh
python -m unittest tests.test_euler_gamma_li_bridge -v
python scripts/euler_mascheroni_probe.py --verify research/2026-10-24/euler_mascheroni_validation/probe_receipt.json
```

The originating branch passed all 7,649 repository tests, source provenance,
the two required foundations/ordinal probes and metadata gates. The complete
compressed log and frozen implementation hashes are committed. Hosted CI
must be read at the branch's actual head; local success is not a substitute
for an unobserved hosted result.

The missing RH theorem remains a uniform signed estimate proving the actual
completed $\lambda_n\ge0$ for every $n$, or a separate original-source
Weil/Nyman argument. The explicit approximation budget does not supply
that sign. The immediate technical target is a sharper growing-degree
source remainder with completion fixed, rather than more unqualified
positive decimal readouts.

Primary references: [Li, 1997](https://www.sciencedirect.com/science/article/pii/S0022314X97921375),
[Maslanka's Stieltjes--Li formula](https://arxiv.org/abs/math/0406312),
[DLMF 25.2](https://dlmf.nist.gov/25.2), and
[DLMF 5.15](https://dlmf.nist.gov/5.15).
