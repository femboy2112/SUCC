#!/usr/bin/env python3
"""Independent Lean 4.14 authority audit; no production/formal source mutations.

Compiler output, hashes, exact calibration sources and authority boundaries are
captured. --compare reruns every compiler/control and compares stable authority
fields; it does not compare temporary-path-dependent diagnostic text bytewise.
"""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

ROOT=Path(__file__).resolve().parents[1]
RUNTIME=Path('/workspace/scratch/6d134115e8ca/lean-runtime')
DEFAULT_COMPILER=RUNTIME/'lean-4.14.0-linux/bin/lean'
DEFAULT_LOCATOR=RUNTIME/'self_exe_locator.so'
ALLOWED={'propext','Classical.choice','Quot.sound'}


def digest(path):
    return sha256(Path(path).read_bytes()).hexdigest()


def uncomment(source):
    """Remove nested Lean comments before keyword/declaration scans."""
    out=[]; i=0; depth=0
    while i<len(source):
        if source.startswith('/-',i):
            depth+=1; i+=2
        elif depth and source.startswith('-/',i):
            depth-=1; i+=2
        elif not depth and source.startswith('--',i):
            end=source.find('\n',i)
            i=len(source) if end<0 else end
        else:
            if not depth: out.append(source[i])
            elif source[i]=='\n': out.append('\n')
            i+=1
    if depth: raise ValueError('unterminated Lean comment')
    return ''.join(out)


def axiom_rows(stdout):
    result={}
    for name,body in re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]",stdout,re.S):
        result[name]=sorted(x.strip() for x in body.replace('\n',' ').split(',') if x.strip())
    for name in re.findall(r"'([^']+)' does not depend on any axioms",stdout):
        result[name]=[]
    return result


