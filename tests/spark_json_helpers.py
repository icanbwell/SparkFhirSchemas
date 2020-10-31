from json import dumps
from json import loads
from os import makedirs
from pathlib import Path
from typing import Any


# noinspection SpellCheckingInspection
def create_jsonl_files(
    src_file: Path, dst_folder: Path, dst_file_name: str
) -> Path:
    with open(src_file, "r") as file:
        json_object: Any = loads(file.read())
    json_text: str = dumps(obj=json_object, separators=(',', ':'))
    makedirs(dst_folder)
    minified_json_path: Path = dst_folder.joinpath(dst_file_name)
    with open(minified_json_path, "w+") as file:
        file.write(json_text)
    return minified_json_path
