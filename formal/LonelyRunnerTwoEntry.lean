import LonelyRunnerDeletion
import Mathlib.Data.Rat.Cast.Order

/-!
Full upper-half one-insertion hole, including rational-time and real-distance
quantifiers. For n >= 5, (n-1)/2 < r < s <= n-1 and every w >= n, the
retained source ([n-1] minus {r,s}) union {w} has a rational time in [0,1]
at which every speed is strictly farther than 1/n from every integer.

If one removed speed does not divide w, use its reciprocal as the time.
If w = r*m = s*l, positivity and r < s force l < m. Thus
m*(n-r) >= n-1+m. The explicit perturbation (n+1)/(n^2*w) is below the
retained source's safe radius and moves w into the open good arc. The final
export proves this construction for the actual retained-plus-inserted source;
it does not assume a separation certificate or a one-insertion hole.

The unrestricted-deletion Gamma bound and complete finite census remain
paper-plus-exact-enumeration results; this file certifies the upper-half
universal hole theorem only, together with its supporting lemmas.
-/

namespace ObservationalSUCC.LonelyRunnerTwoEntry

open ObservationalSUCC.LonelyRunnerDeletion

theorem common_multiple_margin (n r s w : ℤ)
    (hn : 5 ≤ n) (hr : 1 ≤ r) (hrs : r < s) (hs : s ≤ n-1)
    (hw : n ≤ w) (hd : r ∣ w) (he : s ∣ w) :
    ∃ m : ℤ, w = r*m ∧ 1 ≤ m ∧ (n+1)*(n-1) < n*m*(n-r) := by
  obtain ⟨m, hm⟩ := hd
  obtain ⟨l, hl⟩ := he
  have hm0 : 1 ≤ m := by
    by_contra h
    have : m ≤ 0 := by omega
    nlinarith
  have hl0 : 1 ≤ l := by
    by_contra h
    have : l ≤ 0 := by omega
    nlinarith
  have hml : l < m := by
    by_contra h
    have : m ≤ l := by omega
    nlinarith [mul_nonneg (show 0 ≤ l-m by omega) (show 0 ≤ r by omega)]
  have hprod : l*s ≤ (m-1)*(n-1) := by
    nlinarith [mul_nonneg (show 0 ≤ m-1-l by omega) (show 0 ≤ n-1 by omega),
      mul_nonneg (show 0 ≤ l by omega) (show 0 ≤ n-1-s by omega)]
  have hmargin : n-1+m ≤ m*(n-r) := by nlinarith
  refine ⟨m, hm, hm0, ?_⟩
  nlinarith [mul_nonneg (show 0 ≤ n by omega) (show 0 ≤ m*(n-r)-(n-1+m) by omega)]

theorem nonmultiple_integer_gap (r w z : ℤ) (hd : ¬r ∣ w) :
    1 ≤ |w-z*r| := by
  have hne : w-z*r ≠ 0 := by
    intro h
    apply hd
    exact ⟨z, by nlinarith⟩
  have : w-z*r ≤ -1 ∨ 1 ≤ w-z*r := by omega
  rcases this with h | h
  · rw [abs_of_nonpos (by omega)]
    omega
  · exact le_trans h (le_abs_self _)

theorem perturbation_gap (i c u z δ : ℝ) (hi : 0 ≤ i) (hu : 0 ≤ u)
    (hc : δ + i*u < |i*c-z|) : δ < |i*(c+u)-z| := by
  have htri : |i*c-z| ≤ |i*(c+u)-z| + i*u := by
    calc
      |i*c-z| = |(i*(c+u)-z)+(-i*u)| := by congr 1; ring
      _ ≤ |i*(c+u)-z| + |-i*u| := abs_add _ _
      _ = |i*(c+u)-z| + i*u := by
        rw [abs_mul, abs_neg, abs_of_nonneg hi, abs_of_nonneg hu]
  linarith

theorem fractional_integer_gap (m z : ℤ) (x δ : ℝ)
    (hlo : δ < x) (hhi : x < 1-δ) : δ < |(m:ℝ)+x-(z:ℝ)| := by
  have hz : z ≤ m ∨ m+1 ≤ z := by omega
  rcases hz with hz | hz
  · have hzR : (z:ℝ) ≤ m := by exact_mod_cast hz
    exact lt_of_lt_of_le (by linarith) (le_abs_self _)
  · have hzR : (m:ℝ)+1 ≤ z := by exact_mod_cast hz
    exact lt_of_lt_of_le (by linarith) (neg_le_abs _)

