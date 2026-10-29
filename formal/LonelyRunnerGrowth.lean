import LonelyRunnerTwoEntry
import Mathlib.Data.Real.Archimedean
import Mathlib.Data.Finset.Max
import Mathlib.Data.Int.Interval

/-!
Actual source geometry and an unconditional upper-half cubic growth theorem.

Bad and Covers below are predicates on every real time and integer winding.
A finite source's good point produces a positive open gap whose endpoints
retain actual source labels. Integer numerator spacing includes the crucial
same-speed case. A covered open interval lies in one bad band; a two-runner
cover has a geometric width bound when a whole first-runner good arc cannot
fit in a second-runner bad band.

Combining these results with the previously proved full one-insertion hole
gives w2 <= 2(n-1)w1 and w2 < 3*n^3 for two deleted speeds in the upper half.
No supplied gap, occupancy estimate, generic Lonely Runner conjecture, or
classification theorem is assumed by upper_half_cubic_growth. The general
inserted_speed_bound_from_hole exposes its actual uncovered-point hypothesis;
it is not an unconditional arbitrary-deletion theorem. No unrestricted Gamma
or new academic-priority claim is made by this formalization.
-/

namespace ObservationalSUCC.LonelyRunnerGrowth

open ObservationalSUCC.LonelyRunnerTwoEntry
open ObservationalSUCC.LonelyRunnerDeletion

/-- The actual unshifted closed bad set, quantified over integer windings. -/
def Bad (v δ t : ℝ) : Prop := ∃ k : ℤ, |v*t-(k:ℝ)| ≤ δ

/-- Pointwise coverage of the real unit interval by the declared source. -/
def Covers (V : Finset ℤ) (δ : ℝ) : Prop :=
  ∀ t : ℝ, 0 ≤ t → t ≤ 1 → ∃ v ∈ V, Bad (v:ℝ) δ t

theorem covered_open_interval_one_band (v δ a b : ℝ)
    (hv : 0 < v) (hδ : δ < 1/2) (hab : a < b)
    (hc : ∀ t : ℝ, a < t → t < b → Bad v δ t) :
    ∃ k : ℤ, (k:ℝ)-δ ≤ v*a ∧ v*b ≤ (k:ℝ)+δ := by
  obtain ⟨k, hk⟩ := hc ((a+b)/2) (by linarith) (by linarith)
  obtain ⟨hkl, hku⟩ := abs_le.mp hk
  refine ⟨k, ?_, ?_⟩
  · by_contra h
    have ha : v*a < (k:ℝ)-δ := lt_of_not_ge h
    let x := (max (v*a) ((k:ℝ)-1+δ)+((k:ℝ)-δ))/2
    have hxlo : max (v*a) ((k:ℝ)-1+δ) < x := by
      dsimp [x]
      have hh : max (v*a) ((k:ℝ)-1+δ) < (k:ℝ)-δ := max_lt ha (by linarith)
      linarith
    have hxhi : x < (k:ℝ)-δ := by
      dsimp [x]
      have hh : max (v*a) ((k:ℝ)-1+δ) < (k:ℝ)-δ := max_lt ha (by linarith)
      linarith
    have hxa : v*a < x := lt_of_le_of_lt (le_max_left _ _) hxlo
    have hxb : x < v*b := by nlinarith [mul_pos hv (show 0 < b-a by linarith)]
    obtain ⟨j, hj⟩ := hc (x/v) ((lt_div_iff₀ hv).mpr (by nlinarith))
      ((div_lt_iff₀ hv).mpr (by nlinarith))
    have hg := fractional_integer_gap (k-1) j (x-((k:ℝ)-1)) δ
      (by have := lt_of_le_of_lt (le_max_right (v*a) ((k:ℝ)-1+δ)) hxlo; linarith)
      (by linarith)
    have hxe : v*(x/v) = x := by field_simp
    rw [hxe] at hj
    have hge : δ < |x-(j:ℝ)| := by convert hg using 1 <;> push_cast <;> congr 1 <;> ring
    linarith
  · by_contra h
    have hb : (k:ℝ)+δ < v*b := lt_of_not_ge h
    let x := (((k:ℝ)+δ)+min (v*b) ((k:ℝ)+1-δ))/2
    have hxlo : (k:ℝ)+δ < x := by
      dsimp [x]
      have hh : (k:ℝ)+δ < min (v*b) ((k:ℝ)+1-δ) := lt_min hb (by linarith)
      linarith
    have hxhi : x < min (v*b) ((k:ℝ)+1-δ) := by
      dsimp [x]
      have hh : (k:ℝ)+δ < min (v*b) ((k:ℝ)+1-δ) := lt_min hb (by linarith)
      linarith
    have hxa : v*a < x := by nlinarith [mul_pos hv (show 0 < b-a by linarith)]
    have hxb : x < v*b := lt_of_lt_of_le hxhi (min_le_left _ _)
    obtain ⟨j, hj⟩ := hc (x/v) ((lt_div_iff₀ hv).mpr (by nlinarith))
      ((div_lt_iff₀ hv).mpr (by nlinarith))
    have hg := fractional_integer_gap k j (x-(k:ℝ)) δ (by linarith)
      (by have := lt_of_lt_of_le hxhi (min_le_right (v*b) ((k:ℝ)+1-δ)); linarith)
    have hxe : v*(x/v) = x := by field_simp
    rw [hxe] at hj
    have hge : δ < |x-(j:ℝ)| := by convert hg using 1 <;> congr 1 <;> ring
    linarith

