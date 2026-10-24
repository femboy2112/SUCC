"""Finite exact, source-labelled SUCC/FUCC history and stopped-Pascal laboratory.

Scope: rational labelled Markov histories, arithmetic *sampling clocks*, finite
prime alphabets with independent truncated-geometric terminal occupations,
uniform multiset-order histories, and exact reverse cotransitions. Infinite
prime Gibbs claims are PAPER (Euler product + Borel-Cantelli), not numerical
certificates. No reverse physical time, plasma prime law, RH, or gravity.
"""
from __future__ import annotations

from fractions import Fraction as Q
from itertools import product, permutations
from math import factorial, isqrt, prod


class SourceHistoryError(ValueError):
    """Malformed source labels, clocks, rational rates, or probability models."""


def exact(x):
    if type(x) not in (int, Q):
        raise SourceHistoryError("Exact integers/Fractions only; no floats or bools")
    return Q(x)


def genuine_prime(p):
    if type(p) is not int or p < 2 or any(p % d == 0 for d in range(2, isqrt(p)+1)):
        raise SourceHistoryError("Actual rational prime label required")
    return p


def _validate_timeline(layers, kernels, initial):
    if not isinstance(layers, tuple) or not layers or not isinstance(kernels, tuple) or len(kernels) != len(layers)-1:
        raise SourceHistoryError("One layer per tick and one adjacent kernel per step")
    for layer in layers:
        if not isinstance(layer, tuple) or not layer or len(set(layer)) != len(layer):
            raise SourceHistoryError("Each finite layer must contain distinct hashable states")
    if set(initial) != set(layers[0]) or sum((exact(v) for v in initial.values()), Q()) != 1 or any(exact(v) < 0 for v in initial.values()):
        raise SourceHistoryError("Authenticated normalized initial source required")
    for t, k in enumerate(kernels):
        if set(k) != set(layers[t]):
            raise SourceHistoryError("Missing source row")
        for x, row in k.items():
            if not isinstance(row, tuple) or not row:
                raise SourceHistoryError("Every active row needs labelled channels")
            seen = set()
            for entry in row:
                if not isinstance(entry, tuple) or len(entry) != 3:
                    raise SourceHistoryError("Each channel is (label,target,probability)")
                label, y, rate = entry
                if not isinstance(label, str) or not label or y not in layers[t+1] or (label, y) in seen or exact(rate) < 0:
                    raise SourceHistoryError("Bad source-labelled channel")
                seen.add((label, y))
            if sum((exact(w) for _, _, w in row), Q()) != 1:
                raise SourceHistoryError("Each labelled probability row must sum to 1")


def source_path_law(layers, kernels, initial):
    """Return probability of each complete *ordered* source history, not endpoints.

    Histories are (start_state, (label1,state1), ...). Equal endpoint states
    with distinct labels remain distinct paths. Zero-mass histories omitted.
    """
    _validate_timeline(layers, kernels, initial)
    mass = {(x,): exact(initial[x]) for x in layers[0] if exact(initial[x])}
    for kernel in kernels:
        following = {}
        for path, previous_mass in mass.items():
            for label, y, probability in kernel[path[-1] if len(path)==1 else path[-1][1]]:
                weight = previous_mass * exact(probability)
                if weight:
                    next_path = path + ((label, y),)
                    following[next_path] = following.get(next_path, Q()) + weight
        mass = following
    if sum(mass.values(), Q()) != 1:
        raise ArithmeticError("Original source path mass lost")
    return mass


def interval_law(kernels, start, end, start_state):
    """Exact distribution over histories on [start,end] from a fixed state.

    Returns suffix tuples ((label,target),...). No implicit projected events.
    """
    if type(start) is not int or type(end) is not int or not 0 <= start <= end <= len(kernels):
        raise SourceHistoryError("Invalid chronological interval")
    mass = {(): Q(1)}
    for j in range(start, end):
        following = {}
        for path, w in mass.items():
            x = start_state if not path else path[-1][1]
            if x not in kernels[j]:
                raise SourceHistoryError("Source path exited typed history layer")
            for label, y, rate in kernels[j][x]:
                following[path+((label,y),)] = w*exact(rate)
        mass = following
    return mass


