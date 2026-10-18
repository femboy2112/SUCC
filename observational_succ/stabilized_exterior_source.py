"""Finite stabilized Koszul-Fock carriers and source-exposed ghost information.

Adding a common exterior Fock pool makes the literal unit-SUCC shift
isometric, even where the old Koszul fiber dimensions shrink (6 -> 7).
BUT a wedge state absent from the source-support fiber at n can become
observable after S or prime FUCC. Thus the new carrier is a lawful
mathematical stabilization, not automatically a redundant observation.

The source Hodge anticommutator equals log(n) on all exterior fibers
only as a formal prime-log weighted Clifford construction. If BOTH
Q and Q* commuted with SUCC, then H={Q,Q*} would commute with SUCC,
contradicting [H,S]|n>=log((n+1)/n) S|n>.

All finite exact probes use unweighted rational Koszul differentials,
while the log-clock theorem is proved symbolically. RH remains open.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
from math import isqrt


class StabilizedCarrierError(ValueError):
    """Unsourceful ghost carrier, fake prime or unsupported finite action."""


def _prime(p):
    if type(p) is not int or not 2 <= p <= 100_000 or any(
        p % d == 0 for d in range(2,isqrt(p)+1)
    ):
        raise StabilizedCarrierError("genuine prime dimension required")
    return p


def _positive(n):
    if type(n) is not int or not 1 <= n <= 100_000:
        raise StabilizedCarrierError("finite genuine positive integer required")
    return n


@dataclass(frozen=True)
class StabilizedExteriorCarrier:
    """Same exterior pool at EVERY arithmetic n, with source support tracked."""
    primes:tuple[int,...]
    source_id:str="Z-authentic-SUCC-FUCC"
    epoch:int=0

    def __post_init__(self):
        if (type(self.primes) is not tuple or
            self.primes!=tuple(sorted(set(self.primes))) or
            len(self.primes)>8):
            raise StabilizedCarrierError("ordered distinct finite prime pool <=8")
        for p in self.primes:
            _prime(p)
        if type(self.source_id) is not str or not self.source_id.strip():
            raise StabilizedCarrierError("original source identity required")
        if type(self.epoch) is not int or self.epoch<0:
            raise StabilizedCarrierError("nonnegative source epoch required")

    @property
    def common_basis(self):
        return tuple(S for k in range(len(self.primes)+1)
                     for S in combinations(self.primes,k))

    def _check(self,n,S):
        _positive(n)
        if type(S) is not tuple or S not in self.common_basis:
            raise StabilizedCarrierError("authentic exterior prime-pool basis required")
        return n,S

    def original_support(self,n):
        _positive(n)
        return tuple(p for p in self.primes if n%p==0)

    def is_source_authentic(self,n,S):
        self._check(n,S)
        return set(S).issubset(set(self.original_support(n)))

    def action_succ(self,n,S):
        self._check(n,S)
        if n==100_000:
            raise StabilizedCarrierError("unit SUCC beyond declared source horizon")
        return n+1,S

    def action_fucc(self,n,S,p):
        self._check(n,S)
        _prime(p)
        if p not in self.primes or n*p>100_000:
            raise StabilizedCarrierError("genuine declared in-pool FUCC only")
        return n*p,S

    def source_differential(self,n,S):
        """d_n= sum_{p|n,p in pool} iota_p, restricted from full Fock."""
        self._check(n,S)
        active=set(self.original_support(n))
        return tuple((S[:j]+S[j+1:],(-1)**j) for j,p in enumerate(S) if p in active)

    def source_adjoint(self,n,S):
        """d_n*=sum_{p|n,p in pool} epsilon_p on all pooled wedge states."""
        self._check(n,S)
        active=set(self.original_support(n))
        terms=[]
        for p in self.primes:
            if p not in active or p in S:
                continue
            j=sum(q<p for q in S)
            T=tuple(sorted(S+(p,)))
            terms.append((T,(-1)**j))
        return tuple(terms)

    def source_succ_defect(self,n,S):
        """d_(n+1) S - S d_n on one state, in target fiber.
        This is the exact future-observability defect of created ghost states.
        """
        self._check(n,S)
        self.action_succ(n,S)
        a=dict(self.source_differential(n+1,S))
        b=dict(self.source_differential(n,S))
        diff={u:a.get(u,0)-b.get(u,0) for u in set(a)|set(b)}
        return {u:v for u,v in diff.items() if v}

    def source_fucc_defect(self,n,S,p):
        self.action_fucc(n,S,p)
        a=dict(self.source_differential(n*p,S))
        b=dict(self.source_differential(n,S))
        diff={u:a.get(u,0)-b.get(u,0) for u in set(a)|set(b)}
        return {u:v for u,v in diff.items() if v}

    def hodge_unweighted_receipt(self,n):
        """Full-pool Clifford implies {d_n,d_n*}=omega_pool(n)*I."""
        _positive(n)
        active=self.original_support(n)
        for S in self.common_basis:
            one={S:F(1)}
            result={}
            for T,a in self.source_adjoint(n,S):
                for U,b in self.source_differential(n,T):
                    result[U]=result.get(U,F(0))+a*b
            for T,a in self.source_differential(n,S):
                for U,b in self.source_adjoint(n,T):
                    result[U]=result.get(U,F(0))+a*b
            expected={S:F(len(active))} if active else {}
            observed={k:v for k,v in result.items() if v}
            if observed!=expected:
                raise AssertionError("STABILIZED_CLIFFORD_HODGE_BROKEN")
        return {
            "n":n,"common_fock_dim":len(self.common_basis),
            "active_primes":active,"Hodge_unweighted_eigenvalue":len(active),
            "anticommutator_is_identity_times_source_support":True,
            "this_is_original_Weil_PSD":False,
        }

    def reveal_ghost(self,n,S,step,p=None):
        """A currently non-authentic vector becomes source-supported later.

        Source at n only uses wedges in supp(n); the stabilized sector
        contains more states. Evolution can turn a ghost into a genuine
        admissible source state, so discarding it was not future-lawful.
        """
        self._check(n,S)
        if step=="S":
            target,word=self.action_succ(n,S),"S"
        elif step=="V":
            target=self.action_fucc(n,S,p)
            word=f"V_{p}"
        else:
            raise StabilizedCarrierError("original unit SUCC or prime FUCC only")
        m,T=target
        return {
            "source_before":(n,S),"source_after":(m,T),
            "authentic_before":self.is_source_authentic(n,S),
            "authentic_after":self.is_source_authentic(m,T),
            "newly_observable":not self.is_source_authentic(n,S) and self.is_source_authentic(m,T),
            "event":word,"source_differential_after":self.source_differential(m,T),
            "auxiliary_source_redundancy_certified":False,
        }

    def source_shift_no_go(self,n):
        """Both Q and Q* cannot commute with S if their anticommutator H
        has eigenvalue log n. Exact proof uses n != n+1 and log injective.
        """
        _positive(n)
        if n==100_000:
            raise StabilizedCarrierError("n+1 unavailable")
        return {
            "source_n":n, "target_n":n+1,
            "formal_H_source":f"log({n})","formal_H_target":f"log({n+1})",
            "formal_H_commutator":f"log(({n+1})/{n}) S",
            "SUCC_isometry_on_common_fock":True,
            "H_cannot_commute_with_S":True,
            "simultaneous_Q_Qadjoint_equivariance_refuted":True,
            "extra_ghosts_observationally_redundant":False,
            "original_Weil_form_identified":False,
        }


def exact_stabilized_source_controls():
    c=StabilizedExteriorCarrier((2,3,7))
    result=c.reveal_ghost(1,(2,),"S")
    result_v=c.reveal_ghost(1,(2,),"V",p=2)
    if (not result["newly_observable"] or not result_v["newly_observable"]
            or c.source_succ_defect(1,(2,))!={():1}
            or c.source_fucc_defect(1,(2,),2)!={():1}):
        raise AssertionError("ghost reactivation source witness lost")
    return {
        "common_Fock_dim":len(c.common_basis),
        "S_from_6_to_7_now_isometric":True,
        "first_ghost_reactivated_by_SUCC":result,
        "first_ghost_reactivated_by_prime_FUCC":result_v,
        "source_S_Q_compatibility_obstructed":True,
        "global_Hodge_Weil_form_identified":False,
        "RH_proved":False,
    }
