/-!
Positive strategy and ranked adversarial certificates for source-realization
safety games. Requests are selected by the environment; matching responses are
selected by the resolver. Both players see the private state in this contract.
No finite table, fixed-point algorithm, or public-only semantics is smuggled in.
The rank theorem verifies any supplied certificate independently of generation.
-/
set_option autoImplicit false
namespace ObservationalSUCC.ForgeGameCertificates
universe u v w

structure Game (State : Type u) (Request : Type v) where
  requested : State → Request → Prop
  response : State → Request → State → Prop

def Positive {S : Type u} {R : Type v} (game : Game S R)
    (safe : S → Prop) (resolve : S → R → S) : Prop :=
  ∀ s, safe s → ∀ r, game.requested s r →
    game.response s r (resolve s r) ∧ safe (resolve s r)

inductive PolicyRun {S : Type u} {R : Type v} (game : Game S R)
    (resolve : S → R → S) : S → List R → S → Prop
  | nil (s) : PolicyRun game resolve s [] s
  | cons {s z r rest} : game.requested s r →
      PolicyRun game resolve (resolve s r) rest z →
      PolicyRun game resolve s (r :: rest) z

inductive LawfulPath {S : Type u} {R : Type v} (game : Game S R) :
    S → List R → S → Prop
  | nil (s) : LawfulPath game s [] s
  | cons {s t z r rest} : game.requested s r → game.response s r t →
      LawfulPath game t rest z → LawfulPath game s (r :: rest) z

/-- Every environment request history under the certified positional resolver
has an actual lawful realization and stays in the certified region. -/
theorem positive_policy_is_lawful {S : Type u} {R : Type v}
    (game : Game S R) (safe : S → Prop) (resolve : S → R → S)
    (certificate : Positive game safe resolve)
    {s z : S} {word : List R} (run : PolicyRun game resolve s word z)
    (initial : safe s) : LawfulPath game s word z ∧ safe z := by
  induction run with
  | nil => exact ⟨LawfulPath.nil _, initial⟩
  | cons requested tail ih =>
    have accepted := certificate _ initial _ requested
    have remainder := ih accepted.2
    exact ⟨LawfulPath.cons requested accepted.1 remainder.1, remainder.2⟩

/-- Source authentication is a separate edge law, preserved along actual paths. -/
theorem lawful_path_preserves_origin {S : Type u} {R : Type v} {Origin : Type w}
    (game : Game S R) (origin : S → Origin)
    (faithful : ∀ s r t, game.response s r t → origin s = origin t)
    {s z : S} {word : List R} (path : LawfulPath game s word z) :
    origin s = origin z := by
  induction path with
  | nil => rfl
  | cons requested edge tail ih => exact (faithful _ _ _ edge).trans ih

def Ranked {S : Type u} {R : Type v} (game : Game S R)
    (losing : S → Prop) (challenge : S → R) (rank : S → Nat) : Prop :=
  ∀ s, losing s → 0 < rank s ∧ game.requested s (challenge s) ∧
    ∀ t, game.response s (challenge s) t → losing t ∧ rank t < rank s

inductive AdversaryRun {S : Type u} {R : Type v} (game : Game S R)
    (challenge : S → R) : Nat → S → S → Prop
  | nil (s) : AdversaryRun game challenge 0 s s
  | cons {n s t z} : game.response s (challenge s) t →
      AdversaryRun game challenge n t z →
      AdversaryRun game challenge (n + 1) s z

/-- All resolver responses are quantified: the rank excludes even histories
chosen with knowledge of the future, and hence every online resolver. -/
theorem adversary_run_shorter_than_rank {S : Type u} {R : Type v}
    (game : Game S R) (losing : S → Prop) (challenge : S → R) (rank : S → Nat)
    (certificate : Ranked game losing challenge rank)
    {n : Nat} {s z : S} (run : AdversaryRun game challenge n s z)
    (initial : losing s) : n < rank s ∧ losing z := by
  induction run with
  | nil => exact ⟨(certificate _ initial).1, initial⟩
  | cons edge tail ih =>
    have decrease := (certificate _ initial).2.2 _ edge
    have rest := ih decrease.1
    exact ⟨Nat.lt_of_le_of_lt (Nat.succ_le_of_lt rest.1) decrease.2, rest.2⟩

/-- Failure is forced within rank(start) requests, with no fairness premise. -/
theorem ranked_certificate_forces_finite_failure {S : Type u} {R : Type v}
    (game : Game S R) (losing : S → Prop) (challenge : S → R) (rank : S → Nat)
    (certificate : Ranked game losing challenge rank)
    (s : S) (initial : losing s) :
    ¬ ∃ z, AdversaryRun game challenge (rank s) s z := by
  rintro ⟨z, run⟩
  exact Nat.lt_irrefl _
    (adversary_run_shorter_than_rank game losing challenge rank certificate run initial).1

/-- Positive and negative certificate regions cannot overlap. -/
theorem positive_and_ranked_regions_disjoint {S : Type u} {R : Type v}
    (game : Game S R) (safe losing : S → Prop)
    (resolve : S → R → S) (challenge : S → R) (rank : S → Nat)
    (positive : Positive game safe resolve)
    (negative : Ranked game losing challenge rank) :
    ∀ s, losing s → ¬ safe s := by
  have separate : ∀ n s, rank s = n → losing s → safe s → False := by
    intro n
    induction n using Nat.strongRecOn with
    | ind n ih =>
      intro s rank_eq loses survives
      have chosen := positive s survives (challenge s) (negative s loses).2.1
      have lower := (negative s loses).2.2 (resolve s (challenge s)) chosen.1
      exact ih _ (by rw [← rank_eq]; exact lower.2) _ rfl lower.1 chosen.2
  intro s loses survives
  exact separate (rank s) s rfl loses survives