def compose_at_cut(kernels, start, cut, end, start_state):
    """Split/concatenate with all intermediate source events retained."""
    if not start <= cut <= end:
        raise SourceHistoryError("Cuts must be chronological")
    left = interval_law(kernels, start, cut, start_state)
    joined = {}
    for lhs, wl in left.items():
        midpoint = start_state if not lhs else lhs[-1][1]
        for rhs, wr in interval_law(kernels, cut, end, midpoint).items():
            joined[lhs+rhs] = joined.get(lhs+rhs, Q()) + wl*wr
    if joined != interval_law(kernels, start, end, start_state):
        raise ArithmeticError("Source-labelled Chapman-Kolmogorov split failed")
    return joined


def affine_history_square(kernels, clock_n, prime, source_state):
    """Exact common fine history with two DIFFERENT clock-observation receipts.

    Source tick n corresponds to kernel index 0. SUCC then FUCC checks
    n,n+1,p(n+1); FUCC then p successors checks n,pn,...,p(n+1).
    Both are projections of one history, NOT identical observation receipts.
    """
    genuine_prime(prime)
    if type(clock_n) is not int or clock_n < 1:
        raise SourceHistoryError("Positive source clock")
    p, n = prime, clock_n
    end_tick = p*(n+1)
    if len(kernels) != end_tick-n:
        raise SourceHistoryError("Complete fine source events required, no teleportation")
    a = (n, n+1, end_tick)
    b = (n,) + tuple(range(p*n,end_tick+1))
    if a[-1] != b[-1] or b[0] != a[0]:
        raise ArithmeticError("Authentic prime affine braid failed")
    def route(cuts):
        accumulated = {():Q(1)}
        for u,v in zip(cuts,cuts[1:]):
            revised = {}
            for prefix, pw in accumulated.items():
                where = source_state if not prefix else prefix[-1][1]
                for suffix, sw in interval_law(kernels,u-n,v-n,where).items():
                    whole = prefix+suffix
                    revised[whole] = revised.get(whole,Q())+pw*sw
            accumulated=revised
        return accumulated
    A,B=route(a),route(b)
    if A != B:
        raise ArithmeticError("Fine-grained source-history braid mismatch")
    return {"S_then_Vp_clock":a,"Vp_then_Sp_clock":b,
            "fine_source_law":A,"routes_agree_on_source_histories":True,
            "clock_receipts_identical":a==b,"prime":p,
            "physical_prime_growth_derived":False}


def dual_labelled_messages(layers,kernels,initial,success):
    """Forward alpha, future-conditioned beta and true Bayes reverse on labels."""
    _validate_timeline(layers,kernels,initial)
    if set(success) != set(layers[-1]) or any(exact(w) not in (0,1) for w in success.values()):
        raise SourceHistoryError("Exact terminal event indicator required")
    alphas=[{x:exact(initial[x]) for x in layers[0]}]
    for t,k in enumerate(kernels):
        nxt={y:Q() for y in layers[t+1]}
        for x,row in k.items():
            for _,y,rate in row:
                nxt[y]+=alphas[-1][x]*exact(rate)
        alphas.append(nxt)
    betas=[None]*len(layers)
    betas[-1]={x:exact(success[x]) for x in layers[-1]}
    for t in reversed(range(len(kernels))):
        betas[t]={x:sum((exact(rate)*betas[t+1][y]
                            for _,y,rate in kernels[t][x]),Q()) for x in layers[t]}
    cuts=tuple(sum((alphas[t][x]*betas[t][x] for x in layers[t]),Q()) for t in range(len(layers)))
    if len(set(cuts))!=1:
        raise ArithmeticError("Future and past source models disagree")
    reverse=[]; conditioned=[]; flux=[]
    for t,k in enumerate(kernels):
        backwards={y:{} for y in layers[t+1] if alphas[t+1][y]>0}
        forward={x:{} for x in layers[t] if betas[t][x]>0}
        flux_t={}
        for x,row in k.items():
            for label,y,rate in row:
                f=alphas[t][x]*exact(rate)
                flux_t[(x,label,y)]=f
                if alphas[t+1][y]>0:
                    backwards[y][(x,label)]=f/alphas[t+1][y]
                if betas[t][x]>0:
                    forward[x][(label,y)]=exact(rate)*betas[t+1][y]/betas[t][x]
        for row in backwards.values():
            if sum(row.values(),Q())!=1:
                raise ArithmeticError("Bayesian reversal not stochastic on support")
        for row in forward.values():
            if sum(row.values(),Q())!=1:
                raise ArithmeticError("Doob conditioning not stochastic on support")
        reverse.append(backwards);conditioned.append(forward);flux.append(flux_t)
    return {"alpha":tuple(alphas),"beta":tuple(betas),"cut_overlaps":cuts,
            "Z":cuts[0],"reverse":tuple(reverse),"doob":tuple(conditioned),
            "unconditioned_edge_flux":tuple(flux)}


