# X11 non-deriver crucible — B11 reviewer

**Verdict: SURVIVES, with one local terminology correction.** X11-S, X11-N and
X11-P have valid written proofs under the explicit interfaces and input types
below. The principal-derived C19 selector candidate also survives this fresh
review. The channel wording in X11 §6 needs correction; its intended support
countermodel is valid. No claim of academic novelty or kernel formalization is
made. Integration remains the principal's decision.

**Provenance and independence.** Author checkpoint:
`30d630504ee429bfcba8be83f921eb57a2b8eb36`, X11 dossier SHA-256
`3b95abc76ffef92fe69fd9b5d2de378af2f9a65e73fb1cd4045ed580ca72a2e6`.
Review starts from B11 checkpoint
`f57d09eb456e49a1ae10f8a614bc2b8cc15993d0`. I read only the author's dossier
before constructing the proofs below, then read the principal's candidate at
`reviews/C19_EFFECTIVE_SELECTOR_CANDIDATE.md` (SHA-256
`e5b9e5ef5e2d2e93692ccf3a246e5edca77b96bb8633e03301c38f7090c97a54`).
No author probe or receipt was read. This is a separate implementation and a
fresh non-deriver proof attempt, **not independent provider/source lineage**:
the task already named the principal's relevant hypotheses, the same provider
was retained, and B11 is one of the bridge's input dossiers. No other swarm
conclusions were used for this review.

## 1. Exact statements accepted

Let C={P0,P1} be the immutable ORIGINAL candidate class on the **entire current
qubit interface**. Every branch is one common CP trace-nonincreasing map given
by an exact finite list of real rational Kraus matrices. For finite history u,
write sigma_i=T_u(Pi), A_u={i:tr sigma_i>0}, U_i=supp sigma_i. Admitted words
have nonempty A at every prefix. All conclusions concern this declared model,
not authentication of a physically prepared state.

* **X11-S, PROVED LOCAL:** i is safe against every admitted common continuation
  iff U_j subset U_i for every j, when rational projector instruments and
  identity continuations are available. The forward implication from dominance
  holds for any restricted common CP toolkit. Necessity is toolkit-relative.
  ORIGINAL-bit identification requires A_u to be singleton.
* **X11-N and C19 candidate, CLASSICAL / PROVED LOCAL:** there is no total
  cylinder-continuous selector on all admitted oracle words and no total
  computable selector on the separate finite program-index family. On the
  exact-rational oracle-word representation, the multivalued eventual-survivor
  problem is strongly Weihrauch-equivalent to negative closed choice C2.
* **X11-P, PROVED LOCAL:** a complete, closed, deterministic, no-input N-state
  branch-word generator has preperiod mu and cycle length lambda with
  mu+lambda<=N. Fixed qubit CP cycle iteration gives
  A_infinity=A_(mu+2 lambda), with deadline at most 2N. Source selection is total
  with exact rational arithmetic and the nonempty-word promise. This is an
  externally certified word, not a report-driven apparatus forcing outcomes.

## 2. Independent support proof and hostile cases

For PSD X and CP Phi with Kraus K_a, y belongs to ker Phi(X) iff every
K_a^*y belongs to ker X: each summand y^*K_a X K_a^*y is nonnegative, so their
sum vanishes exactly when every summand does. Taking orthogonal complements
gives supp Phi(X)=span_a K_a supp X. Thus support inclusion is preserved under
each common continuation and under composition. If U_j subset U_i, killing i
also kills j; an admitted continuation cannot kill the chosen i.

Conversely, if U_j is not contained in U_i, choose a vector in ker sigma_i
having positive sigma_j quadratic form. Because the matrices and their kernels
are rational, a rational such vector exists: a rational basis of ker sigma_i
cannot all lie in ker sigma_j. Its projector vv^*/(v^*v) has exact rational
entries, kills i and preserves j. With its complementary projector and future
identities, this is an admitted instrument branch refuting safe choice.

The reset channel with Kraus P0 and |0><1| maps both original candidates to P0;
both choices are safe but neither original bit is identified. Identity-only
futures similarly make both incomparable P0/P1 safe, refuting unrestricted
toolkit necessity. If retained original-correlated memory is omitted from the
interface, reset produces P0 tensor Pi on the true interface; a memory projector
can then kill one candidate. Completeness of the *current* interface is therefore
load-bearing, not a label.

**Local correction:** X11 §6 calls sigma0=I/4, sigma1=P0 a channel. A
trace-preserving channel cannot have those images: their traces are 1/2 and 1.
The intended CP trace-nonincreasing branch exists with Kraus P0/2,
|1><0|/2 and |0><1|; only bit0 support-dominates. Replace “channel” by “CP branch,”
or give a TP variant with sigma0=I/2. This correction does not change X11-S.

## 3. Independent no-go and representation audit

For a selector on oracle words, consider the identity word and its output b.
Continuity into discrete {0,1} supplies a finite cylinder fixing b. Place
P_(1-b) after every coordinate constrained by that cylinder. The modified word
is still admitted, but its only eventual survivor is 1-b: contradiction.

For program indices, define an always-computable word by bounded simulation of
phi_e(e): identities before any bit output, then P_b after output b. Every index
produces an admitted word, including divergence or non-bit output. A total
selector gives a total bit function g with g(e)=phi_e(e) whenever that value is
a bit. A program for x -> 1-g(x) has an index k, yielding
g(k)=phi_k(k)=1-g(k), contradiction. This argument does not transfer program
indices to arbitrary noncomputable oracle names. The stabilization-index variant
uses identities until halting, then P0. Compute the exact prefix effect at the
returned index: rank two would certify that no later projection occurs, hence
nonhalting; rank one certifies halting. This is a total halting decision.

