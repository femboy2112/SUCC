# General carrier, authentic realization, and an observer that preserves the update

**Scope.** This is a mathematical carrier and observer construction assembled
from the proved results of this round and parent #417. It specifies actual
maps and retained information. It does not derive the BBP coefficients from
counting, identify a mathematical observer with a physical mind, or prove
selected digit cancellation.

## 1. Build the arithmetic carrier before selecting the source

Begin with finite labeled sets and selection histories. At time n, binary
selection words of grade k are counted by `C(n,k)`. Concatenating labeled
blocks gives the Pascal and Vandermonde identities. Keep the histories and
their colored block embeddings: endpoint grade alone forgets their order.

Cardinality gives N; signed additive completion gives Z. The retained
mixed grade-two operation recovers the ordinary integer product through

    ab=C(a+b,2)-C(a,2)-C(b,2).

Localizing nonzero integers then gives Q. These are explicit arithmetic
constructions, not a claim that an unlabelled triangle determines every
possible physical or semantic structure.

The first-jet carrier is the unit group of `Q[epsilon]/(epsilon^2)`. Every
unit is uniquely `a(1+q epsilon)`, with `a!=0`. Its operations are

    (a,q)*(c,r)=(ac,q+r),       (a,q)^m=(a^m,mq).

The maps `value(a,q)=a` and `L(a,q)=q` distinguish the multiplicative
rational value from the additive logarithmic first derivative. Keeping
only the value loses the entire q-coordinate.

| Layer | Retained object | Exact map or update |
|---|---|---|
| Finite Pascal carrier | Labels, time, selection histories, grades | Concatenation and Pascal/Vandermonde composition |
| Integer/rational arithmetic | Signed cardinalities and fractions | Grade-two multiplication, then localization |
| Dual-number unit | Rational pair `(a,q)`, `a!=0` | Product `(ac,q+r)`; logarithmic observation `L=q` |
| Source instance | Clock, exact rational source law, initial function | `B_(n+1)=B_n^16 V(8n+1+u)` |
| Exact finite observer | `n,U_n`, integer lift, circle residual, source carry | `U_(n+1)=16U_n+r(n+1)` |
| Additional observations | Prime components or rational-frame value ratios | Typed character reconstruction or certified log intervals |

## 2. Realize the authentic BBP instance

Select the declared source contract

    V(a)=a^4/[(a+3)^2(a+4)(a+5)],
    R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5),
    r(n)=R(8n-7),       B_0(u)=1.

Define the finite rational-function carrier recursively by

    B_(n+1)(u)=B_n(u)^16 V(8n+1+u).

Let `J(f)=f(0)(1+(f'(0)/f(0))epsilon)` whenever f is regular and nonzero
at zero. The product rule gives `J(fg)=J(f)J(g)` and `J(f^16)=J(f)^16`.
The identity `V'/V=R` therefore gives a commuting update:

    L(J(B_(n+1)))=16 L(J(B_n))+r(n+1).

Consequently `U_n=L(J(B_n))` is exactly the original rational recurrence
with `U_0=0`. The source is an authenticated specialization of the general
carrier; its coefficients have not been deduced from Pascal counting.

## 3. Embed an observer with sufficient retained state

At a finite horizon the observer may store the source identifier and
contract, clock n, exact rational U_n, and its decomposition

    ell_n=floor(U_n),       x_n=U_n-ell_n.

Its next literal source carry and state are computed by

    kappa_(n+1)=floor(16x_n+r(n+1)),
    x_(n+1)=16x_n+r(n+1)-kappa_(n+1),
    ell_(n+1)=16ell_n+kappa_(n+1).

Thus the observation commutes with the declared carrier update. These
records admit finite integer encodings at every finite time; their size
can grow. No fixed memory bound for all time is asserted. A coarse digit
or endpoint-grade observation generally lacks this closure.

**Closure and faithfulness proposition.** Inside the stated class of
sources `sum_i c_i/(8n-b_i)` with at most four distinct simple poles,
no polynomial part, fixed clock 8 and `|b_i|<8`, the eight-moment authentication certificate identifies the
original source uniquely. The displayed potential V is uniquely fixed by
its logarithmic derivative R and the normalization V(a)->1 as a->infinity:
the quotient of two such potentials has zero logarithmic derivative, hence
is constant, and the normalization fixes that constant. Once this V and
`B_0=1` are fixed, the rational-function recurrence determines every B_n
uniquely. Applying J
and L determines every U_n, and the floor formulas determine every
literal carry uniquely. Proof: source authentication followed by induction
on n and the displayed commuting maps. This is faithfulness for these
specified observables and hypotheses, not injectivity of every quotient
of the carrier.

## 4. Keep finite states, completions, and readouts separate

The finite U_n is rational. The completed real boundary is a different
object:

    alpha=sum_(j>=1)16^(-j)r(j)=pi/16,
    U_n=16^n alpha-T_n,
    T_n=sum_(j>=1)16^(-j)r(n+j)>0.

The real tail is not an exact finite rational memory item. Source-derived
intervals can bound it. Literal forced carries must not be substituted
for pure radix digits without retaining the tail's integer seam.

All additive prime principal parts recover `U_n mod Z`; their assembly
requires the global carry seam proved in PRIME_FRAME_TRANSPORT. Prime
valuations of B_n(0) instead observe the multiplicative value and miss
changes to the initial first derivative.

Rational-frame ratios `B_n(1/M)/B_n(0)` yield exact prime-log expressions.
Their real logarithms have certified rational interval readouts and the
proved error bounds approaching U_n. A first jet alone does **not**
determine these nonzero-frame values: initial functions 1 and `1+u^2`
have identical first jets but different frames. Retain the full declared
source and initial-function law, or the corresponding finite rational
expression, whenever such frame measurements are used.

These maps establish source identity and observation adequacy within their
domains. The remaining estimate concerns the signed time distribution of
the selected U_n. Exact encoding, faithful updating, and arbitrarily
accurate readout do not supply that statistical theorem.
