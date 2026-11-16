import YM.UVExtension.Orchard.Barrel
namespace YM
def authenticatedValue : Nat := 7
theorem authenticatedValue_eq : authenticatedValue = 7 := rfl
end YM
namespace Vintage.YM
def authenticatedValue : Nat := 7
end Vintage.YM
vintage YM.authenticatedValue_eq
example : Vintage.YM.authenticatedValue = 7 := Vintage.YM.authenticatedValue_eq
#print Vintage.YM.authenticatedValue_eq
#print axioms Vintage.YM.authenticatedValue_eq
