from toolbox import get_folders, rename_folders

root_path = get_folders("./")
sub_path = get_folders(root_path)

path = f'{root_path}/{sub_path}'
user_option = input('Do you want the files with index: (Type yes or no)\n')
user_option = user_option.lower()
rename_folders(path, sub_path, user_option)
print("Done!")
