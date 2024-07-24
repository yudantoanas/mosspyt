import shutil

def filesCopier(fileNames: list, sourceDir: str, outputDir: str):
    for fileName in fileNames:
        try:
            shutil.copyfile(f'{sourceDir}/{fileName}', f'{outputDir}/{fileName}')
        except FileNotFoundError as e:
            raise FileNotFoundError(e)
        else:
            print(f'Extracted user code to {outputDir}/{fileName}')
        
    return None