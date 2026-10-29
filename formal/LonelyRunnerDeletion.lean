import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity

/-!
Source-faithful deleted-speed rational witnesses.

For all integer n >= 5 and 1 <= r <= n-2, construct a rational time in
[0,1] at which EVERY retained speed i in [1,n-1] is at distance at least
2/(2n-3) from EVERY integer; hence strictly farther than 1/(n-1).
The Euclidean denominator construction and forbidden residues are proved,
not assumed as certificate inputs. This is an elementary corollary of known
Lonely Runner deletion results, not a new proof of the general conjecture.

The exact deletion formula and sharp minimizer classification remain paper
proofs in research/2026-10-28/lonely_runner/ALPHA.md. Only the named exports
below are certified by this file. Standard Mathlib axioms are audited below.
-/

namespace ObservationalSUCC.LonelyRunnerDeletion

/-- No nonzero integer multiple of a positive denominator lies between its neighbours. -/
lemma multiple_gap (D q x : ℤ) (hD : 0 < D) (hx : -D < x ∧ x < D)
    (he : q * D = x) : x = 0 := by
  have hq : q = 0 := by
    by_contra h
    have : q ≤ -1 ∨ 1 ≤ q := by omega
    rcases this with h | h <;> nlinarith
  simp_all

/-- An explicit inverse witness excludes residues zero and plus/minus one. -/
theorem inverse_integer_gap (n r k D i z : ℤ)
    (hn : 3 ≤ n) (hr : 1 ≤ r) (hD : n + r ≤ D)
    (hk : k * r + 1 = D) (hi : 1 ≤ i ∧ i < n) (hne : i ≠ r) :
    2 ≤ |i * k - z * D| := by
  have hDp : 0 < D := by omega
  let x := i * k - z * D
  let q := i - z * r
  have he : q * D = r * x + i := by dsimp [q, x]; rw [← hk]; ring
  by_contra h
  have hx : -1 ≤ x ∧ x ≤ 1 := by
    dsimp [x]; have := abs_lt.mp (lt_of_not_ge h); omega
  have cases : x = -1 ∨ x = 0 ∨ x = 1 := by omega
  rcases cases with hx | hx | hx
  · rw [hx] at he
    have hc := multiple_gap D q (i-r) hDp (by omega) (by nlinarith [he])
    omega
  · rw [hx] at he
    have hc := multiple_gap D q i hDp (by omega) (by nlinarith [he])
    omega
  · rw [hx] at he
    have hc := multiple_gap D q (i+r) hDp (by omega) (by nlinarith [he])
    omega

/-- The centre witness has no retained zero residue in the upper half. -/
theorem centre_integer_gap (r i z : ℤ) (hr : 1 ≤ r)
    (hi : 1 ≤ i ∧ i < 2*r) (hne : i ≠ r) : 1 ≤ |i-z*r| := by
  by_contra h
  have hz : i-z*r = 0 := by have := abs_lt.mp (lt_of_not_ge h); omega
  have hz1 : z = 1 := by
    have hlow : 1 ≤ z := by
      by_contra hh
      have : z ≤ 0 := by omega
      nlinarith
    have hupp : z ≤ 1 := by
      by_contra hh
      have : 2 ≤ z := by omega
      nlinarith
    omega
  subst z
  omega

/-- Integer separation gives separation from every real integer translate. -/
theorem integer_gap_to_real (a D i z c : ℤ) (hD : 0 < D)
    (hgap : c ≤ |i*a-z*D|) :
    (c:ℝ)/(D:ℝ) ≤ |(i:ℝ)*((a:ℝ)/(D:ℝ))-(z:ℝ)| := by
  have hDp : (0:ℝ) < D := by exact_mod_cast hD
  have hg : (c:ℝ) ≤ |(i:ℝ)*(a:ℝ)-(z:ℝ)*(D:ℝ)| := by exact_mod_cast hgap
  have he : (i:ℝ)*((a:ℝ)/(D:ℝ))-(z:ℝ) =
      ((i:ℝ)*(a:ℝ)-(z:ℝ)*(D:ℝ))/(D:ℝ) := by field_simp; ring
  rw [he, abs_div, abs_of_pos hDp]
  exact div_le_div_of_nonneg_right hg (le_of_lt hDp)

/-- Explicit Euclidean construction of a short inverse denominator. -/
theorem middle_denominator (n r : ℤ) (hn : 5 ≤ n) (hr : 1 ≤ r)
    (hmid : 2*r ≤ n-1) :
    ∃ k D : ℤ, 1 ≤ k ∧ 0 < D ∧ k ≤ D ∧ k*r+1=D ∧
      n+r ≤ D ∧ D ≤ 2*n-3 := by
  by_cases hb : n = 2*r+1
  · refine ⟨3, 3*r+1, ?_⟩
    omega
  · have hstrong : 2*r+2 ≤ n := by omega
    let q := (n+r-2)/r
    let b := (n+r-2)%r
    have he : r*q+b = n+r-2 := Int.ediv_add_emod (n+r-2) r
    have hb0 : 0 ≤ b := Int.emod_nonneg _ (by omega)
    have hbr : b < r := Int.emod_lt_of_pos _ (by omega)
    have hq : 0 ≤ q := Int.ediv_nonneg (by omega) (by omega)
    refine ⟨q+1, (q+1)*r+1, ?_⟩
    have hm : 0 ≤ q*(r-1) := mul_nonneg hq (by omega)
    constructor
    · omega
    constructor
    · nlinarith
    constructor
    · nlinarith
    constructor
    · rfl
    constructor <;> nlinarith

