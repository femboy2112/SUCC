# Scott-domain relativistic defect: certified information, invariant arithmetic, and the Goldbach cylinder

**2026-11-12 · Research addendum to `../prime_fixedpoint_cylinder/` · additive, not a proof of Goldbach.**

## Executive verdict

The user's hypothesis has a provable **relative information** interpretation, but its literal **arithmetic** interpretation is refuted: the integer defect `b(n)=max(Omega(n)-1,0)` is invariant under all sound factorization histories. What changes with the observer's computational path is the *certified interval* around it, not its value. Scott domains make this a natural exact theorem. The defect is simultaneously the number of genuine nontrivial binary splits in **every** complete prime-normalizing factorization tree. It is not removable by beta-conversion or a gauge change. On the arithmetic cylinder the corresponding source-dependent phase averages annihilate composites exactly, but existence of a surviving zero mode is still the Goldbach conjecture. This note defines an explicit Scott domain, a Scott-continuous global evidence operator with a constructive least fixed point, a source-faithful prime transport, and finitary Goldbach observers with falsifiers.

**Grounding:** `AGENTS.md`, `docs/METHOD.md`, `docs/ARCHITECTURE.md`, `docs/PI_NORMALITY_FRONTIER.md`; prior local package in `../prime_fixedpoint_cylinder/` and `../prime_interferometer_legacy/`. External domain theory: Abramsky & Jung, *Domain Theory*, §§2.1–2.2, https://www.cs.famaf.unc.edu.ar/~mpagano/cursos/dominios/libros/abramsky-jung-domain-theory.pdf ; Abramsky, *Domain Theory in Logical Form*, https://www.cs.ox.ac.uk/people/samson.abramsky/dtlf.pdf . Chen's theorem is an external classical import, not established here.

## SCD-01 (PROVED LOCAL): all complete factorization paths have identical split degree

Let `m>=2`. A *legal binary factorization tree* has root `m`; each internal node with value `u` has two children `a,b>=2` with `ab=u`; each terminal leaf is a prime. Write `s(T)` for the number of internal binary splits. Product of the prime leaves is `m`, so by unique factorization their total number, including multiplicity, is `Omega(m)`. Every finite full binary tree satisfies `#leaves = #internal nodes + 1`; hence

`boxed(s(T) = Omega(m)-1 = b(m))`.

This does not depend on splitting order, syntactic beta steps, branch scheduling, or the shape of the tree. For example `60 -> (2,30) -> (2,2,15) -> (2,2,3,5)` and `60 -> (6,10) -> (2,3,2,5)` both have exactly three binary splits. Administrative beta reductions can be arbitrarily many and are **not** counted: only source-authenticated nontrivial factor splits contribute to this grade.

Consequently, the integer defect cannot be a mere byproduct of *path relativity*: every **completed** path has the same defect. The relative quantity is how much of that invariant has already been certified.

## SCD-02 (PROVED LOCAL): finite information trees form a Scott domain

For each `m>=2`, define a finite rooted *partial factorization tree* recursively:

- `?m` is an unresolved leaf, no arithmetic claim beyond the label `m`.
- `[p]` is a leaf carrying a valid finite primality certificate for `p`. Our executable demonstration checks it by trial division through `floor(sqrt p)`; other sound certificates may be substituted.
- `Split(u;T_a,T_b)` is an internal node with `a*b=u`, `a,b>=2`, and partial subtrees at `a,b`.

Write `T <= T'` when `T'` is obtained by resolving some unresolved leaves, never discarding or changing already recorded certificates. Different first splits can be incompatible: `Split(60;2,30)` and `Split(60;6,10)` need not have a common refinement under this *literal tree* order. They remain semantically equivalent upon forgetting branch structure and retaining the prime multiset.

The set `D_m` of partial trees is a finite pointed poset (`?m` is bottom). Any family with an upper bound has a unique least upper bound: recursively merge compatible recorded nodes. In a finite poset every directed subset has its greatest element; every element is compact. Hence `D_m` is a bounded-complete algebraic dcpo (a finite Scott domain).

