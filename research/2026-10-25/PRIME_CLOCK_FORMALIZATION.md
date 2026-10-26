# Complete-period contraction: checked finite Lean kernel

**Status: PROVED LOCAL (Lean 4.14.0 finite algebra).** This file supplies a
narrow formal authority for the prime-period compression used in the resonance
round. It does not formalize prime arithmetic, complex Hilbert orthogonality,
BGK, the authentic BBP source, an asymptotic estimate, or pi normality.

The verified input branch was PR #296 at
`461942c0bf616518e668d236d1c6b1596665a7dd`.

## Exact formal statements

[`formal/PrimeClockProjection.lean`](../../formal/PrimeClockProjection.lean)
uses only `Std.Tactic`. Its explicit `SumAlgebra` coefficient hypotheses are:
commutative associative addition with zero, and a multiplication satisfying
`a*0=0` and `a*(b+c)=a*b+a*c`. The file supplies an integer instance so those
hypotheses have an explicit model. They are parameters of the theorems, not
new global Lean axioms.

For all natural B,L, coefficient sequences u,v, and the **finite** hypothesis

    u(b*L+j)=u(j), for every b<B and j<L,

`periodic_contraction` proves

    sum_(t<B*L) u(t)*v(t)
      = sum_(j<L) u(j) * sum_(b<B) v(b*L+j).

`zero_fiber_annihilation` proves that if every inner complementary sum is
zero, the complete selected sum is zero. `equal_fibers_equal_coupling` proves
that any two complementary vectors with equal fiber sums give the same
selected sum. Thus all within-fiber zero-sum information is formally invisible
to any clock satisfying the stated repetition law.

Auxiliary checked lemmas include finite bounded congruence, distributivity,
Fubini, concatenation of adjacent intervals, and the full block decomposition
of `[0,B*L)`. No lost endpoint is hidden in the passage from t to (b,j).

For B,L positive, interpreting the same finite identity in complex arithmetic
and dividing by B*L gives the paper's average identity

    W/(B*L) = (1/L) sum_(j<L) u(j) * ((1/B) sum_(b<B) v(j+b*L)).

**Authority boundary:** the checked code is polymorphic over the explicitly
specified algebra. It does not import a Lean complex-number library or check
a complex-number instance of `SumAlgebra`; nor does it formalize division or
the normalized Hilbert projection. Those are ordinary paper steps, separated
from the finite theorem above. B=0 or L=0 is accepted by the sum theorem but
cannot be used for its normalized interpretation.

## Observed verification and mutation control

The official Lean 4.14.0 Linux binary reports:

    Lean (version 4.14.0, x86_64-unknown-linux-gnu,
          commit 410fab728470, Release)

The final file compiled with exit code 0. Its three principal `#print axioms`
outputs contain exactly `[propext, Quot.sound]`; no `sorryAx`, choice axiom,
external theorem postulate, or new axiom is used by those proofs.

A separate uncommitted mutation changed the compressed clock coefficient
from `u j` to `u (j+1)` in the claimed contraction, leaving the original proof
and hypotheses intact. Lean rejected it with exit code 1 and the explicit
unproved equality

    u j * fiberSum = u (j+1) * fiberSum.

This is a failure control for index preservation, not an independent proof of
the original theorem. The erroneous temporary mutant is not imported.

Checked source SHA-256:

    ba49c1216ecfa89d18d75fe2a91ec378e04c592bfe8efed386da49e6674640a1

Official archive:
<https://github.com/leanprover/lean4/releases/download/v4.14.0/lean-4.14.0-linux.tar.zst>

Downloaded archive SHA-256 (recorded, not compared with a signed upstream digest):

    320f18e7d58271d95fced740522b5a5ed41b85b2af5bf0e8ab9a8dbc380e450a

Ordinary replay from the repository root:

```sh
lean --version
lean formal/PrimeClockProjection.lean
```

## Runtime compatibility detail

This execution environment allowed `/proc/self/exe` but denied the equivalent
`/proc/<current-numeric-pid>/exe` query used by Lean 4.14. Consequently even
`lean --version` initially failed with `error: failed to locate application`.
An isolated local preload shim translated **only the current process's own
executable query** to `/proc/self/exe`; all other `readlink` calls were forwarded
unchanged. The compiler binary, its kernel, and libraries were unmodified.
This shim performed path discovery only; it supplied no theorem results.

The exact compatibility shim was:

```c
#define _GNU_SOURCE
#include <dlfcn.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
ssize_t readlink(const char *path, char *buf, size_t size) {
  static ssize_t (*real_readlink)(const char *, char *, size_t);
  if (!real_readlink) real_readlink = dlsym(RTLD_NEXT, "readlink");
  char own_exe[64];
  snprintf(own_exe, sizeof own_exe, "/proc/%d/exe", getpid());
  return real_readlink(strcmp(path, own_exe) == 0 ? "/proc/self/exe" : path,
                       buf, size);
}
```

It was built using `gcc -shared -fPIC ... -ldl` and supplied via `LD_PRELOAD`.
A normal machine does not require this compatibility step. No shared build
configuration or existing formal source was changed.

## Remaining proof obligation

Complete-period contraction is an exact reduction, not a cancellation bound.
The finite anti-phase complement still survives it. A proof of decay must
bound the authenticated compressed complementary vector's interaction with
the prime clock using additional arithmetic; formal reindexing does not
establish that estimate.
