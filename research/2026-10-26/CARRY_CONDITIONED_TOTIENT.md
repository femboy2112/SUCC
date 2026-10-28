# Literal-carry Oily totients: exact coupling, dyadic alias, and inverse

**Status:** paper-proved finite algebra and quantitative transport; finite exact
tests corroborate the implementation. **No stronger selected Fourier bound is
proved.** The actual source remains the four-pole recurrence with zero initial
state. The native adapter is `observational_succ/integer_bbp_carrier.py`, not a
new forcing engine. Parent: PR #310, `a8c7c85b7a1900d422090f1757c174e7aac69f44`.

The construction answers a precise part of Front A: a primitive arithmetic
observable can actually read the integer carry word, retain its source
conductor, and have an exactly checked complex Fourier map. It also answers
why that construction alone does not answer Front E: its unprojected packet
operator is explicitly invertible; primitive projection introduces an
uncontrolled high-frequency alias.

## 1. Hole contract and novelty boundary

The requested target is cancellation of

$$S_N^U(h)=\sum_{n=1}^N e(hU_n),\qquad e(t)=\exp(2\pi i t),$$

for each fixed nonzero integer $h$. The original source and zero seed are
fixed throughout. Before this construction, the packet primitive character
was conditioned on source time alone, with no actual carry in its argument.

Here the proposed missing edge is: **does adding literal arithmetic carry
information to the packet primitive filter force a better signed estimate?**
The cheapest falsifiers are a same-forcing changed seed, two-digit laws with
equal one-digit marginals, and exact inversion of the proposed averaging
operator. All three are supplied below. The answer for the specified
translation coupling is **no automatic improvement**. This is a finite
construction plus an explicit obstruction, not a new normality criterion
disguised as a proof. A different coupling is not refuted by this result.

## 2. The actual carry word has an exact odd-conductor decoder

Write $x_n=\{U_n\}$, $m_n=\lfloor U_n\rfloor$, and
$c_n=m_n-16m_{n-1}$. For $n\ge1$, $L\ge1$, set

$$q=16^L,\qquad
A_{n,L}=\sum_{j=1}^L16^{L-j}c_{n+j}=m_{n+L}-qm_n.$$

The equality follows by telescoping. **The literal carries are retained:**
$c_n$ can equal 16, so $A_{n,L}$ is not silently assumed to lie in
$\{0,\ldots,q-1\}$. Its cyclic residue is used only when evaluating a
character or a finite quotient.

Let $Q=Q_{n+L}$ be the existing common source conductor, and define

$$B=Q\sum_{j=1}^L16^{L-j}r(n+j),\qquad R=Qx_{n+L}.$$

The original reduced forcing denominator is odd, and each denominator up
to time $n+L$ divides $Q$. Thus $Q$ is odd, $B,R,Qx_n$ are integers, and
the recurrence gives the **literal carry constraint**

$$\boxed{QA_{n,L}=qQx_n+B-R.}$$

Reducing modulo $q$, and using the invertibility of $Q$ modulo $q$, gives

$$\boxed{A_{n,L}\equiv(B-R)Q^{-1}\pmod q.}$$

This is a source-preserving finite morphism: the complete forcing segment,
the arrival remainder, the time, and the actual odd conductor determine
the carry word modulo $16^L$. It is not a statement that arbitrary local
prime residues determine the selected real-circle distribution.

### Exact primitive collapse

Because $q$ is a power of two,

$$\boxed{\mathbf1_{\gcd(A_{n,L},q)=1}
=\mathbf1_{A_{n,L}\text{ odd}}
=\mathbf1_{c_{n+L}\text{ odd}}.}$$

Every earlier carry in the word is multiplied by 16. Therefore **scalar
dyadic primitivity reads only the terminal carry parity, regardless of
word length**. The full character $e(hA_{n,L}/q)$ still reads the entire
word. This is the exact information retained and discarded, rather than
an inference from a numerical match.

## 3. Quantified transport of these words to the selected orbit

Use the already proved authentic Green tail $T_n$ and put
$Y_n=x_n+T_n$. Source completion gives

$$U_{n+L}+T_{n+L}=q(U_n+T_n),\qquad
\boxed{A_{n,L}/q=Y_n-Y_{n+L}/q.}$$

The existing source bounds imply $0<Y_n<16/15$ for $n\ge1$ (for example,
$T_n\le47/[225(n+1)^2]$ and $x_n<1$ suffice), and
$\sum_{n\ge1}T_n\le17/648$. For

$$F_{N,L}(h)=\frac1N\sum_{n=1}^N e(hA_{n,L}/q),$$

the Lipschitz inequality $|e(u)-e(v)|\le2\pi|u-v|<7|u-v|$ gives

$$\boxed{
\left|F_{N,L}(h)-\frac{S_N^U(h)}N\right|
\le\frac{119|h|}{648N}+\frac{112|h|}{15\,16^L}.}$$

