**Proof Teeth minimum-observation audit — 2026-10-15**

Verdict: **two reproducible certificate defects; no refutation found of PT-C01–05 under their stated hypotheses.** F1 is high severity because the dependency audit loses unresolved premises through a conditional intermediate capsule. F2 is medium severity because an explicitly open target can bypass even the direct-premise check by carrying a higher authority label. Neither defect constitutes a Lean proof or a mathematical refutation of the five paper arguments.

This is a shared-worktree, same-model agent audit. It is not external peer review, a blind independent reasoner, a novelty assessment, or a kernel verification. The mathematical arguments below were checked separately from the producer's tests. Numerical agreement is reported only as numerical agreement.

Authority and preservation: read `AGENTS.md`, `docs/METHOD.md`, and the relevant Aletheia skills. Only this review file was written by this audit. No source/test edits, commits, pushes, agents, full-suite launches, or interference with other processes. Python executions used `PYTHONDONTWRITEBYTECODE=1`. The principal owns final full-suite/CI validation. The new capsule builder was inspected statically and was **not executed**.

Checkout: `/media/leah/SPANKBANK/SUCCYBOI/SUCC-proof-teeth`, branch `research/succ-yean-proof-teeth-ultra-2026-10-15`, remote `https://github.com/femboy2112/SUCC.git`. Initial HEAD was `0f86ba2478a72bf90cf33a4ee192cb2265d992dd`; HEAD was `bed7553fa2c09cb2ae98549d3649f66eb6268741` at the 2026-10-16T01:33:42Z checkpoint. This was concurrent work by others, not an audit commit. All five scoped file hashes remained identical at that checkpoint. Findings refer to these bytes, not an assertion that the shared branch stayed frozen.

| Scoped file | SHA256 |
|---|---|
| `observational_succ/minimal_observation.py` | `0c429dd4087d9be774e26dd0c5b975b20707aaba122d0b436a6353310950ef80` |
| `observational_succ/minimal_weil_window.py` | `5b3599fbd66473a4f2a91e8915ff04d155f2f2cf15012c9b3d41ca38ee24ead0` |
| `observational_succ/source_proof_certificate.py` | `0c6d2f29393884b9af8595787db93d3e5ef0685d68565d3fa01dcf95ebb43ea0` |
| `tests/test_minimal_observation.py` | `e1632ec4452e6e63552453990fa883c346df66b5f4de57cd56821dceb553310c` |
| `research/2026-10-15/MINIMAL_OBSERVATION_CARRIER_THEOREMS.md` | `939688b57602388f354bf4ba8d9cd1b004306f42ac0fd9d75eede017b67e508b` |

**F1 — HIGH — transitive premise laundering in the dependency audit.**

Location: `observational_succ/source_proof_certificate.py:97–113,143–146`; contract: `SOURCE_PROOF_CERTIFICATE_SPEC.md:26–40`; missing regression: `tests/test_source_proof_certificate.py:48–58` checks only a direct conditional.

`visit(dep)` recursively visits the graph, but the consumer discards the dependency's outstanding obligations. It examines only `table[dep]["authority"]`. Thus a `PAPER_PROVED` intermediate with `ASSUME:U` is treated as established by its consumer even when U is explicitly unresolved, refuted, or model-only. The consumer passes with both `open_dependencies=[]` and `retained_hypotheses=[]`.

Concrete logical interpretation: let the common source contain an unrestricted integer x. U is `x=0`, B is `x+1=1` under U, and C is `x=0` obtained by subtracting 1 from B. B's conditional argument is valid; C without U is false at x=1. The metadata audit catches direct omission of U but accepts the same omission through B. This is a structural premise-reporting failure, not a claim that the byte auditor can or should parse arbitrary mathematics.

The output still includes `semantic_authority_issued: null` and `theorems_proved_by_this_audit: []`. Those are useful limits and must be retained. They do not repair a dependency interface that reports the last node without its outstanding premise.

Repair boundary: propagate undisclosed assumption/dependency debt transitively, or distinguish references to conditional propositions from applications of their conclusions and require an explicit discharge record. Do not indiscriminately prohibit a proved theorem from depending on another conditional theorem: using an implication as an implication can be valid. The present schema has no such distinction or discharge mechanism.

**F2 — MEDIUM — open conclusion mode bypasses dependency status checks.**

Location: `observational_succ/source_proof_certificate.py:89–113`. The checker enforces `UNVERIFIED => OPEN_TARGET`, but permits `PAPER_PROVED + OPEN_TARGET`. Its dependency check reads authority alone, so a consumer of that explicitly open node passes without `ASSUME:<id>`. The audit output omits the dependency's conclusion mode as well.

The narrower defensible claim is structural: fields that explicitly identify an open target are ignored when deciding whether a premise remains open. This is not an allegation that an arbitrary forged paper hash can be detected by this interface; the specification correctly disclaims that. Either reject the contradictory status combination, or preserve its open mode as debt independently of authority. Specify and test the authority/scope/conclusion-mode compatibility matrix.

