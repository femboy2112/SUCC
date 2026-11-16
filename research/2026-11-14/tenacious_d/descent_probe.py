"""Exact finite cross-checks for the action/word/path interface. Standard library only."""

from collections import Counter, defaultdict, deque
from itertools import product
import json


def indexed(edges):
    result = defaultdict(set)
    for source, letter, target in edges:
        result[source, letter].add(target)
    return result


def graph_quotient(edges, blocks):
    return {(blocks[x], label, blocks[y]) for x, label, y in edges}


def language_witness(edges, blocks, roots):
    """Find a shortest omitted word or exhaust the exact subset-product automaton."""
    letters = {letter for _, letter, _ in edges}
    source = indexed(edges)
    quotient = indexed(graph_quotient(edges, blocks))
    initial = (frozenset(roots), frozenset(blocks[x] for x in roots))
    queue = deque([(initial, ())])
    seen = {initial}
    while queue:
        (up, down), word = queue.popleft()
        actual = {blocks[x] for x in up}
        if actual != down:
            assert actual < down
            return word
        for letter in sorted(letters):
            new_up = frozenset(y for x in up for y in source.get((x, letter), ()))
            new_down = frozenset(y for x in down for y in quotient.get((x, letter), ()))
            next_pair = (new_up, new_down)
            if next_pair not in seen:
                seen.add(next_pair)
                queue.append((next_pair, word + (letter,)))
    return None


def all_starts_exact(edges, blocks):
    return all(language_witness(edges, blocks, [x]) is None for x in range(len(blocks)))


def all_blocks_exact(edges, blocks):
    return all(language_witness(edges, blocks, [x for x, b in enumerate(blocks) if b == a]) is None
               for a in set(blocks))


def congruent(table, blocks):
    """Direct function-descent test, independent of the language automaton."""
    signatures = defaultdict(set)
    for x, row in enumerate(table):
        results = tuple(None if step is None else (step[0], blocks[step[1]]) for step in row)
        signatures[blocks[x]].add(results)
    return all(len(values) == 1 for values in signatures.values())


def partitions(n):
    if n == 0:
        yield ()
        return
    for prefix in partitions(n - 1):
        for block in range(max(prefix, default=-1) + 2):
            yield prefix + (block,)


def deterministic_census():
    counts = Counter()
    for n, actions, output_count in [(2, 2, 2), (3, 1, 2)]:
        choices = [None, *product(range(output_count), range(n))]
        for flat in product(choices, repeat=n * actions):
            table = [flat[x * actions:(x + 1) * actions] for x in range(n)]
            edges = [(x, (a, step[0]), step[1]) for x, row in enumerate(table)
                     for a, step in enumerate(row) if step is not None]
            for blocks in partitions(n):
                faithful = all_starts_exact(edges, blocks)
                assert faithful == congruent(table, blocks)
                counts['models_with_partition'] += 1
                counts['rooted_exact'] += faithful
    assert 0 < counts['rooted_exact'] < counts['models_with_partition']
    return counts


def independent_edge_census():
    counts = Counter()
    for n in (1, 2, 3):
        possible = list(product(range(n), repeat=2))
        for mask in range(1 << len(possible)):
            edges = [(u, i, v) for i, (u, v) in enumerate(possible) if mask & (1 << i)]
            for blocks in partitions(n):
                pooled = all_blocks_exact(edges, blocks)
                rooted = all_starts_exact(edges, blocks)
                pair_condition = all(blocks[v] != blocks[s] or v == s
                                     for _, _, v in edges for s, _, _ in edges)
                source_condition = all(blocks.count(blocks[u]) == 1 for u, _, _ in edges)
                assert (pooled, rooted) == (pair_condition, source_condition)
                counts['models_with_partition'] += 1
                counts['pooled_exact'] += pooled
                counts['rooted_exact'] += rooted
    assert 0 < counts['rooted_exact'] < counts['pooled_exact'] < counts['models_with_partition']
    return counts


