# Direct diagonal/Frobenius transport: a proved domain obstruction

**DF-01, local paper proof using inherited conductor births.** The generating
series sum_(n>=0) U_n z^n of the authentic selected rational BBP trajectory
is not the diagonal of any finite-variable rational function over Q that is
regular at the origin. The same conclusion holds after multiplication of
U_n by any fixed nonzero rational function of n (ignoring its finitely many
zeros/poles). This is a restriction on a direct proposed representation,
not a theorem against Dwork methods with a different auxiliary object.

## Proof by denominators

If F(x_1,...,x_d)=A/B is rational over Q with B(0)!=0, choose one positive
integer M containing the denominators of every coefficient of A,B and the
numerator of B(0). The formal geometric expansion of 1/B has all its
coefficients in Z[1/M]. Every coefficient of F, and hence every diagonal
coefficient, lies in that same fixed localization. Only finitely many
denominator primes are possible. This assertion uses no analytic continuation.

The authentic first-birth theorem AT-03 of PR #399 says that, for every odd
prime q and every a>=1, at

```
b(q^a) = (q^a+7)/8  if q^a=1 mod8,
         (q^a+3)/8  if q^a=5 mod8,
         (q^a+1)/4  if q^a=3 or7 mod8,
```

the rational U_b has v_q(U_b)=−a. The residue is respectively 4,−1,−1/2;
the small q=3,5 cases are part of that proof. Choosing q outside the finite
prime set of M contradicts the proposed direct diagonal identity.

For a fixed nonzero rational function R(n)=P(n)/Q(n) over Q, clear the fixed
coefficient denominators and use the inherited sharp theorem
log den(U_n)=6n+o(n). Multiplying by P(n) removes at most log|P(n)|=O(log n)
from the denominator; dividing by Q(n) adds at most O(log n). Thus

```
log den(R(n) U_n) = 6n+o(n).
```

If these denominators had support in a fixed finite prime set S, their
logarithms would instead be O_S(log n): v_q(den U_n)<=floor(log_q(8n))
from the source LCM, and R(n) adds at most O_R(log n). Contradiction.
Finite changes of initial coefficients cannot repair either argument. QED.

## DF-02. Every odd prime has infinitely many integral-model failures

At the birth times b(p^a), v_p(U_b)=−a for every a. No fixed multiplicative
constant p^m makes the whole original sequence p-integral, at any odd p.
Thus the direct original coefficient sequence does not meet the integral
constant-term hypotheses in Mellit–Vlasenko's Dwork theorem, or the
integral rational-diagonal setup used for automatic congruences. Merely
renaming the one-step source Gamma ratio as a Frobenius matrix does not
repair this failure. A time-dependent denominator clearing may be valid,
but its exact effect on the selected complementary character must be proved.

At p=2 the authentic canceled rational source and trajectory ARE integral,
and the inherited finite odometer/isometry supplies exact residue cycles.
The positive age-family mutants preserve arbitrary fixed precision and
eventual complete finite cycles. These facts refute the inference from
the available two-adic automaton alone to real-circle equidistribution.

## Compatible adelic statement and its limitation

Every rational U_n has a finite primary decomposition in Q/Z, and its
real root of unity is the product of those primary characters. This is an
exact identity on rational inputs. The all-prime affine Morita derivatives
reproduce individual unit/polar source pieces; they do not supply an
independent random measure on the changing primary components. A finite
product of normalized absolute values obeys the classical product formula;
it controls height, not the sign of e(hU_n).

The Gauss dossier strengthens this distinction: fixed-field algebraic
reconstruction fails by the actual cofiber conductor, and arbitrarily many
ordinary finite-field Gauss sums still miss higher prime-power roots at
authentic birth times. Galois-averaged Ramanujan cancellation is a different
test space from the one selected complex embedding. None of these negative
results excludes an analytic estimate using all places and the zero boundary.

## Primary sources and applicability audit

- Mellit and Vlasenko, [Dwork congruences for constant terms of Laurent
  polynomial powers](https://arxiv.org/abs/1306.5811): the constant-term
  object and its integral model are actual hypotheses, not conclusions
  from a Gamma-shaped formula.
- Rowland and Yassawi, [Automatic congruences for diagonals of rational
  functions](https://arxiv.org/abs/1310.8635): the rational diagonal and
  reduction assumptions must be supplied first.
- Lagarias, [On the Normality of Arithmetical Constants](https://arxiv.org/abs/math/0101055):
  Hypothesis A is a conjectural dynamical input, not an available selected
  orbit theorem. The Gamma description here does not establish it.

Literature checked 2026-10-30. No scholarly-priority claim is made for the
elementary denominator argument or its application.