theorem covered_open_interval_width (v δ a b : ℝ)
    (hv : 0 < v) (hδ : δ < 1/2) (hab : a < b)
    (hc : ∀ t : ℝ, a < t → t < b → Bad v δ t) :
    b-a ≤ 2*δ/v := by
  obtain ⟨k, ha, hb⟩ := covered_open_interval_one_band v δ a b hv hδ hab hc
  apply (le_div_iff₀ hv).mpr
  nlinarith

theorem integer_numerator_spacing (D A B : ℤ) (hD : 0 < D)
    (hab : (A:ℝ)/(D:ℝ) < (B:ℝ)/(D:ℝ)) :
    1/(D:ℝ) ≤ (B:ℝ)/(D:ℝ)-(A:ℝ)/(D:ℝ) := by
  have hDR : (0:ℝ) < D := by exact_mod_cast hD
  have hAB : A < B := by
    have : (A:ℝ) < B := (div_lt_div_iff_of_pos_right hDR).mp hab
    exact_mod_cast this
  have hgap : (1:ℝ) ≤ (B:ℝ)-(A:ℝ) := by exact_mod_cast (show 1 ≤ B-A by omega)
  rw [← sub_div]
  exact div_le_div_of_nonneg_right hgap (le_of_lt hDR)

theorem common_scale_endpoint_spacing (n u v A B : ℤ)
    (hn : 0 < n) (hu : 0 < u) (hv : 0 < v)
    (hab : (A:ℝ)/((n:ℝ)*(u:ℝ)) < (B:ℝ)/((n:ℝ)*(v:ℝ))) :
    1/((n:ℝ)*(u:ℝ)*(v:ℝ)) ≤
      (B:ℝ)/((n:ℝ)*(v:ℝ))-(A:ℝ)/((n:ℝ)*(u:ℝ)) := by
  have hnR : (0:ℝ) < n := by exact_mod_cast hn
  have huR : (0:ℝ) < u := by exact_mod_cast hu
  have hvR : (0:ℝ) < v := by exact_mod_cast hv
  have heq : (B:ℝ)/((n:ℝ)*(v:ℝ))-(A:ℝ)/((n:ℝ)*(u:ℝ)) =
      ((B*u-A*v:ℤ):ℝ)/((n:ℝ)*(u:ℝ)*(v:ℝ)) := by push_cast; field_simp; ring
  have hnum : 0 < B*u-A*v := by
    have hh : (0:ℝ) < ((B*u-A*v:ℤ):ℝ)/((n:ℝ)*(u:ℝ)*(v:ℝ)) := by rw [← heq]; linarith
    have hh' := (lt_div_iff₀ (show (0:ℝ) < (n:ℝ)*(u:ℝ)*(v:ℝ) by positivity)).mp hh
    have : (0:ℝ) < ((B*u-A*v:ℤ):ℝ) := by simpa using hh'
    exact_mod_cast this
  rw [heq]
  apply div_le_div_of_nonneg_right _ (by positivity)
  exact_mod_cast (show 1 ≤ B*u-A*v by omega)

theorem one_large_source_endpoint_spacing (n M w u v A B : ℤ)
    (hn : 0 < n) (hM : 1 ≤ M) (hw : M ≤ w)
    (hu : 1 ≤ u) (hv : 1 ≤ v)
    (hsourceu : u ≤ M ∨ u = w) (hsourcev : v ≤ M ∨ v = w)
    (hab : (A:ℝ)/((n:ℝ)*(u:ℝ)) < (B:ℝ)/((n:ℝ)*(v:ℝ))) :
    1/((n:ℝ)*(w:ℝ)*(M:ℝ)) ≤
      (B:ℝ)/((n:ℝ)*(v:ℝ))-(A:ℝ)/((n:ℝ)*(u:ℝ)) := by
  have hnR : (0:ℝ) < n := by exact_mod_cast hn
  have hMR : (0:ℝ) < M := by exact_mod_cast (show 0 < M by omega)
  have hwR : (0:ℝ) < w := by exact_mod_cast (show 0 < w by omega)
  have huR : (0:ℝ) < u := by exact_mod_cast (show 0 < u by omega)
  have hvR : (0:ℝ) < v := by exact_mod_cast (show 0 < v by omega)
  by_cases he : u = v
  · subst v
    have hule : u ≤ w*M := by
      have huW : u ≤ w := by rcases hsourceu with h | rfl <;> omega
      nlinarith
    have huleR : (u:ℝ) ≤ (w:ℝ)*(M:ℝ) := by exact_mod_cast hule
    have hsmall : (1:ℝ)/((n:ℝ)*(w:ℝ)*(M:ℝ)) ≤ 1/((n:ℝ)*(u:ℝ)) := by
      apply div_le_div_of_nonneg_left (by norm_num) (by positivity)
      nlinarith
    apply le_trans hsmall
    simpa only [Int.cast_mul] using integer_numerator_spacing (n*u) A B (by positivity)
      (by simpa only [Int.cast_mul] using hab)
  · have hprod : u*v ≤ w*M := by
      rcases hsourceu with huM | rfl <;> rcases hsourcev with hvM | rfl
      · nlinarith [mul_nonneg (show 0 ≤ M-u by omega) (show 0 ≤ v by omega),
          mul_nonneg (show 0 ≤ w-v by omega) (show 0 ≤ M by omega)]
      · nlinarith
      · nlinarith
      · exact False.elim (he rfl)
    have hprodR : (u:ℝ)*(v:ℝ) ≤ (w:ℝ)*(M:ℝ) := by exact_mod_cast hprod
    have hsmall : (1:ℝ)/((n:ℝ)*(w:ℝ)*(M:ℝ)) ≤ 1/((n:ℝ)*(u:ℝ)*(v:ℝ)) := by
      apply div_le_div_of_nonneg_left (by norm_num) (by positivity)
      nlinarith
    exact le_trans hsmall (common_scale_endpoint_spacing n u v A B hn (by omega) (by omega) hab)

