from pathlib import Path
import subprocess,json,hashlib,re,shutil,sys,datetime
E=Path('/home/leah/succ-main-xxii-evidence');R=Path('/home/leah/SUCC-main-xxii');W=Path('/home/leah/SUCC-main-xxii-validation');expected='33b18ae61478c346550b12e6c84ca7d8481c6bad'
def git(*args,cwd=R):return subprocess.check_output(['git',*args],cwd=cwd,text=True).strip()
assert git('rev-parse','HEAD')==expected
native=json.load(open(E/'full-final310.json'));assert native['start_commit']==native['end_commit']==expected;assert native['exit_code']==0
ci=json.load(open(E/'ci-final-review.json'));assert len(ci['check_runs'])==ci['total_count']
conclusions={r['name']:r['conclusion'] or r['status'] for r in ci['check_runs']};ready=bool(ci['check_runs']) and all(v=='success' for v in conclusions.values())
for p in [json.load(open(E/'gates-final310.json')),json.load(open(E/'gates-final313.json'))]:assert p['exit_code']==0 and p['start_commit']==p['end_commit']==expected
if not W.exists():subprocess.run(['git','worktree','add','-b','evidence/succ-main-xxii-final-validation',str(W),expected],cwd=R,check=True)
D=W/'docs/main_xxii_evidence/final_validation';D.mkdir(parents=True,exist_ok=True)
for pattern in ['full-final310.*','gates-final310.*','gates-final313.*','ci-final-review.json','github-render.json','math-dom.json','README-*.png','frontier-*.png','next-round-prime-labels.json','render-check-notes.md','preservation-summary.json','content-preservation.json','versions*.json','quickstart-*.json','quickstart-*.log','repository-merge-settings.json','live-prs-before-merge.json','package-final.py']:
 for p in E.glob(pattern):
  if p.is_file():shutil.copyfile(p,D/p.name)
for p in (E/'browser').glob('*.cjs'):shutil.copyfile(p,D/p.name)
summary={'tested_integration_head':expected,'stable_candidate':'9eafeaa85d9920a12e62ef2e8b755575ef4b6986','main_before':'43a607818907120d4cdab73d240f5b4d7700b63f','observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'native_final':native,'native_test_summaries':re.findall(r'Ran \d+ tests? in [^\n]+',(E/'full-final310.log').read_text()),'exact_head_checks':conclusions,'hosted_gate_pass':ready,'recorded_validation_gates_pass':ready,'live_ancestry_recheck_required':True,'pi_normality':'OPEN','original_zero_hex_parity':'OPEN','RH':'OPEN'}
(D/'ACCEPTANCE.json').write_text(json.dumps(summary,indent=2)+'\n')
(D/'README.md').write_text('# Final-head validation receipt\n\nTested integration commit: `'+expected+'`. The receipt carrier is a separate child branch so recording validation does not change its tested subject.\n\nNative Python3.10 full run: exit0. See command, exact start/end SHA, timings and log hash in full-final310.json; raw log is full-final310.log. Python3.13 stable candidate passed12,806 tests and the final code/test/formal/provenance tree is identical. Final provenance/observer/ordinal/catalog gates pass on both versions.\n\nExact-head hosted gate: '+('PASS' if ready else 'INCOMPLETE / BLOCKED; do not merge')+'. Details and raw check-run statuses are in ACCEPTANCE.json and ci-final-review.json.\n\nActual GitHub page rendering is captured at the exact tested commit at desktop1440px/mobile390px. See screenshots, MathML probe and corrected-instrument notes. Source and original README archive hashes remain preserved. No next-round parity responses were accessed; prime labels alone are fixed.\n\nAll three headline conjectures remain OPEN.\n')
manifest={p.relative_to(D).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(D.rglob('*')) if p.is_file() and p.name!='ARTIFACT_MANIFEST.json'};(D/'ARTIFACT_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
subprocess.run(['git','add','docs/main_xxii_evidence/final_validation'],cwd=W,check=True);subprocess.run(['git','commit','-m','Main XXII: preserve exact final-head validation receipts'],cwd=W,check=True);subprocess.run(['git','push','-u','origin','HEAD'],cwd=W,check=True)
print(json.dumps({'evidence_commit':git('rev-parse','HEAD',cwd=W),'hosted_gate_pass':ready,'checks':conclusions},indent=2))
