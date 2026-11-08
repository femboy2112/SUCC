# Sharp replica energy and a normal but strongly correlated control

Status: **PROVED PAPER**, with separate finite oracles. No new Lean
certification or worldwide novelty claim. The original-zero signed gate is OPEN.

## RE1. An explicit sharp subaction for every even multiplier

For every even integer b>=2 and every real theta,

    b cos(theta) + cos(b theta) >= -(b+1) cos(pi/(b+1)).       (RE1)

Equality holds exactly at theta=pi +/- pi/(b+1) modulo2pi.

Proof. The derivative vanishes precisely when
`sin((b+1)theta/2) cos((b-1)theta/2)=0`. At the first family of stationary
points theta=2pi*k/(b+1), the value is `(b+1)cos(theta)`; since b+1 is odd,
its minimum is `-(b+1)cos(pi/(b+1))`, at the two stated points. At the other
family theta=(2k+1)pi/(b-1), the value is `(b-1)cos(theta)>=-(b-1)`.
The latter is strictly larger: putting n=b+1>=3,
`n(1-cos(pi/n)) <= pi^2/(2n)<2`. Compactness of the circle and elementary
calculus complete the proof. QED.

Write f(theta)=cos(theta), T(theta)=b*theta and g=-f/(b+1). RE1 is the
nonnegative subaction certificate

    f + cos(pi/(b+1)) - (g o T-g) >=0.

