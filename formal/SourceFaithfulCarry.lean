/-!
# Source-faithful carry: exact finite arithmetic and future-safe repair

Standalone Lean 4.14.0, with no imports or added axioms. Source labels are
positive natural numbers n. Internally q = m-1 is zero-based, so
`encode a q r = a*q+r+1` and the paper's one-based quotient is q+1.
The primitive coordinate theorems require a>0 and 0<=r<a where appropriate.
Polynomial address identities hold for all Nat inputs, but invalid digits
do not describe canonical polyphase coordinates. Mixed-radix address equality
does not identify causal histories. No Hilbert-space, heat-limit, prime
selection, signed Weil positivity, or physical-instrument claim is formalized.

Future equivalence below covers arbitrary total deterministic action systems
and all finite words. The a-1 horizon theorem is specific to quotient reports
and the genuine successor on positive source labels. This is a source-relative
minimality theorem, not a universal ban on useful lossy observations.
-/

namespace ObservationalSUCC.SourceFaithfulCarry

set_option autoImplicit false
universe u v w z

def encode (a q r : Nat) : Nat := a * q + r + 1

def quotient (a n : Nat) : Nat := (n - 1) / a

def residue (a n : Nat) : Nat := (n - 1) % a

theorem source_reconstruction (a n : Nat) (positive : 0 < n) :
    encode a (quotient a n) (residue a n) = n := by
  unfold encode quotient residue
  have h := Nat.mod_add_div (n - 1) a
  omega

theorem residue_bound (a n : Nat) (radix : 0 < a) : residue a n < a := by
  exact Nat.mod_lt _ radix

theorem coordinates_of_encoding (a q r : Nat) (radix : 0 < a) (digit : r < a) :
    quotient a (encode a q r) = q ∧ residue a (encode a q r) = r := by
  constructor
  · unfold quotient encode
    rw [Nat.add_sub_cancel, Nat.add_comm, Nat.add_mul_div_left _ _ radix,
      Nat.div_eq_of_lt digit, Nat.zero_add]
  · unfold residue encode
    rw [Nat.add_sub_cancel, Nat.add_comm, Nat.add_mul_mod_self_left,
      Nat.mod_eq_of_lt digit]

theorem no_carry_successor (a q r : Nat) :
    encode a q r + 1 = encode a q (r + 1) := by
  unfold encode
  omega

theorem terminal_carry_successor (a q : Nat) (radix : 0 < a) :
    encode a q (a - 1) + 1 = encode a (q + 1) 0 := by
  simp only [encode, Nat.mul_add, Nat.mul_one]
  omega

theorem authentic_multiplier_terminal (a n : Nat) (radix : 0 < a) (positive : 0 < n) :
    a * n = encode a (n - 1) (a - 1) := by
  have hn : n = (n - 1) + 1 := by omega
  have hprod : a * n = a * (n - 1) + a := by
    calc
      a * n = a * ((n - 1) + 1) := congrArg (fun x => a * x) hn
      _ = a * (n - 1) + a := Nat.mul_succ a (n - 1)
  unfold encode
  omega

theorem affine_successor (a n : Nat) : a * (n + 1) = a * n + a := by
  exact Nat.mul_succ a n

theorem mixed_radix_address (a b q r s : Nat) :
    encode a (encode b q s - 1) r = encode (a * b) q (a * s + r) := by
  simp only [encode, Nat.add_sub_cancel, Nat.mul_add, Nat.mul_assoc]
  omega

theorem triple_address_coherence (a b c q r s t : Nat) :
    encode a (encode b (encode c q t - 1) s - 1) r =
      encode (a * b * c) q (a * b * t + a * s + r) := by
  simp only [encode, Nat.add_sub_cancel, Nat.mul_add, Nat.mul_assoc]
  omega

theorem decoded_no_carry (a q r : Nat) (digit : r + 1 < a) :
    quotient a (encode a q r + 1) = q ∧
      residue a (encode a q r + 1) = r + 1 := by
  rw [no_carry_successor]
  exact coordinates_of_encoding a q (r + 1) (by omega) digit

theorem decoded_terminal_carry (a q : Nat) (radix : 0 < a) :
    quotient a (encode a q (a - 1) + 1) = q + 1 ∧
      residue a (encode a q (a - 1) + 1) = 0 := by
  rw [terminal_carry_successor a q radix]
  exact coordinates_of_encoding a (q + 1) 0 radix radix

theorem binary_quotient_failure :
    quotient 2 1 = quotient 2 2 ∧ quotient 2 (1 + 1) ≠ quotient 2 (2 + 1) := by
  decide

theorem binary_quotient_has_no_successor :
    ¬ ∃ next : Nat → Nat, ∀ n, 0 < n →
      quotient 2 (n + 1) = next (quotient 2 n) := by
  rintro ⟨next, descends⟩
  have left := descends 1 (by decide)
  have right := descends 2 (by decide)
  have same := binary_quotient_failure.1
  rw [same] at left
  exact binary_quotient_failure.2 (left.trans right.symm)

