# A posterior path law connects the golden transform, Euler's constant and the shrinking error

**Result.** The finite polynomial family used in the earlier oily-macaroni
bridge is exactly a rescaled Bayesian posterior after a specified sequence
of failures. Its negative log-survival coordinate has the exponential law
at every finite stage. Updating by one more failure is an exact exponential
tilt followed by a scale change, and that normalized operation preserves
the exponential law. The Euler remainder is the expected logarithmic defect
between this coordinate and its finite linear approximation.

Together with the inherited authentic BBP error comparison, this gives an
explicit path-conditioning interpretation of the connection

$$
\delta-\left[\lambda+\mathbb E\log X_m\right]
=\epsilon_m,\qquad
T_m\sim\frac{\epsilon_m^2}{16},
\qquad \lambda=\varphi^{-1},\quad\delta=\lambda-\gamma.
$$

The conditioning model is declared, and its conditional independence is
load-bearing. It is not an authenticated stochastic generation law for the
BBP orbit. The scalar bridge does not identify the two probability laws,
and no selected Weyl saving or normality theorem follows.

## 1. Provenance and the precise new connection

This dossier belongs to the round based on PR #313,
`79344c62c39c96755b742700b3d4d22fa60d86da`. It combines existing results:

- The [common-source bridge, §§3–5](OILY_MACARONI_SOURCE_BRIDGE.md)
  already constructs the polynomial densities, their exponential limit,
  the golden Laplace fixed point, the Euler remainder and the all-index
  comparison with the original BBP tail.
- [Realized paths and field feedback](REALIZED_PATHS_AND_FIELD_FEEDBACK.md)
  identifies the classical equality between Pólya reinforcement and
  a static Beta bias for every finite observed word.
- [Selection likelihood and revelation](SELECTION_LIKELIHOOD_AND_REVELATION.md)
  distinguishes full path selection from marginal information and keeps
  the reference probability law explicit.

Bayes' rule, Beta conjugacy, the probability integral transform and the
Gamma/Laplace identities are classical. The contribution here is the
exact identification of the previously used finite family with this
posterior experiment, and the resulting interpretation of its already
authenticated scalar error. No independent scholarly-priority claim is
made. The original source and production modules remain unchanged.

## 2. One declared joint law and its finite posteriors

Let $\Theta$ have the uniform probability law on $(0,1)$. Conditional on
$\Theta=\theta$, let the trial outcomes be independent, with

$$
\Pr(L_i\mid\Theta=\theta)=\theta,\qquad
\Pr(R_i\mid\Theta=\theta)=1-\theta.
$$

For every integer $m\ge1$, define

$$
A_m=\bigcap_{i=1}^{m-1}R_i,
$$

where $A_1$ is the whole sample space. Write $\mathbb E_m$ and
$\Pr_m$ for expectation and probability conditional on $A_m$.
This specifies one consistent joint model, rather than separately
postulating a posterior at each horizon.

Every finite observed-word probability is rational. For a particular
ordered word of length $n$ with $l$ occurrences of $L$ and $r$ of $R$,

$$
\Pr(\text{word})=\int_0^1\theta^l(1-\theta)^r\,d\theta
=\frac{l!r!}{(n+1)!},\qquad l+r=n.
$$

The latent parameter remains continuous. A finite number of observations
and a finite-degree density do not turn it into a finite-state law or
make an irrational constant an exact finite rational output.

### Proposition 1: the earlier finite family is exactly this posterior

For every $m\ge1$,

$$
\Pr(A_m)=\frac1m,\qquad
\Theta\mid A_m\sim\operatorname{Beta}(1,m).
$$

Consequently, the coordinate $X_m=m\Theta$, observed under $\Pr_m$,
has density

$$
\boxed{p_m(x)=(1-x/m)^{m-1},\qquad 0<x<m.}
$$

**Proof.** Conditional independence gives
$\Pr(A_m\mid\Theta=\theta)=(1-\theta)^{m-1}$. Integration against
the uniform prior gives $1/m$. Bayes' rule therefore gives posterior
density $m(1-\theta)^{m-1}$. Substituting $x=m\theta$ yields the
displayed density, including its normalization. $\square$

The evidence $1/m$ belongs to this static-bias mixture. The same word
under known independent fair trials has probability $2^{-(m-1)}$.
These are different reference laws, not competing evaluations of one law.

For every integer $k\ge0$, the posterior predictive probability is