/- The same certificate pattern with adversarial command outcomes. This is the
quantifier order needed after a separately justified public-belief compilation:
environment request, resolver command, adversarial outcome. -/
structure AlternatingGame (State : Type u) (Request : Type v) (Command : Type w) where
  requested : State → Request → Prop
  enabled : State → Request → Command → Prop
  outcome : State → Request → Command → State → Prop

def AlternatingPositive {S : Type u} {R : Type v} {C : Type w}
    (game : AlternatingGame S R C) (safe : S → Prop) (resolve : S → R → C) : Prop :=
  ∀ s, safe s → ∀ r, game.requested s r →
    game.enabled s r (resolve s r) ∧
    (∃ t, game.outcome s r (resolve s r) t) ∧
    ∀ t, game.outcome s r (resolve s r) t → safe t

def AlternatingRanked {S : Type u} {R : Type v} {C : Type w}
    (game : AlternatingGame S R C) (losing : S → Prop)
    (challenge : S → R) (counter : S → C → S) (rank : S → Nat) : Prop :=
  ∀ s, losing s → 0 < rank s ∧ game.requested s (challenge s) ∧
    ∀ c, game.enabled s (challenge s) c →
      game.outcome s (challenge s) c (counter s c) ∧
      losing (counter s c) ∧ rank (counter s c) < rank s

inductive AlternatingAdversaryRun {S : Type u} {R : Type v} {C : Type w}
    (game : AlternatingGame S R C) (challenge : S → R) (counter : S → C → S) :
    Nat → S → S → Prop
  | nil (s) : AlternatingAdversaryRun game challenge counter 0 s s
  | cons {n s z c} : game.enabled s (challenge s) c →
      AlternatingAdversaryRun game challenge counter n (counter s c) z →
      AlternatingAdversaryRun game challenge counter (n + 1) s z

/-- A ranked counterstrategy beats every sequence of enabled resolver commands.
The certificate also ensures its selected counter-outcomes are actual outcomes. -/
theorem alternating_adversary_run_shorter_than_rank
    {S : Type u} {R : Type v} {C : Type w}
    (game : AlternatingGame S R C) (losing : S → Prop)
    (challenge : S → R) (counter : S → C → S) (rank : S → Nat)
    (certificate : AlternatingRanked game losing challenge counter rank)
    {n : Nat} {s z : S}
    (run : AlternatingAdversaryRun game challenge counter n s z)
    (initial : losing s) : n < rank s ∧ losing z := by
  induction run with
  | nil => exact ⟨(certificate _ initial).1, initial⟩
  | cons enabled tail ih =>
    have lower := (certificate _ initial).2.2 _ enabled
    have rest := ih lower.2.1
    exact ⟨Nat.lt_of_le_of_lt (Nat.succ_le_of_lt rest.1) lower.2.2, rest.2⟩

theorem alternating_ranked_forces_finite_failure
    {S : Type u} {R : Type v} {C : Type w}
    (game : AlternatingGame S R C) (losing : S → Prop)
    (challenge : S → R) (counter : S → C → S) (rank : S → Nat)
    (certificate : AlternatingRanked game losing challenge counter rank)
    (s : S) (initial : losing s) :
    ¬ ∃ z, AlternatingAdversaryRun game challenge counter (rank s) s z := by
  rintro ⟨z, run⟩
  exact Nat.lt_irrefl _ (alternating_adversary_run_shorter_than_rank
    game losing challenge counter rank certificate run initial).1

/-- The command/outcome quantifiers have opposite ownership. Losing and winning
certificates cannot both hold at a state, regardless of carrier finiteness. -/
theorem alternating_certificates_disjoint {S : Type u} {R : Type v} {C : Type w}
    (game : AlternatingGame S R C) (safe losing : S → Prop)
    (resolve : S → R → C) (challenge : S → R)
    (counter : S → C → S) (rank : S → Nat)
    (positive : AlternatingPositive game safe resolve)
    (negative : AlternatingRanked game losing challenge counter rank) :
    ∀ s, losing s → ¬ safe s := by
  have separate : ∀ n s, rank s = n → losing s → safe s → False := by
    intro n
    induction n using Nat.strongRecOn with
    | ind n ih =>
      intro s rank_eq loses survives
      have chosen := positive s survives (challenge s) (negative s loses).2.1
      have lower := (negative s loses).2.2 (resolve s (challenge s)) chosen.1
      have next_safe := chosen.2.2 _ lower.1
      exact ih _ (by rw [← rank_eq]; exact lower.2.2) _ rfl lower.2.1 next_safe
  intro s loses survives
  exact separate (rank s) s rfl loses survives

#print axioms positive_policy_is_lawful
#print axioms lawful_path_preserves_origin
#print axioms adversary_run_shorter_than_rank
#print axioms ranked_certificate_forces_finite_failure
#print axioms positive_and_ranked_regions_disjoint
#print axioms alternating_adversary_run_shorter_than_rank
#print axioms alternating_ranked_forces_finite_failure
#print axioms alternating_certificates_disjoint
end ObservationalSUCC.ForgeGameCertificates
