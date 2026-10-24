import BBPSourceGenesis

/-!
# Selected BBP states, dyadic prefixSum erasure and centered signed Abel transport

All statements are finite identities or inequalities. The original source
`tail` and `liftedOrbit` retain their separately checked identification with pi.
Changing the initial state is explicitly typed; no declaration asserts decay
of the authentic mixed-source interference or pi normality.
-/

noncomputable section
open scoped BigOperators ComplexConjugate
open ObservationalSUCC.BaileyCrandall ObservationalSUCC.PiSourceGenesis

namespace ObservationalSUCC.CyclotomicSelectedSource

/-- The unique initial state selecting the zero corrected orbit. It is a
real-state control, not a rational-primary-component certificate. -/
theorem selected_zero_lift (n : ℕ) :
    liftedFrom (-tail 0) n = -tail n := by
  have h := liftedFrom_source_selection (-tail 0) n
  linarith

/-- The genuine finite transient made by a base-16 rational initial shift. -/
theorem dyadic_lift_difference (c : ℤ) (K n : ℕ) :
    liftedFrom ((c : ℝ)/16^K) (K+n) - liftedOrbit (K+n) =
      16^n*(c : ℝ) := by
  unfold liftedFrom
  rw [pow_add]
  have h : (16 : ℝ)^K ≠ 0 := pow_ne_zero _ (by norm_num)
  field_simp
  ring

/-- After K steps the dyadically changed source and the authentic source
are exactly the same circle state, not merely close. -/
theorem dyadic_state_erased (c : ℤ) (K n : ℕ) :
    (liftedFrom ((c : ℝ)/16^K) (K+n) : AddCircle (1 : ℝ)) =
      circleOrbit (K+n) := by
  have hd := dyadic_lift_difference c K n
  have heq : liftedFrom ((c : ℝ)/16^K) (K+n) =
      liftedOrbit (K+n)+16^n*(c : ℝ) := by linarith
  have hz : ((16^n*(c : ℝ) : ℝ) : AddCircle (1 : ℝ)) = 0 := by
    apply (AddCircle.coe_eq_zero_iff (1 : ℝ)).2
    refine ⟨(16 : ℤ)^n*c, ?_⟩
    simp only [zsmul_eq_mul, Int.cast_mul, Int.cast_pow, Int.cast_ofNat, mul_one]
  rw [heq, AddCircle.coe_add, hz, add_zero]
  rfl

/-- Exact source-state error before any fractional-part representative is
chosen. Its growth is paid explicitly rather than hidden in continuity. -/
theorem selected_state_error (s : ℝ) (n : ℕ) :
    liftedFrom s n - (-tail n) = 16^n*(s+tail 0) := by
  have h := liftedFrom_source_selection s n
  linarith

theorem selected_character_error (a s : ℝ) (n : ℕ) :
    ‖phase a (liftedFrom s n)-phase a (-tail n)‖ ≤
      |a| *16^n*|s+tail 0| := by
  have h := phase_lipschitz a (-tail n) (liftedFrom s n)
  rw [selected_state_error, abs_mul, abs_of_nonneg (by positivity : (0 : ℝ) ≤ 16^n)] at h
  simpa only [mul_assoc] using h

def selectedWindow (a s : ℝ) (J L : ℕ) : ℂ :=
  ∑ j ∈ Finset.range L, phase a (liftedFrom s (J+j+1))

/-- A finite-state counterfeit budget; this theorem does not apply the
changed-state conclusion to the source-selected state s=0 for free. -/
theorem selected_window_error (a s : ℝ) (J L : ℕ) :
    ‖selectedWindow a s J L-selectedWindow a (-tail 0) J L‖ ≤
      |a| *|s+tail 0| *(∑ j ∈ Finset.range L, (16 : ℝ)^(J+j+1)) := by
  unfold selectedWindow
  rw [← Finset.sum_sub_distrib]
  calc
    _ ≤ ∑ j ∈ Finset.range L,
        ‖phase a (liftedFrom s (J+j+1))-phase a (liftedFrom (-tail 0) (J+j+1))‖ :=
      norm_sum_le _ _
    _ ≤ ∑ j ∈ Finset.range L, |a| *16^(J+j+1)*|s+tail 0| := by
      apply Finset.sum_le_sum
      intro j hj
      rw [selected_zero_lift]
      exact selected_character_error a s _
    _ = _ := by rw [Finset.mul_sum]; apply Finset.sum_congr rfl; intro j hj; ring

