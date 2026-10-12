"""Finite E/E'' dual-place handshake over one declared rational source class.

Reports are simulator-generated from one rational original source and checked
against finite source fibers. Relay never grants the recipient hidden source
truth, physical sensor provenance or a new machine instruction for free.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from typing import Mapping
from .diagonal_adele_zeta import (DiagonalSourceError,rational,prime,
                                 modulo_padic_integral,bounded_height_injection)

@dataclass(frozen=True)
class PlaceReceipt:
    source_id:str
    version:int
    basis_id:str
    observer:str
    kind:str
    label:str
    precision:int
    data:tuple

@dataclass(frozen=True)
class RationalClaim:
    name:str
    values:Mapping[F,str]

class DualPlaceProof:
    """Actual original source withheld from proof decoding, as in ObsSUCC."""
    def __init__(self,source_id:str,basis_id:str,version:int,height:int,
                 probes:Mapping[int,int]):
        if not source_id or not basis_id or type(version) is not int or version<0:
            raise DiagonalSourceError("Declared source/basis/version required")
        if type(height) is not int or height<1 or height>20:
            raise DiagonalSourceError("Finite proof universe 1<=height<=20")
        bounded_height_injection(height,probes)
        self.source_id,self.basis_id,self.version=source_id,basis_id,version
        self.probes=dict(probes)
        self.height=height
        self.sources=tuple(sorted({F(a,b) for a in range(-height,height+1)
                                   for b in range(1,height+1)
                                   if all(b%p for p in probes)}))

    def _auth(self,receipt:PlaceReceipt)->None:
        if not isinstance(receipt,PlaceReceipt) or (receipt.source_id,
            receipt.version,receipt.basis_id)!=(self.source_id,self.version,self.basis_id):
            raise DiagonalSourceError("Wrong causal source or observer basis")
        if not receipt.observer or receipt.kind not in ('finite','arch'):
            raise DiagonalSourceError("Missing observer or malformed place")
        if receipt.kind=='finite':
            try:p=int(receipt.label)
            except (ValueError,TypeError):raise DiagonalSourceError("Bad finite prime label")
            if p not in self.probes or not prime(p) or receipt.precision!=self.probes[p] or \
                    type(receipt.data) is not tuple or len(receipt.data)!=1 or \
                    type(receipt.data[0]) is not int or not 0<=receipt.data[0]<p**receipt.precision:
                raise DiagonalSourceError("Forged finite clock, precision or residue")
        else:
            if receipt.label!='real-interval' or receipt.precision!=-1 or \
                    len(receipt.data)!=2 or any(type(v) is not F for v in receipt.data) or \
                    receipt.data[0]>receipt.data[1]:
                raise DiagonalSourceError("Malformed exact real interval")

    def finite_observation(self,source:F,p:int,observer:str)->PlaceReceipt:
        """SIMULATOR ONLY: caller supplies hidden true rational for test calibration."""
        source=rational(source)
        if source not in self.sources or p not in self.probes or not observer:
            raise DiagonalSourceError("No declared source/probe/observer")
        k=self.probes[p]
        return PlaceReceipt(self.source_id,self.version,self.basis_id,observer,
                            'finite',str(p),k,(modulo_padic_integral(source,p,k),))

    def real_observation(self,source:F,tolerance:F,observer:str)->PlaceReceipt:
        source=rational(source)
        tol=rational(tolerance)
        if source not in self.sources or tol<0 or not observer:
            raise DiagonalSourceError("No declared source/tolerance/observer")
        return PlaceReceipt(self.source_id,self.version,self.basis_id,observer,
                            'arch','real-interval',-1,(source-tol,source+tol))

    def fiber(self,receipts:tuple[PlaceReceipt,...])->tuple[F,...]:
        for item in receipts:self._auth(item)
        out=[]
        for q in self.sources:
            okay=True
            for r in receipts:
                if r.kind=='finite' and modulo_padic_integral(q,int(r.label),r.precision)!=r.data[0]:
                    okay=False;break
                if r.kind=='arch' and not(r.data[0]<=q<=r.data[1]):
                    okay=False;break
            if okay:out.append(q)
        return tuple(out)

    def conclude(self,receipts:tuple[PlaceReceipt,...],claim:RationalClaim)->dict:
        if not isinstance(claim,RationalClaim) or set(claim.values)!=set(self.sources):
            raise DiagonalSourceError("Original-source target not declared for full field")
        all_consistent=self.fiber(receipts)
        if not all_consistent:
            return {'status':'INCONSISTENT_SOURCE','fiber_size':0,'value':None}
        target={claim.values[q] for q in all_consistent}
        return {'status':'PROVED' if len(target)==1 else 'UNRESOLVED',
                'fiber_size':len(all_consistent),
                'value':next(iter(target)) if len(target)==1 else None,
                'original_source_id':self.source_id,
                'one_epistemic_macro_update':True,
                'external_observation_authentication':False}

    def cross_check(self,finite:tuple[PlaceReceipt,...],real:tuple[PlaceReceipt,...])->dict:
        finite_f=self.fiber(finite)
        real_f=self.fiber(real)
        joint=self.fiber(finite+real)
        return {'finite_only_size':len(finite_f),'arch_only_size':len(real_f),
                'joint_size':len(joint),'intersection_equals_joint':
                tuple(sorted(set(finite_f)&set(real_f)))==joint,
                'joint_consistent':bool(joint),
                'same_source_verified_inside_declared_model':True,
                'physical_source_authenticated':False}
