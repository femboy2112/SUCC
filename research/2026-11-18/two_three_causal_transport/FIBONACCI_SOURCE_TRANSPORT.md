# The recovered Fibonacci frames and exact ternary source transport

**Scope.** This note reconciles the definitions recovered during this
operation from `15_angry_blind_fibonaccis_2x5x3_research.md` with the
independently defined CRT cycle comparisons in
[CYCLIC_SOURCE_FILTERS.md](CYCLIC_SOURCE_FILTERS.md). The recovered
construction uses two-coordinate Fibonacci states in five frames and
three quadratic readouts per frame. Those numbers are state, frame, and
readout counts. The paired residue clocks of CSF section 5 are a different
declared construction. Neither interpretation alone identifies a local
field or a dynamical factor of the selected BBP orbit.

The exact identities below were independently checked from their literal
matrices and polynomials. No claim of global mathematical priority is made.

## 1. Source complementary filter on the Fibonacci state

Keep

```math
A=\begin{pmatrix}1&1\\1&0\end{pmatrix},\qquad
M=A^{-1}=\begin{pmatrix}0&1\\1&-1\end{pmatrix},\qquad
M^2+M=I.
```

The original BBP polynomials and their complementary filter are

```math
Q(t)=4-2t^3-t^4-t^5=(1-t)H(t),
```

```math
H(t)=4+4t+4t^2+2t^3+t^4,\qquad
K(t)=4-4t+2t^3-t^4,\qquad HK=16-t^8.
```

**FST-01 — PROVED.** Reducing these exact polynomials by `1-t-t^2` gives

```math
\boxed{H(M)=8I+M,\qquad K(M)=3M,\qquad Q(M)=7I-6M.}
```

Explicitly,

```math
H(M)=\begin{pmatrix}8&1\\1&7\end{pmatrix},\quad
K(M)=\begin{pmatrix}0&3\\3&-3\end{pmatrix},\quad
Q(M)=\begin{pmatrix}7&-6\\-6&13\end{pmatrix}.
```

Further,

```math
M^8=13I-21M,\qquad
\boxed{16I-M^8=3(I+7M)=H(M)K(M).}
```

**Proof.** Repeated substitution of `t^2=1-t` gives the three linear
remainders; matrix substitution proves the identities. The same recurrence
gives `M^8=13I-21M`. There is no approximation or limit in this reduction.

For every prime `p`, both `M` and `A` are integer unimodular and hence
isometries for the maximum norm on `Q_p^2`. Since

```math
\det H(M)=\det Q(M)=55=5\cdot11,
```

`H(M)` and the **literal signed filter `Q(M)` are ternary isometries**.
The complementary filter is instead an exact uniform ternary contraction:

```math
\|K(M)v\|_3=\frac13\|v\|_3,\qquad
\|(16I-M^8)v\|_3=\frac13\|v\|_3
\quad(v\in\mathbb Q_3^2).
```

The second equality follows because `H(M)` is an isometry. Thus the
ternary contraction is located in a specified source-derived operator;
it is not assigned indiscriminately to the whole Fibonacci or BBP dynamics.

The integer Smith forms are

```math
H(M),Q(M):\ (1,55),\qquad K(M):\ (3,3).
```

For `H(M)` and `Q(M)`, the gcd of entries is one and the determinant is
55; `K(M)=3M` gives its form directly. For H(M) and Q(M), the sharp inverse norms at five
and eleven are respectively five and eleven. At all other primes these
two operators are isometries. The source's special value `55=F_10` therefore carries
genuine five- and eleven-adic precision defects, while `K(M)=3M` supplies
the exact ternary connection.

## 2. Why this is also the pentagonal Gram pair

Let `S=S_5` be cyclic successor on five coefficient channels, let
`V={v in R^5:sum(v)=0}`, and put `B=S+S^-1` on `V`. Let `D` be the
permutation `D e_j=e_(2j mod5)`.

**FST-02 — PROVED.** On the retained augmentation space `V`,

```math
B^2+B=I,\qquad DBD^{-1}=-I-B.
```

For the source Gram operator `G=H(S)^*H(S)`,

```math
\boxed{G|_V=13I+6B=D\,Q(B)\,D^{-1}.}
```

