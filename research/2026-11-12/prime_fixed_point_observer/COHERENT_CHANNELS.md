# Coherent transport: what an inaccessible carrier may learn

Parent publication: `e9639c0ddb07385c6000b670d26cf0f7b91dacaa`;
validated local equivalent: `599c55ef`, content tree
`d591ba032b6b0cef8f62a32100455f9c3857b681`.
Status: **CLASSICAL** finite channel/recovery theory with **PROVED LOCAL**
specializations, explicit proofs and exact finite controls. No physical
collapse mechanism, new quantum advantage, or arithmetic asymptotic is asserted.

## 0. The faithful question and the present interface

The user's refinement asks whether a path can interact with the carrier in
a way that damages the twins' eventual comparison, and whether a coherent
path avoids that damage until the meeting. The useful protected object is
the **logical information required by the declared current output**. A
carrier interaction can preserve it, alter its calibrated phase, attach
a recoverable syndrome, or leak it into an inaccessible subsystem. These
possibilities have different mathematical tests.

Fix finite complex Hilbert spaces `C`, `B`, `E`, with `d=dim C>=1`.
`C` is the chosen logical code; `B` is everything accessible to one observer
at the meeting before its declared decoder; `E` is inaccessible there.
Take `W:C -> B tensor E` as the declared logical input interface. A
prepared pure carrier state independent of the arbitrary logical input,
followed by an isometric full evolution, supplies such an interface. A
fixed mixed initial carrier, also independent of that input, can be
purified by putting its purifying register into `E`; the access partition
must remain explicit. Known input/carrier correlations require a specified
encoding included in `W`. Arbitrary pre-existing correlations do not by
themselves define one channel on all logical inputs. Define

\[
 \mathcal N(X)=\operatorname{Tr}_E(WXW^*),\qquad
 \mathcal N^c(X)=\operatorname{Tr}_B(WXW^*).
\]

Choose a basis `|a>` of `E` and write
`W psi = sum_a E_a psi tensor |a>`. Then
`sum_a E_a^* E_a=I_C`, and `N(X)=sum_a E_a X E_a^*`.
These are mathematical descriptions of a present channel. Neither `W`
nor its Kraus list is automatically supplied by one physical observation.

Fix a common calibrated orthonormal basis of `C` and a reference register
`R` of dimension `d`. Put

\[
 |\Phi_d\rangle=d^{-1/2}\sum_{j=0}^{d-1}|j\rangle_C|j\rangle_R.
\]

The comparator may receive a declared joint measurement on the **current**
`B,R` outputs at the meeting. It receives no raw histories. All transport,
phase conventions, source authentication and accessibility assumptions
must be justified separately, as in [TWIN_OBSERVERS.md](TWIN_OBSERVERS.md).

The reference in this channel test is untouched, or has a separately known
transport already removed by calibration. It is not permissible to insert
an unknown noisy evolution of the other twin and still call the resulting
state the Choi test of `N`. With independent local channels one may analyze
each against its own reference. With a shared carrier, use the actual joint
isometry and access partition; a tensor product of independent noise models
is an additional assumption. Preserving one specified joint state under an
arbitrary joint interaction does not certify its action on all joint inputs.