theorem upper_half_nonmultiple_witness (n r w : ℤ)
    (hn : 5 ≤ n) (hr : 1 ≤ r) (hrn : r < n) (hupper : n-1 < 2*r)
    (hd : ¬r ∣ w) :
    ∃ t : ℚ, 0 ≤ t ∧ t ≤ 1 ∧
      (∀ i : ℤ, 1 ≤ i → i < n → i ≠ r → ∀ z : ℤ,
        1/(n:ℝ) < |(i:ℝ)*(t:ℝ)-(z:ℝ)|) ∧
      (∀ z : ℤ, 1/(n:ℝ) < |(w:ℝ)*(t:ℝ)-(z:ℝ)|) := by
  have hnR : (0:ℝ) < n := by exact_mod_cast (show 0 < n by omega)
  have hrR : (0:ℝ) < r := by exact_mod_cast (show 0 < r by omega)
  have hrQ : (1:ℚ) ≤ r := by exact_mod_cast hr
  have hcmp : (1:ℝ)/(n:ℝ) < 1/(r:ℝ) := by
    apply (div_lt_div_iff₀ hnR hrR).mpr
    simpa using (show (r:ℝ) < n by exact_mod_cast hrn)
  refine ⟨1/(r:ℚ), by positivity, (div_le_one (by linarith)).mpr hrQ, ?_, ?_⟩
  · intro i hi hin hne z
    have hg := integer_gap_to_real 1 r i z 1 (by omega)
      (by simpa using centre_integer_gap r i z hr ⟨hi,by omega⟩ hne)
    exact lt_of_lt_of_le hcmp (by simpa using hg)
  · intro z
    have hg := integer_gap_to_real 1 r w z 1 (by omega)
      (by simpa using nonmultiple_integer_gap r w z hd)
    exact lt_of_lt_of_le hcmp (by simpa using hg)

theorem upper_half_common_multiple_witness (n r s w : ℤ)
    (hn : 5 ≤ n) (hr : 1 ≤ r) (hrs : r < s) (hs : s ≤ n-1)
    (hupper : n-1 < 2*r) (hw : n ≤ w) (hd : r ∣ w) (he : s ∣ w) :
    ∃ t : ℚ, 0 ≤ t ∧ t ≤ 1 ∧
      (∀ i : ℤ, 1 ≤ i → i < n → i ≠ r → ∀ z : ℤ,
        1/(n:ℝ) < |(i:ℝ)*(t:ℝ)-(z:ℝ)|) ∧
      (∀ z : ℤ, 1/(n:ℝ) < |(w:ℝ)*(t:ℝ)-(z:ℝ)|) := by
  obtain ⟨m, hm, hm0, hmargin⟩ := common_multiple_margin n r s w hn hr hrs hs hw hd he
  have hn5 : (5:ℝ) ≤ n := by exact_mod_cast hn
  have hnR : (0:ℝ) < n := by linarith
  have hr2 : (2:ℝ) ≤ r := by exact_mod_cast (show 2 ≤ r by omega)
  have hrR : (0:ℝ) < r := by linarith
  have hwR : (0:ℝ) < w := by exact_mod_cast (show 0 < w by omega)
  have hnm : (0:ℝ) < (n:ℝ)-1 := by linarith
  have hmR : (w:ℝ) = (r:ℝ)*(m:ℝ) := by exact_mod_cast hm
  have hmarginR : ((n:ℝ)+1)*((n:ℝ)-1) < (n:ℝ)*(m:ℝ)*((n:ℝ)-(r:ℝ)) := by
    exact_mod_cast hmargin
  let u : ℝ := ((n:ℝ)+1)/((n:ℝ)^2*(w:ℝ))
  have hu0 : 0 < u := by dsimp [u]; positivity
  have hun : u < ((n:ℝ)-(r:ℝ))/((n:ℝ)*(r:ℝ)*((n:ℝ)-1)) := by
    dsimp [u]
    apply (div_lt_div_iff₀ (by positivity) (by positivity)).mpr
    rw [hmR]
    have hh := mul_lt_mul_of_pos_left hmarginR (mul_pos hnR hrR)
    nlinarith [hh]
  have hsafe : ((n:ℝ)-1)*u < 1/(r:ℝ)-1/(n:ℝ) := by
    have hh := mul_lt_mul_of_pos_left hun hnm
    have heq : ((n:ℝ)-1)*(((n:ℝ)-(r:ℝ))/((n:ℝ)*(r:ℝ)*((n:ℝ)-1))) =
        1/(r:ℝ)-1/(n:ℝ) := by field_simp; ring
    rwa [heq] at hh
  have hui : u < 1/(r:ℝ) := by
    have hmul : u ≤ ((n:ℝ)-1)*u := by nlinarith
    have hrec : (0:ℝ) < 1/(n:ℝ) := by positivity
    linarith
  let t : ℚ := 1/(r:ℚ)+((n:ℚ)+1)/((n:ℚ)^2*(w:ℚ))
  have ht : (t:ℝ) = 1/(r:ℝ)+u := by simp [t, u]
  have ht0 : (0:ℝ) ≤ (t:ℝ) := by rw [ht]; positivity
  have ht1 : (t:ℝ) ≤ 1 := by
    rw [ht]
    have hrec : (1:ℝ)/(r:ℝ) ≤ 1/2 := by
      apply (div_le_div_iff₀ hrR (by norm_num)).mpr
      linarith
    linarith
  refine ⟨t, by exact_mod_cast ht0, by exact_mod_cast ht1, ?_, ?_⟩
  · intro i hi hin hne z
    have hiR : (0:ℝ) ≤ i := by exact_mod_cast (show 0 ≤ i by omega)
    have hinR : (i:ℝ) ≤ (n:ℝ)-1 := by exact_mod_cast (show i ≤ n-1 by omega)
    have hg := integer_gap_to_real 1 r i z 1 (by omega)
      (by simpa using centre_integer_gap r i z hr ⟨hi,by omega⟩ hne)
    have hbase : (1:ℝ)/(r:ℝ) ≤ |(i:ℝ)*(1/(r:ℝ))-(z:ℝ)| := by simpa using hg
    rw [ht]
    apply perturbation_gap (i:ℝ) (1/(r:ℝ)) u (z:ℝ) (1/(n:ℝ)) hiR (le_of_lt hu0)
    have hmul : (i:ℝ)*u ≤ ((n:ℝ)-1)*u := mul_le_mul_of_nonneg_right hinR (le_of_lt hu0)
    linarith
  · intro z
    have hwu : (w:ℝ)*u = ((n:ℝ)+1)/(n:ℝ)^2 := by dsimp [u]; field_simp; ring
    have hlo : (1:ℝ)/(n:ℝ) < ((n:ℝ)+1)/(n:ℝ)^2 := by
      apply (div_lt_div_iff₀ hnR (by positivity)).mpr
      nlinarith
    have hhi : ((n:ℝ)+1)/(n:ℝ)^2 < 1-1/(n:ℝ) := by
      apply (div_lt_iff₀ (by positivity)).mpr
      have heq : (1-1/(n:ℝ))*(n:ℝ)^2 = (n:ℝ)^2-(n:ℝ) := by field_simp; ring
      rw [heq]
      nlinarith
    have heq : (w:ℝ)*(t:ℝ)-(z:ℝ) = (m:ℝ)+(w:ℝ)*u-(z:ℝ) := by
      rw [ht, hmR]
      field_simp
      ring
    rw [heq, hwu]
    exact fractional_integer_gap m z _ _ hlo hhi