This is a transport estimate, **not** a bound on either side by a quantity
tending to zero. It holds with $L=L_N\to\infty$ for each fixed $h$.
It does not give a useful vanishing bound at the alias frequency
$h+16^L/2$ encountered below. The two frequencies must not be conflated.

## 4. A declared joint carry–packet law

At each time $n$, retain exactly PR #310's joint packet law

$$\Pr_n(J=j,X\in dx)=x^{8n}p_j(x)\,dx/T_n.$$

Now adjoin the deterministic, authenticated word $A_{n,L}$ and push forward
by the **declared addition map**

$$K=A_{n,L}+J\pmod q.$$

Equivalently, choose $n$ uniformly in $\{1,\ldots,N\}$, sample its actual
source packet law, and apply this map. This gives a positive probability
law $\nu^{\mathrm{src}}_{N,L}$ on $\mathbb Z/q$ and an arithmetic totient

$$\Phi^{\mathrm{src}}_{N,L}
=\nu^{\mathrm{src}}_{N,L}\{k:\gcd(k,q)=1\}.$$

This law genuinely depends on the source-selected carry history. Unlike
the old time-only primitive filter, it can distinguish changed-seed carry
tapes. **No theorem makes addition of these two grades canonical.** It is
an explicit admissible coupling, tested for what it actually does.

Let $\mu_{N,L}$ be the empirical law of $A_{n,L}\pmod q$. The limiting
packet weights are $w_j=(j+1)/2^{j+2}$, with

$$G(z)=\sum_{j\ge0}w_jz^j=(2-z)^{-2}.$$

Wrap these weights modulo $q$ to obtain the exact rational law

$$w_q(a)=2^{-a-2}\left[
\frac{a+1}{1-2^{-q}}+\frac{q2^{-q}}{(1-2^{-q})^2}\right],
\quad0\le a<q.$$

The endpoint translated law is the **actual cyclic convolution**
$\nu_{N,L}=\mu_{N,L}*w_q$. Source translation preserves total variation,
so PR #310's source/endpoint packet estimate gives

$$\boxed{\|\nu^{\mathrm{src}}_{N,L}-\nu_{N,L}\|_1
\le\frac1N\sum_{n=1}^N\frac8{8n+3}
\le\frac{\mathcal H_N}{N}.}$$

Here $\mathcal H_N=\sum_{n=1}^N1/n$ is the harmonic number, distinct from
any prescribed Fourier-band width. Keeping the first $M$ source packets,
normalizing at each actual time before averaging, costs an additional
$2\rho_M$, $\rho_M=(M+2)/2^{M+1}$. This holds for every bounded character
or primitive masked character; it does not bound unbounded logarithmic
observables. The implementation computes these finite source distributions
as exact rational integrals of the existing packet polynomials.

## 5. Exact primitive Fourier map, with the off-diagonal mode retained

Let $z=e(h/q)$. The full endpoint character is

$$\widehat\nu_{N,L}(h)=G(z)F_{N,L}(h).$$

The primitive and complementary characters are

$$P_{N,L}(h)=\sum_{k\text{ odd}}\nu_{N,L}(k)e(hk/q),\qquad
E_{N,L}(h)=\sum_{k\text{ even}}\nu_{N,L}(k)e(hk/q).$$

The elementary identity $\mathbf1_{k\text{ odd}}=(1-(-1)^k)/2$
proves the **nonfactorizing signed transform**

$$\boxed{
P_{N,L}(h)=\tfrac12\left[
G(z)F_{N,L}(h)-G(-z)F_{N,L}(h+q/2)\right],}$$

$$\boxed{
E_{N,L}(h)=\tfrac12\left[
G(z)F_{N,L}(h)+G(-z)F_{N,L}(h+q/2)\right].}$$

Both identities hold for all integer $h$, every $N,L\ge1$, with no
distributional assumption. For the true time-conditioned packet law, each
identity has additive error at most $\mathcal H_N/N$. The interaction is
now with an actual carry word; it is not the old scalar packet multiplier.
But the new term is exactly an **uncontrolled growing alias frequency**.

At $h=0$, the formula specializes to the rational scalar law

$$\boxed{\Phi_{N,L}=\frac49+
\frac19\cdot\frac1N\sum_{n=1}^N\mathbf1_{c_{n+L}\text{ odd}}.}$$

Thus scalar totient mass learns precisely one actual parity statistic. It
does not certify the remaining fifteen hexadecimal possibilities, two-digit
interactions, or any growing Fourier band.

For general modulus $q$ and a declared integer word law, the classical
Ramanujan formula would give

$$P(h)=\frac1q\sum_{k=0}^{q-1}c_q(k)
G(e((h+k)/q))F(h+k),$$

where $c_q(k)=\sum_{d\mid\gcd(q,k)}d\mu(q/d)$. This follows by the finite
Fourier expansion of the unit indicator. It is only an algebraic extension;
no alternate modulus is claimed to be the base-16 carry modulus. The
dyadic case above is the exact source-relevant two-term specialization.

