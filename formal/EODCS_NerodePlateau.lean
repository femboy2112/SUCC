/-!
# Global finite-horizon plateau to all-future SUCC agreement

A complete equality of two consecutive observational word partitions
for a *stationary deterministic* source is not merely a numerical plateau:
it implies forward action congruence and all-future agreement. The bound
on WHEN a finite partition plateau must occur is a separate cardinality
argument and is not formalized in this file.

No external source authentication or single physical specimen replay.
-/

namespace ObservationalSUCC

universe u v

def IterSUCC {S : Type u} (U : S → S) : Nat → S → S
  | 0, s => s
  | n+1, s => IterSUCC U n (U s)

def AgreeThrough {S : Type u} {O : Type v}
    (q : S → O) (U : S → S)
    (h : Nat) (s t : S) : Prop :=
  ∀ i : Nat, i ≤ h → q (IterSUCC U i s) = q (IterSUCC U i t)

/-- Order of forward composition is coherent for one stationary U. -/
theorem iter_succ_commutes {S : Type u}
    (U : S → S) (n : Nat) (s : S) :
    IterSUCC U n (U s) = U (IterSUCC U n s) := by
  induction n generalizing s with
  | zero => rfl
  | succ n ih =>
      change IterSUCC U n (U (U s)) = U (IterSUCC U n (U s))
      exact ih (U s)

/-- If every h-indistinguishable pair is also indistinguishable at
h+1, the h-equivalence is stable under the source update U. -/
theorem plateau_implies_action_congruence
    {S : Type u} {O : Type v}
    (q : S → O) (U : S → S) (h : Nat)
    (plateau : ∀ s t : S,
      AgreeThrough q U h s t → AgreeThrough q U (h+1) s t)
    (s t : S) (hagree : AgreeThrough q U h s t) :
    AgreeThrough q U h (U s) (U t) := by
  intro i hi
  exact plateau s t hagree (i+1) (Nat.succ_le_succ hi)

/-- The legitimate all-future conclusion: from one globally verified
complete partition plateau and the source pair's h-equivalence,
every later q-report agrees. This does not assert that one observer
physically executed infinitely many successive experiments. -/
theorem plateau_certifies_all_future
    {S : Type u} {O : Type v}
    (q : S → O) (U : S → S) (h : Nat)
    (plateau : ∀ s t : S,
      AgreeThrough q U h s t → AgreeThrough q U (h+1) s t)
    (s t : S) (hagree : AgreeThrough q U h s t) :
    ∀ n : Nat, q (IterSUCC U n s) = q (IterSUCC U n t) := by
  have hclosed : ∀ a b : S,
      AgreeThrough q U h a b →
      AgreeThrough q U h (U a) (U b) := by
    intro a b hab
    exact plateau_implies_action_congruence q U h plateau a b hab
  have future_blocks : ∀ n : Nat,
      AgreeThrough q U h (IterSUCC U n s) (IterSUCC U n t) := by
    intro n
    induction n with
    | zero =>
        exact hagree
    | succ n ih =>
        have moved := hclosed (IterSUCC U n s) (IterSUCC U n t) ih
        change AgreeThrough q U h
          (IterSUCC U n (U s)) (IterSUCC U n (U t))
        rw [iter_succ_commutes U n s, iter_succ_commutes U n t]
        exact moved
  intro n
  exact (future_blocks n) 0 (Nat.zero_le h)

end ObservationalSUCC
