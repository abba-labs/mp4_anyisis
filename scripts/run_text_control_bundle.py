"""Run the two mobile controls from the accompanying selective evidence bundle.

No workflow writes, credentials, package installation, or automatic model switch.
Use --preflight to validate without importing Paddle. A prepared Python 3.11
runtime is required for actual inference; the upstream engine may fetch models.
"""
from pathlib import Path
import hashlib
import json
import runpy
import sys


def main():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root/'bundle_manifest.json').read_text(encoding='utf-8'))
    for name, expected in manifest['files'].items():
        path = (root/name).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError(f'missing or nonlocal bundle member: {name}')
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError(f'bundle member changed: {name}')
    extra = sys.argv[1:]
    sys.path.insert(0, str(root/'src'))
    sys.argv = ['probe_saved_text_recognition.py', str(root/'baseline/sarc'),
                '--evidence', str(root/'docs/step11_evidence.json'),
                '--recognizer', 'mobile', *extra]
    if '--preflight' not in extra and not any(a in {'-o', '--output'} or a.startswith('--output=') for a in extra):
        sys.argv += ['-o', str(root/'results/mobile')]
    runpy.run_path(str(root/'scripts/probe_saved_text_recognition.py'), run_name='__main__')


if __name__ == '__main__':
    main()
