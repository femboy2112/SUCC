# Positive histories, entropy and the operator boundary

Date: 2026-10-24. Pinned parent: #272 at
6e8fa8b77886b13f1f533ed8083fd88c849d14b3.
Authority: paper proofs and identified classical inputs. These reductions
do not establish an authentic-source asymptotic estimate or pi normality.

## 1. Positive history stationarity: an exact equivalence

Let U be a bounded linear operator on a complex Banach space with ||U|| <= 1.
Let P(z)=sum_{j=0}^J p_j z^j, where p_j >= 0, sum p_j=1, and at least one
positive j has p_j>0. Put

    d = gcd{ j >= 1 : p_j > 0 }.

Then

    ker(I-P(U)) = ker(I-U^d).

The zero-length history is allowed. The identity-only mixture is excluded.

**Proof.** Write P(z)=R(z^d). The positive supported exponents of R have gcd
one. For |w|<1, |R(w)|<1. For |w|=1, equality R(w)=1 forces w^k=1 for every
positive supported k: equality in the triangle inequality forces every
supported term to be 1. Thus w=1. Consequently

    Q(w) = (1-R(w))/(1-w)

has no zero on the closed unit disk; its value at 1 is R'(1)>0. The reciprocal
1/Q has a power series with radius of convergence greater than one. Its
absolutely summable coefficients define the bounded inverse of Q(U^d).
Factor

    I-P(U) = (I-U^d) Q(U^d)

and use commutation and invertibility. This proves equality of the kernels.

For finite signed measures in total variation, U=(T_3)_* is a contraction.
Hence a probability law satisfying P(U)mu=mu satisfies (T_{3^d})_*mu=mu.
If d=1, this is precisely same-law tripling. If d>1, it is still adequate
for the rigidity route: 16 and 3^d are multiplicatively independent.

### Weak approximate version

For a **fixed** P as above and any sequence of circle probabilities mu_n,

    mu_n - P((T_3)_*) mu_n -> 0 weakly

if and only if

    mu_n - (T_{3^d})_* mu_n -> 0 weakly.

For the forward implication, take any weakly convergent subsequence of the
compact space of circle probabilities. Continuity of T_3 passes the assumed
identity to the limit. Apply the exact theorem. Every subsequential limit of
the second defect is zero. The reverse implication follows by finitely
telescoping R(U^d)-I. Wasserstein-1 also metrizes this convergence on the
compact circle. The total-variation inverse above is not automatically a
Lipschitz-norm inverse, so this argument asserts no linear W1 bound.

**Consequence for the proposed histories.** At a radix-invariant limiting
law, a positive finite random mixture of words in T_16 and T_3 reduces to a
polynomial in T_3, since the maps commute and T_16 already preserves the law.
For d=1 this is exactly same-law tripling. For d>1 it is the weaker
T_(3^d)-invariance condition, which still suffices for the rigidity route
when the same positive all-scale collision premise is supplied.

### Sharp controls

1. **Signed weights.** Let U=(T_3)_* and order the denominator-5 cycle as
   (1/5,3/5,4/5,2/5). Assign weights (3/8,1/8,3/8,1/8). Then
   T_16*mu=mu, U^2 mu=mu, and U mu != mu. Nevertheless

       (U+U^2-U^3) mu = mu.

   The supported lengths have gcd one. The final output is a positive
   probability; that alone does not restore the missing positive-coefficient
   hypothesis. Its total-variation tripling defect is exactly 1/2.

2. **Varying weights.** For P_n(z)=1-epsilon_n+epsilon_n z and
   epsilon_n -> 0, the P_n-stationarity defect vanishes for every fixed mu,
   even when its U-invariance defect is 1. A fixed nontrivial mixture, or an
   appropriate uniform nondegeneracy condition, is essential.

3. **Gcd.** The same denominator-5 alternating law is stationary for
   (U^2+U^4)/2 and under U^2, but not under U. A gcd-one conclusion would be
   wrong. Radix-16 plus U^2 is nevertheless enough for the cited rigidity
   theorem once positive all-scale dimension is proved.