def _occupations(primes, cap):
    return tuple(product(range(cap+1), repeat=len(primes)))


def _falling(a,k):
    if k>a:
        return 0
    return factorial(a)//factorial(a-k)


def _multinomial(alpha):
    return factorial(sum(alpha))//prod(factorial(a) for a in alpha)


def finite_stopped_pascal(primes, beta, cap):
    """Finite exact independent geometric source; order prime factors uniformly.

    Each A_p in [0,cap] has P(A_p=a)=t_p^a/sum_{j=0}^cap t_p^j,
    t_p=p^-beta. Source alphabets P⊂Q are EXACTLY projective under deleting
    Q/P symbols, because full A_p are independent and their order uniform.
    """
    if (type(primes) is not tuple or not primes or len(primes)!=len(set(primes))
            or len(primes)>4 or type(beta) is not int or beta<2
            or type(cap) is not int or not 0<=cap<=4):
        raise SourceHistoryError("Small exact unique-prime tuple, integer beta>=2, cap 0..4")
    for p in primes:genuine_prime(p)
    t=tuple(Q(1,p**beta) for p in primes)
    z=tuple(sum((v**j for j in range(cap+1)),Q()) for v in t)
    alpha_all=_occupations(primes,cap)
    terminal={a:prod(t[i]**a[i]/z[i] for i in range(len(primes))) for a in alpha_all}
    # q(a) is probability of one exact STOPPED word with occupation a.
    stopped={a:terminal[a]/_multinomial(a) for a in alpha_all}
    # m(a) is probability of any specific ordered prefix with occupation a.
    prefix={}
    for a in alpha_all:
        k=sum(a)
        prob=Q()
        for v,w in terminal.items():
            if any(v[i]<a[i] for i in range(len(a))):continue
            m=sum(v)
            conditional=Q(1)
            if k:
                numer=prod(_falling(v[i],a[i]) for i in range(len(a)))
                conditional=Q(numer,_falling(m,k))
            prob+=w*conditional
        prefix[a]=prob
    transitions={}
    for a in alpha_all:
        if not prefix[a]:continue
        row={"STOP":stopped[a]/prefix[a]}
        for i,p in enumerate(primes):
            if a[i]<cap:
                b=a[:i]+(a[i]+1,)+a[i+1:]
                row[p]=prefix[b]/prefix[a]
        if sum(row.values(),Q()) !=1:
            raise ArithmeticError("Stopped Pascal source not prefix-consistent")
        transitions[a]=row
    return {"primes":primes,"beta":beta,"cap":cap,"terminal":terminal,
            "stopped_word_mass":stopped,"prefix_word_mass":prefix,
            "transitions":transitions,"origin":(0,)*len(primes),
            "normalizer_per_prime":z}


def word_probability(model, word):
    """Probability of the EXACT ordered prime word followed by STOP."""
    if not isinstance(word,tuple):
        raise SourceHistoryError("Ordered source word required")
    a=model['origin']; mass=Q(1)
    for p in word:
        if p not in model['primes']:
            raise SourceHistoryError("Unknown prime-labelled source event")
        if p not in model['transitions'][a]:
            return Q()
        mass *= model['transitions'][a][p]
        i=model['primes'].index(p)
        a=a[:i]+(a[i]+1,)+a[i+1:]
    return mass*model['transitions'][a]['STOP']


