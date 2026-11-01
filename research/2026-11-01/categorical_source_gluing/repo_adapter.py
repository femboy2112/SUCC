"""Optional adapter into SUCC's EXISTING path category; no competing category core.

Run inside a complete pinned SUCC checkout. This file intentionally imports the
canonical classes instead of copying or replacing them. The finite-field carrier
is a categorical control, not an Archimedean BBP phase carrier.
"""
import importlib.util
from pathlib import Path
import sys

def _research_module():
    name='succ_categorical_gluing_adapter_payload_v1'
    if name not in sys.modules:
        spec=importlib.util.spec_from_file_location(name,Path(__file__).with_name('source_gluing.py'))
        module=importlib.util.module_from_spec(spec)
        sys.modules[name]=module
        spec.loader.exec_module(module)
    return sys.modules[name]

def build_existing_path_category(p: int = 7, horizon: int = 2):
    from observational_succ.noncommuting_proof_transport import FiniteCarrier, Instrument
    from observational_succ.operational_yoneda_descent import BeliefGame, ObservationPathCategory
    m=_research_module()
    q=m.projective_cover_table(p);S=m.successor_table(p);ids=tuple(range(p+1))
    enabled=(True,)*(p+1)
    actions=(Instrument('observe-cover',q,ids,enabled),
             Instrument('source-successor',tuple(q[S[x]] for x in ids),S,enabled))
    field=FiniteCarrier(p+1,actions,f'original-R-projective-F{p}-CONTROL',f'P1-F{p}-with-infinity')
    game=BeliefGame.build(field,ids,tuple(f'source:{x}' for x in ids),
                         target_id=f'original-projective-source-point-F{p}')
    return ObservationPathCategory(game,horizon,max_objects=512,max_paths=100000)
