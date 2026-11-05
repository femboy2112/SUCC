# Pressure growth, entropy, and adversarial completions

**Status:** paper derivations submitted for independent review. No unconditional
BBP occupancy or signed-cancellation bound is asserted. The entropy tools are
classical; no global novelty claim is made. Additive child of #518 at
`749931f0f357c60ef4e21879d96b0306999f428f`.

## R-01. Every non-Haar invariant measure has exponential pressure growth

Let b>=2, T(x)=bx mod1 on the circle, and let mu be a T-invariant Borel
probability. Use canonical half-open radix cells I_{m,w}. Put

    p_m(w)=mu(I_{m,w}), H_m=-sum_w p_m(w) log p_m(w),
    D_m=m log b-H_m, P_m=b^m sum_w p_m(w)^2,

with 0 log0=0 and natural logarithms. For every pair of positive integers m,k,

    log P_m >= D_m >= floor(m/k) D_k.                 (R1)

**Proof.** The canonical digit map d_j(x)=floor(b T^(j-1)x) is measurable and
its first m digits label exactly I_{m,w}, including terminating expansions and
0 on the circle. T-invariance makes the digit process stationary. For two
adjacent blocks X,Y, nonnegativity of relative entropy to the product marginal
implies H(X,Y)<=H(X)+H(Y). Nonnegativity itself follows from
log t<=t-1, applied to t=q_i/p_i for p_i>0; zero probabilities follow by limits.
Consequently H_{r+s}<=H_r+H_s. Write m=qk+r, 0<=r<k, and use
H_r<=r log b to obtain D_m>=qD_k. Finally Jensen's inequality for concave log,
with weights p_m(w), gives

    sum p_m(w) log p_m(w) <= log(sum p_m(w)^2),

so D_m<=log P_m. This proves (R1).

If mu is non-Haar, some finite cell distribution is nonuniform: otherwise the
cell probabilities agree with Haar on a generating semiring, hence mu is Haar.
For that k, strict equality conditions in finite relative entropy give D_k>0.
Thus

    liminf_{m->infinity} (log P_m)/m >= D_k/k > 0.    (R2)

Conversely Haar has P_m=1. This strengthens #518's invariant pressure divergence
to an exponential dichotomy. It uses no density or atomlessness assumption.
It is a classical entropy consequence, not an original-source inequality.

## R-02. Boundary-safe zero exponential-rate criterion for the original orbit

Let x_n={U_n}, U_0=0, U_{n+1}=16 U_n+r_o(n+1), with the original four poles.
Let mu_A=A^-1 sum_{A<=n<2A} delta_{x_n}, and define

    C_m=limsup_{A->infinity} P_{A,m} in [1,infinity].

The sufficient premise is

    g := liminf_{m->infinity} (log C_m)/m = 0.       (R3, OPEN)

Then mu_A converges weakly to Haar and pi is normal in base16.

**Source and dynamical steps.** The original source bound from #518 is
0<r_o(n)<=c/n^2 for n>=2, c=1920/2457. For any circle Lipschitz f and A>=1,

    |mu_A(f o T)-mu_A(f)|
       <= 2||f||_infinity/A + c Lip(f)/A^2.         (R4)

Indeed replace f(T x_n) by f(x_{n+1}), costing at most
Lip(f) sum_{n=A}^{2A-1}r_o(n+1)/A<=c Lip(f)/A^2, then telescope the two
endpoints. Hence every weak limit mu of mu_A is T-invariant. This part is
seed-uniform and is not a selection argument.

**Boundary step.** For any fixed m let M=16^m and choose a subsequence
mu_{A_j}->mu. Extract further so that its M cell masses a_{j,w} converge to a_w.
For each I_w choose an open neighborhood O_w containing its closure and lying
inside the union of cells w-1,w,w+1 (cyclic indices). Portmanteau gives

    mu(I_w)<=mu(O_w)<=liminf_j mu_{A_j}(O_w)
             <=a_{w-1}+a_w+a_{w+1}.

