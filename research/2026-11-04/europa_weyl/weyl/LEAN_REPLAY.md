The standalone cocycle and quarter-rotation proofs were compiled with Lean 4.14.0 (410fab728470) against the repository-pinned mathlib 4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84. Their file SHA-256 is a6e9bace37e65e76e37b3239af2f25e694f54ab394aed5c63245e2219c8d7dce. Under the pinned duck_pi project, with mathlib and dependencies installed, the replay command is

~~~sh
lake env lean /absolute/path/to/weyl/CocycleScratch.lean
~~~

The corresponding compilation with -o in an isolated copy of the pinned Lean project exited 0. The two axiom reports list propext and Quot.sound. These lemmas prove the doubled bilinear phase's associativity identity and its invariance under the specified rotation in a commutative ring. The finite source, analytic inequalities and explicit formula in this PR have paper proofs. The historical formal baseline has no edits.
