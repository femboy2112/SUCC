"""Read-only two-track research probe; no RH claim."""
import json
from fractions import Fraction as F
from observational_succ.affine_pontryagin_transfer import (
    exact_transfer_relations, history_loss_witness,
)
from observational_succ.source_direct_quotient_gate import CertifiedSourceDirectQuotientTrial


def main():
    relations=exact_transfer_relations(F(1,6),F(1,7),2,3)
    schur=CertifiedSourceDirectQuotientTrial(J_deriv=2,grid=8,J_galerkin=64,rank=5,eta=F(1,4))
    print(json.dumps({
        'arithmetic_relations_exact':{k:v for k,v in relations.items() if isinstance(v,bool)},
        'history_loss':history_loss_witness(2),
        'schur_source_gate':schur.get('source_gate_passed',False),
        'schur_first_window_verdict':schur['verdict'],
        'S4_lower_diagonal':tuple(schur['certified_S4_lower'][i][i] for i in range(4)) if schur.get('source_gate_passed') else None,
        'RH_PROVED':False,
    },default=str,indent=2))


if __name__=='__main__':
    main()
