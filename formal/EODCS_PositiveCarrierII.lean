/-!
# Positive carrier realization II: kernel-checked finite cores

Lean 4.14.0; no mathlib.  Discrete statements used by Part II of the
positive carrier dossier
(research/2026-10-13/POSITIVE_CARRIER_REALIZATION_THEORY_II.md).

1. `fooling_set_bound` (general): if a nonnegative integer factorization
   with `m` rank-one terms has `k` cells that are positive and pairwise
   fooling (for `t ≠ s` at least one of the two cross cells vanishes), then
   `k ≤ m`.  This is the nonnegative-rank lower bound used for every support
   obstruction (PWₙ, the ghost blocks of the phantom walks), for arbitrary
   size; the inherited `calibration_fooling_bound` is the 4×4 instance.
   The pigeonhole principle `fin_injective_le` is proved from scratch.

2. `golden_slope_irrational`: there are no integers `p, q` with `q ≠ 0` and
   `p² + p·q − q² = 0`.  Hence the eigen-slopes of [[2,1],[1,1]] — the roots
   of `s² + s − 1` — are irrational; this is the number-theoretic core of the
   irrational-contact obstruction: the Fibonacci cat system has a two-state
   positive carrier over `ℚ(√5)` and no positive carrier over `ℚ`.
   Proved by descent through `sqrt5_descent : x·x = 5·y·y → y = 0` in ℕ.

3. `menu_count_bound`: the menu after a legal history is a function of the
   support of the current law; `2^m` supports bound the number of distinct
   menus a carrier with `m` states can display (finite-set pigeonhole in the
   same style).

Nothing here claims a physical preparation, reset, or sensor.
-/

namespace ObservationalSUCC

namespace PositiveCarrierII

/-! ## 0. Finite sums over `Fin m` (as in Part I) -/

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

/-! ## 1. Pigeonhole: an injection `Fin k → Fin m` forces `k ≤ m` -/