/-- Distinct source digits in one quotient block are separated after at most a-1 successors. -/
theorem distinct_digits_have_finite_witness (a q r s : Nat)
    (ordered : r < s) (digit : s < a) :
    ∃ t, t ≤ a - 1 ∧
      quotient a (encode a q r + t) ≠ quotient a (encode a q s + t) := by
  have radix : 0 < a := by omega
  have smallDigit : r + (a - s) < a := by omega
  have leftAddress : encode a q r + (a - s) = encode a q (r + (a - s)) := by
    unfold encode
    omega
  have rightAddress : encode a q s + (a - s) = encode a (q + 1) 0 := by
    simp only [encode, Nat.mul_add, Nat.mul_one]
    omega
  refine ⟨a - s, by omega, ?_⟩
  rw [leftAddress, rightAddress,
    (coordinates_of_encoding a q (r + (a - s)) radix smallDigit).1,
    (coordinates_of_encoding a (q + 1) 0 radix radix).1]
  omega

/-- The complete quotient transcript up to a-1 successors determines a positive source label. -/
theorem finite_quotient_transcript_injective (a n m : Nat)
    (radix : 0 < a) (positiveN : 0 < n) (positiveM : 0 < m)
    (same : ∀ t, t ≤ a - 1 → quotient a (n + t) = quotient a (m + t)) : n = m := by
  have qsame : quotient a n = quotient a m := by
    simpa only [Nat.add_zero] using same 0 (Nat.zero_le _)
  have nr := source_reconstruction a n positiveN
  have mr := source_reconstruction a m positiveM
  have nb := residue_bound a n radix
  have mb := residue_bound a m radix
  have rsame : residue a n = residue a m := by
    apply Nat.le_antisymm
    · apply Nat.le_of_not_gt
      intro reversed
      obtain ⟨t, ht, distinct⟩ := distinct_digits_have_finite_witness
        a (quotient a n) (residue a m) (residue a n) reversed nb
      have ma : encode a (quotient a n) (residue a m) = m := by
        rw [qsame]
        exact mr
      rw [ma, nr] at distinct
      exact distinct (same t ht).symm
    · apply Nat.le_of_not_gt
      intro ordered
      obtain ⟨t, ht, distinct⟩ := distinct_digits_have_finite_witness
        a (quotient a n) (residue a n) (residue a m) ordered mb
      have ma : encode a (quotient a n) (residue a m) = m := by
        rw [qsame]
        exact mr
      rw [nr, ma] at distinct
      exact distinct (same t ht)
  calc
    n = encode a (quotient a n) (residue a n) := nr.symm
    _ = encode a (quotient a m) (residue a m) := by rw [qsame, rsame]
    _ = m := mr

/-- The universal a-1 action horizon is sharp for the pair of source labels 1 and 2. -/
theorem quotient_horizon_sharp (a : Nat) (radix : 1 < a) :
    (∀ t, t < a - 1 → quotient a (1 + t) = quotient a (2 + t)) ∧
      quotient a (1 + (a - 1)) ≠ quotient a (2 + (a - 1)) := by
  constructor
  · intro t ht
    unfold quotient
    have h1 : (1 + t - 1) < a := by omega
    have h2 : (2 + t - 1) < a := by omega
    rw [Nat.div_eq_of_lt h1, Nat.div_eq_of_lt h2]
  · unfold quotient
    have h1 : 1 + (a - 1) - 1 < a := by omega
    have h2 : 2 + (a - 1) - 1 = a := by omega
    rw [Nat.div_eq_of_lt h1, h2, Nat.div_self (by omega)]
    decide

/-- Any exact successor compression retaining the quotient must retain every positive source label. -/
theorem exact_successor_quotient_compression_injective
    {Small : Type z} (a : Nat) (radix : 0 < a)
    (forget : Nat → Small) (next : Small → Small) (visible : Small → Nat)
    (actions : ∀ n, 0 < n → forget (n + 1) = next (forget n))
    (observations : ∀ n, 0 < n → quotient a n = visible (forget n))
    (n m : Nat) (positiveN : 0 < n) (positiveM : 0 < m)
    (same : forget n = forget m) : n = m := by
  have stateSame : ∀ t, forget (n + t) = forget (m + t) := by
    intro t
    induction t with
    | zero => simpa only [Nat.add_zero] using same
    | succ t ih =>
      rw [Nat.add_succ, Nat.add_succ,
        actions (n + t) (by omega), actions (m + t) (by omega), ih]
  apply finite_quotient_transcript_injective a n m radix positiveN positiveM
  intro t _
  rw [observations (n + t) (by omega), observations (m + t) (by omega), stateSame t]