theorem upper_half_one_insertion_hole (n r s w : ℤ)
    (hn : 5 ≤ n) (hr : 1 ≤ r) (hrs : r < s) (hs : s ≤ n-1)
    (hupper : n-1 < 2*r) (hw : n ≤ w) :
    ∃ t : ℚ, 0 ≤ t ∧ t ≤ 1 ∧
      ∀ i : ℤ, ((1 ≤ i ∧ i < n ∧ i ≠ r ∧ i ≠ s) ∨ i = w) →
        ∀ z : ℤ, 1/(n:ℝ) < |(i:ℝ)*(t:ℝ)-(z:ℝ)| := by
  by_cases hd : r ∣ w
  · by_cases he : s ∣ w
    · obtain ⟨t, ht0, ht1, hbase, hwit⟩ :=
        upper_half_common_multiple_witness n r s w hn hr hrs hs hupper hw hd he
      refine ⟨t, ht0, ht1, ?_⟩
      intro i hi z
      rcases hi with ⟨hi, hin, hne, _⟩ | rfl
      · exact hbase i hi hin hne z
      · exact hwit z
    · obtain ⟨t, ht0, ht1, hbase, hwit⟩ :=
        upper_half_nonmultiple_witness n s w hn (by omega) (by omega) (by omega) he
      refine ⟨t, ht0, ht1, ?_⟩
      intro i hi z
      rcases hi with ⟨hi, hin, _, hne⟩ | rfl
      · exact hbase i hi hin hne z
      · exact hwit z
  · obtain ⟨t, ht0, ht1, hbase, hwit⟩ :=
      upper_half_nonmultiple_witness n r w hn hr (by omega) hupper hd
    refine ⟨t, ht0, ht1, ?_⟩
    intro i hi z
    rcases hi with ⟨hi, hin, hne, _⟩ | rfl
    · exact hbase i hi hin hne z
    · exact hwit z

end ObservationalSUCC.LonelyRunnerTwoEntry

#print axioms ObservationalSUCC.LonelyRunnerTwoEntry.common_multiple_margin
#print axioms ObservationalSUCC.LonelyRunnerTwoEntry.nonmultiple_integer_gap
#print axioms ObservationalSUCC.LonelyRunnerTwoEntry.perturbation_gap
#print axioms ObservationalSUCC.LonelyRunnerTwoEntry.fractional_integer_gap
#print axioms ObservationalSUCC.LonelyRunnerTwoEntry.upper_half_nonmultiple_witness
#print axioms ObservationalSUCC.LonelyRunnerTwoEntry.upper_half_common_multiple_witness
#print axioms ObservationalSUCC.LonelyRunnerTwoEntry.upper_half_one_insertion_hole
