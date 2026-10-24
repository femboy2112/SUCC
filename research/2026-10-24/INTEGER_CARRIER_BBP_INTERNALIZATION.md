# OPERATION INTEGER HOST: BBP is an internal program, not the carrier

2026-10-24. Research-only; proposed against main
`e648df3e4fca73ab6b942232b5ca4b310e9cac08`.
**Pi normality in every base: OPEN.** Paper proofs and exact finite tests;
no new Lean proof, physical-carrier identification, or scholarly novelty claim.
The main source archives are unchanged. All `ICB` labels below are LOCAL
manuscript identifiers, not installed theorem-registry admissions.

## 0. Live-context audit and the user's actual proposal

The user proposes an ordinary N or Z carrier with a model INSIDE it handling
BBP, rather than identifying the rational BBP observation with the carrier.
That distinction agrees with SUCC's founding separation of carrier, source,
record, representation, and observable. It does not require abandoning BBP.

Main is still the #267 consolidation. Latest inspected sibling research:
- #270 `3acd547ff122368d5694efdab029b3156a292d8a`: authenticated dyadic
  isometry of the UNWRAPPED source; real-circle statistics remain open.
- #272 `6e8fa8b77886b13f1f533ed8083fd88c849d14b3`: source jets, conductor
  heights and filters, with source-selection/real-frequency firewalls.
- #277 `5d51f9329149cdbf0db1fce3065924c681f64de6`: odd-denominator source,
  full prime reconstruction, and genuinely noncommuting all-prime limits.
- #278 `e50a7b88e2eec8d7815e1aab3fd860d5f4f29983`: trimmed joint entropy,
  rational-function source authentication, weakened conditional targets.
- #279 `c098f44b29c9671ecd3050f2934eea8676a111c4`: exact source-relative
  twisted-pair comparisons; common-mode cancellation is not pi normality.
These are inspected, NOT silently merged or used as installed Lean authority.

The exact rational source remains
  U_0=0, U_n=16 U_(n-1)+r(n), y_n={U_n},
  r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2).
BBP is a source-identification and observation algorithm, not an axiom that
its digit trajectory is random. Lagarias' classical orbit-shadowing theorem
is relevant: representations of this kind also exist for nonnormal numbers.
Gibbons' integer-state streaming pi algorithms are classical prior art for
integer-hosted generation; no priority claim for integer coding is made here.

## ICB-01. Entire authenticated state evolution uses natural integers only

An exact algebraic simplification, already in #277, gives
  r(n)=P(n)/D(n),
  P(n)=120n^2-89n+16,
  D(n)=(2n-1)(4n-1)(8n-7)(8n-3).
For integer n>=1 both are positive and D(n) is odd. Reduce P/D to a_n/b_n.
Set Q_0=1 and
  Q_n=lcm(Q_(n-1),b_n), g_n=Q_n/Q_(n-1), c_n=Q_n*a_n/b_n.
Then the NATURAL-INTEGER program
  A_0=0, A_n=16 g_n A_(n-1)+c_n                         (1)
satisfies U_n=A_n/Q_n exactly, by induction. No pi digits, real arithmetic,
Galois randomness or external statistical premise enters the state update.

Q_n is the LEAST positive nested conductor schedule that makes every forcing
sample through n integral. This is a conductor for the entire source prefix;
it need not equal the smaller reduced denominator of U_n itself.

Let R_n=A_n mod Q_n and H_n=floor(A_n/Q_n). Exact Euclidean division gives
  R_n=(16g_n R_(n-1)+c_n) mod Q_n,
  k_n=floor((16g_n R_(n-1)+c_n)/Q_n),
  H_n=16H_(n-1)+k_n.                                  (2)
Thus the internal integer model preserves the literal source carry, the
unwrapped source, and the fractional circle observation simultaneously.

All b_n divide the odd lcm through 8n-3: use
  r(n)=4/(8n-7)-1/(8n-3)-(3n-1)/[(2n-1)(4n-1)],
and gcd(2n-1,4n-1)=1. Hence Q_n divides that odd lcm.
In particular a crude elementary storage upper bound is O(n log n) bits;
U_n<16^n and the same order of bits suffices for A_n. No bounded-memory
finite automaton or constant-time large-integer arithmetic is asserted.

## ICB-02. A literal internal dynamical model on N, not just a metaphor

Let C be Cantor pairing C(a,b)=(a+b)(a+b+1)/2+b. Define on EVERY code in N
  F(C(n,A))=C(n+1,16g_(n+1) A+c_(n+1)),                (3)
