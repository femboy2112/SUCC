# Completion debt for arithmetic source transports

Status: paper proofs below; exact finite controls in `test_round2_completion.py`.
No functional-analytic statement in this file has Lean authority. RH PROVED: NO.
This continues INS-05--08 at source commit
`e42096ec0186228dd0f748767599e470f2ca2e1d`; the previous paper and its failures
remain unchanged. Academic priority is unestablished. The results use classical
Haar scaling, Hilbert duality, Bessel synthesis and distribution transposition.

## 1. Objects and finite vacuum cost (COST-01)

Let H_d=ell²(N>=1), H_c=L²(Zhat,m), with normalized additive Haar m.
V_p e_n=e_(pn) and U_p f(x)=sqrt(p)1_(p Zhat)(x)f(x/p).
For a finite set of genuine primes F, put
E_F={x:p does not divide x for every p in F},
alpha_F=product_(p in F)(1-1/p), and v_F=1_(E_F)/sqrt(alpha_F).
CRT gives m(E_F)=alpha_F>0. If F is a subset of G, then

    <v_F,v_G> = sqrt(alpha_G/alpha_F),
    ||v_F-v_G||² = 2(1-sqrt(alpha_G/alpha_F)).                 (1)

Indeed E_F intersect E_G=E_G; integrate the two real indicators, then use
unit norms. For general F,G the overlap is
alpha_(F union G)/sqrt(alpha_F alpha_G). Thus nestedness matters.
Along increasing finite sets exhausting a prime set S, these canonical
vacua are Cauchy iff sum_(p in S)1/p is finite. In that case their norm limit
is 1_(E_S)/sqrt(alpha_S), by dominated convergence. Otherwise alpha_F tends
to zero, and after any F one can choose G with alpha_G/alpha_F<=1/4,
so the squared distance is at least 1. In this divergent case v_F nevertheless converges
weakly to zero: for f in L², |<f,v_F>|<=||1_(E_F)f||₂, which tends to zero.
The Euler-product equivalence follows from
1/p <= -log(1-1/p) <= 2/p for p>=2.

## 2. Every finite-prime unitary escapes weakly (COST-02)

**Theorem.** Let F_k be finite prime sets such that each prime eventually
belongs to every F_k. For each k let W_k:H_d -> H_c be ANY unitary satisfying
W_k V_p=U_p W_k for p in F_k. Then W_k -> 0 in the weak operator topology,
and W_k* -> 0 weakly. Neither sequence converges strongly to zero.
The same conclusion holds for any exhausted S with sum_(p in S)1/p=infinity.

**Proof.** Unitarity upgrades the forward identity to W_k V_p*=U_p*W_k.
For fixed m, V_p*e_m=0 when p does not divide m. Since
U_p*f(x)=p^(-1/2)f(px), ker U_p* consists exactly of functions vanishing
almost everywhere on p Zhat. Thus W_k e_m is supported in
E_(F_k minus {p:p divides m}). For any finite P subset of S avoiding m,
this support eventually lies in E_P. Its measure is at most alpha_P,
which can be made arbitrarily small. Absolute continuity of the L² integral
therefore gives, for each f in H_c,

    |<W_k e_m,f>| <= ||1_(E_(F_k minus divisors(m))) f||₂ -> 0. (2)

Finite linear combinations of e_m are dense; ||W_k||=1 permits approximation
of any fixed source vector. This proves WOT convergence. Adjoint matrix
coefficients give the reverse conclusion. Strong convergence to zero would
contradict ||W_k e_m||=1; any strong limit would also be the weak limit zero.
No compatibility or canonical choice of the W_k is assumed. Existence for
finite F is the explicitly constructed wandering-space unitary of INS-06.

The word 'exhausting' here means **eventual inclusion**, not merely union.
Taking F_(2k)={2} with the same nonzero W on that subsequence, and F_(2k+1)
increasing to all primes, refutes the union-only version.

**Uniformly bounded forward repair.** More generally let sup_k||T_k||<infinity
and let T_k V_p-U_p T_k ->0 in WOT for every fixed p. Then T_k->0 in WOT,
using the forward-only obstruction proved in [the operator paper](ROUND2_OPERATORS.md).
Every WOT cluster point in the weak-operator compact bounded ball intertwines
all primes, hence is zero. Compactness follows by weak-* compactness of
bounded operators (or by diagonal extraction of matrix coefficients in these
separable spaces); uniqueness of the cluster point implies convergence.
The reverse-direction assertion is identical. This is a conditional deduction
from FWD-01/02, not a replacement proof of those theorems. Dropping a uniform
bound invalidates this compactness argument.

## 3. The missing datum in positive finite representations

**Bessel completion criterion (classical).** Given vectors h_n in a fixed
Hilbert space H, the consistent synthesis J_0 e_n=h_n on c00 extends to a
bounded operator ell² -> H with norm at most C iff EVERY finite Gram matrix
G_I=(<h_m,h_n>)_(m,n in I) obeys G_I <= C² I. Its norm squared is exactly
the supremum of the finite Gram norms.

Proof: the inequality is exactly ||sum a_n h_n||²<=C² sum|a_n|² on c00.
Continuity and completeness uniquely extend it; restriction proves necessity.
Consistency of columns, fixed target topology, and a uniform upper bound are
all explicit hypotheses. Positivity G_I>=0 alone provides none of the upper
bound. It can construct an abstract Gram Hilbert space, whose norm need not
be the source ell² norm. COST-03 in the operator paper gives a genuine
arithmetic counterexample: h_n=U_n1 has positive finite Grams and unbounded
synthesis norms. This is a source metric mismatch, not negative energy.

## 4. Sharp regularity of the Dirac interface (COST-04)

