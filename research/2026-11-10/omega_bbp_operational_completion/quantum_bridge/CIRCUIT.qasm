OPENQASM 3.0;
include "stdgates.inc";
// Explicit five-qubit parity-character monodromy interferometer.
// b[0] is least significant bit; b[3] is most significant.
// qasm3 parser not installed in the source-review environment; the
// corresponding 32-entry controlled-increment truth table is tested separately.
qubit[4] b;
qubit c;
bit result;

// |0001> -> |chi_8>=H^(tensor 4)|0001>.
x b[0];
h b[0];
h b[1];
h b[2];
h b[3];

// Prepare path reference |+>.
h c;

// Controlled increment modulo 16, high carry before low-bit mutation.
// When c=0 leaves all b untouched; when c=1 implements S|k>=|k+1 mod16>.
ctrl(4) @ x c, b[0], b[1], b[2], b[3];
ctrl(3) @ x c, b[0], b[1], b[2];
ccx c, b[0], b[1];
cx c, b[0];

// Parity eigenphase -1 sends the path |+> to |->, so the result is 1.
h c;
result = measure c;
