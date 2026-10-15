"""Cross-implementation witness: finite SUCC characters = Tate S-lattice phases.

The three routes are genuinely different existing implementations:
(1) Q/Z character from one Z/nZ observation;
(2) finite adelic principal parts of r*z;
(3) Tate's old source-indexed rational S-chart with real coordinate zero.

Every equality here is exact rational phase equality on a finite
representation of source values; global Pontryagin completeness remains
a separately cited classical topological theorem.
"""
from __future__ import annotations

from fractions import Fraction as F

from .diagonal_adele_zeta import factor_positive, prime
from .edge_carrier_reconstruction import ProfiniteProgram
from .finite_adelic_character_bridge import character_adele_pairing
from .pontryagin_source_duality import (
    PontryaginSourceError, RationalCircleCharacter
)
from .tate_lattice_descent import (
    RationalSChart, character_naturality
)


def three_way_tate_duality(
    character: RationalCircleCharacter,
    source: ProfiniteProgram,
    *,
    extra_primes: tuple[int, ...] = ()
) -> dict:
    """Keep the Tate real + / finite - convention visible in the comparison."""
    if not isinstance(character, RationalCircleCharacter) or not isinstance(source,ProfiniteProgram) or (
        character.source_id,character.epoch)!=(source.source_id,source.epoch):
        raise PontryaginSourceError("Cross implementation must use one source and epoch")
    denominator_primes=tuple(sorted(factor_positive(character.frequency.denominator)))
    if type(extra_primes) is not tuple or any(not prime(p) for p in extra_primes):
        raise PontryaginSourceError("Only genuine declared new prime places are allowed")
    if len(set(extra_primes))!=len(extra_primes):
        raise PontryaginSourceError("Duplicate new finite places")
    full_primes=tuple(sorted(set(denominator_primes).union(extra_primes)))
    # Rational source values are sufficient to evaluate the FULL
    # finite-support character: at each p|denominator n we need
    # z_p modulo p^v_p(n). Extra integral places may be arbitrary.
    factors=factor_positive(character.frequency.denominator)
    local={}
    for p in full_primes:
        modulus=p**factors.get(p,1)
        local[p]=F(source.residue(modulus))
    chart=RationalSChart.from_places(
        full_primes,F(0),local,
        source_id=character.source_id,epoch=character.epoch
    )
    dual_phase=character.evaluate(source)
    adelic=character_adele_pairing(character,source)
    tate_finite_sign=chart.character_phase(character.frequency)
    if (dual_phase!=adelic["character_phase"] or
        tate_finite_sign!=(-dual_phase)%1):
        raise AssertionError("SUCC finite character does not transport to Tate atlas")
    # Adding an unobserved local place cannot alter an already existing
    # conductor-n character. This is the actual refinement square.
    refine=character_naturality(chart,denominator_primes,character.frequency)
    if not refine["commutes"]:
        raise AssertionError("Tate S-quotient projections lost a character")
    return {
        "source_id":character.source_id,"epoch":character.epoch,
        "rational_frequency":character.frequency,
        "minimal_primes":denominator_primes,
        "full_primes":full_primes,
        "direct_modular_phase":dual_phase,
        "finite_adelic_principal_phase":adelic["finite_adele_principal_sum"],
        "Tate_finite_negative_phase":tate_finite_sign,
        "Tate_projection_commutes":refine["commutes"],
        "three_way_compatibility":True,
        "full_topological_duality_proved_by_finite_check":False,
        "RH_proved":False,
    }
