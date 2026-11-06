# Front A/H preregistration

Pinned inherited source: c9dfcdf057c4870f113e898464e4821c2ff5fedf;
Gamma Prybar parent: af5c7ba30ea57d725bd334310798357d50f12fce.
No original source, contract, seed, or historical proof is edited.

Before the new probes run, the candidate is the all-derivative tail bound

`0 < (k+1)!/(64 x^(k+2)) - (-1)^k T^(k)(x)
   < 7(k+2)!/(1024 x^(k+3))`, for x>0 and integer k>=0.

The companion exact-tail discrete chirp candidate is

`M_A^(-pi/16)(H)=256/(pi Lambda)+O(Lambda^-2+A^-1)`

uniformly for integer A>=4 and H with `1<=Lambda=H/A²<=A`.
It would extend the coherent asymptotic to `Lambda->infinity`, `Lambda/A->0`.
This is a same-forcing changed-seed obstruction, not a zero-seed saving.

Fresh rational checks use n in {17,193,1021} and k in {0,1,2,3,4,5}.
Two term-derivative implementations are used: the four signed poles and the
expanded positive Mellin polynomial. They share BBP provenance. Infinite
remainders receive exact monotone bounds; floating-point agreement is not a
certificate. Every bound must contain the full interval with strict endpoints.
Known controls: k=0 recovers the old CC-01; the new coefficient 7/512 must be
smaller than 1/64. Negative source mutation drops the fourth pole and must fail
at least one original-source bound. Original zero seed and fixed coherent seed
are never identified. Passing finitely many cases validates instrumentation,
not the quantified theorem.

No numerical search will be used to infer the 256/pi constant. A paper proof
will use exact discrete summation by parts and an independently checked Laplace
moment bound. The first selected-source obstacle will be recorded explicitly.