noncomputable def leftEndpoint (n v k : ℤ) : ℝ :=
  ((n*k+1:ℤ):ℝ)/((n:ℝ)*(v:ℝ))

noncomputable def rightEndpoint (n v k : ℤ) : ℝ :=
  ((n*(k+1)-1:ℤ):ℝ)/((n:ℝ)*(v:ℝ))

theorem endpoint_formulas (n v k : ℤ) (hn : 0 < n) (hv : 0 < v) :
    leftEndpoint n v k = ((k:ℝ)+1/(n:ℝ))/(v:ℝ) ∧
    rightEndpoint n v k = ((k:ℝ)+1-1/(n:ℝ))/(v:ℝ) := by
  have hnR : (0:ℝ) < n := by exact_mod_cast hn
  have hvR : (0:ℝ) < v := by exact_mod_cast hv
  constructor <;> simp only [leftEndpoint, rightEndpoint] <;> push_cast <;> field_simp <;> ring

theorem source_good_cell (n v : ℤ) (t₀ : ℝ) (hn : 0 < n) (hv : 0 < v)
    (hgood : ∀ z : ℤ, 1/(n:ℝ) < |(v:ℝ)*t₀-(z:ℝ)|) :
    leftEndpoint n v ⌊(v:ℝ)*t₀⌋ < t₀ ∧
      t₀ < rightEndpoint n v ⌊(v:ℝ)*t₀⌋ := by
  have hvR : (0:ℝ) < v := by exact_mod_cast hv
  let k : ℤ := ⌊(v:ℝ)*t₀⌋
  have hlo : (k:ℝ) ≤ (v:ℝ)*t₀ := Int.floor_le _
  have hhi : (v:ℝ)*t₀ < (k:ℝ)+1 := Int.lt_floor_add_one _
  have hg0 := hgood k
  have hg1 := hgood (k+1)
  rw [abs_of_nonneg (by linarith)] at hg0
  have hg1' : 1/(n:ℝ) < (k:ℝ)+1-(v:ℝ)*t₀ := by
    push_cast at hg1
    rw [abs_of_nonpos (by linarith)] at hg1
    linarith
  obtain ⟨heL, heR⟩ := endpoint_formulas n v k hn hv
  change leftEndpoint n v k < t₀ ∧ t₀ < rightEndpoint n v k
  rw [heL, heR]
  constructor
  · apply (div_lt_iff₀ hvR).mpr
    nlinarith
  · apply (lt_div_iff₀ hvR).mpr
    nlinarith

theorem within_source_cell (n v k : ℤ) (t : ℝ) (hn : 0 < n) (hv : 0 < v)
    (hleft : leftEndpoint n v k < t) (hright : t < rightEndpoint n v k) :
    ∀ z : ℤ, 1/(n:ℝ) < |(v:ℝ)*t-(z:ℝ)| := by
  have hvR : (0:ℝ) < v := by exact_mod_cast hv
  obtain ⟨heL, heR⟩ := endpoint_formulas n v k hn hv
  rw [heL] at hleft
  rw [heR] at hright
  have hl := (div_lt_iff₀ hvR).mp hleft
  have hr := (lt_div_iff₀ hvR).mp hright
  intro z
  have h := fractional_integer_gap k z ((v:ℝ)*t-(k:ℝ)) (1/(n:ℝ))
    (by nlinarith) (by nlinarith)
  convert h using 1 <;> congr 1 <;> ring

