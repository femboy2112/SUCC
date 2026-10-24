import Std.Tactic
/-!
Carry-safe polyphase: the finite arithmetic kernel of the carry-safe observer
round, in Lean 4.14 core + Std. Choice-free, no `sorry`, no custom `axiom`.

Formalized here (and ONLY here):
  * CSA-01 one-based Euclidean reconstruction  q*((n-1)/q) + (n-1)%q + 1 = n
  * CSA-01 controlled-carry successor, no-wrap and wrap cases
  * CSA-04 mixed-radix composition  odx p r (odx q s b) = odx (p*q) (p*s+r) b
  * FSO-01 future-insufficiency witness: the quotient O_p agrees at n=1,2 but
    differs after p-1 successors (at n=p and n=p+1)

This file does NOT formalize the infinite-dimensional Cuntz O_q relations, the
tomography parameter algebra (it involves logarithms, outside this kernel), the
probe-compiler minimax, or any Weil/RH statement. A finite Lean fact about Nat
maps is not a theorem about unbounded Hilbert operators. RH_PROVED: NO.
-/

namespace ObservationalSUCC.CarrySafePolyphase

/-- CSA-01. One-based polyphase reconstruction: n = q*(block) + residue + 1. -/
theorem polyphase_reconstruct (q n : Nat) (_hq : 0 < q) (hn : 0 < n) :
    q * ((n - 1) / q) + (n - 1) % q + 1 = n := by
  have h := Nat.div_add_mod (n - 1) q
  omega

/-- CSA-01. Controlled carry, NO wrap: residue+1 < q advances the residue only. -/
theorem carry_no_wrap (q n : Nat) (_hq : 0 < q) (hn : 0 < n)
    (_hnw : (n - 1) % q + 1 < q) :
    q * ((n - 1) / q) + ((n - 1) % q + 1) + 1 = n + 1 := by
  have h := Nat.div_add_mod (n - 1) q
  omega

/-- CSA-01. Controlled carry, WRAP: residue = q-1 carries the block, residue→0. -/
theorem carry_wrap (q n : Nat) (_hq : 0 < q) (hn : 0 < n)
    (hw : (n - 1) % q + 1 = q) :
    q * ((n - 1) / q + 1) + 0 + 1 = n + 1 := by
  have h := Nat.div_add_mod (n - 1) q
  have e : q * ((n - 1) / q + 1) = q * ((n - 1) / q) + q := Nat.mul_succ q _
  omega

/-- 0-based residue-isometry image coordinate: U_{q,r} shifts block b to q*b+r. -/
def odx (q r b : Nat) : Nat := q * b + r

/-- CSA-04. Mixed-radix composition: U_{p,r} ∘ U_{q,s} = U_{p*q, p*s+r}. -/
theorem mixed_radix_compose (p q r s b : Nat) :
    odx p r (odx q s b) = odx (p * q) (p * s + r) b := by
  unfold odx
  have e1 : p * (q * b + s) = p * (q * b) + p * s := Nat.mul_add p (q * b) s
  have e2 : p * (q * b) = p * q * b := (Nat.mul_assoc p q b).symm
  omega

/-- The quotient observation O_p(n) = ceil(n/p) = (n-1)/p + 1. -/
def Oq (p n : Nat) : Nat := (n - 1) / p + 1

/-- FSO-01. Future-insufficiency witness: O_p cannot tell n=1 from n=2, but after
    p-1 successors (at n=p and n=p+1) the quotient observations differ. -/
theorem fso01_insufficiency (p : Nat) (hp : 2 ≤ p) :
    Oq p 1 = Oq p 2 ∧ Oq p p ≠ Oq p (p + 1) := by
  unfold Oq
  refine ⟨?_, ?_⟩
  · have h1 : (1 - 1) / p = 0 := by simp
    have h2 : (2 - 1) / p = 0 := Nat.div_eq_of_lt (by omega)
    omega
  · have h3 : (p - 1) / p = 0 := Nat.div_eq_of_lt (by omega)
    have h4 : (p + 1 - 1) / p = 1 := by
      have hpp : p + 1 - 1 = p := by omega
      rw [hpp, Nat.div_self (by omega)]
    omega

end ObservationalSUCC.CarrySafePolyphase

-- Axiom audit (must show only the standard kernel axioms, choice-free where noted):
#print axioms ObservationalSUCC.CarrySafePolyphase.polyphase_reconstruct
#print axioms ObservationalSUCC.CarrySafePolyphase.carry_no_wrap
#print axioms ObservationalSUCC.CarrySafePolyphase.carry_wrap
#print axioms ObservationalSUCC.CarrySafePolyphase.mixed_radix_compose
#print axioms ObservationalSUCC.CarrySafePolyphase.fso01_insufficiency
