# Round II source and ancestry reconstruction

Snapshot: 2026-10-19T00:12:03.698836+00:00. Default main: `610efacf02556e1c5922bc5d4e87d0087f19b446`.
The requested heads remain unchanged. None of the nine inspected draft heads is an ancestor of default main. PR base labels are not used as ancestry evidence.

| PR | Actual head | Other inspected heads that are ancestors |
|---|---|---|
| #161 | `eb62620300add80f8b38ebf0f7cd54c2a3c5ae36` | none |
| #169 | `64aa0810d9016c9c6948034d0543424f46db011e` | none |
| #171 | `8c46cca801b57a6381dfac08e41731ca70d38904` | none |
| #174 | `6fb1dba87ed273350a636b14b248fccacfb88934` | #171 |
| #175 | `8216c6fc042704aecd5fb7872facd681216e4be7` | #169 |
| #176 | `a17197697c0ea0259592500b233419fbedf691cf` | #169, #175 |
| #177 | `f309d9104ba480c1999c962af1df7c50f19e1bfe` | #171, #174 |
| #178 | `e42096ec0186228dd0f748767599e470f2ca2e1d` | none |
| #179 | `81684b4b8956f9f5da56c376ba7e4339277eb665` | #171, #174, #177 |

PR #179 is a newly discovered sibling continuation of #177. Its Gamma approximation already records a worsened signed lower bound; the signed stream inspects it to avoid repeating that route. #178 and #177 are incomparable continuations with common main ancestor. The new operator/causal branch descends only from #178; the signed branch descends only from #177. No whole-branch merge crosses this boundary.

All original worktrees remain in place. Raw snapshot includes exact file lists, PR bodies and current check records. Cancelled duplicate checks remain recorded; they are not converted into failures or successes. Zero duplicate whole-commit patch IDs is not evidence that there are no copied source files, derivations or shared premises.

The existing 72-entry provenance manifest and source blob identities remain unchanged. Source mathematical correctness is a separate obligation from byte identity.

Scope: this is an update of the #178 reconstruction, not a repeated audit of every theorem in drafts #153--179. The relevant source papers are read by their owning research streams, with the independent source map recorded in the resulting manuscripts.
