# Exact macro-carry correction exclusion, and its selection obstruction

Status: paper proofs with exact finite checks; awaiting independent mathematical
review. No Lean/kernel certification, external novelty claim, signed Weyl decay,
bounded all-depth cell pressure, or normality proof.

## AC-01: a quantitative carry correction bound

Let `r(n)` be any real sequence satisfying `0<=r(n)<=C/n^2` for every `n>=2`,
where `C>0`. Let `U_0=s` be any real seed and
`U_(n+1)=16 U_n+r(n+1)`, retaining this unwrapped recurrence. Write `x_n={U_n}`
and `c_(n+1)=floor(16 x_n+r(n+1))` for the literal carry. For integers `m>=1`
put

```
B = 16^m,
R_m(n) = sum_(j=1)^m 16^(m-j) r(n+j),
K_m(n) = sum_(j=1)^m 16^(m-j) c_(n+j)
       = floor(U_(n+m)) - B floor(U_n),
W_m(n) = floor(B x_n),
b_m(n) = K_m(n) - W_m(n).
```

For an integer epoch `A>=1`, assume `B <= 15(A+1)^2/C`. Define

```
L = floor(log_B(15(A+1)^2/C)) >= 1,
E_(A,m) = #{n in [A,2A): b_m(n)=1}.
```

Then the exact finite bound is

\[
\boxed{b_m(n)\in\{0,1\},\qquad
 E_{A,m}\le m\left\lceil {A\over mL}\right\rceil.}\tag{AC1}
\]

Within each residue class modulo m, any two successive correction times are
separated by at least `mL`. In particular, for every fixed m,

\[
E_{A,m}\le {A\over L}+m
=\left({m\over2\log_{16}A}+O_m((\log A)^{-2})\right)A+O(m).
\tag{AC2}
\]

**Proof.** For `n>=A`, positivity and the assumed source bound give

\[
0\le R_m(n)\le q:={C(B-1)\over15(A+1)^2}<1.
\]

Telescoping the literal carries gives
`x_(n+m)=B x_n+R_m(n)-K_m(n)`, hence
`K_m(n)=floor(B x_n+R_m(n))` and `b_m(n)` is 0 or 1. If it equals 1, then

\[
0\le x_{n+m}<R_m(n)\le q.\tag{AC3}
\]

After this reset, the unwrapped positive upper comparison at the kth following
macro transition is

\[
q(1+B+\cdots+B^k)
={C(B^{k+1}-1)\over15(A+1)^2}.
\]

For `1<=k<=L-1`, this is strictly less than 1, since
`B^(k+1)<=B^L<=15(A+1)^2/C`. Thus the complete macro carry there is zero;
in particular its correction is zero. This proves separation by `mL`.
There are at most `ceil(A/m)` starts in each residue class modulo m, so that
class has at most `ceil(ceil(A/m)/L)=ceil(A/(mL))` corrections. Summing the m
classes proves AC1. The floor in L gives AC2. No seed typicality has entered.

**Authentic source specialization.** The four signed poles simplify exactly to

\[
r_o(n)={120n^2-89n+16\over(2n-1)(4n-1)(8n-7)(8n-3)},
\quad 0<r_o(n)\le{1920\over2457n^2}\quad(n\ge2).
\]

This is the already-proved #518 source bound; AC1 applies with
`C=1920/2457` to the exact original zero history and to *every other seed*.
The exceptional first injection `r_o(1)=47/15` is never used in the epoch
estimate, because every source index in `R_m(n)` is at least `A+1>=2`.

The result is a new auxiliary inequality in this dossier, **not class A** under
the task's source-selection definition: its proof does not use `s=0` and its
countermodel discrimination is deliberately negative. It is not a finite
trend extrapolation. No claim of literature novelty is made.

## AC-02: exact pressure transport and the unpaid count

