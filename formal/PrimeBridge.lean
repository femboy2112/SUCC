import Std.Tactic

/-!
# Prime Bridge: exact finite code and reconstruction certificates

Pinned compiler: Lean 4.14.0. No mathlib and no analytical imports.
The qutrit code is W|k> = 3^(-1/2) sum_r |r,r+k,r+2k>, all labels mod 3.
We certify its support counts, exact two-share permutation decoders and the
abstract commutation obstruction to disjoint reconstruction. The Hilbert-space
linear-extension and infinite-dimensional TFD arguments remain paper proofs.
-/

namespace ObservationalSUCC.PrimeBridge

set_option maxRecDepth 10000
set_option maxHeartbeats 4000000

abbrev Trit := Fin 3

def trit (n : Nat) : Trit := ⟨n % 3, Nat.mod_lt _ (by decide)⟩
def fadd (a b : Trit) : Trit := trit (a.val + b.val)
def fsub (a b : Trit) : Trit := trit (a.val + 3 - b.val)
def fmul (a b : Trit) : Trit := trit (a.val * b.val)

def share (k r i : Trit) : Trit := fadd r (fmul i k)

/-- A region labels the erased share; the retained pair has ascending indices. -/
def pair (e k r : Trit) : Trit × Trit :=
  if e = 0 then (share k r 1, share k r 2)
  else if e = 1 then (share k r 0, share k r 2)
  else (share k r 0, share k r 1)

/-- Decode the retained pair into (logical label, erased-share label).
For e=1, the separation is 2, whose inverse in F3 is also 2. -/
def decode (e : Trit) (xy : Trit × Trit) : Trit × Trit :=
  let x := xy.1
  let y := xy.2
  if e = 0 then (fsub y x, fsub (fmul 2 x) y)
  else if e = 1 then (fmul 2 (fsub y x), fsub (fmul 2 y) x)
  else (fsub y x, fsub (fmul 2 y) x)

def encodePair (e : Trit) (kt : Trit × Trit) : Trit × Trit :=
  pair e kt.1 (fsub kt.2 (fmul e kt.1))

/-- The actual decoder, checked in all 27 (erasure, logical, randomizer) cases. -/
theorem decode_codeword : ∀ e k r : Trit,
    decode e (pair e k r) = (k, share k r e) := by
  decide

/-- Each decoder is a permutation of nine computational basis labels. -/
theorem decode_encodePair : ∀ (e : Trit) (k t : Trit),
    decode e (encodePair e (k,t)) = (k,t) := by
  decide

theorem encodePair_decode : ∀ (e : Trit) (x y : Trit),
    encodePair e (decode e (x,y)) = (x,y) := by
  decide

def sum3 (f : Trit → Nat) : Nat := f 0 + f 1 + f 2

/-- Inner products of UNNORMALIZED codeword columns are natural-number counts. -/
def gramCount (k l : Trit) : Nat :=
  sum3 fun r => sum3 fun t =>
    if share k r 0 = share l t 0 ∧
       share k r 1 = share l t 1 ∧
       share k r 2 = share l t 2 then 1 else 0

theorem codeword_gram_count : ∀ k l : Trit,
    gramCount k l = if k = l then 3 else 0 := by
  decide

/-- Partial trace of |Wk><Wl| onto share e, before the common 1/3 factor. -/
def singletonTraceCount (e k l x y : Trit) : Nat :=
  sum3 fun r => sum3 fun t =>
    if share k r e = x ∧ share l t e = y ∧ pair e k r = pair e l t
    then 1 else 0

/-- Therefore the normalized singleton channel sends E_kl to delta_kl I/3.
This count establishes off-diagonal cancellation as well as diagonal secrecy. -/
theorem singleton_partial_trace_count : ∀ e k l x y : Trit,
    singletonTraceCount e k l x y = if k = l ∧ x = y then 1 else 0 := by
  decide

/-- Computational pair and erased coordinate of an arbitrary boundary triple. -/
def pairCoordinates (e x y z : Trit) : Trit × Trit :=
  if e = 0 then (y,z) else if e = 1 then (x,z) else (x,y)

def erasedCoordinate (e x y z : Trit) : Trit :=
  if e = 0 then x else if e = 1 then y else z

/-- Integer coefficient of an unnormalized codeword in the full boundary basis. -/
def codeCoefficient (k x y z : Trit) : Nat :=
  sum3 fun r =>
    if share k r 0 = x ∧ share k r 1 = y ∧ share k r 2 = z then 1 else 0

/-- Matrix entry of D_e^* (E_ab tensor I) D_e, in the retained-pair basis. -/
def reconstructedEntry (e a b : Trit) (outPair inPair : Trit × Trit) : Nat :=
  if (decode e outPair).1 = a ∧ (decode e inPair).1 = b ∧
     (decode e outPair).2 = (decode e inPair).2 then 1 else 0