The finite channel/isometry convention is standard: Watrous,
[*The Theory of Quantum Information*, Chapter 2, Corollary 2.27 and the
isometric-channel example](https://jhwatrous.github.io/TQI.2.pdf).

## 1. Exact preservation of a specified twin

Let `V:C -> B` be a **fixed calibrated isometry**, and put
`|Phi_V>=(V tensor I_R)|Phi_d>`. Its choice fixes the intended output
transport, rather than selecting a convenient transport after seeing a
failed comparison.

**CCH-01 — CLASSICAL / PROVED LOCAL, fixed-output criterion.** The following
four statements are equivalent:

1. `N(X)=V X V^*` for every `X in End(C)`.
2. `(N tensor id_R)(|Phi_d><Phi_d|)=|Phi_V><Phi_V|`.
3. There is one unit vector `eta in E`, independent of the logical input,
   with `W psi=V psi tensor eta` for every `psi in C`.
4. For every environment index `a`, `E_a=c_a V`, where
   `sum_a |c_a|^2=1`.

**Proof.** Statement 1 gives 2 by expanding the `d^2` matrix units in the
twin density. Assume 2. The vector `(W tensor I_R)Phi_d` has the pure
`B,R` reduction `|Phi_V><Phi_V|`. Decompose it along `Phi_V` and its
orthogonal complement. The squared norm of the latter is the trace of
that complementary projection against the reduced density, hence zero.
Thus the full vector is `Phi_V tensor eta`, after the harmless register
reordering, for a unit `eta`. Comparing its coefficients at each reference
basis vector proves 3. Expanding `eta=sum_a c_a|a>` proves 4. Substituting
4 into the channel proves 1. This also proves the result for `d=1`; that
case has no nontrivial logical quantum information to protect. QED.

This is an exact meaning of a path leaving **no information about the
protected input in the inaccessible carrier** while implementing the
specified output isometry. It does not require the carrier to remain in
its initial state. The same change `eta_initial -> eta` may occur for
every logical input. A nontrivial interaction can act differently outside
the code while acting identically on all inputs inside it.

The test in statement 2 is exact equality of channel output states. A
single accepted physical projector outcome does not establish that
equality; Section 4 quantifies the acceptance probability.

### Pure local outputs do not suffice

The channel `N(X)=Tr(X)|0><0|` sends every pure input to a pure output.
Its isometry `W|j>=|0>_B|j>_E` transfers the entire input to the environment.
Its twin output is `|0><0|_B tensor I_R/d`, not a preserved twin for `d>1`.
Thus local purity alone does not certify transmission, source agreement,
or surviving reference correlation.

## 2. Recoverable interaction is more general than an unchanged pure output

The previous theorem specifies a pure isometric output **before recovery**.
The user can instead permit a declared present decoder
`R:L(B)->L(C)`, completely positive and trace preserving. Such recovery is
part of the current-output processing, not an exchange of histories.

**CCH-02 — CLASSICAL Knill--Laflamme criterion, explicit proof.** The
following are equivalent:

1. A channel `R` exists with `R N(X)=X` for every `X in End(C)`.
2. For all Kraus indices `a,b`, there are scalars `lambda_ab` such that
   `E_a^* E_b=lambda_ab I_C`.
3. A density matrix `tau_E` exists with
   `N^c(X)=Tr(X)tau_E` for every `X in End(C)`.

This is the finite exact quantum error-correction condition. Its original
source is Knill and Laflamme, [*A Theory of Quantum Error-Correcting Codes*,
Theorems 3.2--3.5](https://arxiv.org/pdf/quant-ph/9604034), especially the
logical-state, completely entangled-state, and syndrome characterizations.

**Proof of 1 implies 2.** Let `R_b` be Kraus operators of the recovery.
The composite channel has Kraus operators `R_b E_a` and equals the
identity. CCH-01 with `V=I_C` gives `R_b E_a=c_ba I_C`. Consequently

\[
 E_a^*E_c
 =\sum_b E_a^*R_b^*R_b E_c
 =\left(\sum_b\overline{c_{ba}}c_{bc}\right)I_C.
\]

**Proof of 2 implies 1.** The scalar matrix `lambda` is positive
semidefinite: for coefficients `z_a` and a unit logical vector `psi`,
`sum_ab conjugate(z_a)lambda_ab z_b=||sum_a z_a E_a psi||^2>=0`.
It has trace one. Change the Kraus basis by a unitary diagonalizing this
Gram matrix. The new Kraus operators obey
`F_j^* F_k=p_j delta_jk I_C`, with `p_j>=0` and `sum_j p_j=1`.
Ignore indices with `p_j=0` and set `V_j=F_j/sqrt(p_j)`.
These are isometries with mutually orthogonal ranges. Let
`Q=sum_j V_j V_j^*` and choose any density matrix `omega` on `C`. Then

\[
 \mathcal R(Y)=\sum_j V_j^*YV_j
       +\operatorname{Tr}((I_B-Q)Y)\,\omega
\]

is a channel: each term is completely positive, and the traces add to
`Tr Y`. Orthogonality gives
`R N(X)=sum_j p_j X=X`.

**Proof of 2 iff 3.** The environment matrix entries are

\[
 (\mathcal N^c(X))_{ab}=\operatorname{Tr}(E_b^*E_a X).
\]

Under 2 these equal `lambda_ba Tr X`; thus `tau_ab=lambda_ba`.
Conversely equality for every matrix unit `X` forces
`E_b^*E_a=tau_ab I_C` by nondegeneracy of the trace pairing. QED.

The statement includes **all** logical matrix units. Checking only the
environment marginals of a basis of pure inputs misses information about
superpositions. An exact four-dimensional countercontrol in the probe has

\[
 W|0\rangle=\tfrac12\sum_{a=0}^3|a\rangle_B|a\rangle_E,\qquad
 W|1\rangle=\tfrac12\sum_{a=0}^3s_a|a\rangle_B|a\rangle_E,
 \quad(s_0,s_1,s_2,s_3)=(1,1,-1,-1).
\]

The two columns are orthonormal, and their environment densities are both
`I_E/4`. Nevertheless
`N^c(|0><1|)=diag(1,1,-1,-1)/4` is nonzero. The carrier learns a
superposition observable; exact logical recovery from `B` fails.

### A positive interaction example with a changing carrier

Let `B=C tensor S`, where `S` is an accessible two-level syndrome.
Set `V_j psi=psi tensor |j>` and

\[
 E_0=\tfrac35 V_0,\qquad E_1=\tfrac45 V_1.
\]

Then
`N(X)=X tensor diag(9/25,16/25)` and
`N^c(X)=Tr(X)diag(9/25,16/25)`. Tracing out the accessible syndrome
recovers `X`, including when it is correlated with the twin reference.
A pure logical input gives a mixed raw `B` state with purity `337/625`.
Thus raw-output mixedness can coexist with exact recovery of the logical
twin. The inaccessible environment has acquired syndrome information,
but no logical-input information.

The source program already contains this distinction in its
[weighted Bruhat--Tits code](../../2026-10-22/PADIC_BULK_RECONSTRUCTION.md),
QEC-2 and QEC-3, and
[Prime Bridge ledger](../../../docs/CLAIM_SUPPLEMENT_ARITHMETIC_ER_EPR.md),
PBR-14--17. Those files were inspected, not altered. Their latest joint
history entry is `13d5a4062e0812ef9b31e3585381f4ceedb7bbe4`.
The addition here is the criterion tied explicitly to the present twin
interface, together with the quantitative residual and new countercontrols;
there is no priority claim for quantum error correction.

## 3. Learning a logical label leaves a precise cost

Consider a reversible source computation with a fresh carrier record:

\[
 C_f|x\rangle|0\rangle=|x\rangle|f(x)\rangle.
\]

The input labels are orthogonal, so this is an isometry regardless of
whether `f` is injective. With the record inaccessible, the current source
channel is

\[
 |x\rangle\langle y|\longmapsto
 \mathbf1_{f(x)=f(y)}|x\rangle\langle y|.
\]

**CCH-03 — PROVED LOCAL.** On the coordinate code spanned by a nonempty
set `D` of labels, the unchanged logical channel survives exactly when
`f` is constant on `D`. This follows directly from the displayed action
on every matrix unit. If two code labels have distinct records, the
channel sends their plus and minus superpositions to the same density,
so no channel acting only on the retained output can recover both.

The global computation remains reversible. If the record is accessible,
applying its inverse can restore the superposition. Retaining a useful
output can also be legitimate, provided that its logical role and cost
are included. What fails is claiming that an inaccessible, informative
record preserved an arbitrary unknown superposition unchanged.

For nonorthogonal preserved pure states the constraint is even sharper.
If an isometry obeys
`W psi=V psi tensor eta_psi` and
`W phi=V phi tensor eta_phi` for a common isometry `V`, preservation of
inner products gives
`<psi,phi>=<psi,phi><eta_psi,eta_phi>`. Whenever `<psi,phi> != 0`, the
two unit records must coincide. This elementary equality is the relevant
no-information-without-disturbance statement under the stated exact
preservation assumption; it is not a ban on computation or all observation.

## 4. A quantitative current twin residual

For the fixed target isometry `V`, define the current entanglement fidelity

\[
 F_V=\langle\Phi_V|
 (\mathcal N\otimes\mathrm{id})(|\Phi_d\rangle\langle\Phi_d|)
 |\Phi_V\rangle.
\]

It is the acceptance probability of the projector onto `Phi_V`, **if**
that joint measurement is available on the current outputs. A mathematical
proof of `F_V=1` has a different scope from observing one acceptance.

**CCH-04 — PROVED LOCAL, exact residual identity.** Put
`c_a=Tr(V^*E_a)/d`. Then

\[
 \boxed{
 F_V=\frac1{d^2}\sum_a|\operatorname{Tr}(V^*E_a)|^2,
 \qquad
 1-F_V=\frac1d\sum_a\|E_a-c_aV\|_F^2.}
\]

**Proof.** Expanding the reference basis gives
`<Phi_V,(E_a tensor I)Phi_d>=Tr(V^*E_a)/d`; summing the outer products
over the Kraus index gives the first identity. Since `||V||_F^2=d`,
`c_aV` is the orthogonal projection of `E_a` onto the line spanned by
`V` in the Hilbert--Schmidt inner product. Therefore
`||E_a-c_aV||_F^2=||E_a||_F^2-d|c_a|^2`.
Sum over `a`, use `sum_a||E_a||_F^2=Tr I_C=d`, and substitute the first
identity. QED.

Thus the exact full-reference comparison fails by precisely the total
normalized squared Kraus component orthogonal to the intended isometry.
This quantity includes calibrated logical transport error **and** leakage;
it should not be renamed a pure decoherence score. For example, a unitary
phase error can make `F_V=0` while preserving maximal entanglement.

For a quantitative all-input statement, assume `F_V>0`, let
`c=sum_a c_a|a>`, and set `eta=c/sqrt(F_V)`. For every unit `psi in C`,

\[
 \|W\psi-V\psi\otimes\eta\|
 \le\sqrt{d(1-F_V)}+1-\sqrt{F_V}.
\]

Indeed `W-V tensor c` has squared Hilbert--Schmidt norm `d(1-F_V)`;
its operator norm is no larger. The second term is the norm difference
between `c` and `eta`. This bound records its explicit dimension cost.
It is not a dimension-free guarantee or an infinite-carrier certificate.

## 5. Record overlap separates amplitude loss from a coherent phase

Choose unit environment records `eta_j` and the nondemolition isometry
`W|j>=|j>_B eta_j`. Write `g_ij=<eta_j,eta_i>`, with inner product
conjugate-linear in its first argument. The current twin density is

\[
 \rho_{BR}=\frac1d\sum_{i,j}g_{ij}|ii\rangle\langle jj|.
\]

**CCH-05 — PROVED LOCAL.** Its two individual marginals are `I/d`, and

\[
 \boxed{
 \operatorname{Tr}\rho_{BR}^2=\frac1{d^2}\sum_{i,j}|g_{ij}|^2,
 \qquad F_I=\frac1{d^2}\left\|\sum_j\eta_j\right\|^2,
 \qquad
 1-F_I=\frac1{2d^2}\sum_{i,j}\|\eta_i-\eta_j\|^2.}
\]

**Proof.** Matrix units `|ii><jj|` multiply with a Kronecker delta,
giving the purity. Pairing each side with `Phi_d` gives the double sum
of record inner products. Expanding every pairwise squared distance
proves the last equality. The individual partial traces retain only
`i=j`, where `g_ii=1`. QED.

These formulas are **present-state** diagnostics. They can be computed
from a supplied channel model; their derivation does not authorize the
comparator to inspect historical records in different frames.

If `eta_j=exp(i theta_j)eta`, then all records have the same density
and the channel is the coherent diagonal unitary
`D=diag(exp(i theta_j))`. No logical information leaks. A known output
calibration `D^*` restores the target twin. Conversely, the joint twin
state is pure exactly when all record vectors are collinear: by the
purity formula equality to one forces every `|g_ij|=1`, hence equality
in Cauchy--Schwarz. Collinearity is weaker than literal equality of the
records; it permits a logical phase.

### Exact two-level cases

For `d=2`, set `gamma=<eta_1,eta_0>`. On the subspace spanned by
`|00>,|11>`, the twin density is
`[[1,gamma],[conjugate(gamma),1]]/2`. Its partial transpose has eigenvalues
`1/2,1/2,|gamma|/2,-|gamma|/2`: the middle two-dimensional block has
characteristic polynomial `t^2-|gamma|^2/4`.

For `gamma != 0` that partial transpose has a negative direction. Every
separable state's partial transpose is positive, since a product positive
matrix remains positive under a transpose on one factor, and sums preserve
positivity. The output is therefore entangled. For `gamma=0` it is the
explicit separable mixture of `|00>` and `|11>`. Consequently, in this
model **partial leakage need not destroy all entanglement**.

| Records | `gamma` | Fixed-target `F_I` | Joint purity | Meaning |
| --- | ---: | ---: | ---: | --- |
| Equal | `1` | `1` | `1` | Exact original twin |
| `eta_0=(1,0)`, `eta_1=(3/5,4/5)` | `3/5` | `4/5` | `17/25` | Partial leakage; still entangled |
| Orthogonal | `0` | `1/2` | `1/2` | Separable correlated output |
| Opposite signs | `-1` | `0` | `1` | Pure maximally entangled phase-shifted twin |

All four cases have the same individual marginals and perfect equality
of computational-basis outcomes. Those coarse present outputs cannot
distinguish the cases. A richer joint, phase-calibrated output is required.

For fresh, independent record registers and nondemolition labels,
`eta_j=eta_j^(1) tensor ... tensor eta_j^(n)` gives
`g_ij=product_t g_ij^(t)` by the tensor inner-product law. With a reused
carrier this product model can fail: a CNOT recording interaction followed
by the same CNOT unrecords it exactly. Earlier local decoherence need not
be permanent when the relevant carrier remains accessible. This does not
recover inaccessible information by merely changing the comparison frame.

## 6. Earned interpretation and next probe

The precise surviving form of the proposal is:

> Choose a logical code and current readout; transport them in declared
> frames. Preserve the required information by a fixed isometric output,
> or supply a valid present recovery. The inaccessible complementary
> channel must contain no information about arbitrary logical inputs.

An interaction, a logical phase mismatch, loss of local coherence, and
objective physical collapse are distinct. An entirely unitary carrier can
produce the local leakage diagnosed here. The calculation determines no
special physical collapse event at the meeting.

The construction closes a finite architectural criterion. It still needs
a source-derived arithmetic code/output and a quantitative connection to
the prime-pair or digit target. Setting the desired answer as the protected
input does not create a new proof of that answer. The next useful probe is
a candidate arithmetic walk whose *current* output satisfies the criterion
with a declared computation, access and error budget, while rejecting a
logical-label leakage mutation and a phase/calibration mutation.

`coherent_channels_probe.py` compares direct current twin densities with
the trace/residual formulas, tests full logical matrix-unit recovery,
retains the four record controls and the basis-only leakage counterexample,
and checks fresh versus reused records. Gaussian-rational arithmetic makes
every recorded equality exact. Finite checks calibrate these implementations;
the universal finite-dimensional statements rely on the proofs above.
Same-model derivations and replay are not external peer review.
