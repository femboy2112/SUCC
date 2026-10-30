# Complementary review of complete Gauss-unit blindness

Reviewed `../gauss/GAUSS_UNIT_BLINDNESS.md`, especially GG-01, GG-02 and GG-05.
Same-model-family complementary proof review; not blind external authority.

**Verdict:** no blocking mathematical issue found in the reviewed statements.

1. Starting from `J(B,phi)=Σ_y B(1-y²)-Σ_x B(x)`, the substitution y=1-2t
   gives `B(4)J(B,B)` and the latter character sum vanishes. The two Gauss/Jacobi
   product identities then give the inverse B(4) factor exactly. Applying to
   B=chi and chi² yields `G1G5G6/G4³=chi(2)^(-6)=chi(2)²`; no missing sign.
2. For q=p with p1mod8,2 is a square. For q=p², every base-field nonzero element
   is a square because `(q-1)/2` is divisible by p-1. Thus chi(2)^4=1 and the
   entire complete Gauss product is identical for every even t in the age
   direction. Changing additive character has zero mutation exponent because
   `1-12+5+6=0`.
3. The declared p-adic embedding matches chi=bar(omega)^((q-1)/8), and the
   exponent `(p-1)Σ fractions` is the standard integer digit-sum exponent.
   Mutation age sums vanish separately under all four odd residue multipliers,
   so the uniformizer exponent is unchanged. The complete normalized unit
   equality follows from complete Gauss equality. The separate numerical power
   check does not independently choose an m-th root; the dossier correctly says
   its root choice still relies on classical GK normalization.
4. At p17, automorphisms acting independently on ζ8 and fixing ζ17 exist because
   the conductors are coprime. Applying their fixed p-adic valuation gives the
   displayed rank3 matrix. Its primitive integer null direction has first
   coordinate1, so the entire integer kernel is Ze. With g=3, 3^14=2 mod17 and
   chi(2)²=ζ8^(-28)=−1, forcing t even. This proves necessity as well as
   sufficiency of the claimed exact algebraic fiber.
5. The all-time fixed2^k source/orbit equality then forces t divisible by
   2^(k+2): offset4 has uniquely smallest valuation−2 and the radix recurrence
   cannot cancel that minimum. This is compatible with all integer t, not only
   positive mutants. Positivity is correctly added only for t>=0.

Additional scope checks found no issue: semiprimitive p7mod8 evaluation has the
right trace-zero sign; a foreign cofiber conductor prime excludes membership in
Q(ζ8p); the sharp conductor extension uses an explicit log(8n) bound per removed
prime; ordinary finite-field additive characters do not supply prime-square
roots; Galois/Ramanujan averaging is not the selected embedding. Normalized GK
units formed by separately dividing by varpi are correctly kept outside the
raw global-field closure argument. These are source-identification/domain
results, not a selected signed cancellation theorem.

Reviewed dossier SHA256: `381e39415d54adce9265f52f5e6a571175238eee92b909575cc946ba574dd8ad`.
