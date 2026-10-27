# Package replay and exact-arithmetic performance correction

The first package reproduced all 40 tests, but cold-cache certificate replay hit
execution limits (45 seconds, and an attempted larger requested limit). The
original source-tree replay had passed; the failed package attempts produced no
mathematical contradiction. A diagnostic run located the cost in repeated Fraction
Taylor powers/additions, not in phase precision or source data.

Replaced those evaluations by homogeneous integer Horner polynomials, with one
rational reduction per polynomial. The Taylor polynomials, remainder bounds and
outward rounding are unchanged. An extra independent test compares both exact
arithmetic forms at 25 signed/rational argument-and-degree pairs. Every numerical
field in the old receipt is identical; only the bound source-file hashes change.
The original test file and parent source are byte unchanged. The new test is
separately hashed by the replay script. Final test count is 41 (24 new,17 inherited).
These are local package checks, not the full native repository suite.
