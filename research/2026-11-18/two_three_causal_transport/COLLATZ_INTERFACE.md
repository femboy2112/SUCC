# BBP and Collatz: local transport and sharp causal memory

**Status:** PROVED elementary local identities and calibrated finite checks;
positive-integer Collatz termination, RH, and pi normality remain OPEN.

**Provenance:** The affine Syracuse composition and valuation cylinders are
classical, explicitly present in Tao (2022). This note gives a source-typed
comparison with BBP and proves the sharp finite-precision causal-memory
consequences. It makes no claim of academic priority. The original BBP four
poles and literal zero seed are unchanged.

**Boundary:** The register on `Q_3` is driven by valuation symbols produced by
the actual positive-integer source. No intrinsic `v_2` operation on `Q_3`, no
random-law replacement of a selected orbit, and no backward physical time are
assumed.

## 1. Inherited SUCC frontier

`research/2026-10-31/two_three_joint_carrier/README.md`, `PROOF.md`, `CLAIMS.md`,
and `NEXT.md` already establish and distinguish:

* Exact joint time Haar for `(U_n mod 2^a, 16^n mod 3^b)` on every complete
  period of length `2^a 3^(b-1)`.
* The 3-adic clock `16^n` is NOT the generally nonintegral 3-adic BBP state
  `U_n`.
* No continuous equivariant decoder from the pure profinite time odometer
  `Z_2 x Z_3` can select an irrational orbit of the expanding real map `x ->16x`.
* A source-selected real tripling/carry interface and its exact tail bound.
* The conditional Rudolph rigidity route, requiring positive entropy in EVERY
  joint ergodic component; positive average entropy is insufficient.
* The missing signed mixed real/local Fourier phase estimate.

These are inherited results; this dossier adds a comparison with the chronological Syracuse valuation register.

## 2. Exact local slope comparison

**Status: PROVED, elementary affine algebra / rational product formula.**

For two BBP trajectories driven by the identical forcing `r(n)` at identical
times, with rational seed difference `delta != 0`,

`Delta_k = 16^k delta`.

The ratios of final to initial absolute values are

| Place | BBP magnification |
|---|---:|
| real | `16^k` |
| 2-adic | `16^(-k)` |
| 3-adic | `1` |

Every other finite-prime magnification is also 1. Their product is 1.
This is fibrewise sensitivity to the seed with fixed source time. It does not
contradict the inherited isometry of the different map `n -> F_2(n)`.

For positive odd Syracuse dynamics use the precise convention

`N_j = (3 N_(j-1)+1)/2^(a_j)`, `a_j = v_2(3 N_(j-1)+1) >= 1`.

Let `A_k=sum_(j=1)^k a_j`. On a common finite valuation itinerary, the affine
slope is `3^k/2^(A_k)`. For two rational starting values driven by this same
word, their difference is multiplied by this slope. The magnifications are

| Place | Same-itinerary Syracuse magnification |
|---|---:|
| real | `3^k / 2^(A_k)` |
| 2-adic | `2^(A_k)` |
| 3-adic | `3^(-k)` |

The product is again 1. A branch derivative is not a globally differentiable
map: changing the integer starting point may change the itinerary. The common
word is essential.

**Consequence.** Collatz has a genuine 2-to-3 local resolution transfer in its
linear branch dynamics. BBP's homogeneous multiplier is 3-adically isometric;
its new 3-adic information must enter through its rational forcing and source
clock. Importing a Collatz contraction argument into BBP without this distinction
would be invalid.

The product formula determines a real magnitude for one rational diagonal
quantity. It does not determine its real sign or additive circle phase, and it
does not turn a local norm estimate into signed Weyl cancellation.

## 3. Exact positive-integer cylinder theorem

**Status: PROVED, classical; compare Tao (2022), equations (1.3), (1.5), and the
proof of Proposition 1.9 in section 4.**

Fix any finite word `a=(a_1,...,a_k)` with all `a_j>=1`. Write

`A_j = a_1+...+a_j`, `A_0=0`,

`B_k = sum_(j=1)^k 3^(k-j) 2^(A_(j-1))`.

Its affine composition is

`Aff_a(x) = (3^k x+B_k)/2^(A_k)`

`= 3^k 2^(-A_k) x + F_k(a)`,

where

`F_k(a) = sum_(j=1)^k 3^(k-j) 2^(-(a_j+...+a_k))`.

The positive odd starting integers whose first k actual valuations equal a are
exactly the positive integers in the single odd residue class

`N_0 = 3^(-k) (2^(A_k)-B_k) mod 2^(A_k+1)`.

Here `3^(-k)` means its modular inverse. Consequently every finite positive
valuation word has positive odd integer realizers.

### Proof of sufficiency, including intermediate legality

Necessity follows from the affine formula and oddness of the terminal integer.
Conversely, the congruence makes `X_k=Aff_a(N_0)` a positive odd integer.
For a prefix of length j, define `B_j` by the same rule and let `B_tail` be the
integer numerator belonging to `(a_(j+1),...,a_k)`. Then

`B_k = 3^(k-j) B_j + 2^(A_j) B_tail`.

