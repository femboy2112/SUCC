"""Rebuild exact Duck/pi sources; emit observations, never self-authenticating authority."""
from __future__ import annotations
import argparse, base64, gzip, hashlib, json, os, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / 'formal/duck_pi'
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}
MODULES = {
    'DuckPrinciple': ('formal', 'ObservationalSUCC.Duck'),
    'DuckObserver': ('formal', 'ObservationalSUCC.Duck.Observer'),
    'BaileyCrandall': ('formal/duck_pi', 'ObservationalSUCC.BaileyCrandall'),
    'BBPIntegral': ('formal/duck_pi', 'DuckPiIntegral'),
    'LogisticFactor': ('formal/duck_pi', 'ObservationalSUCC.DuckPi'),
    'Normality': ('formal/duck_pi', 'ObservationalSUCC.DuckPi'),
    'PiSource': ('formal/duck_pi', 'ObservationalSUCC.DuckPi.Source'),
    'WeylBridge': ('formal/duck_pi', 'ObservationalSUCC.DuckPi'),
}

# Each mutant has a compiling positive counterpart using the same imports and
# proof method. Rejecting a missing import or a parser error is not a pass.
CONTROLS = [
    ('duck_erased_factor', 'DuckObserver',
     'open ObservationalSUCC.Duck\n'
     'example : IsFactor (fun (_ : Unit) (b : Bool) => b) '
     '(fun (_ : Unit) (b : Bool) => b) (fun b => b) := by\n  intro a b\n  rfl\n',
     '(b : Bool) => b)', '(b : Bool) => !b)'),
    ('bbp_sharp_constant', 'BaileyCrandall',
     'open ObservationalSUCC.BaileyCrandall\n'
     'example : forcing 1 ≤ (47/15 : ℝ) := by\n'
     '  norm_num [forcing, numerator, denominator]\n',
     '≤ (47/15 : ℝ)', '≤ (3 : ℝ)'),
    ('bbp_clock', 'BaileyCrandall',
     'open ObservationalSUCC.BaileyCrandall\n'
     'example : forcing 1 ≠ forcing 2 := by\n'
     '  norm_num [forcing, numerator, denominator]\n',
     '1 ≠ forcing', '1 = forcing'),
    ('logistic_coefficient', 'LogisticFactor',
     'open ObservationalSUCC.DuckPi\n'
     'example : logistic (1/2) = (4 : ℝ)*(1/2)*(1-1/2) := by\n'
     '  norm_num [logistic]\n',
     '(4 : ℝ)', '(3 : ℝ)'),
    ('canonical_zero_digit', 'Normality',
     'open ObservationalSUCC.DuckPi\n'
     'example : canonicalBlock 16 1 0 0 = 0 := by\n'
     '  simp [canonicalBlock_zero]\n',
     '0 0 = 0', '0 0 = 1'),
    ('normality_exceptional_orbit', 'Normality',
     'open ObservationalSUCC.DuckPi\n'
     'example : ¬ NormalTo 16 0 := by\n  exact zero_not_normal 16\n',
     '¬ NormalTo', 'NormalTo'),
]

SOURCE_MUTATIONS = [
    ('half_open_cylinder', 'Normality', 'Set.Ico ((a : ℝ) /', 'Set.Icc ((a : ℝ) /'),
    ('word_frequency', 'Normality', '(𝓝 ((b : ℝ) ^ k)⁻¹)', '(𝓝 (1 : ℝ))'),
    ('bbp_source_coefficient', 'BBPIntegral',
     '4/(8*(n:ℝ)+1) - 2/(8*(n:ℝ)+4)', '4/(8*(n:ℝ)+1) - 3/(8*(n:ℝ)+4)'),
    ('haar_normalization', 'WeylBridge',
     'def haarMean (F : CircleTest) : ℂ := ∫ z, F z ∂circleHaar',
     'def haarMean (F : CircleTest) : ℂ := 2 * (∫ z, F z ∂circleHaar)'),
]

