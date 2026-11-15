"""Independent exact finite controls; imports no SUCC production module.

Domains were frozen in ADVERSARY_NOTES.md before this implementation.
Python integers/Fraction only, no numerical tolerance and no random seed.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb, gcd
import json


def r(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def green(base, tape, seed=Q(0)):
    values = [seed]
    for value in tape:
        values.append(base*values[-1]+value)
    return values


def direct_green(base, tape, n):
    return sum((base**(n-j)*tape[j-1] for j in range(1,n+1)), Q(0))


def floor(q):
    return q.numerator // q.denominator


def fractional(q):
    return q-floor(q)


def sigma(a,b):
    return floor(a+b)


def gamma_weight(m,j):
    return Q(comb(j+m-1,j), 2**(j+m))


def rate_weight(m,rate,j):
    return Q(comb(j+m-1,j))*Q(rate)**m/Q(rate+1)**(j+m)


def tail_prefix(n,d):
    return sum((r(n+k)/16**k for k in range(1,d+1)), Q(0))


def add_coefficient(poly, exponent, coefficient):
    poly[exponent] = poly.get(exponent,Q(0))+coefficient


def tail_gamma_polynomial_integral(n,d,m,cutoff):
    # Build R_D directly from its four original polynomial coefficients.
    # This route never calls r() or tail_prefix().
    forcing = {0:Q(4),3:Q(-2),4:Q(-1),5:Q(-1)}
    polynomial = {}
    for k in range(1,d+1):
        for exponent, coefficient in forcing.items():
            for j in range(cutoff+1):
                add_coefficient(polynomial, 8*n+8*(k-1)+exponent+8*j,
                                coefficient*gamma_weight(m,j)/16**k)
    return sum((coefficient/Q(exponent+1)
                for exponent,coefficient in polynomial.items()), Q(0))


def run():
    out = {"arithmetic":"int/Fraction", "random_seed":None,
           "production_imports":False, "mutations_rejected":{}}
    bases = (Q(-3,2),Q(-1,2),Q(0),Q(2,3),Q(1),Q(2),Q(16))
    seeds = (Q(-2,3),Q(0),Q(5,4))
    tapes = (
        tuple(r(j) for j in range(1,18)),
        tuple(Q((-1)**j,j+1) for j in range(1,18)),
        tuple(Q(j*j-3,2*j+1) for j in range(1,18)),
    )
    green_checks = 0
    for b,c,u,v in product(bases,bases,seeds,seeds):
        for tape_index in range(3):
            f,g = tapes[tape_index],tapes[(tape_index+1)%3]
            y,z = green(b,f,u),green(c,g,v)
            forcing = tuple(f[j-1]*z[j]+g[j-1]*y[j]-f[j-1]*g[j-1]
                            for j in range(1,18))
            for n in range(18):
                expected = (b*c)**n*u*v+direct_green(b*c,forcing,n)
                assert y[n]*z[n] == expected
                green_checks += 1
    out["green_product"] = {"bases":list(map(str,bases)),"seeds":list(map(str,seeds)),
                            "tape_pairs":3,"maximum_horizon":17,"checks":green_checks}
    assert 1*1 != 1*1+1*1
    out["mutations_rejected"]["omitted_diagonal_subtraction"] = {"true":"1","false":"2"}
    # Constant input one, base2: Y_1=1,Y_2=3; product at2 is9.
    # Correct forcing is(1,5); wrong product base2 yields7, correct base4 yields9.
    assert direct_green(Q(2),(Q(1),Q(5)),2)==7
    assert direct_green(Q(4),(Q(1),Q(5)),2)==9
    out["mutations_rejected"]["ungraded_product_base"] = {"true":"9","false":"7"}
    assert green(Q(1),(Q(1),),Q(0))[1]*green(Q(1),(Q(0),),Q(1))[1] == 1
    out["mutations_rejected"]["homogeneous_seed_term_only"] = {"true":"1","false":"0"}

    convolution_checks = 0
    for a,b,n in product(range(1,5),range(1,5),range(13)):
        assert sum((gamma_weight(a,j)*gamma_weight(b,n-j) for j in range(n+1)),Q(0))==gamma_weight(a+b,n)
        convolution_checks += 1
    assert gamma_weight(1,1)**2 == Q(1,16)
    assert gamma_weight(2,1) == Q(1,4)
    out["gamma_convolution_checks"] = convolution_checks
    out["mutations_rejected"]["hadamard_equals_cascade"] = {"hadamard":"1/16","cascade":"1/4"}

    circle = (Q(0),Q(1,7),Q(1,2),Q(6,7))
    cocycle_checks = 0
    for a,b,c in product(circle,repeat=3):
        left=sigma(a,b)+sigma(fractional(a+b),c)
        right=sigma(b,c)+sigma(a,fractional(b+c))
        assert left==right==floor(a+b+c)
        cocycle_checks += 1
    multipliers=(-3,-1,0,1,2,16)
    shifts=(Q(-7,3),Q(-1,2),Q(0),Q(2,5),Q(47,15))
    states=(Q(0),Q(1,16),Q(1,2),Q(15,16),Q(256,257))
    affine_checks = 0
    for b,c,a,d,q in product(multipliers,multipliers,shifts,shifts,states):
        first_carry=floor(b*q+a)
        first_state=fractional(b*q+a)
        second_carry=floor(c*first_state+d)
        assert floor(c*b*q+c*a+d)==c*first_carry+second_carry
        for integer_lift in (-3,0,2):
            original=Q(integer_lift)+q
            assert c*(b*original+a)+d == (c*b*integer_lift+c*first_carry+second_carry
                                                       +fractional(c*first_state+d))
        affine_checks += 1
    out["carry"]={"cocycle_checks":cocycle_checks,"affine_cases":affine_checks,
                   "integer_lifts_per_case":3}
    assert floor(Q(3,4)+Q(3,4))==1 and floor(Q(3,4))+floor(Q(3,4))==0
    out["mutations_rejected"]["omitted_carry_seam"]={"true":1,"false":0}
    assert floor(Q(-1,2)) == -1

    orbit=green(Q(16),tuple(r(j) for j in range(1,25)))
    block_checks=0
    for start in range(19):
        for middle in range(start,19):
            for stop in range(middle,19):
                def block(a,b):
                    return sum((Q(16)**(b-j)*r(j) for j in range(a+1,b+1)),Q(0))
                qa,qm=fractional(orbit[start]),fractional(orbit[middle])
                ka=floor(16**(middle-start)*qa+block(start,middle))
                kb=floor(16**(stop-middle)*qm+block(middle,stop))
                assert floor(16**(stop-start)*qa+block(start,stop)) == 16**(stop-middle)*ka+kb
                assert orbit[stop]==16**(stop-start)*orbit[start]+block(start,stop)
                block_checks += 1
    out["original_bbp_block_checks"] = block_checks
    assert orbit[1]==Q(47,15) and floor(orbit[1])==3
    full=fractional(orbit[1]/2)
    dropped=fractional(fractional(orbit[1])/2)
    assert fractional(full-dropped)==Q(1,2)
    out["mutations_rejected"]["authentic_first_state_carry_drop"]={
        "U1":str(orbit[1]),"weighted_full_mod1":str(full),
        "weighted_fraction_only_mod1":str(dropped),"character_ratio":"-1"}

    denominator_checks=0
    fixed_residue_failures=0
    shapes=(1,2,3,5)
    frequencies=(-7,-2,1,3,16)
    residues=(1,2,4,16,256,65536)
    for m,h in product(shapes,frequencies):
        for j in range(41):
            coefficient=h*gamma_weight(m,j)
            denominator=coefficient.denominator
            numerator=abs(h)*comb(j+m-1,j)
            assert denominator==2**(j+m)//gcd(numerator,2**(j+m))
            assert denominator*numerator>=2**(j+m)
            assert (coefficient*denominator).denominator==1
            if denominator>1:
                assert (coefficient*(denominator//2)).denominator!=1
            denominator_checks += 1
        for modulus in residues:
            first=next(j for j in range(81) if (h*gamma_weight(m,j)*modulus).denominator!=1)
            assert (h*gamma_weight(m,first)*modulus).denominator!=1
            fixed_residue_failures += 1
    out["gamma_lift_residues"]={"coefficient_checks":denominator_checks,
        "fixed_residue_counterexamples":fixed_residue_failures,
        "shapes":shapes,"frequencies":frequencies,"residues":residues}

    # Exact phase/average and shared-source witnesses: only +/-1 characters.
    # e(mean(0,1))=-1 while mean(e(0),e(1))=1.
    assert (Q(0)+Q(1))/2==Q(1,2)
    out["mutations_rejected"]["phase_inside_average"]={"phase_of_mean":"-1","mean_of_phases":"1"}
    assert (Q(0)**2+Q(1)**2)/2==Q(1,2)
    assert ((Q(0)+Q(1))/2)**2==Q(1,4)
    out["mutations_rejected"]["shared_source_redrawn"]={"shared":"1/2","redrawn":"1/4"}

    growth_checks=0
    for m,n,j in product(shapes,(1,2,5),(0,1,2,3,7,11)):
        term=gamma_weight(m,j)*orbit[n+j]
        next_term=gamma_weight(m,j+1)*orbit[n+j+1]
        assert term>0 and next_term>8*term
        growth_checks += 1
    out["raw_U_gamma_growth"]={"checks":growth_checks,"every_next_term_exceeds_eight_times_previous":True}
    out["mutations_rejected"]["raw_future_gamma_sum_converges"]={"source":"original zero-seeded BBP","ratio_lower_bound":8}

    tempered_checks=0
    critical_integer_checks=0
    for m,rate in product(shapes,(1,15,16,31)):
        partial=Q(0)
        for cutoff in range(17):
            partial+=rate_weight(m,rate,cutoff)*16**cutoff
            if rate>15:
                total=Q(rate,rate-15)**m
                assert 0<partial<total
                tempered_checks+=1
            if rate==15:
                assert partial==Q(15,16)**m*comb(cutoff+m,cutoff)
                critical_integer_checks+=1
            if rate<15 and cutoff:
                term=rate_weight(m,rate,cutoff)*16**cutoff
                previous=rate_weight(m,rate,cutoff-1)*16**(cutoff-1)
                assert term>=8*previous
    half_coefficient=Q(1)
    half_partial=Q(1)
    cumulative_product=Q(1)
    for j in range(1,257):
        previous=half_coefficient
        half_coefficient*=Q(2*j-1,2*j)
        half_partial+=half_coefficient
        cumulative_product*=1+Q(1,2*j)
        assert 0<half_coefficient<previous
        assert half_partial==cumulative_product
    out["tempering"]={"rates":[1,15,16,31],"positive_geometric_enclosures":tempered_checks,
        "critical_integer_partial_identities":critical_integer_checks,
        "critical_half_shape_partial_identities":256,
        "critical_half_shape_terms_decrease":True}
    out["mutations_rejected"]["critical_terms_to_zero_implies_summability"]={
        "shape":"1/2","rate":15,"exact_partial_sum":"product_(k=1)^M(1+1/(2k))"}

    integral_checks=0
    boundary_checks=0
    for n,d,cutoff,m in product((0,1,2,5,13),(1,3,7),(0,1,4,8),shapes):
        direct=sum((gamma_weight(m,j)*tail_prefix(n+j,d) for j in range(cutoff+1)),Q(0))
        assert direct==tail_gamma_polynomial_integral(n,d,m,cutoff)
        integral_checks += 1
        next_direct=sum((gamma_weight(m,j)*tail_prefix(n+j+1,d) for j in range(cutoff+1)),Q(0))
        forcing=sum((gamma_weight(m,j)*r(n+j+1) for j in range(cutoff+1)),Q(0))
        boundary=sum((gamma_weight(m,j)*r(n+j+d+1) for j in range(cutoff+1)),Q(0))/16**d
        assert 16*direct-next_direct == forcing-boundary
        assert boundary>0 and 16*direct-next_direct != forcing
        boundary_checks += 1
    out["retained_tail"]={"polynomial_integral_checks":integral_checks,"finite_boundary_checks":boundary_checks}
    out["mutations_rejected"]["dropped_finite_Green_boundary"]={"counterexamples":boundary_checks,"sign":"strictly positive omitted term"}
    out["result"]="PASS"
    return out


if __name__=="__main__":
    print(json.dumps(run(),indent=2,sort_keys=True))
