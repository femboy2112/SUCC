# Pascal transport of the authentic BBP spectral source

## Scope, provenance, and status

This is a local paper derivation extending PR #417 at
`1c6ce7d7ee83a0bd751bde8092e46ff798855fd3`, especially
`BBP_SOURCE_TWISTED_ZETA_POLE.md` and `NEXT_ZETA_GRADE_HANDOFF.md`.
The ingredients are classical geometric series, meromorphic continuation of
zeta, polylogarithms, binomial translation, and finite moment reconstruction.
No scholarly-priority claim is made. The exact source is unchanged:

\[
r_u(n)=\sum_{i=1}^4\frac{c_i}{8n-b_i+u},\quad
b=(7,4,3,2),\quad c=(4,-2,-1,-1),\quad n\ge1.
\]

At `u=0`, `U_0=0`, `U_N=16U_{N-1}+r_0(N)` is the original selected BBP
lift. This report proves source transport and source identification in a
specified rational class; it proves no asymptotic cancellation of the
selected real-circle characters, no normality, and no RH statement.

## S1. Every negative-integer pole has an exact source moment

For complex `|u|<1` define

\[
a_j(u)=\frac{1}{8^j}\sum_i c_i(b_i-u)^{j-1}\quad(j\ge1).
\]

Thus `a_1=0`, and the first terms are

\[
a_2=\frac{15}{64},\qquad
a_3=\frac{151-30u}{512},\qquad
a_4=\frac{1209-453u+45u^2}{4096}.
\]

**Theorem.** Initially for `Re(s)>-1`, and subsequently by meromorphic
continuation to every complex `s`,

\[
\boxed{D(s,u):=\sum_{n\ge1}n^{-s}r_u(n)
=\sum_{j\ge2}a_j(u)\zeta(s+j).}\tag{S1}
\]

The right side converges normally on every compact subset away from its
possible pole hyperplanes. Its only possible poles in `s` are simple poles
at `s=1-j`, with residue exactly `a_j(u)`. At `u=0` all these residues are
strictly positive, so every `-1,-2,...` is an actual simple pole.

**Proof.** Set `alpha_i=(b_i-u)/8`. If `|u|<1`, then
`|alpha_i|<1`, and the geometric expansion gives

`r_u(n)=(1/8) sum_i c_i sum_(k>=0) alpha_i^k n^(-k-1)`.

The `k=0` term vanishes because `sum c_i=0`. The resulting series is
absolutely summable after multiplication by `n^(-s)` when `Re(s)>-1`,
which permits exchanging the sums. On a compact subset of `|u|<1`, put
`rho=sup_i |alpha_i|<1`. Since `sum |c_i|/8=1`,
`|a_j(u)|<=rho^(j-1)`. For `j` sufficiently large, `zeta(s+j)` is
uniformly bounded on any fixed compact `s` set. The tail therefore
converges normally. At `s=1-j0`, only the `j0` term has a pole, and
zeta's residue at 1 is 1. At `u=0`, for every integer `j>=2`,

\[
\frac{15}{56}(7/8)^{j-1}\le a_j(0)<\frac12(7/8)^{j-1}.
\tag{S1a}
\]

Indeed the ratio of the three negative contributions to
`4*7^(j-1)` is at most its value `13/28` at `j=2`.

**Finite certificate.** If `sigma=Re(s)` and integer `J>=2` satisfies
`sigma+J>0`, then, for `rho=(7+|u|)/8<1`,

\[
\left|D(s,u)-\sum_{j=2}^J a_j(u)\zeta(s+j)\right|
\le\left(1+\frac1{\sigma+J}\right)\frac{\rho^J}{1-\rho}.
\tag{S1b}
\]

The estimate applies to the analytic tail, including when a retained
finite term accounts for a pole; the full `D(s,u)` itself is not finite
at that pole. It follows from
`|zeta(s+j)|<=zeta(sigma+j)<=1+1/(sigma+j-1)` in the tail.
For a mixed derivative of orders `(k,ell)`, use complex radii
`delta>0`, `epsilon>0` with `sigma-delta+J>0` and
`|u|+epsilon<1`. Cauchy's estimate multiplies the same bound, evaluated
at `sigma-delta` and `rho_epsilon=(7+|u|+epsilon)/8`, by
`k! ell!/(delta^k epsilon^ell)`. This supplies rigorous finite tail
control for every finite mixed jet.

## S2. Source translation is a Pascal group on the residue tower

For all complex `u,v`, polynomial identities give

\[
\boxed{a_j(u+v)=\sum_{r=1}^j
\binom{j-1}{r-1}(-v/8)^{j-r}a_r(u).}\tag{S2}
\]

On every finite grade truncation the lower triangular matrices in S2
satisfy `T(v+w)=T(v)T(w)` and `T(0)=I`; they are invertible with
inverse `T(-v)`. This is literal Pascal translation of the same source
moments, not a metaphorical correspondence between triangles.

