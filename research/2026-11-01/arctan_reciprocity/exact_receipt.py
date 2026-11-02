"""Deterministic exact rational AR-02/04/05 claim receipt generator."""
from __future__ import annotations
import importlib.util,sys,json
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('mirror_core_receipt',HERE/'arctan_mirror.py')
m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)


def run():
    g=m.rational_mirror_label()
    Q=F(106,819)
    vals=[]
    for h in (1,2,3,5,7,11):
        n=15*h
        re,im=m.gaussian_integer_power(819,106,n)
        sq=m.mirror_sine_squared(h)
        assert sq==F(im*im,681997**n)
        assert 0<sq<1
        vals.append({"h":h,"nonzero_gaussian_imag":str(im),
                     "sine_squared_exact":str(sq) if h<=3 else "see exact_receipt.py",
                     "sine_squared_approx_descriptive_only":round(float(sq),17),
                     "integer_coefficient_quadrature":list(m.signed_gaussian_quadrature_coefficients(h)) if h<=3 else "see exact_receipt.py"})
    rec={"claim":"AR-02/04/05 EXACT RATIONAL RECEIPT","normality_proved":False,
         "original_source_r1":str(m.forcing(1)),"original_source_r2":str(Q),
         "mirror_matrix":[[-819,106],[106,819]],
         "matrix_square_scalar":681997,
         "gamma_real":str(g['gamma_real']),"gamma_imag":str(g['gamma_imag']),
         "gamma_not_root_of_unity_proof":"Q(i) roots unity only ±1,±i; both displayed components nonzero",
         "radix_error_global_constant_per_h":"(2+165*abs(h)/56)/N",
         "source_tail_sum_upper":"15/32",
         "h_certificates":vals,
         "original_radix_circle_prefix":[str(x) for x in m.rational_orbit(10)],
         "source_axis_depth3_midpoint":str(sum(m.rotated_axis_bracket(3),F(0))/2),
         "source_axis_depth3_width":str(m.axis_midpoint_error(3)*2),
         "selected_green_sine_transport_constant":"11*abs(h)/(56*N) using inherited sum T_n<1/32"}
    (HERE/'FINITE_RECEIPT.json').write_text(json.dumps(rec,indent=2)+"\n")
    print('ARCTAN_EXACT_RECEIPT_PASS',len(vals),'harmonics, exact signed coefficient & denominator certificates')
    return rec

if __name__=='__main__':run()
