#!/usr/bin/env python3
"""Audit integration guards using explicit synthetic fixtures, plus real D queries.

Fixtures test verifier reconciliation and process-status classification only.
They are not substituted mathematical experiments or fake compiler executions.
Production files/archives are read only. The output records snapshot hashes.
"""
from __future__ import annotations
import argparse
import ast
from copy import deepcopy
from fnmatch import fnmatchcase
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import re
from types import SimpleNamespace
import sys
import tempfile

DEFAULT_ROOT=Path(__file__).resolve().parents[1]


def load_function(source,name):
    tree=ast.parse(source)
    nodes=[n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name==name]
    assert len(nodes)==1,name
    return nodes[0]


def isolated_exec(node,scope):
    code=ast.fix_missing_locations(ast.Module(body=[node],type_ignores=[]))
    exec(compile(code,'<copied-verifier-guard>','exec'),scope)


def rejected(call):
    try: call()
    except AssertionError: return True
    return False


def report(root):
    research=root/'research/2026-10-13'
    aggregate=(root/'scripts/cambrian_campaign_verify.py').read_text()
    portable=(root/'scripts/cambrian_formal_ci.py').read_text()
    manifest=json.loads((research/'CAMBRIAN_SWARM_MANIFEST.json').read_text())
    workflow=(root/'.github/workflows/cambrian.yml').read_text()
    campaign=(root/'docs/CAMBRIAN_CAMPAIGN_2026-10-13.md').read_text()

    # Verbatim current replay guard, using explicitly synthetic subprocess stdout.
    # Actual mathematical implementations are not run in these guard fixtures.
    replay_node=load_function(aggregate,'replay')
    def replay_fixture(filename,changes,runtime_fields=()):
        payload=json.loads((research/filename).read_text())
        payload.update(changes)
        scope={'ROOT':root,'RESEARCH':research,'sys':sys,'json':json,
               'subprocess':SimpleNamespace(run=lambda *a,**k:SimpleNamespace(stdout=json.dumps(payload)))}
        isolated_exec(replay_node,scope)
        return scope['replay']('synthetic-guard-fixture.py',filename,runtime_fields)
    guard_controls={
      'matching_D_receipt_accepted':not rejected(lambda:replay_fixture('CAMBRIAN_D_RESULTS.json',{})),
      'D_source_hash_mutation_rejected':rejected(lambda:replay_fixture('CAMBRIAN_D_RESULTS.json',{'implementation_sha256':'0'*64})),
      'D_proof_status_mutation_rejected':rejected(lambda:replay_fixture('CAMBRIAN_D_RESULTS.json',{'formal_lean_verified':True})),
      'declared_python_only_change_accepted':not rejected(lambda:replay_fixture('CAMBRIAN_D_RESULTS.json',{'python':'3.13.0'},('python',))),
      'E_current_head_only_change_accepted':not rejected(lambda:replay_fixture('CAMBRIAN_E_ARITHMETIC_RECEIPT.json',{'execution_head_sha':'synthetic-other-checkout'},('execution_head_sha',))),
    }
    # Verbatim actual basename reconciliation branch, after the H-requested repair.
    tree=ast.parse(aggregate)
    branch=next(n for n in ast.walk(tree) if isinstance(n,ast.If) and
                ast.unparse(n.test)=="letter == 'A'")
    archived=json.loads((research/'CAMBRIAN_AUDIT_A_RECEIPT.json').read_text())['source_sha256']
    relocated={str(Path('/relocated')/Path(k).name):v for k,v in archived.items()}
    def normalize_fixture(actual_map):
        scope={'letter':'A','actual':{'source_sha256':deepcopy(actual_map)},
               'expected':{'source_sha256':deepcopy(archived)},'runtime':{},'Path':Path}
        isolated_exec(branch,scope)
        assert scope['actual']==scope['expected']
    first_name=Path(next(iter(archived))).name
    collision={str(Path('/different')/first_name):'0'*64,**relocated}
    legacy=lambda d:{Path(k).name:v for k,v in d.items()}
    basename_controls={
      'legitimate_relocation_accepted':not rejected(lambda:normalize_fixture(relocated)),
      'legacy_normalization_loses_bad_hash':legacy(collision)==legacy(archived),
      'current_collision_guard_rejects':rejected(lambda:normalize_fixture(collision)),
    }

    # Verbatim current portable compiler status guard. These are PROCESS FIXTURES,
    # not observed compiler outcomes. Actual local compiler audit is separate.
    check_node=load_function(portable,'check')
    def process_fixture(returncode,stdout):
        with tempfile.TemporaryDirectory(prefix='succ-audit-h-guard-') as tmp:
            scope={'Path':Path,'temporary':tmp,'args':SimpleNamespace(lean='synthetic-process-fixture'),
                   'ROOT':root,'subprocess':SimpleNamespace(run=lambda *a,**k:
                     SimpleNamespace(returncode=returncode,stdout=stdout,stderr='')),
                   'axiom_rows':lambda _: {},'ALLOWED':{'propext','Classical.choice','Quot.sound'},
                   'results':[]}
            isolated_exec(check_node,scope)
            scope['check']('fixture.lean','-- synthetic fixture only',False)
    process_controls={
      'elaboration_error_rc1_accepted_as_rejection':not rejected(lambda:process_fixture(1,'error: type mismatch')),
      'crash_rc_minus11_rejected':rejected(lambda:process_fixture(-11,'segmentation fault')),
      'other_failure_rc2_rejected':rejected(lambda:process_fixture(2,'error: infrastructure unavailable')),
      'rc1_without_error_diagnostic_rejected':rejected(lambda:process_fixture(1,'worker stopped')),
      'rc0_false_control_rejected':rejected(lambda:process_fixture(0,'')),
    }

    paths=re.findall(r"^\s+- '([^']+)'",workflow,re.M)
    ci_controls={
      'lowercase_F_receipt_triggers':any(fnmatchcase('research/2026-10-13/cambrian_f_results.json',p) for p in paths),
      'uppercase_receipts_trigger':any(fnmatchcase('research/2026-10-13/CAMBRIAN_C_RECEIPT.json',p) for p in paths),
      'campaign_branch_push_triggers':any(fnmatchcase('research/cambrian-integration-2026-10-13',p) for p in paths),
      'both_declared_python_versions':all(v in workflow for v in ('3.10','3.13')),
      'all_prefix_depth_gate_visible_in_graph':'EVERY finite prefix' in campaign,
    }
    stored_hashes=[]
    for filename,field in [('CAMBRIAN_A_VALIDATION.json','sha256'),
                           ('CAMBRIAN_C_ASSIGNMENTS.json','artifact_hashes_sha256')]:
        contract=json.loads((research/filename).read_text())[field]
        stored_hashes.append({'contract':filename,'entries':len(contract),
            'all_current_bytes_match':all(sha256((root/p).read_bytes()).hexdigest()==h for p,h in contract.items())})

    # Actual learner execution on a VALID finite unary Moore source.
    # One equivalence round does not mean one membership query or one source tick.
    sys.path.insert(0,str(root))
    from observational_succ.cambrian_d_computation import learn_history_memory, declared_history_teacher
    from observational_succ.eodcs_multi_action_source import ActionSource
    n=65
    states=tuple(str(i) for i in range(n))
    source=ActionSource('audit-H-finite-budget',0,'declared-counter',states,states,
                       ('advance',),(tuple(str(min(i+1,n-1)) for i in range(n)),))
    membership,equivalence=declared_history_teacher(source,'0')
    actual_words=[]; equivalent_calls=[]
    def counted_membership(word):
        actual_words.append(word)
        return membership(word)
    def counted_equivalence(model):
        equivalent_calls.append(len(model.outputs))
        return equivalence(model)
    model,learning=learn_history_memory(source.actions,counted_membership,counted_equivalence,max_rounds=1)
    assert model is not None and learning['status']=='EXACT_TEACHER_CERTIFIED'
    assert len(equivalent_calls)==1 and len(actual_words)>1
    source_ticks=sum(len(w) for w in actual_words)
    learner_control={'finite_source_states':n,'outer_equivalence_round_budget':1,
         'actual_equivalence_calls':len(equivalent_calls),'actual_membership_queries':len(actual_words),
         'sequential_source_ticks_with_reset_queries':source_ticks,
         'max_requested_word_length':max(map(len,actual_words)),
         'reconstructed_states':len(model.outputs),
         'scope':'Actual finite-source run. Source simulator and exact teacher privileged; max_rounds is not a query/time/memory cap.'}

    audited_paths=['docs/CAMBRIAN_CAMPAIGN_2026-10-13.md','docs/CLAIM_LEDGER.md',
       'scripts/cambrian_campaign_verify.py','scripts/cambrian_formal_ci.py',
       '.github/workflows/cambrian.yml','.github/workflows/eodcs-lean.yml',
       'research/2026-10-13/CAMBRIAN_SWARM_MANIFEST.json',
       'research/2026-10-13/CAMBRIAN_REVIEWED_CORRECTIONS.json']
    controls=list(guard_controls.values())+list(basename_controls.values())+list(process_controls.values())+list(ci_controls.values())
    assert all(controls) and all(x['all_current_bytes_match'] for x in stored_hashes)
    return {'schema':'cambrian_audit_h_v1','status':'DESIGN_CONTROLS_PASS_WITH_PUBLICATION_GATES',
       'base_commit':'fa6ebb12a8ab9f016aae59b43535fff145a9862e',
       'snapshot_hashes':{p:sha256((root/p).read_bytes()).hexdigest() for p in audited_paths},
       'verifier_guard_fixtures':guard_controls,'basename_guard_fixtures':basename_controls,
       'compiler_process_guard_fixtures':process_controls,'workflow_and_graph_checks':ci_controls,
       'stored_source_hash_checks':stored_hashes,'actual_D_resource_control':learner_control,
       'swarm':{'workers':manifest['actual_research_workers'],
          'explorations':len(manifest['explorations']),'audits':len(manifest['audits']),
          'exploration_ids_complete':sorted(a['id'] for a in manifest['explorations'])==list(range(1,37)),
          'audit_statuses_at_snapshot':{a['id']:a['execution_status'] for a in manifest['audits']}},
       'publication_gates':['Commit/integrate audit H then mark its manifest row executed',
          'Rerun aggregate verifier on committed integration head',
          'Report actual exact-head GitHub statuses after publication, separately from local checks'],
       'not_reviewing_own_F_mathematical_correctness':True,
       'synthetic_fixtures_are_not_mathematical_or_compiler_runs':True}


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--repo',type=Path,default=DEFAULT_ROOT)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    result=report(args.repo.resolve())
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(text)
        print(json.dumps({'status':result['status'],'learner_control':result['actual_D_resource_control']},sort_keys=True))
    else: print(text,end='')