theorem fin_injective_le : ∀ (k m : Nat) (f : Fin k → Fin m),
    (∀ a b, f a = f b → a = b) → k ≤ m := by
  intro k
  induction k with
  | zero => intro m f _; exact Nat.zero_le m
  | succ k ih =>
    intro m f hf
    cases m with
    | zero => exact absurd (f ⟨0, Nat.succ_pos k⟩).isLt (Nat.not_lt_zero _)
    | succ m' =>
      -- delete the image of 0 from the codomain
      let y0 : Fin (m' + 1) := f ⟨0, Nat.succ_pos k⟩
      have hne : ∀ i : Fin k, (f ⟨i.val + 1, Nat.succ_lt_succ i.isLt⟩).val ≠ y0.val := by
        intro i h
        have := hf _ _ (Fin.ext h)
        have := congrArg Fin.val this
        simp at this
      let g : Fin k → Fin m' := fun i =>
        let y := f ⟨i.val + 1, Nat.succ_lt_succ i.isLt⟩
        if h : y.val < y0.val then ⟨y.val, by have := y0.isLt; omega⟩
        else ⟨y.val - 1, by have := y.isLt; have := hne i; omega⟩
      have hg : ∀ a b, g a = g b → a = b := by
        intro a b hab
        have hv := congrArg Fin.val hab
        simp only [g] at hv
        have ha := hne a
        have hb := hne b
        have hfa := (f ⟨a.val + 1, Nat.succ_lt_succ a.isLt⟩).isLt
        have hfb := (f ⟨b.val + 1, Nat.succ_lt_succ b.isLt⟩).isLt
        have key : (f ⟨a.val + 1, Nat.succ_lt_succ a.isLt⟩).val =
                   (f ⟨b.val + 1, Nat.succ_lt_succ b.isLt⟩).val := by
          by_cases h1 : (f ⟨a.val + 1, Nat.succ_lt_succ a.isLt⟩).val < y0.val <;>
          by_cases h2 : (f ⟨b.val + 1, Nat.succ_lt_succ b.isLt⟩).val < y0.val <;>
          simp [h1, h2] at hv <;> omega
        have := hf _ _ (Fin.ext key)
        have := congrArg Fin.val this
        exact Fin.ext (by simp at this; omega)
      exact Nat.succ_le_succ (ih m' g hg)

/-! ## 2. The general fooling-set bound -/

/-- Entry (i, j) of the nonnegative factorization `∑_k u k i * v k j`. -/
def entry (m nr nc : Nat) (u : Fin m → Fin nr → Int) (v : Fin m → Fin nc → Int)
    (i : Fin nr) (j : Fin nc) : Int :=
  fsum m (fun k => u k i * v k j)

theorem term_nonneg (m nr nc : Nat) (u : Fin m → Fin nr → Int) (v : Fin m → Fin nc → Int)
    (hu : ∀ k i, 0 ≤ u k i) (hv : ∀ k j, 0 ≤ v k j) (i : Fin nr) (j : Fin nc) :
    ∀ k, 0 ≤ u k i * v k j := fun k => Int.mul_nonneg (hu k i) (hv k j)

/-- A nonzero entry is covered by a term with both factors positive. -/
theorem cover_term (m nr nc : Nat) (u : Fin m → Fin nr → Int) (v : Fin m → Fin nc → Int)
    (hu : ∀ k i, 0 ≤ u k i) (hv : ∀ k j, 0 ≤ v k j) (i : Fin nr) (j : Fin nc)
    (hne : entry m nr nc u v i j ≠ 0) : ∃ k, 0 < u k i ∧ 0 < v k j := by
  obtain ⟨k, hk⟩ := fsum_ne_zero_witness m _ (term_nonneg m nr nc u v hu hv i j) hne
  refine ⟨k, ?_, ?_⟩
  · rcases Decidable.em (0 < u k i) with h | h
    · exact h
    · have hz : u k i = 0 := by have := hu k i; omega
      rw [hz, Int.zero_mul] at hk
      exact absurd hk (Int.lt_irrefl 0)
  · rcases Decidable.em (0 < v k j) with h | h
    · exact h
    · have hz : v k j = 0 := by have := hv k j; omega
      rw [hz, Int.mul_zero] at hk
      exact absurd hk (Int.lt_irrefl 0)

/-- A term with both factors positive makes the entry positive. -/
theorem entry_pos_of_term (m nr nc : Nat) (u : Fin m → Fin nr → Int) (v : Fin m → Fin nc → Int)
    (hu : ∀ k i, 0 ≤ u k i) (hv : ∀ k j, 0 ≤ v k j) (i : Fin nr) (j : Fin nc)
    (k : Fin m) (hki : 0 < u k i) (hkj : 0 < v k j) : 0 < entry m nr nc u v i j :=
  fsum_pos_of_term m _ (term_nonneg m nr nc u v hu hv i j) k (Int.mul_pos hki hkj)

/-- **General fooling-set bound (kernel-checked).**  `k` cells `(row t, col t)`
that are positive and pairwise fooling in a nonnegative factorization with
`m` terms force `k ≤ m`.  Clearing denominators transfers the statement to
rational factorizations of rational nonnegative matrices (same support), so
this is the lower bound `rank₊ ≥ k` and, through the Hankel factorization
`H = O·R` of any positive carrier, `d⁺ ≥ k`. -/
theorem fooling_set_bound (m nr nc k : Nat) (u : Fin m → Fin nr → Int)
    (v : Fin m → Fin nc → Int) (hu : ∀ k i, 0 ≤ u k i) (hv : ∀ k j, 0 ≤ v k j)
    (row : Fin k → Fin nr) (col : Fin k → Fin nc)
    (hpos : ∀ t, entry m nr nc u v (row t) (col t) ≠ 0)
    (hfool : ∀ t s, t ≠ s →
      entry m nr nc u v (row t) (col s) = 0 ∨ entry m nr nc u v (row s) (col t) = 0) :
    k ≤ m := by
  have cover : ∀ t : Fin k, ∃ j : Fin m, 0 < u j (row t) ∧ 0 < v j (col t) :=
    fun t => cover_term m nr nc u v hu hv (row t) (col t) (hpos t)
  let f : Fin k → Fin m := fun t => Classical.choose (cover t)
  have hf_spec : ∀ t, 0 < u (f t) (row t) ∧ 0 < v (f t) (col t) :=
    fun t => Classical.choose_spec (cover t)
  have hf : ∀ t s, f t = f s → t = s := by
    intro t s hts
    by_cases hne : t = s
    · exact hne
    exfalso
    rcases hfool t s hne with h | h
    · -- cross cell (row t, col s) vanishes, but term f t = f s covers it
      have hpos' := entry_pos_of_term m nr nc u v hu hv (row t) (col s) (f t)
        (hf_spec t).1 (hts ▸ (hf_spec s).2)
      omega
    · have hpos' := entry_pos_of_term m nr nc u v hu hv (row s) (col t) (f s)
        (hf_spec s).1 (hts ▸ (hf_spec t).2)
      omega
  exact fin_injective_le k m f hf

/-! ## 3. Irrationality of the golden slopes: `p² + p q − q² ≠ 0` for `q ≠ 0` -/

/-- Squares modulo 5 vanish only for multiples of 5. -/
theorem five_dvd_of_five_dvd_sq (x : Nat) (h : x * x % 5 = 0) : x % 5 = 0 := by
  have hm : x * x % 5 = (x % 5) * (x % 5) % 5 := Nat.mul_mod x x 5
  rw [hm] at h
  have hb : x % 5 < 5 := Nat.mod_lt x (by decide)
  rcases (by omega : x % 5 = 0 ∨ x % 5 = 1 ∨ x % 5 = 2 ∨ x % 5 = 3 ∨ x % 5 = 4) with
    h0 | h1 | h2 | h3 | h4
  · exact h0
  · rw [h1] at h; simp at h
  · rw [h2] at h; simp at h
  · rw [h3] at h; simp at h
  · rw [h4] at h; simp at h

/-- Descent: `x·x = 5·y·y` in ℕ forces `y = 0`. -/
theorem sqrt5_descent : ∀ (n : Nat) (x y : Nat), y ≤ n → x * x = 5 * (y * y) → y = 0 := by
  intro n
  induction n with
  | zero => intro x y hy _; omega
  | succ n ih =>
    intro x y hy hxy
    by_cases hy0 : y = 0
    · exact hy0
    · -- 5 ∣ x
      have h5x : x % 5 = 0 := by
        apply five_dvd_of_five_dvd_sq
        rw [hxy]
        exact Nat.mul_mod_right 5 (y * y)
      obtain ⟨x', hx'⟩ : ∃ x', x = 5 * x' := ⟨x / 5, by omega⟩
      -- 25 x'² = 5 y²  ⇒  5 x'² = y²
      have h2 : y * y = 5 * (x' * x') := by
        rw [hx'] at hxy
        have : 5 * (5 * (x' * x')) = 5 * (y * y) := by
          rw [← hxy]
          simp [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
        exact (Nat.eq_of_mul_eq_mul_left (by decide : 0 < 5) this).symm
      have h5y : y % 5 = 0 := by
        apply five_dvd_of_five_dvd_sq
        rw [h2]
        exact Nat.mul_mod_right 5 (x' * x')
      obtain ⟨y', hy'⟩ : ∃ y', y = 5 * y' := ⟨y / 5, by omega⟩
      have h3 : x' * x' = 5 * (y' * y') := by
        rw [hy'] at h2
        have : 5 * (5 * (y' * y')) = 5 * (x' * x') := by
          rw [← h2]
          simp [Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]
        exact (Nat.eq_of_mul_eq_mul_left (by decide : 0 < 5) this).symm
      have hlt : y' ≤ n := by omega
      have := ih x' y' hlt h3
      omega

theorem sqrt5_irrational_nat (x y : Nat) (h : x * x = 5 * (y * y)) : y = 0 :=
  sqrt5_descent y x y (Nat.le_refl y) h

/-- **Kernel-checked core of the irrational-contact obstruction.**  No integers
`p, q` with `q ≠ 0` satisfy `p² + p q − q² = 0`; equivalently the roots of
`s² + s − 1` (the eigen-slopes of `[[2,1],[1,1]]`, i.e. the golden-ratio
directions) are irrational. -/
theorem sq_sum (a b : Int) : (a + b) * (a + b) = a * a + 2 * (a * b) + b * b := by
  simp only [Int.add_mul, Int.mul_add]
  rw [Int.mul_comm b a]
  omega

theorem golden_slope_irrational (p q : Int) (hq : q ≠ 0) : p * p + p * q - q * q ≠ 0 := by
  intro h
  -- (2p + q)² = 5 q²
  have hA : (2 * p) * (2 * p) = 2 * (2 * (p * p)) := by
    rw [Int.mul_assoc, Int.mul_left_comm p 2 p]
  have hB : (2 * p) * q = 2 * (p * q) := Int.mul_assoc 2 p q
  have hsq : (2 * p + q) * (2 * p + q) = 5 * (q * q) := by
    rw [sq_sum, hA, hB]
    omega
  -- pass to natural numbers through natAbs
  have hn : (2 * p + q).natAbs * (2 * p + q).natAbs = 5 * (q.natAbs * q.natAbs) := by
    have := congrArg Int.natAbs hsq
    rw [Int.natAbs_mul, Int.natAbs_mul, Int.natAbs_mul] at this
    simpa using this
  have := sqrt5_irrational_nat _ _ hn
  exact hq (Int.natAbs_eq_zero.mp this)

/-! ## 4. Menus are functions of supports: a counting bound -/

/-- Binary code of a support predicate on `Fin m` (bit `i` = `S i`). -/
def supportCode : (m : Nat) → (Fin m → Bool) → Nat
  | 0, _ => 0
  | m + 1, S => (if S ⟨0, Nat.succ_pos m⟩ then 1 else 0)
                + 2 * supportCode m (fun i => S ⟨i.val + 1, Nat.succ_lt_succ i.isLt⟩)

theorem supportCode_lt : ∀ (m : Nat) (S : Fin m → Bool), supportCode m S < 2 ^ m := by
  intro m
  induction m with
  | zero => intro S; simp [supportCode]
  | succ m ih =>
    intro S
    simp only [supportCode]
    have := ih (fun i => S ⟨i.val + 1, Nat.succ_lt_succ i.isLt⟩)
    have h2 : 2 ^ (m + 1) = 2 * 2 ^ m := by rw [Nat.pow_succ]; omega
    rw [h2]
    split <;> omega

theorem supportCode_injective : ∀ (m : Nat) (S T : Fin m → Bool),
    supportCode m S = supportCode m T → S = T := by
  intro m
  induction m with
  | zero => intro S T _; funext i; exact absurd i.isLt (Nat.not_lt_zero _)
  | succ m ih =>
    intro S T h
    simp only [supportCode] at h
    have hS := supportCode_lt m (fun i => S ⟨i.val + 1, Nat.succ_lt_succ i.isLt⟩)
    have hT := supportCode_lt m (fun i => T ⟨i.val + 1, Nat.succ_lt_succ i.isLt⟩)
    have h0 : S ⟨0, Nat.succ_pos m⟩ = T ⟨0, Nat.succ_pos m⟩ := by
      show S 0 = T 0
      cases hs : S 0 <;> cases ht : T 0 <;>
        simp [hs, ht] at h <;> first | rfl | omega
    have hrest : (fun i : Fin m => S ⟨i.val + 1, Nat.succ_lt_succ i.isLt⟩)
               = (fun i : Fin m => T ⟨i.val + 1, Nat.succ_lt_succ i.isLt⟩) := by
      apply ih
      cases hs : S 0 <;> cases ht : T 0 <;>
        simp [hs, ht] at h <;> omega
    funext i
    rcases i with ⟨iv, hi⟩
    cases iv with
    | zero => exact h0
    | succ j =>
      have := congrFun hrest ⟨j, Nat.lt_of_succ_lt_succ hi⟩
      exact this

/-- **Menu-count bound.**  If `k` histories have pairwise distinct menus and
each menu is a function of the support of the current law in an `m`-state
carrier, then `k ≤ 2^m`.  (Part I Lemma 8.4; the empty support never occurs
for a history of positive probability, giving `2^m − 1` in practice.) -/
theorem menu_count_bound {Menu : Type} (m k : Nat)
    (support : Fin k → (Fin m → Bool)) (menuOf : (Fin m → Bool) → Menu)
    (hdistinct : ∀ a b, menuOf (support a) = menuOf (support b) → a = b) :
    k ≤ 2 ^ m := by
  let f : Fin k → Fin (2 ^ m) := fun a => ⟨supportCode m (support a), supportCode_lt m _⟩
  have hf : ∀ a b, f a = f b → a = b := by
    intro a b hab
    have hv := congrArg Fin.val hab
    simp only [f] at hv
    have := supportCode_injective m _ _ hv
    exact hdistinct a b (by rw [this])
  exact fin_injective_le k (2 ^ m) f hf

end PositiveCarrierII

end ObservationalSUCC
