"""Exact hostile probes for source-authenticated boundary spectral reconstruction."""
import unittest
from fractions import Fraction as F
from itertools import product

from observational_succ.spectral_boundary_rigidity import (
    SpectralSourceError, poly, pa, ps, pm, pd, pgcd,
    rational_response, response_at, chain_jacobi, chain_response,
    chain_moments, round_trip_new_depth, recover_positive_chain,
    interpolate_response, finite_response_identity, recover_operational_jacobi,
    boundary_krylov_top_coefficient, approximate_hidden_mode_pair,
    exact_determinant, boundary_moment_hankel, hankel_depth_certificate,
)
from observational_succ.boundary_realization_selection import (
    FiniteNetwork, boundary_response, matrix_inverse
)


def independent_network(g):
    n=len(g)-1
    if n==0:
        return FiniteNetwork(2,(0,1),((0,1,g[0]),))
    return FiniteNetwork(n+2,(0,n+1),
                         tuple((i,i+1,g[i]) for i in range(n+1)),
                         tuple((i,F(1)) for i in range(1,n+1)))


class ExactSpectralInverseTests(unittest.TestCase):
    def test_exact_polynomial_division_and_gcd_independent_identity(self):
        a=(F(1),F(3),F(3),F(1))
        b=(F(1),F(2),F(1))
        quotient,remainder=pd(a,b)
        self.assertEqual(quotient,(F(1),F(1)))
        self.assertEqual(remainder,(F(),))
        self.assertEqual(pm(b,quotient),a)
        self.assertEqual(pgcd(a,b),b)
        self.assertEqual(rational_response(a,b),((F(1),F(1)),(F(1),)))

    def test_resistor_chain_forward_matches_independent_full_schur(self):
        cases=((F(1,2),),
               (F(1),F(1)),
               (F(1),F(2),F(3)),
               (F(2),F(3),F(5)),
               (F(2),F(3),F(5),F(7)),
               (F(3,2),F(4,3),F(5,2),F(3,5),F(4)))
        for g in cases:
            y=chain_response(g)
            n=independent_network(g)
            for s in (0,1,2,3,5,11):
                with self.subTest(g=g,s=s):
                    self.assertEqual(response_at(y,s),boundary_response(n,s)[0][0])

    def test_rational_inverse_recovers_all_source_edges(self):
        for g in ((1,),(1,1),(1,2,3),(2,3,5),(2,3,5,7),
                  (F(3,2),F(4,3),F(5,2),F(3,5),F(4)),
                  (F(1,11),F(13,17),F(3,7),F(2,5))):
            self.assertEqual(recover_positive_chain(chain_response(g)),tuple(map(F,g)))

    def test_exact_spectral_signature_example_depth2(self):
        y=chain_response((2,3,5))
        self.assertEqual(y,((F(30),F(22),F(2)),(F(31),F(13),F(1))))
        self.assertEqual(response_at(y,0),F(30,31))
        self.assertEqual(response_at(y,1),F(6,5))
        self.assertEqual(recover_positive_chain(y),(F(2),F(3),F(5)))

    def test_known_bound_2d_plus_one_freqs_determine_whole_response(self):
        for g in ((F(1,2),),
                  (F(1),F(1)),
                  (F(2),F(3),F(5)),
                  (F(2),F(3),F(5),F(7)),
                  (F(1,2),F(3,5),F(7,11),F(9,13),F(1,3))):
            for d in (len(g)-1,len(g)):
                y=chain_response(g)
                samples=tuple((s,response_at(y,s)) for s in range(1,2*d+2))
                recovered=interpolate_response(samples,d)
                self.assertEqual(recovered,y)
                self.assertEqual(recover_positive_chain(recovered),tuple(map(F,g)))
                self.assertTrue(finite_response_identity(y,recovered,tuple(range(1,2*d+2)),d))

    def test_fake_lower_degree_prior_rejected_as_out_of_class(self):
        y=chain_response((F(2),F(3),F(5),F(7)))
        samples=tuple((s,response_at(y,s)) for s in range(1,8))
        with self.assertRaises(SpectralSourceError):
            interpolate_response(samples,2)
        with self.assertRaises(SpectralSourceError):
            finite_response_identity(y,chain_response((F(2),F(3))),range(1,6),2)

    def test_distinct_rational_responses_cannot_fake_full_degree_scoped_census(self):
        a=chain_response((2,3,5))
        b=chain_response((2,3,5,7))
        self.assertFalse(finite_response_identity(a,b,range(1,9),3))
        self.assertTrue(finite_response_identity(a,a,range(1,9),3))

    def test_observed_McMillan_order_detects_hidden_depth_when_cyclic(self):
        for g in ((1,),(1,1),(1,2,3),(2,3,5,7),(F(3,2),F(4,3),F(5,2),F(3,5),F(4))):
            y=chain_response(g)
            self.assertEqual(len(y[1])-1,len(g)-1)

    def test_source_response_positive_and_strictly_increasing_on_positive_axis(self):
        for g in ((1,1),(1,2,3),(2,3,5,7)):
            vals=[response_at(chain_response(g),s) for s in range(12)]
            self.assertTrue(all(0<vals[i]<vals[i+1]<g[0] for i in range(11)))

    def test_boundary_moment_zeroth_order_is_one(self):
        for g in ((1,1),(2,3,5),(2,3,5,7)):
            moments=chain_moments(g,8)
            self.assertEqual(moments[0],F(1))
            self.assertEqual(moments[1],F(g[0]+g[1]))

    def test_source_Krylov_path_minimality_coefficient(self):
        for g in ((1,1),(2,3,5),(2,3,5,7),(F(1,2),F(7,4),F(3,5))):
            A=chain_jacobi(g)
            n=len(A)
            v=[F(1)]+[F()]*(n-1)
            for _ in range(n-1):
                v=[sum((A[i][j]*v[j] for j in range(n)),F()) for i in range(n)]
            self.assertEqual(v[n-1],boundary_krylov_top_coefficient(g))
            self.assertNotEqual(v[n-1],0)

    def test_infinite_precision_does_not_make_static_response_identify_chain(self):
        a=(F(1,2),)
        b=(F(1),F(1))
        self.assertNotEqual(a,b)
        self.assertEqual(response_at(chain_response(a),0),response_at(chain_response(b),0))
        self.assertNotEqual(response_at(chain_response(a),1),response_at(chain_response(b),1))