## 2. Host gives Haar after observer averaging, not source preservation

**Primary source.** Michael Hochman, *A short proof of Host's equidistribution
theorem*, arXiv:2103.08938v2, Theorem 1.1, dated 26 June 2023:

https://arxiv.org/html/2103.08938v2

The statement used here is Theorem 1.1.

Exact imported hypothesis/conclusion: if mu is T_a-invariant, T_a-ergodic,
and has positive T_a-entropy, then mu-almost every point is Haar-generic
under T_b whenever a,b are multiplicatively independent. The pair 16,3 also
meets Host's original relatively-prime hypothesis. No T_3-invariance of mu
is assumed in this theorem.

### Corollary for the repository's collision premise

Suppose mu is T_16-invariant and, for some s>0 and finite C,

    Q_mu(rho) = (mu x mu){(x,y): dist(x,y)<=rho} <= C rho^s

for all sufficiently small rho. Then

    (1/K) sum_{j=0}^{K-1} (T_{3^j})_* mu -> Haar weakly.

This statement does not require mu itself to be T_3-invariant.

**Proof of the nonergodic step.** For the radix-16 partition P_k,

    sum_{I in P_k} nu(I)^2 <= Q_nu(16^{-k}).

The Shannon entropy dominates collision entropy, so a collision exponent s
gives h_nu(T_16)>=s log 16 for every invariant nu with that bound.
Decompose mu into T_16-ergodic components. For any positive-mass measurable
set E of component labels, with decomposition mass c>0, its normalized
mixture nu_E satisfies nu_E<=mu/c. Thus

    Q_nu_E(rho) <= Q_mu(rho)/c^2 <= (C/c^2) rho^s,

and h_nu_E(T_16)>=s log16. Entropy is affine over the ergodic decomposition.
If a positive set of components had entropy below s log16, some positive
subset would be bounded below that threshold by a fixed amount, contradicting
the preceding inequality. Thus almost every component has entropy at least
s log16>0. Apply Host componentwise. For every continuous f,

    (1/K) sum_j f(T_{3^j} x) -> integral f dHaar

for mu-almost every x. Integration and bounded convergence give the claimed
averaged-law convergence.

**Decisive countermodel.** The base-16 Bernoulli measure with independent
equiprobable digits 0 and 1 has entropy log2, a positive collision exponent
log2/log16=1/4, and support inside [0,1/15]. It is not Haar. Its tripling
history averages nevertheless converge to Haar by the corollary. Its
tripling image assigns at least half the mass outside [0,1/15], because the
first digit 1 forces x>=1/16 and therefore 3x>1/15. Thus preserving mu is a
substantial extra demand.

The stronger observer ensemble can become Haar while the original radix
law remains singular. Almost-everywhere conclusions also do not designate
the authentic source point pi as typical for an auxiliary law.

## 3. Audit of the existing Rudolph–Johnson closure

**Primary source.** Bourgain, Lindenstrauss, Michel and Venkatesh, *Some
effective results for x a x b*, Theorem 1.3:

https://math.stanford.edu/~akshay/research/blmv.pdf

The theorem states:
jointly invariant mu with h_mu(T_a)=eta log a dominates eta times Haar, for
multiplicatively independent a,b. This version needs no ergodicity premise.

The proof in `PI_BASE_THREE_RIGIDITY.md` is valid: positive collision exponent
gives entropy; subtract a fixed positive Haar component; the normalized
residual remains invariant and inherits the same collision exponent with a
larger constant. Iterate to exhaust the mass. The same argument works with
3^d in place of 3. A mixed law with merely positive entropy does not by itself
force full Haar; the persistent all-scale collision exponent pays that debt.

The BLMV introduction also recalls Furstenberg's density theorem. Since pi
is irrational, {16^n 3^m pi mod 1 : n,m>=0} is already dense. This is a
classical unconditional statement about the range of the enlarged observer
family. It assigns no frequencies and does not prove normality of its
single row m=0.