def digest(b): return hashlib.sha256(b).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output', type=Path, required=True)
    args=ap.parse_args(); output=args.output.resolve(); output.mkdir(parents=True, exist_ok=True)
    sys.path.insert(0,str(ROOT));sys.path.insert(0,str(ROOT/'scripts'))
    from cambrian_audit_c_lean import uncomment
    paths=[ROOT/'formal'/f'{n}.lean' for n in ['DuckPrinciple','DuckObserver','FutureSafeForgetting']]
    paths += [p for p in PROJECT.rglob('*') if p.is_file() and '.lake' not in p.parts and '__pycache__' not in p.parts and p.suffix in {'.lean','.py','.toml'}]
    paths += [PROJECT/'lean-toolchain',PROJECT/'lake-manifest.json',ROOT/'formal/kernel_audit/ExportCommand.lean',ROOT/'.github/workflows/duck-pi-proof.yml']
    paths += [ROOT/'observational_succ/duck_observer.py']
    hashes={str(p.relative_to(ROOT)):digest(p.read_bytes()) for p in sorted(set(paths))}
    for p in paths:
        if p.suffix=='.lean' and re.search(r'\b(sorry|admit|axiom|unsafe|native_decide)\b',uncomment(p.read_text())):
            raise RuntimeError('Forbidden proof token in '+str(p))
    manifest=json.loads((PROJECT/'lake-manifest.json').read_text())
    pins={p['name']:p['rev'] for p in manifest['packages']}
    assert pins['mathlib']=='4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84'
    for name, rev in pins.items():
        directory=PROJECT/'.lake/packages'/name
        actual=subprocess.check_output(['git','rev-parse','HEAD'],cwd=directory,text=True).strip()
        dirty=subprocess.check_output(['git','status','--porcelain','--untracked-files=no'],cwd=directory,text=True).strip()
        assert actual==rev and not dirty,(name,actual,rev,dirty)
    version=subprocess.check_output(['lean','--version'],text=True).strip()
    assert 'version 4.14.0' in version
    print(version,flush=True)
    commands=[]
    def run(label,cmd,cwd,env=None):
        p=subprocess.run(cmd,cwd=cwd,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (output/(label+'.log')).write_text(p.stdout)
        commands.append({'label':label,'command':cmd,'cwd':str(Path(cwd).relative_to(ROOT)),'exit_code':p.returncode,'log_sha256':digest(p.stdout.encode())})
        print('COMMAND',label,'EXIT',p.returncode,flush=True)
        for line in p.stdout.splitlines():
            if 'SUCC_THEOREM_JSON ' not in line: print(line,flush=True)
        return p
    standalone=output/'standalone';standalone.mkdir(exist_ok=True)
    env={**os.environ,'LEAN_PATH':str(standalone)}
    prerequisite=run('FutureSafeForgetting',['lean','-o',str(standalone/'FutureSafeForgetting.olean'),'FutureSafeForgetting.lean'],ROOT/'formal',env)
    exports={}; successes=[]; failures=[]
    template=(ROOT/'formal/kernel_audit/ExportCommand.lean').read_text()
    for module,(directory,namespace) in MODULES.items():
        cwd=ROOT/directory;source=cwd/(module+'.lean')
        names=[namespace+'.'+n for n in re.findall(r'^(?:@\[[^\]]+\]\s*)?theorem\s+([A-Za-z0-9_]+)',source.read_text(),re.M)]
        if directory=='formal':
            cmd=['lean','-o',str(standalone/(module+'.olean')),source.name]; use_env=env
        else:
            build=cwd/'.lake/build/lib';build.mkdir(parents=True,exist_ok=True)
            cmd=['lake','env','lean','-o',str(build/(module+'.olean')),source.name];use_env=None
        p=run(module+'-build',cmd,cwd,use_env)
        if p.returncode: failures.append(module);continue
        audit=output/(module+'Audit.lean')
        audit.write_text('import '+module+'\n'+template+'\n'+''.join('#check @'+n+'\n#print axioms '+n+'\n#succ_export '+n+'\n' for n in names))
        cmd=(['lean'] if directory=='formal' else ['lake','env','lean'])+[str(audit)]
        p=run(module+'-exports',cmd,cwd,use_env)
        if p.returncode:failures.append(module);continue
        found={}
        for line in p.stdout.splitlines():
            if 'SUCC_THEOREM_JSON ' not in line:continue
            e=json.loads(line.split('SUCC_THEOREM_JSON ',1)[1]);name=e.pop('name')
            assert name in names and name not in found
            assert not (set(e['axioms'])-ALLOWED),(name,e['axioms'])
            e['type_sha256']=digest(e['type_expr'].encode());found[name]=e
            print('KERNEL_EXPORTED',name,e['type_sha256'],e['axioms'],flush=True)
        assert set(found)==set(names),(module,set(names)-set(found))
        exports.update(found);successes.append(module)
    mutations=[]
    for label,module,body,old,new in CONTROLS:
        if module not in successes:
            mutations.append({'name':label,'status':'BLOCKED_BY_POSITIVE_MODULE'});continue
        directory,_=MODULES[module];cwd=ROOT/directory
        prefix=['lean'] if directory=='formal' else ['lake','env','lean']
        use_env=env if directory=='formal' else None
        assert old in body
        pair={}
        for kind,contents in [('positive',body),('mutant',body.replace(old,new,1))]:
            file=output/(label+'_'+kind+'.lean')
            file.write_text('import '+module+'\n'+contents)
            pair[kind]=run(label+'-'+kind,prefix+[str(file)],cwd,use_env)
        positive=pair['positive'];negative=pair['mutant']
        diagnostic=negative.stdout.lower()
        infrastructure=any(word in diagnostic for word in
            ['unknown module','unknown constant','unknown identifier','unexpected token','invalid import'])
        semantic=any(word in diagnostic for word in
            ['unsolved goals','type mismatch','tactic','failed to prove'])
        passed=positive.returncode==0 and negative.returncode!=0 and semantic and not infrastructure
        mutations.append({'name':label,'status':'REJECTED_WITH_POSITIVE_CONTROL' if passed else 'FAILED',
            'positive_exit':positive.returncode,'mutant_exit':negative.returncode,
            'positive_source_sha256':digest(('import '+module+'\n'+body).encode()),
            'mutant_source_sha256':digest(('import '+module+'\n'+body.replace(old,new,1)).encode())})
        if not passed:failures.append('mutation:'+label)
    for label,module,old,new in SOURCE_MUTATIONS:
        if module not in successes:
            mutations.append({'name':label,'status':'BLOCKED_BY_POSITIVE_MODULE'});continue
        directory,_=MODULES[module];cwd=ROOT/directory
        source=(cwd/(module+'.lean')).read_text();assert old in source
        changed=source.replace(old,new,1)
        file=output/(module+'_'+label+'.lean');file.write_text(changed)
        p=run(label+'-source-mutant',['lake','env','lean',str(file)],cwd)
        diagnostic=p.stdout.lower()
        passed=p.returncode!=0 and any(x in diagnostic for x in ['unsolved goals','type mismatch','tactic'])
        passed=passed and not any(x in diagnostic for x in ['unknown module','unknown constant','unknown identifier','unexpected token'])
        mutations.append({'name':label,'status':'REJECTED_WITH_POSITIVE_MODULE' if passed else 'FAILED',
            'positive_module':module,'mutant_exit':p.returncode,'mutant_source_sha256':digest(changed.encode())})
        if not passed:failures.append('mutation:'+label)
    generated=[]
    if 'DuckObserver' in successes:
        from observational_succ.duck_observer import FiniteObserver, distinguish, lean_closed_relation_certificate
        def model(tag,rows,outputs):
            return FiniteObserver(tag,0,'literal-output',tuple(str(i) for i in range(len(outputs))),
                tuple(str(i) for i in range(len(rows))),rows,outputs)
        pairs=[('two_actions',model('left',((1,0,1),(2,1,0)),('a','b','a')),
                model('right',((1,0),(0,1)),('a','b'))),
               ('empty_alphabet',model('left',(),('a',)),model('right',(),('a',)))]
        for label,left,right in pairs:
            body=lean_closed_relation_certificate(left,right,distinguish(left,right,0,0))
            ns='ObservationalSUCC.Duck.Generated.'
            footer='\n'+''.join('#print axioms '+ns+n+'\n#succ_export '+ns+n+'\n'
                for n in ['checked','initial_mem','all_words'])
            file=output/('Generated_'+label+'.lean');file.write_text('import DuckObserver\n'+template+'\n'+body.removeprefix('import DuckObserver\n')+'\n'+footer)
            positive=run('generated-'+label,['lean',str(file)],ROOT/'formal',env)
            found={}
            for line in positive.stdout.splitlines():
                if 'SUCC_THEOREM_JSON ' in line:
                    e=json.loads(line.split('SUCC_THEOREM_JSON ',1)[1]);name=e.pop('name')
                    assert not set(e['axioms'])-ALLOWED
                    e['type_sha256']=digest(e['type_expr'].encode());found[name]=e
            changed=re.sub(r'(?m)^(def observeRight[^\n]*:=).+$',r'\1 fun _ => 99',body)
            assert changed!=body
            mutant=output/('Generated_'+label+'_mutant.lean');mutant.write_text(changed)
            negative=run('generated-'+label+'-mutant',['lean',str(mutant)],ROOT/'formal',env)
            passed=positive.returncode==0 and len(found)==3 and negative.returncode!=0 and 'decide' in negative.stdout
            generated.append({'name':label,'passed':passed,'source_sha256':digest(body.encode()),'compiled_source_sha256':digest(file.read_bytes()),
                'mutant_sha256':digest(changed.encode()),'theorem_exports':found})
            if not passed:failures.append('generated:'+label)
    assert hashes=={p:digest((ROOT/p).read_bytes()) for p in hashes},'source changed during build'
    record={'schema':'succ.duck-pi.kernel-observation.v1','build_succeeded':not failures and prerequisite.returncode==0,'git_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'git_tree':subprocess.check_output(['git','rev-parse','HEAD^{tree}'],cwd=ROOT,text=True).strip(),'lean_version':version,'source_hashes':hashes,'dependency_revisions':pins,'successful_modules':successes,'failed_modules':failures,'commands':commands,'theorem_exports':exports,'authority_admitted':False,'negative_mutations':mutations,'generated_certificates':generated}
    encoded=json.dumps(record,sort_keys=True,separators=(',',':')).encode()
    (output/'kernel-observation.json').write_bytes(encoded+b'\n')
    print('DUCK_PI_RECORD_BASE64 '+base64.b64encode(gzip.compress(encoded)).decode(),flush=True)
    print('KERNEL_RESULT',record['build_succeeded'],'EXPORTS',len(exports),flush=True)
    if not record['build_succeeded']:raise SystemExit(1)

if __name__=='__main__':main()