def run_audit(compiler,locator):
    env=os.environ.copy()
    env['LD_PRELOAD']=str(locator)
    def compile_source(name,source,expected):
        with tempfile.TemporaryDirectory(prefix='succ-audit-c-') as tmp:
            path=Path(tmp)/name
            path.write_text(source)
            cmd=[str(compiler),str(path)]
            done=subprocess.run(cmd,cwd=ROOT,env=env,text=True,capture_output=True,timeout=60)
            rows=axiom_rows(done.stdout)
            unexpected={n:a for n,a in rows.items() if set(a)-ALLOWED}
            return {'name':name,'source_sha256':sha256(source.encode()).hexdigest(),
                    'returncode':done.returncode,'expected_acceptance':expected,
                    'calibrated':(done.returncode==0)==expected,
                    'command':cmd,'stdout':done.stdout,'stderr':done.stderr,
                    'theorem_axioms':rows,'unexpected_axioms':unexpected}
    version=subprocess.run([str(compiler),'--version'],env=env,text=True,capture_output=True,timeout=15)
    files=sorted((ROOT/'formal').glob('EODCS_*.lean'))
    sources={str(p.relative_to(ROOT)):p.read_text() for p in files}
    scans={}
    jobs=[]
    for path,source in sources.items():
        code=uncomment(source)
        forbidden=sorted(set(re.findall(r'\b(?:sorry|admit|axiom|unsafe|native_decide)\b',code)))
        names=re.findall(r'^\s*theorem\s+([A-Za-z_0-9]+)',code,re.M)
        checks='\n'.join('#check ObservationalSUCC.'+name+'\n#print axioms ObservationalSUCC.'+name
                         for name in names)
        scans[path]={'imports':re.findall(r'^import\s+(.+)$',code,re.M),
                     'forbidden_code_tokens':forbidden,'theorems':names}
        jobs.append((Path(path).name,source+'\n'+checks+'\n',True))
    appendix=ROOT/'research/2026-10-13/CAMBRIAN_AUDIT_C_CONTROLS.lean'
    appendix_code=uncomment(appendix.read_text())
    appendix_theorems=re.findall(r'^\s*theorem\s+([A-Za-z_0-9]+)',appendix_code,re.M)
    appendix_forbidden=sorted(set(re.findall(r'\b(?:sorry|admit|axiom|unsafe|native_decide)\b',appendix_code)))
    appendix_checks='\n'.join('#print axioms CambrianAudit.'+name for name in appendix_theorems)
    appended=sources['formal/EODCS_CambrianRealization.lean']+'\n'+appendix.read_text()+'\n'+appendix_checks+'\n'
    jobs.append(('CAMBRIAN_AUDIT_C_CONTROLS.lean',appended,True))
    failures={
      'false_zero_eq_one.lean':'import Std.Tactic\nexample : (0 : Nat) = 1 := by\n  rfl\n',
      'missing_finite_successor_completeness.lean':appended+r"""
open ObservationalSUCC CambrianAudit
example : ∃ history : Nat → Nat,
    history 0 = 0 ∧ ∀ t, InfiniteRootRelation t (history t) (history (t+1)) := by
  exact cambrian_nondeterministic_history_realization
    InfiniteRootRelation (fun _ _ => [])
    (by intro t s next edge; simpa using edge)
    0 infinite_root_arbitrarily_extendable
""",
      'invalid_finite_to_infinite_quantifier_swap.lean':sources['formal/EODCS_CambrianRealization.lean']+r"""
open ObservationalSUCC
example : ∃ history : Nat → Nat,
    ∀ t, CambrianCountdown t (history t) (history (t+1)) := by
  exact cambrian_countdown_all_finite_depths
""",
      'missing_downward_closure.lean':appended+r"""
open ObservationalSUCC CambrianAudit
example : ∃ x : Bool, x ∈ [true, false] ∧ ∀ d, Alternating d x := by
  exact cambrian_finite_coherent_choice [true, false] Alternating
    (by intro e d x order hx; exact hx)
    alternating_every_depth_has_a_finite_menu_witness
""",
    }
    jobs.extend((name,source,False) for name,source in failures.items())
    with ThreadPoolExecutor(max_workers=3) as pool:
        outputs=list(pool.map(lambda job:compile_source(*job),jobs))
    count=sum(len(x['theorems']) for x in scans.values())
    all_printed=all(len(output['theorem_axioms'])==len(scans['formal/'+output['name']]['theorems'])
                    for output in outputs if 'formal/'+output['name'] in scans)
    passed=(version.returncode==0 and 'version 4.14.0' in version.stdout and
            all(not s['forbidden_code_tokens'] for s in scans.values()) and not appendix_forbidden and
            all(o['calibrated'] and not o['unexpected_axioms'] for o in outputs) and all_printed)
    library=compiler.parent.parent/'lib/lean/libleanshared.so'
    return {
      'schema':'cambrian_audit_c_lean_v1','audited_base':'6fc5ae9f1a92abbab259b37440aefed23ee04e92',
      'target_cluster_commit':'906de6f','status':'PASS_WITH_SCOPE_BOUNDARY' if passed else 'FAIL',
      'compiler_version':version.stdout.strip(),'compiler_version_returncode':version.returncode,
      'compiler_path':str(compiler),'compiler_sha256':digest(compiler),
      'shared_lean_library_sha256':digest(library),
      'locator_path':str(locator),'locator_sha256':digest(locator),
      'locator_source_sha256':digest(locator.with_suffix('.c')),
      'locator_source_content':locator.with_suffix('.c').read_text(),
      'locator_scope':'readlink override only own numeric /proc/pid/exe -> /proc/self/exe; source inspected',
      'formal_source_hashes':{path:digest(ROOT/path) for path in sources},
      'audit_appendix_sha256':digest(appendix),
      'audit_appendix_scan':{'theorems':appendix_theorems,'forbidden_code_tokens':appendix_forbidden},
      'module_count':len(sources),'new_module_count':1,'inherited_module_count':len(sources)-1,
      'theorem_count':count,'all_theorem_axioms_printed':all_printed,'source_scans':scans,
      'compiler_invocations':outputs,
      'rejection_control_sources':failures,
      'proof_scope':{'dependent_state_types':True,'finite_complete_successor_supersets':True,
         'finite_initial_candidate_list':True,'uniform_finite_state_bound_required':False,
         'determinism_or_stationarity_required':False,'topology_kernel_checked':False,
         'effective_branch_selector_checked':False,'physical_infinite_execution_checked':False,
         'source_authentication_checked':False},
      'pr45':{'commit':'b2774ca485db4b5b4f7ce92e535220352fb3af2f',
         'toolchain':'leanprover/lean4:v4.19.0','source_correspondence_read':True,
         'compiled_in_this_audit':False,'imported_into_4_14':False}}


def stable(report):
    return {k:report[k] for k in (
       'status','compiler_version','compiler_sha256','shared_lean_library_sha256','locator_sha256',
       'formal_source_hashes','audit_appendix_sha256','audit_appendix_scan','module_count','theorem_count',
       'all_theorem_axioms_printed','source_scans','proof_scope','pr45')} | {
         'compiler_verdicts':[(r['name'],r['source_sha256'],r['returncode'],
            r['calibrated'],r['theorem_axioms'],r['unexpected_axioms']) for r in report['compiler_invocations']]}


if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--compiler',type=Path,default=DEFAULT_COMPILER)
    p.add_argument('--locator',type=Path,default=DEFAULT_LOCATOR)
    p.add_argument('--output',type=Path)
    p.add_argument('--compare',type=Path)
    args=p.parse_args()
    report=run_audit(args.compiler.resolve(),args.locator.resolve())
    if args.compare and stable(report)!=stable(json.loads(args.compare.read_text())):
        raise SystemExit('Lean authority audit differs from recorded stable fields')
    if args.output:
        args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
        print(json.dumps({k:report[k] for k in ('status','module_count','theorem_count',
                                              'all_theorem_axioms_printed')},sort_keys=True))
    else:
        print(json.dumps(report,indent=2,sort_keys=True))
    if report['status']!='PASS_WITH_SCOPE_BOUNDARY': raise SystemExit(1)
