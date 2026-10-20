import Lean.Elab.Command
import Lean.Elab.Print
import Lean.Util.CollectAxioms

/- Kernel-environment export, used after building the exact local theorem sources.
The raw Expr contains every binder, hypothesis and conclusion. An English label
is never a proposition identifier. The enclosing build record is not self-authenticating.
-/
open Lean Elab Command

elab "#succ_export " id:ident : command => do
  let names ← liftCoreM <| realizeGlobalConstWithInfos id
  if names.length != 1 then
    throwError "expected one fully qualified theorem name"
  for name in names do
    let ci ← getConstInfo name
    match ci with
    | .thmInfo _ => pure ()
    | _ => throwError "exported declaration is not a theorem: {name}"
    let axioms ← collectAxioms name
    let record := Json.mkObj [
      ("name", toJson name.toString),
      ("type_expr", toJson (reprStr ci.type)),
      ("universe_parameters", toJson (ci.levelParams.map Name.toString)),
      ("axioms", toJson ((axioms.qsort Name.lt).toList.map Name.toString))]
    logInfo m!"SUCC_THEOREM_JSON {record.compress}"
