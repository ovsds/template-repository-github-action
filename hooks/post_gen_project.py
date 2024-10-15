#!/usr/bin/env python
import pathlib
import shutil


def remove_folder(folder_path: str) -> None:
    folder = pathlib.Path(folder_path)
    shutil.rmtree(folder)


def remove_file(file_path: str, missing_ok: bool = False) -> None:
    file = pathlib.Path(file_path)
    file.unlink(missing_ok=missing_ok)


if __name__ == "__main__":
    if "{{ cookiecutter.action_type }}" != "node20":
        remove_folder("src")
        remove_folder("tests")
        remove_file(".eslintignore")
        remove_file(".eslintrc.json")
        remove_file(".prettierignore")
        remove_file("tsconfig.json")
        remove_file("tsconfig_eslint.json")
        remove_file("vitest.config.ts")

    # Remove files from older versions
    remove_file(".husky/.huskyrc", missing_ok=True)
