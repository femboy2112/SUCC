# First-cause nucleation: finite recognition from a fair causal walk

**Steelman.** At a mastered frame's limit, no next admissible action is preferred by its existing novelty score. The observer nevertheless moves, records and analyzes its actual source-coupled causal history. If the required differential is constructible and reachable under a coherent non-starving exploration law, can discovery be used as a finite-time existence step in a proof? Yes under the following explicit obligations.

## PRF-01. Certificate contract and finite stopping time

Fix a carrier x, source passport sigma, lawful action/history space, filtration F_t (actual retained action/readout labels, internal state and permitted random coins), and a sound finite certificate predicate Ver(h,c). A certificate c is a finite object specifying the required tool's construction, source/domain, necessary causal readouts, and proof or calibrated scoped discriminator. The verifier must accept on the declared evidence, not on an omniscient hidden truth label. Sound means every accepted c implies the stated target T(x) within its domain. The acceptance event is F_t-measurable; account for verification time as part of t if claiming wall-clock computational termination. Use an effective proof checker or a specified finite exact readout test; universal semantic validity is not assumed decidable.

Let tau = inf{t >= 0: a sound certificate has been accepted by t}, with inf(empty)=infinity. Keep certificates once accepted; tau is a stopping time. If only a hypothesis is verified, the conclusion is only that hypothesis's scoped test result.

Assume integers L >= 1, 0 < eps <= 1 such that for every k, on {tau > kL},

\[
 {\mathbb P}(\tau\le (k+1)L\mid\mathcal F_{kL})\ge\epsilon .
\]

Then

\[
 {\mathbb P}(\tau>kL)\le(1-\epsilon)^k,\qquad
 {\mathbb P}(\tau<\infty)=1,\qquad E\tau\le L/\epsilon.
\]

Proof: multiply the conditional survival inequality by the indicator of {tau > kL}, take expectations and iterate. For the mean, sum P(tau>t) over t>=0 and bound each L-term block by its first term. No independence, stationarity, or Gaussian model is needed. Conditional versions hold after an a.s. finite starting stopping time with the same post-start bound. For eps=1, the first block suffices.

This is a probabilistic finite-time theorem, not a finite worst-case deadline. A null set of infinite walks can exist. For 0<eps<1 the probability of discovery by kL is at least 1-(1-eps)^k; a confidence target 1-delta is met for k >= log(delta)/log(1-eps). Certainty about the target follows from soundness of actual accepted certificates, not from that confidence bound.

## PRF-02. Sharp hazard criterion and adaptive sufficient condition

Define h_t=P(tau=t | tau>=t), when survival is positive. Then

\[
 P(\tau>k)=P(\tau>0)\prod_{t=1}^k(1-h_t).
\]

Assume P(tau>0)>0. If any h_t=1, survival ends there. Otherwise P(tau=infty)=0 iff sum h_t diverges: use log(1-h)<=-h, and for a convergent sum h_t->0, hence -log(1-h_t)<=2h_t eventually. The formula is exact, but the h_t are ensemble hazards conditional on survival, not per-history exploration probabilities.

For an adapted walk let q_t=P(tau=t | F_(t-1)) (zero after acceptance). If sum q_t= infinity on the event of nontermination, except possibly a null set, then P(tau=infty)=0. Proof: M_k=1_{tau>k} exp(sum_{t<=k} q_t) is a nonnegative supermartingale since (1-q)e^q<=1; E M_k <=1. On the claimed surviving paths M_k tends to infinity. Fatou's lemma rules out positive probability of such paths. Equivalently one may use Levy's conditional Borel-Cantelli theorem. This argument does not assume independent steps.

Countermodels with independent time-dependent trials, indexed t>=1:
- h_t=1/(t+1)^2 > 0: survival after k = (k+2)/(2(k+1)), tending to 1/2. All odds positive, yet discovery fails with positive probability.
- h_t=1/(t+1): survival =1/(k+1), tending to zero, but E tau=infinity. Almost-sure finite time does not imply finite expected time.
- constant 0<p<1: geometric survival; no deterministic finite bound even though E tau=1/p.

These identities telescope exactly and are calibrated in the receipt.

## PRF-03. Finite causal graph corollary: equal-priority blind search

Let S be a finite directed graph of actual reachable search states (include all history-relevant state in the model, or give a valid quotient preserving target reachability and probabilities). The target B consists of states with a recognized certificate. From every reachable non-target state there is a directed path to B. Suppose each legal edge used on such a path has conditional probability at least p>0 at its step, regardless of the prior history. Then from every pre-hit state there is a simple path of length <= |S|-1. With L=max(1,|S|-1), following its edges hits with conditional probability >= p^L. PRF-01 gives finite a.s. discovery and E tau <= L/p^L.