theorem finite_source_labelled_gap (n M w : ℤ) (V : Finset ℤ) (t₀ : ℝ)
    (hn : 3 ≤ n) (hM : 1 ≤ M) (hw : M ≤ w) (hV : V.Nonempty)
    (hpos : ∀ v ∈ V, 1 ≤ v) (hlabels : ∀ v ∈ V, v ≤ M ∨ v = w)
    (ht0 : 0 ≤ t₀) (ht1 : t₀ ≤ 1)
    (hgood : ∀ v ∈ V, ∀ z : ℤ, 1/(n:ℝ) < |(v:ℝ)*t₀-(z:ℝ)|) :
    ∃ a b : ℝ, 0 ≤ a ∧ b ≤ 1 ∧ a < t₀ ∧ t₀ < b ∧
      1/((n:ℝ)*(w:ℝ)*(M:ℝ)) ≤ b-a ∧
      (∃ u ∈ V, ∃ v ∈ V, ∃ k l : ℤ,
        a = leftEndpoint n u k ∧ b = rightEndpoint n v l) ∧
      ∀ t : ℝ, a < t → t < b →
        ∀ v ∈ V, ∀ z : ℤ, 1/(n:ℝ) < |(v:ℝ)*t-(z:ℝ)| := by
  classical
  let L : ℤ → ℝ := fun v => leftEndpoint n v ⌊(v:ℝ)*t₀⌋
  let R : ℤ → ℝ := fun v => rightEndpoint n v ⌊(v:ℝ)*t₀⌋
  obtain ⟨u, hu, humax⟩ := Finset.exists_max_image V L hV
  obtain ⟨v, hv, hvmin⟩ := Finset.exists_min_image V R hV
  have hnR : (0:ℝ) < n := by exact_mod_cast (show 0 < n by omega)
  have huR : (0:ℝ) < u := by exact_mod_cast (show 0 < u by have := hpos u hu; omega)
  have hvR : (0:ℝ) < v := by exact_mod_cast (show 0 < v by have := hpos v hv; omega)
  have hLu : L u < t₀ := (source_good_cell n u t₀ (by omega)
    (by have := hpos u hu; omega) (hgood u hu)).1
  have hRv : t₀ < R v := (source_good_cell n v t₀ (by omega)
    (by have := hpos v hv; omega) (hgood v hv)).2
  have htstrict : t₀ < 1 := by
    by_contra h
    have he : t₀ = 1 := by linarith
    have hg := hgood u hu u
    rw [he] at hg
    simp at hg
    linarith [one_div_pos.mpr hnR]
  have hLu0 : 0 ≤ L u := by
    have hk : 0 ≤ ⌊(u:ℝ)*t₀⌋ := Int.floor_nonneg.mpr (mul_nonneg (le_of_lt huR) ht0)
    dsimp [L, leftEndpoint]
    apply div_nonneg _ (by positivity)
    exact_mod_cast (show 0 ≤ n*⌊(u:ℝ)*t₀⌋+1 by nlinarith)
  have hRv1 : R v ≤ 1 := by
    have hk : ⌊(v:ℝ)*t₀⌋ < v := Int.floor_lt.mpr (by nlinarith)
    have hkR : (⌊(v:ℝ)*t₀⌋:ℝ)+1 ≤ (v:ℝ) := by exact_mod_cast (show ⌊(v:ℝ)*t₀⌋+1 ≤ v by omega)
    dsimp [R]
    rw [(endpoint_formulas n v _ (by omega) (by have := hpos v hv; omega)).2]
    apply (div_le_one hvR).mpr
    linarith [one_div_pos.mpr hnR]
  have hspacing : 1/((n:ℝ)*(w:ℝ)*(M:ℝ)) ≤ R v-L u := by
    apply one_large_source_endpoint_spacing n M w u v
      (n*⌊(u:ℝ)*t₀⌋+1) (n*(⌊(v:ℝ)*t₀⌋+1)-1)
      (by omega) hM hw (hpos u hu) (hpos v hv) (hlabels u hu) (hlabels v hv)
    exact lt_trans hLu hRv
  refine ⟨L u, R v, hLu0, hRv1, hLu, hRv, hspacing,
    ⟨u, hu, v, hv, _, _, rfl, rfl⟩, ?_⟩
  intro t hat htb z hz k
  apply within_source_cell n z ⌊(z:ℝ)*t₀⌋ t (by omega) (by have := hpos z hz; omega)
  · exact lt_of_le_of_lt (humax z hz) hat
  · exact lt_of_lt_of_le htb (hvmin z hz)

def retainedSource (n r s : ℤ) : Finset ℤ :=
  (Finset.Icc 1 (n-1)).filter (fun i => i ≠ r ∧ i ≠ s)

theorem inserted_speed_bound_from_hole (n M w₁ w₂ : ℤ) (V : Finset ℤ)
    (hn : 3 ≤ n) (hM : 1 ≤ M) (hw₁ : M ≤ w₁) (hw₂ : 0 < w₂)
    (hV : V.Nonempty) (hpos : ∀ v ∈ V, 1 ≤ v)
    (hlabels : ∀ v ∈ V, v ≤ M ∨ v = w₁)
    (hhole : ∃ t₀ : ℝ, 0 ≤ t₀ ∧ t₀ ≤ 1 ∧
      ∀ v ∈ V, ∀ z : ℤ, 1/(n:ℝ) < |(v:ℝ)*t₀-(z:ℝ)|)
    (hcover : Covers (insert w₂ V) (1/(n:ℝ))) :
    w₂ ≤ 2*w₁*M := by
  obtain ⟨t₀, ht0, ht1, hgood⟩ := hhole
  obtain ⟨a, b, ha0, hb1, hat, htb, hlength, hsource, hgap⟩ :=
    finite_source_labelled_gap n M w₁ V t₀ hn hM hw₁ hV hpos hlabels ht0 ht1 hgood
  have hw₂R : (0:ℝ) < w₂ := by exact_mod_cast hw₂
  have hnR : (3:ℝ) ≤ n := by exact_mod_cast hn
  have hnpos : (0:ℝ) < n := by linarith
  have hMpos : (0:ℝ) < M := by exact_mod_cast (show 0 < M by omega)
  have hw₁pos : (0:ℝ) < w₁ := by exact_mod_cast (show 0 < w₁ by omega)
  have hband : ∀ t : ℝ, a < t → t < b → Bad (w₂:ℝ) (1/(n:ℝ)) t := by
    intro t hat' htb'
    obtain ⟨v, hv, k, hk⟩ := hcover t (by linarith) (by linarith)
    rcases Finset.mem_insert.mp hv with rfl | hv
    · exact ⟨k, hk⟩
    · have hg := hgap t hat' htb' v hv k
      exact False.elim (not_lt_of_ge hk hg)
  have hδ : (1:ℝ)/(n:ℝ) < 1/2 := by
    apply (div_lt_div_iff₀ hnpos (by norm_num)).mpr
    linarith
  have hwidth := covered_open_interval_width (w₂:ℝ) (1/(n:ℝ)) a b hw₂R hδ
    (lt_trans hat htb) hband
  have hcompare : (1:ℝ)/((n:ℝ)*(w₁:ℝ)*(M:ℝ)) ≤ 2/((n:ℝ)*(w₂:ℝ)) := by
    have hh := le_trans hlength hwidth
    convert hh using 1 <;> field_simp <;> ring
  have hh := (div_le_div_iff₀
    (show (0:ℝ) < (n:ℝ)*(w₁:ℝ)*(M:ℝ) by positivity)
    (show (0:ℝ) < (n:ℝ)*(w₂:ℝ) by positivity)).mp hcompare
  have hresult : (w₂:ℝ) ≤ 2*(w₁:ℝ)*(M:ℝ) := by nlinarith
  exact_mod_cast hresult

