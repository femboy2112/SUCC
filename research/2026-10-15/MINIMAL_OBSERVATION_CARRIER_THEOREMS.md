# Minimum sufficient observations: exact theorems and bounded compilers

Operation Proof Teeth, 2026-10-15. Source parent: SUCC `0f86ba2478a72bf90cf33a4ee192cb2265d992dd`;
YEAN `f58cdf5147e96148aa82481c0a37ea53d21247cf`. Status: PAPER_PROVED below,
with separately labeled EXACT_FINITE_CHECK implementations. These are classical
quotient/periodicity/Newton arguments and new-to-SUCC integrations, not claims of
academic priority. No mathematical theorem in this file is promoted to Lean
merely because its finite compiler runs. RH PROVED: NO.

## PT-C01: the correct factorization type and the executable compiler

For sets S,A,B and maps O:S→A, h:S→B, put s~t iff O(s)=O(t).
There exists a unique decoder on Coim(O)=S/~ with d([s])=h(s) iff
∀s,t, O(s)=O(t) ⇒ h(s)=h(t). Necessity follows by substitution;
sufficiency defines d([s])=h(s), which is well-defined by exactly that
hypothesis; uniqueness follows because every class has a representative.
This is the existing `Yean.MemeSufficientArtifact.factor_iff/factor_unique`,
not a new theorem. Its quotient construction does not choose arbitrary
representatives or invent outputs on unreachable artifacts.

**Type correction:** a total decoder on all A additionally needs an extension
outside im(O). If B is inhabited, one fixed b∈B supplies it; if O is onto,
there is nothing to extend. Without either, the user-facing unrestricted
formula has a degenerate counterexample: S=B=∅, A={*}. Fiber constancy is
vacuous but no map A→B exists. The compiler therefore certifies only reachable
artifacts, including the empty coimage, and refuses queries elsewhere.

`FiniteObservation` declares S=Fin(N) with the WHOLE observation/target table,
source identity, epoch, laws, proof theory and cost model. It is not a sample
from a larger source. `compile_factorization` reuses `OriginalSourceSquare`;
`replay_factorization` independently checks the full commuting square and
pairwise fibers. Successful output contains a decoder; failure contains two
indices with the same observation and unequal targets. Its digest binds the
source, epoch, laws and both tables. Digests are integrity evidence, not physical
authentication. The decoder accepts only an artifact, never a hidden source.

`minimum_in_menu` orders observations by refinement: O≼R iff equal R-values
force equal O-values. It returns every least sufficient observation *in that
finite menu*. Several equivalent minima are allowed. Incomparable minima or
an insufficient menu yield UNRESOLVED_MINIMUM_IN_MENU unless the JOINT readout
has a target collision. Only the latter proves a toolkit obstruction for all
deterministic functions of that joint readout (including adaptive rereads).
It does not declare an impossible target merely because no individual probe
suffices. Adding h to O is the abstract coarsest sufficient refinement from
YEAN; it is executable only if h itself is an authorized available probe.

## PT-C02: chi4 has exactly the required residue moduli

Define χ4 on every integer by the existing table (0,1,0,-1) at x mod 4.
For every integer n≥1,

    χ4 factors through Z→Z/nZ  iff  4 divides n.

If 4|n, x≡y mod n implies x≡y mod4; decode r by the table at r mod4.
If n is odd, 0 and n have identical n-residues but values 0 and ±1.
If n≡2 mod4, 1 and 1+n have identical n-residues but values 1 and −1.
These exhaust the negative cases. Thus 4 is the least sufficient modulus
in the divisibility order, not merely the smallest tested integer.

`chi4_observation` uses `Chi4TateSource`'s source identity and epoch. The older
`character_four` evaluator restricts integers to ±10^12; the adapter calls it
only on residues 0..3, so it does not silently inherit that execution bound
as a mathematical bound on the theorem.