**Exact reproduction of F1 and F2.** Run from the checkout root; no file writes. The existing `AGENTS.md` is only a stable, hashable dossier fixture, not purported proof evidence. This intentionally tests the declared structural boundary.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from pathlib import Path
from observational_succ.source_proof_certificate import (
    audit_capsules, evidence_file, CapsuleError,
)
root = Path('.')
evidence = evidence_file(root, 'AGENTS.md', 'OPEN_DOSSIER')
def cap(cid, authority='PAPER_PROVED', deps=(), hypotheses=(),
        mode='THEOREM_UNDER_HYPOTHESES'):
    c = {k: 'audit countermodel' for k in (
        'statement', 'source', 'operations_relations', 'target_carrier',
        'observation_morphisms', 'topology_measure', 'universal_property',
        'comparison_maps', 'source_identity')}
    c.update(claim_id=cid, authority=authority, source_epoch=0,
        scope='UNIVERSAL', conclusion_mode=mode,
        hypotheses=list(hypotheses), dependencies=list(deps),
        evidence=[evidence], access={k: 'declared' for k in (
            'permitted_observations', 'constructible_witness', 'oracle',
            'probe_discrimination', 'proof_theory', 'execution_cost')},
        adversarial={k: 'declared' for k in (
            'domain_tests', 'negative_examples', 'source_mutations', 'replay')})
    return c
u = cap('U', 'UNVERIFIED', mode='OPEN_TARGET')
try:
    audit_capsules([u, cap('direct', deps=('U',))], root)
except CapsuleError as e:
    print('direct negative control:', str(e))
else:
    raise AssertionError('direct missing premise unexpectedly accepted')
for authority, mode in (
    ('UNVERIFIED', 'OPEN_TARGET'),
    ('REFUTED', 'COUNTEREXAMPLE'),
    ('TESTED_MODEL', 'INSTANCE_ONLY'),
):
    u = cap('U', authority, mode=mode)
    if authority == 'TESTED_MODEL':
        u['scope'] = 'NUMERICAL_MODEL'
    b = cap('B', deps=('U',), hypotheses=('ASSUME:U',))
    c = cap('C', deps=('B',))
    result = audit_capsules([u, b, c], root)
    last = result['claims'][-1]
    print('hidden', authority, result['audit'],
          last['recorded_authority'], last['open_dependencies'],
          last['retained_hypotheses'])
u = cap('open-with-proof-label', mode='OPEN_TARGET')
c = cap('consumer', deps=('open-with-proof-label',))
result = audit_capsules([u, c], root)
last = result['claims'][-1]
print('open-mode bypass', result['audit'],
      last['open_dependencies'], last['retained_hypotheses'])
