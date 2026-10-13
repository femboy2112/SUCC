/-!
# Positive carrier realization: kernel-checked finite cores

Lean 4.14.0; no mathlib.  Three discrete statements used by the positive
carrier realization dossier (research/2026-10-13/POSITIVE_CARRIER_REALIZATION_THEORY.md).

1. `calibration_fooling_bound`: the support pattern of the calibration
   matrix P = 1/2 [[1,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,1]] admits no
   nonnegative integer factorization with fewer than four terms.  Since any
   nonnegative RATIONAL factorization becomes a nonnegative integer
   factorization of a positive multiple of P after clearing denominators
   (same support pattern), this is the kernel-checked core of
   "nonnegative rank of P is at least 4", hence "no three-state positive
   carrier realizes the path-walk process".  The proof is the fooling-set
   argument: the four cells (0,0),(1,2),(2,1),(3,3) are positive and
   pairwise fooling, so they are covered by four distinct rank-one terms.

2. `gaussian_rotation_never_real`: (3+4i)^n has imaginary part congruent
   to 4 modulo 5 for every n >= 1, hence is never a real number.  This is
   the exact certificate that the rational rotation with cos = 3/5,
   sin = 4/5 has infinite order (equivalently, that its angle is an
   irrational multiple of pi), which is the number-theoretic core of the
   peripheral-spectrum obstruction for the rational probability clock.

3. `closed_loop_law_transport`: the closed-loop joint law of an adaptive
   public-history policy is a function of the behavior on legal words
   alone; two models that agree on legal words induce identical laws for
   every policy, independently of their internal carriers.

Nothing here claims a physical preparation, reset, or sensor.
-/

namespace ObservationalSUCC

namespace PositiveCarrier

/-! ## 1. Fooling-set bound for the calibration support pattern -/

/-- Support pattern of the calibration matrix (row-major, Fin 4 x Fin 4). -/
def calibSupp : Fin 4 → Fin 4 → Bool
  | ⟨0, _⟩, ⟨0, _⟩ => true | ⟨0, _⟩, ⟨1, _⟩ => true
  | ⟨1, _⟩, ⟨0, _⟩ => true | ⟨1, _⟩, ⟨2, _⟩ => true
  | ⟨2, _⟩, ⟨1, _⟩ => true | ⟨2, _⟩, ⟨3, _⟩ => true
  | ⟨3, _⟩, ⟨2, _⟩ => true | ⟨3, _⟩, ⟨3, _⟩ => true
  | _, _ => false

/-- The fooling cells: rows and columns of (0,0),(1,2),(2,1),(3,3). -/
def foolRow : Fin 4 → Fin 4 := fun t => t
def foolCol : Fin 4 → Fin 4
  | ⟨0, _⟩ => ⟨0, by decide⟩ | ⟨1, _⟩ => ⟨2, by decide⟩
  | ⟨2, _⟩ => ⟨1, by decide⟩ | ⟨3, _⟩ => ⟨3, by decide⟩

theorem fool_cells_positive : ∀ t, calibSupp (foolRow t) (foolCol t) = true := by
  decide

theorem fool_cells_fooling :
    ∀ t s, t ≠ s → ¬ (calibSupp (foolRow t) (foolCol s) = true ∧
                       calibSupp (foolRow s) (foolCol t) = true) := by
  decide

/-- Finite sum over `Fin m`. -/
def fsum : (m : Nat) → (Fin m → Int) → Int
  | 0, _ => 0
  | m + 1, f => f ⟨0, Nat.succ_pos m⟩ + fsum m (fun k => f ⟨k.val + 1, Nat.succ_lt_succ k.isLt⟩)

theorem fsum_nonneg (m : Nat) (f : Fin m → Int) (h : ∀ k, 0 ≤ f k) : 0 ≤ fsum m f := by
  induction m with
  | zero => simp [fsum]
  | succ m ih =>
    simp only [fsum]
    have h0 := h ⟨0, Nat.succ_pos m⟩
    have hr := ih (fun k => f ⟨k.val + 1, Nat.succ_lt_succ k.isLt⟩) (fun k => h _)
    omega

/-- If a sum of nonnegative terms is nonzero, some term is positive. -/
theorem fsum_ne_zero_witness (m : Nat) (f : Fin m → Int) (h : ∀ k, 0 ≤ f k)
    (hne : fsum m f ≠ 0) : ∃ k, 0 < f k := by
  induction m with
  | zero => simp [fsum] at hne
  | succ m ih =>
    simp only [fsum] at hne
    by_cases h0 : 0 < f ⟨0, Nat.succ_pos m⟩
    · exact ⟨_, h0⟩
    · have hz : f ⟨0, Nat.succ_pos m⟩ = 0 := by
        have := h ⟨0, Nat.succ_pos m⟩
        omega
      rw [hz, Int.zero_add] at hne
      obtain ⟨k, hk⟩ := ih (fun k => f ⟨k.val + 1, Nat.succ_lt_succ k.isLt⟩) (fun k => h _) hne
      exact ⟨_, hk⟩

