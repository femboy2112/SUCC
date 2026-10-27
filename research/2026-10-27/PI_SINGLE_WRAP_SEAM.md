# Single-wrap seam theorem and discontinuous-observer saturation

Status: **PROVED** paper mathematics; finite validation is recorded separately. This is a new application of elementary radix expansion and the
authentic BBP tail inequalities, not an external-priority claim. It does not
prove normality of pi. The entire source remains

$$
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),\qquad
T_n=\sum_{j\ge1}16^{-j}r(n+j).
$$

The inherited bounds are $0<T_n<1/[15(n+1)^2]<1/16$, for $n\ge1$,
and $\sum_{n\ge1}T_n=B$. Define, for any fixed real carrier $\alpha$,

$$
y_n=\{16^{n-1}\alpha\},\qquad x_n=\{16^{n-1}\alpha-T_n\},
\qquad I_{n,a}=1_{[a/16,a/16+T_n)}(y_n),\quad 0\le a\le15.
$$

All windows lie inside $[0,1)$, are pairwise disjoint, and use the
half-open convention shown. The authentic selected orbit is $\alpha=\pi$.
For a different carrier the unwrapped states have the same forcing and
initial value $(\alpha-\pi)/16$.

The upper bound, exact Green identity, and summability are imported from
`research/2026-10-27/BBP_ECHO_DELAY_TRANSPORT.md`, sections 1--2, at parent
commit `fca58d3e0289e57596dd8ca74bace325a450df31`. The interior-cut theorem
applies to the authentic source, but its proof uses only those tail bounds
and radix expansion, not any additional four-pole arithmetic rigidity. The
explicit lower bound (SC-6) is derived directly from all four canceled poles.
No academic priority is claimed for the general packing method or its
application here.

## 1. Nonzero-cut packing, uniformly over every carrier

Put $C_N^+=\sum_{n=1}^N\sum_{a=1}^{15}I_{n,a}$. For an integer
$0\le Q<N$, define

$$
L(Q)=\max\{\ell\ge0:16^{\ell+1}\le15(Q+2)^2\},\qquad
P(N,Q)=Q+\left\lceil\frac{N-Q}{L(Q)+1}\right\rceil.
$$

The set defining $L(Q)$ is nonempty even at $Q=0$. Then

$$
\boxed{C_N^+\le\min\left(N,\min_{0\le Q<N}P(N,Q)\right).}
\tag{SC-1}
$$

**Proof.** Suppose a nonzero-cut event occurs at $n>Q$, so
$y_n=a/16+\delta$, $1\le a\le15$, $0\le\delta<T_n$.
For every $1\le j\le L(Q)$,

$$
16^j\delta<\frac{16^j}{15(n+1)^2}
\le\frac{16^j}{15(Q+2)^2}\le\frac1{16}.
$$

Consequently $y_{n+j}=16^j\delta<1/16$, with no omitted modular
wrap, so none of those times is a nonzero-cut event. Distinct event times
after $Q$ are separated by at least $L(Q)+1$. Packing an interval
of $N-Q$ integer times gives the displayed ceiling; the first $Q$
times cost at most $Q$. This includes exact boundary hits $\delta=0$.

For example take $Q=\lfloor\sqrt N\rfloor$ when $N\ge2$. Since
$L(Q)+1=\lfloor\log_{16}(15(Q+2)^2)\rfloor$, this is an explicit
all-N bound of order

$$
\boxed{C_N^+=O(N/\log(N+1))}
$$

with a constant independent of $\alpha$. It applies in particular to
the actual pi orbit. The theorem pays for arithmetic expansion after a
visit; it does not infer visit counts from Lebesgue window lengths.

## 2. Exact single-wrap decomposition for arbitrary digit observers

Let $D(x)=\lfloor16x\rfloor$ for $0\le x<1$, and let
$f:\{0,\ldots,15\}\to\mathbb C$ be arbitrary. Define

$$
J_0=f(15)-f(0),\qquad J_a=f(a-1)-f(a)\quad(1\le a\le15),
\qquad J_+=\max_{1\le a\le15}|J_a|.
$$

Because $T_n<1/16$, at most one digit boundary is crossed, and

$$
\boxed{f(D(x_n))-f(D(y_n))=J_0I_{n,0}+\sum_{a=1}^{15}J_aI_{n,a}.}
\tag{SC-2}
$$

Thus for any complex weights $|w_n|\le1$, even chosen using the
time labels and observation history,

