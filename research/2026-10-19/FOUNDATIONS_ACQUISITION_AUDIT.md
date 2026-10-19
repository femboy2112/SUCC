# Independent acquisition audit

**Verdict:** the finite deterministic, observed-cost acquisition theorem and
checker survived this audit. One sentence in the completeness proof needs
the correction below. No new theorem or academic-priority finding is claimed.
The audited implementation hash and exact finite counts are in
`FOUNDATIONS_AUDIT_RECEIPT.json`. The foundations worktree was not edited.

## Proof boundary

The all-action Bellman inequality is a **lower** certificate: induction on
any finite successful policy tree gives `L <= tree cost`. In particular an
infinity-labelled belief cannot have a finite successful tree. The selected
policy's reverse cost inequality gives an **upper** certificate only together
with its strictly decreasing natural-number rank. That rank rejects a free
nonidentifying loop even when its Bellman equation admits value zero.

The finite horizon argument is sound for the stated contract. A repeated
origin/current belief on one branch permits replacing the earlier subtree
by the later one. All original possibilities then remain available to the
replacement; deleting nonnegative charges cannot increase total cost.
Repetition elimination bounds successful trees by the finite arena size.

**Completeness correction:** a root-optimal minimax tree can have suboptimal
internal subtrees on slack branches. It is not true that every action in
every optimal tree is locally optimal. For example, one root outcome incurs
cost 10 and terminates, while another incurs zero then identifies at cost 5
despite a zero-cost identifying alternative. The tree is root-optimal at 10,
but its second action is not optimal at that child belief.

The needed rank existence follows by a different argument. Call an action
optimal if all children are finite and its cost-plus-optimal-child maximum
is at most the parent's value. Suppose a set `U` of finite-valued beliefs
remains outside the goal attractor formed using optimal actions. Choose the
minimum value `m` in `U`, then choose a belief of value `m` with a shortest
optimal tree among such beliefs. Its root action is optimal, so it has an
outcome child still in `U`. Nonnegative cost and minimality of `m` force
that child to have value `m` and its entering cost to be zero. The subtree
then has cost at most `m`, hence is optimal, and is shorter: contradiction.
Thus every finite-valued belief enters the attractor, giving a single
proper positional policy and decreasing ranks. This theorem, not testing
alone, justifies the oracle's stationary-policy enumeration. The correction
was sent to the foundations author before integration.

Exact costs are observed, as explicitly declared in the model. Thus the past
charge is common to all originals compatible with one transcript. If charges
were hidden and source-dependent, this unweighted belief state would in
general omit information needed for minimax accumulated cost. The present
proof does not cover that changed interface. It also does not cover negative
costs, stochastic termination, bounded controller memory, restoration, or
authentication of the original-source label.

Restricting a successful acquisition policy to fewer originals preserves
universal legality and cost feasibility. The budget-feasible sets are
therefore hereditary. Minimal infeasible sets characterize feasible color
classes, so weak hypergraph coloring gives the exact prior-advice alphabet.
The maximum over initially known observation fibers correctly permits code
reuse. `advice_frontier` reports the bit/cost frontier; equal-width alphabet
improvements need not be separate bit-frontier points.

## Independent executable receipt

Run from an integrated checkout:

```sh
python research/2026-10-19/audit_foundations_acquisition.py
```

For the separate audited lane, add `--repo /path/to/SUCC-forge-foundations`.
The script rebuilds the reachable beliefs directly from raw edge tables,
enumerates all stationary policies, and simulates each fixed original source.
It does not use the production arena, goal, branching function, Bellman
recurrence, rank construction, partition enumeration, or minimal-bad-set
algorithm as an oracle. Only raw model dataclasses are shared. This closes
the narrower independence boundary of the original tests, whose policy
oracle received the production certificate's belief universe.

* All **6,561** two-carrier, two-action tables: each of four rows is absent
  or one of `2 targets × 2 receipts × 2 costs {0,1}`.
* **140** fresh three-carrier, three-original, two-action models, seed
  `202610199113`, observed costs in `{0,1/2,1}`; no skipped models.
* **482** budget comparisons against independent source-subset values and
  literal advice-code enumeration, including minimal infeasible hyperedges.
* **1,527** false value mutations and **497** zeroed nonterminal-rank
  mutations rejected. The largest enumerated policy family had 256 members.

All agreed. These are finite implementation checks. The source hash fixes
the checked artifact; later implementation changes require rerunning it.

## Primary-source priority clarification

Hierons and Türker, *Incomplete Distinguishing Sequences for Finite State
Machines*, DOI [10.1093/comjnl/bxv041](https://doi.org/10.1093/comjnl/bxv041):
the [institutional full manuscript](https://bura.brunel.ac.uk/bitstream/2438/11127/1/Fulltext.pdf)
was obtained and its Definitions 1.4/3.3, Lemma 6.2, and §7.1 inspected.
Original/current bookkeeping is already explicit: Lemma 6.2 tracks state
pairs, while §7.1 maintains initial and current sets. It is not a new
source-indexing invention. Their MinSetADS problem covers every pair with
distinguishable subsets; our prior-advice problem instead partitions sources
according to already-known labels. Their §2 also attributes partitioning into
sets admitting distinguishing sequences to Kohavi, Rivierre and Kohavi
(1974). That attribution was found, but the 1974 full paper was not audited.
The downloaded 27-page manuscript SHA256 is
`0afb45a803ac7789315b3785e76d4da3a8f817fecc8f92a4c09ad5e2e4892ab9`.
The public endpoint uses `application/octet-stream`; the earlier browser
parsing failure did not mean that its PDF was unavailable. No third-party
PDF is committed.

Türker, Ünlüyurt and Yenigün, *Effective algorithms for constructing minimum
cost adaptive distinguishing sequences*, Information and Software Technology
74 (2016), 69–85, DOI
[10.1016/j.infsof.2016.02.001](https://doi.org/10.1016/j.infsof.2016.02.001):
the primary publisher's abstract/introduction were inspected. They already
study cost objectives including tree height, external path length and weighted
leaf depth. This is direct prior art to cost-sensitive identification. It
does not, in the inspected material, establish the identical observed
state-dependent charge/prior-advice formulation. No full-paper priority
clearance is inferred from that narrower comparison.

**Remaining verdict:** the budget-parametrized hypergraph statement is a
proved specialization of a classical hereditary-family equivalence. Its
precise academic priority remains **UNVERIFIED**. Finite correctness and
clear model boundaries should survive; claims of invention of destructive
identification, original/current bookkeeping, or feasible-set partitions
should not be made.
