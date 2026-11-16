"""Independent source-trace validator, never imports the source or observer.

Verifies trace under revealed OS-random tape and declared program SHA256.
No ability to prove actual OS randomness or external-world source identity.
"""
from __future__ import annotations
from fractions import Fraction
import hashlib
import json
from pathlib import Path


class ReplayError(Exception):
    pass


def audit_observer_feedback(session):
    """Fresh implementation of policy/likelihood/Bayes update, not an import.

    Verifies actions were predictably selected from public evidence, and that
    the observer's forward/retrospective claims agree with the declared J.
    Source RNG quality, physical sensor calibration remain separate.
    """
    probabilities=(Fraction(3,4),Fraction(1,2))
    pairs=[[[Fraction(1,2),Fraction(0)],[Fraction(0),Fraction(1,2)]]
           for _ in probabilities]
    lik=[Fraction(1),Fraction(1)]
    brier=[Fraction(0),Fraction(0)]
    scored=0
    for t,entry in enumerate(session['steps']):
        action=entry['action']
        obs=entry['result']['outcome']
        current_p=(sum(pairs[0][u][0] for u in range(2)),
                   sum(pairs[0][u][1] for u in range(2)))
        selected=('flip' if current_p[1]>=Fraction(1,2) else 'reset') \
            if t>0 and t%5==4 else 'sense'
        if action != selected:
            raise ReplayError('Observer selected an unlicensed or non-predictable action')
        for model,accuracy in enumerate(probabilities):
            predictive=[Fraction(0)]*(1 if action=='flip' else 2)
            pre_total=[sum(pairs[model][u][x] for u in range(2)) for x in range(2)]
            for x,mass in enumerate(pre_total):
                if action=='flip':
                    predictive[0]+=mass
                else:
                    predictive[x]+=mass*accuracy
                    predictive[1-x]+=mass*(1-accuracy)
            reported=entry['predictive_P' if model==0 else 'predictive_Q']
            if [str(x) for x in predictive]!=reported:
                raise ReplayError('Observer predictions differ from actual joint source law')
            if obs not in range(len(predictive)) or predictive[obs]<=0:
                raise ReplayError('Source produced modeled zero-likelihood event')
            z=predictive[obs]
            next_belief=[[Fraction(0)]*2 for _ in range(2)]
            for u in range(2):
                for x in range(2):
                    if action=='flip':
                        next_belief[u][1-x]+=pairs[model][u][x]
                    else:
                        xp=x if action=='sense' else 0
                        prob=accuracy if obs==x else (1-accuracy)
                        next_belief[u][xp]+=pairs[model][u][x]*prob
            pairs[model]=[[v/z for v in row] for row in next_belief]
            initial=[str(sum(row,Fraction(0))) for row in pairs[model]]
            reported_initial=entry['posterior_initial_P' if model==0 else 'posterior_initial_Q']
            if initial!=reported_initial:
                raise ReplayError('Retrospective original-state posterior mismatch')
            lik[model]*=z
            if len(predictive)==2:
                brier[model]+=2*(predictive[1]-Fraction(obs))**2
        if len(entry['predictive_P'])==2:scored+=1
        ratio=lik[0]/lik[1]
        if Fraction(entry['e_value'])!=ratio:
            raise ReplayError('Online likelihood ratio was not an authentic adapted update')
    if Fraction(session['observer_e_value'])!=lik[0]/lik[1]:
        raise ReplayError('Final e-value differs from recorded events')
    if [Fraction(session[k]) for k in ('brier_P_total','brier_Q_total')]!=brier:
        raise ReplayError('Proper-score holdout was not computed from forward forecasts')
    if session['brier_scored_events']!=scored:
        raise ReplayError('Brier observation count mismatch')
    return {"adapted_policy_verified":True,"likelihood_ratio":str(lik[0]/lik[1]),
            "original_posterior_P":[str(sum(r,Fraction(0))) for r in pairs[0]]}


def validate_session(session, source_file:Path):
    public=session['start']
    reveal=session['reveal']
    tape=bytes.fromhex(reveal['tape_hex'])
    if hashlib.sha256(b'SUCC-COMMIT-TAPE-v1|' + reveal['truth'].encode() + b'|' + tape).hexdigest()!=public['commitment']:
        raise ReplayError('Precommitted tape mismatch')
    if public['source_sha256']!=hashlib.sha256(Path(source_file).read_bytes()).hexdigest():
        raise ReplayError('Source binary changed or falsely announced')
    if public['protocol']!='SUCC-COMMIT-TAPE-v1':
        raise ReplayError('Unrecognized protocol')
    if public['actions']!=['flip','reset','sense']:
        raise ReplayError('Unrecognized action menu')
    truth={'P':3,'Q':2}.get(reveal['truth'])
    if truth is None:raise ReplayError('Unrecognized source model')
    records=session['steps']
    if len(records)!=reveal['steps'] or len(records)>=len(tape):
        raise ReplayError('Step count / tape length mismatch')
    state=tape[0]&1
    credit_total=0
    for i,entry in enumerate(records):
        public_r=entry['result']
        act=entry['action']
        if act not in ('sense','flip','reset') or public_r['action']!=act:
            raise ReplayError('Unlicensed or substituted action')
        if public_r['kind']!='result' or public_r['step']!=i:
            raise ReplayError('Malformed record order')
        if type(public_r['internal_elapsed_ns']) is not int or public_r['internal_elapsed_ns']<=0:
            raise ReplayError('Invalid recorded timing')
        if type(entry['client_round_trip_ns']) is not int or entry['client_round_trip_ns']<=0:
            raise ReplayError('Invalid independently measured timing')
        draw=tape[i+1]%4
        if act=='flip':
            expected_out=0
            state=1-state
            credits=1
        else:
            expected_out=state if draw<truth else 1-state
            credits=2 if act=='sense' else 4
            if act=='reset':state=0
        if expected_out!=public_r['outcome'] or credits!=public_r['credits']:
            raise ReplayError('The source transcript is not consistent with committed randomness')
        credit_total+=credits
    if reveal['final_hidden_state']!=state:
        raise ReplayError('State at end of replay disagrees')
    if session['observer_credit_total']!=credit_total:
        raise ReplayError('Observer cost total disagrees with source meter')
    feedback=audit_observer_feedback(session)
    return {"verified":True,"steps":len(records),"final_hidden":state,
            "credit_total":credit_total,"source_model":reveal['truth'],
            "program_sha256":public['source_sha256'],
            "feedback_verified":feedback["adapted_policy_verified"]}


def validate_file(filename,source_file):
    transcript=json.loads(Path(filename).read_text())
    return [validate_session(s,source_file) for s in transcript['sessions']]