$$
\boxed{\Pr(A_{m+k}\mid A_m)
=\mathbb E_m(1-\Theta)^k
=\frac{m}{m+k}
=\frac1{1+k/m}.}
$$

This exact reciprocal transform will reappear as a Laplace transform.
Its values at rational arguments are already given by finite observed-word
probability ratios.

## 3. One more observation is a normalized transformation

Put $c_m=(m+1)/m$. Bayes' rule for one additional failure gives, for
every bounded measurable function $f$,

$$
\boxed{
\mathbb E_{m+1}f(X_{m+1})
=c_m\mathbb E_m\left[
\left(1-\frac{X_m}{m}\right)f(c_mX_m)\right].
}
$$

The factor $1-X_m/m=1-\Theta$ is the new failure likelihood. Its
posterior mean is $m/(m+1)$, which explains the normalization $c_m$.
The argument changes because the coordinate itself is rescaled from
$m\Theta$ to $(m+1)\Theta$.

### Proposition 2: the log-survival coordinate is exactly exponential

Define

$$
\boxed{Z_m=-m\log(1-\Theta).}
$$

For every $m\ge1$, under $\Pr_m$,

$$
\boxed{Z_m\sim\operatorname{Exp}(1),\qquad
X_m=m(1-e^{-Z_m/m}).}
$$

**Proof.** The posterior survival function of $\Theta$ is
$S_m(\theta)=(1-\theta)^m$. For $z\ge0$,

$$
\Pr_m(Z_m>z)
=\Pr_m(\Theta>1-e^{-z/m})
=(e^{-z/m})^m=e^{-z}.
$$

The relation to $X_m$ is the inverse change of coordinates. $\square$

Thus $Z_m=-\log S_m(\Theta)$ is the negative logarithm of posterior
survival, a dimensionless classical probability calibration. This is an
exact finite-stage law, not merely the large-$m$ limit of $X_m$.

One more failure weights the old coordinate by
$1-\Theta=e^{-Z_m/m}$, while the new coordinate is $Z_{m+1}=c_mZ_m$.
Therefore

$$
\boxed{
\mathbb E_{m+1}f(Z_{m+1})
=c_m\mathbb E_{Z\sim\operatorname{Exp}(1)}
\left[e^{-Z/m}f(c_mZ)\right]
=\mathbb E_{Z\sim\operatorname{Exp}(1)}f(Z).
}
$$

The last equality follows by substituting $u=c_mz$ in the integral.
It is a precise exponential tilt, normalization and scale change that
preserves the law. It does not say that the same numerical value of $Z$
is preserved along an observed sample path.

In Laplace coordinates, the general normalized transformation is

$$
\mathcal R_m[L](s)=
\frac{L(c_ms+1/m)}{L(1/m)}.
$$

For $L(s)=1/(1+s)$, its normalizer is $L(1/m)=1/c_m$, and

$$
\mathcal R_m[L](s)=c_mL(c_ms+1/m)=\frac1{1+s}=L(s).
$$

This is the normalized multiplication-to-log connection in the declared
posterior model. Its source assumptions and uniqueness limits are stated
in §7 below.

## 4. The same law gives the three classical constants

### 4.1 Exponential survival and a finite rational sequence

The exact exponential coordinate has $\Pr_m(Z_m>1)=e^{-1}$.
For a construction that does not put an exponential threshold into the
finite input, the linear coordinate instead gives

$$
\Pr_m(X_m>1)=(1-1/m)^m\longrightarrow e^{-1}.
$$

The left side is rational for every finite $m$, including zero at $m=1$.
This is the inherited finite survival construction, now identified with
a specific posterior law.

### 4.2 Harmonic sums and the logarithmic mean

Let $H_m=\sum_{j=1}^m1/j$. Then

$$
\mathbb E_m\log\Theta=-H_m,\qquad
\boxed{\mathbb E_m\log X_m=\log m-H_m.}
$$

For a direct proof, use the posterior distribution function to write

$$
-\mathbb E_m\log\Theta
=\int_0^1\frac{1-(1-x)^m}{x}\,dx
=\int_0^1\sum_{j=0}^{m-1}u^j\,du=H_m.
$$

The first equality is the tail-integral formula for $-\log\Theta$,
and the substitution is $u=1-x$. These integrals are finite.

The logarithmic mean of the exponential coordinate is

$$
\mathbb E_m\log Z_m=-\gamma.
$$

