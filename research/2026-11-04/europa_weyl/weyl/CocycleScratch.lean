-- Finite algebra lemmas checked with the duck_pi v4.14.0 pins.
-- The doubled phase avoids a choice of inverse for 2.
import Mathlib.Tactic.Ring
import Mathlib.Algebra.Group.Prod

namespace EuropaWeyl

def twicePhase {R : Type*} [CommRing R] (v w : R × R) : R :=
  v.2 * w.1 - v.1 * w.2

theorem twicePhase_cocycle {R : Type*} [CommRing R] (v w z : R × R) :
    twicePhase v w + twicePhase (v + w) z =
      twicePhase w z + twicePhase v (w + z) := by
  rcases v with ⟨a, b⟩
  rcases w with ⟨c, d⟩
  rcases z with ⟨f, g⟩
  change (b*c-a*d)+((b+d)*f-(a+c)*g) =
      d*f-c*g+(b*(c+f)-a*(d+g))
  ring

theorem rotation_preserves_twicePhase {R : Type*} [CommRing R] (a b c d : R) :
    twicePhase (-b, a) (-d, c) = twicePhase (a, b) (c, d) := by
  unfold twicePhase
  ring

end EuropaWeyl
