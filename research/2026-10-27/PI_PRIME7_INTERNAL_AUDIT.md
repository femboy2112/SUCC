# Independent constructor audit of the primary-arithmetic lane

2026-10-27. Audited `PI_PRIME7_MODULAR_REAL_BRIDGE.md`. **PASS:** the local cancellation, exact 2/7 calibration, refinement identity, and character coefficient mappings are correct as stated with L>=2 and unit a. No real selected-cancellation claim is earned.

## Independent proof of the 2 sqrt(q) bound

This removes any need to rely on the precise scope of an external stationary-phase theorem.

On regular source disks 1,5,6 modulo7, the values of `(r,r',r'')` are `(5,0,1)`, `(1,0,2)`, `(2,1,2)`. These were independently recomputed from

    W=A'D-AD', W'=A''D-AD'',
    r'=W/D^2, r''=(W'D-2WD')/D^3.

On disk6, translation by delta=q/7 changes r modulo q by delta, so its sum vanishes for L>=2 and 7 not dividing a.

In either critical disk, Hensel gives a unique critical point c. The elementary p-adic Morse coordinate, proved in the constructor dossier, gives an isometric bijection t<->w of 7Z_7 with

    r(c+t)=r(c)+b w^2, b=r''(c)/2 a unit.

Thus its complete disk character sum equals

    e_q(a r(c)) * 7 * G_{7^(L-2)}(ab),
    G_m(v)=sum_{j modm} e_m(v j^2).

The factor seven is exact: t and w range over 7Z/7^L, and after writing w=7u the phase has modulus 7^(L-2), while u ranges modulo 7^(L-1). For L=2, use G_1=1.

For every odd modulus m and unit v, the invertible substitution `(j,k)->(j-k,j+k)` gives

    |G_m(v)|^2=sum_{s,t modm}e_m(vst)=m.

Each critical disk therefore has magnitude `7 sqrt(7^(L-2))=sqrt(q)`. Summing the two critical contributions proves the stated bound `2sqrt(q)`.

## Mirror and energy checks

The mirror constant c=89/120 is 7-integral, and c=5 modulo7. Only x=6 has both D(x) and D(c-x) units. Its mirror difference F has F'=2 modulo7. The delta=q/7 translation has quadratic Taylor error divisible by q exactly when L>=2; denominator-unit hypotheses make all Taylor coefficients 7-integral. Therefore the exact mirror sum vanishes.

On regular disks1 and5, A' is a unit and their A-value residues are respectively5 and2, so they generate two disjoint collections of q/7 singleton regular fibers. Their mirror partners are excluded pole disks4 and0. On disk6, A'=0 modulo7 and r'=1 modulo7. The same translation preserves each A-fiber and rotates its source phase by e_7(a). Hence every central fiber sum vanishes. The unnormalized energy is exactly2q/7, and N=mq yields normalized energy2/7. The scalar normalized bound is2/sqrt(q), with no missing factor m or q.

Independent exact coefficient-count verification passed L=2,3,4,5. The respective singleton counts were14,98,686,4802, and the nonempty central balanced-fiber counts were1,4,22,151. Counts were checked by cyclotomic exponent multiplicities, with no floating cancellation.

The L>=2 restriction is necessary for these exact vanishings: at L=1 the mirror-regular disk has one point and its character sum is1; the unnormalized A-energy is3, not2. Thus the first-depth false mutation is rejected.

## Refinement audit

For N>=1, parent sum S=sum_i u_i, and p child bins, exactly

    p sum_i|u_i|^2-|S|^2=sum_{i<j}|u_i-u_j|^2.

Multiplying by p^L/N^2 proves the dossier's refinement identity at every N, including incomplete blocks and empty children. No balancing hypothesis is needed. Independent integer-valued Gaussian-weight checks passed N in {1,2,3,6,7,8,10,48,50,199}, L in {1,2}. The same argument with p replaced by M'/M proves ordinary time-residue monotonicity whenever M divides M'.

For precision in comparing with empirical conditional expectation: if a bin contains n_b observations, its contribution is multiplied by q n_b/N in the PR325 energy relative to the conditional-expectation norm. On complete periods this equals the exact fiber multiplicity m_L(b), explaining the ramified-fiber overweight. For arbitrary incomplete samples, use the exact multiplier rather than a blanket comparative claim.

## Character coefficient audit

For positive denominator B prime to7, R=A B^{-1} modq and K=(BR-A)/q give both identities correctly:

    e(hu/q)=e_q(hR)e_B(-hK),
    e(hu)=e_B(-hqK),  h integer.

The missing factor q is explicitly retained in the second identity, and the integer R disappears. Example u=1/2,q=7 gives R=4,K=1: the complementary sign transforms e_7(4) into e(1/14), while e(u)=-1 is wholly complementary to the trivial genuine7-local factor.

For reduced denominator7^v d, the CRT identity is also correct: `d s+7^v t=1 mod(7^v d)` for the specified inverses, hence

    e(hu)=e_{7^v}(hAs)e_d(hAt).

At modulus1, take its character as1; no invertibility convention at modulus1 is needed beyond that harmless convention.

The final translation-defect bound is the triangle inequality applied to the exact identity `sum(z_tau-lambda z)=(1-lambda)sum z`. It is a strong sufficient matching condition, not a consequence of scalar cancellation. The dossier labels that limitation correctly.

## Verdict

No load-bearing error found. Pole exclusions, L=2 Taylor threshold, stationary-phase conductor, A-fiber weights, and real/modular coefficient mapping all check. The elementary Gauss proof above is preferable as the internal proof because it shares already established local hypotheses and avoids importing unnecessary theorem scope. Selected real Weyl cancellation remains unproved.