This is the classical Gamma derivative identity. Section 5 also derives
it directly from the harmonic-limit definition of $\gamma$ and a
pointwise bound on the change of coordinates.

### 4.3 A golden fixed point of the predictive/Laplace transform

For $s\ge0$, the common exponential law has

$$
L(s)=\mathbb E_m e^{-sZ_m}=\frac1{1+s}.
$$

At $s=k/m$, this is exactly the predictive probability in §2, because
$e^{-(k/m)Z_m}=(1-\Theta)^k$. Its unique nonnegative fixed point is

$$
L(\lambda)=\lambda,
\qquad \lambda^2+\lambda=1,
\qquad \boxed{\lambda=\frac{\sqrt5-1}{2}=\varphi^{-1}.}
$$

The reciprocal map preserves rational inputs and has an elementary
finite iteration: $q_0=0$, $q_{r+1}=1/(1+q_r)$. Its even iterates
increase toward $\lambda$, its odd iterates decrease toward it, and
$q_{2r}\le\lambda\le q_{2r+1}$. Indeed the second iterate is
$(1+x)/(2+x)$, which is increasing with derivative at most $1/4$ on
$[0,1]$; consequently the bracket width is at most $4^{-r}$.
Equivalently the iterates are successive Fibonacci ratios. This is a
finite arithmetic construction of brackets, not a claim that observing
a finite word returns an exact irrational value.

The inherited linear-coordinate transforms $L_m(s)=\mathbb E_m e^{-sX_m}$
have unique fixed points $\lambda_m\in(0,1)$ and satisfy

$$
0\le L_m(s)-L(s)\le\frac{s}{m+1},\qquad
\lambda<\lambda_m\le\lambda+\frac{\lambda}{m+1},
\qquad \lambda_m\downarrow\lambda.
$$

These bounds and their rational certificates are inherited from the
[common-source proof](OILY_MACARONI_SOURCE_BRIDGE.md) and
[exponential Gamma bridge module](../../observational_succ/exponential_gamma_bridge.py).

## 5. The Euler remainder is an exact logarithmic coordinate defect

The previous identities give, for every $m\ge1$,

$$
\boxed{
\epsilon_m=H_m-\log m-\gamma
=\mathbb E_m[\log Z_m-\log X_m]
=\mathbb E_{Z\sim\operatorname{Exp}(1)}
\log\frac{Z}{m(1-e^{-Z/m})}.
}
$$

This is a positive defect of replacing the normalized log-survival
coordinate by the linear coordinate. It does not arise from the
numerical proximity of $\lambda$ and $\gamma$.

For completeness, put $u=Z/m>0$. The inequalities

$$
1-e^{-u}<u,
\qquad
1-e^{-u}=2e^{-u/2}\sinh(u/2)>ue^{-u/2}
$$

give the strict pointwise bounds

$$
0<\log\frac{u}{1-e^{-u}}<\frac u2.
$$

Since $\mathbb EZ=1$, the log-coordinate difference is integrable and

$$
\boxed{0<\epsilon_m<\frac1{2m}.}
$$

This also proves $\mathbb E\log Z=-\gamma$ without taking a Gamma
derivative: $\mathbb E\log X_m=\log m-H_m\to-\gamma$, and the
expected difference tends to zero by the displayed bound.

With the named offset $\delta=\lambda-\gamma$,

$$
\boxed{
\delta-\left[\lambda+\mathbb E_m\log X_m\right]=\epsilon_m.
}
$$

The golden center is itself selected by the declared reciprocal transform.
Nevertheless, this subtraction does not distinguish it: for every real
$c$, with $\delta_c=c-\gamma$,

$$
\delta_c-\left[c+\mathbb E_m\log X_m\right]=\epsilon_m.
$$

Thus the common posterior supplies a genuine construction of the golden
transform and the Gamma logarithmic mean, while the shrinking defect is
unchanged by a common additive center. It does not prove that the oily
offset is necessary for a cancellation estimate.

### The inherited comparison to the original BBP tail

Retain the unchanged original four-pole source

$$
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\qquad U_0=0,\quad U_n=16U_{n-1}+r(n),
$$

and its authentic Green tail

$$
T_m=\sum_{j\ge1}16^{-j}r(m+j),\qquad m\ge1.
$$

The [previous all-index theorem, §5](OILY_MACARONI_SOURCE_BRIDGE.md)
already proves