/-- One fixed wrong initial state produces nearly constant finite windows
under the very same forcing. This uses the authentic BBP tail bound. -/
theorem selected_zero_window_bound (a : ℝ) (J L : ℕ) :
    ‖selectedWindow a (-tail 0) J L - (L : ℂ)‖ ≤
      |a| /(32*((J : ℝ)+1)) := by
  have hsum : (L : ℂ) = ∑ j ∈ Finset.range L, (1 : ℂ) := by simp
  rw [hsum]
  unfold selectedWindow
  rw [← Finset.sum_sub_distrib]
  calc
    _ ≤ ∑ j ∈ Finset.range L, ‖phase a (liftedFrom (-tail 0) (J+j+1))-1‖ :=
      norm_sum_le _ _
    _ ≤ ∑ j ∈ Finset.range L, |a| *tail (J+j+1) := by
      apply Finset.sum_le_sum
      intro j hj
      rw [selected_zero_lift]
      have hp := phase_lipschitz a 0 (-tail (J+j+1))
      simpa [phase, abs_of_pos (tail_pos _)] using hp
    _ = |a| * ∑ j ∈ Finset.range L, tail (J+1+j) := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro j hj
      congr 2; omega
    _ ≤ |a| * ((1/32 : ℝ)*(1/((J : ℝ)+1)-1/((J : ℝ)+L+1))) :=
      mul_le_mul_of_nonneg_left (tail_block_sum_bound J L) (abs_nonneg a)
    _ ≤ |a| /(32*((J : ℝ)+1)) := by
      have hp : 0 ≤ 1/((J : ℝ)+L+1) := by positivity
      have h := mul_nonneg (abs_nonneg a) hp
      have heq : |a| /(32*((J : ℝ)+1)) = |a| *((1/32 : ℝ)*(1/((J : ℝ)+1))) := by
        simp only [div_eq_mul_inv, mul_inv_rev]
        ring
      rw [heq]
      nlinarith

/-- Combined error budget for rational initial-state selectors. -/
theorem selected_window_constant_bound (a s : ℝ) (J L : ℕ) :
    ‖selectedWindow a s J L - (L : ℂ)‖ ≤
      |a| *|s+tail 0| *(∑ j ∈ Finset.range L, (16 : ℝ)^(J+j+1)) +
      |a| /(32*((J : ℝ)+1)) := by
  calc
    _ ≤ ‖selectedWindow a s J L-selectedWindow a (-tail 0) J L‖ +
        ‖selectedWindow a (-tail 0) J L-(L : ℂ)‖ := by
      simpa only [dist_eq_norm] using dist_triangle
        (selectedWindow a s J L) (selectedWindow a (-tail 0) J L) (L : ℂ)
    _ ≤ _ := add_le_add (selected_window_error a s J L) (selected_zero_window_bound a J L)

def prefixSum (u : ℕ → ℂ) (n : ℕ) : ℂ := ∑ s ∈ Finset.range n, u s

theorem prefixSum_succ (u : ℕ → ℂ) (n : ℕ) : prefixSum u (n+1) = prefixSum u n+u n := by
  exact Finset.sum_range_succ _ _

/-- Signed summation by parts for the precise block-centered interference.
No absolute values are taken until the following estimate. -/
theorem centered_abel_identity (u v : ℕ → ℂ) (n : ℕ) :
    (∑ s ∈ Finset.range (n+1), u s*(v s-v 0)) =
      prefixSum u (n+1)*(v n-v 0) -
        ∑ s ∈ Finset.range n, prefixSum u (s+1)*(v (s+1)-v s) := by
  induction n with
  | zero => simp [prefixSum]
  | succ n ih =>
    rw [Finset.sum_range_succ, ih, Finset.sum_range_succ, prefixSum_succ u (n+1)]
    ring

/-- The correct input for weighted cancellation is an incomplete-prefixSum
bound as well as a complementary variation bound. A full-period bound alone
is not a hypothesis of this theorem. -/
theorem centered_abel_bound (u v : ℕ → ℂ) (n : ℕ) (M : ℝ)
    (hu : ∀ k ≤ n+1, ‖prefixSum u k‖ ≤ M) :
    ‖∑ s ∈ Finset.range (n+1), u s*(v s-v 0)‖ ≤
      M*(‖v n-v 0‖ + ∑ s ∈ Finset.range n, ‖v (s+1)-v s‖) := by
  rw [centered_abel_identity]
  calc
    _ ≤ ‖prefixSum u (n+1)*(v n-v 0)‖ +
        ‖∑ s ∈ Finset.range n, prefixSum u (s+1)*(v (s+1)-v s)‖ := norm_sub_le _ _
    _ ≤ M*‖v n-v 0‖ + ∑ s ∈ Finset.range n, M*‖v (s+1)-v s‖ := by
      apply add_le_add
      · rw [norm_mul]
        exact mul_le_mul_of_nonneg_right (hu _ le_rfl) (norm_nonneg _)
      · apply (norm_sum_le _ _).trans
        apply Finset.sum_le_sum
        intro s hs
        rw [norm_mul]
        exact mul_le_mul_of_nonneg_right (hu _ (by have := Finset.mem_range.mp hs; omega))
          (norm_nonneg _)
    _ = _ := by rw [← Finset.mul_sum]; ring

