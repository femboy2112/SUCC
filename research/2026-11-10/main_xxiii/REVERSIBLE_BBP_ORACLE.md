# Finite reversible BBP carry oracle

**PROVED** for the declared finite gate model. The gate list implements a permutation of computational basis states, so its linear extension is unitary. The declared arithmetic semantics apply on the subspace of valid seed encodings with zero-initialized work registers. The circuit leaves every work wire available for exact inversion. Its length is compiled into the circuit.

[Gate generator](bbp_reversible_oracle.py) · [Independent rational replay](test_bbp_reversible_oracle.py) · [Donor's finite dagger bridge](../omega_bbp_operational_completion/quantum_bridge/README.md)

## Source and arithmetic semantics

For a fixed length \(L\ge1\), set \(D=16^L\operatorname{lcm}_{0\le j<L}(8j+1,8j+4,8j+5,8j+6)\) and \(c_j=D R(j)\), with the four original coefficients \((4,-2,-1,-1)\). This common denominator retains every pole prime power at this horizon and represents the hostile seed \(-P_L\), where \(P_L=\sum_{j<L}16^{-j-1}R(j)\). A valid seed satisfies \(s=I_0+r_0/D\), \(I_0\in\{-1,0\}\) and \(0\le r_0<D\). A dedicated bit stores \(-I_0\).

Each chronological row writes
\[
T_j=16r_j+c_j,\qquad q_j=\lfloor T_j/D\rfloor,\qquad
r_{j+1}=T_j-Dq_j .
\]
The integer lift is losslessly encoded by the stored seed bit and all \(q_j\). Indeed \(I_{j+1}=16I_j+q_j\) gives \(I_{j+1}+r_{j+1}/D=16(I_j+r_j/D)+R(j)\). At each stage both the full lift and the numerator modulo every prime power of \(D\) can be recovered. These are representations of the exact values. The circuit outputs the winding residue and integer carry rather than allocating an extra register for each CRT coordinate. At any \(0\le n\le L\), exact decoding of the final lift and residue yields
\[
16^{n-L}(I_L+r_L/D)=16^n(s+P_L).
\]
This finite phase includes the future summands between index \(n\) and horizon \(L\). The donor's analytic tail estimate gives the error to the infinite phase for the original seed.

The moment representation with numerator \((1-x)(x^2+2)(x^2+2x+2)\) gives \(R(j)>0\), and the original pole formula gives \(R(j)<4\). Thus \(0\le T_j<20D\). Five greedy trial subtractions of \(16D,8D,4D,2D,D\) give the five bits of \(q_j\), including carries above 15. For each trial, subtraction is addition of a two's-complement constant. With \(B=\operatorname{bitlength}(D)\) and \(M=B+6\), every signed trial difference is strictly between \(-2^{M-1}\) and \(2^{M-1}\). The complemented high bit is therefore the exact select flag. Starting from the untouched input, XOR the flagged original bit and the flagged trial bit into each fresh output. That selects the trial on success and the original on failure.

Each constant adder writes a new sum and a new bit carry per column, using XOR for the sum and the three-input majority polynomial for the carry. Trial values, trial carries, flags, and selected values all remain present. The inverse executes the same self-inverse X, CNOT and Toffoli gates in reverse order. This also restores the seed and work registers on a superposition by linearity. An inverse test alone checks only the permutation property. Removing one gate gives another reversible circuit that fails the independent four-pole source check.

## Resource contract

The generator emits actual gates over X, CNOT and Toffoli. Each row uses one \(M\)-bit constant adder and five trial circuits. A constant adder uses \(2M\) new wires, at most \(M\) Toffoli, \(4M\) CNOT and \(M\) X. Each trial adds a flag and \(M\) selected bits, at most \(2M\) Toffoli, \(M+1\) CNOT and one X beyond its adder. The full circuit uses exactly \(1+B+L(17M+5)\) qubits and at most \(16LM\) Toffoli, \(L(29M+5)\) CNOT and \(L(6M+5)\) X.

| Horizon | Qubits | X | CNOT | Toffoli |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 288 | 35 | 325 | 245 |
| 6 | 8,162 | 1,083 | 10,122 | 7,518 |
| 24 | 122,815 | 13,708 | 149,408 | 114,936 |

These counts use abstract logical gates with arbitrary wire connectivity and retain the entire history. Phase synthesis, epoch-address selection and hardware compilation are separate open implementation tasks. The arithmetic circuit gives the coherent wrong seed \(-P_L\) exactly zero completed phase, so reversibility and source authentication alone supply no signed cancellation estimate.

Run the finite checks from this directory.

~~~sh
python -W error -m unittest -v test_bbp_reversible_oracle
~~~

**VERIFIED_FINITE.** The checks exhaust the 1,920 valid seeds at \(L=1\). They independently replay rational states, lift carries, and selected completed phases at \(L=2,6,11,24\), including zero, \(-P_L\), lattice boundary, and fixed-seed random controls. The next resource probe is an address-controlled, bounded-precision phase readout that preserves exact arithmetic evidence and reproduces both the zero-seed and coherent wrong-seed output.
