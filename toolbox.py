import os


def get_folders(folder):
    sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
    print('Reading...')
    try:
        print('     Removing unwanted folders.')
        sub_folders.remove('.idea')
        sub_folders.remove('venv')
        sub_folders.remove('__pycache__')
    except (Exception,):
        print('     No more folders to remove.')
        pass
    print('Folders:')
    print(f'    {sub_folders}')
    folder = input('Select a folder: ')

    path = sub_folders[sub_folders.index(folder)]

    return path


def rename_folders(path, sub_path):
    files = os.listdir(path)
    type_file = input(f'Type the files format, like [txt, mp4, jpeg] :')
    for index, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, f'{sub_path}'
                                                         .join([f'aula{str(int(index + 1))}-', f'.{type_file}'])))