For uniform selection among a nonempty finite set of legal edges of out-degree <=d, p=1/d. This formalizes equal-priority wandering at a plateau. Equal immediate novelty readouts alone do not imply uniform selection, Markov behavior, returnability, or independence. Uniform choice is an explicit policy; do not silently give the observer access to hidden states to implement it.

If the graph is finite and time-homogeneous with fixed positive edge weights, absence of reachable closed non-target classes is the equivalent reachability condition. A finite irreducible graph automatically qualifies for a nonempty target. If an accepting history, rather than a state, is required, augment by its finite recognizer or keep a proved history-progress quotient; mere endpoint reachability is not enough.

### Sharp infinite-graph crucible

On the infinite 3-regular tree, choose every neighbor with probability 1/3, at every step, and always move. Root is the target. Every vertex can reach it, yet starting one edge away the probability of ever hitting it is 1/2. Give every old-frame readout the same value if desired.

Proof: distance j>=1 from the root moves inward with probability 1/3 and outward with probability 2/3. Before depth K, the probability of reaching depth 0 is H_K(j)=(2^(K-j)-1)/(2^K-1), from the two boundary values and harmonicity H(j)=(H(j-1)+2H(j+1))/3. Exit of the finite interval is a.s. finite by PRF-03, or the same block argument. As K->infinity, the increasing events of hitting 0 before K exhaust eventual hitting, and H_K(1)->1/2. Thus even uniform movement, connectedness and a finite constructive path do not force discovery. The tree's escaping paths are a genuine recurrence obstruction, not mere bad luck in one experiment.

A simpler nonreversible counterexample is the binary tree of append-only words: the target word starts with A, and the first B edge makes it unreachable. A random path need not enumerate all words. Keep an append-only *journal* but allow lawful return/replay of the source configuration.

## PRF-04. A constructive repair: recurrent anchors and countable fair search

Let a repeatable lawful anchor (preparation or state with a verified return transport) be available, and a countable recursively enumerable set of finite admissible candidate scripts w_1,w_2,... . Scripts can include multiple preparations, readouts, tool combinations and proof-check steps. Require a finite, sound verifier; candidate testing must terminate or be fairly interleaved (dovetail any partial computations). A failed attempt must not destroy the possibility of subsequent trials, and reset must be a legal action, with its history retained. A script can certify a tool only when its source assumptions and finite data genuinely support the target.

At each anchor trial, sample index j with probability 2^(-j) for j>=1, independently of past attempts, or use a predictable lower bound with divergent cumulative mass. Execute/interleave the script, preserving the journal. For a specific finite valid script w_J that succeeds under the declared preparation, the first sampling time is geometric, hence finite a.s., with mean 2^J trials. If every attempted script finishes in finite steps a.s., finite successful trial index also gives finite actual step time a.s.; it need not have finite mean step cost unless costs are controlled. Uniform bounded blocks or integrable expected attempt costs give quantitative time bounds. If a script succeeds probabilistically with conditional probability q>0 given selection, replace its trial hazard by >= 2^(-J) q. A countable distribution with full support is a design choice, not entailed by subjective indistinguishability.

An alternative with a finite alphabet of size d and independent uniform next action is to reserve repeatable blocks of length L containing a particular successful script. Its exact word has probability d^(-L); no need to know which word it is during search. If the start state varies and the word is not portable, the bound is invalid. If resets are unavailable, prove recurrent return to a lawful anchor and a positive conditional success chance on each return; apply the same survival bound in return counts. Null recurrence can give infinite mean elapsed time.

For countably many finite certificates each with a valid positive probability and recognizable acceptance, every individual certificate is eventually seen a.s. by countable intersection of probability-one events. In an adaptive stage tower with stage k starting at tau_(k-1), prove conditional a.s. completion at each finite stage; induction and countable intersection give P(forall k<infty, tau_k<infty)=1. There is no claimed uniform finite time for all stages, uncountable simultaneous coverage, or existence of an infinite hierarchy from its first member. With disjoint finite targets requiring at least one step each, tau_k>=k.

### Deterministic extraction and proof rule

