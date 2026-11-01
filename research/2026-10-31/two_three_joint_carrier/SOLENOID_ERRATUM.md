# Erratum to inherited Atom-3 {2,3}-solenoid finite/global duality argument

**2026-10-31. Additive repair; do not edit the originating historical source.** Refers to
research/2026-10-27-ravel-prime-ladder/ATOM3_TWO_THREE_SOLENOID.md §2,
inherited source archive (not modified). The intended classical result
\(\widehat{X_{2,3}}\simeq\mathbb Z[1/6]\) is CORRECT, but the specific
intermediate duality and interpretation in that archived dossier are FALSE.

## Error 1 — a circle is not its finite cyclic integer subgroup

The archive writes \(\widehat{\mathbb R/N\mathbb Z}\cong
\mathbb Z/N\mathbb Z\). **REFUTED.** For any N≥1,
\[
\widehat{\mathbb R/N\mathbb Z}=
\{\,x\mapsto\exp(2\pi i kx/N):k\in\mathbb Z\,\}
\simeq (1/N)\mathbb Z\simeq\mathbb Z.
\]
The finite subgroup of integer points \(\mathbb Z/N\mathbb Z\)
embedded in this circle does have finite dual \(\mathbb Z/N\mathbb Z\).
But restricting all circle characters to the integer subgroup loses
infinitely many modes: \(k=0\) and \(k=N\) agree at all integer points,
but at \(x=1/2\) their phases are respectively \(0\) and \(1/2\) mod1.
This is a literal finite→continuum source-map information loss.

With N=2^a3^b, the correct directed system of **circle character lattices**
is \((1/N)\mathbb Z\) under natural inclusions, whose union is
\(\mathbb Z[1/6]\), torsion-free. The finite character groups
\((1/N)\mathbb Z/\mathbb Z\cong\mathbb Z/N\mathbb Z\) instead have union
\(\mathbb Z[1/6]/\mathbb Z\), a **torsion** group. Its Pontryagin dual is
the profinite group \(\mathbb Z_2\times\mathbb Z_3\), NOT the connected
solenoid. Using the finite direct limit to assert the connected solenoid's
dual conflates two completely different carriers.

**Correct proof:** The solenoid is the inverse limit of actual connected
circles \(\mathbb R/N\mathbb Z\), with quotient bonding maps for divisibility.
Pontryagin duality turns this into the direct limit of their full infinite
lattices \((1/N)\mathbb Z\). That colimit is \(\mathbb Z[1/6]\). The associated
compact dual is connected because its dual is torsion-free. No finite
self-duality is substituted for a circle.

## Error 2 — unit action is not coordinate identity

The archived dossier states that multiplication ×16 only moves the 2-adic
factor, and ×3 only moves the 3-adic factor. **REFUTED as a literal
coordinate action.** Multiplication by 16 on Q₃ is invertible but not
identity (16≡7 mod9); multiplication by 3 on Q₂ is invertible but not
identity (3≡3 mod8). Both also act on the real coordinate. What is correct
is the complementary **valuations**:
\(v_2(16)=4,v_3(16)=0;\ v_2(3)=0,v_3(3)=1\).
This creates multiplicative rank two in the S-arithmetic solenoid, but
neither stochastic independence nor Haar selected orbit statistics follows.

## Scope, controls, and repair

- Positive: finite CRT self-duality for Z/NZ is correct; the global solenoid
  character group Z[1/6] and the rank-two nature of ×16×3 remain correct.
- Negative: using finite character colimits loses integer spectral modes;
  claiming the two multipliers act trivially on complementary local fields
  misstates the actual action.
- Exact regression: compare k=0 and k=N on integer points and on real
  x=1/2, and compare 16 modulo 9, 3 modulo 8.
- All source/normality claims keep their original statuses. Nothing here
  repairs π-selected ×3 invariance or proves Furstenberg's conjecture.

Classical context: Pontryagin duality for solenoids; e.g.
https://ems.press/content/serial-article-files/37049 and existing SUCC
docs/CLAIM_SUPPLEMENT_ADELIC_SOLENOID_POISSON.md.
