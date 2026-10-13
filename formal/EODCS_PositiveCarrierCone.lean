/-!
# The cone theorem's algebra, kernel-checked over a commutative semiring

Lean 4.14.0; no mathlib.  Part I Theorem 4.1 ("normalized invariant cone ⇒
positive carrier") rests on three exact identities, proved here for matrices
over ANY commutative semiring `R` (the structure `CSR` declares exactly the
laws used; it is instantiated at `Nat` and `Int` below, so the hypotheses are
satisfiable; `ℚ` and `ℝ` are instances by the field axioms, not constructed
here because core Lean 4.14 ships no rational-number algebra):

1. `word_intertwine`: if `T l · G = G · B l` for every letter `l`, then
   `T_w · G = G · B_w` for every word `w` (event operators act first letter
   first, i.e. rightmost).
2. `behavior_transport`: if moreover `τ · G = 1ᵀ` (every generator has mass
   one), then for every coefficient vector `λ`,
   `τ · (T_w (G λ)) = 1ᵀ · (B_w λ)` — the carrier reproduces every word value.
3. `column_stochastic`: if `Σ_z τ · (T (a,z) g_i) = 1` for each action `a` and
   generator `g_i` (mass conservation on generators), then
   `Σ_z Σ_j B (a,z) j i = 1` — the coefficient matrices are column-stochastic.

Nonnegativity of `B` and `λ` is a hypothesis of the cone theorem that is not
an algebraic identity (it is the cone-membership choice); it is not restated
here.  Nothing here claims a physical preparation, reset, or sensor.
-/

namespace ObservationalSUCC

namespace PositiveCarrierCone

/-- The commutative-semiring laws used below. -/
class CSR (R : Type) extends Add R, Mul R where
  zero : R
  one : R
  add_assoc : ∀ a b c : R, a + b + c = a + (b + c)
  add_comm : ∀ a b : R, a + b = b + a
  zero_add : ∀ a : R, zero + a = a
  mul_assoc : ∀ a b c : R, a * b * c = a * (b * c)
  mul_comm : ∀ a b : R, a * b = b * a
  one_mul : ∀ a : R, one * a = a
  mul_add : ∀ a b c : R, a * (b + c) = a * b + a * c
  mul_zero : ∀ a : R, a * zero = zero

instance : CSR Nat where
  zero := 0
  one := 1
  add_assoc := Nat.add_assoc
  add_comm := Nat.add_comm
  zero_add := Nat.zero_add
  mul_assoc := Nat.mul_assoc
  mul_comm := Nat.mul_comm
  one_mul := Nat.one_mul
  mul_add := Nat.mul_add
  mul_zero := Nat.mul_zero

instance : CSR Int where
  zero := 0
  one := 1
  add_assoc := Int.add_assoc
  add_comm := Int.add_comm
  zero_add := Int.zero_add
  mul_assoc := Int.mul_assoc
  mul_comm := Int.mul_comm
  one_mul := Int.one_mul
  mul_add := Int.mul_add
  mul_zero := Int.mul_zero

variable {R : Type} [CSR R]

/-! ## Finite sums -/

def sumFin : (n : Nat) → (Fin n → R) → R
  | 0, _ => CSR.zero
  | n + 1, f => f ⟨0, Nat.succ_pos n⟩ + sumFin n (fun i => f ⟨i.val + 1, Nat.succ_lt_succ i.isLt⟩)

theorem add_zero' (a : R) : a + CSR.zero = a := by
  rw [CSR.add_comm]; exact CSR.zero_add a

theorem zero_mul' (a : R) : CSR.zero * a = CSR.zero := by
  rw [CSR.mul_comm]; exact CSR.mul_zero a

theorem add_mul' (a b c : R) : (a + b) * c = a * c + b * c := by
  rw [CSR.mul_comm, CSR.mul_add, CSR.mul_comm c a, CSR.mul_comm c b]

theorem add_left_comm' (a b c : R) : a + (b + c) = b + (a + c) := by
  rw [← CSR.add_assoc, CSR.add_comm a b, CSR.add_assoc]

theorem sum_add : ∀ (n : Nat) (f g : Fin n → R),
    sumFin n (fun i => f i + g i) = sumFin n f + sumFin n g := by
  intro n
  induction n with
  | zero => intro f g; simp [sumFin, CSR.zero_add]
  | succ n ih =>
    intro f g
    simp only [sumFin]
    rw [ih]
    rw [CSR.add_assoc, CSR.add_assoc, add_left_comm' (sumFin n _) (g _)]

theorem mul_sum : ∀ (n : Nat) (c : R) (f : Fin n → R),
    c * sumFin n f = sumFin n (fun i => c * f i) := by
  intro n
  induction n with
  | zero => intro c f; simp [sumFin, CSR.mul_zero]
  | succ n ih =>
    intro c f
    simp only [sumFin]
    rw [CSR.mul_add, ih]

theorem sum_mul : ∀ (n : Nat) (f : Fin n → R) (c : R),
    sumFin n f * c = sumFin n (fun i => f i * c) := by
  intro n f c
  rw [CSR.mul_comm, mul_sum]
  congr 1
  funext i
  exact CSR.mul_comm c (f i)

theorem sum_zero_fun : ∀ (m : Nat), sumFin m (fun _ : Fin m => (CSR.zero : R)) = CSR.zero := by
  intro m
  induction m with
  | zero => rfl
  | succ m ih => simp only [sumFin]; rw [CSR.zero_add]; exact ih

theorem sum_comm : ∀ (n m : Nat) (f : Fin n → Fin m → R),
    sumFin n (fun i => sumFin m (fun j => f i j)) = sumFin m (fun j => sumFin n (fun i => f i j)) := by
  intro n
  induction n with
  | zero =>
    intro m f
    simp only [sumFin]
    exact (sum_zero_fun m).symm
  | succ n ih =>
    intro m f
    simp only [sumFin]
    rw [ih m (fun i j => f ⟨i.val + 1, Nat.succ_lt_succ i.isLt⟩ j)]
    rw [← sum_add]

theorem sum_congr (n : Nat) (f g : Fin n → R) (h : ∀ i, f i = g i) : sumFin n f = sumFin n g := by
  have : f = g := funext h
  rw [this]

/-! ## Matrices and vectors -/

def Mat (R : Type) (n m : Nat) := Fin n → Fin m → R
def Vec (R : Type) (n : Nat) := Fin n → R

def mmul {n m k : Nat} (A : Mat R n m) (B : Mat R m k) : Mat R n k :=
  fun i l => sumFin m (fun j => A i j * B j l)

def mvec {n m : Nat} (A : Mat R n m) (x : Vec R m) : Vec R n :=
  fun i => sumFin m (fun j => A i j * x j)

def vmat {n m : Nat} (τ : Vec R n) (A : Mat R n m) : Vec R m :=
  fun j => sumFin n (fun i => τ i * A i j)

def dot {n : Nat} (τ : Vec R n) (x : Vec R n) : R :=
  sumFin n (fun i => τ i * x i)

def ident (n : Nat) : Mat R n n :=
  fun i j => if i = j then CSR.one else CSR.zero

def ones (m : Nat) : Vec R m := fun _ => CSR.one

def col {n m : Nat} (G : Mat R n m) (i : Fin m) : Vec R n := fun r => G r i

theorem mmul_assoc {n m k l : Nat} (A : Mat R n m) (B : Mat R m k) (C : Mat R k l) :
    mmul (mmul A B) C = mmul A (mmul B C) := by
  funext i q
  simp only [mmul]
  -- Σ_c (Σ_b A i b * B b c) * C c q = Σ_b A i b * (Σ_c B b c * C c q)
  have h1 : sumFin k (fun c => sumFin m (fun b => A i b * B b c) * C c q)
          = sumFin k (fun c => sumFin m (fun b => A i b * B b c * C c q)) := by
    apply sum_congr; intro c; rw [sum_mul]
  have h2 : sumFin m (fun b => A i b * sumFin k (fun c => B b c * C c q))
          = sumFin m (fun b => sumFin k (fun c => A i b * (B b c * C c q))) := by
    apply sum_congr; intro b; rw [mul_sum]
  rw [h1, h2, sum_comm]
  apply sum_congr; intro b; apply sum_congr; intro c
  exact CSR.mul_assoc _ _ _

theorem mmul_mvec {n m k : Nat} (A : Mat R n m) (B : Mat R m k) (x : Vec R k) :
    mvec (mmul A B) x = mvec A (mvec B x) := by
  funext i
  simp only [mmul, mvec]
  have h1 : sumFin k (fun c => sumFin m (fun b => A i b * B b c) * x c)
          = sumFin k (fun c => sumFin m (fun b => A i b * B b c * x c)) := by
    apply sum_congr; intro c; rw [sum_mul]
  have h2 : sumFin m (fun b => A i b * sumFin k (fun c => B b c * x c))
          = sumFin m (fun b => sumFin k (fun c => A i b * (B b c * x c))) := by
    apply sum_congr; intro b; rw [mul_sum]
  rw [h1, h2, sum_comm]
  apply sum_congr; intro b; apply sum_congr; intro c
  exact CSR.mul_assoc _ _ _

theorem dot_mvec {n m : Nat} (τ : Vec R n) (G : Mat R n m) (y : Vec R m) :
    dot τ (mvec G y) = dot (vmat τ G) y := by
  simp only [dot, mvec, vmat]
  have h1 : sumFin n (fun i => τ i * sumFin m (fun j => G i j * y j))
          = sumFin n (fun i => sumFin m (fun j => τ i * (G i j * y j))) := by
    apply sum_congr; intro i; rw [mul_sum]
  have h2 : sumFin m (fun j => sumFin n (fun i => τ i * G i j) * y j)
          = sumFin m (fun j => sumFin n (fun i => τ i * G i j * y j)) := by
    apply sum_congr; intro j; rw [sum_mul]
  rw [h1, h2, sum_comm]
  apply sum_congr; intro i; apply sum_congr; intro j
  exact (CSR.mul_assoc _ _ _).symm

theorem mvec_col {n m k : Nat} (G : Mat R n m) (B : Mat R m k) (i : Fin k) :
    mvec G (col B i) = col (mmul G B) i := by
  funext r
  simp only [mvec, col, mmul]

theorem ident_mmul {n m : Nat} (A : Mat R n m) : mmul (ident n) A = A := by
  funext i j
  simp only [mmul, ident]
  -- Σ_k (if i = k then 1 else 0) * A k j = A i j
  have key : ∀ (p : Nat) (f : Fin p → R) (i : Fin p),
      sumFin p (fun k => (if i = k then CSR.one else CSR.zero) * f k) = f i := by
    intro p
    induction p with
    | zero => intro f i; exact absurd i.isLt (Nat.not_lt_zero _)
    | succ p ih =>
      intro f i
      simp only [sumFin]
      by_cases h0 : i.val = 0
      · have hi : i = ⟨0, Nat.succ_pos p⟩ := Fin.ext h0
        subst hi
        simp only [if_true, CSR.one_mul]
        have : sumFin p (fun k => (if (⟨0, Nat.succ_pos p⟩ : Fin (p + 1)) = ⟨k.val + 1, Nat.succ_lt_succ k.isLt⟩
            then CSR.one else CSR.zero) * f ⟨k.val + 1, Nat.succ_lt_succ k.isLt⟩) = CSR.zero := by
          have hz : ∀ k : Fin p, (if (⟨0, Nat.succ_pos p⟩ : Fin (p + 1)) = ⟨k.val + 1, Nat.succ_lt_succ k.isLt⟩
              then CSR.one else CSR.zero) * f ⟨k.val + 1, Nat.succ_lt_succ k.isLt⟩ = CSR.zero := by
            intro k
            have hne : (⟨0, Nat.succ_pos p⟩ : Fin (p + 1)) ≠ ⟨k.val + 1, Nat.succ_lt_succ k.isLt⟩ := by
              intro h; have := congrArg Fin.val h; simp at this
            rw [if_neg hne]; exact zero_mul' _
          rw [sum_congr p _ (fun _ => CSR.zero) hz]
          exact sum_zero_fun p
        rw [this, add_zero']
      · have hne : i ≠ ⟨0, Nat.succ_pos p⟩ := fun h => h0 (congrArg Fin.val h)
        rw [if_neg hne, zero_mul', CSR.zero_add]
        have hi' : i.val - 1 < p := by have := i.isLt; omega
        have ih' := ih (fun k => f ⟨k.val + 1, Nat.succ_lt_succ k.isLt⟩) ⟨i.val - 1, hi'⟩
        have e : (⟨i.val - 1 + 1, Nat.succ_lt_succ hi'⟩ : Fin (p + 1)) = i := by
          apply Fin.ext; simp; omega
        simp only [] at ih'
        rw [e] at ih'
        rw [← ih']
        apply sum_congr; intro k
        have : (i = ⟨k.val + 1, Nat.succ_lt_succ k.isLt⟩) ↔
               ((⟨i.val - 1, hi'⟩ : Fin p) = k) := by
          constructor
          · intro h; apply Fin.ext; have := congrArg Fin.val h; simp at this; simp; omega
          · intro h; apply Fin.ext; have := congrArg Fin.val h; simp at this; simp; omega
        by_cases hk : (⟨i.val - 1, hi'⟩ : Fin p) = k
        · rw [if_pos (this.mpr hk), if_pos hk]
        · rw [if_neg (fun h => hk (this.mp h)), if_neg hk]
  exact key n (fun k => A k j) i

/-! ## Words and the three identities -/

/-- `wordOp T w` = `T lₙ ⋯ T l₁` for `w = [l₁, …, lₙ]`: the first letter acts first. -/
def wordOp {L : Type} {n : Nat} (T : L → Mat R n n) : List L → Mat R n n
  | [] => ident n
  | l :: w => mmul (wordOp T w) (T l)

/-- **Identity 1 (intertwining along words).** -/
theorem word_intertwine {L : Type} {n m : Nat} (T : L → Mat R n n) (B : L → Mat R m m)
    (G : Mat R n m) (hTG : ∀ l, mmul (T l) G = mmul G (B l)) :
    ∀ w : List L, mmul (wordOp T w) G = mmul G (wordOp B w) := by
  intro w
  induction w with
  | nil =>
    simp only [wordOp]
    rw [ident_mmul]
    -- G = G · I : prove I is a right identity through transposition-free argument
    funext i j
    simp only [mmul, ident]
    have key : ∀ (p : Nat) (f : Fin p → R) (j : Fin p),
        sumFin p (fun k => f k * (if k = j then CSR.one else CSR.zero)) = f j := by
      intro p f j
      have := congrFun (congrFun (ident_mmul (R := R) (fun k (_ : Fin 1) => f k)) j) ⟨0, Nat.one_pos⟩
      simp only [mmul, ident] at this
      rw [← this]
      apply sum_congr; intro k
      rw [CSR.mul_comm]
      by_cases h : k = j
      · subst h; simp
      · rw [if_neg h, if_neg (fun e => h e.symm)]
    exact (key m (fun k => G i k) j).symm
  | cons l w ih =>
    simp only [wordOp]
    rw [mmul_assoc, hTG, ← mmul_assoc, ih, mmul_assoc]

/-- **Identity 2 (behavior transport).**  With `τ · G = 1ᵀ`, every word value of
the linear system on `G λ` equals the carrier's word value on `λ`. -/
theorem behavior_transport {L : Type} {n m : Nat} (T : L → Mat R n n) (B : L → Mat R m m)
    (G : Mat R n m) (τ : Vec R n) (hTG : ∀ l, mmul (T l) G = mmul G (B l))
    (hN : vmat τ G = ones m) (lam : Vec R m) (w : List L) :
    dot τ (mvec (wordOp T w) (mvec G lam)) = dot (ones m) (mvec (wordOp B w) lam) := by
  rw [← mmul_mvec, word_intertwine T B G hTG w, mmul_mvec, dot_mvec, hN]

/-- **Identity 3 (column-stochastic normalization).**  Mass conservation on the
generators, `Σ_z τ · (T (a,z) g_i) = 1`, becomes `Σ_z Σ_j B (a,z) j i = 1`. -/
theorem column_stochastic {A : Type} {n m : Nat} (k : Nat)
    (T : A → Fin k → Mat R n n) (B : A → Fin k → Mat R m m)
    (G : Mat R n m) (τ : Vec R n) (hTG : ∀ a z, mmul (T a z) G = mmul G (B a z))
    (hN : vmat τ G = ones m)
    (hM : ∀ a i, sumFin k (fun z => dot τ (mvec (T a z) (col G i))) = CSR.one) :
    ∀ a i, sumFin k (fun z => sumFin m (fun j => B a z j i)) = CSR.one := by
  intro a i
  rw [← hM a i]
  apply sum_congr; intro z
  -- τ · (T g_i) = τ · (G (B e_i)) = 1ᵀ · col_i B = Σ_j B j i
  have h1 : mvec (T a z) (col G i) = col (mmul (T a z) G) i := mvec_col (T a z) G i
  have h2 : col (mmul (T a z) G) i = mvec G (col (B a z) i) := by
    rw [hTG a z]; exact (mvec_col G (B a z) i).symm
  rw [h1, h2, dot_mvec, hN]
  simp only [dot, ones, col]
  apply sum_congr; intro j
  exact (CSR.one_mul _).symm

end PositiveCarrierCone

end ObservationalSUCC