The global domain `D = product_(m>=2) D_m` with coordinatewise information order is a bounded-complete, **omega-algebraic** pointed dcpo. Its countable compact basis is given by finite-support assignments of partial trees; arbitrary increasing chains have coordinatewise suprema. This is a genuine infinite Scott domain accommodating a finite-program observer that refines arbitrarily many integers over unbounded mathematical execution time.

**Typing caveat:** the local `refine_once` routine makes an eager branch choice. It is order-increasing along its own run, but need not be monotone between *incompatible* input trees. It is **not claimed Scott-continuous on all `D_m`**. The separately defined global Horn closure operator in SCD-05 is monotone and Scott-continuous.

## SCD-03 (PROVED LOCAL): effective interval for computational defect

Given a partial tree `T` of value `m>=2`, let `P(T)` be the count of certified prime leaves and `U(T)` the multiset of unresolved leaf labels. Define

`L_Omega(T)=P(T)+|U(T)|`,

`U_Omega(T)=P(T)+sum_(u in U(T)) floor(log_2 u)`.

Every unknown integer `u>=2` has at least one prime factor and at most `floor(log_2 u)` prime factors counted with multiplicity. Therefore

`boxed(L_Omega(T) <= Omega(m) <= U_Omega(T)).`

When an unresolved `u` is split into `a*b`, the lower bound increases by exactly one; the upper bound does not increase because `floor(log_2 a)+floor(log_2 b) <= floor(log_2(ab))`. When an unresolved prime is certified, the lower bound stays fixed and the upper bound becomes 1. Consequently every legal refinement `T <= T'` yields

`[L_Omega(T'),U_Omega(T')] subseteq [L_Omega(T),U_Omega(T)]`.

At any fully certified normal form `T*`, both endpoints equal `Omega(m)`; for `m>=2` subtract one to obtain the nested certified defect interval `[L_b(T),U_b(T)]` for `b(m)`. For the unit `m=1`, set `b(1)=0` separately.

**Concrete relativity:** with no tests, `?9` gives `b(9) in [0,2]`. After recording `9=3*3`, both endpoints collapse to `1`. The arithmetic defect did not change. An observer with only the first trace cannot claim that 9 is prime simply because the *lower* defect is 0.

The interval map from each finite `D_m` into the interval-information order (reverse inclusion) is Scott-continuous. Each fixed-coordinate map on the product `D` is Scott-continuous, so finite collections of such measurements are Scott-continuous as well. Exact per-integer convergence does **not** give a uniform bound on discovery time over all integers.

## SCD-04 (PROVED LOCAL): a Scott-natural prime-birth commutator

For a genuine prime `p` and `m>=2`, transport a partial tree `T in D_m` into `D_(pm)` by the *certified* root split `pm=p*m`, with the left child the prime certificate `[p]` and the right child the **same** carried subtree `T`. Denote this lifting `Vhat_p(T)`.

It is monotone and Scott-continuous: all certificates of `T` remain intact, and its refinements are preserved within the transported subtree. The number-of-factors interval obeys

`[L_Omega(Vhat_p T),U_Omega(Vhat_p T)] = [L_Omega(T)+1,U_Omega(T)+1]`.

Therefore for the defect interval,

`boxed(I_b(Vhat_p T) = I_b(T) + [1,1], m>=2)`.

For `m=1`, transporting the unit to `p` gives grade zero (the vacuum exception). The terminal-state version is the SUCC/FUCC identity from the cylinder dossier:

`[B,V_p] = V_p (I - |1><1|)` on finite-support vectors, `B|m>=b(m)|m>`.

**Information provenance is load-bearing.** If the observer multiplies an unexamined `m` by `p` but discards the proof tree, the new bottom trace `?(pm)` gives a looser interval, and a naive *observed* commutator can be 0 or undefined. This is not genuine arithmetic holonomy. Carrying the original proof evidence restores the exact diagram. No `p`-adic clocks or RH statements are imported by this fact.

