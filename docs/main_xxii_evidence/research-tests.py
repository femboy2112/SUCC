import json,pathlib,subprocess,sys
M=json.load(open('docs/SUCC_MAIN_XXII_INTEGRATION_MANIFEST_2026-11-09.json'))
folders=sorted({str(pathlib.Path(f['path']).parent) for p in M['prs'] for f in p['own_changed_files'] if f['path'].startswith('research/') and '/test_' in f['path'] and f['path'].endswith('.py')})
for folder in folders:
 cmd=[sys.executable,'-m','unittest','discover','-s',folder,'-p','test_*.py','-v'];print('COMMAND',cmd,flush=True);r=subprocess.run(cmd);print('EXIT',r.returncode,flush=True)
 if r.returncode:sys.exit(r.returncode)
print('ALL',len(folders),'RESEARCH TEST DIRECTORIES PASS')