/-- Full rational-witness metric statement for every retained integer speed.
This quantifies over every integer translate; it is a circle-distance lower
bound, not merely an arithmetic certificate conditional on supplied residues. -/
theorem universal_deleted_speed_witness (n r : ℤ)
    (hn : 5 ≤ n) (hr : 1 ≤ r ∧ r ≤ n-2) :
    ∃ a D : ℤ, 0 < D ∧ 0 ≤ a ∧ a ≤ D ∧
      ∀ i : ℤ, 1 ≤ i → i < n → i ≠ r → ∀ z : ℤ,
      (2:ℝ)/(2*(n:ℝ)-3) ≤ |(i:ℝ)*((a:ℝ)/(D:ℝ))-(z:ℝ)| := by
  have hnR : (5:ℝ) ≤ n := by exact_mod_cast hn
  have hrR : (1:ℝ) ≤ r ∧ (r:ℝ) ≤ (n:ℝ)-2 := by exact_mod_cast hr
  by_cases hmid : 2*r ≤ n-1
  · obtain ⟨k,D,hk,hD,hkD,he,hlo,hup⟩ := middle_denominator n r hn hr.1 hmid
    refine ⟨k,D,hD,by omega,hkD,?_⟩
    intro i hi hin hne z
    have hg := integer_gap_to_real k D i z 2 hD
      (inverse_integer_gap n r k D i z (by omega) hr.1 hlo he ⟨hi,hin⟩ hne)
    have hDR : (0:ℝ) < D := by exact_mod_cast hD
    have hupR : (D:ℝ) ≤ 2*(n:ℝ)-3 := by exact_mod_cast hup
    have hcmp : (2:ℝ)/(2*(n:ℝ)-3) ≤ 2/(D:ℝ) := by
      apply div_le_div_of_nonneg_left (by norm_num) hDR hupR
    exact le_trans hcmp (by simpa using hg)
  · refine ⟨1,r,by omega,by norm_num,hr.1,?_⟩
    intro i hi hin hne z
    have hgap := centre_integer_gap r i z hr.1 ⟨hi,by omega⟩ hne
    have hg := integer_gap_to_real 1 r i z 1 (by omega) (by simpa using hgap)
    have hnpos : (0:ℝ) < 2*(n:ℝ)-3 := by linarith
    have hrpos : (0:ℝ) < r := by linarith
    have hcmp : (2:ℝ)/(2*(n:ℝ)-3) ≤ 1/(r:ℝ) := by
      apply (div_le_div_iff₀ hnpos hrpos).mpr
      nlinarith [hrR.2]
    exact le_trans hcmp (by simpa using hg)

/-- The actual real-time metric lower bound, including the closed unit interval. -/
theorem deleted_speed_metric_bound (n r : ℤ)
    (hn : 5 ≤ n) (hr : 1 ≤ r ∧ r ≤ n-2) :
    ∃ t : ℝ, 0 ≤ t ∧ t ≤ 1 ∧ ∀ i : ℤ, 1 ≤ i → i < n → i ≠ r →
      ∀ z : ℤ, (2:ℝ)/(2*(n:ℝ)-3) ≤ |(i:ℝ)*t-(z:ℝ)| := by
  obtain ⟨a,D,hD,ha,haD,h⟩ := universal_deleted_speed_witness n r hn hr
  have hDR : (0:ℝ) < D := by exact_mod_cast hD
  have haR : (0:ℝ) ≤ a := by exact_mod_cast ha
  have haDR : (a:ℝ) ≤ D := by exact_mod_cast haD
  exact ⟨(a:ℝ)/(D:ℝ), div_nonneg haR (le_of_lt hDR),
    (div_le_one hDR).mpr haDR, h⟩

/-- Strictly more than the predicted cardinality bound at one common real time. -/
theorem deleted_speed_strict_bound (n r : ℤ)
    (hn : 5 ≤ n) (hr : 1 ≤ r ∧ r ≤ n-2) :
    ∃ t : ℝ, 0 ≤ t ∧ t ≤ 1 ∧ ∀ i : ℤ, 1 ≤ i → i < n → i ≠ r →
      ∀ z : ℤ, 1/((n:ℝ)-1) < |(i:ℝ)*t-(z:ℝ)| := by
  obtain ⟨t,ht0,ht1,h⟩ := deleted_speed_metric_bound n r hn hr
  refine ⟨t,ht0,ht1,?_⟩
  intro i hi hin hne z
  have hnR : (5:ℝ) ≤ n := by exact_mod_cast hn
  have hc : 1/((n:ℝ)-1) < 2/(2*(n:ℝ)-3) := by
    apply (div_lt_div_iff₀ (by linarith) (by linarith)).mpr
    linarith
  exact lt_of_lt_of_le hc (h i hi hin hne z)

end ObservationalSUCC.LonelyRunnerDeletion

#print axioms ObservationalSUCC.LonelyRunnerDeletion.inverse_integer_gap
#print axioms ObservationalSUCC.LonelyRunnerDeletion.centre_integer_gap
#print axioms ObservationalSUCC.LonelyRunnerDeletion.integer_gap_to_real
#print axioms ObservationalSUCC.LonelyRunnerDeletion.middle_denominator
#print axioms ObservationalSUCC.LonelyRunnerDeletion.universal_deleted_speed_witness
#print axioms ObservationalSUCC.LonelyRunnerDeletion.deleted_speed_metric_bound
#print axioms ObservationalSUCC.LonelyRunnerDeletion.deleted_speed_strict_bound