assert result['theorems_proved_by_this_audit'] == []
assert last['semantic_authority_issued'] is None
PY
```

Observed behavior of the reproduced paths:

```text
direct negative control: Unproved premises cannot disappear from a theorem type
hidden UNVERIFIED STRUCTURE_AND_BYTES_VALID PAPER_PROVED [] []
hidden REFUTED STRUCTURE_AND_BYTES_VALID PAPER_PROVED [] []
hidden TESTED_MODEL STRUCTURE_AND_BYTES_VALID PAPER_PROVED [] []
open-mode bypass STRUCTURE_AND_BYTES_VALID [] []
```

The actual new builder currently retains the direct `ASSUME:PT-ALL-COMPRESSIONS` at `scripts/build_proof_teeth_capsules.py:95–113`. `PT-SCHUR-OPEN` remains `UNVERIFIED / OPEN_TARGET` at lines 114–127. No unconditional consumer of `PT-DENSE-POSITIVITY` appears in that builder. Therefore F1 identifies an exploitable schema contract, **not an observed false unconditional positivity claim in the current builder**. The PT-C02 and PT-C05 capsule statements preserve the integer-character and independent-tape distinctions. The generated JSON was absent when checked before the principal announced the builder; no generated-bundle replay is claimed here.

**Mathematical verdicts and hostile controls.** References below are to `MINIMAL_OBSERVATION_CARRIER_THEOREMS.md` unless another file is named.

| Claim | Audit verdict | Reason and boundary |
|---|---|---|
| PT-C01, lines 12–45 | SURVIVES, paper argument plus finite checks | Fiber constancy defines the unique quotient decoder. The extension to all artifacts is explicitly separate. Exact whole-table checking is valid for the declared finite domain only. |
| PT-C02, lines 49–69 | SURVIVES, paper argument | The parity cases give actual collisions for every positive n not divisible by 4. The upstream bounded character is called on residues; integer and local multiplicative characters remain distinct. |
| PT-C03, lines 73–95 | SURVIVES, paper argument | Periods form a subgroup; a smaller period induces a smaller modulus character only after the zero-support/prime-divisor argument. The implementation tests the unit character's induction, not just table period. |
| PT-C04, lines 99–134 | SURVIVES, paper argument | Newton interpolation holds over Q with integer difference coefficients; generalized binomials are integer-valued on all Z. The lower bound is for probes returning residues modulo n on a known structural family. Quotient descent is a separate condition. |
| PT-C05, lines 138–184 | SURVIVES, paper argument | Smooth two-bump autocorrelations isolate each active paired atom. Their existence rules out cancellation by simultaneous changes at other coordinates. Minimality is for the independent tape mutation class, not alternative zeta functions or cost of computing canonical coefficients. |
| Capsule premise closure | REFUTED as a general structural guarantee | F1 and F2 above. No mathematical authority is issued by loading the capsule. |

For PT-C01, the empty-domain countermodel to the unrestricted extension is exactly `S=B=empty`, `A={*}`. There is a unique empty quotient decoder but no map from the singleton A to empty B. The wrapper at `minimal_observation.py:83–84` correctly handles an empty coimage before calling `OriginalSourceSquare`, whose constructor requires a nonempty carrier. The actual upstream `decoder()` at `covariant_proof_descent.py:72–87` compares target values on after-observation fibers. The wrapper supplies the identity carrier map, so that reuse is correct. Replay checks the exact reachable key set; decode refuses unreachable labels. In particular, the binary-decoder enumeration in the supplied test alone would not test an empty target codomain, but the paper explicitly handles that codomain.

For menu minimality, the order at `minimal_observation.py:155–157` has the correct direction: every sufficient candidate must refine a claimed least candidate. Incomparable minima yield unresolved. A joint observation can recover an XOR target even when neither individual coordinate suffices. No assertion of a toolkit obstruction follows merely from a failed individual probe. This was checked independently using set kernels of partitions, including the empty source.

For PT-C03, if d divides c and is a period, any p dividing c but not d gives, by CRT, x congruent to 1 mod d and 0 mod p. Periodicity gives value 1 while zero extension gives 0. Hence c and d have the same prime divisors. The descended d-periodic multiplicative function has exactly unit support and induces the original character; primitivity forces d=c. A general period n reduces to gcd(n,c). The conductor-1 primitive character has period 1, so the theorem also handles that edge case; the executable real-table family deliberately starts at modulus 2 and does not implement the conductor-1 case.

The principal character `(0,1,1)` modulo 3 is the explicit falsifier of the conflation between conductor and integer period: its integer period is 3 and its conductor is 1. The implementation rejects it. Independently, the unit-fiber criterion used in the code is justified because `(Z/q)^* -> (Z/d)^*` is onto when d divides q: lift a unit mod d and use CRT to avoid primes dividing q but not d. A homomorphism descends exactly when its value is 1 on that reduction kernel.

Upstream character inspection: `source_character_interaction.py:18–22` really does impose the bounded integer evaluator. `tate_chi4.py:83–90` strips the 2-adic valuation before applying the residue character, while `ramified_test` at lines 112–116 is the difference of two unit balls. Thus `chi4(2)=0` and `chi2(2)=1` are compatible facts about different functions. Calling `character_four(x % 4)` in the new adapter does not inherit the old input-size restriction as a theorem hypothesis.

For PT-C04, a useful independent derivation is

```text
Delta_n P(x) = sum_{k=0}^{d-1} b_k binom(x,k),
b_k = sum_{j=k+1}^{d} c_j binom(n,j-k).
```

Vandermonde's polynomial identity proves this on all Z; terms with j-k>n vanish for positive integer n. Thus descent is equivalent to every b_k being 0 mod n. The executed independent check uses this coefficient condition, whereas the producer checks d consecutive difference values. These are different algorithms connected by the unitriangular evaluation matrix. Negative inputs are covered algebraically, not by extrapolating a sample.

There are exactly `n^(d+1)` residue functions in the stated polynomial family: coefficients modulo n determine all integer values and the unitriangular evaluations at 0,...,d recover those coefficient residues. An n-valued depth-m decision tree has at most n^m leaves; shorter termination does not increase that bound. This gives the adaptive lower bound without assuming a field or inverting d!. The analogous matrix/affine counting argument is valid under the stated `r,s>=1` and `n>=2` hypotheses. It is not a separate tested matrix compiler.

Hostile polynomial controls: `P(x)=binom(x,2)` at n=2 has the collision (0,2), values (0,1). Removing the x=2 observation from degree-at-most-4 interpolation admits Newton coefficients `(0,0,1,-3,6)`, whose observations are `(0,0,1,0,0)`. Dropping the degree promise entirely fails: `binom(x,5)` vanishes at 0,...,4 but equals -1 at -1. None of these counterexamples violates the repaired statements in the paper.

For PT-C05, put x=log(q), c=eta*eta-tilde, and f(t)=eta(t+x/2)+eta(t-x/2). Direct expansion yields `g(s)=2c(s)+c(s-x)+c(s+x)`. Since every positive active atom exceeds 2 epsilon, all central contributions at active atoms vanish; since all other positive atoms are farther than 2 epsilon from x, the translated terms vanish there too. At x, only c(0) survives. The negative atom is symmetric. Outside the active set, compact support strictly inside (-a,a) makes every value at |s|>=2a zero, including the endpoint.

Smoothness is the usual explicit flat-bump argument: derivatives inside the bump are polynomial/rational factors times the exponential, and all tend to zero at the boundary. Its norm is positive. On [-epsilon/2,epsilon/2], eta squared is at least exp(-8/3)>1/27, so the paired coefficient response exceeds `2*abs(delta)*epsilon/27`. These analytic facts, rather than the quadrature check, justify the universal statement. Comparing any two tapes and isolating any differing active coordinate proves equality of fibers, not just failure under single-coordinate deletion.

The independent-mutation hypothesis is essential. If the admissible tape class were the singleton canonical zeta tape with its coefficient law known, a constant observation is sufficient; there is no nontrivial information-theoretic coordinate minimum on that singleton. The document expressly avoids this overclaim. Likewise the chi4 canonical coefficient at q=2 is zero, but a tape mutation may change it; retaining that coordinate is intentional and was checked.

The upstream arithmetic/interval path was inspected, not treated as an oracle: `completed_weil_transport.py:75–92` enumerates genuine prime powers by a prime sieve and successive powers; it does not include composite 6 or substitute log(q) for log(p). `tate_weil_window.py:35–54` uses `q<3^ceil(2a)`, a conservative cutoff since e<3. `suzuki_arch_intervals.py:40–51` uses z=(x-1)/(x+1) and bounds the positive tail after N terms by `2*z^(2N+1)/((2N+1)*(1-z*z))`. This is valid because subsequent denominators are at least 2N+1. The new integer-log reduction has k>=0 and reduced argument in [1,2), so addition and multiplication preserve enclosure direction. The witness's epsilon is one eighth of the smallest positive certified margin, giving strict support and separation. An unresolved comparison is refused rather than rounded into a theorem.

**Executed checks and reproducibility.** All listed executions exited 0. No complete test suite or CI run is claimed.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_minimal_observation.py' -v
```

