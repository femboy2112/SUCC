# Low-slip words, a sharp collision countermodel, and Stoneham's actual grid

All statements here are paper proofs in their stated domains, not Lean proofs
or external refereeing. No assertion of scholarly priority. The BBP source is
exactly the four signed poles in PR411; its selected seed remains zero. The
counterseed is explicitly different. Author provenance for the SUCC triangle,
Harmonic/Golden/Euler–Mascheroni and Oily–Macaroni is preserved; no positive
observer law is substituted for the selected digit law.

## C1. An exact bridge from low-slip cylinders to hexadecimal words

Write D(x)={16x}, y_n={U_n+T_n}, t_n=T_n-T_(n+1). For every real seed,

    U_(n+1)-U_n = 15(U_n+T_n)+t_n,
    ||U_(n+1)-U_n|| = ||15 y_n+t_n||.                 (1)

The equality is in the real line before reduction in its first version.
For the authentic source, the proved tail bound is

    0<t_n<=16/(8n+1)^3.                              (2)

This is the exact connection missing from an identification of the two cylinder
types: the low-slip set at time n is the inverse image under multiplication by
15 of the arc [-delta-t_n,delta-t_n], whereas a digit cylinder is an inverse
image under powers of D. They are different sets.

**Theorem C1a.** Take delta=1/20, A>=2 and L>=1. Let K be the number of strict
slips ||U_(n+1)-U_n||>delta among n=A,...,A+L-1, for any seed with the authentic
forcing. The length-L hexadecimal word of the completed orbit starting at A
has at most min(L-1,2K) adjacent digit changes. In particular K=0 forces a
constant word. This theorem applies in particular to U_0=0, without asserting
that K is large there.

**Proof.** Put eps=delta+16/(8A+1)^3. Direct rational comparison at A=2 gives
eps<1/17; the bound decreases with A. At a good position,
||15y_n||<=eps. Thus y_n lies within eps/15 of one of the 15 distinct fixed
points j/15, j=0,...,14 of D. If two adjacent positions are good, their centers
must correspond to the same fixed point: after applying D the first error is
at most 16eps/15, the second at most eps/15, whereas two different centers
are separated by at least 1/15. The strict inequality 17eps<1 excludes this.

For j=1,...,14, the interval of radius eps/15 about j/15 is contained in the
digit-j cylinder: its distance to either boundary is at least 1/(15*16),
and eps<1/17<1/16. Near j=0 the two sides give digit 0 and digit 15; applying
D preserves the side while both positions are good. The point zero itself
has digit zero and maps to zero. Therefore adjacent good positions have equal
digits. Every unequal adjacent pair has a bad endpoint, and each bad position
is an endpoint of at most two pairs. This proves the count. ∎

The result immediately gives a finite combinatorial cover: the possible words
with at most K strict slips are contained in a family of at most

    16 sum_(j=0)^min(2K,L-1) binom(L-1,j) 15^j        (3)

words. This upper bound is not a source-selected probability or exclusion.
As K/L becomes small, it describes low-transition words, but no arithmetic
argument here excludes the selected pi word from the resulting union.

**Theorem C1b (one-sided reverse inclusion).** If the completed orbit has a
constant hexadecimal word of length L+2 beginning at A>=2, all the first L
positions are low-slip at delta=1/20.

**Proof.** If the repeated digit is d, the initial point is within 16^-(L+2)
of d/15 in circle distance (including d=0 and d=15). At the last of the first
L positions, ||15y_n||<=15/16^3=15/4096. Hence (1)-(2) give

    ||U_(n+1)-U_n|| <=15/4096+16/(8A+1)^3 <1/20.

The last inequality already holds at A=2. ∎

The two-cylinder gap is real: a constant word of length L alone need not give
L low slips. For example y=1/32 has first digit zero but ||15y||=15/32.
Theorems C1a/C1b retain the complete source tail. They apply to changed seeds
too and consequently cannot themselves prove a zero-boundary theorem.

**Corollary C1c (two-sided transition comparison).** If C counts adjacent
digit changes in the length-L completed word and K counts the corresponding
strict lag-one slips, then

    (K-2)/2 <= C <= 2K.                              (4a)

Indeed C1b with L=1 says that each slip must have a digit change on at least
one of its next two edges. At most two slips near the right endpoint need
edges outside the length-L word; each internal change can account for at
most two slips. Thus K<=2C+2. Together with C1a this proves (4a). Positive
lower density of these slips is equivalent, up to factors, to positive lower
density of digit transitions. This is a substantial typing restriction on
what the lag-one route could prove; it is not a normality certificate.

For general frequency h, (1) becomes ||15h y_n+h t_n||. If
delta+|h|16/(8A+1)^3<1/17, adjacent good centers j/(15|h|) follow the exact
finite map j ->16j mod 15|h|. Calling those centers constant hexadecimal words
would be wrong for h!=1. Radix seams require their own digit branches.

## C2. Every lag-one position can slip while the finite-band energy diverges

Let beta=1/255=0.overline(01)_16 and choose the *changed* seed
s=(beta-pi)/16. It has the original forcing, but s!=0. Its completed orbit is

    y_(2j+1)=1/255,  y_(2j+2)=16/255.

Thus ||15y_n||=1/17 at every time. By (2), for every n>=2,

    ||U_(n+1)(s)-U_n(s)|| >=1/17-16/(8n+1)^3 >1/20.  (4)

All sufficiently late lag-one positions are strict slips, with a fixed margin.
Nevertheless for every even N and integer H>=1 the exact completed Fejer energy
is

    F_(H,N)(y) = (H+F_H(1/17))/2 >=H/2.              (5)

