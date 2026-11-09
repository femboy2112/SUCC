# TDH-09 — The signed Pascal hierarchy of SUCC-wavelet differences

Additive continuation of [the main two-road Haar junction](PROOFS.md), on the same non-main research branch. Original source poles/seed unchanged; pi normality, original-zero signed parity and RH OPEN.

## Exact theorem: iterate the signed successor

For each parent word w, write the 16 child masses as a vector v_a=p_(j+1)(w,a)-p_j(w)/16. This vector has zero sum. Let S_16 cyclically advance the child-digit label and D=I-S_16. For every integer m>=1, the binomial theorem gives the **exact signed Pascal expansion**

~~~text
D^m = (I-S_16)^m
    = sum_(k=0)^m (-1)^k binomial(m,k) S_16^k.    (P1)
~~~

This is the literal statement that positive/negative unit-SUCC contributions produce higher signed Pascal triangles. It is a convolution on the **child-digit circle**, not a chronological n-shift on the BBP orbit.

Define the m-th contrast energy

~~~text
J_j^(m) = 16^(j+1) sum_(|w|=j) sum_(a=0)^15
              [sum_(k=0)^m (-1)^k C(m,k) p_(j+1)(w,a-k)]^2.
~~~

The centered parent term disappears because D^m kills constants. On the finite Fourier mode h=1,...,15 the squared multiplier is |1-exp(-2pi*i*h/16)|^(2m). Thus for EVERY finite word law, not just pi,

~~~text
[2-sqrt(2+sqrt(2))]^m * (E_(j+1)-E_j)
  <= J_j^(m) <= 4^m * (E_(j+1)-E_j).              (P2)
~~~

Sharpness: at h=1 or 15 one has the lower spectral endpoint; at h=8 the upper. Small real Fourier perturbations of a uniform positive parent law attain the endpoints. The tests use the rigorous weaker rational constant (3/20)^m.

### Exact hostile controls

- Single occupied child and m<=15: the signed outputs are the alternating binomial row, hence J_0^(m)=16*C(2m,m); checked with exact Fractions for m=1,...,5.
- Alternating h=8 positive digit law: J_0^(m)=4^m E_1 exactly; checked for m=1,...,4.
- Original certified BBP digits at A=16: m=1 reproduces TDH-04's first signed successor energy at j=0,1,2; m=3 obeys the rigorous lower bound.
- A plain *time-index* difference still telescopes and remains useless for normality.

## Crucial no-go: repeated differences are NOT automatic Haar contraction

Let c=2-sqrt(2+sqrt(2)), with 0<c<1. For a nonzero low-frequency h=1 child contrast, its raw m-fold difference energy is exactly c^m times its original Haar-detail energy, so it tends to zero as m grows **even though the non-Haar contrast has not changed at all**. An uncalibrated test that interprets small J^(m) at m→infinity as Haar has a direct counterexample.

Meanwhile h=8 is amplified like 4^m. Thus the Pascal hierarchy is a **frequency-selective diagnostic**, with an exponential conditioning cost; it does not independently improve the original zero-seed signed Weyl gate. Any actual source argument must declare an order m, compensate the frequency response, and show original-zero (not seed-averaged) signed decay on the de Bruijn/real carrier.

## Reproduction

Additive modules: observational_succ/haar_pascal_successor.py, tests/test_haar_pascal_successor.py. Isolated local Python 3.13 tests: 3 new cases PASS; together with the 15 base Haar-junction cases this is **18/18 PASS**. The main and test-only local duck_bbp fixture scope remains exactly as disclosed in VALIDATION.md; hosted exact-head CI and full native suite are separately tracked. The new files are independently blob-verified against locally tested bytes; no formal Lean result or scholarly priority is asserted.

**Verdict:** P1/P2 PROVED LOCAL; local exact receipts OBSERVED FINITE; stronger claim "higher SUCC differences converge to Haar by themselves" REFUTED by the h=1 spectral countermodel; original-zero pi cancellation OPEN.