class SourceRoundTripHistoryTests(unittest.TestCase):
    def test_first_new_depth_is_exactly_two_times_old_depth(self):
        for g in ((F(1),F(1)),(F(2),F(3),F(5)),(F(2),F(3),F(5),F(7)),
                  (F(1,2),F(7,4),F(3,5))):
            for extra in (F(1,5),F(1),F(7)):
                r=len(g)-1
                x=round_trip_new_depth(g,extra)
                self.assertEqual(x['first_distinguishing_moment'],2*r)
                self.assertEqual(x['moments_before'][:2*r],x['moments_after'][:2*r])
                self.assertEqual(x['difference'],
                                 __import__('math').prod(F(q)**2 for q in g[1:]))

    def test_first_return_difference_is_independent_of_new_terminal_weight(self):
        g=(F(2),F(3),F(5))
        vals=[round_trip_new_depth(g,t)['difference'] for t in (F(1,9),F(1),F(100))]
        self.assertEqual(vals,[F(225)]*3)

    def test_high_frequency_order_separates_finite_depths(self):
        g=(F(2),F(3),F(5))
        orig=chain_moments(g,6)
        new=chain_moments(g+(F(7),),6)
        self.assertEqual(orig[:4],new[:4])
        self.assertEqual(new[4]-orig[4],F(225))
        self.assertNotEqual(orig[5],new[5])

    def test_arbitrarily_small_coupling_makes_extra_node_hard_to_measure(self):
        for eps in (F(1,10),F(1,100),F(1,1000)):
            short,long=approximate_hidden_mode_pair(eps)
            self.assertNotEqual(short,long)
            for s in (0,1,2,5,25):
                gap=abs(response_at(long,s)-response_at(short,s))
                self.assertGreater(gap,0)
                self.assertLess(gap,eps*eps)

    def test_no_uniform_topology_recovery_with_unbounded_condition_number(self):
        eps=F(1,1000)
        short,long=approximate_hidden_mode_pair(eps)
        for s in (0,1,2,3,4,5):
            self.assertLess(abs(response_at(short,s)-response_at(long,s)),F(1,1000000))
        self.assertEqual(len(recover_positive_chain(short)),2)
        self.assertEqual(len(recover_positive_chain(long)),3)

    def test_dark_boundary_mode_is_invisible_despite_connected_interior(self):
        # A has offdiagonal symmetry: (0,1,-1) is a genuine dark eigenmode,
        # orthogonal to the boundary state e1 despite both arms being coupled.
        A=((F(3),F(-1),F(-1)),
           (F(-1),F(2),F()),
           (F(-1),F(),F(2)))
        dark=(F(),F(1),F(-1))
        self.assertEqual(tuple(sum((A[i][j]*dark[j] for j in range(3)),F()) for i in range(3)),
                         tuple(2*x for x in dark))
        self.assertEqual(dark[0],0)
        # Its resolvent is the same boundary response as the 2-dimensional
        # Jacobi  [[3,-sqrt(2)],[-sqrt(2),2]] by symmetry reduction.
        # Test rational m(s) by independent exact block Schur at sampled s:
        for s in (0,1,2,3,5):
            S=tuple(tuple(A[i][j]+(F(s) if i==j else F()) for j in range(3))
                    for i in range(3))
            inv=matrix_inverse(S)
            spectral=F(1)/(F(s+3)-F(2,s+2))
            self.assertEqual(inv[0][0],spectral)

    def test_disconnected_extra_hidden_modes_do_not_affect_any_response(self):
        # This is an even simpler no-go: a decoupled extra degree of freedom
        # contributes no boundary-accessible pole or moment at all.
        g=(F(2),F(3),F(5))
        A=chain_jacobi(g)
        for s in (0,1,2,3,4):
            base=tuple(tuple(A[i][j]+(F(s) if i==j else F()) for j in range(2)) for i in range(2))
            ext=tuple(tuple(
                (A[i][j] if i<2 and j<2 else
                 (F(11) if i==j==2 else F()))+(F(s) if i==j else F())
                for j in range(3)) for i in range(3))
            self.assertEqual(matrix_inverse(base)[0][0],matrix_inverse(ext)[0][0])


    def test_operational_krylov_canonical_chain_recovers_physical_path(self):
        for g,diag,off in (
            ((F(1),F(1)),(F(2),),()),
            ((F(2),F(3),F(5)),(F(5),F(8)),(F(9),)),
            ((F(2),F(3),F(5),F(7)),(F(5),F(8),F(12)),(F(9),F(25))),
        ):
            result=recover_operational_jacobi(chain_response(g))
            self.assertEqual(result['port'],g[0])
            self.assertEqual(result['diagonal'],diag)
            self.assertEqual(result['offdiagonal_squared'],off)
            self.assertEqual(result['minimal_observable_order'],len(g)-1)

    def test_dark_star_canonical_minimal_geometry_differs_from_physical_graph(self):
        # Symmetric star with one boundary-invisible antisymmetric eigenmode.
        # Canonical observable chain has b^2=2 (not a physical g^2).
        response=rational_response((F(2),F(4),F(1)),
                                   (F(4),F(5),F(1)))
        result=recover_operational_jacobi(response)
        self.assertEqual(result['port'],F(1))
        self.assertEqual(result['diagonal'],(F(3),F(2)))
        self.assertEqual(result['offdiagonal_squared'],(F(2),))
        self.assertEqual(result['minimal_observable_order'],2)
        with self.assertRaises(SpectralSourceError):
            recover_positive_chain(response)

    def test_operational_inverse_rejects_invalid_nonpositive_Jacobi_link(self):
        # This synthetic response has formal continued-fraction link b^2<0.
        bad=rational_response((F(2),F(4),F(1)),
                              (F(2),F(5),F(1)))
        with self.assertRaises(SpectralSourceError):
            recover_operational_jacobi(bad)

    def test_wrong_source_numeric_and_zero_coupling_rejected(self):
        with self.assertRaises(SpectralSourceError):
            chain_response((F(1),F(0)))
        with self.assertRaises(SpectralSourceError):
            chain_response((F(1),0.5))
        with self.assertRaises(SpectralSourceError):
            recover_positive_chain(rational_response((F(1),F(1)),(F(1),F(1),F(1))))
        with self.assertRaises(SpectralSourceError):
            interpolate_response(((F(1),F(2)),),2)
        with self.assertRaises(SpectralSourceError):
            interpolate_response(((F(1),F(2)),)*5,2)