/-- Coefficient of the reconstructed matrix unit applied to the code column k. -/
def intertwinerCount (e a b k x y z : Trit) : Nat :=
  sum3 fun r =>
    if share k r e = erasedCoordinate e x y z
    then reconstructedEntry e a b (pairCoordinates e x y z) (pair e k r)
    else 0

/-- All coefficients of O_A W = W E_ab; the shared 1/sqrt(3) cancels.
This is a complete finite matrix-unit identity, not a numerical tolerance test. -/
theorem matrix_unit_intertwining_count : ∀ e a b k x y z : Trit,
    intertwinerCount e a b k x y z =
      if k = b then codeCoefficient a x y z else 0 := by
  decide

/-- A singleton cannot recover even the computational logical label from a
single support sample: k=0 and k=1 have a common possible value at each wire. -/
theorem singleton_label_alias : ∀ e : Trit,
    ∃ r t : Trit, share 0 r e = share 1 t e := by
  intro e
  refine ⟨0, fsub 0 e, ?_⟩
  exact (by decide : ∀ i : Trit, share 0 0 i = share 1 (fsub 0 i) i) e

/-- Removing the factor 2 inverse in the separated pair decoder really fails. -/
theorem wrong_middle_decoder_receipt :
    fsub (share 1 0 2) (share 1 0 0) ≠ (1 : Trit) := by
  decide

/-- The arithmetic affine braid is not ordinary commutation, already at n=1,p=2. -/
theorem wrong_semigroup_braid_receipt : (2 : Nat) * (1 + 1) ≠ 2 * 1 + 1 := by
  decide

section AbstractReconstruction
universe u v
variable {L : Type u} {B : Type v}

/-- If two commuting physical actions both intertwine an injective encoding,
the corresponding logical actions commute. Disjoint tensor actions satisfy
the physical commutation premise; no Hilbert-specific fact is smuggled in. -/
theorem commuting_reconstructions_force_logical_commutation
    (W : L → B) (injective : ∀ x y, W x = W y → x = y)
    (P Q : B → B) (A C : L → L)
    (hP : ∀ x, P (W x) = W (A x))
    (hQ : ∀ x, Q (W x) = W (C x))
    (commute : ∀ y, P (Q y) = Q (P y)) :
    ∀ x, A (C x) = C (A x) := by
  intro x
  apply injective
  calc
    W (A (C x)) = P (W (C x)) := (hP (C x)).symm
    _ = P (Q (W x)) := congrArg P (hQ x).symm
    _ = Q (P (W x)) := commute (W x)
    _ = Q (W (A x)) := congrArg Q (hP x)
    _ = W (C (A x)) := hQ (A x)

end AbstractReconstruction

section MirrorWords
universe u
variable {C : Type u}

/-- Ordered generator word; no claim that the supplied generators are primes. -/
def wordProduct : List Nat → Nat
  | [] => 1
  | p :: ps => p * wordProduct ps

def wordTransport (T : Nat → C → C) (a : C) : List Nat → C
  | [] => a
  | p :: ps => T p (wordTransport T a ps)

def lawfulWord (allowed : Nat → Prop) : List Nat → Prop
  | [] => True
  | p :: ps => allowed p ∧ lawfulWord allowed ps

/-- A source satisfying each generator recurrence satisfies its whole word.
The analytic rigidity theorem additionally uses prime factorization, nonzero
mirror coefficients, and square summability; these hypotheses are NOT erased. -/
theorem mirror_recurrence_along_words
    (a : Nat → C) (T : Nat → C → C) (allowed : Nat → Prop)
    (law : ∀ p n, allowed p → a (p * n) = T p (a n)) :
    ∀ ps, lawfulWord allowed ps →
      a (wordProduct ps) = wordTransport T (a 1) ps := by
  intro ps
  induction ps with
  | nil => intro _; rfl
  | cons p ps ih =>
    intro h
    change a (p * wordProduct ps) = T p (wordTransport T (a 1) ps)
    rw [law p _ h.1, ih h.2]

end MirrorWords

#print axioms decode_codeword
#print axioms decode_encodePair
#print axioms encodePair_decode
#print axioms codeword_gram_count
#print axioms singleton_partial_trace_count
#print axioms matrix_unit_intertwining_count
#print axioms singleton_label_alias
#print axioms wrong_middle_decoder_receipt
#print axioms wrong_semigroup_braid_receipt
#print axioms commuting_reconstructions_force_logical_commutation
#print axioms mirror_recurrence_along_words

end ObservationalSUCC.PrimeBridge