**Proof.** The sum `I+S+...+S^4` vanishes on `V`, giving the quadratic
identity. Index doubling gives `DSD^-1=S^2`, hence
`DBD^-1=S^2+S^-2=-I-B`. The exact cyclic autocorrelation of
`(4,4,4,2,1)` is `(53,46,40,40,46)`, so

```math
G=53I+46(S+S^{-1})+40(S^2+S^{-2}).
```

Restricting to `V` reduces this to `13I+6B`. Since `Q(B)=7I-6B`,
conjugating by `D` gives precisely that operator. QED.

The two eigenvalues of the two-state matrix `Q(M)` are
`10-3sqrt(5)` and `10+3sqrt(5)`, each positive, with product 55. These are
the two pentagonal Gram eigenvalues on `V`, each appearing there twice.
The complete four-dimensional augmentation Gram determinant is therefore
`55^2`; the two-state determinant is 55. The full five-channel constant
Gram eigenvalue is `H(1)^2=225` and is retained separately. The displayed
intertwining is not asserted on that constant channel.

This proves a genuine shared source/Fibonacci operator algebra, beyond a
numerical match of eigenvalues. It remains an identity between declared
observation spaces, with no conjugacy of `M` to the actual sequence `U_n`
assumed or proved.

## 3. A precise candidate for two-state, three-frame, five-readout dynamics

The recovered quadratic construction uses
`nu_2(x,y)=(x^2,xy,y^2)` in each of five frames. Its update is
`nu_2(Av)=Sym^2(A)nu_2(v)`.

A **new, explicitly defined candidate** for the requested `(2,3,5)`
arrangement is three frames with two-state updates `v_j -> A v_j`, and
the quartic readout in each frame

```math
\nu_4(x,y)=(x^4,x^3y,x^2y^2,xy^3,y^4).
```

**FST-03 — PROVED construction, not a prior-construction identification.**
In this monomial convention the five readouts have the closed update

```math
\nu_4(Av)=
\begin{pmatrix}
1&4&6&4&1\\
1&3&3&1&0\\
1&2&1&0&0\\
1&1&0&0&0\\
1&0&0&0&0
\end{pmatrix}\nu_4(v).
```

Its characteristic polynomial is

```math
(\lambda-1)(\lambda^2+3\lambda+1)(\lambda^2-7\lambda+1).
```

**Proof.** Binomial expansion of `(x+y,x)` gives the matrix. If `phi` and
`psi=-1/phi` are the two eigenvalues of `A`, the five quartic eigenvalues
are `phi^4,-phi^2,1,-phi^-2,phi^-4`. Pairing the reciprocal eigenvalues,
using `phi^2+phi^-2=3` and `phi^4+phi^-4=7`, gives the characteristic
polynomial. Direct integer expansion verifies the same expression.

The three-frame construction has fifteen output coordinates, as does
the five-frame quadratic construction. Their input dimensions and
polynomial degrees differ, so this shared count does not establish an
equivalence. In particular `nu_4(v)=nu_4(-v)` on unrestricted real states.
Even when a declared positive-quadrant domain removes that sign ambiguity,
the image satisfies constraints such as `z_0 z_2=z_1^2` and
`z_0 z_4=z_2^2`. The five readouts are not five freely varying state
coordinates. Extra frame transition rules would have to be supplied to
identify this candidate with a specific earlier triangle.

## 4. The selected-source boundary and a falsifying control

FST-01 supplies an actual ternary contraction derived from the original
polynomial evaluated in the Fibonacci algebra. FST-02 proves the precise
pentagonal intertwiner. FST-03 constructs a five-channel readout with
explicit dynamics. None of these identities contains the authenticated
zero-seed real-circle phase as an input.

For an exact negative control, take a nonzero Fibonacci trajectory
`v_n=A^n(1,1)` and attach the circle coordinate `z_n=0` in the product
system. All polynomial, Gram, and symmetric-power identities above still
hold, while every circle character is identically one. If the original
BBP forcing is also required in the real coordinate, the inherited
same-forcing seed `s=-pi/16` supplies the completed locked phase exactly.
That seed violates the original zero-seed condition and is used only to
show that these observer identities alone do not authenticate it.

The next missing theorem is therefore a source-faithful map or signed
inequality coupling these operators to the literal zero-seeded BBP
trajectory, with its ordered boundary state retained. A nontrivial
all-shell anti-lock or Fourier estimate through that map would be a
proof advance. The present identities, including the quartic candidate,
do not by themselves prove R0, pi normality, Collatz, or RH.
