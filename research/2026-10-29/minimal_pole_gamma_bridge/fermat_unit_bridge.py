"""Source-adjacent arithmetic mirror U(15) ~= U(16), not a BBP digit dynamics map.

Classical Chinese remainder theorem and 2-adic unit structure. Exact finite tests.
"""
from __future__ import annotations
from math import gcd


def units(modulus:int)->tuple[int,...]:
    if type(modulus) is not int or modulus<2:raise ValueError('modulus>=2')
    return tuple(x for x in range(1,modulus) if gcd(x,modulus)==1)


def totient(modulus:int)->int:return len(units(modulus))


def coordinates15(x:int)->tuple[int,int]:
    if type(x) is not int or gcd(x,15)!=1:raise ValueError('input a unit modulo15')
    x%=15
    e=0 if x%3==1 else 1
    k=next(k for k in range(4) if pow(2,k,5)==x%5)
    return e,k


def unit15_to16(x:int)->int:
    e,k=coordinates15(x)
    return ((-1)**e * pow(5,k,16))%16


def unit16_to15(x:int)->int:
    if type(x) is not int or gcd(x,16)!=1:raise ValueError('input a unit modulo16')
    y=x%16
    for a in units(15):
        if unit15_to16(a)==y:return a
    raise AssertionError('bijection unexpectedly broken')


def powers_of_i(k:int)->tuple[int,int]:
    return ((1,0),(0,1),(-1,0),(0,-1))[k%4]


def character15(u:int,v:int,x:int)->tuple[int,int]:
    if type(u) is not int or u not in (0,1):raise ValueError('u=0/1')
    if type(v) is not int or not 0<=v<4:raise ValueError('v=0..3')
    e,k=coordinates15(x)
    re,im=powers_of_i(v*k)
    sign=(-1)**(u*e)
    return sign*re,sign*im


def finite_multiplicative_orders(modulus:int)->dict[int,int]:
    if modulus not in (15,16,255,256):raise ValueError('only finite certified control groups')
    result={}
    for x in units(modulus):
        value=x%modulus
        power=1
        for k in range(1,modulus+1):
            power=(power*value)%modulus
            if power==1:
                result[x]=k;break
        else: raise AssertionError('finite group order computation failed')
    return result


def fermat_stage(k:int)->tuple[int,int]:
    if type(k) is not int or not 1<=k<=5:raise ValueError('k in [1,5]')
    v=2**(2**k)
    return v-1,v


if __name__=='__main__':
    a=units(15);b=units(16)
    assert len(a)==len(b)==8
    assert set(unit15_to16(x) for x in a)==set(b)
    for x in a:
        for y in a:
            assert unit15_to16((x*y)%15)==unit15_to16(x)*unit15_to16(y)%16
    assert max(finite_multiplicative_orders(255).values())==16
    assert max(finite_multiplicative_orders(256).values())==64
    print('FERMAT_CRT_UNIT_BRIDGE_PASS 64 products; U15=U16; U255!=U256')


def hybrid_basis16():
    """16x16 Gaussian-integer matrix: 8 odd CRT characters + 8 even Walsh.

    A basis-vector entry is (real,imag), with real and imag integers; no
    numerical trigonometric approximations. This is a fixed *single-digit*
    representation, NOT a theorem on any selected digit/carry distribution.
    """
    rows=[]
    for u in (0,1):
        for v in range(4):
            row=[]
            for digit in range(16):
                row.append(character15(u,v,unit16_to15(digit)) if digit%2 else (0,0))
            rows.append(tuple(row))
    for j in range(8):
        row=[]
        for digit in range(16):
            if digit%2: row.append((0,0))
            else:
                k=digit//2
                row.append(((-1)**((j&k).bit_count()%2),0))
        rows.append(tuple(row))
    return tuple(rows)


def gaussian_conj(x):return(x[0],-x[1])


def gaussian_mul(x,y):return(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])


def gaussian_add(x,y):return(x[0]+y[0],x[1]+y[1])


def basis_gram16():
    """Exact Gaussian-integer Gram matrix G[i,j]=sum_d B[i,d]conj(B[j,d])."""
    b=hybrid_basis16()
    return tuple(tuple(sum_gaussian(gaussian_mul(x,gaussian_conj(y))
              for x,y in zip(b[i],b[j])) for j in range(16)) for i in range(16))


def sum_gaussian(values):
    a,b=0,0
    for x,y in values:a+=x;b+=y
    return a,b
