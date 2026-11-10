# Round 2 protocol: signed covariance without discarding the cross terms

Pinned parent: 1990b05117d84b33094c8e0f53f7d19b60f48060.
Pinned main: d32342d375f44ddf62221ad6aff2f534abdc0a03 (live fetch unchanged).
Original four-pole source and literal U0=0 are immutable. Work is additive
under this namespace, on the existing research branch and draft PR544.

## Rival hypotheses and measurements (before execution)

For z_n=e(h U_n), n in J=[A,2A), extend z by zero outside J. Define
C_l=A^-1 sum_(n=A)^(2A-1-l) z_(n+l) conjugate(z_n), and
E_H=(AH^2)^-1 sum_t |sum_(j=0)^(H-1) z_(t+j)|^2.
Then E_H=1/H+(2/H)sum_(l=1)^(H-1)(1-l/H)Re C_l.
The exact signed cross terms are retained. An independent sliding-window
sum checks this identity using the inherited outward integer rectangles.

Finite hypothesis SL2: E_H <= 2/H on the declared original-zero cases.
Also measure the unsigned replacement, the signed excess H E_H-1, |W|^2,
and the finite van der Corput upper bound (A+H-1)E_H/A. This finite threshold
is a falsifiable diagnostic, not an assertion for unbounded epochs.

Development epochs A=97,193. Holdout windows A=307,613,1229,2459; stress A=4919.
h=1,2,3,5. H in {2,4,8,16,32,64}, restricted to H<=A/4.
No tuning after development. These are fresh windows/parameters relative to
the prior round, not a separate physical dataset; the deterministic source
and interval implementation are shared. Some source times overlap prior data.

For the largest good prime p_A and m=ord_p(16), transport every lag l<H
when H<=m using k_l=h(16^l-1) and the EXACT forcing
F_l(n)=sum_(j=1)^l16^(l-j)r(n+j):
a_l,n=e(k_l[U_n]_p), v_l,n=e(k_l(U_n-[U_n]_p)+hF_l(n)).
Their product equals the full lag phase. Record the weighted bilinear
covariance, weighted marginal products, and deleted-endpoint contribution.
Independent rational sample checks must verify the phase identity, including
huge k_l, and an intentionally omitted forcing correction must fail.
No uncontrolled 16^H/A^2 approximation is allowed.

Controls: horizon-matched positive rational same-forcing seed with p_A and
3,5,7,11 principal parts unchanged, K=32 two-adic bits, eta=2^-20. Recompute
its full phase using exact seed transport. It must produce near-coherent
energy and reject SL2 at every H>=4. It is not one fixed nonnormal rational.
The coherent real seed -pi/16 and periodic completed orbits are handled by
proved controls in the hostile paper; finite samples do not certify pi tails.
Exact rational Gaussian-integer toy sequences validate signed/unsigned and
all-h distinctions; wrong four poles and nonzero initial boundary must fail
source authentication. Never use seed1/5 as a nonnormal counterexample.

PASS_FINITE requires the interval upper endpoint <=2/H; REFUTED_FINITE
requires lower endpoint >2/H; overlap is INCONCLUSIVE. All raw rectangles,
source/code hashes, seeds and failures are retained. No fitted asymptotic
exponent. A proof or exact counterexample is required for universal promotion.

## Independent fronts

Cube: exact cyclic cube decomposition, squared subgroup saving, degeneracy
floor and nonlinear observer dual atoms. See cube/PROTOCOL.md.
Chronology: causal prime-history laws, modular resonances, precision/memory
horizon and exact finite oracles. See chronology/PROTOCOL.md.
Hostile: all-epoch covariance-to-Weyl-to-normality audit, phase-corrected
signed-lag criterion, fixed-small-block necessity and wrong-source controls.

Agents share one model and source/BK inputs. Distinct proofs/algorithms are
recorded as such, never as external scholarly certification. New asymptotic
proofs are paper proofs unless a separately stated kernel check is executed.
Pi base16 normality OPEN; RH OPEN.
