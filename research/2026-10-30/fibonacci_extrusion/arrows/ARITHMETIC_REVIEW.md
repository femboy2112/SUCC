# Complementary review of the arithmetic front

Reviewed FA01–FA02 and FA04 in
`../arithmetic/FIBONACCI_ARITHMETIC.md`. Exact reviewed dossier SHA256 is in
`receipts/arithmetic-review.json`. This is a second derivation and separate
code path within the same model family, not an external referee.

**Verdict: the scoped paper claims survive.**

1. Solving both row equations gives x=16y and239y=0, so the Smith factors
   are1,239. Higher prime-power fixed-radix rows are imprimitive. The unique
   Hensel lift of the root16 is44231 at precision239²; it changes the native
   clock. The wording was clarified from “second root” to “second-precision
   lift,” since there is only one root in the selected mod239 residue class.
2. Direct recurrence elimination gives239U_n+15r_(n+1)+r_(n+2), with the
   authentic signs retained. Both kernel inequalities imply the stated
   common-denominator bounds. The initial residue198 refutes an unforced
   Fibonacci law even before any239 denominator appears.
3. First denominator multiples occur at60,90,120,210 for offsets2,3,4,7.
   Hence every state through59 is239-integral. At60 the scaled source
   contributes−1/2≡119, with all previous contributions vanishing after
   multiplication by239. There is no cancellation at this first birth.
4. The sparse edit set has O((log N)^3) positions because Fibonacci indices
   grow geometrically. For any fixed block width, only a bounded multiple of
   the edit count can change indicators. This proves normality preservation
   from an assumed normal input, while k² zeros enforce coherent snapshots.
   The same-forcing seed transfer has the correct extra16 and time index.

The separate executable uses SymPy's integer Smith form, brute-force Hensel
digits (not the front's Newton digit), direct exact rational unrolling, and
finite digit-window surgery. It checks seven moduli, five fresh precision
lifts,59 pre-birth states, all first pole times, the exact initial forcing
defect, and six finite surgery controls. These do not replace the universal
paper arguments.

No additional inference is licensed: a modular homogeneous compatibility is
not an Archimedean conjugacy; the complementary conductor phase is retained
as an unresolved coordinate. The normal snapshot control changes the seed
and is correctly excluded from the authentic U_0=0 theorem.