section FiniteClock
variable {G : Type*} [Fintype G] [AddCommGroup G]

def clockCorrelation (u : G → ℂ) (d : G) : ℂ :=
  ∑ s, u (s+d) * conj (u s)

/-- Finite Wiener--Khinchin identity with the actual complex signs.
The hypotheses describe a unit-modulus temporal character. -/
theorem twisted_clock_identity (u χ : G → ℂ)
    (hχ : ∀ s d, χ (s+d)=χ s*χ d) (hunit : ∀ s, ‖χ s‖=1) :
    (∑ s, u s*χ s) * conj (∑ s, u s*χ s) =
      ∑ d, clockCorrelation u d * χ d := by
  classical
  have hc (s : G) : χ s * conj (χ s) = 1 := by
    rw [Complex.mul_conj, Complex.normSq_eq_norm_sq, hunit]
    norm_num
  have hp (s d : G) : u (s+d)*conj (u s)*χ d =
      (u (s+d)*χ (s+d))*conj (u s*χ s) := by
    rw [hχ s d, map_mul]
    calc
      _ = u (s+d)*conj (u s)*χ d*(χ s*conj (χ s)) := by rw [hc]; ring
      _ = _ := by ring
  have ht (s : G) : (∑ d, u (s+d)*χ (s+d)) = ∑ d, u d*χ d := by
    have hb : Function.Bijective (fun d : G => s+d) := by
      constructor
      · intro a b hab
        exact add_left_cancel hab
      · intro b
        exact ⟨b-s, by simp [sub_eq_add_neg, add_comm, add_left_comm]⟩
    exact hb.sum_comp (fun d => u d*χ d)
  symm
  simp only [clockCorrelation, Finset.sum_mul]
  rw [Finset.sum_comm]
  simp_rw [hp, ← Finset.sum_mul, ht]
  rw [← Finset.mul_sum, ← map_sum]

/-- Every temporal twist is controlled by the full collection of nonzero
local lags. This is the finite algebra required before applying a subgroup
cancellation theorem; it assumes no weighted BGK estimate. -/
theorem twisted_clock_square_bound (u χ : G → ℂ) (C E : ℝ)
    (hχ : ∀ s d, χ (s+d)=χ s*χ d) (hunit : ∀ s, ‖χ s‖=1)
    (hzero : ‖clockCorrelation u 0‖ ≤ C)
    (hother : ∀ d ≠ 0, ‖clockCorrelation u d‖ ≤ E) :
    ‖∑ s, u s*χ s‖^2 ≤ C + (Fintype.card G-1 : ℕ)*E := by
  classical
  have hid := twisted_clock_identity u χ hχ hunit
  have hn : ‖∑ s, u s*χ s‖^2 = ‖∑ d, clockCorrelation u d*χ d‖ := by
    rw [← hid, norm_mul, RCLike.norm_conj, pow_two]
  rw [hn]
  calc
    _ ≤ ∑ d, ‖clockCorrelation u d*χ d‖ := norm_sum_le _ _
    _ = ∑ d, ‖clockCorrelation u d‖ := by simp [norm_mul, hunit]
    _ ≤ ∑ d : G, if d=0 then C else E := by
      apply Finset.sum_le_sum
      intro d hd
      split_ifs with h
      · subst d; exact hzero
      · exact hother d h
    _ = C + (Fintype.card G-1 : ℕ)*E := by
      rw [← Finset.sum_erase_add _ _ (Finset.mem_univ (0 : G))]
      simp only [ite_true]
      have he : (∑ d ∈ Finset.univ.erase (0 : G), if d=0 then C else E) =
          (Fintype.card G-1 : ℕ)*E := by
        calc
          _ = ∑ d ∈ Finset.univ.erase (0 : G), E := by
            apply Finset.sum_congr rfl
            intro d hd
            simp [(Finset.mem_erase.mp hd).1]
          _ = _ := by simp
      rw [he]
      ring

end FiniteClock

end ObservationalSUCC.CyclotomicSelectedSource