Differentiating gives, with `a_1=0`,

\[
\partial_u^\ell a_j(u)=
\frac{(-1)^\ell}{8^\ell}
\frac{(j-1)!}{(j-1-\ell)!}a_{j-\ell}(u)
\quad(0\le\ell<j),\tag{S2a}
\]

and zero when `ell>=j`. Consequently `partial_u^ell D` has no poles
to the right of `s=-ell-1`, and its rightmost pole is

\[
\operatorname{Res}_{s=-\ell-1}\partial_u^\ell D(s,u)
=\frac{(-1)^\ell(\ell+1)!}{8^\ell}\frac{15}{64}.
\tag{S2b}
\]

For `partial_s^k partial_u^ell D`, the principal part at `s=1-j` is

\[
\frac{(-1)^k k!\,\partial_u^\ell a_j(u)}
{(s-(1-j))^{k+1}}.
\tag{S2c}
\]

All parameter derivatives commute wherever the joint analytic function
is defined. Thus this construction supplies no nonzero holonomy of
spectral-order and source-shift differentiation. A different connection
would require its own definition and proof.

### The first source tangent removes the original pole

Write `q_i(u)=1-(b_i-u)/8`, `alpha_i=1-q_i`. The finite part at `s=-1`
is the existing source-specific digamma function

\[
F(u)=-\frac18\sum_i c_i\alpha_i(u)\psi(q_i(u)).
\tag{S2d}
\]

Since `a_2` is constant, every positive source derivative removes that
pole. For each integer `ell>=1`,

\[
\boxed{\partial_u^\ell D(-1,u)
=\sum_{n\ge1}n\,\partial_u^\ell r_u(n)
=F^{(\ell)}(u)
=\frac1{8^{\ell+1}}\sum_i c_i
\left[\ell\psi^{(\ell-1)}(q_i)-\alpha_i\psi^{(\ell)}(q_i)\right].}
\tag{S2e}
\]

The source derivative decays as `n^(-ell-2)`, so the displayed
weighted series converges absolutely. For real `|u|<1`, its sign is
`(-1)^ell`, strictly: use the positive original Laplace kernel
`Q(t)=4-2e^(-3t)-e^(-4t)-e^(-5t)>0` and differentiation under its
integral. This is an operational regularization effect of the source
tangent, separate from the analytic value `zeta(-1)`.

## S3. A common family connects zeta data to the actual BBP endpoint

For `|z|<1`, `|u|<1`, and any complex `s`, put

\[
\Theta(s,z,u)=\sum_{n\ge1}z^n n^{-s}r_u(n).
\]

It is entire in `s` and analytic in the other indicated variables.
Absolute summation gives the exact common-basis transport

\[
\boxed{\Theta(s,z,u)=\sum_{j\ge2}a_j(u)\operatorname{Li}_{s+j}(z).}
\tag{S3}
\]

On `Re(s)>-1`, letting real `z` tend to 1 from below recovers `D(s,u)`.
Elsewhere its `z=1` specialization requires the meromorphic
continuation established in S1; a direct divergent limit is not
asserted. With the original source and zero seed,

\[
\boxed{\Theta(0,1/16,0)=\pi/16.}\tag{S3a}
\]

The last equality uses precisely the original BBP series. The finite
selected lift is recovered without any infinite future input:

\[
\boxed{U_N=\sum_{j\ge2}a_j(0)
\sum_{n=1}^N\frac{16^{N-n}}{n^j}.}\tag{S3b}
\]

An alternative common integral, initially on `Re(s)>-1`, is

\[
D(s,u)=\int_0^\infty e^{(7-u)t}Q(t)
\operatorname{Li}_s(e^{-8t})\,dt.\tag{S3c}
\]

Here `partial_u` multiplies the integrand by `-t`; `partial_s`
differentiates the polylogarithm's order. Absolute convergence of the
original series proves the valid interchange. For `ell` source
derivatives its domain expands to `Re(s)>-ell-1`.

**Boundary.** Every `a_j`, `D`, and `Theta` in this section depends only
on the source. A seed `sigma` remains the separate initial datum:
`U_N(sigma)=16^N sigma+U_N(0)`, with completed endpoint
`sigma+Theta(0,1/16,0)`. No spectral-source identity alone selects the
authentic seed or bounds its signed long-time occupation. Even after
the seed is marked, an exact representation is not cancellation.

## S4. A finite source certificate in the four-pole rational class

Let `mu_k=sum_i c_i b_i^k=8^(k+1)a_(k+1)(0)`. For the authentic source,

\[
(\mu_0,\ldots,\mu_7)
=(0,15,151,1209,8995,64905,461611,3259089).
\tag{S4}
\]

