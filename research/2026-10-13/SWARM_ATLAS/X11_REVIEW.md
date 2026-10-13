# X11 independent audit of B12/B13 and the new bridge

Reviewed snapshot: `71eaf11e48ca3ccb349858bba64abf36b59ee6f5`.
Auditor: `/root/cross11_domain_prooflimits`, a second-generation agent who did
not write B12/B13. Scope: paper statements, relevant implementation, new
finite controls; no claim of independent Lean verification in this review.

**B12 survives.** For the full partial-map domain, directed unions are
functions, finite supports are exactly the compact elements, every report
is the directed union of finite restrictions, and fixed reindexing commutes
with these unions. Nonempty directedness matters for the empty support case.
The totality counterexample correctly requires an infinite address set and
nonempty alphabet. Source-compatible finite reports need not have a
source-compatible join; code-level information compatibility has the stated
weaker meaning. X11 adds the source-admissible ideal completion explicitly:
it retains local admissibility while still admitting phantom total unions.
Restricting to reports with a whole original-source extension would not
generally leave a dcpo, as the eventual-zero source demonstrates.

**B13 theorem survives.** A finite derivation has finite leaf support; a
directed family puts that support in one stage. Used rule licenses must be
included when the calculus grows. The infinite-antecedent rule countermodel
is valid when no other rule can derive its conclusion. Its Lean support
lemma is narrower than the paper directed-family theorem, as the dossier
already states. Semantic rule soundness is not needed for *syntactic*
continuity, but is needed for the intended truth interpretation.

**One necessary wording correction.** B13's final bridge calls the closure
Scott-continuous “exactly under the finitary proof assumptions above.” This
must not be read as necessity for every presentation. For example, include
both the finite rule `a_0 / b` and the infinitary rule `{a_n : n∈N} / b`.
The latter is redundant: whenever all its premises hold, `a_0` already
permits the finite rule. The induced closure therefore equals a finitary
continuous closure despite the presentation containing an infinitary rule.
The accurate invariant is finite-support derivability of every conclusion;
having only finite proof trees and finitary rules is a sufficient syntactic
condition. No change to B13's stated theorem or its countermodel is required.

**New theorem audit.** `K_X` uses nonempty source cylinders; this excludes
vacuous simultaneous positive/negative certificates. An ideal's directedness
places any two finite witnesses below one admissible upper bound, establishing
that the flat Boolean report is single-valued. The map `η` is continuous
because its basic inverse images are product cylinders. Compact-basis
generation proves the converse support presentation, with no effectiveness
smuggled in. The non-r.e. family supplies an explicit effective boundary.
The directed all-finite-scattered-support family witnesses noncontinuity at
the phantom all-one ideal, without relying on a chosen prefix chain.

**Boundaries independently challenged.** Persistent Kripke negation can fail
Scott continuity: negating “some coordinate is zero” holds only at the total
all-one map. A total continuous discrete Boolean answer on the entire
bottomed evidence domain is necessarily constant; a flat partial Boolean
codomain is essential. A source promise can legitimately establish a global
property without observations, but that promise is a semantic premise.
For example, eventual-zero membership is trivial on the declared eventual-
zero source; X11 instead uses first-zero parity to avoid disguising that
promise as a limit proof.

**Implementation review.** Certificates are replayed against separately
supplied available evidence and licenses, not merely against their own
asserted leaf list. Source/basis changes are rejected. Lack of a derivation
returns `None` as unresolved rather than a negative mathematical verdict.
The finite source classifier rejects an empty compatible fiber. The catalog
is declared and may contain semantically unsound rules; an explicit control
retains this distinction. No physical infinite process or missing source
authenticator is supplied.

**Verification.** Ten dedicated tests passed. Independent direct formulas,
existing Horn closure, all six rule orders, all comparable evidence/license
pairs, finite ideal enumeration, and scattered opposite-answer witnesses
agree. The general Scott/ideal and computability arguments remain paper
proofs. Full-suite and integrated adversarial review remain the principal's
responsibility.