class BoundaryHankelDepthTests(unittest.TestCase):
    def test_hankel_principal_minors_measure_exact_visible_layers(self):
        for g,expected in (
            ((F(1),F(1)),(F(1),F(0))),
            ((F(2),F(3),F(5)),(F(1),F(9),F(0))),
            ((F(2),F(3),F(5),F(7)),(F(1),F(9),F(2025),F(0))),
            ((F(1,2),F(7,4),F(3,5)),(F(1),F(49,16),F(0))),
        ):
            witness=hankel_depth_certificate(g)
            self.assertEqual(witness['hankel_determinants'],expected)
            self.assertEqual(witness['first_zero_order'],len(g))
            for r,v in enumerate(expected,1):
                self.assertEqual(exact_determinant(boundary_moment_hankel(g,r)),v)

    def test_hankel_is_gram_of_independently_computed_krylov_vectors(self):
        for g in ((F(1),F(1)),(F(2),F(3),F(5)),
                  (F(2),F(3),F(5),F(7))):
            A=chain_jacobi(g)
            n=len(A)
            vectors=[]
            v=[F(1)]+[F()]*(n-1)
            for j in range(n):
                vectors.append(tuple(v))
                v=[sum((A[i][k]*v[k] for k in range(n)),F())
                   for i in range(n)]
            Gram=tuple(tuple(sum((vectors[i][k]*vectors[j][k]
                                  for k in range(n)),F())
                             for j in range(n)) for i in range(n))
            self.assertEqual(Gram,boundary_moment_hankel(g,n))
            self.assertEqual(exact_determinant(Gram),
                             hankel_depth_certificate(g)['hankel_determinants'][n-1])

    def test_weak_new_layer_makes_positive_hankel_rank_arbitrarily_small(self):
        for eps in (F(1,10),F(1,100),F(1,10000)):
            g=(F(1),eps,F(1))
            dets=hankel_depth_certificate(g)['hankel_determinants']
            self.assertEqual(dets,(F(1),eps*eps,F()))
            self.assertGreater(dets[1],0)
        self.assertLess(hankel_depth_certificate((F(1),F(1,10000),F(1)))['hankel_determinants'][1],F(1,1000000))

    def test_connected_dark_star_has_krylov_rank_two_not_physical_three(self):
        A=((F(3),F(-1),F(-1)),
           (F(-1),F(2),F()),
           (F(-1),F(),F(2)))
        v=[F(1),F(),F()]
        mu=[]
        for k in range(5):
            mu.append(v[0])
            v=[sum((A[i][j]*v[j] for j in range(3)),F()) for i in range(3)]
        H2=((mu[0],mu[1]),(mu[1],mu[2]))
        H3=tuple(tuple(mu[i+j] for j in range(3)) for i in range(3))
        self.assertEqual(exact_determinant(H2),F(2))
        self.assertEqual(exact_determinant(H3),F())
        self.assertEqual(recover_operational_jacobi(rational_response(
            (F(2),F(4),F(1)),(F(4),F(5),F(1))))['minimal_observable_order'],2)

    def test_invalid_hankel_order_and_malformed_determinant_rejected(self):
        with self.assertRaises(SpectralSourceError):
            boundary_moment_hankel((F(2),F(3),F(5)),0)
        with self.assertRaises(SpectralSourceError):
            boundary_moment_hankel((F(1),),1)
        with self.assertRaises(SpectralSourceError):
            exact_determinant(((F(1),F(2)),))
        with self.assertRaises(SpectralSourceError):
            exact_determinant(((F(1),0.5),(F(2),F(3))))

if __name__=="__main__":
    unittest.main()