## SCD-05 (PROVED LOCAL): a genuinely Scott-continuous omega observer

Let `Facts` be the countable syntax of finite trial-division facts `seen(n)`, `tested(n,k)`, `prime(n)`, and `composite(n,d)` (with `n>=2`). Consider the powerset Scott domain `E=P(Facts)` ordered by inclusion, bottom empty, compact elements the finite subsets.

Define the inflationary one-step rule operator `Phi:E->E` by adding `seen(2)` and applying all these **finitary** Horn rules to facts already in `X`:

1. `seen(n)` yields `seen(n+1)` and `tested(n,1)`.
2. `tested(n,k)` for `k<floor(sqrt n)` yields `composite(n,k+1)` if `(k+1)|n`, else `tested(n,k+1)`.
3. `tested(n,k)` for `k>=floor(sqrt n)` yields `prime(n)`.

The arithmetic conditions in rule 2 are evaluated by exact integer division. The soundness statement concerns only the chain generated from `X_0=empty`, not adversarial arbitrary sets of counterfeit `tested` facts. Every rule has one finite premise, so `Phi` preserves directed unions; it is Scott-continuous and inflationary. Kleene's theorem gives the least fixed point

`boxed(E_infty = lfp(Phi)=union_(t<omega) Phi^t(empty)).`

For each fixed `n`, `seen(n)` arrives after finitely many stages. Trial division up to `floor(sqrt n)` then yields a sound `prime(n)` or a proper divisor certificate, also after finitely many stages. Thus the single finite program represented by `Phi` eventually enumerates **every** genuine prime and classifies every integer. It runs through unbounded natural-number registers; there is no assertion that infinitely many real-world steps finish or that one finite lambda term beta-reduces to an infinite completed numeral.

The first-order arithmetic rules can be encoded as a recursive evaluator; the executable demonstration uses standard-library integer operations rather than claiming a typed Lambda–Haar compiler lowering has already been verified. **Finite representation of an observer is not universal proof of a positive property of every Goldbach midpoint.**

## SCD-06 (PROVED LOCAL): Scott-lifted cylinder gives monotone certified Goldbach intervals

For midpoint `n>=2`, let `d=0,...,n-2`, endpoints `a=n-d,b=n+d`, and partial endpoint trees `T_a,T_b`. Their true cylinder grade is `h_n(d)=b(a)+b(b)`. Form its sound interval by adding the defect intervals:

`[ell_d,u_d] = I_b(T_a)+I_b(T_b)`.

Since grades are nonnegative integers,

- `u_d=0` **certifies** a prime pair (both defects must be 0).
- `ell_d>0` **refutes** a prime pair at that displacement.
- `ell_d=0<u_d` is **unresolved**; it is not a prime-pair witness.

Define `L_G(n)=sum_d 1[u_d=0]` and `U_G(n)=sum_d 1[ell_d=0]`. They satisfy the exact inequalities

`boxed(L_G(n) <= G(n) <= U_G(n))`.

As any endpoint trace refines, `L_G` cannot decrease and `U_G` cannot increase. When the finitely many endpoint trees for `2,...,2n-2` are complete, the bounds coincide exactly with `G(n)`. The predicates `L_G(n)>0` (one certified witness) and `U_G(n)=0` (a certified failure for that specific midpoint) are finite-evidence/Scott-open events. For all **fixed** `n` the process terminates because all relevant integers admit finite primality or factorization certificates.

The original cylinder's exact angular projector `P_0=(1/2pi) int_0^(2pi) exp(i theta H_n)dtheta` is not a computer that fills in unknown endpoint grades. Its certified Scott approximation is the interval `[L_G,U_G]`. Any algorithm that replaces unresolved grades by zero and then claims a positive projector trace is UNSOUND; the test `?9` witnesses the problem.

