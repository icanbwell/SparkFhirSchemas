# type: ignore
# This file implements the code generator for generating schema and resolvers for FHIR
# It reads the FHIR XML schema and generates resolvers in the resolvers folder and schema in the schema folder
import os
import shutil
from os import path
from pathlib import Path
from typing import List, Union

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

    # clean out old stuff
    classes_resources_folder = classes_dir.joinpath("resources")
    if os.path.exists(classes_resources_folder):
        shutil.rmtree(classes_resources_folder)
    os.mkdir(classes_resources_folder)
    classes_resources_folder.joinpath("__init__.py").touch()

    classes_simple_types_folder = classes_dir.joinpath("simple_types")
    if os.path.exists(classes_simple_types_folder):
        shutil.rmtree(classes_simple_types_folder)
    os.mkdir(classes_simple_types_folder)
    classes_simple_types_folder.joinpath("__init__.py").touch()

    classes_complex_types_folder = classes_dir.joinpath("complex_types")
    if os.path.exists(classes_complex_types_folder):
        shutil.rmtree(classes_complex_types_folder)
    os.mkdir(classes_complex_types_folder)
    classes_complex_types_folder.joinpath("__init__.py").touch()

    classes_backbone_elements_folder = classes_dir.joinpath("backbone_elements")
    if os.path.exists(classes_backbone_elements_folder):
        shutil.rmtree(classes_backbone_elements_folder)
    os.mkdir(classes_backbone_elements_folder)
    classes_backbone_elements_folder.joinpath("__init__.py").touch()

    # schema_file_path = classes_dir.joinpath("myschema.json")

    schema_pickle_file_path = classes_dir.joinpath("myschema_pickle.json")

    import jsonpickle

    with open(schema_pickle_file_path, "r") as file2:
        contents = file2.read()
    fhir_entities: List[FhirEntity] = jsonpickle.decode(contents)
    resource_types_fhir_name: List[str] = []

    # now print the result
    for fhir_entity in fhir_entities:
        # use template to generate new code files
        resource_name: str = fhir_entity.cleaned_name
        entity_file_name = fhir_entity.name_snake_case
        if fhir_entity.is_value_set:  # valueset
            pass
            # with open(data_dir.joinpath("template.value_set.jinja2"), "r") as file:
            #     template_contents = file.read()
            #     from jinja2 import Template
            #
            #     file_path = value_sets_folder.joinpath(f"{entity_file_name}.graphql")
            #     print(f"Writing value_set: {entity_file_name} to {file_path}...")
            #     template = Template(
            #         template_contents, trim_blocks=True, lstrip_blocks=True
            #     )
            #     result = template.render(
            #         fhir_entity=fhir_entity,
            #     )
            #
            # if not path.exists(file_path):
            #     with open(file_path, "w") as file2:
            #         file2.write(result)
        elif fhir_entity.is_resource:
            resource_types_fhir_name.append(resource_name)
            # write Javascript classes
            with open(data_dir.joinpath("template.jinja2"), "r") as file:
                template_contents = file.read()
                from jinja2 import Template

                file_path = classes_resources_folder.joinpath(
                    f"{entity_file_name.lower()}.py"
                )
                print(f"Writing domain resource: {entity_file_name} to {file_path}...")
                template = Template(
                    template_contents, trim_blocks=True, lstrip_blocks=True
                )
                result = template.render(fhir_entity=fhir_entity)
            if not path.exists(file_path):
                with open(file_path, "w") as file2:
                    file2.write(result)
        elif fhir_entity.type_ == "BackboneElement" or fhir_entity.is_back_bone_element:
            with open(data_dir.joinpath("template.jinja2"), "r") as file:
                template_contents = file.read()
                from jinja2 import Template

                file_path = classes_backbone_elements_folder.joinpath(
                    f"{entity_file_name.lower()}.py"
                )
                print(f"Writing back bone class: {entity_file_name} to {file_path}...")
                template = Template(
                    template_contents, trim_blocks=True, lstrip_blocks=True
                )
                result = template.render(
                    fhir_entity=fhir_entity,
                )
            if not path.exists(file_path):
                with open(file_path, "w") as file2:
                    file2.write(result)
        elif fhir_entity.is_extension:  # valueset
            # write Javascript classes
            with open(data_dir.joinpath("template.jinja2"), "r") as file:
                template_contents = file.read()
                from jinja2 import Template

                file_path = classes_complex_types_folder.joinpath(
                    f"{entity_file_name.lower()}.py"
                )
                print(f"Writing complex type: {entity_file_name} to {file_path}...")
                template = Template(
                    template_contents, trim_blocks=True, lstrip_blocks=True
                )
                result = template.render(
                    fhir_entity=fhir_entity,
                )
            if not path.exists(file_path):
                with open(file_path, "w") as file2:
                    file2.write(result)
        elif not fhir_entity.is_basic_type:
            # write Javascript classes
            with open(data_dir.joinpath("template.jinja2"), "r") as file:
                template_contents = file.read()
                from jinja2 import Template

                file_path = classes_complex_types_folder.joinpath(
                    f"{entity_file_name.lower()}.py"
                )
                print(f"Writing complex type: {entity_file_name} to {file_path}...")
                template = Template(
                    template_contents, trim_blocks=True, lstrip_blocks=True
                )
                result = template.render(
                    fhir_entity=fhir_entity,
                )
            if not path.exists(file_path):
                with open(file_path, "w") as file2:
                    file2.write(result)
        elif fhir_entity.type_ in ["Quantity"]:  # valueset
            with open(data_dir.joinpath("template.jinja2"), "r") as file:
                template_contents = file.read()
                from jinja2 import Template

                file_path = classes_complex_types_folder.joinpath(
                    f"{entity_file_name.lower()}.py"
                )
                print(f"Writing complex_type: {entity_file_name} to {file_path}...")
                template = Template(
                    template_contents, trim_blocks=True, lstrip_blocks=True
                )
                result = template.render(
                    fhir_entity=fhir_entity,
                )

            if not path.exists(file_path):
                with open(file_path, "w") as file2:
                    file2.write(result)
        elif fhir_entity.is_basic_type:  # basic type
            with open(data_dir.joinpath("template.jinja2"), "r") as file:
                template_contents = file.read()
                from jinja2 import Template

                file_path = classes_simple_types_folder.joinpath(
                    f"{entity_file_name.lower()}.py"
                )
                print(f"Writing simple_type: {entity_file_name} to {file_path}...")
                template = Template(
                    template_contents, trim_blocks=True, lstrip_blocks=True
                )
                result = template.render(
                    fhir_entity=fhir_entity,
                )

            if not path.exists(file_path):
                with open(file_path, "w") as file2:
                    file2.write(result)
        else:
            # assert False, f"{resource_name}: {fhir_entity.type_} is not supported"
            print(f"{resource_name}: {fhir_entity.type_} is not supported")
        # print(result)

    with open(data_dir.joinpath("template_index.jinja2"), "r") as file:
        template_contents_index: str = file.read()
        from jinja2 import Template

        template_index = Template(
            template_contents_index, trim_blocks=True, lstrip_blocks=True
        )
        result_index: str = template_index.render(resources=resource_types_fhir_name)
        with open(
            classes_resources_folder.joinpath("resource_schema_index.py"), "w"
        ) as file2:
            file2.write(result_index)
    return 0


if __name__ == "__main__":
    exit(main())