$$
\boxed{\frac1{(8m+7/2)^2}<T_m<\frac{\epsilon_m^2}{16}},
\qquad
\boxed{
\left(\frac m{m+7/16}\right)^2
<\frac{16T_m}{\epsilon_m^2}<1.
}
$$

Therefore

$$
\boxed{
T_m\sim\frac1{16}
\left[\mathbb E_m(\log Z_m-\log X_m)\right]^2
=\frac{\epsilon_m^2}{16}.
}
$$

The comparison theorem and its positive-polynomial certificate are
**inherited**, not newly proved by the posterior interpretation. The new
statement identifies the exact posterior quantity already appearing in
that authenticated scalar comparison. It does not identify the posterior
law with the BBP source's endpoint law. In particular, the genuine BBP
endpoint scaling has Gamma shape two, whereas this all-failure posterior
normalization has exponential, or Gamma shape one, law.

## 6. Path information and marginal posterior information differ

Let $\mathbb P$ be the declared joint law of $\Theta$ and the trials,
and let $\mathbb Q_m=\mathbb P(\cdot\mid A_m)$. Its full likelihood
is $m\mathbf1_{A_m}$, so

$$
D(\mathbb Q_m\Vert\mathbb P)=\log m.
$$

The same value is the relative entropy of selecting the all-failure
observed prefix against its reference word law. The latent posterior
has a different likelihood relative to the uniform prior:

$$
\rho_m(\theta)=m(1-\theta)^{m-1}.
$$

Since $\mathbb E_m\log(1-\Theta)=-1/m$, its entropy is

$$
\boxed{
D(\mathbb Q_m^{\Theta}\Vert\mathbb P^{\Theta})
=\log m-1+\frac1m.
}
$$

Equivalently, the log likelihood is
$\log\rho_m=\log m-(1-1/m)Z_m$. These are exact formulas in nats.
They also hold at $m=1$, when both entropies vanish.

The chain-rule gap is exactly

$$
\log m-\left(\log m-1+\frac1m\right)
=1-\frac1m.
$$

It is the posterior mean of the conditional cost of forcing the observed
word at fixed $\Theta$:

$$
\mathbb E_m[-\log\Pr(A_m\mid\Theta)]
=-(m-1)\mathbb E_m\log(1-\Theta)=1-\frac1m.
$$

This is an exact instance of information discarded by marginalization.
The full selected-event cost $\log m$ and the latent-posterior cost
$\log m-1+1/m$ must not be substituted for one another.

## 7. Controls that delimit the interpretation

### Conditional independence is essential

Keep the same uniform $\Theta$ and the same one-trial probabilities,
but draw just one independent uniform variable $V$ and set
$R_i=\{V>\Theta\}$ for every $i$. Conditional on $\Theta=\theta$,
each individual trial still has failure probability $1-\theta$.
The trials now share the same coin.

For every $m\ge2$, their repeated-failure event has likelihood
$1-\theta$, not $(1-\theta)^{m-1}$. Consequently

$$
\Pr(A_m)=\frac12,\qquad
\Theta\mid A_m\sim\operatorname{Beta}(1,2),\qquad
\mathbb E[m\Theta\mid A_m]=\frac m3.
$$

The polynomial posterior family, predictive law and exponential
normalization claimed above do not follow from one-step probabilities
alone. The full joint path law is necessary. This is a concrete hostile
control, not a hypothetical warning.

### The evidence alone does not identify the posterior

In the conditionally independent uniform-prior model, $m-1$ consecutive
successes also have probability $1/m$, but give posterior
$\operatorname{Beta}(m,1)$. The event labels and their likelihoods,
not just their scalar evidence, select the posterior. A Bayesian update
therefore uses retained joint information; it is not an inverse derived
from an averaged probability by itself.

### The prior and normalization matter

For a simple exact prior control, replace the uniform prior by
$\operatorname{Beta}(2,1)$ and keep conditional independence. After the
same $m-1$ failures the posterior is $\operatorname{Beta}(2,m)$, and
$\widetilde X_m=m\Theta$ has density

$$
\widetilde p_m(x)=\frac{m+1}{m}\,x(1-x/m)^{m-1},\qquad 0<x<m.
$$

For $m\ge2$ this is bounded by $(3/2)xe^{-x/2}$ and converges
pointwise to $xe^{-x}$. Dominated convergence proves a Gamma-shape-two
limit, with Laplace transform $(1+s)^{-2}$ and logarithmic mean
$1-\gamma$. Its direct positive Laplace fixed point solves
$q(1+q)^2=1$, rather than $q^2+q=1$.