where Q_n,g_n,c_n are computable from n by the fixed integer source program.
F is a TOTAL primitive-recursive map N->N and is INJECTIVE: differing n
land at differing levels, and at any fixed n the affine coefficient is positive.
A partial inverse subtracts c, checks divisibility by 16g and nonnegativity,
then unpairs. Inputs outside the image fail closed.
The authentic source is exactly the orbit F^n(0)=C(n,A_n).

There are TWO distinct arrows:
- external successor n -> n+1 on the clock N;
- internal update F on encoded integer model states.
The realization sigma(n)=C(n,A_n) satisfies F sigma=sigma SUCC. F is NOT
ordinary code+1. Executing F costs arithmetic operations and memory; encoding
states does not implement them for free in an embodied observer.
All rationals and real-circle phases are READOUTS of integer states, not
replacement ontologies. Physical carrier=N is not an empirical claim here.

## ICB-03. The finite authentic phase update is lossless, not sixteen-to-one

At a source step n, abbreviate q=Q_(n-1), q'=Q_n=gq and c=c_n. On the
old finite phase clock Z/qZ the map is
  f_n(x)=16g x+c mod q'.                              (4)
All q and q' are odd, so 16 is a unit. If f_n(x)=f_n(z), then q divides
16(x-z), hence x=z mod q. Its image is exactly the residue coset
  x' = c mod g,
