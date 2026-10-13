#!/usr/bin/env python3
"""Reject proof placeholders/local axioms in the swarm's own Lean sources.

This lexical gate complements compilation; it does not audit imported mathlib.
Nested Lean block comments and line comments are ignored, as are string literals.
"""
from pathlib import Path
import re


def code_only(text):
    out = []
    i = depth = 0
    in_string = False
    while i < len(text):
        pair = text[i:i+2]
        if depth:
            if pair == '/-':
                depth += 1
                i += 2
            elif pair == '-/':
                depth -= 1
                i += 2
            else:
                i += 1
        elif in_string:
            if text[i] == '\\':
                i += 2
            elif text[i] == '"':
                in_string = False
                i += 1
            else:
                i += 1
        elif pair == '/-':
            depth = 1
            out.append(' ')
            i += 2
        elif pair == '--':
            end = text.find('\n', i)
            i = len(text) if end < 0 else end
        elif text[i] == '"':
            in_string = True
            out.append(' ')
            i += 1
        else:
            out.append(text[i])
            i += 1
    return ''.join(out)


def forbidden(text):
    return re.findall(r'\b(?:sorry|admit|axiom|unsafe)\b', code_only(text))


def main():
    assert forbidden('theorem bad : False := by sorry') == ['sorry']
    assert forbidden('axiom bad : False') == ['axiom']
    assert not forbidden('/- nested /- sorry -/ axiom -/ -- admit\n def s := "unsafe"')
    root = Path(__file__).resolve().parents[1]
    paths = sorted((root/'formal').glob('Swarm_*.lean'))
    paths += sorted((root/'formal/swarm_topology').glob('Swarm*.lean'))
    for path in paths:
        bad = forbidden(path.read_text())
        if bad:
            raise SystemExit(f'{path.relative_to(root)}: forbidden proof tokens {bad}')
    print(f'PASS: {len(paths)} own Lean files; placeholder/axiom mutation controls rejected.')


if __name__ == '__main__':
    main()
