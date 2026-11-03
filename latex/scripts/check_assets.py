"""Check active TeX inputs, images, bibliography files, and citation keys.

Run from any directory: python scripts/check_assets.py main|example
Only Python's standard library is required. Optional private signatures are skipped.
"""
from pathlib import Path
import argparse
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def uncomment(text):
    text = re.sub(r'\\begin\{(lstlisting|verbatim)\}.*?\\end\{\1\}', '', text, flags=re.S)
    text = re.sub(r'\\verb(.).*?\1', '', text)
    return '\n'.join(re.split(r'(?<!\\)%', line, maxsplit=1)[0] for line in text.splitlines())


def check(entry):
    errors = []
    visited = set()
    texts = []
    start = ROOT / f'{entry}.tex'
    if not start.is_file():
        return [f'Missing entry: {entry}.tex'], 0, 0
    entry_text = uncomment(start.read_text(encoding='utf-8'))
    variables = dict(re.findall(r'\\newcommand\{\\(\w+)\}\{([^{}]+)\}', entry_text))

    def locate(raw, extensions=('',)):
        if raw.startswith('\\'):
            raw = variables.get(raw[1:], raw)
        candidate = (ROOT / raw).resolve()
        if not candidate.is_relative_to(ROOT):
            errors.append(f'Path escapes project: {raw}')
            return None
        for suffix in extensions:
            p = Path(str(candidate) + suffix)
            if p.is_file():
                # Enforce exact case even when this runs on Windows.
                parent = ROOT
                for part in p.relative_to(ROOT).parts:
                    if part not in {x.name for x in parent.iterdir()}:
                        errors.append(f'Filename case mismatch: {raw}')
                        break
                    parent /= part
                return p
        errors.append(f'Missing file: {raw}')
        return None

    def visit(path):
        if path in visited:
            return
        visited.add(path)
        text = uncomment(path.read_text(encoding='utf-8'))
        texts.append(text)
        for raw in re.findall(r'\\(?:input|include)\{([^}]+)\}', text):
            p = locate(raw, ('', '.tex'))
            if p:
                visit(p)
        for raw in re.findall(r'\\(?:includegraphics|thesisImage)(?:\[[^\]]*\])?\{([^}]+)\}', text):
            # Definitions containing #1 / #2 are not actual resource references.
            if '#' not in raw:
                locate(raw, ('', '.pdf', '.png', '.jpg', '.jpeg'))

    visit(start)
    if re.search(r'\\documentclass(?:\[[^\]]*\])?\{HZAU\}', entry_text):
        locate('HZAU.cls')
    keys = set()
    for text in texts:
        for raw in re.findall(r'\\addbibresource(?:\[[^\]]*\])?\{([^}]+)\}', text):
            p = locate(raw)
            if p:
                keys.update(re.findall(r'@\w+\s*\{\s*([^,\s]+)\s*,', p.read_text(encoding='utf-8')))
    cited = set()
    for text in texts:
        for raw in re.findall(r'\\(?:cite|parencite|textcite|citep|citet)\*?(?:\[[^\]]*\])*\{([^}]+)\}', text):
            cited.update(k.strip() for k in raw.split(',') if '#' not in k)
    for key in sorted(cited - keys):
        errors.append(f'Undefined citation: {key}')
    return sorted(set(errors)), len(visited), len(cited)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('entry', choices=['main'])
    args = parser.parse_args()
    problems, files, citations = check(args.entry)
    for problem in problems:
        print(problem)
    print(f'{args.entry}: {files} TeX files; {citations} citation keys; {len(problems)} problem(s).')
    sys.exit(1 if problems else 0)
