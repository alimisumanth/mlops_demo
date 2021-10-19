import os

dirs = [
    os.path.join('data', 'raw'),
    os.path.join('data', 'processed'),
    'notebooks',
    'src']

files = [
    'params.yaml',
    'dvc.yaml',
    '.gitignore',
    os.path.join('src', '__init__.py')
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), 'w') as d:
        pass

for file in files:
    with open(file, 'w') as f:
        pass