/-- Full source-specific G2 in the upper-half regime: no supplied gap or
endpoint certificate occurs among the hypotheses. -/
theorem upper_half_second_speed_bound (n r s w₁ w₂ : ℤ)
    (hn : 5 ≤ n) (hr : 1 ≤ r) (hrs : r < s) (hs : s ≤ n-1)
    (hupper : n-1 < 2*r) (hw₁ : n ≤ w₁) (hw₂ : w₁ < w₂)
    (hcover : Covers (insert w₂ (insert w₁ (retainedSource n r s))) (1/(n:ℝ))) :
    w₂ ≤ 2*(n-1)*w₁ := by
  let V := insert w₁ (retainedSource n r s)
  have hpos : ∀ v ∈ V, 1 ≤ v := by
    intro v hv
    rcases Finset.mem_insert.mp hv with rfl | hv
    · omega
    · simp only [retainedSource, Finset.mem_filter, Finset.mem_Icc] at hv
      exact hv.1.1
  have hlabels : ∀ v ∈ V, v ≤ n-1 ∨ v = w₁ := by
    intro v hv
    rcases Finset.mem_insert.mp hv with rfl | hv
    · exact Or.inr rfl
    · simp only [retainedSource, Finset.mem_filter, Finset.mem_Icc] at hv
      exact Or.inl hv.1.2
  obtain ⟨t, ht0, ht1, hgood⟩ := upper_half_one_insertion_hole n r s w₁ hn hr hrs hs hupper hw₁
  have hhole : ∃ t₀ : ℝ, 0 ≤ t₀ ∧ t₀ ≤ 1 ∧
      ∀ v ∈ V, ∀ z : ℤ, 1/(n:ℝ) < |(v:ℝ)*t₀-(z:ℝ)| := by
    refine ⟨(t:ℝ), by exact_mod_cast ht0, by exact_mod_cast ht1, ?_⟩
    intro v hv z
    apply hgood v _ z
    rcases Finset.mem_insert.mp hv with rfl | hv
    · exact Or.inr rfl
    · simp only [retainedSource, Finset.mem_filter, Finset.mem_Icc] at hv
      exact Or.inl ⟨hv.1.1, by omega, hv.2.1, hv.2.2⟩
  have hresult := inserted_speed_bound_from_hole n (n-1) w₁ w₂ V
    (by omega) (by omega) (by omega) (by omega)
    (Finset.insert_nonempty _ _) hpos hlabels hhole hcover
  nlinarith

theorem bad_neg (v δ t : ℝ) : Bad v δ (-t) ↔ Bad v δ t := by
  constructor <;> rintro ⟨k, hk⟩ <;> refine ⟨-k, ?_⟩
  · have he : v*t-((-k:ℤ):ℝ) = -(v*(-t)-(k:ℝ)) := by push_cast; ring
    rw [he, abs_neg]
    exact hk
  · have he : v*(-t)-((-k:ℤ):ℝ) = -(v*t-(k:ℝ)) := by push_cast; ring
    rw [he, abs_neg]
    exact hk

theorem two_band_right_extent (v₁ v₂ δ a b c : ℝ) (k : ℤ)
    (hv₁ : 0 < v₁) (hv₂ : 0 < v₂) (hδ0 : 0 ≤ δ) (hδ : δ < 1/2)
    (hgap : 2*δ/v₂ < (1-2*δ)/v₁)
    (hac : a < c) (hcb : c < b) (hk : |v₁*c-(k:ℝ)| ≤ δ)
    (hcover : ∀ t : ℝ, a < t → t < b → Bad v₁ δ t ∨ Bad v₂ δ t) :
    b ≤ ((k:ℝ)+δ)/v₁+2*δ/v₂ := by
  let p := ((k:ℝ)+δ)/v₁
  let q := ((k:ℝ)+1-δ)/v₁
  have hp : a < p := by
    have hh := (abs_le.mp hk).2
    dsimp [p]
    apply (lt_div_iff₀ hv₁).mpr
    nlinarith [mul_pos hv₁ (sub_pos.mpr hac)]
  have hpq : 2*δ/v₂ < q-p := by
    have he : q-p = (1-2*δ)/v₁ := by dsimp [p, q]; field_simp; ring
    rwa [he]
  by_contra h
  have hb : p+2*δ/v₂ < b := lt_of_not_ge h
  let d := min b q
  have hpd : p+2*δ/v₂ < d := lt_min hb (by linarith)
  have hwidth0 : 0 ≤ 2*δ/v₂ := by positivity
  have hpd' : p < d := by linarith
  have hsecond : ∀ t : ℝ, p < t → t < d → Bad v₂ δ t := by
    intro t hpt htd
    have htb : t < b := lt_of_lt_of_le htd (min_le_left _ _)
    have htq : t < q := lt_of_lt_of_le htd (min_le_right _ _)
    have hl : (k:ℝ)+δ < t*v₁ := (div_lt_iff₀ hv₁).mp hpt
    have hr : t*v₁ < (k:ℝ)+1-δ := (lt_div_iff₀ hv₁).mp htq
    rcases hcover t (lt_trans hp hpt) htb with ⟨j,hj⟩ | hj
    · have hg := fractional_integer_gap k j (v₁*t-(k:ℝ)) δ (by nlinarith) (by nlinarith)
      have he : (k:ℝ)+(v₁*t-(k:ℝ))-(j:ℝ) = v₁*t-(j:ℝ) := by ring
      rw [he] at hg
      exact False.elim (not_lt_of_ge hj hg)
    · exact hj
  have hh := covered_open_interval_width v₂ δ p d hv₂ hδ hpd' hsecond
  linarith