There are N^2/2 ordered equal-state pairs and N^2/2 cross-state pairs at
distance 1/17. Nonnegativity proves (5). The original-source Green transport
from PR411 applies for every seed, so

    F_(H,N)(U(s)) >= H/2-pi(H^2-1)/(24N).            (6)

At the declared H_N~N^(1/3), this is H_N/2-o(1), failing the subexponential
finite-band certificate despite *maximal* lag-one slip density.

**Verdict.** Positive-density lag-one phase slips, even every-position slips,
do not suffice to control pair collisions. A source-selected theorem needs
more frequency/context information. This is a concrete obstruction to a
universal inference, not a counterexample to an as-yet-unproved zero-seed
estimate. No rational p-adic residue is assigned to the irrational seed s.
The completed rational orbit beta and the rational difference-coordinate
calculations are separate typed objects.

The period-two completed word has Q_m=16^m/2 for m>=1. Its exact selected
Walsh refinement obeys all 15-channel identities yet grows exponentially.
An order-two de Bruijn cycle strengthens the finite-context warning:
Q_1=Q_2=1, Q_3=16, and Q_m=16^(m-2) thereafter. Such balanced short contexts
do not force higher-context contraction.

This obstruction has a concrete spectral repair test: at frequency h=17,
e(17y_n)=e(1/15) at every time, so the completed Weyl magnitude is exactly N.
For the forced representation, the original summable Green budget gives
|sum_(n<=N)e(17U_n(s))|>=N-34pi B, with B=sum T_n<1/32. Retaining frequency
17 detects the period-two organization that lag-one slips at h=1 miss.

## C3. Direct all-horizon Stoneham finite-band estimate

This section independently reconstructs the arithmetic of PR395 at commit
2d4fcc6db5657a2559b0e28ca8c8e1413b6c4548. Its interval bound is valid, including
the incomplete last stage; we found no missing interval-length factor.
Normality of Stoneham constants is classical, e.g. Bailey–Crandall,
*Random Generators and Normal Numbers* (2002),
https://www.davidhbailey.com/dhbpapers/bcnormal-em.pdf.
The following proof uses the actual finite conductor grids directly and does
not assume normality to infer a moving-scale estimate.

For c in {3,5}, let

    alpha_c=sum_(p>=1) 1/(c^p 16^(c^p)),
    x_n={16^n alpha_c},
    z_n={sum_(c^p<=n) 16^(n-c^p)/c^p},  n>=0.

At stage c^p<=n<c^(p+1), z_n is on the translated uniform grid

    G_p={(1+cj)/c^p : 0<=j<c^(p-1)}.

The birth numerator is 1 mod c. Since v_c(16-1)=1, the elementary binomial/LTE
identity v_c(16^k-1)=1+v_c(k) proves ord_(c^p)(16)=c^(p-1).
There are exactly c(c-1) traversals of G_p per complete stage; every partial
stage has multiplicity at most M=c(c-1). The same conclusion fails for c=2,
because 16 is not invertible modulo its conductors.

The positive future correction delta_n satisfies x_n={z_n+delta_n}. Summing
by impulses, using positivity to exchange the series, gives the particularly
useful all-horizon budget

    sum_(n>=0) delta_n
      =sum_(p>=1) (1-16^(-c^p))/(15c^p)
      <1/[15(c-1)].                                  (7)

**Theorem C3.** For N>c, H>=2 and P=floor(log_c(N-1)),

    F_(H,N)(x_0,...,x_(N-1))
      <= c + H[c+c(c-1)P]/N
           +4pi(H^2-1)/[45(c-1)N].                   (8)

In particular H=O(N^(1/3)) yields limsup F<=c. This improves the direct
3c calibration constant in PR411 without any conclusion about BBP pi.

**Proof.** For a grid of q points, finite Fourier orthogonality gives

    sum_(j=0)^(q-1) F_H(a+j/q-t)
      =q[1+2 sum_(l>=1,lq<H)(1-lq/H)cos(2pi*lq*(a-t))]
      <=q+H.                                        (9)

For completeness, if k=floor((H-1)/q), then
2k-(q/H)k(k+1)<=H/q because (k-H/q)^2+k>=0.
This proves the inequality, including q>=H where the sum is exactly q.

For every t, nonnegativity of F_H permits replacing each partial stage by
its complete multiplicity grid. The first c indices cost at most cH.
Moreover sum_(p=1)^P M c^(p-1)=c^(P+1)-c<cN. Hence

    N^-1 sum_(n<N) F_H(z_n-t)
      <=c+H(c+MP)/N.

Integrate in t against the empirical z law. This bounds the full paired
surrogate energy, not just a primary character marginal. The derivative bound
||F_H'||_infty<=2pi(H^2-1)/3, coupled with (7) and the same ordered-pair
transport argument as PR411, gives the last term of (8). ∎

The actual residue law and uniformly bounded multiplicity are load-bearing.
BBP's exponentially large exact conductor grids do not supply either (9) at
cost O(N), or a multiplicity budget. The original Green tail supplies only
the approximation leg; the missing arithmetic cannot be inferred from the
coincidence of exceptional primes 2,3,5.

## Remaining selected obligation and attempted contradiction

C1 converts a hypothetical low-slip exclusion into a concrete statement about
near-constant selected digit words. We tried to use this as an inverse theorem
for large Fejer energy. C2 refutes the needed universal inverse implication:
large energy can arise from a period-two organization with no low-slip
positions at all. The all-context Walsh energy detects it, but gives no bound.

A meaningful weaker next obligation is an authentic-zero-seed bound excluding
*all short-period organizations at the moving depth*, with explicit weighted
coverage of time pairs, rather than merely excluding fixed-point shadowing.
Even that only handles one inverse-theorem class. The unrestricted selected
finite-band upper bound remains DARK. No positive-density pi dispersion or
new all-horizon signed cancellation is claimed by this front.
