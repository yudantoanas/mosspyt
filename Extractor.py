from pathlib import Path
import os
import nbformat
import shutil

def scriptExtractor(filePaths: list):
    for path in filePaths:
        shutil.copyfile(f'./{path.split('/')[1]}', f'./outputs/{path.split('/')[1]}')
        print(f'Extracted user code to ./outputs/{path.split('/')[1]}')

def notebookExtractor(filePaths: list):
    for path in filePaths:
        try:
            # read notebook file
            nb = nbformat.read(path, as_version=4)
        except Exception as e:
            print(e)
            continue

        # extract code from cell
        user_code = ''
        for cell in nb.cells:
            # only reads cell with type code and not having "# EXCLUDE THIS CELL" flag
            if cell.cell_type == 'code' and '# EXCLUDE THIS CELL' not in cell.source:
                user_code += cell.source + '\n\n'

        # generate output file
        output_path = os.path.join(
            "outputs", # folder name in current directory
            path.split('/')[1] + '.py' # file name
        )
        with open(output_path, mode='w', encoding='utf-8') as f:
            f.write(user_code)
        
        print(f'Extracted user code to {output_path}')