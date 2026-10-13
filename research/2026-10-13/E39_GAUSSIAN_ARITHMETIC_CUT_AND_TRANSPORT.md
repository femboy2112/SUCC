# E39 — Gaussian arithmetic cuts and faithful voltage transport

## 1. Original question

Can finite observational records certify transport in the **actual** Gaussian-prime graph, while separating complete windows from unknown exterior paths? The faithful steelman asks for an explicit arithmetic barrier, not a declaration that a finite plot proves an infinite moat. This independent first-generation contribution uses immutable parent `5eb09e7cba36ec01b8f9d6834b78b5766fd93935` on `research/swm-e39-2026-10-13`. No sibling conclusions or atlas registry were read.

## 2. Existing mathematical context

[Conrad, Theorem 9.9](https://kconrad.math.uconn.edu/blurbs/ugradnumthy/Zinotes.pdf) classifies Gaussian primes: off-axis, rational-prime norm; on-axis, prime coordinate magnitude congruent to 3 modulo 4. Thus 3 is prime despite norm 9; 5 and 3+4i are not. Historical context is [Gethner–Wagon–Wick's publisher record](https://www.tandfonline.com/doi/abs/10.1080/00029890.1998.12004889); its full text was unavailable, so no numerical thresholds are imported.

[Schluchter §3](https://arxiv.org/html/1501.01060v1) describes ordinary voltage graphs and their **derived covering graph**. That covering hypothesis matters. The pinned [OpenAI periodicity reduction](https://raw.githubusercontent.com/openai/math/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/periodicity.tex) uses actual periodic norm sieves and finite exceptional primes. Its separate all-step theorem is unnecessary here; Lean was not executed.

Frozen SUCC dossiers originate at `b606b78bb8ea716fd30fe858043b971c0d43a788` (moats), `a737061cf880292261a63a703b73eb3f198a6600` (holonomy), and `d1e64948f60662601074c1738d355b3456a17dcf` (source-completeness calculus). The import manifest records FuckingRH `ba075348b7bcc66d938b3e0ca96c26e95bba340a`; that commit object is unavailable locally, while the preserved originals and blob verifier are accessible.

## 3. Proposed SUCC objects

Fix integer (K\ge0), all Gaussian-prime associates \(\mathcal G\), and the oriented basis \((1,i)\). Source darts are actual \(u\to v\) with \(0<N(v-u)\le K\), labelled \(v-u\in\mathbb Z^2\). Reverse darts have opposite labels.

A complete window record lists **every** lattice point's arithmetic classification and every legal prime-prime dart. For finite connected prime set \(C\), define

\[
\partial_K C=\{z+s:z\in C,\ 0<N(s)\le K\}\setminus C.
\]

Residue observation \(q_Q(z)=z\bmod Q\) forgets source identity. The observed multigraph retains every original dart and displacement; endpoint coincidence grants no periodic source law.

## 4. Candidate theorem

**E39.1 — PROVED LOCAL, finite arithmetic cut.** For every integer \(K\ge0\), every nonempty finite connected \(C\subseteq\mathcal G\), and every root \(c\in C\),

\[
C=\operatorname{Comp}_{G_K}(c)
\quad\Longleftrightarrow\quad
\partial_K C\cap\mathcal G=\varnothing.
\]

Connectivity and **all** boundary nonprimality certificates suffice, regardless of the unbounded exterior.

**E39.2 — PROVED LOCAL, residue-section obstruction.** For a finite connected source subgraph on \(C\), form its complete residue multigraph. There exists \(h:q_Q(C)\to\mathbb Z^2\) satisfying every observed dart equation \(h(q_Qv)-h(q_Qu)=v-u\) iff \(q_Q|_C\) is injective. These are elementary classical graph arguments, not academic novelty claims.

## 5. Proof attempt

For E39.1, any source path leaving \(C\) has a first exit dart whose endpoint is a prime in \(\partial_K C\), contradicting the certificate. Hence leaving and later re-entry are both excluded. Conversely, a prime boundary point is adjacent to \(C\), so lies in the full component. Internal connectivity gives equality.

For E39.2, integrate the equations along an actual source path from fixed \(c\) to \(z\). They telescope to \(h(q_Qz)-h(q_Qc)=z-c\). Equal residues therefore force equal source coordinates. Conversely, injectivity defines \(h(q_Qz)=z\), and every equation holds. This proves the actual map-level obstruction; flatness on the coordinate graph is automatic and says nothing by itself about component size.

## 6. Crucible

The independent standard-library probe certifies the complete window \([-12,12]^2\): 625 points, 168 Gaussian primes, 336 directed \(K=2\) darts. The component of \((1,1)\) has 100 vertices, maximum coordinate magnitude 11, and 265 **nonprime** boundary points. E39.1 therefore certifies this full global component, not merely its window intersection.

Eighty-one integer certificates contain exhaustive nonzero trial-division remainders or exact divisors. A separate Eratosthenes sieve checks rational classifications; all-pairs squared-distance enumeration independently checks generated edges.

The actual path

\[
(1,1),(1,2),(0,3),(-1,2),(-2,1),(-3,0),(-4,1)
\]

is residue-closed modulo 5 with voltage \((-5,0)\). Repeating its translation encounters \((-4,2)\), norm 20, which is composite. Thus nonzero observed holonomy does not establish a prime escape path.

All 12 controls reject: missing vertex, missing edge, fake norm-25 prime, forged primality, reversed voltage, missing boundary, missing component vertex, exterior/re-entry path, false truncated-component globality, excessive step, false repeated lift, and missing certificate shard. A genuine exterior path connects \((1,1)\) to \((-1,1)\) through \((1,2),(0,3),(-1,2)\), although the complete \([-1,1]^2\) window has four isolated vertices.

## 7. Verdict

**SURVIVES:** E39.1/E39.2 at PROVED LOCAL by written proofs; the explicit arithmetic certificate and mutations at TESTED MODEL. **REFUTED:** “complete-window separation implies global separation” and “nonzero prime-image quotient voltage implies arithmetic escape,” with the displayed receipts.

\(\kappa\) is direct contact with declared integer arithmetic; \(\phi\) is the exact checker pathway; \(\sigma\) retains source coordinates and frozen hashes. Six packet partitions share one source and do not create independent bearings. Commitment risk \(\rho\) earns no status promotion.

## 8. Remaining obstruction

The certificate concerns one root and one step bound. Other unbounded components remain unchecked. No uniform bound for all roots or all \(K\), independent all-step sieve existence, infinite observation, physical carrier identification, or RH theorem follows. Any RH route still owes authentic Euler/source identification, conductor, half-density, Gamma/poles, admissible tests and completed-form positivity without zero-position inputs. None is supplied here.

## 9. Cross-domain connection with actual maps

The path-groupoid map \(F_Q\) sends source vertices to residues and each source dart to its retained observed dart. The additive voltage functor obeys \(\Delta F_Q(\gamma)=\operatorname{end}(\gamma)-\operatorname{start}(\gamma)\). Source loops telescope to zero; observed loops need not lift to source loops. Moduli 23 and 29 are injective on this component, providing genuine coordinate sections. Rotation \((a,b)\mapsto(-b,a)\) transports voltage to \((0,-5)\); conjugation then gives \((0,5)\), verified exactly.

For certificate descent, restriction \(r_j\) keeps integer certificates with \(n\equiv j\pmod6\); compatible union \(m\) satisfies \(m(r_0c,\ldots,r_5c)=c\). The receiver rechecks complete geometry and arithmetic. This is a static restriction/union identity. A downward network protocol additionally needs actual issuance, authorized relays and causal ancestry; the probe runs no network and invents no such events.

## 10. Deliverables

New scoped files: [probe](E39_gaussian_cut_probe.py), [exact receipt](E39_GAUSSIAN_CUT_RECEIPT.json), and this dossier. The receipt binds the probe and five frozen inputs by SHA-256; it stores all vertices, darts, component, boundary and integer certificates.

A separate serialized-JSON replay verified the cut and all six stored hashes, exit 0. Retrieval of the pinned 2,735-byte `periodicity.tex` independently matched SHA-256 `1c3929027ce8db0174143c29134a8b38c812b9e27eed0d6d7af11d42acd408aa` and Git blob `73a1088e05c8a0651dba73553345d894618ce5a1`, exit 0. This verifies source bytes, not the theorem. Assertion checks run in ordinary Python; optimized Python is explicitly refused.

Commands: `python research/2026-10-13/E39_gaussian_cut_probe.py > research/2026-10-13/E39_GAUSSIAN_CUT_RECEIPT.json`, exit 0; `python scripts/verify_provenance.py`, exit 0, 72 items verified. Origin inspection `git cat-file -t ba075348b7bcc66d938b3e0ca96c26e95bba340a` exited 128: missing local object, explicitly preserved as an access boundary. No full suite/compiler ran under the swarm protocol. No archives, defaults, shared metadata or sibling files changed; no push.

**Next small lemma:** certify a minimal coordinate-retaining refinement of the mod-5 observation and prove its decoder recovers exactly this component's displacement potential, retaining the repeated-path composite falsifier. Independent crucible/principal acceptance remains pending.