and its inverse on that image is
  x=16^(-1)*((x'-c)/g) mod q.                          (5)
The implementation checks both the image condition and source level.

Therefore a final remainder R_N plus the authenticated conductor/forcing
schedule reconstructs EVERY previous phase R_n and every literal carry k_n.
The progressively larger conductor already retains that information. A single
fixed-size clock, arbitrary coarser residue, or unknown source schedule does not.

The unforced multiplier 16 is likewise an automorphism of the group of
rational torsion with odd denominator. In contrast, it is sixteen-to-one on
the complete real circle. There is NO contradiction: these are different
objects with different admissible inverses and topologies.

## ICB-04. The exact place the circle completion destroys inverse stability

Take q=16k-1 and x_k=1/q. In the odd rational torsion group,
  16^(-1)x_k = k/(16k-1),
because 16k=q+1. While x_k->0 in the real-circle metric, its unique odd-torsion
preimage tends to 1/16, not 0. Thus the inverse is NOT continuous for that
metric and cannot extend as a single-valued continuous inverse on the circle.

This is an explicit distinction between a reversible internal rational model
and an expanding, noninvertible completed observation. It does not imply
that all coding is hopeless or that real topology is invalid; it requires
naming which morphism a theorem needs to preserve.

## ICB-05. Four-bit carries are exact integer observations, not free fairness

Reducing the numerator update in (2) modulo16 yields
  k_n = (c_n-R_n)*Q_n^(-1) mod16.                     (6)
This is a source-authenticated path from the NATURAL-INTEGER state to the
four-bit carry residue. It does not assert that the 16 residue classes occur
with frequency 1/16. Literal forced carries can equal16 on valid odd-clock
states, so carry residue0 cannot automatically be interpreted as carry0.

At source time n>=1, let
  t_n=sum_(j>=1)16^(-j)r(n+j),
  e_n=floor(y_n+t_n), x_(n-1)={16^(n-1)pi}.
The authentic source identity gives x_(n-1)=y_n+t_n-e_n. The actual next
hexadecimal digit d_n=floor(16 x_(n-1)) satisfies
  d_n=k_(n+1)+e_(n+1)-16e_n.                          (7)
These boundary bits must NOT be suppressed by a marginal or average argument.
For each finite n the positive rational tail enclosures certify the digit
when both outward endpoints have the same floor. Exact source replay rejects
an altered numerator even if its conductor is canonical. Irrationality of pi
ensures eventual certification for each fixed digit, but no uniform depth
bound or digit-frequency theorem follows.

## ICB-06. Full selected collision counts become pure integer inequalities

For any finite list of states (n_i,Q_i,A_i), choose Q*=lcm_i Q_i and set
  X_i=(Q*/Q_i)*(A_i mod Q_i), 0<=X_i<Q*.
Then every real-circle pair distance is represented exactly by
  dist(y_i,y_j)=min(|X_i-X_j|,Q*-|X_i-X_j|)/Q*.
At radius1/M the exact predicate is simply
  M*min(|X_i-X_j|,Q*-|X_i-X_j|) <= Q*.                (8)
No floats, unknown pi digits, independent prime sampling, boundary erasure,
or pair-independence assumption enters. The complete selected source and all
cross-prime correlations survive in this SINGLE finite integer clock.

The current pi proof target is now a distributional theorem about the special
integer sequence X_i produced by (1), not a demand to embed an infinite real
carrier literally inside a finite one. Existing SCE/trimmed entropy bridges
can use these counts unchanged. Equation (8) has not been bounded at the
required growing scales: representing a pair predicate is not proving its
average small. Q* grows rapidly and generic whole-modulus estimates may be
far too expensive for the actual short selected time window.

## ICB-07. A new explicit continuity/error obstruction for source time

Despite all source arithmetic being integer-native, the authentic fractional
phase cannot be a continuous observation of the PROFINITE completion of the
time carrier. This is separate from internal computability on discrete N.

Suppose Phi:Zhat->T were continuous with Phi(n)=y_n for all n>=0.
For each fixed m>=0 take n_j=m+j!, so n_j->m profinitely and n_j->infinity
as a real integer. Continuity and the exact source recurrence, with r(n)->0
in the real metric, imply Phi(m+1)=16Phi(m). But Phi(0)=0 and
Phi(1)=y_1=2/15, a contradiction. The same proof for Z_p uses n_j=m+p^j.
It uses the ACTUAL forcing and initial state, not a mutated source.

There is a quantitative finite version. Let a decoder D read only n mod q,
q>=2, and have worst-case circle error epsilon on times 0,1,q,q+1.
The triangle inequality and Lipschitz constant16 give
  34 epsilon >= 2/15-r(q+1).
Since r(q+1)<=r(3)<1/15,
  epsilon > 1/510.                                    (9)
Letting the later two times be jq,jq+1 shows that ANY periodic decoder of
ANY finite period has all-time worst-case error at least1/255.

This does not deny the existing 2-adic source isometry: U_n in Q_2 and
{U_n} in the real circle use DIFFERENT readout topologies. It also does not
forbid finite-horizon reconstruction by n, source-adaptive resolution, or
full integer memory. It says that a fixed compact local-residue decoder
cannot replace the authentic ordered real observation uniformly in time.

## ICB-08. Integer hosting and reversible odd clocks do not force normality

Take a different source with
  t*_n=1/[(2n+1)(2n+3)],
  r*(n)=16t*_(n-1)-t*_n>0.
Every forcing value has odd denominator and is rational O(n^-2), and the
same natural-integer conductor compilation and injective odd-clock maps
apply, with initial U*_0=0. Yet
  U*_n+t*_n=16^n/3,
whose real-circle phase is fixed at1/3 under times16. Its tail is a positive
continuous moment sequence (t*_n=(1/2)int_0^1 t^(2n)(1-t^2)dt).
Thus simplicity, infinite memory, integer internalization and reversibility
can all coexist with a nonnormal selected orbit. This counterfeit changes
the exact four-pole BBP formula and is not a counterexample to pi normality.

## ICB-09. What this closes and the next source-dependent problem

CLOSED: literal N-native generation, internal exact BBP realization,
reversible finite source phases, faithful literal-carry and pair-count
readouts, source-only finite digit certification, and an explicit
profinite-to-real decoder obstruction. Classical integer/state-coding and
Euclidean-division tools, with new-to-SUCC source-specific integration.

OPEN: for the ACTUAL zero-initial sequence A_n, bound selected real-cell
collisions or the signed temporal sums at all required horizons. A useful
new integer-theoretic inequality should constrain (8), or the selected carry
cocycle (6)-(7), without assuming its own uniformity. This is where a proof
of normality would advance, and it is no longer confused with choosing the
correct ambient mathematical carrier.

## Validation and sources

Local isolated Python3.13.5: 15 new exact/adversarial tests passed. Original
four-pole Fraction recurrence independently checked through n=512, source
normal-form arithmetic through1024; all phase histories through256 recovered;
128 source-only hexadecimal digits independently certified with Machin's
arctangent intervals, not copied digits. Exact integer collision checks on
p=17,41,97,257 agree with an independent Fraction all-pairs oracle; p97 returns
240 ordered close pairs at M16, reproducing the inherited 80/27 scaled count.

Network cloning failed (GitHub DNS unavailable in local container); therefore
NO local full repository checkout, full-suite, archive, or Lean success is
claimed. The dedicated hosted workflow runs required provenance/observer/
ordinal gates; inspect the actual final SHA and CI, not this planning text.
Receipt: INTEGER_BBP_FINITE_RECEIPT.json. Existing archives untouched.

Primary references and declared predecessor sources:
- J. C. Lagarias, *On the Normality of Arithmetical Constants* (2001),
  https://arxiv.org/abs/math/0101055 — single-source orbit correspondence;
  representations by themselves do not establish normality.
- J. Gibbons, *Unbounded Spigot Algorithms for the Digits of Pi* (2006),
  https://www.cs.ox.ac.uk/publications/publication1674-abstract.html — classical
  streaming integer-state generation, distinct from proving distribution.
- SUCC #270, #272, #277, #278, #279 at the exact pins in section0.
- In-main BBP source repair and collision entropy proofs, source main pin above.
