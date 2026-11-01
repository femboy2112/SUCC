"""Generate deterministic finite source receipt; not a universal theorem proof."""
from __future__ import annotations
import json,importlib.util
from pathlib import Path
root=Path(__file__).parent
spec=importlib.util.spec_from_file_location('acss_receipt',root/'arctan_chiral.py')
A=importlib.util.module_from_spec(spec);spec.loader.exec_module(A)

levels={}
for j in range(1,5):
    q=16**j
    seen={A.source_residue(n,j) for n in range(q)}
    levels[str(q)]={'permuted_residue_count':len(seen),'clock_size':q,'exact_bijection':len(seen)==q}

examples={}
for n in (1,2,3,4):
    examples[str(n)]={'source':str(A.source(n)),
        'source_mod_16':A.source_residue(n,1),'source_derivative_mod_16':A.lifted_derivative(n),
        'actual_U':str(A.finite_orbit(n)[n]),
        'chiral_unwrapped':str(A.chiral_orbit(n)[n]),
        'chiral_carry':A.chiral_integer_carry(n)}

fours={}
for k in (0,1,2,3,4,7,8):
    allowed=[l for l in range(16) if A.source_fourier16_numerator(k,l)!=(0,)*8]
    fours[str(k)]={'allowed_ell':allowed,'polynomial_numerator':{str(l):list(A.source_fourier16_numerator(k,l)) for l in allowed}}

machin=A.machin_pi_bounds(12)
result={
    'source':'unchanged four-pole BBP, literal U0=0',
    'test_scope':'finite exact Fraction/cyclotomic test receipts; analytic claims separately proved in PROOFS',
    'clock_permutation_receipts':levels,
    'source_examples':examples,
    'fourier_16_exact_cyclotomic_coefficients':fours,
    'all_r_ge_2_Fourier_support_rule':'ell == 3*k or 11*k (mod 16), necessary not sufficient',
    'dual_chiral_law':'J(z)=-z^-1, J F_r J=F_(1/2-r)',
    'solenoid_odd_torsion_r1_first4':[str(x) for x in A.odd_torsion_tower(A.source(1),4)],
    'chosen_halfturn_tower_first4':[str(x) for x in A.half_turn_tower(4)],
    'Machin_Gaussian_factor':'(5+i)^4 = 2(1+i)(239+i) = 476+480i',
    'Machin_rational_pi_bounds_12terms':[str(x) for x in machin],
    'chiral_torsor_Q15_permutation_count':len({A.finite_chiral_torsor_map(i,15,A.source(1)) for i in range(30)}),
    'finite_carrier_fourier_square':'DFT_(2Q)^2|x> = |-x>; shift by Q realizes x->Q-x',
    'selected_normality_theorem_proved':False,
    'full_repository_tests_executed':False,
}
if __name__=='__main__':
    (root/'FINITE_RECEIPT.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('Exact receipt generated',root/'FINITE_RECEIPT.json')