The moment matrix `H=(mu_(i+j))_(0<=i,j<=3)` factors as
`V diag(c) V^T`, where `V_(k,i)=b_i^k`. Therefore

\[
\det H=(\prod_i c_i)\prod_{i<j}(b_i-b_j)^2=-115200\ne0.
\tag{S4a}
\]

Solving

`H (p_0,p_1,p_2,p_3)^T=-(mu_4,mu_5,mu_6,mu_7)^T`

gives `(p_0,p_1,p_2,p_3)=(168,-206,89,-16)`, hence the exact
annihilator

\[
p(t)=t^4-16t^3+89t^2-206t+168
=(t-7)(t-4)(t-3)(t-2).\tag{S4b}
\]

Recovering its distinct roots and solving the four-row Vandermonde
system for the weights returns exactly `(b,c)`, up to permutation.

**Identification theorem.** Among sources
`sum_(i=1)^d c_i/(8n-b_i)` with `d<=4`, distinct nodes `|b_i|<8`, nonzero
weights, and the specified clock 8, these eight exact moments uniquely
determine the original rational source. No pole positions need be
supplied in advance. Nonzero `det H` first forces `d=4`; the linear
annihilator system and Vandermonde inversion then prove uniqueness.
If the four nodes are already fixed, `mu_0,...,mu_3` suffice.

The moment `mu_0=0` is the known absence of the potential `s=0` pole;
the other seven are the scaled residues at `s=-1,...,-7`. The theorem
is a finite exact source certificate under an explicit rational-class
hypothesis. It is not a claim that finite observations determine an
arbitrary infinite source. Entire additions to the Dirichlet family
can leave every polar residue unchanged outside this class.

## S5. Exact cost of naive spectral-grade truncation

Let integer `J>=1`, `N>=1`, and replace the source by the truncated
geometric expansion `r^(J)(n)=sum_(j=2)^J a_j(0)n^(-j)`, keeping
the same zero seed and radix 16. Denote its lift by `U_N^(J)` and set
`E_(N,J)=U_N-U_N^(J)`. This is the **unwrapped rational lift error**.

Every omitted coefficient is positive, and S1a gives

\[
\boxed{\frac{15}{112}16^N(7/8)^J
\le E_{N,J}<\frac4{15}16^N(7/8)^J.}\tag{S5}
\]

**Proof.** The source tail at `n=1` is between
`(15/7)(7/8)^J` and `4(7/8)^J`. Its first-time contribution is
multiplied by `16^(N-1)`, proving the lower bound. For the upper
bound, all positive source tails are at most the tail at `n=1`;
sum `16^(N-n)` over `n=1,...,N` to get `(16^N-1)/15`.

More precisely,

\[
r_0(1)-r^{(J)}(1)
=4(7/8)^J-\frac12(1/2)^J-\frac15(3/8)^J-\frac16(1/4)^J.
\tag{S5a}
\]

For `J` tending to infinity,
`E_(N,J)/(16^N(7/8)^J)` tends to `1/4` uniformly for `N>=1`;
the `n=1` term gives that limit, and the sum of `n>=2` terms is
bounded by a constant times `2^(-J)`.

Consequently, as `N` tends to infinity,

\[
E_{N,J(N)}\longrightarrow0
\quad\Longleftrightarrow\quad
J(N)-\frac{\log16}{\log(8/7)}N\longrightarrow+\infty.
\tag{S5b}
\]

This is an exact quantitative warning about **this truncation
algorithm**. It is not an information-theoretic impossibility theorem.
The finite rational-source reconstruction in S4 bypasses the
truncation cost by recovering the exact law. Nor does divergence of
the unwrapped error prove failure of circle-phase approximation:
large errors can be near integers. The valid sufficient character
bound is

`|exp(2pi i h U_N)-exp(2pi i h U_N^(J))| <= min(2,2pi |h| E_(N,J))`.

The source maps are thus genuinely operational and calibrated, but no
new fixed-frequency macroscopic cancellation bound is obtained.

## Literature authority and audit boundary

The only special-function facts used as external inputs are zeta's
Dirichlet series, simple pole with residue 1, meromorphic continuation,
the polylogarithm defining series, and standard digamma/polygamma
identities. Primary reference pages retrieved in this round:

- NIST DLMF §25.2, equations 25.2.1 and 25.2.4:
  <https://dlmf.nist.gov/25.2>.
- NIST DLMF §25.12, equation 25.12.10:
  <https://dlmf.nist.gov/25.12#E10>.
- NIST DLMF §5.15, equations 5.15.1 and 5.15.5:
  <https://dlmf.nist.gov/5.15>.

S1--S5 are elementary deductions presented in full above, not claims
that DLMF states these SUCC-specific propositions. Exact tests check
the rational maps, finite truncation bounds, Prony reconstruction,
translation group and countermodels. Analytic theorems rest on the
paper convergence arguments, not finite numerical agreement.
