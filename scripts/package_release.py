"""Package the reviewed thesis template and the two PowerPoint template sets."""
from pathlib import Path
import argparse
import zipfile

ROOT = Path(__file__).resolve().parents[1]
EXTENSIONS = {'.tex', '.sty', '.cls', '.bib', '.md', '.py', '.png', '.jpg', '.jpeg', '.pdf', '.json', '.yml', '.yaml', '.pptx', '.potx'}
SPECIAL = {'.gitignore', '.gitattributes', 'latexmkrc'}
STAGES = {'latex': 'Thesis'}
PUBLIC_DIRS = {'latex', 'ppt', 'docs', 'scripts', '.github'}


def public(path):
    rel = path.relative_to(ROOT)
    if len(rel.parts) > 1 and rel.parts[0] not in PUBLIC_DIRS:
        return False
    if any(part.startswith('.') and part not in {'.github', '.vscode'} for part in rel.parts[:-1]):
        return False
    if path.is_symlink() or '__pycache__' in rel.parts or path.name.startswith('~$'):
        return False
    if path.stem.lower() in {'author_signature', 'mentor_signature'}:
        return False
    if 'private' in rel.parts and path.name != 'README.md':
        return False
    if 'original' in rel.parts and path.suffix.lower() == '.pdf':
        return False
    if rel.parts[0] in STAGES and rel.as_posix() == rel.parts[0] + '/main.pdf':
        return False
    return path.suffix.lower() in EXTENSIONS or path.name in SPECIAL


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    stage_outputs = {folder: output.with_name(output.stem + '-' + label + '-Overleaf.zip') for folder, label in STAGES.items()}
    for dest in [output, *stage_outputs.values()]:
        if dest.is_relative_to(ROOT):
            raise ValueError('Place archives outside the source project')
        if dest.exists():
            raise FileExistsError(dest)
    paths = sorted(p for p in ROOT.rglob('*') if p.is_file() and public(p))
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
        for p in paths:
            archive.write(p, p.relative_to(ROOT).as_posix())
    for folder, dest in stage_outputs.items():
        with zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED) as archive:
            for p in paths:
                if p.is_relative_to(ROOT / folder):
                    archive.write(p, p.relative_to(ROOT / folder).as_posix())
    print(f'GitHub: {output}')
    for folder, dest in stage_outputs.items():
        print(f'{folder} Overleaf: {dest}')


if __name__ == '__main__':
    main()