def run {State : Type u} {Action : Type v}
    (step : Action → State → State) : List Action → State → State
  | [], x => x
  | a :: w, x => run step w (step a x)

def FutureEq {State : Type u} {Action : Type v} {Report : Type w}
    (step : Action → State → State) (observe : State → Report) (x y : State) : Prop :=
  ∀ word, observe (run step word x) = observe (run step word y)

theorem future_refines_present {State : Type u} {Action : Type v} {Report : Type w}
    (step : Action → State → State) (observe : State → Report) (x y : State)
    (same : FutureEq step observe x y) : observe x = observe y := by
  exact same []

theorem future_stable {State : Type u} {Action : Type v} {Report : Type w}
    (step : Action → State → State) (observe : State → Report) (x y : State)
    (same : FutureEq step observe x y) (a : Action) :
    FutureEq step observe (step a x) (step a y) := by
  intro word
  exact same (a :: word)

theorem future_equivalence {State : Type u} {Action : Type v} {Report : Type w}
    (step : Action → State → State) (observe : State → Report) :
    (∀ x, FutureEq step observe x x) ∧
    (∀ x y, FutureEq step observe x y → FutureEq step observe y x) ∧
    (∀ x y z, FutureEq step observe x y → FutureEq step observe y z →
      FutureEq step observe x z) := by
  refine ⟨?_, ?_, ?_⟩
  · intro x word; rfl
  · intro x y same word; exact (same word).symm
  · intro x y z xy yz word; exact (xy word).trans (yz word)

theorem coarsest_future_safe_refinement {State : Type u} {Action : Type v} {Report : Type w}
    (step : Action → State → State) (observe : State → Report)
    (relation : State → State → Prop)
    (present : ∀ x y, relation x y → observe x = observe y)
    (stable : ∀ a x y, relation x y → relation (step a x) (step a y)) :
    ∀ x y, relation x y → FutureEq step observe x y := by
  intro x y related word
  induction word generalizing x y with
  | nil => exact present x y related
  | cons a word ih => exact ih (step a x) (step a y) (stable a x y related)

theorem exact_compression_preserves_futures
    {State : Type u} {Small : Type z} {Action : Type v} {Report : Type w}
    (step : Action → State → State) (observe : State → Report)
    (smallStep : Action → Small → Small) (smallObserve : Small → Report)
    (forget : State → Small)
    (actions : ∀ a x, forget (step a x) = smallStep a (forget x))
    (observations : ∀ x, observe x = smallObserve (forget x))
    (x y : State) (same : forget x = forget y) : FutureEq step observe x y := by
  apply coarsest_future_safe_refinement step observe (fun x y => forget x = forget y)
  · intro x y h
    rw [observations x, observations y, h]
  · intro a x y h
    rw [actions a x, actions a y, h]
  · exact same

end ObservationalSUCC.SourceFaithfulCarry

#print axioms ObservationalSUCC.SourceFaithfulCarry.source_reconstruction
#print axioms ObservationalSUCC.SourceFaithfulCarry.residue_bound
#print axioms ObservationalSUCC.SourceFaithfulCarry.coordinates_of_encoding
#print axioms ObservationalSUCC.SourceFaithfulCarry.no_carry_successor
#print axioms ObservationalSUCC.SourceFaithfulCarry.terminal_carry_successor
#print axioms ObservationalSUCC.SourceFaithfulCarry.authentic_multiplier_terminal
#print axioms ObservationalSUCC.SourceFaithfulCarry.affine_successor
#print axioms ObservationalSUCC.SourceFaithfulCarry.mixed_radix_address
#print axioms ObservationalSUCC.SourceFaithfulCarry.triple_address_coherence
#print axioms ObservationalSUCC.SourceFaithfulCarry.decoded_no_carry
#print axioms ObservationalSUCC.SourceFaithfulCarry.decoded_terminal_carry
#print axioms ObservationalSUCC.SourceFaithfulCarry.binary_quotient_failure
#print axioms ObservationalSUCC.SourceFaithfulCarry.binary_quotient_has_no_successor
#print axioms ObservationalSUCC.SourceFaithfulCarry.distinct_digits_have_finite_witness
#print axioms ObservationalSUCC.SourceFaithfulCarry.finite_quotient_transcript_injective
#print axioms ObservationalSUCC.SourceFaithfulCarry.quotient_horizon_sharp
#print axioms ObservationalSUCC.SourceFaithfulCarry.exact_successor_quotient_compression_injective
#print axioms ObservationalSUCC.SourceFaithfulCarry.future_refines_present
#print axioms ObservationalSUCC.SourceFaithfulCarry.future_stable
#print axioms ObservationalSUCC.SourceFaithfulCarry.future_equivalence
#print axioms ObservationalSUCC.SourceFaithfulCarry.coarsest_future_safe_refinement
#print axioms ObservationalSUCC.SourceFaithfulCarry.exact_compression_preserves_futures
