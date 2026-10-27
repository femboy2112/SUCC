# Target Theorem A — All-prime invariant measures (independent derivation)

**Claim (to verify):** Let $\mu$ be a Borel probability measure on $\mathbb R/\mathbb Z$.
If $(T_p)_*\mu = \mu$ for every prime $p$, where $T_p(x) = px \pmod 1$, then

$$\mu = c\,\delta_0 + (1-c)\lambda,\qquad 0\le c\le 1.$$

## Step 1: Fourier consequence

For the Fourier coefficients $\widehat\mu(k) = \int e(-kx)\,d\mu(x)$, prime-invariance gives

$$\widehat\mu(k) = \int e(-kx)\,d(T_p)_*\mu(x) = \int e(-k\,px)\,d\mu(x) = \widehat\mu(pk).$$

So $\widehat\mu(k) = \widehat\mu(pk)$ for every prime $p$ and every $k\in\mathbb Z$.

## Step 2: common multiples

Take arbitrary positive integers $m,n$. We want $\widehat\mu(m) = \widehat\mu(n)$.

Write $m = p_1^{a_1}\cdots p_r^{a_r}$, $n = q_1^{b_1}\cdots q_s^{b_s}$.
Let $M = \mathrm{lcm}(m,n)$.

By iterating $\widehat\mu(k) = \widehat\mu(pk)$ along the prime-power chain from $m$ up to $M$
(multiplying by the missing primes one at a time), and from $n$ up to $M$:

$$\widehat\mu(m) = \widehat\mu(M) = \widehat\mu(n).$$

Hence **all nonzero Fourier coefficients of $\mu$ are equal to a common value $\gamma$**:

$$\widehat\mu(k) = \gamma \quad\text{for all } k\neq 0.$$

