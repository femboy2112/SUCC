# Exact joint-source and shifted-numerator collision laws

2026-10-27. Root derivation with independent internal algebra audit. **Status: paper proof; not a selected real cancellation bound.** All inputs are affine residues modulo q=p^L, p prime at least7, L>=1. Counts are ordered pairs. This theorem neither invokes the SUCC zero seed nor controls real selected phases.

Set

    A(x)=120x^2-89x+16,
    D(x)=(2x-1)(4x-1)(8x-7)(8x-3),
    H(x)=930A(x)-1243,
    c=89/120.

## 1. Exact identities

The following polynomial identities hold over Q:

    3375D(x)=120A(x)^2+2746A(x)-3781-8xH(x),             (1)
    D(x)-D(c-x)=-(240x-89)H(x)/50625,                  (2)
    16H(x)=31(240x-89)^2-27359,  27359=109*251.         (3)

They were independently verified coefficient by coefficient with exact Fraction arithmetic, including composition at c-x. These constants are not numerical fits. Formula (2) also follows immediately by applying (1) at x and c-x, since A is mirror-invariant and `x-(c-x)=(240x-89)/120`.

## 2. Equivalent joint-collision system

Let

    u=x-y, v=120(x+y)-89.

The affine transformation (x,y)->(u,v) has determinant240, a unit for every p>=7, hence is bijective modulo q. Numerator equality is exactly

    A(x)-A(y)=uv=0 modq.

Once A(x)=A(y), identity (1), and the invertibility of 3375 and 8, show that D(x)=D(y) is equivalent to

    u H(x)=0 modq.

Moreover `240x-89=v+120u`, so (3) becomes

    16H(x)=31(v+120u)^2-27359.                         (4)

Thus the supplied two-congruence description is exact; no cancellation by a possible nonunit u is being made.

## 3. Generic primes and p=31

The case u=0 contributes precisely q diagonal pairs. For nonzero u modulo q put a=v_p(u), so 0<=a<L. The equation uv=0 forces v divisible by p^(L-a).

If a>=1 then v is divisible by p, and (4) gives

    16H(x)=-27359 modp.

At p not in {109,251}, H is therefore a unit, contradicting uH=0. Hence all generic off-diagonal solutions have u a unit. They consequently satisfy v=0 modulo q and

    31*120^2*u^2=27359 modq.                           (5)

At p=31, H is already a unit for every x because H=-1243=-3 modulo31. There are no off-diagonal pairs, so the count is q at every depth.

For p>=7 excluding31,109,251, the right side of (5), divided by its unit coefficients, is nonzero modulo p. There are no roots if 27359/31 is a quadratic nonresidue modulo p. If it is a quadratic residue, there are exactly two simple roots modulo p, each having a unique Hensel lift to every p^L. The square120^2 does not affect the residue criterion. Each root u, together with v=0, determines exactly one ordered pair (x,y).

Therefore the joint (A,D) collision count is

    q+2  if 27359/31 is a quadratic residue modulo p,
    q    otherwise,

with the stated exclusions and with p31 separately giving q.

## 4. The exceptional primes 109 and 251

Both divide 27359 to valuation exactly one. If u were a unit, v=0 would make the first term in (4) a unit while 27359 is divisible by p, so H would be a unit, impossible. Thus a>=1, and v is also divisible by p. Then `(v+120u)^2` is divisible by p^2, while 27359 has valuation one. Consequently

    v_p(H(x))=1

exactly. The condition uH=0 now forces a=L-1. This is impossible when L=1; when L>=2 it is also sufficient provided v is divisible by p.

There are p-1 possible u of valuation L-1 modulo p^L and p^(L-1) possible v divisible by p. Thus the total ordered collision count is

    L=1:   q,
    L>=2:  q+(p-1)p^(L-1).

A more explicit fiber description follows. Let b=89/240 modulo p. Outside the residue disk x=b modulo p every joint fiber is a singleton. Inside this disk, for L>=2, two inputs have the same joint image exactly when they agree modulo p^(L-1). Hence there are p^(L-2) fibers of size p, and all remaining fibers are singletons. This directly corroborates the count and gives an additional finite calibration.

## 5. Any shifted second numerator

For any integer shift s, including zero and negative shifts, let

    k=min(v_p(s),L), taking k=L for s=0.

The two numerator congruences are equivalent to

    uv=0 modq,  240s u=0 modq,

because the second difference is `u(v+240s)`. Since 240 is a unit, a nonzero u of valuation a is allowed exactly when a>=L-k. For each such a the product condition admits

    (p-1)p^(L-a-1) * p^a = (p-1)p^(L-1)

pairs (u,v). There are k such strata; u=0 again contributes q. Therefore

    #{(x,y): A(x)=A(y), A(x+s)=A(y+s) modq}
       =q+k(p-1)p^(L-1).

In particular a unit shift is exactly injective at every depth. A shift divisible by p is not; the probe includes this false-injectivity control.

## 6. Energy scope warning and optional bound

At generic primes with two off-diagonal pairs, grouping any bounded weights by the joint (A,D) labels differs from time-residue energy by one signed cross term, hence by at most `(2/q)(1+q/N)^2`, as in the root claim.

That O(1/q) comparison must NOT be extended to the exceptional primes. For coherent weights on complete periods their joint energy equals `2-1/p`, while ordinary time-residue energy equals1. The difference persists at every L>=2.

Nevertheless the explicit exceptional fiber description yields, for arbitrary complex weights and L>=2,

    G_AD(N,p^L) >= E(N,p^(L-1)),

where both energies use their respective modulus in the usual prefactor. To see this, group all p children of every residue modulo p^(L-1). On the critical disk G_AD assigns q times the squared grouped sum, which is p times the corresponding coarse contribution. Elsewhere it assigns q times the sum of child squares, at least (q/p) times the squared grouped sum by Cauchy--Schwarz. Summing proves the bound. Thus the existing prescribed moving-energy counterexample also obstructs a universal normality-implies-G_AD-decay claim at these exceptional primes by applying it to the schedule q/p.

The exact refinement identity from the primary lane applies to the scalar A-label tree, which has p children per parent. It should not be indiscriminately applied to joint (A,D) labels with normalization p^L: a joint parent can split into more than p different joint child labels. For example the generic complete-period joint energy1+2/p^L decreases with L.

## Exact probe and receipt

`pi_joint_source_observation_probe.py` uses only the Python standard library. It verifies all polynomial coefficients exactly and exhaustively checks finite joint collision counts at primes7,11,13,17,19,23,29,31,37,41,43,109,251, with multiple depths. In particular it checks the exceptional primes through p^2 and p31 through p^3. It also checks the shifted-numerator formula for zero, positive, negative, unit and p-divisible shifts.

All checks passed. The receipt is `pi_joint_source_observation_receipt.json`. The proof above establishes all levels independently of those finite checks. No unsupported constant, pole deletion, or division by a potentially nonunit difference remains.
