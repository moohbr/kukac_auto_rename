from toolbox import get_folders, rename_folders

root_path = get_folders("./")
sub_path = get_folders(root_path)

path = f'{root_path}/{sub_path}'

rename_folders(path, sub_path)
print("Done!")