def enumerate_stopped_words(model):
    """Independent direct multinomial oracle, not the transition recursion."""
    words={}
    for alpha, weight in model['terminal'].items():
        letters=tuple(p for p,a in zip(model['primes'],alpha) for _ in range(a))
        different=set(permutations(letters))
        each=weight/len(different)
        for word in different:
            words[word]=each
    if sum(words.values(),Q())!=1:
        raise ArithmeticError("Gibbs source is not normalized")
    return words


def project_word(word, retained_primes):
    return tuple(p for p in word if p in retained_primes)


def project_pascal_words(model, retained_primes):
    if type(retained_primes) is not tuple or not set(retained_primes)<=set(model['primes']):
        raise SourceHistoryError("Projection must select valid source-prime alphabet")
    pushed={}
    for word,w in enumerate_stopped_words(model).items():
        new=project_word(word,retained_primes)
        pushed[new]=pushed.get(new,Q())+w
    return pushed


def pascal_cotransition_identity(model):
    """Test exact killed/absorbing Pascal recursion with last-prime alpha_p/k.

    Unnormalized rank-k SURVIVAL mass is multinomial(alpha)*prefix(alpha).
    Missing mass from rank k-1 equals terminal STOP, not a projectivity bug.
    """
    out={}
    for alpha,m in model['prefix_word_mass'].items():
        k=sum(alpha)
        survive=_multinomial(alpha)*m
        stop=_multinomial(alpha)*model['stopped_word_mass'][alpha]
        successors=Q()
        for i,p in enumerate(model['primes']):
            if alpha[i]>=model['cap']:continue
            b=alpha[:i]+(alpha[i]+1,)+alpha[i+1:]
            next_survive=_multinomial(b)*model['prefix_word_mass'][b]
            successors+=next_survive*Q(alpha[i]+1,k+1)
        out[alpha]=(survive,stop,successors)
        if survive != stop+successors:
            raise ArithmeticError("Backward Pascal with STOP violates projectivity")
    return out


def valuation_edit_lower_bound(k):
    """SUCC at n=2^k removes k prime-2 occupation units, exactly."""
    if type(k) is not int or k<1:
        raise SourceHistoryError("Positive exponent required")
    n=2**k
    before=k
    after=0  # n+1 is odd
    return {"n":n,"successor":n+1,"before_v2":before,
            "after_v2":after,"min_occupation_L1_edits":k,
            "uniform_bounded_prime_edit_S_possible":False}


def conditioned_bidirectional_path_law(layers, kernels, initial, success):
    """Both time orientations reconstruct the SAME conditioned full histories.

    Forward: initial(x0)*prod K_t(x_t,label_t,x_t+1)*1_A(xT)/Z.
    Backward: final_posterior(xT)*prod R_t(x_t+1; x_t,label_t).
    If Z=0, no conditional probability exists; do not invent one.
    """
    receipt=dual_labelled_messages(layers,kernels,initial,success)
    if receipt['Z']==0:
        raise SourceHistoryError("Cannot condition on a zero-probability future event")
    forward={}; backward={}
    all_paths=source_path_law(layers,kernels,initial)
    T=len(kernels)
    for path,weight in all_paths.items():
        terminal=path[-1][1] if T else path[0]
        selected=weight*exact(success[terminal])/receipt['Z']
        if not selected:
            continue
        backward_weight=(receipt['alpha'][-1][terminal]
                         *exact(success[terminal])/receipt['Z'])
        for t in reversed(range(T)):
            x=path[0] if t==0 else path[t][1]
            label,y=path[t+1]
            backward_weight*=receipt['reverse'][t][y].get((x,label),Q())
        forward[path]=selected
        backward[path]=backward_weight
    if forward!=backward or sum(forward.values(),Q())!=1:
        raise ArithmeticError("Forward Doob and backward Bayes histories disagree")
    return {"Z":receipt['Z'],"forward_histories":forward,
            "backward_histories":backward,"cut_overlaps":receipt['cut_overlaps'],
            "past_causal_reversal_proved":False}