Receipt: 12 tests, 0.148 seconds reported by unittest, `OK`, Python 3.12.3. This is the only unittest suite launched by this audit. No process corresponding to the principal's two full-suite PIDs was launched or killed by this audit.

`scripts/minimal_observation_probe.py` was executed through `runpy.run_path(..., run_name='__main__')`, with stdout captured in memory. Stdout SHA256 was `6a47b9a0a69337a090722ab6e03fa00a6cbf6c62c5b2cc4c3a5c8c990234eb8a`. It produced the expected positive/negative finite certificates, chi4 outcomes, refuted binomial descent, and sensitive autocorrelation; both `RH_proved` and `Lean_verification_performed_by_this_probe` were false. Direct execution with bytecode disabled reproduces that probe output.

Independent finite/polynomial/character probe, separate from the supplied tests:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from itertools import product
from fractions import Fraction as Q
from math import comb, gcd
from observational_succ.minimal_observation import (
    FiniteObservation, compile_factorization, replay_factorization,
    minimum_in_menu, newton_coefficients, newton_value, polynomial_descent,
    PrimitiveRealCharacter, ObservationError,
)
def partitions(n):
    if n == 0:
        yield ()
        return
    for p in partitions(n-1):
        for x in range(max(p, default=-1)+2):
            yield p+(x,)
count = menus = 0
for size in range(6):
    ps = list(partitions(size))
    for o in ps:
        for h in ps:
            expected = all(o[i] != o[j] or h[i] == h[j]
                for i in range(size) for j in range(size))
            p = FiniteObservation('partition-countercheck', 0, o, h)
            c = compile_factorization(p)
            assert (c.outcome == 'PROVEN_FACTORIZATION') == expected
            assert replay_factorization(p, c)
            count += 1
    if size <= 4:
        for h in ps:
            p = FiniteObservation('menu-countercheck', 0, h, h)
            for a, b in product(ps, repeat=2):
                menu = (a,b)
                ker = lambda r: {(i,j) for i in range(size)
                    for j in range(size) if r[i] == r[j]}
                targetker = ker(h)
                suff = [i for i,r in enumerate(menu) if ker(r) <= targetker]
                least = tuple(i for i in suff if all(
                    ker(menu[j]) <= ker(menu[i]) for j in suff))
                result = minimum_in_menu(p, menu)
                assert result['least_indices'] == least
                expected = ('PROVEN_MINIMUM_IN_MENU' if least else
                    'PROVEN_TOOLKIT_OBSTRUCTION' if not ker(a)&ker(b) <= targetker
                    else 'UNRESOLVED_MINIMUM_IN_MENU')
                assert result['outcome'] == expected
                menus += 1
