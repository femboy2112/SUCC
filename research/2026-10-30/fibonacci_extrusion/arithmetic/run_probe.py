from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
from fibonacci_arithmetic import *

root=Path(__file__).resolve().parent
configs=[(k,h,'declared') for k in range(7,16) for h in (1,3,7)]
configs += [(16,h,'fresh_holdout') for h in (11,13)]
u=states(fibonacci(17))
rows=[]
for k,h,regime in configs:
    a,b=fibonacci(k),fibonacci(k+1)
    distances=[distance(h*(u[n+1]-u[n])) for n in range(a,b)]
    slip_indices=[a+j for j,t in enumerate(distances) if t>=Q(1,20)]
    coherent_bound=Q(16*abs(h),(8*a+1)**3)
    # Digest exact source-selected rational distances, never floating evidence.
    payload='\n'.join(str(t) for t in distances).encode()
    rows.append(dict(k=k,h=h,regime=regime,start=a,stop_exclusive=b,
        count=len(distances),slips=len(slip_indices),threshold='1/20',
        first_slips=slip_indices[:12],half_prediction=2*len(slip_indices)>len(distances),
        exact_distance_sha256=sha256(payload).hexdigest(),
        coherent_distance_upper=str(coherent_bound),
        coherent_has_no_slips=coherent_bound<Q(1,20)))
    assert rows[-1]['half_prediction'] and rows[-1]['coherent_has_no_slips']

moduli=list(range(2,41))+[239,478,239**2,239**3,257,263]
receipt=dict(created_utc=datetime.now(timezone.utc).isoformat(),
    authority='Exact finite observations and formula checks; no asymptotic density claim',
    modular_rows=[dict(modulus=m,number=len(intertwiners(m))) for m in moduli],
    hensel_roots=[dict(modulus=m,root=x) for m,x in hensel_roots(5)],
    scalar_order_239=scalar_order(16,239),matrix_order_239=matrix_order(239),
    source_defect_n0=str(15*forcing(1)+forcing(2)),source_defect_n0_mod239=198,
    first_239_birth=60,first_239_primary=119,
    selected_windows=rows,
    exact_intertwiner_row='(16t,t); 239t=0',
    edit_counts=[dict(horizon=n,edits=len(snapshot_positions(n)))
                 for n in (1000,10000,100000,1000000)],
    source_code_sha256=sha256((root/'fibonacci_arithmetic.py').read_bytes()).hexdigest())
(root/'probe_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':'PASS','selected_windows':len(rows),
    'finite_slips':sum(x['slips'] for x in rows),'finite_tested':sum(x['count'] for x in rows),
    'all_half_predictions':all(x['half_prediction'] for x in rows),
    'all_coherent_zero_slip_controls':all(x['coherent_has_no_slips'] for x in rows),
    'hensel_second_root':receipt['hensel_roots'][1]},indent=2))
