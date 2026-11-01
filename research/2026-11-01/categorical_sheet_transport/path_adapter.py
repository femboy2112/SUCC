"""Adapter to SUCC's existing ObservationPathCategory; no rival category.

Requires a complete SUCC checkout. In a standalone archive, integration
checks must be reported as SKIPPED, not simulated with a substitute category.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class ArithmeticPathAdapter:
    category: object
    arithmetic: object
    Q: int

    def image(self, arrow):
        """Source-ordered monomial representation of a verified path arrow."""
        op=self.arithmetic.Monomial(self.Q)
        for name,j in self.category.pretty_path(arrow):
            if name!='original_bbp_successor':
                raise ValueError('unrecognized source operation')
            op=self.arithmetic.source_operator(j,self.Q).compose(op)
        return op

    def fourier_image(self,arrow):
        return self.image(arrow).fourier()


def build_path_adapter(horizon,arithmetic):
    from observational_succ.noncommuting_proof_transport import FiniteCarrier,Instrument
    from observational_succ.operational_yoneda_descent import BeliefGame,ObservationPathCategory
    if type(horizon) is not int or not 1<=horizon<=5:
        raise ValueError('existing finite path category supports horizons 1..5 here')
    # State indices are clocks; exact U_j labels are independently authenticated.
    values=arithmetic.states(horizon)
    arithmetic.authenticate(values)
    size=horizon+1
    instrument=Instrument('original_bbp_successor',tuple(j+1 for j in range(size)),
                          tuple(min(j+1,horizon) for j in range(size)),
                          tuple(j<horizon for j in range(size)))
    carrier=FiniteCarrier(size,(instrument,),
        'original-four-pole-U0=0-exact-recurrence-checked',
        'chronological-source-labels-not-sphere-sheet-permutations')
    game=BeliefGame.build(carrier,(0,),tuple('original_zero_seed' for _ in range(size)),
                         target_id='selected-original-BBP-source-boundary')
    cat=ObservationPathCategory(game,horizon)
    return ArithmeticPathAdapter(cat,arithmetic,arithmetic.conductor(horizon))
