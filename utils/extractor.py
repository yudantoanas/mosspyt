import os
import pathlib

import nbformat


def notebook_extractor(data: dict):
    for file_name in data['paths']:
        try:
            # read notebook file
            nb = nbformat.read(f"clone/{file_name}", as_version=4)
        except Exception as e:
            print(e)
            continue

        # extract code from cell
        user_code = ''
        for cell in nb.cells:
            # only reads cell with type 'code'
            if cell.cell_type == 'code':
                # append code strings
                user_code += cell.source + '\n\n'

        # generate output file
        output_path = os.path.join(
            "moss",  # folder name in current directory
            f"{pathlib.Path(file_name).stem}.py"  # extract filename from extension
        )

        with open(output_path, mode='w', encoding='utf-8') as f:
            f.write(user_code)

    return None