This remains true when mu charges endpoints. Cauchy-Schwarz followed by summing
w yields

    P_m(mu)<=9 M sum_w a_w^2<=9 C_m.                (R5)

If C_m is infinite the statement is automatic. If mu were non-Haar, R1 would
give, for some k with D_k(mu)>0,

    log(9 C_m)>=floor(m/k)D_k(mu) for every m.

Taking the lower exponential rate contradicts R3. Every weak limit is therefore
Haar, and compactness proves convergence of the full epoch sequence.

**Epoch to prefix.** For a continuous f with Haar mean zero, convergence of
A^-1 sum_{A<=n<2A}f(x_n) to zero implies prefix convergence. To see this without
assuming only dyadic endpoints, recursively set N_0=N, N_{j+1}=floor(N_j/2).
The interval [N_{j+1},N_j) is an exact doubling epoch plus at most one point.
For fixed large B, all epochs with N_{j+1}>=B have relative error at most epsilon;
the remaining prefix has at most 2B points, and O(log N) endpoint errors have
normalized size tending to zero. Let N->infinity, then epsilon->0.

Finally U_n=16^n(pi/16)-T_n, with authentic positive T_n->0; uniform continuity
transfers prefix distribution to the multiplication orbit. This gives normality.

**What was reduced.** Unlike #518's one constant C for every depth, R3 allows
unbounded envelopes, e.g. exp(sqrt(m)), and even only a cofinal sequence of good
depths. This is genuinely weaker as an envelope hypothesis. Under the already
proved asymptotic invariance both criteria are equivalent to normality. No
original arithmetic upper bound on C_m has been obtained here.

## R-03. Quantitative Fourier obstruction from any positive pressure rate

For any invariant weak limit mu and finite g from R3,

    D_k(mu)<=k g.

The finite Pinsker inequality gives ||p_k-u_k||_1<=sqrt(2D_k). For completeness,
let A={w:p_w>=u_w}, a=u(A), t=p(A)-a. The log-sum inequality reduces relative
entropy to the Bernoulli relative entropy at masses a+t and a. As a function of
t its second derivative is 1/(a+t)+1/(1-a-t)>=4, and its value and derivative
at 0 vanish. Hence D_k>=2t^2=||p_k-u_k||_1^2/2; degenerate cases follow by limits.

For any nonzero integer h and k with 16^k>|h|, the uniform discrete character
sum over the 16^k left endpoints is exactly zero. Approximating e(hx) by its
left-endpoint value costs at most 2 pi |h|16^-k. Therefore

    |mu_hat(h)|<=2 pi |h|16^-k + sqrt(2 k g).        (R6)

For g=0, letting k grow proves each nontrivial Fourier coefficient zero. This
is an alternate direct discriminator; an unknown g has not been estimated by
using this formula. It supplies no critical-frequency maximal-subinterval bound.

## R-04. Arbitrarily weak exponential pressure is compatible with non-Haar

Take independent base16 digits with probabilities
p_0=1/16+epsilon, p_1=1/16-epsilon, p_2=...=p_15=1/16,
where 0<epsilon<1/16. Their circle measure nu_epsilon is T-invariant,
atomless (cylinder masses at most p_max^m->0), and full support. It is non-Haar
because its first digit is biased. Exact product factorization gives

    P_m(nu_epsilon)=(16 sum_j p_j^2)^m=(1+32 epsilon^2)^m. (R7)

Thus no positive universal tolerance for g can replace zero in R3. The
preregistered epsilon=1/128 gives P_m=(513/512)^m. This is an exact theorem,
not a fitted growth curve.

Uniform one-digit marginals do not repair the gap. The stationary Markov chain
with uniform marginal and transition

    Q(i,j)=(1-eta)/16+eta 1_{i=j}, 0<eta<1,

has P_1=1 but P_m=(1+15 eta^2)^(m-1). It is full support, atomless, invariant
and non-Haar. The choice eta=1/3 gives (8/3)^(m-1).

## R-05. A positive absolutely continuous component does not force Haar

