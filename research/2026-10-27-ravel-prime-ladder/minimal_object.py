"""Derive the EXACT minimal mathematical object whose existence closes pi-normality.

From the session's proved reductions:
  pi base-16 normal  <=>  W_N(h) = (1/N) sum_n e(h 16^n pi) -> 0  for all h != 0
  <=>  every weak-* limit mu of (1/N) sum delta_{16^n pi} is x3-invariant AND ergodic
       with positive entropy (Rudolph-Johnson)  -- entropy is FREE (transcendence)
  <=>  Furstenberg x2x3 at pi.

So the single missing object is: a proof that pi's orbit is x3-invariant as a MEASURE.

The cleanest, weakest form of that object -- what I would "pontificate into existence" --
is a SUBLINEAR bound on the Weyl sum with a SPECIFIC saving, OR an equivalent.

Let me make it fully precise.  There are two equivalent "smallest objects":

OBJECT 1 (analytic): prove  |W_N(h)| = o(1)  for all h != 0.
  Equivalent:  |W_N(h)| <= C_h * N^{-delta} for SOME delta > 0 (any delta), all h.

OBJECT 2 (arithmetic): a genuinely NEW structural fact about pi that no generic
  irrational has, strong enough to force W_N(h)->0.  Candidates:
    (a) pi has a BBP-type formula with a "sublinear tail" -- but BBP gives sparse digits only.
    (b) pi's continued fraction / irrationality measure implies a digit-mixing bound --
        NO such implication is known (Liouville numbers have huge irrationality measure
        but are non-normal; irrationality measure does NOT control normality).
    (c) a NEW "pi-specific" arithmetic regularity.

The profound realization: the object to conjure is a theorem of the form
  "pi satisfies property P, and P => base-16 normality, and P is NOT equivalent to
   normality (it is provably weaker and provably true for pi)."

So the question reduces to: what is the WEAKEST property P with (i) P provable for pi,
(ii) P => normality, (iii) P not obviously equivalent to normality?

I can name the exact candidate class and the exact weakest known such P.  Let me
enumerate them precisely and rank by "provability gap" (how much easier is P than normality).
"""
print("""
THE MINIMAL OBJECT TO CONJURE -- exact candidate properties P with P(pi) provable and P => normal
================================================================================================

For each candidate P, I state: (i) exact statement, (ii) why P => base-16 normality,
(iii) the provability gap (is P genuinely weaker than normality?).

------------------------------------------------------------------
P1. Bailey--Crandall "Hypothesis A" (the named one).
   P1(pi): the x16-orbit of pi is not confined to a closed invariant set of zero entropy
           (equivalently: pi's digits have positive entropy rate).
   => normality: combined with x2x3 measure rigidity (Rudolph-Johnson), positive entropy
      + joint x2/x3 invariance forces Haar.
   Gap: P1 is genuinely WEAKER than normality (it's "positive entropy", one bit, vs "all
      block frequencies correct").  BUT the x2x3-invariance input is still needed, and THAT
      is the wall.  So P1 alone is NOT sufficient; it needs the rigidity bridge.

------------------------------------------------------------------
P2. The single object that WOULD close it (minimal conjure):
   "pi's base-16 expansion has a sublinear-discrepancy Fourier certificate."

   PRECISE FORM:  there exists delta > 0 and constants C_h such that
      | (1/N) sum_{n<=N} e(h 16^n pi) | <= C_h N^{-delta}   for all h != 0.
   => normality: this IS Weyl's criterion (a sublinear bound, any delta, suffices).
   Gap: ZERO -- this is literally equivalent to normality (it's the Weyl statement).
   So "conjuring P2" = conjuring normality itself.  No shortcut.

------------------------------------------------------------------
P3. A NEW arithmetic property, strictly weaker than normality, provable for pi:
   This is the only genuine "pontification" that would be a real advance, and it must
   be of the form:
      P3(pi): some explicit number-theoretic quantity attached to pi (e.g. a bound on
      a specific exponential sum over the BBP series, or an adelic equidistribution
      statement on the solenoid X_{2,3}) is sublinear.

   The most promising SPECIFIC candidate, given SUCC's machinery:
      P3 = "the canonical solenoid lift of pi is x3-invariant in the real fiber."
   => normality: by Rudolph-Johnson (entropy free, x3-invariance is the input).
   Gap: this is exactly x2x3 at pi -- STILL the wall, but it's the RIGHT object to
      conjure because it's a MEASURE-level statement, not a frequency statement.

------------------------------------------------------------------
THE HONEST ANSWER:  the object to pontificate into existence is

   "pi's orbit is x3-invariant at the MEASURE level, i.e. the sequence of empirical
    measures (1/N) sum delta_{16^n pi} converges weak-* to a measure mu with
    (T_3)_* mu = mu, AND mu is ergodic for x16."

   This is a SINGLE, precisely-stated dynamical-rigidity hypothesis.  It is equivalent
   to Furstenberg x2x3 at pi, it is strictly weaker than "explicitly normal" (it's a
   one-measure statement, not an all-block-frequency statement), and it is the exact
   gate that everything else this session reduced to.

   To "conjure" it is to PROVE it.  There is no weaker object that closes the proof:
   - frequency-level objects are O(1/N) and blind (proved: Infinite-Dimensionality).
   - adic-level objects are logarithmic and don't obstruct (proved: 3-adic Memory).
   - entropy is free (transcendence).
   So the measure-level x3-invariance is THE minimal object, and it is open.

Let me also verify: is there a known theorem that P3 follows from any CLASSICAL property
of pi (irrationality measure, transcendence, BBP)?  I'll state the known negative results
that show NO classical property currently implies P3.
""")

print("""
KNOWN: no classical property of pi implies measure-level x3-invariance.
- Transcendence: does NOT imply normality (many transcendental non-normal numbers).
- Irrationality measure mu(pi): bounded (finite), but irrationality measure does NOT
  control digit frequencies (Liouville numbers: infinite measure, non-normal; badly
  approximable: measure 2, can still be non-normal).
- BBP formula: gives sparse digit extraction (16^k positions), not block frequencies;
  does NOT imply normality (Bailey-Crandall is a CONJECTURE, not theorem).

CONCLUSION: the object is exactly "prove (T_3)_* mu = mu for the limit mu of pi's orbit,
with mu x16-ergodic."  There is no known weaker sufficient object.  This is the honest
answer to "what do I need to pontificate into existence."
""")