def chain_test(letter_sequence, target_word):
    relation = {(i, i) for i in range(len(target_word) + 1)}
    for letter in letter_sequence:
        next_relation = {(i, i + 1) for i, w in enumerate(target_word) if w == letter}
        relation = {(u, v) for u, mid in relation for other, v in next_relation if mid == other}
    return (0, len(target_word)) in relation


def weak_unit_laws():
    """Check every order, associative, monotonicity and union condition on a four-element model."""
    values = range(4)
    unit = 3
    def mul(a, b):
        return a if b else 0
    for a, b, c in product(values, repeat=3):
        assert mul(a, b | c) == (mul(a, b) | mul(a, c))
        assert mul(a | b, c) == (mul(a, c) | mul(b, c))
        assert mul(mul(a, b), c) == mul(a, mul(b, c))
        assert mul(0, a) == mul(a, 0) == 0
        assert mul(a, unit) == a and (a & mul(unit, a)) == a
    assert mul(unit, 1) == 3 != 1


def small_quantale_controls():
    """Exhaust every ordered 3-element chain quantale and the smaller-table witnesses."""
    n = 3
    choice = range(n)
    count = evaluations = 0
    # Bottom is forced absorbing. Only the four positive-positive products vary.
    for entries in product(choice, repeat=4):
        table = ((0, 0, 0), (0, *entries[:2]), (0, *entries[2:]))
        for unit in choice:
            if any(table[unit][a] != a or table[a][unit] != a for a in choice):
                continue
            if any(table[a][table[b][c]] != table[table[a][b]][c]
                   or table[max(a, b)][c] != max(table[a][c], table[b][c])
                   or table[c][max(a, b)] != max(table[c][a], table[c][b])
                   for a, b, c in product(choice, repeat=3)):
                continue
            count += 1
            if unit == 2:
                edges, blocks = [(0, 'a', 0)], (0, 0)
            else:
                edges, blocks = [(0, 'a', 1), (1, 'a', 2), (2, 'a', 0)], (0, 0, 1)
            assert not all_starts_exact(edges, blocks)
            quotient = graph_quotient(edges, blocks)
            for value in choice:
                def closure(size, edge_list):
                    weights = [[unit if i == j else 0 for j in range(size)] for i in range(size)]
                    while True:
                        result = [r.copy() for r in weights]
                        for x in range(size):
                            for u, _, v in edge_list:
                                result[x][v] = max(result[x][v], table[weights[x][u]][value])
                        if result == weights:
                            return weights
                        weights = result
                source_rows = closure(len(blocks), edges)
                abstract_rows = closure(len(set(blocks)), quotient)
                for x, a in enumerate(blocks):
                    for b in set(blocks):
                        assert abstract_rows[a][b] == max(source_rows[x][y] for y, c in enumerate(blocks) if b == c)
                evaluations += 1
    identity = frozenset({(0, 0), (1, 1)})
    edge = frozenset({(0, 1)})
    four = {frozenset(), identity, edge, identity | edge}
    for a, b in product(four, repeat=2):
        assert a | b in four
        assert frozenset((i, k) for i, j in a for l, k in b if j == l) in four
    return {'three_element_unital_quantales': count, 'blind_unary_valuations': evaluations,
            'four_element_subquantale_size': len(four)}


def controls():
    assert all_blocks_exact([(0, 'a', 0)], (0, 0))
    assert language_witness([(0, 'a', 0)], (0, 0), [1]) == ('a',)
    ghost_edges = [(0, 'a', 1), (2, 'b', 3)]
    assert language_witness(ghost_edges, (0, 1, 1, 2), [0]) == ('a', 'b')
    words = [''.join(w) for n in range(5) for w in product('ab', repeat=n)]
    for expected, candidate in product(words, repeat=2):
        assert chain_test(candidate, expected) == (candidate == expected)
    weak_unit_laws()
    return {'singleton_word_comparisons': len(words) ** 2,
            'one_sided_unit': 'left multiplication by the unit maps {u} to {u,v}',
            'pooled_ghost': 'ab', 'rooted_ghost': 'a'}


if __name__ == '__main__':
    print(json.dumps({'D1': deterministic_census(), 'D3': independent_edge_census(),
                      'controls': controls(), 'D1b': small_quantale_controls()}, indent=2, sort_keys=True))
