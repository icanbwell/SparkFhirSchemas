# type: ignore
# This file implements the code generator for generating schema and resolvers for FHIR
# It reads the FHIR XML schema and generates resolvers in the resolvers folder and schema in the schema folder
import dataclasses
import json
import os
import shutil
from pathlib import Path
from typing import List, Union

from fhir_xml_schema_parser import FhirXmlSchemaParser
from fhir_xml_schema_parser import FhirEntity


def my_copytree(
    src: Union[Path, str],
    dst: Union[Path, str],
    symlinks: bool = False,
    # ignore: Union[
    #     None,
    #     Callable[[str, List[str]], Iterable[str]],
    #     Callable[[Union[str, os.PathLike[str]], List[str]], Iterable[str]],
    # ] = None,
) -> None:
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks)
        else:
            shutil.copy2(s, d)


def clean_duplicate_lines(file_path: Union[Path, str]) -> None:
    print(f"Removing duplicate lines from {file_path}")
    with open(file_path, "r") as file:
        lines: List[str] = file.readlines()
    new_lines: List[str] = []
    for line in lines:
        if not line.strip() or not line.lstrip().startswith("from"):
            new_lines.append(line)
        elif line not in new_lines and line.lstrip() not in [
            c.lstrip() for c in new_lines
        ]:
            new_lines.append(line)
    with open(file_path, "w") as file:
        file.writelines(new_lines)


def main() -> int:
    data_dir: Path = Path(__file__).parent.joinpath("./")
    classes_dir: Path = data_dir.joinpath("./")

    schema_file_path = classes_dir.joinpath("myschema.json")
    if os.path.exists(schema_file_path):
        os.remove(schema_file_path)

    schema_pickle_file_path = classes_dir.joinpath("myschema_pickle.json")
    if os.path.exists(schema_pickle_file_path):
        os.remove(schema_pickle_file_path)

    fhir_entities: List[FhirEntity] = FhirXmlSchemaParser.generate_classes()

    # subclass JSONEncoder
    class EnhancedJSONEncoder(json.JSONEncoder):
        def default(self, o):
            if dataclasses.is_dataclass(o):
                return dataclasses.asdict(o)
            if isinstance(
                o, set
            ):  # https://bobbyhadz.com/blog/python-typeerror-object-of-type-set-is-not-json-serializable
                return list(o)
            return super().default(o)

    #
    employeeJSONData = json.dumps(fhir_entities, cls=EnhancedJSONEncoder)
    with open(schema_file_path, "w") as file2:
        file2.write(employeeJSONData)

    import jsonpickle

    frozen = jsonpickle.encode(fhir_entities)
    with open(schema_pickle_file_path, "w") as file2:
        file2.write(frozen)

    return 0


if __name__ == "__main__":
    exit(main())
