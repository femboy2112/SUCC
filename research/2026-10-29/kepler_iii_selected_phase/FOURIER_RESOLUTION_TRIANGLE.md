# Kepler III addendum: a sharp Fourier-resolution / source-information / Oily-grade triangle

**Research only; continuation of the exact original four-pole shrinking target.** This is an observation-resolution theorem, **not** a signed cancellation estimate or physical information law.

At original source time `n>=3`, let `I_n=[T_n,T_n+r_n)` be the exact selected carry-correction window, `r_n~15/(64n²)`. Choose two explicit phases a distance `r_n/2` apart,

`x_in=T_n+3r_n/4` and `x_out=T_n+5r_n/4`.

The first lies strictly inside `I_n` and the second strictly outside, on the right; both lie in `(0,1)` for the original n>=3 source. Let `P(x)=sum_{|k|<=H} c_k exp(2pi i k x)` be a **real-valued** trigonometric polynomial with sup norm `<=1` and robust contrast `P(x_in)>=3/4`, `P(x_out)<=1/4`.

## Exact frequency lower bound

The mean value theorem yields `||P'||_infty >= (1/2)/(r_n/2)=1/r_n`. The classical Bernstein inequality for trigonometric polynomials gives `||P'||_infty <= 2pi H ||P||_infty <=2pi H`. Hence

`H >= 1/(2pi r_n) > n²/pi`,

since the original four-pole forcing obeys `r_n<1/(2n²)` for all n>=3. Thus a **bounded-frequency** trigonometric observer cannot robustly distinguish even those two source-correction configurations at all sufficiently large times. This is a *necessary resolution* for a specified two-point test, not a theorem about arbitrary digit statistics.

## A matching constructive frequency upper scale

For `M=ceil(4/r_n)`, the nonnegative, norm-one Fejer pulse centered at `x_in`,

`P_M(x)=|M^(-1) sum_(k=0)^(M-1) exp(2pi i k(x-x_in))|²`,

is a real trigonometric polynomial of degree `M-1` satisfying `0<=P_M<=1`, `P_M(x_in)=1`, and

`P_M(x_out)=|sin(pi M r_n/2)/(M sin(pi r_n/2))|² <= 1/(M² r_n²) <=1/16`,

where `sin(pi r_n/2)>=r_n` for `r_n<=1`. Therefore the minimum bandwidth for **this two-point robust discrimination problem** is `Theta(1/r_n)=Theta(n²)`. This Fejer pulse does **not** claim accurate classification of *every* point of the interval with no transition zone.

## The resulting three-way information scale

Let `L_n=floor(log_16 n²)` be the previously proved number of forced zero digits. For the source event's Haar-reference information surprise `I_n=-log r_n`, the three quantitative scales agree up to bounded constants:

- Event surprise: `I_n = 2log n + log(64/15)+O(1/n)` nats.
- Forced base-16 branch choices: `L_n log16 = 2log n+O(1)` nats.
- Minimum robust two-point Fourier resolution: `log H_min = 2log n+O(1)` nats of logarithmic bandwidth; this is an instrument-resource scale, NOT a Shannon entropy of the selected deterministic path.

The precise harmonic finite part is inherited from the original four-pole source:

`lim_(n->infinity) (-log r_n -2 H_n)=log(64/15)-2 EulerGamma`.

The separately marked Oily golden fixed point `lambda=phi^-1` is not selected by this information equality; its appearance requires retaining the original two-channel packet grammar. Hence the triangle has a source-derived *Harmonic/Gamma* side and a separately marked golden comparison side, without making the golden constant a physical entropy-production coefficient.

## The moving-grade Oily restriction

A temporal lag of grade `j` in a BBP character has base-16 frequency `16^j` relative to the current pure circle phase (up to the original forcing correction). Thus to reach `H~n²` one needs `j=log_16(n²)+O(1)`, **not fixed j**. The original Oily two-channel endpoint weight of that grade is

`w_j=(j+1)/2^(j+2)`.

At exactly `j=L_n`, the inequalities `16^L_n<=n²<16^(L_n+1)` imply

`(L_n+1)/(4sqrt(n)) <= w_(L_n) < (L_n+1)/(2sqrt(n))`.

So the source's relevant moving high-grade mass decays like `(log n)/sqrt(n)`. Retaining only a **fixed** Oily/Pascal grade truncation cannot resolve the authentic carry-reset window indefinitely, even if its positive source normalization and golden fixed point are exact. A *moving-grade* q6-primitive/cototient observer is a valid next experimental object; it must still prove an independent signed correlation bound before any pi-normality claim.

**Hard firewall:** Neither the Bernstein lower bound, the Fejer upper construction, the moving-grade weight, nor the information-scale matching gives a noncircular Weyl estimate. The coherent original-forcing seed, saturated adversarial seed, finite Fourier alias and de Bruijn countermodels all survive.
