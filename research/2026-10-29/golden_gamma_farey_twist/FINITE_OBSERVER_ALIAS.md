# Finite probe-gap versus true global normality: exact hostile controls

**Additive continuation of the Farey/Gamma/Eisenstein research round.** Exact statements below are classical finite combinatorics and Fourier analysis. They protect the main positive results in [`README.md`](README.md) from a false finite-to-infinite inference. These are deliberate **nonnormal sources**, not claims about π.

## A. Every fixed depth of hexadecimal tests has a periodic impostor

Fix any integer depth K≥1. A de Bruijn cycle B(16,K) is a cyclic word of length 16^K containing every K-symbol hexadecimal word *exactly once* as a cyclic block. It exists by the Euler circuit of the balanced directed de Bruijn graph on words of length K−1. The classical FKM generator implemented in [`finite_alias_probe.py`](finite_alias_probe.py) constructs one explicitly, with exact finite count checks.

For every j≤K, the cycle contains each length-j word exactly 16^(K−j) times. Repeat this cycle forever to obtain the base-16 expansion of the rational number

```
x_K = integer_value(B(16,K)) / (16^(16^K)-1).
```

This rational source is **not normal in base 16** because it has a finite period: among the 16^(K+1) possible (K+1)-blocks, at most 16^K can occur. Yet its limiting empirical distribution of every block of length ≤K is **exactly uniform**. This gives a decisive, all-K quantifier correction:

```
forall K exists a nonnormal rational x_K passing every block test of depth <=K,
but it does NOT follow that exists a single nonnormal x passing all K tests.
```

This control is not an original-four-pole BBP source and must not be used as one. Its role is to disprove inference from any *bounded* block-depth family of perfectly uniform observations to global normality.

## B. Even the full translated Eisenstein energy is arbitrarily small on nonuniform sources

The main dossier proves for y>0 and any probability measure ν on the circle the spectral identity

```
E_y(ν) = sum_(h!=0) a_|h|(y)^2 |νhat(h)|^2,
a_h(y)>0,  a_h(y)~const_y*h*exp(-2pi*h*y).
```

Let `ν_q=(1/q)SUM_{j=0}^{q-1}δ_(j/q)` be the measure uniformly supported on the q equally spaced circle points. Its Fourier transform is exactly

```
νhat_q(h)=1 if q divides h, else 0.
```

Thus ν_q is nonuniform for **every** finite q, but

```
0 < E_y(ν_q) = 2*SUM_{m>=1} a_(mq)(y)^2
                  <= 2*SUM_{h>=q}a_h(y)^2.
```

With `C=pi*zeta(3)/(2*zeta(4)*y)`, `B=2pi*y` and `r=exp(-4pi*y)`, the explicit finite frequency-tail theorem of README gives

```
E_y(ν_q) <= 4*C²*r^q*[
 (1+B*q)^2/(1-r)+B²*r*(1+r)/(1-r)^3
].
```

At fixed y, this is `O_y(q² exp(-4pi*y*q))`. So the Eisenstein energy is **strictly separating at infinite exact precision** (zero iff Haar) but is exponentially ill-conditioned for finite-precision observations. If q exceeds the largest tested Fourier mode H, **all those H coefficients are exactly zero**, while the qth coefficient is 1. The package's numerical oracle records q=2,4,8,16 and confirms the analytic upper bound at high precision.

This is a concrete SUCC **probe-availability / instrument-cost** distinction, *not* proof of a FuckedField under the complete translated observer, and not a claim that nonnormal π is likely. The full family separates. A fixed bounded instrument can be unable to distinguish the alternatives.

## C. True-source acceptance gate remains unchanged

For the actual original zero-seeded four-pole U_n, the limit `ENERGY_N(y)->0` is equivalent to base-16 normality. No finite decreasing energy values, even supported by perfect K-block frequencies for arbitrarily large but **individually chosen** K, settle that fixed-source infinite limit. The coherent same-forcing counterseed remains an essential hostile control, not interchangeable with the periodic de Bruijn family.

**Verdicts:** de Bruijn finite-depth alias — PROVED/CLASSICAL; q-point Fourier alias and explicit exponential Eisenstein cost — PROVED PAPER; an arbitrary finite probe suffices for π-normality — REFUTED by controls; selected zero-seed asymptotic energy decay — OPEN.
