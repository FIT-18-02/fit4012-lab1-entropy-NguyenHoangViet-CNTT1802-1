from pathlib import Path
import subprocess
import sys
import re

root = Path('.')
errors = []
warnings = []

required_files = [
    'README.md',
    'report-page.md',
    'src/entropy_redundancy.cpp',
    'src/mod_inverse.cpp',
    'tests/test_cases.md',
    'logs/run_log.md',
]

for rel in required_files:
    if not (root / rel).exists():
        errors.append(f'Thieu file bat buoc: {rel}')

if errors:
    for e in errors:
        print(f'::error::{e}')
    sys.exit(1)

entropy_code = (root / 'src/entropy_redundancy.cpp').read_text(encoding='utf-8')
modinv_code = (root / 'src/mod_inverse.cpp').read_text(encoding='utf-8')

if 'TODO(student)' in entropy_code:
    errors.append('src/entropy_redundancy.cpp van con TODO(student).')
if 'TODO(student)' in modinv_code:
    errors.append('src/mod_inverse.cpp van con TODO(student).')

if 'return -1.0;' in entropy_code:
    errors.append('calculate_redundancy() chua duoc hoan thien.')
if re.search(r'int\s+mod_inverse\s*\([^)]*\)\s*\{[^}]*return\s+-1\s*;', modinv_code, flags=re.DOTALL):
    errors.append('mod_inverse() chua duoc hoan thien.')

if errors:
    for e in errors:
        print(f'::error::{e}')
    sys.exit(1)

print('::notice::FIT4012 Buổi 2 auto check passed.')
