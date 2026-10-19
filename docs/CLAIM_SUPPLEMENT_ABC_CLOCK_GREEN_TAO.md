# ABC prime-clock / Green--Tao claim supplement (2026-10-19)

Full proofs, assumptions, controls and falsification targets are in [the research dossier](../research/2026-10-19/ABC_CLOCK_GREEN_TAO.md). No original historical claim ID is overwritten. This is a new-to-project arithmetic track, NOT a source-derived Weil positivity result.

| ID | Exact scope | Status | Evidence / falsifier |
| --- | --- | --- | --- |
| ABC-CLK-01 | Each genuine p, integer k>=1; conditional Haar law for primitive (a,b) in Z_p²: no-slot (p-2)/(p+1), each slot exact k (p-1)/((p+1)p^k) | **PROVED LOCAL** | Residue counting and determinant-one Haar transport; exact independent enumeration mod p^(k+1) |
| ABC-CLK-02 | Each 0<theta<1; sum_{n<=X} ris(n)^theta <= C_theta X | **PROVED LOCAL** | Nonnegative Dirichlet-convolution coefficients and convergent Euler product |
| ABC-CLK-03 | For all eps>=0, eta>0, primitive triple count with X<c<=2X and c>rad(abc)^(1+eps) is O(X^(8/5-eps/[5(1+eps)]+eta)) | **PROVED LOCAL** | Holder + ABC-CLK-02 + optimized balanced/unbalanced split; no uniform K_eps proved |
| ABC-CLK-04 | Each odd-prime 3-AP p-d,p,p+d has a primitive linear lift with ris=1 and square lift (p²-d²,d²,p²) with ris>=p but c/rad<1/3 | **PROVED LOCAL**; infinite instances require **EXTERNAL THEOREM Green--Tao** | Exact factorization; composite 7,8,9 mutation is an ABC hit |
| ABC-CLK-05 | Exact convex envelope is the supremum of affine log branches; **assuming ABC**, its positive-epsilon restriction is locally finitely piecewise linear | **CLASSICAL REFORMULATION / CONDITIONAL PROOF** | Needs the full ABC bound at a smaller positive epsilon, not obtained from finite census |
| ABC-CLK-06 | Unordered c<=1200 finite envelope and held-out c>600 exact rational comparisons | **TESTED MODEL** | `scripts/abc_clock_green_tao_probe.py`; `tests/test_abc_clock_families.py` |
| ABC-CLK-07 | W-tricked clock weights automatically yield a family-uniform global ABC bound, positive-density exceptional set, or sufficient high-depth uniformity | **UNVERIFIED** | Missing growing-modulus/sieve majorant, tails and nonlinearity handling |
| ABC-CLK-08 | These elementary positive moments identify with the signed completed Weil distribution and prove RH | **REFUTED AS INFERENCE** | The SUCC source-to-Weil identification and Schur sign are still open |

**Reproduction:** `python -m unittest tests.test_abc_clock_families` or `python -m unittest discover -s tests -p 'test_abc_clock_families.py'`, plus `python scripts/abc_clock_green_tao_probe.py --limit 1200`. All new numerical comparisons are exact rationals; no historical source bytes were changed.

Primary sources: Green and Tao (2008), https://annals.math.princeton.edu/2008/167-2/p03 ; Tao's transference/W-trick lecture, https://terrytao.wordpress.com/2010/06/05/254b-lecture-notes-7-the-transference-principle-and-linear-equations-in-primes/ .


## Literature correction and additional calibrated claims

The 2026 Bernert–Browning–Lichtman–Teräväinen [paper](https://arxiv.org/html/2410.12234), Theorems 1.2–1.3, proves \(N_\lambda(X)\ll X^{(23\lambda+3)/40+\delta}\) for \(0<\lambda\le2\), and \(N_\lambda(X)\ll X^{3/5+\delta}\) when \(0<\lambda<1\). Its prime-exponent anatomy (Lemma 2.2) and Fourier/geometry argument are **prior external research**. ABC-CLK-03 is only an elementary **inferior baseline**, not a new exponent or priority claim.

| ID | Exact scope | Status | Evidence / falsifier |
| --- | --- | --- | --- |
| ABC-CLK-09 | Independent conditional-p-adic primitive clocks, random product \(H_{\mathrm{loc}}=\prod_p p^{(v_p(a_pb_pc_p)-1)_+}\): a.s. finite, \(\mathbb EH_{\mathrm{loc}}^s<\infty\) for \(0\le s<1\), infinite for \(s\ge1\) | **PROVED LOCAL** in specified profinite probability model | Closed local geometric moments, convergence of prime factors, Borel–Cantelli, monotone convergence; NOT an integer-box claim |
| ABC-CLK-10 | A genuine odd-prime L-AP yields exactly floor((L-1)^2/4) distinct prime-3AP square-completion triples with \(c/\operatorname{rad}(abc)<1/3\) | **PROVED LOCAL**, infinite AP length **EXTERNAL THEOREM** | Exact combinatorial center-distance count; hostile composite AP; prime_ap_shadow_fan |
| ABC-CLK-11 | Canonical source-indexed prime-exponent layers reconstruct \((a,b,c)\) and the radical exactly | **PROVED LOCAL** (classical factorization) / **TESTED MODEL** | ABCTriple.exponent_layers, tests; bounded-truncation and harmonic estimates still missing |
| ABC-CLK-12 | Current elementary exception-set count improves or matches the best 2026 published theorem | **REFUTED** | Primary theorem \(X^{3/5+\delta}\) in 2026 paper dwarfs ABC-CLK-03 exponent; scholarly priority unverified |

**Updated validation:** 14 tests on isolated new Python source passed locally (Python 3.13); full upstream SUCC suite and any future hosted CI not locally certified.


| ABC-CLK-13 | Any three finite nonempty positive-integer multisets and modulus m: exact group-algebra coefficient equals the discrete Fourier projector and the count of x+y=z mod m; if m exceeds max(max A+max B, max C), no alias occurs | **PROVED LOCAL** (classical Fourier orthogonality) and **TESTED MODEL** | modular_additive_count, independent brute force, exact hostile alias (1,1,5,m=3); no infinite Fourier cancellation or RH claim |

**Updated isolated local test count: 16/16** on Python 3.13; full existing SUCC test suite / hosted workflow still UNVERIFIED.
