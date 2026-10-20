# Academic Main VII: operator realization and source audit

**Status:** PROVED elementary correction and paper-proof audit; not a formal-kernel
certificate. Audited combined tree: `176d7f0fff8e9c7fae290e545376bac4cefe05ac`.
This is a new audit, not a replay receipt for the earlier research trees.

## Verdict

The cloud primitive-completion theorem and the finite counterexamples in
`operator_space_dict.py` are compatible. The former supplies the missing
quotient, closability and form-core hypotheses needed to transport a
K-relative bound. The latter correctly prevents replacing such a bound by an
absolute bound in derivative coordinates. Neither alone identifies an
arithmetic source.

One assertion in `OPERATOR_SPACE_RECONCILIATION.md`, sections 1.3–1.4, is false
on its stated fixed interval: vanishing of the full-line Gamma multiplier at
frequency zero does **not** show absence of an absolute primitive L² gap after
restriction to that interval. The following elementary calculation refutes
that inference. It does not determine the sign of the full signed source.

## A fixed-support Gamma gap

Let I = [−a,a], a > 0, and let Eα be the bounded self-adjoint integral operator
on L²(I) with kernel exp(−α|x−y|), α > 0. Its nonnegative symmetric kernel has
row integral

\[
 \int_{-a}^a e^{-\alpha|x-y|}\,dy
 =\frac{2-e^{-\alpha(a+x)}-e^{-\alpha(a-x)}}{\alpha}
 \le \frac2\alpha(1-e^{-\alpha a}).
\]

The inequality follows from cosh(αx) ≥ 1. The Schur test, or direct application
of 2|f(x)f(y)| ≤ |f(x)|²+|f(y)|² under the double integral, gives

\[
 \frac2\alpha I-E_\alpha
 \succeq \frac2\alpha e^{-\alpha a}I.
\]

This proof holds for all real or complex L² functions, with no moment or
boundary assumptions. For the actual primitive Gamma rungs on I=[−1/2,1/2],
α=(4j+1)/2 and Γj=4/(4j+1)I−Eα. Hence

\[
 \Gamma_j\succeq \frac4{4j+1}e^{-(4j+1)/4}I,
 \qquad \Gamma_0\succeq4e^{-1/4}I\succeq3I.
\]

The last rational bound uses e^(−x) ≥ 1−x. In particular any finite Gamma sum
containing rung zero, and its monotone closed-form limit, has this primitive
L² lower bound. The full-line multiplier still vanishes at zero: its domain is
different, and zero-extended functions supported in I cannot concentrate
arbitrarily tightly at frequency zero. There is no contradiction.

**Boundary of this correction.** The signed source subtracts the contact and
prime terms and includes both pole terms. A positive Gamma gap is not a
positive gap for that signed sum. Composing with the compact integration map
V gives a K-relative derivative bound, not an absolute derivative L² gap.
The authentic first-window S₄ sign and RH remain OPEN.

**Minimal falsifier of the old inference.** Γ₀ on L²([−1/2,1/2]) has a
full-line symbol vanishing at zero and nevertheless Γ₀ ≥ 3I. This is a universal
analytic counterexample, not a finite eigenvalue observation. The Schur-test
estimate is classical; its use here corrects a project-specific inference.

## The two representations

For a bounded V:H→G, K=V*V and a form q₀ on a linear D₀⊂H, the lower bound
q₀[u]≥κ||Vu||², κ>0, transports to a positive closed form on
E=closure(V D₀) only after checking:

1. q₀(n,u)=0 for every n∈D₀∩ker V and u∈D₀, so the quotient form is defined;
2. the descended form on V D₀ is closable in E;
3. if a separately defined source form is asserted to be its closure, V D₀ is
   a form core for that source, not merely dense in the ambient norm.

`CLOUD_OPERATOR_SOURCE_FORENSICS.md`, COT-01–05, states these requirements and
supplies valid kernel, nonclosability and dense-but-not-core counterexamples.
Its compact-V example correctly allows a primitive identity operator with a
derivative operator whose spectrum accumulates at zero. The finite witnesses
in `operator_space_dict.py` establish only their specified finite matrices;
their `source_form_identified=False` boundary is appropriate. They cannot
refute primitive coercivity of the actual closed source form.

The earlier reconciliation dossier also retains historical numbers (including
1/κ=50) and labels primitive coercivity unproved. The later source comparison
used in the combined tree is the paper inequality D≥κI+w₀(I−A_b) on the
primitive high space, with κ=63/500 or 153/500 and w₀=12/25. It depends on the
all-high Gamma/Legendre estimate, its rational errors, and the source form-core
identification; no Lean formalization of those analytic obligations is claimed.
The older statements must not be used as current numerical or status receipts.

## Source and authority boundary

The actual pinned source is
`observational_succ/source_weil_hierarchy.py`, Git blob
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`. Its introduction is SUCC commit
`b0cef75f47de29b1326b351df35b9e5423f2ed4f`. It is **not** one of the 72 files
copied from the original repository at import anchor
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`; the cloud source dossier already
corrects that historical attribution. A blob match establishes file identity,
not correctness of a theorem or identification of an operator realization.

The source probe invokes `source_parameters()`, which checks that source blob,
the genuine first-window prime-power tape ((2,2),), and exclusion of 6 as a
prime power. Its complete action retains the real Gamma rungs, completed poles,
contact, prime shift log 2, weight log 2/√2, and half-density 1/2. The shifted
polynomial interval errors and omitted-Gamma action errors are essential.
The constraint correction acts on this residual; it does not replace the
signed source by a positive kernel. No zero ordinates occur as inputs.

`exact_piecewise_primitive_action(..., parameters=...)` is a low-level
construction API, not by itself an authentication boundary: it admits parameter
dictionaries satisfying only partial checks. The trusted source run must use
`source_parameters()` and preserve its returned values, as the cloud probe
does. `source_regions()` independently rejects a dictionary unequal to those
source parameters. Synthetic packets and standalone matrix certificates carry
no original-source proof authority.

## Integration disposition and next falsifier

- Accept the cloud completion theorem with its explicit assumptions and paper
  proof status; retain the finite derivative/primitive counterexamples.
- Supersede the fixed-interval Gamma no-gap assertion by the proof above.
- Preserve the source-core and all-high comparison dependencies, and keep the
  first-window signed Schur sign unresolved.
- The next quantitative probe is the exact two-by-two constraint Gram inverse,
  with interval control in b=log 2, on a Gamma depth not used in the earlier
  cloud receipt. Its gain must be certified as a rational matrix inequality.
- An independent derivation of the source-core or all-high Gamma comparison
  would change the strength of source authentication more than additional
  agreement between finite matrix implementations.

This audit is an independent reconstruction by a separate same-family model
agent, not an external mathematical referee or formal verification.