print('partition factorization cases:', count, 'menu cases:', menus)
def poly(cs):
    total = [Q(0)]*len(cs)
    basis = [Q(1)]
    for j,c in enumerate(cs):
        for k,v in enumerate(basis):
            total[k] += c*v
        nxt = [Q(0)]*(len(basis)+1)
        for k,v in enumerate(basis):
            nxt[k] -= Q(j,j+1)*v
            nxt[k+1] += v/Q(j+1)
        basis = nxt
    return total
def evalp(p,x):
    ans = Q(0)
    for c in p[::-1]:
        ans = ans*x+c
    assert ans.denominator == 1
    return ans.numerator
checks = 0
for d in range(6):
    for cs in product((-1,0,1), repeat=d+1):
        pp = poly(cs)
        for x in (-10**6-1,-31,-2,-1,0,1,d+1,37,10**6+1):
            assert newton_value(cs,x) == evalp(pp,x)
        assert newton_coefficients(tuple(evalp(pp,x) for x in range(d+1))) == cs
        for n in (1,2,3,4,6,8,9,12):
            dc = tuple(sum(cs[j]*comb(n,j-k) for j in range(k+1,d+1)
                if j-k <= n) for k in range(d))
            got = polynomial_descent(cs,n)
            assert (got['outcome'] == 'PROVEN_DESCENT') == all(v%n == 0 for v in dc)
            if got['collision']:
                a,b = got['collision']
                assert (evalp(pp,a)-evalp(pp,b)) % n
            checks += 1
print('independent rational-polynomial descent cases:', checks)
accepted = []
total = 0
for q in range(2,21):
    units = [x for x in range(q) if gcd(x,q) == 1]
    for signs in product((-1,1), repeat=len(units)-1):
        v = [0]*q
        v[1] = 1
        for x,s in zip(units[1:], signs):
            v[x] = s
        if any(v[a*b%q] != v[a]*v[b] for a in units for b in units):
            continue
        conductor = next(d for d in range(1,q+1) if q%d == 0 and
            all(v[u] == 1 for u in units if (u-1)%d == 0))
        try:
            ch = PrimitiveRealCharacter(tuple(v))
            valid = True
        except ObservationError:
            valid = False
        assert valid == (conductor == q)
        if valid:
            accepted.append(q)
            for n in (1,2,3,4,5,6,7,8,q,q+1,10**40+q):
                assert (ch.observation(n)['collision'] is None) == (n%q == 0)
        total += 1
print('character homomorphisms:', total, 'accepted primitive moduli:', accepted)
PY
```

Observed receipt:

```text
partition factorization cases: 2960 menu cases: 3510
independent rational-polynomial descent cases: 8736
character homomorphisms: 47 accepted primitive moduli: [3, 4, 5, 7, 8, 8, 11, 12, 13, 15, 17, 19, 20]
```

Independent support/interval/smooth-function probe. The first part uses rational exponential bounds and trial factorization instead of the imported logarithm algorithm and sieve. Decimal logarithms and mpmath quadrature are expressly numerical consistency checks; they are not proof certificates.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -u - <<'PY'
from fractions import Fraction as Q
from math import factorial, isqrt
from decimal import Decimal, localcontext
import mpmath as mp
from observational_succ.minimal_weil_window import (
    minimum_arithmetic_window, autocorrelation_atom_witness, integer_log_bounds,
)
from observational_succ.tate_weil_distribution import TateWeilSource
def pp(n):
    for p in range(2,isqrt(n)+1):
        if n%p == 0:
            r = n
            while r%p == 0:
                r //= p
            return p if r == 1 else None
    return n
def exp_bounds(x):
    total = sum((x**j/factorial(j) for j in range(81)), Q())
    first = x**81/factorial(81)
    return total, total+first/(1-x/82)
labels = [(n,pp(n)) for n in range(2,729) if pp(n) is not None]
for k in range(1,49):
    a = Q(k,16)
    lo,hi = exp_bounds(2*a)
    assert all(not lo <= n <= hi for n,p in labels)
    expected = tuple((n,p) for n,p in labels if n < lo)
    w = minimum_arithmetic_window(a)
    assert not w['unresolved']
    assert tuple((n,p) for n,p,_ in w['active']) == expected
print('48 support windows agree with independent rational exp bounds and trial factors')
with localcontext() as ctx:
    ctx.prec = 110
    for n in range(1,730):
        v = Decimal(n).ln()
        for terms in (1,2,8,32):
            lo,hi = integer_log_bounds(n,terms)
            l = Decimal(lo.numerator)/Decimal(lo.denominator)
            h = Decimal(hi.numerator)/Decimal(hi.denominator)
            assert l <= v <= h
print('2916 log enclosures agree with 110-digit Decimal ln; numerical cross-check only')
mp.mp.dps = 50
val = lambda q: mp.mpf(q.numerator)/q.denominator
eta = lambda u: mp.exp(-1/(1-u*u)) if abs(u) < 1 else mp.mpf(0)
unitnorm = mp.quad(lambda u: eta(u)**2, [-1,0,1])
w = minimum_arithmetic_window(Q(3,2))
active = [n for n,p,b in w['active']]
maxerr = mp.mpf(0)
nonzero_offdiag = 0
minratio = mp.inf
for n in active:
    cert = autocorrelation_atom_witness(Q(3,2),n)
    eps = val(cert['epsilon'])
    x = mp.log(n)
    centers = (-x/2,x/2)
    def f(t):
        return sum(eta((t-c)/eps) for c in centers)
    def g(s):
        return eps*sum(mp.quad(lambda u: eta(u)*f(c+eps*u-s), [-1,0,1])
                       for c in centers)
    for m in active:
        for sign in (-1,1):
            actual = g(sign*mp.log(m))
            expected = eps*unitnorm if m == n else 0
            maxerr = max(maxerr,abs(actual-expected))
            if m != n and actual:
                nonzero_offdiag += 1
    response = 2*g(x)
    lower = val(cert['unit_paired_coefficient_response_abs_lower_strict'])
    minratio = min(minratio,response/lower)
    assert response > lower
assert maxerr < mp.mpf('1e-45') and nonzero_offdiag == 0
print('direct smooth-f quadrature:',len(active),'witnesses;',2*len(active)**2,
      'signed atom checks; max error',mp.nstr(maxerr,5),
      'off-diagonal nonzeros',nonzero_offdiag,
      'min response/lower',mp.nstr(minratio,12))
z = minimum_arithmetic_window(Q(1,2), source=TateWeilSource('chi4','chi4-audit',9))
assert z['active'][0][0] == 2 and z['canonical_zero_coefficients_may_be_mutated']
print('chi4 zero coefficient at q=2 retained in mutation-class minimum')
PY
```