The terminal identity gives

`3^(k-j)(3^j N_0+B_j)
 = 2^(A_j)(2^(A_k-A_j) X_k-B_tail)`.

Because `3^(k-j)` is odd, the numerator `3^j N_0+B_j` is divisible by
`2^(A_j)`, so every `X_j=Aff_(a_1,...,a_j)(N_0)` is an integer. If j<k,
`B_tail` is odd (its first term is odd and every subsequent term is even), and
`A_k-A_j>=1`; hence the right-hand bracket is odd. Thus every X_j is odd.
Each affine step preserves positivity. Finally

`3 X_(j-1)+1 = 2^(a_j) X_j`

with odd positive X_j proves that the exact valuation is a_j, not merely a
lower bound. Uniqueness of the residue class follows because 3 is a unit mod
`2^(A_k+1)`; its oddness follows by reducing the displayed congruence mod2.

The same cylinders have normalized Haar measure `2^(-A_k)` in odd `Z_2`.
Thus an explicitly Haar-random odd 2-adic initial state has independent
geometric valuation symbols with `P(a_j=a)=2^(-a)`, at every finite horizon.
This ensemble statement must not be substituted for the itinerary of one
selected positive integer. On `Z_2`, exceptional inputs whose iterate is
`-1/3` require stopping the valuation construction because `3x+1=0` there.
No such exception occurs on the positive odd integer domain used above.

## 4. Sharp forward causal memory theorem

**Status: PROVED, exact local consequence of the classical affine formula.**

For an actual positive odd Syracuse orbit, for every `k>=m>=1`,

`N_k = sum_(i=0)^(m-1) 3^i
         2^(-(a_(k-i)+...+a_k)) mod 3^m`.

Proof: apply the affine composition formula to the last m steps. Its initial
state contribution is `3^m 2^(-sum last m a) N_(k-m)`, which vanishes mod
`3^m`. All denominators are powers of 2 and are invertible modulo `3^m`.

The last m ORDERED valuation symbols therefore suffice. The result is a forward
update law, not a reversal of physical time. Writing newest symbols first is a
coordinate convention, and reordering a deterministic word is generally wrong.

### Temporal depth is sharp

For each m>=1, consider words

`a=(1,1,...,1)`, `a'=(2,1,...,1)`

of length m. Their last m-1 symbols coincide. Yet

`F_m(a')-F_m(a) = -3^(m-1)/2^(m+1)`.

The 3-adic valuation of this difference is exactly m-1, so they produce
different terminal residues mod `3^m`. Each word has a positive odd realizer by
the cylinder theorem. Thus no universal rule using only the most recent m-1
valuation symbols can recover all terminal residues mod `3^m`.

This is sharpness of temporal suffix length, not a claim that storing m
unbounded symbols is the minimal data representation.

### Exact finite register size and input resolution

For fixed m, the driven register is

`Y -> 2^(-a)(3Y+1) mod 3^m`.

After one step its state is a unit. The powers of 2 generate all units modulo
`3^m`, with order `2*3^(m-1)`. Therefore varying positive a can produce every
unit from any fixed preceding Y. A register with `2*3^(m-1)` states, and input
`a mod 2*3^(m-1)`, is sufficient to update the current output exactly. This input
period is sharp since `3Y+1` is a unit. A deterministic machine whose current
state determines this exact output needs at least that many distinguishable
states because all outputs are reachable. The temporal depth and state count
are different specifications.

The order formula follows from LTE: `v_3(4^b-1)=1+v_3(b)` and the order of 2
mod3 is 2. In contrast, the BBP clock16 has order `3^(m-1)` and lives in the
principal-unit subgroup `1+3 Z_3`.

The smallest visible coupling is particularly direct:

`N_k mod3 = 2^(-a_k) mod3 = (-1)^(a_k)`.

The newest ternary unit digit records the parity of the latest 2-adic division
count.

The 3-adic register is a DRIVEN system. Its a_j must come from the source's
integer valuation record. There is no intrinsic operation `v_2` on `Q_3` that
magically regenerates the same a_j.

### Order control with actual positive integer orbits

`(a_1,a_2)=(1,2)`: `11 ->17 ->13`, and `13 mod9=4`.

`(a_1,a_2)=(2,1)`: `9 ->7 ->11`, and `11 mod9=2`.

Both words have length2, total valuation3, the same multiset of symbols, and
linear slope9/8. Their offsets are respectively5/8 and7/8. Keeping only the
product or total 2-adic expansion discards a load-bearing chronology.

### Finite cylinders do not prove a positive infinite realization

The all-ones word of every finite length m is realized by the positive odd
integer `2^(m+1)-1`. Its infinite compatible 2-adic limit is -1, the negative
fixed point of `(3x+1)/2`. Finite positive realizability at every horizon does
not by itself produce one positive integer realizing the infinite word.

## 5. Random 2-adic input does not create 3-adic Haar

**Status: PROVED exact finite law, classical Syracuse random-variable model.**

If the a_j are independently geometric with `P(a_j=a)=2^(-a)`, the terminal
mod3 state has probabilities `(0,1/3,2/3)` at residues `(0,1,2)`. This follows
because the probability of an even a is1/3 and of an odd a is2/3.

