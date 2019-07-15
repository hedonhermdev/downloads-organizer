from downloadsorganizer.attributes import DOWNLOADS_DIRECTORY
from downloadsorganizer.funcs import print_os_info, change_working_directory, list_all_files, sort_files_by_type, \
    move_files_to_folders



def main():
    dl_dir = DOWNLOADS_DIRECTORY
    print_os_info()
    print(f'DOWNLOADS DIRECTORY: {dl_dir}')
    change_working_directory(dl_dir)
    download_files = list_all_files(dl_dir)
    files_sorted = sort_files_by_type(download_files)
    move_files_to_folders(files_sorted)
    print('DONE!')


if __name__ == '__main__':
    main()
