# X04 independent adversarial review

Reviewer: second-generation X04 investigator, independent of the B and D cohort
authors. Parent `24c93bf0c2bdd4f3f84e9be6367bec15308270ce` contains their frozen
implementations. This is an independent mathematical/implementation audit of
B16 and D28, not an independent reviewer of X04's own new theorem.

**B16: PASS under the stated stationary deterministic source contract.**
The earliest-repeat proof is sound. The partition oracle independently finds
the minimum compatible identification of observed path states. Functional
successor constraints are imposed before output assignments, and the final
unspecified successor can always point to an existing block. The nonempty
source convention correctly gives one state for an empty word. All 875 tested
word/alphabet cases agree, including repeated strings and marker endpoints.
The theorem does not price input tapes, an external time schedule, observer
working memory, or physical energy. No correction to B16 is required.

**D28: PASS for closed full-tent inverse cylinders.** The exact forward oracle
checks both full endpoint pairs and diameters, not only a fitted exponent.
All 12,286 image checks agree. After the final known branch the image is the
whole interval; no continued-small-error inference survives. Closed cylinders
can share endpoints, so their labels are a cover convention and should not
silently be described as a disjoint partition of boundary states. D28 already
states this boundary explicitly. The new arbitrary-future-bin counterexample
shows the load-bearing full-cylinder restriction is stronger than merely
having a finite report alphabet. No correction to D28 is required.

**D25/D26/D32/F44: scope check, not new exhaustive audit.** Their explicit
factor/coverage, complete-source, source-access, and stationary-map assumptions
were read and retained. X04 gives the full-shift witness for D26 and uses the
same factor square as D25. It does not repeat D32's 4,330-source audit or claim
new validation of generic Takens embeddings. It does not infer reset rights
or simultaneous branch execution from a language of possible words.

**New bridge: paper proof plus exact finite controls.** The lower bound in
X04(A) is one word per source state, and the upper bound is an overlap-selected
source, not a homomorphism of the original source. Every hypothesis has a
countercontrol: `{01}` is a dead end, equal initial blocks can have unequal
next blocks, a one-state input recognizer accepts every binary word, and a
constant observer ignores all microscopic symbolic growth. A finite source
can match all words at one horizon and remain periodic; no finite observation
certifies actual infinite chaos. De Bruijn cycles prove tightness even under
the extra one-cycle requirement, while other minimal surrogates may have
multiple components.

**Execution history.** The first probe run failed with `KeyError: 'diameter'`
because this reviewer used an incorrect name for the existing API field.
Inspection showed the correct key is `final_diameter`; the harness was fixed
and strengthened to check `final` endpoints as well. This was an audit-harness
error, not a source theorem failure. The corrected command
`python scripts/swarm_x04_probe.py` exits zero in exact rational arithmetic.
The committed receipt records 511 binary and 364 ternary word cases; 5,372
set partitions; 1,023 cylinders; 12,286 interval images; 936 higher-block
checks from 234 complete source tables; eight de Bruijn cycles and eight
factor counterexamples; 30 horizon/precision thresholds; 1,025 future-bin
grid controls. No full-suite or Lean success is claimed by this assignment.

**Research boundary.** The finite-horizon surrogate theorem, graph proof,
covering proof, and explicit distinctions are local mathematical synthesis of
classical material. This review does not establish academic novelty. A fresh
reviewer can attack the proof of the overlap-selected realization, the use of
closed-cylinder length subadditivity, or the all-time factor contradiction;
each has an explicit map and quantifier rather than a semantic analogy.