theorem two_band_interval_width (v₁ v₂ δ a b : ℝ)
    (hv₁ : 0 < v₁) (hv₂ : 0 < v₂) (hδ0 : 0 ≤ δ) (hδ : δ < 1/2)
    (hgap : 2*δ/v₂ < (1-2*δ)/v₁) (hab : a < b)
    (hcover : ∀ t : ℝ, a < t → t < b → Bad v₁ δ t ∨ Bad v₂ δ t) :
    b-a ≤ 2*δ/v₁+4*δ/v₂ := by
  by_cases hfirst : ∃ c : ℝ, a < c ∧ c < b ∧ Bad v₁ δ c
  · obtain ⟨c, hac, hcb, k, hk⟩ := hfirst
    have hr := two_band_right_extent v₁ v₂ δ a b c k hv₁ hv₂ hδ0 hδ hgap hac hcb hk hcover
    have hcover' : ∀ t : ℝ, -b < t → t < -a → Bad v₁ δ t ∨ Bad v₂ δ t := by
      intro t hbt hta
      rcases hcover (-t) (by linarith) (by linarith) with h | h
      · exact Or.inl ((bad_neg v₁ δ t).mp h)
      · exact Or.inr ((bad_neg v₂ δ t).mp h)
    have hk' : |v₁*(-c)-((-k:ℤ):ℝ)| ≤ δ := by
      have he : v₁*(-c)-((-k:ℤ):ℝ) = -(v₁*c-(k:ℝ)) := by push_cast; ring
      rwa [he, abs_neg]
    have hl := two_band_right_extent v₁ v₂ δ (-b) (-a) (-c) (-k)
      hv₁ hv₂ hδ0 hδ hgap (by linarith) (by linarith) hk' hcover'
    have he : ((k:ℝ)+δ)/v₁+(((-k:ℤ):ℝ)+δ)/v₁ = 2*δ/v₁ := by push_cast; field_simp; ring
    rw [show 4*δ/v₂ = 2*(2*δ/v₂) by ring]
    nlinarith [he]
  · have hsecond : ∀ t : ℝ, a < t → t < b → Bad v₂ δ t := by
      intro t hat htb
      rcases hcover t hat htb with h | h
      · exact False.elim (hfirst ⟨t,hat,htb,h⟩)
      · exact h
    have hh := covered_open_interval_width v₂ δ a b hv₂ hδ hab hsecond
    have h0 : 0 ≤ 2*δ/v₁ := by positivity
    have h1 : 0 ≤ 2*δ/v₂ := by positivity
    rw [show 4*δ/v₂ = 2*(2*δ/v₂) by ring]
    linarith

theorem two_inserted_interval_strict_width (n w₁ w₂ : ℤ) (a b : ℝ)
    (hn : 5 ≤ n) (hw₁ : 0 < w₁) (hw₂ : w₁ < w₂) (hab : a < b)
    (hcover : ∀ t : ℝ, a < t → t < b →
      Bad (w₁:ℝ) (1/(n:ℝ)) t ∨ Bad (w₂:ℝ) (1/(n:ℝ)) t) :
    b-a < 6/((n:ℝ)*(w₁:ℝ)) := by
  have hnR : (5:ℝ) ≤ n := by exact_mod_cast hn
  have hnpos : (0:ℝ) < n := by linarith
  have hw₁R : (0:ℝ) < w₁ := by exact_mod_cast hw₁
  have hw₂R : (w₁:ℝ) < w₂ := by exact_mod_cast hw₂
  have hw₂pos : (0:ℝ) < w₂ := by linarith
  have hδ : (1:ℝ)/(n:ℝ) < 1/2 := by
    apply (div_lt_div_iff₀ hnpos (by norm_num)).mpr
    linarith
  have hgap : 2*(1/(n:ℝ))/(w₂:ℝ) < (1-2*(1/(n:ℝ)))/(w₁:ℝ) := by
    apply (div_lt_div_iff₀ hw₂pos hw₁R).mpr
    have hninv : (n:ℝ)*(1/(n:ℝ)) = 1 := by field_simp
    have hh : 2*(w₁:ℝ) < ((n:ℝ)-2)*(w₂:ℝ) := by nlinarith
    nlinarith [hninv]
  have hh := two_band_interval_width (w₁:ℝ) (w₂:ℝ) (1/(n:ℝ)) a b
    hw₁R hw₂pos (by positivity) hδ hgap hab hcover
  have hrec : (1:ℝ)/(w₂:ℝ) < 1/(w₁:ℝ) := by
    apply (div_lt_div_iff₀ hw₂pos hw₁R).mpr
    simpa using hw₂R
  have hstrict : 2*(1/(n:ℝ))/(w₁:ℝ)+4*(1/(n:ℝ))/(w₂:ℝ) < 6/((n:ℝ)*(w₁:ℝ)) := by
    rw [show (6:ℝ)/((n:ℝ)*(w₁:ℝ)) =
      2*(1/(n:ℝ))/(w₁:ℝ)+4*(1/(n:ℝ))/(w₁:ℝ) by field_simp; ring]
    apply add_lt_add_left
    have hp := mul_lt_mul_of_pos_left hrec (show (0:ℝ) < 4/(n:ℝ) by positivity)
    convert hp using 1 <;> field_simp <;> ring
  exact lt_of_le_of_lt hh hstrict

