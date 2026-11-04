# Source-native seed research validation — exact finite receipt and scope

Baseline: SUCC main a673ec95dfac4ef6a61c60222be8b615fd08535d. Continuation of draft PR #492, no branch merge.

**Actually executed in a locally staged matching directory:** python -m unittest discover -s tests -p 'test_source_native*.py' -v => **8/8 OK**, zero skips or failures (Python 3.13). The original first run reproduced one ordinary mistaken threshold in a test: it assumed the asymptotic source conductor B_A> A^4 16^(2A) already held at A=40. Actual exact B_A disproved that finite onset. The test and paper bound were corrected to the weaker, sufficient B_A>4A²16^(2A), which holds at the chosen positive development cases. This was repaired before the final 8/8 passing run and is NOT proof of an explicit asymptotic onset.

Checked independently: direct four-term source fractions against collapsed polynomial source for indices 1..179; source conductor prime-support predictions at A=8,16,32,64; B_A divisibility, rational alignment and exact shadow formula on A=8,12,24,32,40,48,64,96; wrong-seed nearpair energy at three chosen q; and exact 16^K uniform virtual seed ensemble collapse for K=1,2,3. All source data exact Fraction.

The deterministic source-native receipt uses SHA256 over a canonical JSON record of complete exact rational B, seed, width, original and counterfeit energies. The decimal columns are for reading only, not rigorous enclosures. After writing, exact replay returned SOURCE_NATIVE_SEED_FRACTION_RECEIPT_VERIFIED. Development epochs A=40,48,64,96 with q=8,8,16,16 were used **after examining early examples** and are not blind holdouts. Each exact numerator/denominator construction is itself the certificate.

**Provenance verification:** Source code/tests and receipt files were also uploaded to GitHub as blobs with their expected byte identities checked against the local tested files before final commit. Full hosted exact-head CI is a separate result; do not claim it before it completes. The analytical estimate log B_A≥(6+o(1))A is proved by the displayed PNT-AP argument, not by these tests. The rational height lower bound imports a published irrationality measure and has no explicit constant c.

No changed archived source files, Lean toolchain, production, or previously accepted proof contracts. No new Lean or independent human referee. Signed Weyl gate, J=o(K) and π-normality OPEN.
