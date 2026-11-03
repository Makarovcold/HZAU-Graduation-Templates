"""Check thesis inputs, pictures and citations using only the standard library."""
from pathlib import Path
import importlib.util
import sys

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('asset_checker', ROOT / 'latex/scripts/check_assets.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)
problems = 0
for folder in ['latex']:
    checker.ROOT = (ROOT / folder).resolve()
    errors, files, citations = checker.check('main')
    print(f'{folder}: {files} TeX files; {citations} citation keys; {len(errors)} problem(s).')
    for error in errors:
        print('  ' + error)
    problems += len(errors)
sys.exit(1 if problems else 0)
