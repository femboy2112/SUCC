/-!
# Portable Prime Sundial: algebraic frame certificates (Lean 4.14; no mathlib)

The original source is (a,b;u,v), with two independent integer units.
These are division-free identities underlying the paper's rational ratio,
wedge conservation, and legal frame transports.

No signed Weil identity, positivity, arithmetic completeness, or source
authentication is inferred. No existing frozen EODCS file is modified.
-/

namespace ObservationalSUCC
namespace PortablePrimeSundial

/-- Along k=l=n, the cross difference u*B_n-v*A_n is conserved.
We state it additively (no subtraction or division required):
u*B_n+v*a = v*A_n+u*b. -/
theorem diagonal_cross_balance (a b u v n : Int) :
    u * (b + n * v) + v * a =
      v * (a + n * u) + u * b := by
  have h : u * (n * v) = v * (n * u) := by ac_rfl
  calc
    u * (b + n * v) + v * a
        = u * b + u * (n * v) + v * a := by rw [Int.mul_add]
    _ = v * a + v * (n * u) + u * b := by rw [h]; ac_rfl
    _ = v * (a + n * u) + u * b := by rw [Int.mul_add]

/-- Relabeling numerator time k by shifting the origin h preserves
the actual source coordinate, with k in the new chart and k+h
in the original chart. The denominator law is identical. -/
theorem origin_shift (a u h k : Int) :
    (a + h * u) + k * u = a + (h + k) * u := by
  calc
    (a + h * u) + k * u = a + (h * u + k * u) := by ac_rfl
    _ = a + (h + k) * u := by rw [Int.add_mul]

/-- Scaling the WHOLE source frame by m preserves ratio observables,
expressed as exact cross multiplication (without dividing by zero). -/
theorem homogeneous_cross_ratio (a b u v m k l : Int) :
    (m * (a + k * u)) * (b + l * v) =
      (a + k * u) * (m * (b + l * v)) := by
  ac_rfl

/-- First projective alias: equal initial rational reports do not force
equal next reports when the two source unit frames are NOT homothetic.
The initial cross-product equality and next inequality are both exact. -/
theorem quotient_does_not_determine_unit_succ :
    (1 : Int) * 4 = 2 * 2 ∧
      (2 : Int) * 5 ≠ 3 * 3 := by
  decide

end PortablePrimeSundial
end ObservationalSUCC
