# Source-Gamma completion by finite compensating packets

**Source:** child of original signed-source draft PR #164 at `0fa1fb4e05acbed9bee48f865ddf7e9933f049dc`, frozen Suzuki Git blob `0cc8510b71d178fc79e8d410a86d8b6014cf9178`. **RH PROVED: NO.** All claimed signed source tests are gated against the exact inherited original source and verified via hosted CI; no nontrivial zero ordinate enters.

## Steelman

The user's "modes occur in groups that cancel, so the fifth mode is technically incomplete" admits two distinct mechanisms. (i) Finite low Legendre subspaces fail to see off-diagonal coupled directions: Q(e1)>0 and Q(e2)>0 need not imply Q(e1-e2)>0. Exact counterexample A=[[1,2],[2,1]] gives Q(e1-e2)=-2. This is a **synthetic signed Gram**, never an original Weil sign. (ii) The genuine completed Gamma is a positive sum of OU/Fourier rungs. The original sign flip in the fixed fifth-mode witness at J=64 shows the missing tail compensates for negative source components. Gamma rungs themselves are nonnegative, not opposing each other.

## A rigorous finite packet theorem (new-to-project certificate)

Fix lawful endpoint-zero u in H1_0(-1/2,1/2), *the same u throughout*. Let G_j(u)>=0 be the genuine real Gamma rung energies and q_J=Q_0(u)+sum_(j<J) G_j(u). The inherited exact source bounds for T_J=sum_(j>=J)G_j(u), d_J=4J+1, are

L_J = 2||u||²/d_J² - [4/d_J^4+64/d_J^5]||u'||² <= T_J
<= U_J = [2/d_J²+16/d_J³]||u||².

Therefore, for any J>J0,
P_(J0,J) := sum_(J0<=j<J)G_j(u) = T_J0-T_J >= L_J0-U_J,
and Q_J(u) >= q_J0^lower + L_J0 - U_J.

Suppose the original frozen signed source reports q_J0 in [l,h], h<0, and l+L_J0>0. Since U_J decreases to 0, there exists **a finite J** for which l+L_J0-U_J>0. Our exact integer bisection returns the **smallest J licensed by this particular rational sufficient inequality**, not the first real source crossing. The data-scoped original case is J0=64, u=6P1(2t)-10P3(2t)+4P5(2t) and ||u||²=2136/77, ||u'||²=1296. Its original interval comes exclusively from `authentic_fifth_mode_completion(64)`.

The finite packet strictly repairs that **same source direction**. It does not certify positivity of the whole five-dimensional span, of the original S4 Schur correction, or of the signed Weil form at every radius.

## Key falsifiers / controls

- Source SHA, genuine prime2 half-density, one real Gamma, original contact and both poles are inherited and checked by parent source adapter, not independently reconstructed.
- Any wrong/absent source, interval with h>=0, missing positive completed margin, invalid H1 norm, floats, or bounded-budget failure must fail closed.
- An arbitrary positive covariance/diagonal Gram cannot replace the signed source.
- The packet stops are nested in Gamma truncation **not arbitrary reordering**, so no conditional-convergence rearrangement trick.
- Numerical source samples are not proof; every sign conclusion uses Fraction and the archived original outward interval.
- The inherited Gamma tail estimates depend on endpoint-zero extension; they must not be applied to arbitrary L2 vectors.

## Next independent holdout

Compute the actual original Q_J interval via `authentic_full_low_entry` at one independent Gamma depth near the certified bound, and verify the predicted positive sign without using the packet construction to fit that test. Next explore whether reflection parity and authentic prime-edge partial-shift eigenspaces yield useful almost-invariant packets under the Gamma OU operator. Do not assume the OU and prime swap commute: that commutator is a falsifiable obstruction. External originality unassessed; the fundamental tail inequalities are inherited classical/Fourier facts.

## 5. Decisive packet-no-go: true prime-edge swap does NOT commute with even the first Gamma OU rung

**GPK-06 [PAPER PROVED + EXACT ORIGINAL SOURCE GATE].** Let `b=log 2` (source certifies `5/8<b<3/4`), `I=(-1/2,1/2)`, and `A_b=T_b+T_-b` with zero extension. Let `E_alpha` have kernel `exp(-alpha|x-y|)`, original first real Gamma rung `alpha=1/2`. Choose the legal `f=1_[-1/8,1/8]` (primitive-space L2 test; smooth center approximants exist). Because the support lies strictly in the unshifted center, `A_b f=0`. At `x=-3/8`, `z=x+b in (1/4,3/8)`, while `y in [-1/8,1/8]`. Hence `0<z-y<1/2` and `exp(-(z-y)/2)>1-(z-y)/2>3/4`. Therefore

```
[A_b,E_(1/2)]f(-3/8)
 = (A_b E_(1/2)f)(-3/8) - (E_(1/2) A_b f)(-3/8)
 > (1/4)(3/4) = 3/16.
```

The expression is continuous near the chosen point, so the commutator is nonzero as an L2 operator, not just one anomalous point value. Since the original Gamma rung is `4 I-E_(1/2)`, it too fails to commute with the true prime partial shift. **Thus independent prime-swap eigenmode packets cannot generally be invariant Gamma packets**; diagonally grouping those modes and declaring independent cancellation is invalid. Reflection parity still commutes with both operators, and remains a mathematically legitimate coarse split. This supports studying off-diagonal compensated packets *within parity sectors* rather than inventing a universal simultaneous eigenbasis.

Exact rational geometry and strict `3/16` proof are in `observational_succ/prime_gamma_packet_commutator.py`. Source adapter pins original Git blob, genuine prime2 and log2 interval. This noncommutation theorem is **not** a negative Weil quadratic witness, does not decide S4, and does not alter the valid positive Gamma packet result.

**Independent Q_189 evaluation remains a source-access gap:** the inherited `authentic_full_low_entry` adapter routes through a Gamma cutoff guard `J<=75`. A direct high-J original-source holdout requires an independently extended exact analytic evaluator and fresh provenance/interval controls; do not bypass the guard by silently altering historical code.
