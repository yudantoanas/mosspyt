from pathlib import Path
import os
import nbformat

with open("filePrefix.txt") as f:
    filePrefix = f.readline()

with open("usernames.txt") as f:
    repoNames = f.readlines()

[]

for name in repoNames:
    name = name.replace('\n', '')
    fileName = f"{filePrefix}_{name}"
    targetPath = f"sources/{name}/{fileName}.ipynb"

    try:
        nb = nbformat.read(targetPath, as_version=4)
    except:
        continue

    user_code = ''

    for cell in nb.cells:
        if cell.cell_type == 'code' and '# EXCLUDE THIS CELL' not in cell.source:
            user_code += cell.source + '\n\n'

    p = Path(targetPath)
    output_path = os.path.join("outputs", name + '.py')

    with open(output_path, mode='w', encoding='utf-8') as f:
        f.write(user_code)

    print(f'Extracted user code to {output_path}')
