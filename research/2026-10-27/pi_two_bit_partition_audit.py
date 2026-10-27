#!/usr/bin/env python3
"""Read git blobs; audit the sibling in an isolated scratch namespace."""
from pathlib import Path
import subprocess, hashlib, json, os, sys, argparse
from fractions import Fraction
from collections import defaultdict, Counter
import importlib.util

REPO=Path(__file__).resolve().parents[2]
OUT=None
COMMIT='91d908b775241df6a7f91e9de843c88e6774e0c9'
FILES=[
 'research/2026-10-27/BBP_TWO_BIT_SHEET_VALUE_MACHINE.md',
 'handoffs/CLAUDE_CODEX_TWO_BIT_GAUSSIAN_BRANCH_2026-10-27.md',
 'scripts/bbp_two_bit_sheet_probe.py',
 'tests/test_bbp_two_bit_sheet_probe.py',
]

def run():
    OUT.mkdir(parents=True,exist_ok=True)
    sources=[]
    for name in FILES:
        spec=f'{COMMIT}:{name}'
        data=subprocess.check_output(['git','show',spec],cwd=REPO)
        dest=OUT/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
        blob=subprocess.check_output(['git','rev-parse',spec],cwd=REPO,text=True).strip()
        sources.append(dict(path=name,git_blob=blob,sha256=hashlib.sha256(data).hexdigest(),bytes=len(data)))
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
    commands=[
      ('source_probe',[sys.executable,'scripts/bbp_two_bit_sheet_probe.py']),
      ('unchanged_tests',[sys.executable,'-m','unittest','discover','-s','tests','-p','test_bbp_two_bit_sheet_probe.py','-v']),
    ]
    command_results=[]
    for label,cmd in commands:
        result=subprocess.run(cmd,cwd=OUT,env=env,text=True,capture_output=True)
        (OUT/f'{label}.stdout.log').write_text(result.stdout)
        (OUT/f'{label}.stderr.log').write_text(result.stderr)
        command_results.append(dict(label=label,command=cmd,exit_code=result.returncode,stdout_sha256=hashlib.sha256(result.stdout.encode()).hexdigest(),stderr_sha256=hashlib.sha256(result.stderr.encode()).hexdigest()))
        if result.returncode: raise RuntimeError((label,result.stderr))
    spec=importlib.util.spec_from_file_location('two_bit_sibling',OUT/'scripts/bbp_two_bit_sheet_probe.py')
    mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
    cases=[]
    for p,L in [(7,1),(7,2),(7,3),(7,4),(7,5),(11,1),(11,2),(11,3),(29,1),(29,2),(31,1),(31,2),(241,1),(241,2)]:
        q=p**L;partial=defaultdict(list);without_pole=defaultdict(list);full=set()
        for x in range(q):
            code=mod.encode(x,p,L)
            assert mod.decode(code,p,L)==x
            full.add(code)
            partial[(code.target,code.sheet,code.pole)].append(x)
            without_pole[(code.target,code.sheet)].append(x)
        assert len(full)==q
        assert sorted(sorted(v) for v in partial.values())==sorted(sorted(v) for v in without_pole.values())
        for key,xx in without_pole.items():
            assert len({x%p for x in xx})==1
            assert len({int(mod.D(x)%p==0) for x in xx})==1
        expected_labels=1+(p-1)*sum(p**(L-2*s-1) for s in range((L+1)//2))
        expected_pairs=((L+1)//2)*(p-1)*p**(L-1)+p**(2*(L//2))
        actual_pairs=sum(len(v)**2 for v in partial.values())
        assert len(partial)==expected_labels
        assert actual_pairs==expected_pairs
        expected_sizes=Counter({p**(L//2):1})
        for s in range((L+1)//2):
            expected_sizes[p**s]+=(p-1)*p**(L-2*s-1)
        actual_sizes=Counter(map(len,partial.values()))
        assert actual_sizes==expected_sizes
        # Exact memory/entropy check: logs are represented by rational coefficients.
        coeff = Fraction(0)
        for cell in partial.values():
            assert len({mod.A(x+1)%q for x in cell}) == len(cell)
            size = len(cell); exponent = 0; rest = size
            while rest > 1:
                assert rest % p == 0
                rest //= p; exponent += 1
            coeff += Fraction(size*exponent,q)
        assert coeff == Fraction(1-Fraction(1,p**(L//2)),p-1)
        assert len({(mod.A(x-1)%q,mod.A(x)%q) for x in range(q)}) == q
        b=89*pow(240,-1,q)%q
        cases.append(dict(entropy_log_p_coefficient=str(coeff),adjacent_A_pairs_injective=True,next_A_values_distinct_within_partial_fibers=True,p=p,L=L,q=q,full_codes=len(full),partial_labels=len(partial),partial_pairs=actual_pairs,multiplicity_histogram=dict(sorted(actual_sizes.items())),critical_pole=int(mod.D(b)%p==0)))
    receipt=dict(commit=COMMIT,scope='Exact unchanged sibling focused tests/source probe in isolated scratch; independent partial-partition enumeration; no native full-suite claim',sources=sources,commands=command_results,cases=cases,audit_script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (OUT/'receipt.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(status='PASS',case_count=len(cases),total_residue_states=sum(c['q'] for c in cases),commands=command_results,sources=sources,cases=cases),indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output-dir',type=Path,required=True,
                        help='Isolated directory for unchanged sibling files and receipts')
    OUT=parser.parse_args().output_dir.resolve()
    run()
