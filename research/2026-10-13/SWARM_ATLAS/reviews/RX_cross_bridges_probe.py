"""Fresh exact audit controls. No imports from SUCC implementations."""
from fractions import Fraction as F
from itertools import product
import hashlib
import json
from pathlib import Path


def binary_channels():
    return [((a, 2-a), (b, 2-b)) for a,b in product(range(3), repeat=2)]


def x05():
    # All deterministic binary instruments; T and G have half-integer rows.
    instruments = list(product(list(product(range(2), repeat=2)), repeat=2))
    channels = binary_channels()
    accepted = path_checks = stochastic_t = 0
    for actual, virtual, t, g in product(instruments, instruments, channels, channels):
        if any(g[actual[x][0]][beta]*t[actual[x][1]][yp]
               != 2*sum(t[x][y] for y in range(2) if virtual[y] == (beta,yp))
               for x,beta,yp in product(range(2), repeat=3)):
            continue
        accepted += 1
        stochastic_t += any(1 in row for row in t)
        ax = {(0,0): F(1,3), (1,1): F(2,3)}
        vy = {(o,y): sum(ax.get((o,x),0)*F(t[x][y],2) for x in range(2))
              for o,y in product(range(2), repeat=2)}
        frontier = [(ax,vy)]
        for depth in range(4):
            nxt=[]
            for mu, nu in frontier:
                for o,y in product(range(2), repeat=2):
                    assert nu.get((o,y),0) == sum(mu.get((o,x),0)*F(t[x][y],2) for x in range(2))
                    path_checks += 1
                for o in range(2):
                    assert sum(nu.get((o,y),0) for y in range(2)) == sum(mu.get((o,x),0) for x in range(2))
                if depth == 3:
                    continue
                for beta in range(2):
                    ma, nv = {}, {}
                    for (o,x), mass in mu.items():
                        alpha,xp=actual[x]
                        ma[o,xp]=ma.get((o,xp),0)+mass*F(g[alpha][beta],2)
                    for (o,y), mass in nu.items():
                        b,yp=virtual[y]
                        if b == beta:
                            nv[o,yp]=nv.get((o,yp),0)+mass
                    nxt.append((ma,nv))
            frontier=nxt
    # The availability implication is elementary support transport, checked
    # independently for every channel and every nonempty support and menu.
    guard_checks=0
    for t in channels:
        for support_bits, enabled_bits in product(range(1,4), range(4)):
            support={x for x in range(2) if support_bits>>x&1}
            enabled={y for y in range(2) if enabled_bits>>y&1}
            virtual_support={y for x in support for y in range(2) if t[x][y]}
            robust=virtual_support <= enabled
            each_lift=all(sum(t[x][y] for y in enabled)==2 for x in support)
            assert robust == each_lift
            guard_checks+=1
    return dict(candidate_squares=len(instruments)**2*len(channels)**2,
                accepted=accepted, accepted_with_stochastic_T=stochastic_t,
                exact_path_state_equalities=path_checks, availability_checks=guard_checks)


def x12():
    checked=accepted=rejected_missing_square=0
    # A node is replayed on the original identities; q never relabels originals.
    for enabled, report, update in product(product(range(2),repeat=2),repeat=3):
        for q0 in [(0,0),(0,1)]:
            if any(q0[x]==q0[z] and (enabled[x]!=enabled[z] or
                   (enabled[x] and report[x]!=report[z])) for x,z in product(range(2),repeat=2)):
                continue
            for qnexts in product([(0,0),(0,1)],repeat=2):
                checked+=1
                supports={b:[o for o in range(2) if enabled[o] and report[o]==b] for b in range(2)}
                compatible=True
                for b, originals in supports.items():
                    q1=qnexts[b]
                    compatible &= all(q0[x]!=q0[z] or q1[update[x]]==q1[update[z]]
                                      for x,z in product(originals,repeat=2))
                if not compatible:
                    rejected_missing_square+=1
                    continue
                accepted+=1
                for b, originals in supports.items():
                    q1=qnexts[b]
                    transition={q0[o]:q1[update[o]] for o in originals}
                    compressed_support=[]
                    for o in range(2):
                        representatives=[z for z in range(2) if q0[z]==q0[o]]
                        z=representatives[0]
                        if enabled[z] and report[z]==b:
                            compressed_support.append(o)
                            assert transition[q0[o]]==q1[update[o]]
                    assert compressed_support==originals
    return dict(local_schedules_checked=checked, accepted=accepted,
                rejected_for_missing_cross_stage_square=rejected_missing_square)


def x04():
    cases=accepted=0
    for m in range(1,4):
        words=list(product(range(2),repeat=m))
        for mask in range(1,1<<len(words)):
            language=[w for j,w in enumerate(words) if mask>>j&1]
            successors={w:[v for v in language if w[1:]==v[:-1]] for w in language}
            cases+=1
            if not all(successors.values()):
                continue
            accepted+=1
            emitted=[]
            for w in language:
                current=w; output=[]
                for _ in range(m):
                    output.append(current[0]); current=successors[current][0]
                emitted.append(tuple(output))
            assert set(emitted)==set(language)
            assert len(emitted)==len(set(emitted))
    return dict(nonempty_languages_checked=cases, valid_stationary_languages=accepted)


def partitions(n):
    if n==0:
        yield ()
    else:
        for p in partitions(n-1):
            for new in range(max(p,default=-1)+2):
                yield p+(new,)


def x08():
    tested=stable=affine_checks=0
    for m in range(1,8):
        for p in partitions(m):
            tested+=1
            if not all(p[x]!=p[y] or p[(x+1)%m]==p[(y+1)%m]
                       for x,y in product(range(m),repeat=2)):
                continue
            stable+=1
            period=min(d for d in range(1,m+1) if all(p[x]==p[(x+d)%m] for x in range(m)))
            assert m%period==0
            assert all((p[x]==p[y]) == (x%period==y%period) for x,y in product(range(m),repeat=2))
            for a,b in product(range(m),repeat=2):
                assert all(p[x]!=p[y] or p[(a*x+b)%m]==p[(a*y+b)%m]
                           for x,y in product(range(m),repeat=2))
                affine_checks+=1
    return dict(partitions_checked=tested, successor_stable_partitions=stable,
                affine_stability_checks=affine_checks)


def main():
    result={"scope":"Fresh finite controls, not universal proof or independent academic peer review",
            "X05":x05(),"X12":x12(),"X04":x04(),"X08":x08()}
    result["probe_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == "__main__":
    main()