**Example:** for target `20` (`n=10`), displacement `d=3` is `(7,13)` with grade 0; `d=1` is `(9,11)` with grade 1; `d=0` is `(10,10)` with grade 2. At bottom information every `d` is a *possible* grade-zero candidate, but none is certified. With completed certificates, exactly two unordered prime-pair witnesses remain.

## SCD-07 (CLASSICAL COROLLARY / OPEN SOURCE GAP): Chen is not a defect-collapse rule

Chen's theorem guarantees for every sufficiently large `n` some midpoint displacement with `h_n(d)<=1`. This states the **existence of an arithmetic state** of grade 0 or 1. Scott continuity lets an observer eventually *discover which* grade a **given** endpoint has, but it gives no transition forcing a defect-1 Chen state to grade 0 **at the same midpoint**. Rewriting `9=3*3` into an equal-valued expression never makes 9 prime. A proposed reduction `P_<=1 -> P_0` therefore requires a new source-dependent prime correlation or additive transport theorem; it is not justified by computational path equivalence.

The Goldbach assertion `forall n>=2, G(n)>0` is a countable conjunction of individually decidable local statements. Generic Scott/domain fixed-point principles do not turn all instances into a finite uniform theorem. A source-alphabet counterfeit (`S={p prime : p congruent 1 mod 4}`) retains a valid freely factorized primitive sector and complete normalizing observer but has **no** midpoint witnesses when `2n divisible by 4`. Thus *source-blind* fixed-point/topology arguments cannot prove Goldbach, even though full rational-prime-specific arithmetic might.

## SCD-08 (PROVED LOCAL NO-GO): phase from a path potential is flat

If an oriented arrow `x->y` receives a phase `exp(i theta (b(y)-b(x)))`, the product around any closed composable cycle is exactly 1 by telescoping. Different complete factorization routes have identical net `b(m)` by SCD-01. This is a pure-gauge (gradient) phase assignment and supplies no nontrivial curvature, quantum speedup, or positive witness count. A genuinely new twisted-cylinder mechanism needs a **source-derived non-gradient** cocycle, an operational transport basis, and a quantitative overlap estimate that survives parity/CRT controls; arbitrary rotation factors are insufficient.

## Falsifiers, status and next experiment

- **Verified algebraically in the stated model:** SCD-01..06 and SCD-08 as mathematical derivations (no formal kernel or external blind review). Their finite program checks are `TESTED MODEL`, not universal proof receipts.
- **External theorem used:** Chen's theorem, only for `min h<=1` at sufficiently large midpoint.
- **REFUTED:** `b(m)` itself is a path-dependent artifact; product-preserving beta-equivalences can turn composite `m` into a prime. Receipt: `60` has different paths but `Omega(60)=4`, hence `b(60)=3` in both; evaluation preserves primality.
- **REFUTED:** an unresolved zero *lower* grade proves a prime pair. Receipt: `?9` has lower grade 0 while 9 is composite.
- **UNVERIFIED:** any uniform source-specific inequality forcing `L_G(n)>0` for all sufficiently large `n` without doing direct primality tests or already counting witnesses; and any new non-gradient prime-/CRT-derived curvature with a usable signed estimate.
- **Next verdict-changing probe:** construct and preregister a source-derived transport that distinguishes genuine rational primes from matched fake alphabets, has nontrivial compensated curvature on a declared common basis, and yields an **effective** lower bound for the grade-zero projection independent of oracle factorization. Test it against the source counterfeit, phase-alias, and same-marginal zero-overlap controls in the legacy prime interferometer package.

### Reproducibility contract

Run `python -m unittest -v test_scott_defect` and `python scott_defect.py > SCOTT_RESULTS.json` from this directory. Tests include three distinct factor-splitting policies, independent sieve primality controls, local Scott-bounds monotonicity, exact source-preserving transport, a Horn-step prefix, finite Goldbach enclosures, and counterfeit alphabets. No full repository CI, Lean proof, or physical quantum experiment has run in this additive round. All previous claims about π base-16 normality and RH remain OPEN.