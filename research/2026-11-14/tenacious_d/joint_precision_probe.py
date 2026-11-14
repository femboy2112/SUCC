"""Exact controls for the Jacobi comparison. Run directly to emit the receipt."""
from fractions import Fraction as F
from itertools import product
import json
from math import comb


def generalized_binom(a, length):
    value = F(1)
    for i in range(length):
        value *= (a - i) / (i + 1)
    return value


def four_pole(n):
    return sum(F(a, 8*n+b) for a, b in [(4,-7), (-2,-4), (-1,-3), (-1,-2)])


def radius_from_gram(moments, r, d):
    """Solve Hx=v by exact elimination and return the reciprocal of v.x."""
    vector = [(-r)**i for i in range(d + 1)]
    rows = [[moments[i+j] for j in range(d + 1)] + [vector[i]] for i in range(d + 1)]
    for j in range(d + 1):
        pivot = rows[j][j]
        assert pivot > 0
        rows[j] = [a/pivot for a in rows[j]]
        for i in range(d + 1):
            if i != j:
                scale = rows[i][j]
                rows[i] = [a-scale*b for a, b in zip(rows[i], rows[j])]
    return 1/sum(v*row[-1] for v, row in zip(vector, rows))


def jacobi_terms(alpha, d, r):
    terms = []
    for j in range(d + 1):
        polyn = sum(generalized_binom(j + alpha - 1, j-k) * comb(j+1, k)
                    * (1+r)**(j-k) * r**k for k in range(j+1))
        inv_norm = (2*j+alpha+1)*(j+alpha)/(j+1)
        terms.append(inv_norm*polyn*polyn)
    return terms


def main():
    selected = []
    cases = 0
    for n, d, r in product((1, 2, 8, 80, 1200), (1, 2, 4, 6), (F(1,16), F(1), F(3))):
        cases += 1
        alpha = n-F(7, 8)
        beta = [1/((alpha+k)*(alpha+k+1)) for k in range(2*d+1)]
        forcing = [four_pole(n+k) for k in range(2*d+1)]
        terms = jacobi_terms(alpha, d, r)
        kernel = sum(terms)
        assert radius_from_gram(beta, r, d)*kernel == 1
        actual = radius_from_gram(forcing, r, d)
        assert F(15,64) < actual*kernel < F(1,2)
        # Calculate sum_{k>=0} (k+1)^3 x^k in closed rational form.
        x = 1/(1+r)**2
        factor = 64*(1+4*x+x*x)/(1-x)**4
        assert terms[-1] <= kernel <= factor*terms[-1]
        if (n, d, r) in ((1, 1, F(1)), (8, 2, F(3)), (80, 4, F(1)), (1200, 6, F(1,16))):
            selected.append({"N": n, "d": d, "r": str(r),
                             "authentic_radius_times_beta_kernel": str(actual*kernel),
                             "kernel_to_final_term": str(kernel/terms[-1])})
    # Omission of the beta inverse norms fails even for N=d=r=1.
    a = F(1,8)
    ignored_norms_kernel = 1 + ((1+1)*a+2)**2
    assert ignored_norms_kernel != sum(jacobi_terms(a, 1, F(1)))
    return {"exact_grid_cases": cases, "selected_exact_ratios": selected,
            "omitted_norm_falsified": True}


if __name__ == "__main__":
    print(json.dumps(main(), sort_keys=True, indent=2))
