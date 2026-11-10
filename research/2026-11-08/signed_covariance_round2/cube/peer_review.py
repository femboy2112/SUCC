"""Separate exact checks accompanying a scoped CH/H paper review.

This does not import chronology or hostile implementations. Running it checks
finite algebra; the prose review itself is a separate human-readable artifact.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import argparse
import json


def run():
    counts = {'gram_cases': 0, 'weight_cases': 0, 'chronological_word_cases': 0}
    for A in range(1, 15):
        for H in range(1, 20):
            f = [Q(((r*r+3*r+A) % 7)-3, 3) for r in range(A)]
            blocks = sum(sum(f[max(0, t):min(A, t+H)])**2
                         for t in range(1-H, A))/(A*H*H)
            pairs = sum(x*x for x in f)/(A*H)
            pairs += sum(Q(2*(H-l), H*H*A)*sum(f[r+l]*f[r]
                          for r in range(max(0, A-l))) for l in range(1, H))
            assert blocks == pairs
            assert Q(sum(f), A)**2 <= Q(A+H-1, A)*blocks
            counts['gram_cases'] += 1
    for H in range(1, 65):
        assert sum(Q(2*(H-l)*l, H*H) for l in range(1, H)) == Q(H*H-1, 3*H)
        assert sum(Q(2*(H-l), H*H) for l in range(1, H)) == 1-Q(1, H)
        counts['weight_cases'] += 1
    for p in (41, 73, 97, 137, 193, 241):
        for d in range(1, 5):
            M = 16**d
            orbit = []
            r = 1
            while r not in orbit:
                orbit.append(r)
                r = 16*r % p
            counts_by_word = {}
            for v in orbit:
                y = Q(v, p)
                word = 0
                for _ in range(d):
                    digit = (16*y).numerator//(16*y).denominator
                    y = 16*y-digit
                    word = 16*word+digit
                assert word == M*v//p
                counts_by_word[word] = counts_by_word.get(word, 0)+1
            m = len(orbit)
            tv = (sum(abs(Q(c, m)-Q(1, M)) for c in counts_by_word.values())/2
                  +Q(M-len(counts_by_word), 2*M))
            assert tv >= max(Q(0), 1-Q(m, M))
            if M >= p:
                assert tv == 1-Q(m, M)
            counts['chronological_word_cases'] += 1
    return counts


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    result = {'status': 'all independent finite checks passed',
              'code_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'checks': run(),
              'scope': 'finite arithmetic verification only; see PEER_REVIEW.json for the scoped paper review'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps(result['checks'], sort_keys=True))