The same posterior arises under the original uniform prior after one
specified success and $m-1$ failures. This is a posterior-model relation,
not a proof that its joint law is the authentic BBP endpoint source.
The separately graded golden–Gamma identity in the
[atomic dossier](FOUR_POLE_ATOMIC_SUBSTRATE.md) retains its own assumptions.

The normalized transformation in §3 is not uniquely exponential either.
For every $\alpha>0$, substitution gives

$$
L_\alpha(s)=(1+s)^{-\alpha},\qquad
\frac{L_\alpha(c_ms+1/m)}{L_\alpha(1/m)}
=L_\alpha(s).
$$

Thus every unit-rate Gamma transform is fixed by that general normalized
operation. Its normalizing multiplier is $c_m^\alpha$. The specified
uniform-prior, all-failure model selects shape one and multiplier $c_m$;
normalization invariance alone does not.

For a direct fixed-coordinate control, keep **the same**
$Z_m=-m\log(1-\Theta)$ when changing the model. Under the Beta$(2,m)$
posterior its Laplace transform is

$$\frac{m+1}{(1+s)(m(1+s)+1)},$$

while the shared-coin posterior gives $2/(2+ms)$ for $m\ge2$.
At $m=4,s=1$, the three values are exactly $1/2$ for the original model,
$1/3$ for the shared coin, and $5/18$ for the changed prior. The replay
checks each by independent polynomial integration. For a scale control,
replacing $Z$ by $2Z$ changes its Laplace transform to $1/(1+2s)$ and
its positive fixed point to $1/2$.

Allowing each continuous posterior to choose its own cumulative-hazard
coordinate would make every transformed law exponential by the probability
integral transform. That generic fact is not a source discriminator. The
meaningful result here retains the explicit coordinate, declared prior and
conditional path law, finite linear distortion and inherited BBP error map.

### A coupling of marginals is not the actual observed time path

The inherited construction may use a single auxiliary
$Z\sim\operatorname{Exp}(1)$ and define
$\widehat X_m=m(1-e^{-Z/m})$. This couples the marginal laws
monotonically and proves the inherited error bounds. It is not the same
as following one fixed latent $\Theta$ through an observed trial sequence:
the posterior conditioning changes with $m$, and the coordinate
$Z_m=-m\log(1-\Theta)$ changes too.

In the conditionally independent model,

$$
\Pr\!\left(\bigcap_{m\ge1}A_m\right)
=\lim_{m\to\infty}\frac1m=0.
$$

All the finite posteriors are valid. They do not assign positive
probability to an actual infinite all-failure realization. The all-failure
symbolic word is also a constant, nonnormal word, although the posterior
construction above contains the exponential, golden and Euler constants.
Their common occurrence is not an equidistribution criterion.

## 8. Exact interfaces and the remaining arithmetic obligation

No new production module is needed for this connection. The existing
[field-feedback module](../../observational_succ/path_field_feedback.py)
provides the exact static-Beta and reinforced word probabilities. The
[exponential Gamma bridge](../../observational_succ/exponential_gamma_bridge.py)
provides finite moments, survival probabilities, log intervals, Laplace
intervals, golden brackets and the original Euler/BBP comparison certificates.

The [assembled replay probe](../../scripts/seinfeld_realization_probe.py)
records the finite density, predictive, update and authentic-tail checks.
Its actual results belong to the round's
[validation record](SEINFELD_REALIZATION_VALIDATION.md). This dossier does
not preclaim completion of the running full suite or new formal kernel
authority. Production code and tests were not changed for this connection.

The result is a concrete common construction and an exact error
interpretation. A specified posterior path law produces the old finite
family; negative log-survival supplies its normalized exponential
coordinate; the reciprocal predictive transform selects $\lambda$;
the log mean gives $-\gamma$; and their finite coordinate defect is
exactly the Euler remainder already controlling the authentic BBP tail.

What remains unproved is a source-authenticated relation from those
posterior probabilities or their normalization dynamics to the original
selected arithmetic phases. The additive golden center still cancels
from the shrinking error, and no signed across-time cancellation follows
from the scalar comparison. See the
[round synthesis](SEINFELD_INVERSE_AVERAGING_AND_REALIZATION.md) for the
remaining source and phase-correlation obligations.