/-- A positive term forces a nonnegative sum to be positive. -/
theorem fsum_pos_of_term (m : Nat) (f : Fin m → Int) (h : ∀ k, 0 ≤ f k)
    (k : Fin m) (hk : 0 < f k) : 0 < fsum m f := by
  induction m with
  | zero => exact absurd k.isLt (Nat.not_lt_zero _)
  | succ m ih =>
    simp only [fsum]
    have hr := fsum_nonneg m (fun k => f ⟨k.val + 1, Nat.succ_lt_succ k.isLt⟩) (fun k => h _)
    have h0 := h ⟨0, Nat.succ_pos m⟩
    by_cases hk0 : k.val = 0
    · have : k = ⟨0, Nat.succ_pos m⟩ := Fin.ext hk0
      subst this
      omega
    · have hk' : k.val - 1 < m := by have := k.isLt; omega
      have hpos := ih (fun k => f ⟨k.val + 1, Nat.succ_lt_succ k.isLt⟩) (fun k => h _)
        ⟨k.val - 1, hk'⟩ (by
          have : (⟨k.val - 1 + 1, Nat.succ_lt_succ hk'⟩ : Fin (m + 1)) = k := by
            apply Fin.ext; simp; omega
          simp only []; rw [this]; exact hk)
      omega

/-- Nonnegative integer factorization data for a `Fin 4 x Fin 4` support
pattern through `m` rank-one terms: entry (i,j) = sum_k u k i * v k j. -/
def entry (m : Nat) (u v : Fin m → Fin 4 → Int) (i j : Fin 4) : Int :=
  fsum m (fun k => u k i * v k j)

theorem term_nonneg (m : Nat) (u v : Fin m → Fin 4 → Int)
    (hu : ∀ k i, 0 ≤ u k i) (hv : ∀ k j, 0 ≤ v k j) (i j : Fin 4) :
    ∀ k, 0 ≤ u k i * v k j := fun k => Int.mul_nonneg (hu k i) (hv k j)

/-- **Kernel-checked core of rank+(P) >= 4.**  Any nonnegative integer
factorization whose support pattern is that of the calibration matrix uses
at least four terms. -/
theorem calibration_fooling_bound (m : Nat) (u v : Fin m → Fin 4 → Int)
    (hu : ∀ k i, 0 ≤ u k i) (hv : ∀ k j, 0 ≤ v k j)
    (hsupp : ∀ i j, (entry m u v i j ≠ 0) ↔ calibSupp i j = true) : 4 ≤ m := by
  -- each fooling cell is covered by a term with both factors positive
  have cover : ∀ t : Fin 4, ∃ k : Fin m,
      0 < u k (foolRow t) ∧ 0 < v k (foolCol t) := by
    intro t
    have hne : entry m u v (foolRow t) (foolCol t) ≠ 0 :=
      (hsupp _ _).mpr (fool_cells_positive t)
    obtain ⟨k, hk⟩ := fsum_ne_zero_witness m _ (term_nonneg m u v hu hv _ _) hne
    refine ⟨k, ?_, ?_⟩
    · rcases Decidable.em (0 < u k (foolRow t)) with h | h
      · exact h
      · have hz : u k (foolRow t) = 0 := by have := hu k (foolRow t); omega
        rw [hz, Int.zero_mul] at hk
        exact absurd hk (Int.lt_irrefl 0)
    · rcases Decidable.em (0 < v k (foolCol t)) with h | h
      · exact h
      · have hz : v k (foolCol t) = 0 := by have := hv k (foolCol t); omega
        rw [hz, Int.mul_zero] at hk
        exact absurd hk (Int.lt_irrefl 0)
  -- distinct fooling cells use distinct terms
  have distinct : ∀ t s : Fin 4, t ≠ s → ∀ k : Fin m,
      ¬ ((0 < u k (foolRow t) ∧ 0 < v k (foolCol t)) ∧
         (0 < u k (foolRow s) ∧ 0 < v k (foolCol s))) := by
    intro t s hts k ⟨⟨hut, hvt⟩, ⟨hus, hvs⟩⟩
    apply fool_cells_fooling t s hts
    constructor
    · apply (hsupp _ _).mp
      have := fsum_pos_of_term m (fun k => u k (foolRow t) * v k (foolCol s))
        (term_nonneg m u v hu hv _ _) k (Int.mul_pos hut hvs)
      simp only [entry]; omega
    · apply (hsupp _ _).mp
      have := fsum_pos_of_term m (fun k => u k (foolRow s) * v k (foolCol t))
        (term_nonneg m u v hu hv _ _) k (Int.mul_pos hus hvt)
      simp only [entry]; omega
  -- choose the four covering terms and read off pairwise distinct naturals
  obtain ⟨k0, h0⟩ := cover ⟨0, by decide⟩
  obtain ⟨k1, h1⟩ := cover ⟨1, by decide⟩
  obtain ⟨k2, h2⟩ := cover ⟨2, by decide⟩
  obtain ⟨k3, h3⟩ := cover ⟨3, by decide⟩
  have d01 : k0 ≠ k1 := fun e => distinct _ _ (by decide) k0 ⟨h0, e ▸ h1⟩
  have d02 : k0 ≠ k2 := fun e => distinct _ _ (by decide) k0 ⟨h0, e ▸ h2⟩
  have d03 : k0 ≠ k3 := fun e => distinct _ _ (by decide) k0 ⟨h0, e ▸ h3⟩
  have d12 : k1 ≠ k2 := fun e => distinct _ _ (by decide) k1 ⟨h1, e ▸ h2⟩
  have d13 : k1 ≠ k3 := fun e => distinct _ _ (by decide) k1 ⟨h1, e ▸ h3⟩
  have d23 : k2 ≠ k3 := fun e => distinct _ _ (by decide) k2 ⟨h2, e ▸ h3⟩
  have v01 : k0.val ≠ k1.val := fun e => d01 (Fin.ext e)
  have v02 : k0.val ≠ k2.val := fun e => d02 (Fin.ext e)
  have v03 : k0.val ≠ k3.val := fun e => d03 (Fin.ext e)
  have v12 : k1.val ≠ k2.val := fun e => d12 (Fin.ext e)
  have v13 : k1.val ≠ k3.val := fun e => d13 (Fin.ext e)
  have v23 : k2.val ≠ k3.val := fun e => d23 (Fin.ext e)
  have := k0.isLt; have := k1.isLt; have := k2.isLt; have := k3.isLt
  omega