At modulus9, the length-two terminal law is exactly

`(0,8/63,16/63,0,11/63,4/63,0,2/63,22/63)`.

This agrees with Tao's published explicit recursion and was independently
reconstructed by exact enumeration of exponent residues mod6, with weights
`P(a=r mod6)=2^(6-r)/63` for1<=r<=6.

Tao's analysis proves a quantitative high-frequency stabilisation property for
this nonuniform Syracuse law, then first-passage transport, to obtain almost
bounded orbits for a logarithmic-density-one set. Neither iid input nor a
3-adic contraction proves all-positive-integer termination. The analogy for BBP
is the need for an actual signed transport theorem for the selected source law.

## 6. Executed finite checks

One exact standard-library Fraction implementation, separate from the parent
agent's code, checked:

* 5,460 words of lengths1..6, symbols1..4, against their unique positive odd
  cylinder representative and the actual iterative valuation map.
* 30,948 terminal memory identities, for every1<=m<=k in those words.
* Sharp suffix counterexamples for every1<=m<=30.
* The exact mod9 probability vector above, total mass1.

These are corroborating finite checks of the displayed proofs, not an
independent reasoner or formal verification. No full SUCC gate was run by this
bearing.

Reproduction code:

```python
from fractions import Fraction as F
from itertools import product

def v(n, p):
    c = 0
    while n and n % p == 0:
        n //= p
        c += 1
    return c

def off(a):
    x = F(0)
    for b in a:
        x = (3*x + 1) / 2**b
    return x

def mod(x, q):
    return x.numerator * pow(x.denominator, -1, q) % q

def cylinder(a):
    A, B, s = sum(a), 0, 0
    for j, b in enumerate(a):
        B += 3**(len(a)-1-j) * 2**s
        s += b
    q = 2**(A+1)
    return (pow(3**len(a), -1, q) * (2**A-B)) % q, q

words = checks = 0
for k in range(1, 7):
    for a in product(range(1, 5), repeat=k):
        n, q = cylinder(a)
        assert n % 2 == 1 and n > 0
        x = n
        for b in a:
            assert v(3*x+1, 2) == b
            x = (3*x+1) // 2**b
        for m in range(1, k+1):
            assert x % 3**m == mod(off(a[-m:]), 3**m)
            checks += 1
        words += 1
assert (words, checks) == (5460, 30948)
for m in range(1, 31):
    x, y = off((1,)*m), off((2,)+(1,)*(m-1))
    assert y-x == -F(3**(m-1), 2**(m+1))
    assert mod(x, 3**m) != mod(y, 3**m)
prob = [F(0) for _ in range(9)]
for a, b in product(range(1, 7), repeat=2):
    prob[mod(off((a,b)), 9)] += F(2**(6-a),63)*F(2**(6-b),63)
assert prob == [F(x,63) for x in (0,8,16,0,11,4,0,2,22)]
```

## 7. Primary sources and exact limits

1. D. J. Bernstein and J. C. Lagarias, *The 3x+1 Conjugacy Map* (1996).
   https://websites.umich.edu/~lagarias/doc/bernstein.pdf

   Page2 equations(1.5),(1.6) give parity coding and its inverse; the map is
   defined on all Z2, which includes nonpositive and noninteger states. This
   conjugacy does not establish positive-integer basin coverage.

2. T. Tao, *Almost all orbits of the Collatz map attain almost bounded values*,
   Forum of Mathematics, Pi10(e12),2022.
   https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F
   Equations(1.3),(1.5),(1.24),(1.29), Proposition1.9, Theorem1.3 are relevant.
   The conclusion uses logarithmic density and a diverging bound f(N), not
   bounded descent for every input. The ordered finite formula is classical.

3. T. Tao, author discussion of the above paper, comment15 September2019,
   6:34am.
   https://terrytao.wordpress.com/2019/09/10/almost-all-collatz-orbits-attain-almost-bounded-values/comment-page-1/
   Tao suggests joint 3-adic/Archimedean characters `chi(n)n^(it)` and perhaps
   an adelic organization, as a possible way to retain the coupling needed to
   upgrade density. This is a research suggestion by the author, not an
   established general theorem or a ready-made BBP normality estimate.

4. D. Rudolph, *x2 and x3 invariant measures and entropy* (1990).
   https://www.cambridge.org/core/services/aop-cambridge-core/content/view/64243AD8323B37089540F911F8CC77EB/S0143385700005629a.pdf/2_and_3_invariant_measures_and_entropy.pdf
   Applies to a common invariant Borel probability measure, ergodic for the
   generated semigroup, and positive entropy for at least one of the coprime
   multiplication maps. The existing SUCC dossier already bills every premise.

RH connection: the exact rational product formula and the common adelic
language are genuine architecture, already present in SUCC. They do not supply
the original-source completed Weil-form positivity or any zero-location
theorem. Nor does a positive local covariance equal the signed Weil form. An
RH transfer needs its own identified prime-power/Gamma/pole formula, admissible
test class, and signed inequality. No such new inequality is proved here.
