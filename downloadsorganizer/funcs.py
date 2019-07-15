import os
import platform
import shutil
from downloadsorganizer.helpers import pretty_print
from downloadsorganizer.attributes import EXTENSIONS_DICT


def print_os_info():
    """
    Print the OS name and version. 
    """
    pretty_print(f'Running on: {platform.system()} {platform.release()}')


def change_working_directory(new_directory):
    """
    Change the current working directory to the given directory if it exists, else raise an error.
    """
    if os.path.exists(new_directory):
        os.chdir(new_directory)
    else:
        raise NotADirectoryError(f"The given directory ({new_directory}) oes not exist!")


def list_all_files(directory):
    """
    Given the path to a directory, list all files (excluding directories) in the directory. 
    """
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def get_file_extension(file):
    return os.path.splitext(file)[1].lower()


def sort_files_by_type(files_list):
    """
    Given a list of filenames, return a dictionary that lists the files according to filetype. 
    """
    files_by_type = {ftype: [] for ftype in EXTENSIONS_DICT.keys()}
    for file in files_list:
        for ftype in files_by_type.keys():
            if get_file_extension(file) in EXTENSIONS_DICT[ftype]:
                files_by_type[ftype].append(file)

    return files_by_type


def make_new_directory(name):
    """
    Make new directory with given name. If directory already exists, do nothing. 
    """
    try:
        os.mkdir(name)
    except FileExistsError:
        pass


def move_files_to_folders(sorted_files_dict: dict):
    for ftype in sorted_files_dict.keys():
        make_new_directory(ftype.upper())
        for file in sorted_files_dict[ftype]:
            src = os.path.abspath(file)
            dst = os.path.join(os.path.abspath(ftype.upper()), file)
            shutil.move(src, dst)