For 0<theta<1, mu_theta=(1-theta)lambda+theta delta_0 is invariant, full support,
and has a positive absolutely continuous component. It is not Haar, and

    P_m(mu_theta)=1+theta^2(16^m-1).                 (R8)

More strongly, replacing delta_0 by the full-support atomless measure in R-04
gives an atomless, full-support invariant non-Haar measure with a positive Haar
component. Its pressure is

    1+theta^2(P_m(nu_epsilon)-1).                    (R9)

So even the conjunction of all three weak regularity observations fails.
One needs pure absolute continuity, maximal entropy, zero pressure growth, or
another condition actually excluding the singular remainder. No assertion is
made that these arbitrary invariant measures occur for the literal zero seed.

## R-06. Nearby aperiodic non-Haar completions with small irrationality exponent

Use nu from R-04 with epsilon=1/128, and set
s=log(128/9)/log16. Since (9/128)^3<16^-2, s>2/3. Any interval I of length
delta<=1 intersects at most two cells of length 16^-m when
16^{-(m+1)}<delta<=16^-m. Therefore

    nu(I)<=2(9/128)^m<=2*16^s delta^s.               (R10)

For each v>2/s, cover all approximations |x-a/q|<q^-v in [0,1] by at most
q+3 intervals of length 2q^-v. The sum of their nu masses over q is bounded
by a constant times sum q^(1-vs), which converges. Borel-Cantelli shows that
for nu-almost every beta, only finitely many such approximations occur.
Intersect over rational v>2/s: the irrationality exponent of beta is at most
2/s<3. In particular these beta are irrational.

For each digit word w, its nonoverlapping occurrences in each residue class
modulo its length are independent, identically distributed bounded variables.
The strong law, followed by the finite residue-class union and then a countable
intersection over words, shows that nu-almost every beta has chronological
radix empirical limit nu. These generic beta are nonnormal. Because nu has
full support, every nonempty interval contains beta satisfying BOTH this
genericity and the irrationality-exponent bound.

Let alpha=pi/16 and choose such beta arbitrarily close to alpha. With the
ORIGINAL four-pole forcing and seed s_beta=beta-alpha, exact completion gives

    U_n(s_beta)=16^n beta-T_n.

The Green tail tends to zero, so its empirical circle measure is nu. Thus
same-forcing seeds arbitrarily close to zero can produce aperiodic, atomless,
full-support, non-Haar limits, while their completed constants have irrationality
exponent below 3. These controls defeat a strategy based only on four-pole
forcing, asymptotic invariance, absence of finite attractors, weak regularity,
and a finite Diophantine exponent. They do not refute the literal zero-seed
claim: no argument places alpha in this generic nonnormal set. They also do
not preserve exact rationality of every unwrapped U_n, so exact zero-selected
numerator/carry arithmetic remains a legitimate untested discriminator.

## R-07. Exact rational-seed phase symmetry

The recurrence gives U_n(1/5)-U_n(0)=16^n/5. Since 16=1 mod5,

    e(h U_n(1/5))=e(h/5)e(h U_n(0))                 (R11)

for every integer h and n. Every sharp or smooth weighted character sum has
identical magnitude under this seed change; pair phase differences and Fekete
energies are identical. Haar distribution is preserved by the fixed circle
rotation 1/5. Thus a successful normality argument need not distinguish every
wrong seed, and a character-magnitude discriminator cannot authenticate zero.
This control is coherent with, rather than hostile to, normality equivalence.

## R-08. The envelope relaxation is strict before invariance is imposed

The circle probability with density f(x)=1/(2 sqrt(x)), 0<x<1, is integrable
but not square-integrable. With M=b^m its pressure is exactly

    P_m=sum_{w=0}^{M-1}(sqrt(w+1)-sqrt(w))^2.

For w>=1 the summand is between 1/[4(w+1)] and 1/(4w), so
P_m=(log M)/4+O(1). It is unbounded and has zero exponential rate.
This measure is not invariant. It witnesses strict weakness of the pressure
envelope hypothesis in the ambient measure space; it is not a counterexample
to the invariant dichotomy and is not asserted to be an empirical BBP limit.
