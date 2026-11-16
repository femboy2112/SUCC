import YM.UVExtension.Orchard.Barrel
namespace YM
def authenticatedValue : Nat := 7
theorem authenticatedValue_eq : authenticatedValue = 7 := rfl
end YM
namespace Vintage.YM
def authenticatedValue : Nat := 8
end Vintage.YM
vintage YM.authenticatedValue_eq
