"""Exact integration probe for a prefix-identical, asymptotically coherent source."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'analytic'))
import resolvent as a


def main():
    rows = []
    for d in (1, 2, 3, 5, 8):
        mu = a.moments(2*d+1)
        p = a.monic_orthogonal(mu, d)
        count = 2*d+40
        fake = a.atomic_moments(p, mu, count)
        alpha = a.resolvent(mu, d)
        budget = a.atomic_tail_budget(mu, d)
        original = u = Q()
        tails = []
        previous = None
        for n, value in enumerate(fake, 1):
            assert value > 0
            if previous is not None:
                assert value < previous
            previous = value
            u = 16*u + value
            if n <= 2*d:
                original = 16*original + a.source(n)
                assert u == original
            tail = 16**n*alpha - u
            assert tail > 0
            tails.append(tail)
            # Exact rational boundary supplies the coherent frequency.
            assert (alpha.denominator*(u+tail)).denominator == 1
        assert sum(tails, Q()) < budget
        assert fake[2*d] != mu[2*d]
        # Compare the resolvent budget to direct finite geometric sums and
        # a separately computed remainder using the rational moment recurrence.
        # Sum T_n = [sum r_n -16 alpha]/15, with finite telescoping residual.
        partial_source = sum(fake, Q())
        partial_tails = sum(tails, Q())
        residual = (a.resolvent(mu, d, Q(1))-partial_source-16*tails[-1])/15
        assert budget-partial_tails == residual > 0
        rows.append({'d':d,'matched_states':2*d,'extra_source_terms':40,
                     'boundary':str(alpha),'denominator_bits':alpha.denominator.bit_length(),
                     'tail_budget':str(budget),'coherent_frequency':str(alpha.denominator),
                     'partial_tail_numerator_bits':partial_tails.numerator.bit_length(),
                     'partial_tail_denominator_bits':partial_tails.denominator.bit_length(),
                     'partial_tail_hex_sha256':hashlib.sha256(
                         (hex(partial_tails.numerator)+'/'+hex(partial_tails.denominator)).encode()).hexdigest(),
                     'first_unmatched_source_index':2*d+1})
    print(json.dumps({'status':'PASS','cases':rows,
                      'authority':'exact finite integration checks; asymptotic statement proved in dossier',
                      'input_sha256':hashlib.sha256((HERE/'analytic/resolvent.py').read_bytes()).hexdigest()}, indent=2))


if __name__ == '__main__':
    main()
