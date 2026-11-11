"""Generate a compact exact Fraction receipt from tested source logic.

This is reproducibility metadata, not a mathematical proof kernel.
"""
import json
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal, localcontext
import zero_anchor as z


def exact(q):
    if type(q) is not Q:
        raise TypeError('Fraction required for exact receipt')
    return str(q)


def decimal_display(q, digits=24):
    with localcontext() as ctx:
        ctx.prec=digits+8
        return format(Decimal(q.numerator)/Decimal(q.denominator),f'.{digits}g')


def main():
    root=z.certify_root(Q(1,16**16),max_depth=100)
    hex_digits=z.exact_hex_prefix(24)
    records=[]
    for M in (4,8,16,32):
        v=z.signed_overlap_receipt(M)
        records.append({
            'half_window':M,
            'exact_signed_overlap':exact(v.overlap),
            'exact_absolute_error_bound':exact(v.overlap_error),
            'exact_lower':exact(v.certified_lower),
            'exact_upper':exact(v.certified_upper),
            'overlap_decimal_display_only':decimal_display(v.overlap),
            'error_decimal_display_only':decimal_display(v.overlap_error),
            'max_source_depth':max(v.midpoint_depths),
            'verified_identity':v.entire==(v.early+v.late)/2-v.overlap,
        })
    output={
        'schema':'succ.zero-anchored-dedekind-fingerprint.v1',
        'origin':'exact symbolic seed pair (0,0)',
        'source_contract':'4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2); U0=0',
        'source_value':'x=pi/16 via imported classical BBP evaluation',
        'logical_dependencies':['original forcing identity and positivity','classical BBP pi evaluation',
            'classical Euclidean circumference definition','pi irrationality for Q+Qx normal forms'],
        'root':{
            'depth':root['depth'],
            'bbp_open_interval':[exact(root['bbp'].lo),exact(root['bbp'].hi)],
            'circle_open_interval':[exact(root['geometry'].lo),exact(root['geometry'].hi)],
            'common_open_interval':[exact(root['intersection'].lo),exact(root['intersection'].hi)],
            'common_width':exact(root['intersection'].width),
        },
        'hexadecimal_pi_over_16_first24':''.join('0123456789ABCDEF'[d] for d in hex_digits),
        'seed_tests':{
            'selected':{'const':'0','coeff_of_x':'0','recovered_at_clock_13':str(z.recovered_seed(13,z.state(13,z.ZERO)))},
            'coherent_wrong':{'const':'0','coeff_of_x':'-1','completed_clock_13':str(z.complete(13,z.COHERENT_WRONG)),'passes_zero_anchor':False},
            'rational_alias':{'const':'1/16','coeff_of_x':'0','first_alias_clock':z.eventual_phase_alias(z.ZERO,z.RATIONAL_ALIAS),'passes_zero_anchor':False},
        },
        'finite_fourier_rational_error_budgets':{
            'weyl_N64_h8_depth67':exact(z.weyl_budget(64,8,67)),
            'epoch_A31_h8_depth65':exact(z.epoch_weyl_budget(31,8,65)),
            'ratio_fiber_A31_h8_depth65':exact(z.ratio_fiber_budget(31,8,65)),
            'raw_source_completion_N64_h8':exact(z.source_completion_budget(64,8)),
        },
        'signed_overlap_certificates':records,
        'claim':'All values are finite exact-rational source-selected receipts; no signed decay or normality proof.',
    }
    dest=Path(__file__).with_name('finite_receipt.json')
    dest.write_text(json.dumps(output,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'root_stage':root['depth'],'prefix':output['hexadecimal_pi_over_16_first24'],
                      'signed_half_windows':[t['half_window'] for t in records],
                      'output':dest.name},sort_keys=True))


if __name__=='__main__':main()