Let D(Zhat) be the locally constant complex functions, with the inductive-limit
topology of finite-dimensional spaces of functions modulo k!.
Let D' have the weak topology sigma(D',D). All test functions are bounded;
1 is a permitted test. Measures embed in D', without identifying measures
with Haar L² functions. Suppose 0<w_n<infinity for every n and equip
ell²(w) with ||a||_w²=sum w_n|a_n|². Define J_0e_n=n^(-1/2)delta_n.
Here different positive integers are distinct points of Zhat.

**Theorem.** The following are equivalent:

1. J_0 extends to a continuous linear map ell²(w)->weak D'.
2. C_w²:=sum_(n>=1)1/(n w_n)<infinity.
3. J_0 extends to a bounded map ell²(w)->M(Zhat), with the total-variation norm.

The extension is unique, given by the absolutely convergent atomic measure

    Ja = sum a_n/sqrt(n) delta_n,
    ||Ja||_TV = sum |a_n|/sqrt(n) <= C_w ||a||_w,
    ||J||_(ell²(w)->TV) = C_w.                               (3)

**Proof.** (1) implies continuity of a -> <Ja,1>. Hilbert duality gives the
necessary square-sum condition. Explicitly, on indices n<=N choose
b_n=1/(sqrt(n) w_n). Then ||b||_w²=C_(w,N)² and <Jb,1>=C_(w,N)²,
so any bound on this one scalar functional dominates every C_(w,N).
For (2)->(3), Cauchy--Schwarz proves absolute convergence and the upper bound.
The atoms are distinct; countable additivity of variation makes the displayed
TV sum exact, even though the support can be dense. Truncating b proves that
the operator norm is exactly C_w. When C_w is finite the infinite b/C_w
itself attains this norm. (3)->(1) follows from
|<Ja,phi>|<=||phi||_infinity ||Ja||_TV. Density of c00 and the Hausdorff
weak topology prove uniqueness. If the sum diverges, a^(N)=b/C_(w,N)² has
norm 1/C_(w,N)->0 but <J a^(N),1>=1: a direct continuity counterexample.

Consequently w_n=n^s works **iff s>0**. The logarithmic weight
w_n=(log(n+1))^beta works **iff beta>1**. The latter follows from the
integral test for 1/[x(log x)^beta], with n+1 replacing n only by bounded
ratios for n>=2. The borderline beta=1 diverges. These are universal proofs;
finite partial sums cannot certify convergence.

## 5. Action and adjoint obligations on the repaired domain

Write B_p e_n=1_(p divides n)e_(n/p) for the **original algebraic backward
shift**, which is the unweighted adjoint V_p*. On ell²(w),

    ||V_p||² = sup_n w_(pn)/w_n,
    ||B_p||² = sup_n w_n/w_(pn),                              (4)

with infinity meaning no bounded extension of that action. Both statements
follow by the change of index and are sharp on basis vectors. Summability
in (3) alone does NOT imply (4): choose w_n=n² for odd n and n⁴ for even n.
The sum in (3) converges, but w_(2n)/w_n=16n² for odd n, so V_2 is unbounded.
This refutes the proposed silent source-action repair.

For w_n=n^s, the exact norms are p^(s/2) and p^(-s/2). For logarithmic
weights beta>1, 1<=log(pn+1)/log(n+1)<=1+log(p)/log(2), so both actions
are bounded (||B_p||=1 by n->infinity). Constants may depend on p; no
uniform-in-prime bound is claimed.

On D' define the continuous transpose actions

    (D_p nu)(phi)=nu(U_p*phi)=p^(-1/2)nu(phi(p·)),
    (A_p nu)(phi)=nu(U_p phi)=sqrt(p)nu(1_(p Zhat)phi(·/p)).     (5)

Both tests remain locally constant. On measures ||D_p||=p^(-1/2) and
||A_p||=sqrt(p). If the appropriate ratio in (4) is finite, density extends
J V_p=D_p J and J B_p=A_p J from c00 to all ell²(w).
The Hilbert adjoint in ell²(w) is instead
V_p^(dagger,w)e_(pn)=(w_(pn)/w_n)e_n. For n^s with s>0 it equals p^s B_p;
therefore this interface does **not** intertwine the weighted Hilbert adjoint
with A_p. The test transposes are not Hilbert adjoints on D'. The repaired
map is a bounded injective map to measures, not a Hilbert star-equivalence.

## 6. Controls, prior art, and remaining obligations

The exact tests independently count CRT residue intersections; use rational
squared overlaps and variation/norm extremizers; distinguish nonnested sets;
check the unweighted divergence witness, action-ratio spikes, transpose
identities on residue tests, and weighted-adjoint mismatch. The operator
paper supplies separate GCD Gram controls. No finite observation is used to
prove an infinite limit or summability threshold.

Primary background: François Bruhat, *Distributions sur un groupe localement
compact...*, Bull. SMF 89 (1961), 43--75,
[original article](https://www.numdam.org/articles/10.24033/bsmf.1559/),
for the locally compact distribution framework. We use only the explicitly
defined compact totally disconnected test space above. The bounded synthesis/
Gram equivalence belongs to classical frame theory; see Balazs, Stoeva and
Antoine, *Classification of General Sequences by Frame-Related Operators*,
[arXiv:1009.1496](https://arxiv.org/abs/1009.1496). The proofs here are complete
specializations, not claims of priority over those sources.

New to this SUCC branch: arbitrary-choice finite-prime unitary WOT escape,
exact weighted-Dirac iff criterion and norm, and action-domain counterexample.
Potential academic originality of their joint arithmetic formulation remains
unverified. The next discriminating probes are exact prior-art comparison,
a measure-theoretic Lean formalization, and sharp quantitative WOT decay for
specified Fourier tests (there is no choice-independent norm decay).