Consequently every T-invariant probability measure has
`integral f >= -cos(pi/(b+1))`. Equality forces support on the displayed
two-cycle; invariance forces its two weights to be1/2. This is the unique
minimizing invariant law. This application uses an explicitly proved
coboundary certificate, within the classical framework of
[ergodic optimization](https://arxiv.org/abs/1712.02307).
For odd b, the fixed point theta=pi gives f=-1, so the even-base conclusion
fails. This parity control is necessary.

## RE2. A robust finite, authenticated two-replica energy floor

Let v_0,...,v_(m-1) be unit complex numbers, m>=1, satisfying

    |v_(r+1)-v_r^16| <= eta_r,          0<=r<m-1.

Define `E=(1/m)sum_r (1+Re v_r)/2`, and put `c=cos(pi/17)` and
`s2=(1-c)/2=sin(pi/34)^2`. Then

    E >= (1-1/m)*s2 - (1/(34m))*sum_r eta_r.                 (RE2)

Proof. Sum RE1 for r=0,...,m-2 and replace `Re(v_r^16)` by
`Re(v_(r+1))` with the declared errors. The remaining endpoint contribution
is `Re v_0+16Re v_(m-1)>=-17`. Thus
`17 sum Re v_r >= -17c(m-1)-17-sum eta_r`, which is exactly RE2.
The formula is also valid for m=1. QED.

For the authentic prime clock with **q=2**, n0=L+1 and L=2m, set

    v_r=e(h*(U_(n0+r+m)-U_(n0+r))),
    B_r=(b_(n0+r)+b_(n0+r+m))/2.

The two local principal parts coincide, so `|B_r|^2=(1+Re v_r)/2`.
The source recurrence gives, exactly on all interior edges,

    v_(r+1)=v_r^16 e(h*(r(n0+r+m+1)-r(n0+r+1))).

Therefore RE2 applies with
`eta_r=2pi|h|*|r(n0+r+m+1)-r(n0+r+1)|`. The original source has the
positive anchored identity, for d=8n-7,

    r(n)=6/[d(d+3)]+4/[d(d+4)]+5/[d(d+5)],

so it is decreasing and `0<r(n)<15/(8n-7)^2`. An immediately computable
version is

    mean |B|^2 >= (1-1/m) *
      (sin(pi/34)^2 - 15pi|h|/[17(8n0+1)^2]).               (RE2-source)

Along any q=2 clocks with n0,m->infinity and fixed h, the liminf is at least
`sin(pi/34)^2`, approximately0.00851345. **Existence of infinitely many
selected q=2 primes is not proved here.** The statement is conditional only
on such a sequence of clocks being given, not on unproved source mixing.

This is sharp for the homogeneous transport class: phases8/17,9/17 attain
the invariant constant. It need not be sharp for the literal-zero source.
It improves the squared consequence1/289 of the earlier1/17 L1 floor;
it does not assert a new larger L1 floor. It applies equally to appropriate
same-forcing controls, so it cannot select zero or establish signed decay.

## RE3. Near-minimal energy identifies a two-cycle, not Haar behavior

Let `F(v)=16Re v+Re(v^16)+17c>=0`. Let K_delta be the compact set of
unit phases at angular distance at least delta>0 from the two equality
points, and suppose K_delta is nonempty. Its minimum kappa_delta of F is
strictly positive. For the finite path of RE2,

    (1/m) sum_(r<m-1) F(v_r)
       <=34(E-s2)+17(1-c)/m+(1/m)sum eta_r.

Hence the fraction of the m samples with r<m-1 and v_r in K_delta is at
most that right side divided by kappa_delta. Proof: sum the exact identity
for F and use the same endpoint bounds; then use F>=kappa_delta on K_delta.
This converts an energy near its extremal floor into a quantitative
concentration conclusion. No numerical value of kappa_delta is needed for
the stated theorem. It exposes the non-Haar mechanism at the floor.

## RE4. Fixed-frequency normality does not force large-lag replica decorrelation

There exists a base16-normal real alpha and a sequence m_k->infinity with

    (1/m_k) sum_(n=2m_k)^(3m_k-1)
      e(h*(16^(n+m_k)alpha-16^n alpha)) ->1               (RE4)

for every fixed integer h. Thus its two-replica energy tends1 along these
growing lags, even though all its fixed nonzero Weyl means tend0.

Construction and proof. Let C_k be a base16 de Bruijn cycle of order k,
length d_k=16^k, so each k-letter word appears exactly once cyclically.
Rotate C_1 to begin with digit0. Existence follows by taking an Euler circuit in the directed graph whose
vertices are (k-1)-letter words and whose edges are k-letter words. Equal
in/out degrees and connectivity give a circuit containing every edge.
Let m_k=16^(k^2), N_k=4m_k, N_0=0. Fill digit positions
`N_(k-1)+1,...,N_k` with repetitions of C_k, truncating the last copy.

Fix a word length j. For k>=j, the count of any j-word in any prefix of
the periodic C_k sequence differs from its uniform count by O(d_k+j),
because every complete cycle has exactly16^(k-j) occurrences. Counting
across stage joins adds O(j) per join. For N in stage k the total error
is a fixed finite initial contribution plus O_j(sum_(i=j)^k d_i+k).
As N>=N_(k-1) and `d_k/N_(k-1)->0`, division by N proves normality for
every j. The short k=1,2 beginnings do not affect the limit.

For k>=2, the interval of digit positions from2m_k+1 through4m_k is
inside stage k. Since d_k divides m_k, tails starting at n+1 and n+m_k+1
agree for at least3m_k-n digits, for2m_k<=n<3m_k. Thus their real
fractional parts differ by at most16^(-(3m_k-n)), and

    |mean e(h*(16^(n+m_k)alpha-16^n alpha))-1|
       <= (2pi|h|/m_k) sum_(j=1)^m_k 16^(-j)
       < 2pi|h|/(15m_k).

This proves RE4. The same statement holds for the same-forcing history
with seed `s=alpha-pi/16`, because the established Green tail tends0
uniformly on these windows. The first digit0 ensures alpha<1/16<pi/16,
so this is a nonzero-seed control, not a statement
about rational principal parts of this irrational history.

**Scope:** these m_k are prescribed temporal lags, not asserted orders of
selected prime clocks. This refutes deducing general growing-lag
decorrelation from fixed-frequency normality alone. It does not refute a
source-specific prime-clock theorem. In particular, the empirically observed
energy near1/2 cannot be promoted from normality without additional uniform
correlation control. The de Bruijn ingredients are classical; see
[de Bruijn's original paper](https://pure.tue.nl/ws/portalfiles/portal/4442708/597473.pdf).

## Repository connections and contribution

- [HCB2](../complement_budget/hostile/THEOREMS.md) supplied the earlier
  two-replica L1 obstruction. RE1–2 replace its triangle estimate by an exact
  extremal subaction for squared energy; the forcing and clock remain intact.
- [CZR foundations](../../2026-10-25/COHERENT_ZERO_FOUNDATIONS.md) distinguish
  exact coboundaries from source-selected asymptotic bounds. RE1 gives an
  explicit nonnegative remainder, while RE4 prevents a stronger mixing
  conclusion from being inferred from the Weyl target itself.
- `observational_succ/circle_gamma_prime_digits.py` already uses de Bruijn
  edge flows; `observational_succ/maximal_novelty_source.py` tests binary
  de Bruijn histories. RE4 applies this finite combinatorics to a growing-lag
  obstruction with an infinite normality proof.
- The [observer front](observer/THEOREMS.md) reconstructs two-point laws
  from their mean. RE2 controls an average energy, not pointwise conditioning;
  it does not remove that reconstruction's near-zero instability.

The remaining useful upper estimate is still source-selected signed
covariance decay. These results constrain instruments and asymptotic
inferences without proving that estimate. Pi normality: OPEN. RH: OPEN.
