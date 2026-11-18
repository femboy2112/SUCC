# Borwein Swept-Impulse Source Probe — exact tests, independent Fourier checks and boundary controls

**Date:** 2026-11-17. Companion to [BORWEIN_SWEPT_IMPULSE_BBP.md](BORWEIN_SWEPT_IMPULSE_BBP.md). All universality and equivalence claims rely on included analytic arguments. Exact finite tests are **not an all-shell normality proof**.

## 1. Focused source arithmetic executed

The self-contained standard-library script was executed locally:

~~~sh
python -m unittest -v /mnt/data/test_borwein_bbp_sweep.py
~~~

**9 tests passed, 0 errors, 0 failures**, including:
- First nontrivial Borwein plateau leak as a fully exact 7-dimensional simplex probability, including strict support threshold at the denominator 15.
- Exactly rational two-uniform convolution detector \(L(d)=162/289(d-1/18)_+^2\), its Haar mean \(256/7803\) and known phase controls.
- The strict radix-16 cold-run barrier \(1/17\), positive detector response at \(x=1/17\) and a source-independent cold-run energy calibration.
- The original **literal zero-seeded** four-pole rational endpoint \(U_{2B}\) cross-checked by direct source summation.
- Rational one-shell energy for B=4,8,16,32,64,128 and exact source-tail upper bounds.
- Piecewise-quadratic exact rational circle-origin maximization for original-source endpoints, and hostile locked/nonunit fixed/periodic orbits.
- The analytical proof that the two-pulse Fourier transfer has **no blind integer harmonics**; sample numerical coefficient signs were also checked for modes 1 through 200.
- Rational source-energy/phase-energy comparisons and circle-origin invariance.

The file [tests/test_borwein_bbp_sweep.py](../../../tests/test_borwein_bbp_sweep.py) was fetched from the active GitHub branch and its **Git blob SHA matched the exact executed local bytes**:

~~~text
95d8e83512a973b3231b444c7e2f25eb05faf227
~~~

## 2. Independent high-precision density and Fourier audit

A separate mpmath implementation used 45 decimal working digits, integrated the **triangular convolution density itself**, and verified
\[
\Pr(|\theta+X_1+X_2|>1)=\frac{162}{289}\max(|\theta|-1/18,0)^2
\]
for independent test points θ=0, 1/18, 0.06, 0.13, 0.42, 0.5, with residuals at or below approximately \(10^{-47}\).

The h-th Fourier coefficient was independently computed as the actual finite definite integral
\[
2\int_{1/18}^{1/2}\frac{162}{289}(t-1/18)^2\cos(2\pi ht)\,dt
\]
and compared with the source-independent analytical formula
\[
\frac{648}{289}
\left[\frac{(4/9)(-1)^h}{(2\pi h)^2}
+\frac{\sin(\pi h/9)}{(2\pi h)^3}\right]
\]
at h=1,2,3,9,18,21,50. All numerical residuals were at most about \(8\cdot10^{-48}\). The **universal nonvanishing** is a paper inequality, not extrapolated from these seven frequencies.

A separately coded exact rational maximization (all quadratic vertices and phase breakpoints) was checked against **4,096-grid origin evaluations** at B=4,8,16. Its maxima were greater than or equal to every grid value, as required. A finite grid itself cannot certify the supremum, which is why the exact vertex algorithm is retained.

## 3. Authenticated π-orbit validation

With 4B+55 decimal digits of mpmath precision at shell B, the independently computed real π orbit gave these actual differences from the *exact original-source rational endpoint detector*:

| B | measured \(|\mathcal J_B(\pi/16)-\widehat{\mathcal J}_B|\), diagnostic | proved rational \(\epsilon_B=16r(2B+1)/(7225B)\) |
|---:|---:|---:|
| 16 | \(1.45330262016\times10^{-8}\) | \(3.09596020307\times10^{-8}\) |
| 64 | \(1.35880547961\times10^{-11}\) | \(4.92133142068\times10^{-10}\) |
| 128 | \(4.62348154297\times10^{-11}\) | \(6.16945343915\times10^{-11}\) |

The true-π phase results are **floating numerical cross-checks**, not certified intervals. The rational error inequality is proved independently from original BBP's positive tail and the detector's exact Lipschitz constant.

### Finite in-sample source-rational readings

| B | exact source-rational \(\widehat{\mathcal J}_B(0)\), decimal view | exact full-origin sweep deviation \(\mathcal D_B\), decimal view |
|---:|---:|---:|
| 4 | 0.0533852829065 | 0.0242113055283 |
| 8 | 0.0502716494508 | 0.0222601578762 |
| 16 | 0.0292868871480 | 0.0219138312770 |
| 32 | 0.0315644418506 | 0.0057979609367 |
| 64 | 0.0347618039043 | 0.0043242080699 |

The Haar target for the swept response is \(256/7803\approx0.0328078943995899\). This finite decrease is **not a prospectively validated asymptotic rate** and does not prove full normality. A locked orbit fails the sweep criterion, as do nonunit rational fixed points that nevertheless pass the weaker R0 test.

## 4. Source/meaning firewalls

- The independently drawn **uniform variables are an observer test-kernel construction**, not random initial data inserted into the original BBP seed. The underlying actual π orbit remains deterministic and source-selected.
- The original BBP source-lag impulse polynomial \(Q(t)=4-2t^3-t^4-t^5\) and the two-sinc phase-origin filter \(L\) operate in **different bases**. The shared impulse/convolution language is exact separately; a map transporting source-signed Mellin coefficients directly into positive BBP winding density remains **UNVERIFIED**.
- A single rectangle filter has blind integer frequencies divisible by nine; the second rectangle's quadratic leakage has **none**, as proved from its entire Fourier coefficient formula. This is the exact value of the second convolution for our all-mode observable.
- The classical R0-equivalence of the anchored detector uses the **radix-16 no-wrap cold-run bound** for δ'<1/17. Replacing δ=1/18 with δ=1/17 would miss the periodic fixed-distance x=1/17 control and break the equivalence.
- Full base-16 normality is **equivalent** to the rational sup-deviation \(\mathcal D_B\to0\), by the nonzero Fourier transfer and Weyl's criterion; the test does NOT establish the universal limit, any root 14k+ regression gate, Lean certification, or hosted CI completion.

**Verdict-changing next theorem:** prove from the complete literal signed four-pole source and selected integer carry history either \(\liminf_B\widehat{\mathcal J}_B(0)>0\) (R0) or the far stronger \(\mathcal D_B\to0\) (full base-16 normality). A successful proof must still reject the tuned same-forcing locked counterseed, the alternative positive locked source, the finite rational shadow adversary, and the sparse badly approximable cold-shell source. Neither a finite table nor a new equivalent kernel supplies that missing asymptotic arithmetic inequality.

**External references:** [Borwein integrals MathWorld](https://mathworld.wolfram.com/BorweinIntegrals.html), [Ten Problems in Experimental Mathematics](https://mathexp.eu/bostan/ExpMath19/BaileyBorweinKapoorWeisstein2006_-_Ten_Problems_in_Experimental_Mathematics.pdf), [Random-walk Fourier proof](https://dornsife.usc.edu/sergey-lototsky/wp-content/uploads/sites/211/2023/06/BorweinIntegrals-RandomWalk.pdf); original SUCC sources linked in the main theorem.