Observed receipt:

```text
48 support windows agree with independent rational exp bounds and trial factors
2916 log enclosures agree with 110-digit Decimal ln; numerical cross-check only
direct smooth-f quadrature: 12 witnesses; 288 signed atom checks; max error 0.0 off-diagonal nonzeros 0 min response/lower 3.59332526281
chi4 zero coefficient at q=2 retained in mutation-class minimum
```

Additional boundary controls produced: empty quotient certificate accepted, unreachable decode refused, zero maps from singleton to empty; imprimitive principal mod3 rejected despite period 3; binomial descent refuted with (0,2); omission witness `(0,0,1,-3,6)`; degree-promise countermodel `(0,0,0,0,0,-1)` on inputs `(0,1,2,3,4,-1)`. Enumerating coefficient residues for d=0,...,4 and n=2,3,4 gave all `n^(d+1)` distinct standard evaluation vectors in 15 finite controls. The universal lower bound still rests on the algebraic/counting argument above.

**Evidence independence and remaining limits.** The supplied unit tests and producer share imports, hence their agreement is one implementation family. The audit's partition-kernel calculation, rational monomial/Horner evaluation, Vandermonde descent criterion, kernel-based character conductor calculation, and exp/trial-factor support calculation change the algorithm or representation. They share this Python runtime and this model; no additional reasoner independence is claimed. The direct smooth-f integral is a numerical check of the formula, not a replacement for smoothness and support proofs. No phasor transport, probability-of-truth score, or quantum claim is used.

Contact (kappa) is actual source bytes, exact execution and the stated analytic arguments; toolkit survival (phi) is confined to the declared domains and probes. Source correctness (sigma) is mathematical source declaration plus inspected code, not physical authentication or a genuine-zeta interpretation of mutated tapes. Commitment coupling (rho) remains that of a same-model project audit. The next discriminating checks are three-node premise-closure and status/mode regression tests for F1/F2, followed by the principal's separate generated-capsule replay and final validation. No RH, external-review, novelty, or Lean certification follows from this report.

**Post-fix independent retest — 2026-10-16T01:44:24Z (October 15 local).**

Current verdict: **F1 and F2 are repaired for the declared structural dependency interface.** The historical failures and original source hashes above remain intact. This appendix supersedes the original open-defect verdict for the patched bytes below; it does not convert recorded authority into mathematical proof.

HEAD at retest: `b59d9c9e0c9aa9452f1b8a244975475177095c7b` on the same shared branch. Retested `observational_succ/source_proof_certificate.py` SHA256: `1d7ff7a250582620d81a9063f7c55fe1c71286647514ebe85eeea5dd617b00a4`. Inspected `tests/test_source_proof_certificate.py` SHA256: `f4ffa8de222fb1cf305c8f4deffb79f90481c5661458f7494ca49ed954ed0d6d`. The complete pre-append report SHA256 was `bf697b446358e1e8f0ca625315bccacb8efde880da0577f6258495161ed3c5eb`.