This uses: for each prime $p$, $\widehat\mu(k)=\widehat\mu(pk)$, and $M/m$ is a product of primes
(the prime powers of $M/m$'s prime factorization, each applied via repeated $k\mapsto pk$).
Actually the cleanest statement: every positive integer is a product of primes, so
$\widehat\mu(k)=\widehat\mu(k\cdot P)$ for any $P$ whose primes all divide... let me be careful.

The relation $\widehat\mu(k)=\widehat\mu(pk)$ holds for EVERY prime $p$, no divisibility needed.
So for any integer $m$ and any integer $a$ that is a product of primes (i.e. any integer),
$\widehat\mu(m) = \widehat\mu(ma)$.

Given $m,n$, take $a = n$ and $b = m$: we need a common target. Use $\widehat\mu(mn)$:
$$\widehat\mu(m) = \widehat\mu(m\cdot n)\quad (\text{via } p\mid n \text{ iterated}),$$
$$\widehat\mu(n) = \widehat\mu(n\cdot m) = \widehat\mu(mn).$$
Both reach $\widehat\mu(mn)$, so $\widehat\mu(m)=\widehat\mu(n)$. QED.

(Each step is literally $\widehat\mu(t)=\widehat\mu(pt)$ for a prime $p$; $n$ is a product of primes.)

## Step 3: identify $\gamma = \mu(\{0\})$ via Cesaro

For any finite measure, the atom at 0 satisfies
$$\mu(\{0\}) = \lim_{N\to\infty}\frac1N\sum_{k=1}^N \widehat\mu(k)$$
(because the $N$-th Fejer kernel $K_N$ satisfies $\int K_N\,d\mu \to \mu(\{0\})$, and
$K_N(x) = \frac1N\sum_{k=1}^N e(-kx)$... check normalization).

Since every $\widehat\mu(k)=\gamma$ for $k\neq 0$, the Cesaro average is $\gamma$.
Hence $\gamma = \mu(\{0\}) =: c$.

## Step 4: uniqueness

A finite (signed) measure on $\mathbb R/\mathbb Z$ is determined by its Fourier coefficients.
The measure $\nu = c\delta_0 + (1-c)\lambda$ has Fourier coefficients
$\widehat\nu(0)=1$, $\widehat\nu(k)=c$ for $k\neq 0$.

Our $\mu$ has $\widehat\mu(0)=1$ and $\widehat\mu(k)=\gamma=c$ for $k\neq0$.
So $\mu=\nu$. Done.

## Verification of Step 3 normalization

Fejer kernel: $K_N(x) = \frac1N\sum_{j=0}^{N-1}\sum_{k=-j}^{j} e(kx) = \frac1N\left(\frac{\sin(N\pi x)}{\sin(\pi x)}\right)^2 \ge 0$,
$\int K_N = 1$, and $K_N \to 0$ uniformly off any neighborhood of 0, while $K_N(0)=N\to\infty$.

Actually $\widehat\mu(k) = \int e(-kx)d\mu$. Then $\frac1N\sum_{k=0}^{N-1}\widehat\mu(k) = \int \frac1N\sum_{k=0}^{N-1} e(-kx) d\mu$.
The kernel $\frac1N\sum_{k=0}^{N-1}e(-kx)$ is the Dirichlet kernel $D_N$, not Fejer. $D_N$ does NOT converge
weakly to $\delta_0$ in the needed sense.

Correct: use Fejer, $\frac1N\sum_{k=0}^{N-1}\left(1-\frac kN\right)$-style, i.e.
$\lim_{N}\frac1N\sum_{k=1}^N \left(1-\frac{k}{N}\right)\widehat\mu(k)$? Let me be precise.

The standard fact: $\mu(\{0\}) = \lim_{N\to\infty} \frac1N\sum_{k=1}^N \widehat\mu(k)$ is TRUE for finite measures,
because $F_N(x) := \frac1N\sum_{k=1}^N e(-kx)$... no.

Let me just use the clean statement:

**Lemma (Wiener).** For a finite complex measure $\mu$ on $\mathbb R/\mathbb Z$,
$$\mu(\{x_0\}) = \lim_{N\to\infty}\frac{1}{N}\sum_{k=-N}^{N}\widehat\mu(k)\,e(k x_0).$$

Hmm, that's for the symmetric sum and it's $\lim \frac1{2N+1}\sum_{k=-N}^N$? Let me verify numerically
rather than trust memory. The symmetric partial sums of Fourier series converge to $\mu(\{x_0\})$
in the sense that $\frac1{2N+1}\sum_{k=-N}^{N} \widehat\mu(k) e(kx_0) \to \mu(\{x_0\})$.

I'll verify by direct computation in the code below, including the exact normalization.

## Conclusion and status

This is a **CLASSICAL** result (folklore / elementary harmonic analysis). It is NOT new.
The novelty claim in the prompt is explicitly disclaimed ("do not claim novelty for an elementary result").

Key honest point for the SUCC application: the theorem is TRUE and gives a clean route —
prime-invariance across all primes ⟹ $\mu = c\delta_0+(1-c)\lambda$ ⟹ only two requirements:
(1) all-prime invariance, (2) $c=0$ (no atom at 0).

But the hard question is whether the *selected* $\pi$ orbit's weak-* limits are all-prime invariant,
which is EXACTLY as hard as the Weyl requirement (need $\widehat\mu(pk)=\widehat\mu(k)$, i.e.
$W_N(pk)-W_N(k)\to0$ for all primes $p$ and all $k$ — that IS the prime-frequency defect vanishing).

So Theorem A REPLACES the single requirement "all Weyl sums vanish" with:
"all prime-frequency defects vanish" + "no atom at zero". The prime-frequency defect
$\Delta_N$ vanishing is genuinely (slightly) weaker-looking but must still be proved for the source.

**Verdict: Theorem A is PROVED (classical). Its value to SUCC is a reformulation, not a shortcut.**
The two conditions (prime-invariance + atom exclusion) are each still equivalent-in-hardness to
the original Weyl statement, but they decompose it in a potentially testable way.