The local Tate comparison is exact: the ramified test is
1_(1+4Z2)−1_(3+4Z2), so its restriction to Z is χ4. The multiplicative local
character on Q2* is χ2(2^k u)=χ4(u mod4); it is **not** the zero-extended
integer character. For example χ4(2)=0 while χ2(2)=1. Conductor 4,
integer values and idele-local components are different typed objects.

## PT-C03: primitive characters and periods

For any bi-infinite c-periodic table v, the periods form a subgroup of Z.
If n and c are periods, Bezout implies gcd(n,c) is a period. Hence the least
positive period d divides c and the period set is dZ. Inspecting
v(x+n)=v(x) for 0≤x<c suffices to establish a period on ALL Z by c-periodicity;
a failed row supplies the indistinguishable pair (x,x+n).

For a primitive Dirichlet character of conductor c, its zero-extended integer
sequence has least positive period c. Here is the missing descent argument.
If d|c is a period and a prime p|c does not divide d, CRT gives x≡1 mod d,
x≡0 mod p; periodicity would give χ(x)=χ(1)=1, contradicting χ(x)=0.
Thus c and d have the same prime divisors. The d-periodic sequence therefore
vanishes exactly on nonunits modulo d, and its unit values are multiplicative.
It defines a character modulo d inducing χ, so primitivity forces d=c.
Combining this with the period subgroup argument proves factorization modulo n
iff c|n for every primitive character, including complex-valued ones.

The bounded implementation supports real characters with values −1,0,1 and
c≤128. It verifies multiplicativity, exact unit support, and non-induction
from every proper divisor by UNIT-fiber collisions. Cases c=3,4,5,8 are
exercised; their residue criterion is universal in n by the preceding proof.
Reject the tempting wrong test: the principal character mod3 has least
integer-table period 3 but conductor 1. Table period alone cannot establish
primitivity. No local Hecke component is synthesized from these tables.

## PT-C04: Newton basis, minimum observations, and the descent gate

Let d≥0, n≥2 and P:Z→Z be an integer-valued rational polynomial of degree ≤d.
The finite difference identity gives

    P(x)=sum_(j=0)^d c_j binom(x,j),  c_j=Δ^j P(0)∈Z.

Proof: binom(x,j) is integer-valued also for negative integers, satisfies
Δ binom(x,j)=binom(x,j−1), and has degree j. Induct on d, subtracting
P(0) and summing the Newton expansion for ΔP. Equivalently the evaluation
matrix at 0,..,d is lower triangular with diagonal 1, so the interpolating
polynomial agrees at d+1 points and hence identically over Q. This also proves
that all such polynomials have this representation, with unique coefficients.

Consequently the d+1 values at 0,..,d determine P modulo n at EVERY integer.
No inverse of d! modulo n is used. There are n^(d+1) distinct functions in this
family modulo n, since the same triangular matrix distinguishes their
coefficient residues. Any m fixed point probes have at most n^m output tuples,
so m≥d+1 is necessary; the same bound holds for worst-case depth m adaptive
n-ary decision trees. These are observations of a *known structural family*.
For any one removed standard observation, interpolate the Kronecker value
vector with Newton coefficients: it is invisible at the retained observations
and nonzero at the omitted one. This supplies explicit ablation witnesses.

**Descent must be proved separately.** The integer-valued polynomial
Q(x)=P(x+n)−P(x) has degree ≤d−1. By the preceding basis theorem,
P descends to Z/nZ iff Q(0),...,Q(d−1) vanish modulo n; for d=0 the condition
is empty. Positive n-periodicity gives negative shifts by substitution too.
`polynomial_descent` executes precisely these finite obligations. The witness
P(x)=binom(x,2), n=2 has P(0)=0, P(2)=1 and is REFUTED as a quotient map.
The d+1 lower bound above concerns maps on Z, not the smaller descended family.

