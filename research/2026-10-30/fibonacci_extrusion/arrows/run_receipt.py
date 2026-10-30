import datetime,hashlib,json,subprocess,sys,time
from pathlib import Path

label=sys.argv[1]
command=sys.argv[2:]
root=Path(__file__).resolve().parent
out=root/'receipts'/f'{label}.log'
meta=root/'receipts'/f'{label}.json'
if out.exists() or meta.exists():
    raise SystemExit('receipt already exists')
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
tic=time.monotonic()
r=subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
out.write_bytes(r.stdout)
meta.write_text(json.dumps({'command':command,'cwd':str(Path.cwd()),'started_utc':start,
    'duration_seconds':time.monotonic()-tic,'returncode':r.returncode,
    'output_sha256':hashlib.sha256(r.stdout).hexdigest()},indent=2)+'\n')
print(r.stdout.decode(),end='')
sys.exit(r.returncode)
