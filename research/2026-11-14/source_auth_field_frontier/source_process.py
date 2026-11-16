"""Separate actual subprocess source, precommitted tape, no hidden label oracle.

Do not import an observer model here. The source exposes public actions,
public outcomes and charged credits, never X. A 128-byte OS-random tape is
committed before any adaptive action, and revealed only on termination.
A secure hash commitment attests realized replay under crypto assumptions;
it does not certify OS entropy quality or an external physical law.
"""
import argparse
import hashlib
import json
from pathlib import Path
import secrets
import sys
import time

COSTS={"sense":2,"flip":1,"reset":4}


def send(record):
    sys.stdout.write(json.dumps(record,sort_keys=True,separators=(',',':'))+'\n')
    sys.stdout.flush()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--truth',choices=('P','Q'),required=True)
    args=parser.parse_args()
    tape=secrets.token_bytes(128)
    source_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    state=tape[0] & 1
    truth=(3 if args.truth=='P' else 2)
    n=0
    send({"kind":"start","commitment":hashlib.sha256(b'SUCC-COMMIT-TAPE-v1|' + args.truth.encode() + b'|' + tape).hexdigest(),
          "source_sha256":source_hash,"actions":sorted(COSTS),"protocol":"SUCC-COMMIT-TAPE-v1"})
    for raw in sys.stdin:
        try:
            entry=json.loads(raw)
            if not isinstance(entry,dict) or 'kind' not in entry:
                raise ValueError('Malformed message')
            if entry['kind']=='end':
                send({"kind":"reveal","tape_hex":tape.hex(),
                      "truth":args.truth,"steps":n,"final_hidden_state":state})
                return
            if entry['kind']!='action' or entry.get('step')!=n:
                raise ValueError('Invalid step or message kind')
            action=entry.get('action')
            if action not in COSTS:
                raise ValueError('Unlicensed action')
            if n>=len(tape)-1:raise ValueError('Precommitted tape exhausted')
            start=time.perf_counter_ns()
            pre=state
            draw=tape[n+1]%4
            if action=='sense':
                out=pre if draw<truth else 1-pre
            elif action=='reset':
                out=pre if draw<truth else 1-pre
                state=0
            else:
                out=0
                state=1-pre
            n+=1
            elapsed=max(1,time.perf_counter_ns()-start)
            send({"kind":"result","step":n-1,"action":action,"outcome":out,
                  "credits":COSTS[action],"internal_elapsed_ns":elapsed})
        except (ValueError,KeyError,TypeError) as exc:
            send({"kind":"error","message":str(exc)})
            return

if __name__=='__main__':
    main()