$$
\boxed{\left|\sum_{n\le N}w_n\bigl[f(D(x_n))-f(D(y_n))\bigr]
-J_0\sum_{n\le N}w_n I_{n,0}\right|\le J_+ C_N^+.}
\tag{SC-3}
$$

The discontinuous observer class $f(15)=f(0)$ therefore transports
with an $O_f(N/\log N)=o(N)$ total error, uniformly over all carriers.
This is a genuine extension of the inherited coordinate-Lipschitz
transport to discontinuous nonlinear digit statistics. Their cancellation
problem still belongs to the same completed radix orbit. The exception
has been isolated exactly: only the jump from digit 15 to digit 0 can
retain a positive-density error.

In particular the total mismatch count satisfies the exact estimate

$$
\boxed{C_N=C_N^0+O(N/\log N),\qquad C_N^0=\sum_{n\le N}I_{n,0},}
\tag{SC-4}
$$

where the error is nonnegative and bounded by (SC-1). Thus the fifteen
nonzero hexadecimal cuts are already controlled for the selected pi
orbit. The unresolved boundary problem is the single moving window
$\{16^{n-1}\pi\}<T_n$ at zero.

### Moving nonlinear lag tuples

For arbitrary nonnegative integer lags $\ell_1,\ldots,\ell_m$,
let $F:\{0,\ldots,15\}^m\to\mathbb C$ be unchanged whenever
one coordinate is switched between 15 and 0, with all others fixed.
Suppose changing coordinate $j$ between adjacent internal digits
changes $F$ by at most $A_j$, uniformly in the other coordinates.
Coordinate telescoping and (SC-1) give

$$
\left|\sum_{n\le N}w_n\bigl[F(D(x_{n+\ell_1}),\ldots)
-F(D(y_{n+\ell_1}),\ldots)\bigr]\right|
\le P_*(N)\sum_j A_j,
\tag{SC-5}
$$

where $P_*(N)=\min(N,\min_Q P(N,Q))$. The bound is independent
of lag sizes: within the shifted time interval, the tail bound is still
at most $1/[15(n+1)^2]$, so the identical packing proof applies.
It also permits $F$, the lags, and the weights to depend on $N$,
provided the stated coordinate properties hold and all budgets are paid.
For $\sum_j A_j=o(\log N)$, the normalized discrepancy vanishes.
The target law, when the carrier is normal, remains the deterministic
radix lag graph. This theorem asserts no independent-product Haar law.

## 3. Near-maximal zero-seam occupation with finite Diophantine type

The sparse number

$$
\xi=\sum_{j\ge0}16^{-2^j}
$$

already appears in the inherited `SELECTED_BRANCH_ANALYTIC.md`, which
imports the classical theorem $\mu(\xi)=2$ and proves its sparse
Fourier obstruction. Those results and the construction are not new here.
The new conclusion is its near-maximal occupation of the **authentic
moving Green-tail seam**, rather than a fixed-radius or tail-bin event.

For every $n\ge1$, cancellation of the four poles gives

$$
r(n)=\frac{120n^2-89n+16}{(2n-1)(4n-1)(8n-7)(8n-3)}
>\frac{47}{512n^2},\qquad
T_n>\frac{47}{8192(n+1)^2}.
\tag{SC-6}
$$

Indeed the numerator minus $47n^2$ is
$(n-1)(73n-16)\ge0$, while the positive denominator is strictly
less than $512n^4$. Retaining only the first term of the positive
tail proves its lower bound.

For $N\ge1$, let

$$
H_N=\min\{H\ge1:16^H\ge200(N+1)^2\},\qquad
R_N=\min\bigl(N,(H_N-1)(1+\lfloor\log_2(2N)\rfloor)\bigr).
$$

Then for the single fixed carrier $\alpha=\xi$,

$$
\boxed{C_N^0\ge N-R_N=N-O((\log(N+1))^2).}
\tag{SC-7}
$$

**Proof.** For a time $n\le N$, let $p$ be the least power of
two with $p\ge n$, and put $d=p-n+1$. The first nonzero
future digit is at that distance, so

$$
y_n=\sum_{2^j\ge n}16^{n-1-2^j}
\le\frac{16}{15}16^{-d}.
$$

If $d\ge H_N$, then

$$
y_n\le\frac{16}{3000(N+1)^2}
<\frac{47}{8192(N+1)^2}\le\frac{47}{8192(n+1)^2}<T_n.
$$

