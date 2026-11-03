"""Build the reviewed thesis template with the installed latexmk executable."""
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
latexmk = shutil.which('latexmk')
if not latexmk:
    raise SystemExit('latexmk was not found. Install TeX Live with XeLaTeX, Biber and Chinese support.')
for folder in ['latex']:
    print(f'Building {folder}/main.tex', flush=True)
    result = subprocess.run([latexmk, '-xelatex', 'main.tex'], cwd=ROOT / folder)
    if result.returncode:
        sys.exit(result.returncode)
print('Thesis template built successfully.')