## 4. Unique source versus compact unique ergodicity

Let X be compact metric, S:X->X continuous, and pi_X:X->circle continuous
with pi_X S=T_16 pi_X. If pi_X is onto, (X,S) is not uniquely ergodic.

**Short proof.** The circle points 0 and 1/15 are distinct fixed points of
T_16. Their nonempty compact fibers are S-invariant. Cesaro orbit measures
in each fiber have invariant subsequential limits. These two limits project
to different Dirac measures and are therefore different invariant measures.
In fact the 15 fixed points give at least 15 invariant measures upstairs.

If one orbit upstairs projects to a normal radix-16 orbit, then its projected
orbit is dense. The compact image pi_X(X) contains its closure, so pi_X is
onto and the obstruction applies. Thus a compact continuous uniquely
ergodic extension cannot be the mechanism proving a normal projected orbit.

This does not prohibit a selected point from being Haar-generic in a system
having many invariant measures. Nor does it prohibit a noncompact,
nonautonomous, or discontinuously projected construction. Such alternatives
must explicitly supply the missing genericity theorem. The exact BBP clock
must be accounted for before calling a history space an autonomous extension.

## 5. A global L2 telescoping route is obstructed exactly

Fix an integer b>=2 and integer frequencies m and h, with h!=0 when used
below. Let U_b f(x)=f(bx mod1) on L2(Haar). Let e_m(x)=exp(2 pi i m x). Decompose
nonzero frequencies into chains {ell b^k:k>=0}, where b does not divide ell.

**Fourier-chain classification.** A finite trigonometric polynomial
f=sum_m a_m e_m has an L2 solution to f=(I-U_b)g if and only if a_0=0 and

    sum_{k>=0} a_{ell b^k}=0 for every chain ell.

When these conditions hold, g can itself be a finite trigonometric polynomial.

**Proof.** Along a chain, write c_k=ghat(ell b^k). The coefficient equations
are c_0=a_ell and c_k-c_{k-1}=a_{ell b^k}. Therefore

    c_k=sum_{j=0}^k a_{ell b^j}.

Because f has finite support, this is eventually the constant chain sum.
Square summability forces that constant to vanish. Conversely, zero chain
sums make these coefficients finitely supported. The constant Fourier
coefficient of a coboundary is zero; g's constant remains arbitrary.

For h!=0 and integer q>=1, e_{qh}-e_h is such a coboundary precisely when
q is a nonnegative integer power of b. In particular the tripling defect
e_{3h}-e_h is not an L2 radix-16 coboundary. The finite formal inverse

    g_K=sum_{j=0}^{K-1} U_16^j(e_{3h}-e_h)

satisfies ||g_K||_2^2=2K, while

    (I-U_16)g_K=(e_{3h}-e_h)-U_16^K(e_{3h}-e_h).

The terminal term has fixed L2 norm sqrt2. Sending K to infinity does not
make this a convergent transfer function.

More generally, for any nontrivial finite positive tripling-history mixture,

    f_P=sum_j p_j e_{3^j h}-e_h

occupies distinct radix-16 chains. It has no L2 transfer function. The formal
inverse has squared norm

    K ((1-p_0)^2 + sum_{j>=1} p_j^2).

This obstruction is to a global Haar-regular circle transfer function, not
to an authentic-source-specific arithmetic construction. Even an arbitrary
L2 identity would hold only almost everywhere and would not automatically
cover pi; here the nonexistence is stronger.

The repository already contains the separate point-evaluation norm barrier
in `CYCLOTOMIC_SELECTION_RESOURCES.md` SOR01-SOR03 and the selected-source
claim supplement CSS08. That theorem is inherited, rather than a new contribution of this dossier.


See [the quantitative preservation theorem](PI_HISTORY_PRESERVATION.md),
[the exact claim supplement](../../docs/CLAIM_SUPPLEMENT_SOURCE_PATH_SELECTION.md),
and [validation](PI_PATH_SELECTION_VALIDATION.md).
