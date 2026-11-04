# Validation / exact-source and authority receipt

**Predeclared** child of SUCC PR #496 head `a0a2619578a88182c73420901c99994699eb2024`, with separate preregistration pushed to GitHub BEFORE the fresh large-N cases at `ba185173edd60e57148c930e0fd95041fd4bf11e`. The first four event constants and general theorem direction were DEVELOPMENT observations before preregistration and are not portrayed as new blinded holdouts.

## Validation executed locally in an isolated research stage

- `python -m unittest discover -s /mnt/data/succ_frobenius_round/tests -p 'test_frobenius_prime_saturation.py' -v`: **18/18 tests PASS**, 0 failures/skips after recording and correcting a deliberately overstrong finite-N test claim. A lower prime may cancel at a finite N, consistent with the theorem's eventual `forall eps exists N_eps` quantifier.
- `python research/2026-11-04/frobenius_prime_saturation/symbolic_oracle.py`: **exact all-k symbolic identities PASS** for all four periodic pulse cycles, the original polynomial source, alternative null integral derivative, rational asymptotics and shifted numerator positivity.
- `python research/2026-11-04/frobenius_prime_saturation/generate_receipt.py --verify`: deterministic exact receipt PASS. One development runtime issue (`sys.int_max_str_digits` for gigantic numerator) was repaired using stable length-prefixed signed big-endian integer byte hashing; another was JSON tuple/list canonicalization. Both are preserved here, not claimed as theorem failures.
- `python -m compileall -q`: no errors.

## Fresh original source holdout scope

- N=128,257,509,911,1511, exact Fraction original state, **independent integer common-LCM source recurrence**, reduced denominator and full cumulative conductor. No π digits input.
- All genuinely eligible prime p>max(N/10,sqrt(8N)), p>5 at N=128/257/509/911 were compared in three ways: normalizer C_a(m), fully independent source p-pole modular recurrence, and actual unwrapped full Fraction `p U_N mod p`. Exact equality at all checked cases.
- All four classes mod8, first four rational pulse normalizers, sign checks through 100 octaves, and FULL shell transport for k≤54. Actual original p residues at independent n_{p,k} across at least four primes per class with k=1,2,3.
- Strict dual null finite-state inequality through N=1529; zero completed π formula rational derivative; Gamma/oily asymptotic proven on paper, not inferred from finite data.
- **Honest finite exceptional p cancellations**: (N,p)=(128,37),(257,47),(509,113),(509,151). The initial overly strong development assertion that every p>N/5 survives already at N=509 was REFUTED and repaired. No full uniform finite-N bound asserted.

## Actual proof authority versus probes

The all-m nonzero pulse theorem PF-04 is a FOUR-CASE rational inequality induction. It is not certified by 100 exact finite cycles. The sharp `6` exponent PF-05 imports the *classical* fixed-modulus PNT-AP; finite prime lists cannot prove it. The second π BBP formula is **known classical mathematics** (MathWorld's BBP-Type Formula, formula 3), while its source-typed p-reduction coupling is new to this SUCC dossier. Academic first priority remains **UNVERIFIED**: targeted public search found no direct matching reduced-denominator result, which is not a comprehensive priority search.

**NOT CLAIMED:** the native full 11k+ SUCC test suite, root provenance/foundations/ordinal probes, new Lean kernel formalization, hosted exact-head workflow results before checking, independent human referee, source-selected Archimedean near-pair saving, selected signed Weyl, π base16 normality, or RH. Local stage does NOT include a native full SUCC checkout (public git clone previously failed DNS); the declared original source was audited against exact GitHub primary files. This is a strictly additive research-only draft.
