#!/bin/env python

import os

def get_user_input(prompt, default_value=None):
    if default_value is not None:
        full_prompt = f"{prompt} ({default_value}): "
        user_input = input(full_prompt).strip()
        return default_value if user_input == "" else user_input
    else:
        return input(f"{prompt}: ").strip()

def create_directory_if_missing(path):
    try:
        os.makedirs(path, exist_ok=True)
    except PermissionError:
        print(f"Permission denied: cannot create directory '{path}'.")
    except OSError as e:
        print(f"Error creating directory '{path}': {e}")

def append_to_file(file_path, content):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(content + '\n')

def remove_file_with_confirmation(file_path):
    import os

    if not os.path.isfile(file_path):
        return True

    confirmation = get_user_input(f"Are you sure you want to delete '{file_path}'? (y/n)", "n")

    if confirmation.lower() in ('y', 'yes'):
        try:
            os.remove(file_path)
            return True
        except PermissionError:
            print(f"Permission denied: cannot delete '{file_path}'.")
            return False
        except OSError as e:
            print(f"Error deleting file '{file_path}': {e}")
            return False
    else:
        print("File deletion cancelled.")
        return False

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    project_dir = get_user_input("Input project dir", "./../")
    bestf_dir = get_user_input("Input bestf dir", os.getcwd())
    os.chdir(project_dir)

    if not os.path.isfile("platformio.ini"):
        print("Not PlatformIO project!")

    create_directory_if_missing("test")
    remove_file_with_confirmation("test/test_custom_runner.py")
    remove_file_with_confirmation("test/bestf.h")

    append_to_file("test/bestf.h", "// +-------------------------------------------+\n"
                                   "// | BESTF: Best Framework for Arduino testing |\n"
                                   "// +-------------------------------------------+\n")
    append_to_file("test/bestf.h", "// This file is auto-generated, do not change it if you do not know what you are doing!")
    append_to_file("test/bestf.h", read_file(os.path.join(bestf_dir, "FOR_MACRO.h")))
    append_to_file("test/bestf.h", read_file(os.path.join(bestf_dir, "bestf.h")).replace('#include "FOR_MACRO.h"', "", 1))

    append_to_file("test/test_custom_runner.py", read_file(os.path.join(bestf_dir, "custom_test_runner.py")))

    print("Add the line `test_framework = custom` to the `platformio.ini` file in the appropriate section")
    print("End.")

if __name__ == "__main__":
    main()