The strict numeric comparison is the integer inequality
$131072<141000$. The only possible failures have
$p-n+1<H_N$. For each power $p\le2N$, at most $H_N-1$
times have this property. There are $1+\lfloor\log_2(2N)\rfloor$
such powers. This proves (SC-7), with all future sparse digits retained.

The logarithmic-squared missing count also has a matching lower bound.
Put $J=\lfloor\log_2N\rfloor$. For each $1\le j\le J$,
$p=2^j$, and $1\le d\le\lfloor j/2\rfloor$, the time
$n=p-d+1\ge p/2$ has

$$
y_n\ge16^{-d}\ge p^{-2}>\frac{4}{15p^2}>T_n.
$$

These times are disjoint for distinct powers $p$. Hence

$$
\boxed{\left\lfloor\frac{J^2}{4}\right\rfloor
\le N-C_N^0\le R_N.}
\tag{SC-7a}
$$

In particular the zero-seam occupation is $N-\Theta((\log N)^2)$
for this one fixed carrier. This matching statement concerns the zero
seam, not the count of all sixteen seam windows.

These changed-seed states use the exact original forcing but have seed
$(\xi-\pi)/16\ne0$, since $\xi<1/15<3<\pi$. They are
nonnormal: the inherited sparse-tail summation, or summing directly over
the powers, gives

$$
\sum_{n=1}^N y_n\le\frac{1+\lfloor\log_2N\rfloor}{15}+\frac1{225}.
$$

Therefore, for every fixed integer $h$,

$$
\left|\sum_{n=1}^N e\bigl(h(16^{n-1}\xi-T_n)\bigr)-N\right|
\le2\pi|h|\left(B+\frac{1+\lfloor\log_2N\rfloor}{15}+\frac1{225}\right).
\tag{SC-8}
$$

This is not a zero-seed counterexample, and it does not falsify pi
normality. It decisively falsifies deriving a vanishing moving-seam
density from the complete forcing, tail summability, and a finite
irrationality measure without using the zero selector.

### Elementary finite-type check independent of the imported mu=2 theorem

For every integer $p$ and positive integer $q$,

$$
\boxed{|\xi-p/q|>\frac1{32q^3}.}
\tag{SC-9}
$$

For $q\ge4$, choose the first $Q_j=16^{2^j}>4q$. Then
$Q_j\le16q^2$. The truncation $\xi_j=P_j/Q_j$ is reduced,
because its numerator is 1 modulo 16; it differs from $p/q$, whose
denominator is smaller than $Q_j$. Thus
$|\xi_j-p/q|\ge1/(qQ_j)$, while

$$
0<\xi-\xi_j=\sum_{k\ge1}Q_j^{-2^k}<2/Q_j^2<1/(2qQ_j).
$$

Subtracting gives $|\xi-p/q|>1/(2qQ_j)\ge1/(32q^3)$.
For $q=1,2,3$, the closest candidate is zero because
$0<\xi<1/15<1/(2q)$, and $\xi>1/16>1/(32q^3)$.
This elementary bound is deliberately weaker than the inherited
classical exponent-two result. It supplies a fully internal finite-type
obstruction, with no imported irrationality theorem needed for SC-7.

## 4. Hole contract, controls, and next discriminating obligation

**Earned:** an all-carrier source-tail theorem controlling fifteen cuts,
an exact single-wrap residual for arbitrary digit functions, nonlinear
moving-lag transport outside that residual, and a finite-type carrier
with near-maximal authentic-tail seam occupation.

**Not earned:** an improved selected pi signed-Weyl estimate, an upper
bound on $C_N^0(\pi)$, or any independent stochastic branch law.

**Falsifiable next boundary statement:**
$C_N^0(\pi)=o(N)$, for the zero-selected BBP source. This would
transport all bounded one-digit observers with o(N) error. It is weaker
than normality and would not itself establish uniform digit frequencies.
The exact zero seed must enter any proof, since SC-7 preserves the whole
forcing and finite Diophantine type while violating it maximally.

**Instrument controls:** enumerate all 16 half-open boundary cases;
retain the zero boundary when testing the decomposition; a mutation that
drops the wrap jump must fail on $\alpha=0$; enumerate nonzero-cut
events and verify their packing gaps; classify sparse good times using
only integer powers and certify the entire future sparse and Green tails.
The source lower bound is checked by its explicit polynomial factorization.
No finite run validates an infinite assertion here: the proofs do that.