For oracle words, compute exact rational prefix likelihoods and enumerate i
when sigma_i becomes zero. Zero absorption makes this negative information for
A_infinity. In reverse, a padding symbol gives identity and exclusion of i gives
P_(1-i). The promise forbids exclusion of both points. Both postprocessors are
the identity bit, proving **strong** reductions. Labels are checked explicitly
in the independent probe.

The coefficient representation matters as much as the numeric field. Set
alpha_e=0 for nonhalting e and alpha_e=2^(-h) for first halting time h. This is a
uniform computable-real name, with error <=2^(-n) after n simulation steps, even
though every actual value is rational. The CP branch diag(alpha_e,1) always
preserves candidate1 and kills candidate0 exactly on nonhalting inputs. A
uniform negative-information zero enumerator on these names would enumerate
the nonhalting set. Thus exact rational **numerals**, not merely rational values
given by real names, are essential for the forward C2 transformation.

[Brattka–Gherardi–Hölzl, Definition 2.5 and p.11](https://arxiv.org/pdf/1312.7305)
is the primary closed-choice context. The argument above supplies the actual
maps rather than appealing to the name LLPO.

## 4. Finite-prefix continuity

The admitted finite/infinite prefix dcpo is directed-complete: a directed set
of compatible prefixes has a consistent union, whose every finite prefix was
already admitted. Exclusions are permanent. If the union's A is singleton,
the other bit was excluded at a finite prefix; conversely a finite singleton
persists. Therefore the flat bit report preserves directed suprema and is
Scott-continuous. A limit-only “completed word” token violates this property on
the increasing chain of finite identity prefixes. This does not prohibit a
finite proof about an explicitly supplied generator or the finite-class
common-source existence theorem.

## 5. Independent fixed-cycle proof

Expand the cycle CP map F into Kraus L_a. Put
E_k=(F^*)^k(I) and W_k=ker E_k. Equivalently, E_k is the sum of B^*B over all
length-k Kraus products B. Hence W_k is their joint kernel, giving
W_(k+1)=intersection_a L_a^(-1)W_k. Once every length-k product kills a vector,
every longer product kills it; W_k subset W_(k+1). Equality at any step is
permanent because the same pullback recurrence is iterated. Starting at W0=0,
a two-dimensional space allows at most two strict increases, so W2 is final.

For PSD sigma, tr F^k(sigma)=0 iff supp sigma subset W_k: the trace is a sum
of squared norms, or equivalently tr(E_k sigma). Apply this to each preperiod
state. A candidate alive after two cycles is alive at every later boundary.
Death inside a cycle would persist to the next boundary; therefore no
intermediate prefix can evade the bound. Finally mu+2 lambda<=2N follows from
mu+lambda<=N and lambda<=N. No report-driven choice, time-varying cycle operator,
or omitted memory is allowed in this proof. CP positivity already suffices for
the kernel lemma; TNI supplies the likelihood interpretation.

**Fresh reviewer-derived strengthening, PROVED LOCAL; separate from author
acceptance:** under the admitted-word promise, some preperiod state survives all
cycles, so final W is proper. On a qubit, the increasing chain from zero then
has height at most one. Consequently W1 is final and
A_infinity=A_(mu+lambda), with deadline <=N. This is sharp for a cycle of N
branches whose first N-1 outputs are identity and last output is P0. Its
integration needs a separate principal proof check.

## 6. Minimal failures and exact receipt

A one-state stationary instrument needs only two rational outcomes for arbitrary
delay: K_idle=diag(1,3/5), K_kill=(4/5)P1 have squared effects summing to I.
Any M idle outcomes preserve both candidates; the next kill outcome excludes
candidate0, with positive candidate1 likelihood. Stationary apparatus size does
not constrain the realized word's last exclusion time. Separately,
{(3/5)I,(4/5)I} is complete: an infinite first-outcome word preserves both
supports at every finite stage but has probability limit (9/25)^n -> 0.

Without the qubit restriction, take a four-dimensional contraction fixing e0
and shifting e3 -> e2 -> e1 -> 0. Original candidates e0/e3 keep the word
admitted, but the last exclusion occurs at step3 despite N=1 and 2N=2. Fixed
dimension/face height cannot be omitted. Without a fixed recurrence, arbitrarily
many identity branches before one projector refute any plateau deadline.

The independent standard-library probe checks 209 rational CP maps through six
cycles, 205 complete no-input generator tables (140 survive), reset, a
non-coordinate rational separating projector, negative-name labels, the TP
terminology defect, two-outcome delays, and the four-dimensional failure.
All 140 surviving generator fixtures also satisfy the stronger one-cycle bound.
These are exact **TESTED MODEL** receipts; the proofs establish the quantifiers.

Command, executed exit **0**:

```
PYTHONDONTWRITEBYTECODE=1 timeout 30s python research/2026-10-13/SWARM_ATLAS/reviews/X11_B11_probe.py
```

Limits were 256 MiB address space and 20 CPU seconds. See
`X11_B11_receipt.json` for hashes. No compiler, full suite, children, imported
path mutation, author-code dependency, or push. The only source access failure
was fetching the domain-theory PDF; the Scott argument above is reconstructed
directly. κ is exact declared-model contact; φ is toolkit-relative; σ is shared
source/provider lineage with a separate implementation; ρ includes this reviewer's
prior B11 contribution. The minimal next lemma is a separately reviewed
formalization of the promised one-cycle deadline, retaining the complete
no-input generator and entire-current-interface hypotheses.