## 6. The packet smoothing has a finite signed inverse

Let $S$ be cyclic translation of measures by $+1$. The generating function
identity $(2-z)^2G(z)=1$ proves

$$\boxed{(2I-S)^2\nu_{N,L}=
(4I-4S+S^2)\nu_{N,L}=\mu_{N,L}.}$$

It is an exact finite identity on $\mathbb Z/q$, not a limiting assertion.
The inverse has $\ell^1$ norm at most 9. At character level,
$1/9\le|G(z)|\le1$, so

$$|F_{N,L}(h)|\le9\left(
|\widehat\nu^{\mathrm{src}}_{N,L}(h)|+\mathcal H_N/N\right).$$

The complementary parity output is essential: the primitive projection
alone kills every even-support law. Preserving both outputs recovers

$$F_{N,L}(h)=(2-z)^2[P_{N,L}(h)+E_{N,L}(h)].$$

This proves a narrow **no automatic saving theorem for this grammar**:
the full packet translation is a boundedly invertible encoding of the
actual carry law. The primitive-only projection forgets information, and
its exact Fourier formula replaces that loss by the high-frequency alias.
Neither operation yields an unconditional selected Fourier inequality
stronger than one already supplied for the source. This does not rule out
a future arithmetic estimate for the aliased pair, nor a different
nonfactorizing coupling.

## 7. Hostile controls and exact receipts

**Same forcing, coherent changed seed.** Use $V_0=-\pi/16$, only as a
mathematical countermodel, not as a source input. Then $V_n=-T_n\in(-1,0)$,
so every literal carry is 15 and every $L$-word is $q-1$. The endpoint
translated totient mass is $5/9$, while the authentic finite history can
contain both parities. Its primitive character is

$$z^{-1}\frac{G(z)+G(-z)}2
=z^{-1}\frac{4+z^2}{(4-z^2)^2},$$

which has modulus at least $3/25$ on $|z|=1$. Thus real carry coupling
does distinguish this control, but does not force its characters to
cancel. The control does **not** refute a theorem explicitly requiring
the zero seed. It identifies where that selector must do additional work.

An exact rational test uses instead
$V_0=-\sum_{j=1}^{30}16^{-j}r(j)$. All states before the cutoff are in
$(-1,0)$, their carries are exactly 15, and $V_{30}=0$. This is a finite
control, not a universal statement about a rational-seed limiting orbit.

**Equal marginal digits, different joint characters.** The two uniform
word laws on $\{0,17\}$ and $\{1,16\}$ modulo 256 have identical high
and low hexadecimal digit marginals, and primitive mass $1/2$. Their
$h=1$ characters differ. With $\zeta=e(1/256)$ their difference is

$$\tfrac12(1+\zeta^{17}-\zeta-\zeta^{16})
=\tfrac12(1-\zeta)(1-\zeta^{16})\ne0.$$

This is an exact cross-digit counterexample, not a floating-point plot.
It survives packet convolution because that convolution is invertible.

**Projection loss.** Delta masses at residues 0 and 2 have identical
primitive projections (zero) but different $h=1$ characters modulo 16.

**Mutation.** Adding one to the exact authenticated forcing numerator
$B$ changes the decoded carry residue for every word, since $Q^{-1}$ is
a unit modulo $q$. The checker rejects this deliberate source mutation.

The new test file contains 14 targeted tests. Source identities use an
independent literal four-pole recurrence in the test oracle. Character
identities are checked exactly in
$\mathbb Q[X]/(X^{q/2}+1)$ for dyadic $q$, not by tolerance. The
production finite calculations use the existing integer source and packet
polynomials. No finite test is used to infer normality.

## 8. Earned result and the next arithmetic obligation

The result is a **genuine finite carry-conditioned construction and exact
information-loss theorem**, with a quantitative source-to-word transport.
It goes beyond time-only packet weighting by making a real carry word
load-bearing. The obligatory source, zero seed, odd conductor, complete
word, and higher-bit alias are all visible in the formulas.

The best proved selected modulus is unchanged by this front. The sharpest
remaining question for this specific construction is whether the
authentic source enforces a signed relation between
$F_{N,L_N}(h)$ and $F_{N,L_N}(h+16^{L_N}/2)$ strong enough to control
**both** parity outputs, at a declared growing $L_N$. Scalar primitive
mass, agreement of marginal digits, and smoothing by $G$ do not supply
that relation. Any proposed estimate must survive the all-15 control
because its proof uses the actual zero selector, not because the control
has merely been excluded by its label.

No canonical grading, normality, independence, or scholarly priority is
claimed. Classical inputs are finite Fourier inversion, Möbius/Ramanujan
projectors, and cyclic convolution; the source transport inputs are the
existing `SIGNED_GAMMA_BBP_GREEN_COHERENCE.md`,
`PI_SELECTED_PHASE_FORGE.md`, and PR #310
`OILY_TOTIENT_THIRD_SHADOW.md` dossiers.
