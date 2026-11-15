# The next attack: signed winding, with the finite source retained

## The exact joint statistic

Keep M_n=floor(U_n+1/2), epsilon_n=U_n-M_n, and
K_n=M_(n+1)-16M_n. The event to be forced is precisely

\[
\begin{aligned}
A_n={}&1_{\{K_{n-1}\equiv2\ (4)\}}\\
&+1_{\{K_{n-1}\equiv1\ (4),\ \epsilon_n\ge0\}}\\
&+1_{\{K_{n-1}\equiv3\ (4),\ \epsilon_n<0\}}.
\end{aligned}
\]

A positive lower shell bound for any one of these three disjoint cells is
sufficient. A bound for their sum is exactly the attacked gate. Merely
renaming that sum a coupling or excitation theorem does not advance it.

Equivalently, the exact clock/cofactor formula is

\[
i^{C_n}=i^n\chi_4(-y_n),\qquad
A_n=0\iff[y_n]_4\in\{n,n+1\}\pmod4.
\]

The half-plane to exclude is therefore an explicit two-residue band tied
to the authentic clock. The low-bit recurrence alone feeds the unknown
real carry straight back into this identity.

The fixed-precision controls make the joint issue sharper. For any matching
depth L>=2 their carries are all congruent to three, while their authentic
clock residue is n modulo four. Hence their fractional cofactors satisfy
\([\widetilde y_n]_4=n+1\pmod4\). Both the clock and cofactor residues
separately cycle uniformly through all four values, but their exact joint
correlation gives w=1 at every positive index. Separate marginal uniformity
therefore does not exclude this band. These controls change the finite
source law; the needed restriction must come from the original joint law.

## A finite arithmetic form that retains all four poles

For n>=1 let L_n=lcm(1,3,5,...,8n-1), with L_0=1. The reduced denominator
of U_n divides L_n. To see this directly, combine the two even-denominator
terms of r(n):

\[
-\frac2{8n-4}-\frac1{8n-2}
=-\frac{3n-1}{(2n-1)(4n-1)}.
\]

The two factors on the right are coprime odd integers; the other pole
denominators are odd and at most 8n-1. Each reduced denominator thus divides
L_n. Define a_n to be the integer in [0,L_n) satisfying y_n=a_n/L_n.
These representatives obey the exact growing-modulus recurrence

\[
\boxed{
a_n=\left[
16\frac{L_n}{L_{n-1}}a_{n-1}+L_n r(n)
\right]_{L_n},\qquad a_0=0.
}
\tag{N1}
\]

Here [.]_(L_n) means the least nonnegative integer remainder. Every term
inside the bracket is integral. The target cofactor is

\[
[y_n]_4=a_n L_n^{-1}\pmod4.
\tag{N2}
\]

Thus a source-specific approach can work on the exact residue/sign system
(N1)-(N2), or the equivalent winding cells, while explicitly retaining the
finite pole law and its odd-denominator restrictions. This is an exact
coordinate reduction, not a distribution estimate. Dropping the least
remainder operation loses the real branch information that selects C_n.

## Three pass/fail requirements for a proposed estimate

1. **Seed selection.** State where U_0=0 enters. If every operation first
   applies a filter P(E) with P(16)=0, the homogeneous seed term is gone.
   The same-forcing Thue–Morse control then tests whether an asserted
   signed conclusion is actually independent of that seed.
2. **Finite source rigidity.** Retain a feature that the Mahler controls
   cannot satisfy: the literal finite rational source, specified four
   poles and coefficients, and its resulting arithmetic restrictions.
   Any fixed number of authentic low dyadic bits is insufficient, even
   when matched at every index.
3. **Rate and orientation.** Prove a fixed margin on every sufficiently
   late B-shell. The extensive echo already supplies a nonzero response;
   its bounded reference supplies the correct orientation as an observable.
   The new theorem must bound that signed mean, not repeat either identity.

The original gate would close if such an estimate gave
sum_(B<=n<2B) A_n >= delta B with fixed delta>0. A derived sublinear lower
bound for this particular A_n would still be a distinct weaker result and
must be reported with its actual rate. This round obtained neither such
count estimate; it obtained the explicit instruments and premise tests.

## Keeping R0 as an alternative objective

The chosen fourth-root event is sufficient but stronger than R0. If its
orientation is unnecessarily restrictive, a positive shell density of
nonzero nearest-integer windings would directly imply R0 by the packet
inequality in WINDING_PACKETS.md, without selecting these three cells.
That alternative rate is also unproved here. It should be pursued only if
the proposed source estimate naturally controls it; replacing the named
gate without reporting the change would obscure the research outcome.
