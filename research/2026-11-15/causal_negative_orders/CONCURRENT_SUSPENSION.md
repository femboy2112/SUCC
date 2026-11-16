# The literal forward path: reviewed companion draft #638

During the final publication check, the live repository acquired
[draft #638](https://github.com/femboy2112/SUCC/pull/638), **Principia ×
zeta: forward causal solenoid, Gamma suspension, and finite Pascal trivial
zeros**. Its head is `582e6bea90268b58262ac0f32e6ab23bfaae1951`, with
parent #636 at `397eec34c3637c876ab4e4f71f7c9a5359f75535`.

The root read its complete theorem file, Git blob
`2e91d846250c55fb62b462a80ae814cd36ba1d23`, before publishing this round.
Its code is not imported, its branch is not merged, and its reported
19 tests and independent oracle are not included in our validation counts.

## A precise realization of the user's path picture

The companion supplies a different, complementary meaning of reaching
negative integers. Begin with compatible finite successor clocks

$$L_N=\operatorname{lcm}(1,\ldots,N),\qquad C_N=\mathbb Z/L_N\mathbb Z.$$

The negative integer `-m` is represented at each finite level by the
nonnegative forward count `(-m) mod L_N`. These residues agree under
reduction. Their inverse limit lies in the profinite integer carrier
`Zhat`. This is a compatible arithmetic representation, not a limit of
positive real numbers becoming a negative real number.

To create an actual continuous path, add the explicitly declared
suspension

$$\mathscr S=(\mathbb R\times\widehat{\mathbb Z})/\Delta\mathbb Z,
\qquad(t,a)\sim(t+n,a+n).$$

Equivalently, give every profinite state an interval and glue
`(a,1)` to `(a-1,0)`. The forward flow is

$$\Phi_\tau[(t,a)]=[(t+\tau,a)],\qquad\tau\ge0.$$

It follows directly from the quotient relation that

$$\boxed{\Phi_m[(0,0)]=[(m,0)]=[(0,-m)]\quad(m\ge1).}$$

Thus positive elapsed time reaches the embedded negative arithmetic
coordinate in this declared compact solenoid. Finite clock projections
are `a-t mod L_N`, so the path is compatible with every clock quotient.
Its sign is an orientation convention of the seam; reversing the seam
reverses the endpoint label. Compactness or density alone does not pick
this gluing or build the path.

This construction preserves the user's proposed winding/return picture
more literally than identifying negative integration orders with
negative locations. The constructions have different types: the path
endpoint is a point of a compact suspension; `Phi_-m` in CN-01 is a
distributional operator supported at the original causal endpoint.

## A real reachability boundary

The diagonal integer action is properly discontinuous in the real
coordinate, so interval paths lift locally and then globally to
`R x Zhat`. The profinite coordinate of such a lifted path is constant,
because an interval is connected and `Zhat` is totally disconnected.
The path component of the origin therefore meets the profinite
transverse section exactly at the embedded ordinary integers.
The forward orbit alone meets that section at `-N_0`; the full path
component allows both directions and meets it at `Z`.

There are other profinite points, such as the compatible CRT thread
whose 2-adic component is one and whose odd-adic components are zero.
It cannot be an ordinary integer: divisibility by every power of three
would force it to be zero, contradicting its 2-adic component. It can
be approximated at every finite clock level without being reached by
a finite path from the origin. Approximation and path reachability
remain different even in this compact connected construction.

## Positive Gamma volumes concentrate on the endpoint

For fixed positive integers `m,k`, let `T_(m,k)` have Gamma shape `mk`
and rate `k`. This is a declared sum of positive exponential waits,
with mean `m` and variance `m/k`. Assume explicitly that the observable
is Lipschitz in elapsed time along this orbit:

$$|f(\Phi_\tau o)-f(\Phi_m o)|\le L|\tau-m|\qquad(\tau\ge0).$$

Then the variance identity and Jensen's inequality give

$$\left|\mathbb E f(\Phi_{T_{m,k}}o)-f(\Phi_m o)\right|^2
\le L^2\frac{m}{k}.$$

The volume therefore concentrates on the negative arithmetic endpoint
as `k` increases. The deterministic flow already reaches that point;
Gamma adds a coherent positive averaging law. Independence and the
waiting-time distribution belong to this chosen model, not to an
authenticated physical BBP sensor.
For `m=0`, use the point mass at time zero separately; a Gamma law
with shape zero is not defined.

## What the companion adds to the zeta comparison

Its finite Pascal formula is the same classical/inherited construction
recovered in CN-09. It also notes the exact normalization identity

$$\zeta'(-2m)=(-1)^m\frac{\Gamma(2m+1)}{2(2\pi)^{2m}}\zeta(2m+1).$$

The BBP face with `k=2m-1` has endpoint coefficient
`Gamma(k+2)=Gamma(2m+1)`. This matches a normalization constant in the
classical zeta slope formula. It does not identify the full BBP source
with the theta/Euler source, and the zeta functional equation is an
additional input. CN-06--09 go further in a different direction by
classifying the actual BBP real zeros and testing the same grade
aggregation on both sources.

Classical suspension background was checked in Nekrashevych's
[Groups and topological dynamics](https://people.tamu.edu/~nekrash/teaching/19S/chapter1.pdf).
The elementary quotient, path-lifting and variance arguments are
given above so the scope is directly reviewable. This appendix credits
the companion construction and supplies a read-only mathematical
review; it is not a second implementation or a claim to have run its
tests.

The adversarial follow-up reviewed the explicit quotient, endpoint,
path-lifting and Gamma-variance construction supplied by the root,
not the complete external theorem file. It confirmed the construction
with the three qualifications now explicit above: full path component
versus forward orbit, time-Lipschitz observables, and the separate
zero-time case. The root's complete-file review and this narrower
follow-up are recorded separately in `receipts/proof_review.json`.
