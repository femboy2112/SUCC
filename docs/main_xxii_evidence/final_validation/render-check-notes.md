# GitHub rendering instrument record

Actual branch pages were loaded in Chromium at 1440px and 390px widths, with full-page screenshots. Both page document widths matched the viewport; formulas were visible in browser inspection.

Initial browser scroll failed because GitHub hydration detached the article element. Waiting for hydration before obtaining and scrolling the article locator corrected the probe. The failed tool output remains in the session; it is not a document-rendering failure.

An initial DOM verifier incorrectly required a shadowRoot and flagged every formula although each had a rendered light-DOM MathML node. The corrected probe requires a math node and rejects merror. Its repeat found 4/4 README and 45/45 frontier formulas rendered, with no merror. The initial JSON was overwritten by the corrected repeat; no initial JSON artifact is claimed. Browser output and this note preserve the instrument correction.

GitHub Markdown API receipts are distinct from visual client inspection. API tag counts include opening and closing tags (8 and90); actual formula counts were4 and45. The final documentation-only source/recurrence split requires one more repeat after push.

Final repeat at exact commit33b18ae61478c346550b12e6c84ca7d8481c6bad completed:5/5 README and46/46 frontier formulas have MathML with no merror; all four viewport document-width checks pass. Final screenshots are retained with their exact-commit URLs in github-render.json.