For comparison, matrices defining homomorphisms (Z/n)^r→(Z/n)^s, r,s≥1,
are determined by r standard basis images, with each missing column an
ablation witness. There are n^(sr) such maps and each probe returns at most
n^s values, proving the r lower bound. Affine matrix maps need 0 and those r
basis vectors: n^(s(r+1)) choices give the matching r+1 lower bound. This
paragraph is PAPER_PROVED only; no separate matrix compiler is claimed.

## PT-C05: minimum arithmetic window relative to independent tape mutations

Fix a>0. The source-input class is real coefficient tapes (c_q) indexed by
GENUINE prime powers q=p^k≥2, with each coordinate independently mutable.
The observable target is the functional on ALL f∈Cc∞(−a,a;C):

    A_c(f) = −sum_q c_q [g(log q)+g(−log q)],  g=f*f~.

The canonical zeta tape has c_(p^k)=log(p)/sqrt(p^k). Mutated tapes are NOT
asserted to be other zeta functions or to satisfy Euler/logarithmic coherence.
Gamma, contact and pole terms are fixed separately. If the canonical arithmetic
law is supplied as an executable rule, its coefficients can be recomputed;
this information-theoretic minimum is for a tape-oracle mutation class, not a
universal cost lower bound on computation from the genuine zeta law.

The exact necessary coordinate set is J_a={q prime power: log q<2a}.
It is finite. Each compact support lies strictly inside (−a,a), so g vanishes
at every |x|≥2a, including endpoints. Coordinates outside J_a are invisible
for ALL allowed tests. Thus the target factors through restriction to J_a.

For necessity fix x=log q∈(0,2a). Choose ε>0 so that ε<a−x/2,
2ε is less than every positive active atom and less than every distinct
active atom's distance from x. This is possible by finiteness and positivity
of the separation distances; uniqueness of positive log prime-power labels
prevents aliases. Let η(t)=exp(−1/(1−(t/ε)^2)) for |t|<ε and 0 elsewhere.
Then η is a nonzero real even Cc∞ bump. Put f(t)=η(t+x/2)+η(t−x/2).
Its support lies in (−a,a). If c=η*η~, then

    g(s)=2c(s)+c(s−x)+c(s+x),   supp(c)⊂[−2ε,2ε].

Hence g(x)=g(−x)=c(0)=||η||²>0, while g vanishes at all other active
±log atoms. A change δ≠0 in the q coordinate alone changes the target by
−2δ||η||². On |t|≤ε/2 we have η(t)^2≥exp(−8/3)>1/27 using e<3;
thus the absolute change is strictly greater than 2|δ|ε/27. This proves
necessity even against simultaneous changes at other coordinates: this test
isolates the chosen atom. The target's observational fibers are exactly
agreement on J_a, so restriction to J_a is a coarsest sufficient statistic
up to bijection, not just coordinatewise irredundant.

`minimum_arithmetic_window` reuses `CompactWeilSourceWindow`'s conservative
q<3^ceil(2a) cutoff and refines it with rational log enclosures. It keeps
zero canonical chi4 coefficients in the tape mutation class because those
coordinates are permitted to vary. The implementation caps a≤3 and the
Taylor resource budget; comparisons that straddle an endpoint return
UNRESOLVED. It does not silently decide equality of transcendental inputs.
`autocorrelation_atom_witness` supplies rational ε and all positive isolation
margins, together with the analytic formula and the rational sensitivity bound.
These are smooth autocorrelations; the earlier standalone positive bump
negative-Weil example is a different cone and is not substituted here.

## Verification and limits

Run `python -m unittest discover -s tests -p 'test_minimal_observation.py'`
and `python scripts/minimal_observation_probe.py`. Independent tests compare
finite interpolation to direct polynomial evaluation and periodic characters
to complete cycles; mutate source epochs, decoders, omitted generators,
principal-character primitivity, coefficient tapes and normalization bounds.
Analytic bump smoothness/support and the all-integer extension are proved above,
not inferred by sampling. Source correctness (σ) stays distinct from theorem
validity; actual permitted observation contact (κ) and toolkit collisions (φ)
are explicit; favorable labels do not remove commitment/coupling risk (ρ).