For each fixed carrier satisfying the hypotheses, construct the probability space without assuming the desired theorem. If a sound verifier accepts a finite certificate a.s., the acceptance set is nonempty, so a finite valid witness exists. If hypotheses are effective and all finite witnesses can be enumerated and checked, deterministic enumeration/dovetailing also terminates, even if an explicit time bound is unavailable. Randomness is one discovery policy, not logically required for existence. A proof can invoke this lemma without exhibiting the discovery path. To prove a deterministic universal result, establish the hypotheses for each source separately, with a sound source-relative verifier; do not exchange pointwise a.s. statements with an uncountable simultaneous assertion.

Reductio use: assume not T, derive independently (i) a lawful nonempty search model, (ii) a reachable finite certificate of T under that model, (iii) sound verification and fairness. The probability-one event of acceptance contradicts not T. **Do not hide the theorem inside (ii).** Constructibility of a *candidate* or positive probability of proposing it does not prove a valid certificate exists. If the purported witness is an exact infinite limit without finite evidence or an independent theorem certifying it, PRF-01 does not apply to it. For arbitrary undecidable targets no universal terminating proof finder follows.

## PRF-05. The history decoder and the exact Grokking Abiogenesis control

Import GA-07 from the parent branch. In a declared real four-coordinate source, P=e1^T, A=I+E12+E34 and B=I+E13+E24. All pure histories span only e1,e2,e3; the fourth coordinate is unobserved. A and B commute. At repeated preparations of the SAME x=(x1,x2,x3,x4), take the four labelled cells

O00=x1, O10=x1+x2, O01=x1+x3, O11=x1+x2+x3+x4.

Their mixed differential O11-O10-O01+O00=x4, and its row e4^T lies outside the pure span. With the standard Euclidean metric it is perpendicular. This is an exact source-discriminating bridge, including when the actual readout x4 happens to be zero (rank novelty is a function-level property). A single zero output is not a null theorem.

Assume repeated source preparation is legal, labels retained, and the four cell scripts available to the observer with no preference from its old novelty score. Uniform independent cell trials give the coupon-collector bound P(not all four seen by k)<=4(3/4)^k and mean 4(1+1/2+1/3+1/4)=25/3 trials. Proof: union bound over missing cells; at j distinct cells the next new cell arrives geometrically with probability (4-j)/4. If O00,O10,O01 are already authenticated and reusable, the mixed cell has geometric wait with mean 4 trials; only the remaining certificate is needed. The predetermined decoder can then compile the mixed row as a new primitive, strictly increasing accessible rank; its semantic expressibility already existed in the full word closure. At a point where available data are genuinely indistinguishable across every valid full-history probe, no random walk extracts new source information: same-seed coupling of adaptive histories proves the transcript distributions equal (GA-02). An action label may provide an algebraic discovery route without new source evidence, but cannot distinguish two rivals with identical complete transcripts.

Controls: A0=I+E12, B0=I+E13 produce identical pure histories and zero mixed functional; the mixed cell's observed zero at one x cannot by itself decide between A,B and A0,B0. To certify the functional relation on a whole linear family, require a basis of preparations or symbolic law proof. The experiment's mathematical contract and calibrated generator, not chance alone, supply verification. In-span nonzero contrast (one-dimensional A=2,B=3) is not rank novelty. No new dimension arises after full invariant row closure.

## PRF-06. Limits, operational saturation and learning

The finite-accessible old frame can be saturated while a higher type of object (relations, operators, paths, transport) is underexplored. If all legal word-readouts are already in a fully invariant span W, no word of those actions escapes W; if a fixed complete semantic closure is exhausted, no same-language composition expands it. A macro can instead enlarge bounded accessible closure (GA-03); a changed metric/topology, observation, adjoint, limit operation or type can genuinely enlarge the declared toolkit. These are separate from carrier change.

For an analytic-limit observer, do not conflate:
- equal current novelty score (policy tie);
- indistinguishable source laws under every allowable full history (probe boundary);
- missing route in a larger constructive toolkit;
- full semantic closure (actual boundary).
A fair search can solve route debt, not manufacture information absent from every allowed transcript.

Neural grokking remains a testable hypothesis, not a consequence of the probability lemma. Nanda et al., [Progress measures for grokking via mechanistic interpretability](https://arxiv.org/abs/2301.05217), found Fourier circuits gradually forming before visible generalization; fixed deterministic optimizers can also find routes. Distinguish first finite bridge access, growth, dominance and stabilization. Future tests must vary exploration and evidence independently and retain all failures/censoring. No biological, mental, quantum or neural mechanism is proved.

**Verdict:** conditional almost-sure finite first cause and fair-search realization PROVED LOCAL / classical probability; unconditional always-moving implication REFUTED by the tree and summable hazards; universal recursive growth and neural causal mechanism HYPOTHESIS/UNVERIFIED.