Let `V_m(n)=K_m(n) mod B`. Since `K_m(n)=W_m(n)+b_m(n)`, the two alphabet
labels `V_m(n),W_m(n)` disagree exactly when `b_m(n)=1`, including the case
`K_m(n)=B`, which wraps to zero. Let p and q be their empirical distributions
on `[A,2A)`. Every count changes by at most E, so
`max_w |p_w-q_w|<=E/A`. Therefore

\[
\boxed{\left|B\sum_w p_w^2-B\sum_w q_w^2\right|
 \le B\max_w|p_w-q_w|\sum_w(p_w+q_w)
 \le {2BE\over A}.}\tag{AC4}
\]

Consequently the original hexadecimal cell pressure and the accumulated
literal-carry pressure have the same limsup at every fixed m. This is a
**class B transport**, not a class C reduction: the missing depth-uniform
carry-square-sum bound is equivalent to the old cell-square-sum bound through
AC4. Nothing here estimates that square sum.

The fixed-depth proviso matters. When m grows comparably to log A, L need not
grow, and both AC1 and the factor `B=16^m` in AC4 can lose all useful force.
A finite-sample bound must retain these constants rather than hiding them
inside a claimed depth-uniform O term.

## AC-03: sharp logical obstruction to carry-correction mixing

For the genuine source tail
`T_n=sum_(j>=1)16^-j r_o(n+j)>0`, the completed solutions are
`U_n=16^n beta-T_n`, with initial seed `s=beta-alpha` and `alpha=pi/16`.
The source identity is `R_m(n)=B T_n-T_(n+m)`.

For the coherent completion `beta=0`, eventually `B T_n<1`. Then

```
x_n=1-T_n,
W_m(n)=B-1,
K_m(n)=floor(B-T_(n+m))=B-1,
b_m(n)=0.
```

Its cell pressure is exactly B for all sufficiently large A, at every fixed m.
Thus even the stronger hypothesis **eventually no corrections at all** does
not force Haar or a depth-uniform pressure bound.

The same obstruction holds for every fixed rational periodic completion
`beta=k/(16^p-1)`. If beta is nonintegral, the finitely many completed phases
`{16^n beta}` avoid every B-adic cell boundary: an intersection with a boundary
would have reduced denominator dividing both the odd number `16^p-1` and B,
hence be the zero phase, impossible for a nonintegral beta because 16 is
invertible modulo its reduced denominator. Their finite boundary clearance is
strictly positive. For large n, subtracting `T_n` and applying the exact source
recurrence crosses no B-adic boundary. Thus `b_m(n)=0` eventually. The orbit
has at most p limiting phase values, so for all sufficiently large A its
histogram occupies at most p cells and

\[
\mathcal P_{A,m}\ge B/p.
\]

For integral beta use the coherent argument. Choosing beta nearest to alpha
with denominator `16^p-1` gives the #518 completions arbitrarily close to zero
seed. They satisfy every hypothesis of AC1 and eventually have E=0, while
failing the proposed all-depth pressure gate.

**Class D / refutation receipt.** Any claimed implication from AC1, AC2, or
eventual E=0 to bounded all-depth pressure is false. The precise missing
arithmetic input is the distribution of the selected accumulated carries
`K_m(n) mod 16^m`, not the number of source-induced correction events.
Literal zero authenticates one history, but no inequality here uses that
hypothesis to exclude these coherent or periodic histories.

## A next discriminating inequality, rather than a renamed result

For original zero source let `N^K_(A,m)(w)` count `K_m(n) mod B=w`. The proposed
proof attempt was to bound these counts by controlling correction events.
AC-03 kills that attempt: correction estimates alone cannot bound
`sum_w (N^K_(A,m)(w))^2`. A genuinely new input must pay a centered-numerator
or chronological carry imbalance **inside the E=0 population**. The next
probe should therefore split the exact same-cell pair count by whether either
endpoint is a correction time and ask for a bound on the remaining pair
population. A bound on the removed O(AE) pairs cannot suffice. Any proposed
remaining-population estimate must fail for the coherent and period-p seeds,
which have E=0 yet at least A^2/p same-cell pairs asymptotically.