F1 retest: all three original `U -> B(ASSUME:U) -> C(no assumption)` graphs now fail with `Unproved premises cannot disappear from a theorem type`. This holds for U labeled UNVERIFIED, REFUTED, or TESTED_MODEL. Adding the missing `ASSUME:U` makes the conditional consumer admissible while preserving `open_dependencies=['U']`; the premise is not discharged. Five-node chains were checked in all 120 input orders for each root status. Omitting the assumption at any of the four consumer levels was rejected. A diamond with two independent open roots retained both debts in all 120 input orders; retaining only one root or replacing them with names of intermediate capsules was rejected.

F2 retest: the explicit authority/mode matrix at lines 98–108 rejects higher proof labels combined with OPEN_TARGET. The new instance-scope check also rejects INSTANCE_ONLY with UNIVERSAL scope. An exhaustive 7-authority by 4-mode by 3-scope structural probe yielded 25 permitted combinations and 59 rejections. The Lean-labeled fixtures carried all three required evidence kinds and a declaration name, so their invalid-mode rejection was not accidentally caused by absent Lean fields. Those fixtures are **synthetic metadata**, not Lean executions or authentic Lean proofs.

Ordinary hypothesis retest: a three-node chain/diamond with `bounded A`, `dense chain`, and `same source` retained all three hypotheses at its consumer in every input order, even with `declared_hypotheses=[]`. Thus the effective output remains explicitly conditional. An explicit ASSUME of a node with a proof label still creates debt, and a downstream consumer must retain it. Missing/self-referential ASSUME targets and missing/circular ordinary dependency edges were rejected.

The inspected code supports these results beyond the finite examples: a node is cached only after its dependencies have been visited. The unions at lines 117–118 preserve every dependency's open debt and effective hypotheses. Lines 119–128 add weak-authority dependencies and explicit assumptions, while lines 131–134 require the consumer to declare every inherited debt. By induction on the finite acyclic dependency graph, passing through additional ordinary dependency edges cannot remove cached debt. The authority/mode check occurs before traversal and prevents the original contradictory open-status label. This is an argument about metadata propagation, not about the truth of the statements attached to the graph.

No further material defect was found in this focused retest. Remaining boundaries are deliberate: the checker has no semantic discharge rule, no proof-term application checker, no source authentication, and no ability to distinguish a forged proof transcript by its hash alone. References appearing solely as ASSUME tokens remain explicit opaque debt; they are not automatically treated as applications of the named theorem. Automatic union of ordinary premises is conservative and may retain premises that a real proof could discharge. The output now distinguishes declared from retained hypotheses and includes conclusion mode, which makes that behavior reviewable.

The principal's eight-test suite was inspected but not counted as independent evidence or rerun here. Instead, the following in-memory probe reused the original published audit fixture and performed **595 calls: 512 expected acceptances and 83 expected rejections**, exit 0. No source/test edits, temporary fixture files, full-suite runs, builder execution, commits, pushes, or agent launches were made for this retest. Only this appendix was added.

Exact independent reproduction, from the checkout root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
from pathlib import Path
from itertools import permutations, product
from copy import deepcopy
import re
from observational_succ.source_proof_certificate import audit_capsules, CapsuleError
report = Path('reviews/2026-10-15_PROOF_TEETH_MINIMUM_OBSERVATION_AUDIT.md').read_text()
old = re.search(r"```sh\nPYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'\n(.*?)\nPY\n```", report, re.S).group(1)
# Reuse the original published fixture, not the principal's regression tests.
exec(old.split("u = cap('U', 'UNVERIFIED', mode='OPEN_TARGET')")[0])
counts = {'rejections': 0, 'accepted': 0}
def reject(cs, fragment):
    try:
        audit_capsules(cs, root)
    except CapsuleError as e:
        assert fragment in str(e), str(e)
        counts['rejections'] += 1
        return
    raise AssertionError(('unexpected acceptance', cs))
def accept(cs):
    r = audit_capsules(cs, root)
    assert r['theorems_proved_by_this_audit'] == []
    assert r['physical_source_authentication'] is False and r['RH_proved'] is False
    assert all(x['semantic_authority_issued'] is None for x in r['claims'])
    counts['accepted'] += 1
    return {x['claim_id']: x for x in r['claims']}
for authority, mode in (('UNVERIFIED','OPEN_TARGET'), ('REFUTED','COUNTEREXAMPLE'), ('TESTED_MODEL','INSTANCE_ONLY')):
    u = cap('U', authority, mode=mode)
    if authority == 'TESTED_MODEL': u['scope'] = 'NUMERICAL_MODEL'
    b = cap('B', deps=('U',), hypotheses=('ASSUME:U','x is an integer'))
    c = cap('C', deps=('B',))
    reject([u,b,c], 'Unproved premises')
    c['hypotheses'] = ['ASSUME:U']
    d = cap('D', deps=('C',), hypotheses=('ASSUME:U',))
    e = cap('E', deps=('D',), hypotheses=('ASSUME:U',))
    nodes = [u,b,c,d,e]
    for order in permutations(nodes):
        out = accept(list(order))
        assert out['E']['open_dependencies'] == ['U']
        assert out['E']['retained_hypotheses'] == ['ASSUME:U','x is an integer']
        assert out['E']['declared_hypotheses'] == ['ASSUME:U']
    for omission in range(1,5):
        bad = deepcopy(nodes)
        bad[omission]['hypotheses'] = []
        reject(bad[::-1], 'Unproved premises')
