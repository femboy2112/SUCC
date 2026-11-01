"""Second route for finite path/source identities; does NOT import research model."""
from fractions import Fraction as F

def source_combined(n:int)->F:
    return F(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))

def state_convolution(n:int)->F:
    return sum((16**(n-j)*source_combined(j) for j in range(1,n+1)),F())

def action_convolution(n:int)->F:
    return sum((source_combined(j)/16**j for j in range(1,n+1)),F())

def directed_reference_path_weights()->dict[tuple[str,...],F]:
    return {
      ("A","hit"):F(3,8),
      ("A","miss"):F(1,8),
      ("B","hit"):F(1,8),
      ("B","miss"):F(1,8),
      ("B","sidetrack"):F(1,4),
    }

def target_gibbs_weights(lam:F)->dict[tuple[str,...],F]:
    x=directed_reference_path_weights()
    a=x[("A","hit")]
    b=x[("B","hit")]*lam**2
    return {( "A","hit"):a/(a+b),("B","hit"):b/(a+b)}

def two_step_affine_difference()->F:
    a=source_combined(1);b=source_combined(2)
    return F(15)*(a-b)

def basic_path_distribution():
    # Simple terminal-unconstrained fixed two-stage process, for KL control.
    return (F(1,2),F(1,2))