theorem upper_half_safe_interval (n r : ℤ) (t : ℝ)
    (hn : 5 ≤ n) (hr : 1 ≤ r) (hrn : r < n) (hupper : n-1 < 2*r)
    (ht : |t-1/(r:ℝ)| < ((n:ℝ)-(r:ℝ))/((n:ℝ)*(r:ℝ)*((n:ℝ)-1))) :
    ∀ i : ℤ, 1 ≤ i → i < n → i ≠ r → ∀ z : ℤ,
      1/(n:ℝ) < |(i:ℝ)*t-(z:ℝ)| := by
  have hnR : (5:ℝ) ≤ n := by exact_mod_cast hn
  have hnpos : (0:ℝ) < n := by linarith
  have hrpos : (0:ℝ) < r := by exact_mod_cast (show 0 < r by omega)
  have hnm : (0:ℝ) < (n:ℝ)-1 := by linarith
  have hmove : ((n:ℝ)-1)*|t-1/(r:ℝ)| < 1/(r:ℝ)-1/(n:ℝ) := by
    have hh := mul_lt_mul_of_pos_left ht hnm
    have he : ((n:ℝ)-1)*(((n:ℝ)-(r:ℝ))/((n:ℝ)*(r:ℝ)*((n:ℝ)-1))) =
      1/(r:ℝ)-1/(n:ℝ) := by field_simp; ring
    rwa [he] at hh
  intro i hi hin hne z
  have hiR : (0:ℝ) ≤ i := by exact_mod_cast (show 0 ≤ i by omega)
  have hinR : (i:ℝ) ≤ (n:ℝ)-1 := by exact_mod_cast (show i ≤ n-1 by omega)
  have hg := integer_gap_to_real 1 r i z 1 (by omega)
    (by simpa using centre_integer_gap r i z hr ⟨hi,by omega⟩ hne)
  have hbase : (1:ℝ)/(r:ℝ) ≤ |(i:ℝ)*(1/(r:ℝ))-(z:ℝ)| := by simpa using hg
  have htri : |(i:ℝ)*(1/(r:ℝ))-(z:ℝ)| ≤ |(i:ℝ)*t-(z:ℝ)|+(i:ℝ)*|t-1/(r:ℝ)| := by
    calc
      _ = |((i:ℝ)*t-(z:ℝ))+(i:ℝ)*(1/(r:ℝ)-t)| := by congr 1; ring
      _ ≤ |(i:ℝ)*t-(z:ℝ)|+|(i:ℝ)*(1/(r:ℝ)-t)| := abs_add _ _
      _ = _ := by rw [abs_mul, abs_of_nonneg hiR, abs_sub_comm (1/(r:ℝ)) t]
  have hmul := mul_le_mul_of_nonneg_right hinR (abs_nonneg (t-1/(r:ℝ)))
  linarith

theorem upper_half_first_speed_geometric_bound (n r s w₁ w₂ : ℤ)
    (hn : 5 ≤ n) (hr : 1 ≤ r) (hrs : r < s) (hs : s ≤ n-1)
    (hupper : n-1 < 2*r) (hw₁ : n ≤ w₁) (hw₂ : w₁ < w₂)
    (hcover : Covers (insert w₂ (insert w₁ (retainedSource n r s))) (1/(n:ℝ))) :
    (w₁:ℝ) < 3*(r:ℝ)*((n:ℝ)-1)/((n:ℝ)-(r:ℝ)) := by
  have hnR : (5:ℝ) ≤ n := by exact_mod_cast hn
  have hnpos : (0:ℝ) < n := by linarith
  have hrR : (2:ℝ) ≤ r := by exact_mod_cast (show 2 ≤ r by omega)
  have hrpos : (0:ℝ) < r := by linarith
  have hrn : (r:ℝ) < n := by exact_mod_cast (show r < n by omega)
  have hnm : (0:ℝ) < (n:ℝ)-1 := by linarith
  have hwpos : (0:ℝ) < w₁ := by exact_mod_cast (show 0 < w₁ by omega)
  let c : ℝ := 1/(r:ℝ)
  let ρ : ℝ := ((n:ℝ)-(r:ℝ))/((n:ℝ)*(r:ℝ)*((n:ℝ)-1))
  have hρ : 0 < ρ := by
    dsimp [ρ]
    exact div_pos (sub_pos.mpr hrn) (mul_pos (mul_pos hnpos hrpos) hnm)
  have hρc : ρ < c := by
    dsimp [ρ, c]
    apply (div_lt_div_iff₀ (by positivity) hrpos).mpr
    have hp := mul_pos hrpos (show (0:ℝ) < (n:ℝ)*((n:ℝ)-1)-((n:ℝ)-(r:ℝ)) by nlinarith)
    nlinarith [hp]
  have hc : c ≤ 1/2 := by
    dsimp [c]
    apply (div_le_div_iff₀ hrpos (by norm_num)).mpr
    linarith
  have hsafe : ∀ t : ℝ, c-ρ < t → t < c+ρ →
      ∀ v ∈ retainedSource n r s, ∀ z : ℤ, 1/(n:ℝ) < |(v:ℝ)*t-(z:ℝ)| := by
    intro t htl htr v hv z
    simp only [retainedSource, Finset.mem_filter, Finset.mem_Icc] at hv
    apply upper_half_safe_interval n r t hn hr (by omega) hupper _ v hv.1.1 (by omega) hv.2.1 z
    apply abs_lt.mpr
    constructor <;> dsimp [c, ρ] at * <;> linarith
  have htwo : ∀ t : ℝ, c-ρ < t → t < c+ρ →
      Bad (w₁:ℝ) (1/(n:ℝ)) t ∨ Bad (w₂:ℝ) (1/(n:ℝ)) t := by
    intro t htl htr
    obtain ⟨v, hv, k, hk⟩ := hcover t (by linarith) (by linarith)
    rcases Finset.mem_insert.mp hv with rfl | hv
    · exact Or.inr ⟨k,hk⟩
    · rcases Finset.mem_insert.mp hv with rfl | hv
      · exact Or.inl ⟨k,hk⟩
      · exact False.elim (not_lt_of_ge hk (hsafe t htl htr v hv k))
  have hlength := two_inserted_interval_strict_width n w₁ w₂ (c-ρ) (c+ρ)
    hn (by omega) hw₂ (by linarith) htwo
  have hfrac : 2*((n:ℝ)-(r:ℝ))/((n:ℝ)*(r:ℝ)*((n:ℝ)-1)) < 6/((n:ℝ)*(w₁:ℝ)) := by
    have hh : 2*ρ < 6/((n:ℝ)*(w₁:ℝ)) := by linarith
    convert hh using 1 <;> dsimp [ρ] <;> ring
  have hp := (div_lt_div_iff₀
    (show (0:ℝ) < (n:ℝ)*(r:ℝ)*((n:ℝ)-1) by positivity)
    (show (0:ℝ) < (n:ℝ)*(w₁:ℝ) by positivity)).mp hfrac
  have hp' : (n:ℝ)*(2*(w₁:ℝ)*((n:ℝ)-(r:ℝ))) < (n:ℝ)*(6*(r:ℝ)*((n:ℝ)-1)) := by nlinarith [hp]
  have hcancel := (mul_lt_mul_left hnpos).mp hp'
  apply (lt_div_iff₀ (show (0:ℝ) < (n:ℝ)-(r:ℝ) by linarith)).mpr
  nlinarith