/-! ## 2. The rational rotation (3+4i)/5 has infinite order -/

/-- `gpow n = (a, b)` with `(3+4i)^n = a + b i`. -/
def gpow : Nat → Int × Int
  | 0 => (1, 0)
  | n + 1 => let p := gpow n; (3 * p.1 - 4 * p.2, 4 * p.1 + 3 * p.2)

theorem gpow_mod5 : ∀ n, (gpow (n + 1)).1 % 5 = 3 ∧ (gpow (n + 1)).2 % 5 = 4 := by
  intro n
  induction n with
  | zero => decide
  | succ n ih =>
    show (3 * (gpow (n + 1)).1 - 4 * (gpow (n + 1)).2) % 5 = 3 ∧
         (4 * (gpow (n + 1)).1 + 3 * (gpow (n + 1)).2) % 5 = 4
    omega

/-- **Kernel-checked core of the irrational-angle certificate.**  For every
n >= 1 the imaginary part of (3+4i)^n is nonzero, so (3+4i)^n is never the
real number 5^n: the rotation with cos = 3/5, sin = 4/5 has no finite order. -/
theorem gaussian_rotation_never_real (n : Nat) : (gpow (n + 1)).2 ≠ 0 := by
  have h := (gpow_mod5 n).2
  omega

/-- Concretely, the rotation matrix (1/5)[[3,-4],[4,3]] raised to n+1 is
(1/5^(n+1)) [[a, -b],[b, a]] with (a, b) = gpow (n+1); it equals the identity
only if b = 0, which never happens. -/
theorem rotation_power_not_identity (n : Nat) :
    ¬ ((gpow (n + 1)).1 = 5 ^ (n + 1) ∧ (gpow (n + 1)).2 = 0) :=
  fun h => gaussian_rotation_never_real n h.2

/-! ## 3. Closed-loop policy laws are functions of the legal behavior -/

universe u v w

/-- A policy weight for a history prefix and action; a behavior assigns a
value (unnormalized joint probability in any commutative structure) to a
history.  The closed-loop law multiplies the policy weights along the
history with the behavior value of the full history. -/
def closedLoop {H : Type u} {α : Type v} [Mul α]
    (weights : H → α) (behavior : H → α) (h : H) : α :=
  weights h * behavior h

/-- Two behaviors that agree on every legal history induce the same
closed-loop law for every policy on legal histories.  The carrier that
produced the behavior is irrelevant. -/
theorem closed_loop_law_transport {H : Type u} {α : Type v} [Mul α]
    (legal : H → Prop) (weights : H → α) (p p' : H → α)
    (agree : ∀ h, legal h → p h = p' h) :
    ∀ h, legal h → closedLoop weights p h = closedLoop weights p' h := by
  intro h hl
  simp only [closedLoop, agree h hl]

/-- Source posteriors are ratios of source-indexed behavior values; equal
behaviors on a legal history give equal numerators and evidence. -/
theorem posterior_data_transport {H : Type u} {S : Type w} {α : Type v} [Mul α]
    (legal : H → Prop) (prior : S → α) (p p' : S → H → α)
    (agree : ∀ s h, legal h → p s h = p' s h) :
    ∀ s h, legal h → prior s * p s h = prior s * p' s h := by
  intro s h hl
  rw [agree s h hl]

end PositiveCarrier

end ObservationalSUCC