print('F1: all three original bad graphs rejected; 360 five-node permutations retain U and ordinary hypothesis; 12 omission controls rejected')
u = cap('U','UNVERIFIED',mode='OPEN_TARGET')
v = cap('V','REFUTED',mode='COUNTEREXAMPLE')
b = cap('B',deps=('U',),hypotheses=('ASSUME:U','bounded A'))
c = cap('C',deps=('V',),hypotheses=('ASSUME:V','common source'))
d = cap('D',deps=('B','C'),hypotheses=('ASSUME:U','ASSUME:V'))
for order in permutations([u,v,b,c,d]):
    out = accept(list(order))
    assert out['D']['open_dependencies'] == ['U','V']
    assert out['D']['retained_hypotheses'] == ['ASSUME:U','ASSUME:V','bounded A','common source']
for hyps in ((),('ASSUME:U',),('ASSUME:V',),('ASSUME:B','ASSUME:C')):
    bad = deepcopy(d); bad['hypotheses'] = list(hyps)
    reject([bad,c,b,v,u], 'Unproved premises')
print('diamond: 120 input permutations retain both debts; four incomplete/renamed assumption controls rejected')
proofs = ('CLASSICAL_IMPORTED','PAPER_PROVED','LEAN_KERNEL_PROVED')
auths = proofs + ('EXACT_FINITE_CHECK','TESTED_MODEL','UNVERIFIED','REFUTED')
modes = ('THEOREM_UNDER_HYPOTHESES','INSTANCE_ONLY','OPEN_TARGET','COUNTEREXAMPLE')
scopes = ('FINITE_INSTANCE','UNIVERSAL','NUMERICAL_MODEL')
matrix = {a:set(modes[:2]) for a in proofs}
matrix.update(EXACT_FINITE_CHECK={'INSTANCE_ONLY'},TESTED_MODEL={'INSTANCE_ONLY'},UNVERIFIED={'OPEN_TARGET'},REFUTED={'COUNTEREXAMPLE'})
allowed = denied = 0
for a,m,s in product(auths,modes,scopes):
    node = cap('X',a,mode=m); node['scope'] = s
    if a == 'LEAN_KERNEL_PROVED':
        node['evidence'] = [dict(evidence,kind=k) for k in ('LEAN_SOURCE','LEAN_RECEIPT','AXIOM_MANIFEST')]
        node['kernel_declarations'] = ['Fixture.declaration']
    wanted = m in matrix[a] and not (m == 'INSTANCE_ONLY' and s == 'UNIVERSAL')
    if wanted:
        out = accept([node]); allowed += 1
        assert out['X']['conclusion_mode'] == m
    else:
        reject([node], 'Authority and conclusion mode' if m not in matrix[a] else 'instance cannot')
        denied += 1
print('authority/mode/scope matrix:', allowed, 'accepted,', denied, 'rejected')
a = cap('A',hypotheses=('bounded A','same source'))
b = cap('B',deps=('A',),hypotheses=('dense chain',))
c = cap('C',deps=('A','B'))
for order in permutations([a,b,c]):
    out=accept(list(order)); assert out['C']['declared_hypotheses']==[]
    assert out['C']['retained_hypotheses']==['bounded A','dense chain','same source']
print('ordinary hypotheses: six three-node orders retain all premises')
p = cap('proved')
a = cap('conditional',hypotheses=('ASSUME:proved',))
b = cap('consumer',deps=('conditional',),hypotheses=('ASSUME:proved',))
assert accept([b,a,p])['consumer']['open_dependencies']==['proved']
b['hypotheses']=[]; reject([b,a,p], 'Unproved premises')
for hyps in (('ASSUME:missing',),('ASSUME:bad',)):
    reject([cap('bad',hypotheses=hyps)],'ASSUME must name')
reject([cap('A',deps=('B',)),cap('B',deps=('A',))],'Circular')
reject([cap('A',deps=('missing',))],'Undeclared dependency')
print('no-discharge, invalid ASSUME and cycle/missing-dependency controls passed')
print('TOTAL',counts)
PY
```

Observed receipt:

```text
F1: all three original bad graphs rejected; 360 five-node permutations retain U and ordinary hypothesis; 12 omission controls rejected
diamond: 120 input permutations retain both debts; four incomplete/renamed assumption controls rejected
authority/mode/scope matrix: 25 accepted, 59 rejected
ordinary hypotheses: six three-node orders retain all premises
no-discharge, invalid ASSUME and cycle/missing-dependency controls passed
TOTAL {'rejections': 83, 'accepted': 512}
```