/-- An unconditional cubic upper-half growth theorem from actual real cover.
The interval argument uses no assumed occupancy estimate or measure premise. -/
theorem upper_half_cubic_growth (n r s w₁ w₂ : ℤ)
    (hn : 5 ≤ n) (hr : 1 ≤ r) (hrs : r < s) (hs : s ≤ n-1)
    (hupper : n-1 < 2*r) (hw₁ : n ≤ w₁) (hw₂ : w₁ < w₂)
    (hcover : Covers (insert w₂ (insert w₁ (retainedSource n r s))) (1/(n:ℝ))) :
    w₂ < 3*n^3 := by
  have hfirst := upper_half_first_speed_geometric_bound n r s w₁ w₂ hn hr hrs hs hupper hw₁ hw₂ hcover
  have hsecond := upper_half_second_speed_bound n r s w₁ w₂ hn hr hrs hs hupper hw₁ hw₂ hcover
  have hnR : (5:ℝ) ≤ n := by exact_mod_cast hn
  have hrR : (1:ℝ) ≤ r := by exact_mod_cast hr
  have hrnR : (r:ℝ) ≤ (n:ℝ)-2 := by exact_mod_cast (show r ≤ n-2 by omega)
  have hcompare : 3*(r:ℝ)*((n:ℝ)-1)/((n:ℝ)-(r:ℝ)) ≤
      (3/2:ℝ)*((n:ℝ)-2)*((n:ℝ)-1) := by
    apply (div_le_iff₀ (show (0:ℝ) < (n:ℝ)-(r:ℝ) by linarith)).mpr
    have hp := mul_nonneg (show (0:ℝ) ≤ (n:ℝ)*((n:ℝ)-1) by
      exact mul_nonneg (by linarith) (by linarith))
      (show (0:ℝ) ≤ (n:ℝ)-2-(r:ℝ) by linarith)
    nlinarith [hp]
  have hfirst2 : 2*(w₁:ℝ) < 3*((n:ℝ)-2)*((n:ℝ)-1) := by
    linarith [lt_of_lt_of_le hfirst hcompare]
  have hsecondR : (w₂:ℝ) ≤ 2*((n:ℝ)-1)*(w₁:ℝ) := by exact_mod_cast hsecond
  have hp := mul_lt_mul_of_pos_left hfirst2 (show (0:ℝ) < (n:ℝ)-1 by linarith)
  have hbound : (w₂:ℝ) < 3*((n:ℝ)-2)*((n:ℝ)-1)^2 := by nlinarith [hp]
  have hpoly : 3*((n:ℝ)-2)*((n:ℝ)-1)^2 < 3*(n:ℝ)^3 := by nlinarith
  exact_mod_cast (lt_trans hbound hpoly)

end ObservationalSUCC.LonelyRunnerGrowth

#print axioms ObservationalSUCC.LonelyRunnerGrowth.covered_open_interval_one_band
#print axioms ObservationalSUCC.LonelyRunnerGrowth.covered_open_interval_width
#print axioms ObservationalSUCC.LonelyRunnerGrowth.finite_source_labelled_gap
#print axioms ObservationalSUCC.LonelyRunnerGrowth.inserted_speed_bound_from_hole
#print axioms ObservationalSUCC.LonelyRunnerGrowth.upper_half_second_speed_bound
#print axioms ObservationalSUCC.LonelyRunnerGrowth.two_inserted_interval_strict_width
#print axioms ObservationalSUCC.LonelyRunnerGrowth.upper_half_first_speed_geometric_bound
#print axioms ObservationalSUCC.LonelyRunnerGrowth.upper_half_cubic_growth
