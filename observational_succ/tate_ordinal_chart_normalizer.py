"""ACTUAL local Tate p-adic two-axis SUCC normalization with ordinal ranks.

Grounded in existing tate_observer_completion.PadicBruhatChart, exact
finite source values and authentic additive Haar/Fourier maps.

For one FIXED target chart (R,S) >= (r,s), the ordinal
   rho = omega*(R-r)+(S-s)
strictly decreases as support/precision source refinements occur.
The two orders of refinement yield EXACTLY THE SAME source table
and finite Fourier transform (commuting Tate source diamond).

This proves finite completion of a DECLARED SOURCE TEST CHART.
Increasing the TARGET after completion starts a NEW proof obligation;
one must not misrepresent unbounded cofinal Tate/global work as one
finite ordinal-descending execution. RH source positivity is separate.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F

from .ordinal_ranked_succ import (
    OrdinalDescentError,OrdinalCNF,ordinal_lex_counters
)
from .tate_observer_completion import (
    PadicBruhatChart,local_tate_fourier,
    refine_local_precision,refine_local_support,
    exact_local_biaxial_diamond
)


@dataclass(frozen=True)
class TateOrdinalChartStage:
    chart:PadicBruhatChart
    values:tuple[F,...]
    target_support:int
    target_precision:int
    source_tag:str="DECLARED_SOURCE_QP_BRUHAT_SCHWARTZ"

    def __post_init__(self):
        if (not isinstance(self.chart,PadicBruhatChart)
                or type(self.target_support) is not int
                or type(self.target_precision) is not int
                or not self.chart.support_depth<=self.target_support<=5
                or not self.chart.precision_depth<=self.target_precision<=5
                or type(self.source_tag) is not str or not self.source_tag):
            raise OrdinalDescentError("Fixed lawful Tate source target chart required")
        try:
            terminal=PadicBruhatChart(
                self.chart.p,self.target_support,self.target_precision)
            canonical=self.chart.values(self.values)
        except (ValueError,TypeError) as exc:
            raise OrdinalDescentError("Tate source chart/cells cannot be normalized") from exc
        if canonical!=self.values or terminal.p!=self.chart.p:
            raise OrdinalDescentError("Actual source finite table and Fourier target malformed")

    @property
    def rank(self)->OrdinalCNF:
        return ordinal_lex_counters((
            self.target_support-self.chart.support_depth,
            self.target_precision-self.chart.precision_depth,
        ))

    @property
    def completed(self)->bool:
        return (self.chart.support_depth==self.target_support
                and self.chart.precision_depth==self.target_precision)

    def increase_support(self)->"TateOrdinalChartStage":
        if self.completed or self.chart.support_depth>=self.target_support:
            raise OrdinalDescentError("No legal source support growth remains")
        source=self.chart
        if not refine_local_support(source,self.values)["finite_Fourier_naturality"]:
            raise ArithmeticError("Original Tate p-adic support Fourier square failed")
        later=PadicBruhatChart(source.p,source.support_depth+1,source.precision_depth)
        data=[F() for _ in range(later.modulus)]
        for i,v in enumerate(self.values):
            data[source.p*i]=v
        result=TateOrdinalChartStage(later,tuple(data),
                self.target_support,self.target_precision,self.source_tag)
        if not result.rank<self.rank:
            raise ArithmeticError("Tate support SUCC did not decrease ordinal rank")
        return result

    def increase_precision(self)->"TateOrdinalChartStage":
        if self.completed or self.chart.precision_depth>=self.target_precision:
            raise OrdinalDescentError("No legal source precision growth remains")
        source=self.chart
        if not refine_local_precision(source,self.values)["finite_Fourier_naturality"]:
            raise ArithmeticError("Original Tate p-adic precision Fourier square failed")
        later=PadicBruhatChart(source.p,source.support_depth,source.precision_depth+1)
        data=tuple(self.values[j%source.modulus] for j in range(later.modulus))
        result=TateOrdinalChartStage(later,data,
                self.target_support,self.target_precision,self.source_tag)
        if not result.rank<self.rank:
            raise ArithmeticError("Tate precision SUCC did not decrease ordinal rank")
        return result


def complete_tate_source_chart(
        chart:PadicBruhatChart,raw:tuple[int|F,...],
        target_support:int,target_precision:int,
        *,strategy:str="support-first")->dict:
    """Execute small legal finite chart proof, then audit BOTH path orders.

    Source coefficients exact rationals. No arbitrary local prime,
    unobserved future event, fake Euler-place 6 or infinite stage.
    """
    if strategy not in ("support-first","precision-first"):
        raise OrdinalDescentError("Only source-licensed two-axis schedules")
    try:
        data=chart.values(raw)
    except (ValueError,TypeError,AttributeError) as exc:
        raise OrdinalDescentError("Original local Tate source table unavailable") from exc
    origin=TateOrdinalChartStage(chart,data,target_support,target_precision)
    def execute(schedule:str):
        current=origin
        ranks=[current.rank]
        while not current.completed:
            can_support=current.chart.support_depth<target_support
            if (schedule=="support-first" and can_support
                    or schedule=="precision-first" and
                    not (current.chart.precision_depth<target_precision)):
                current=current.increase_support()
            else:
                current=current.increase_precision()
            if not current.rank<ranks[-1]:
                raise ArithmeticError("Ordinal source normalization ceased descent")
            ranks.append(current.rank)
        return current,tuple(ranks)
    result,ranks=execute(strategy)
    opposite,_ranks=execute("precision-first" if strategy=="support-first" else "support-first")
    if result.values!=opposite.values:
        raise ArithmeticError("Tate two-axis source-normal forms disagree")
    fourier=local_tate_fourier(result.chart,result.values)
    if fourier!=local_tate_fourier(opposite.chart,opposite.values):
        raise ArithmeticError("Tate two-axis source Fourier final forms disagree")
    # The local two-step square additionally checks ALL finite cell corners
    # if both directions available at the original chart.
    if (target_support>chart.support_depth
            and target_precision>chart.precision_depth):
        source_sq=exact_local_biaxial_diamond(chart,data)
        if not (source_sq["strict_source_diamond_commutes"]
                and source_sq["dual_Fourier_diamond_commutes"]):
            raise ArithmeticError("Original Tate local square not lawful")
    return {
        "source":"ACTUAL_DECLARED_TATE_QP_SCHWARTZ_BRUHAT_CHART",
        "prime":chart.p,
        "start_chart":(chart.support_depth,chart.precision_depth),
        "terminal_chart":(target_support,target_precision),
        "normalization_strategy":strategy,
        "initial_rank":str(ranks[0]),
        "terminal_rank":str(ranks[-1]),
        "ordinal_decrease_on_every_executed_refinement":True,
        "actual_completed_refinements":len(ranks)-1,
        "terminal_source_values":result.values,
        "same_source_values_under_opposite_refinement_order":True,
        "same_exact_cyclotomic_Fourier_under_opposite_refinement_order":True,
        "true_global_Qp_Schwartz_colimit_finished_in_finite_time":False,
        "completed_global_Tate_adelic_Poisson":False,
        "RH_proved":False,
    }


def growing_tate_target_rank_no_go()->dict:
    """Retargeting to bigger Tate charts RESETS the proof, not one omega run."""
    chart=PadicBruhatChart(2,0,1)
    proof=complete_tate_source_chart(chart,(1,0),1,1)
    completed=proof["terminal_rank"]
    new_state=TateOrdinalChartStage(
        PadicBruhatChart(2,1,1),(1,0,0,0),2,1
    )
    if not new_state.rank>ordinal_lex_counters((0,0)):
        raise ArithmeticError("New chart target was not a fresh source obligation")
    return {
        "first_fixed_target_finished_rank":completed,
        "new_larger_target_started_rank":str(new_state.rank),
        "single_uniform_ordinal_descent_across_all_growing_targets":False,
        "source_all_finite_charts_exist_by_classical_filtered_union":True,
        "cofinal_Tate_Topology_done_by_finite_trace":False,
        "RH_proved":False,
    }
