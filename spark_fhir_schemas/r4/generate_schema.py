import json
import os
from pathlib import Path
import shutil
from typing import Dict, Optional, List, Any

from attr import dataclass


@dataclass
class PropertyInfo:
    Name: str
    Type: Optional[str]
    UnderlyingDataType: Optional[str]
    IsUniqueUnderlyingDataType: bool
    Description: Optional[str]
    IsResourceType: bool

    def __str__(self) -> str:
        return f"property_name:{self.Name}, type={self.Type}, underlying_type={self.UnderlyingDataType}"


def main() -> int:
    data_dir: Path = Path(__file__).parent.joinpath('./')

    with open(data_dir.joinpath("fhir.schema.json"), "r+") as file:
        contents = file.read()

    # clean out old stuff
    resources_folder = data_dir.joinpath("resources")
    if os.path.exists(resources_folder):
        shutil.rmtree(resources_folder)
    os.mkdir(resources_folder)
    resources_folder.joinpath("__init__.py").touch()

    complex_types_folder = data_dir.joinpath("complex_types")
    if os.path.exists(complex_types_folder):
        shutil.rmtree(complex_types_folder)
    os.mkdir(complex_types_folder)
    complex_types_folder.joinpath("__init__.py").touch()

    fhir_schema = json.loads(contents)
    resources_dict: Dict[str, str] = fhir_schema["discriminator"]["mapping"]
    definitions = fhir_schema["definitions"]
    # print(definitions)
    # print(type(definitions))
    # for key, value in definitions.items():
    #     print(f"{key}:{value}")
    # print(definitions["Patient"])
    for resource_name, resource in definitions.items():
        # resource_name: str = "Patient"
        # resource = definitions[resource_name]
        properties: Dict[
            str,
            Any] = resource["properties"] if "properties" in resource else {}
        properties_info: List[PropertyInfo] = []
        # print("---- Properties ----")
        for key, value in {
            k: v
            for k, v in properties.items() if not k.startswith("_")
        }.items():
            property_name = key
            description: str = value["description"]
            # items: Optional[Dict[str, str]
            #                 ] = value["items"] if "items" in value else None
            type_: Optional[str] = value["type"] if "type" in value else None
            ref_: Optional[str] = (
                value["$ref"] if "$ref" in value and type_ != "array" else
                value["items"]["$ref"]
                if "items" in value and "$ref" in value["items"] else None
            )
            # print(f"{key}:{value}")
            # type_ == None means string
            ref_clean: Optional[str] = ref_[ref_.rfind("/") +
                                            1:] if ref_ else None
            # print(f"property_name:{property_name}, type={type_}, ref={ref_}, ref_clean={ref_clean}")
            properties_info.append(
                PropertyInfo(
                    Name=property_name,
                    Type=type_,
                    UnderlyingDataType=ref_clean,
                    IsUniqueUnderlyingDataType=not any(
                        [
                            pi.UnderlyingDataType == ref_clean
                            for pi in properties_info
                        ]
                    ),
                    Description=description,
                    IsResourceType=ref_clean in resources_dict
                )
            )
            # print(properties_info[-1])
            # print("")

        # use template to generate new code files
        with open(data_dir.joinpath("template.jinja2"), "r") as file:
            template_contents: str = file.read()
            from jinja2 import Template
            template = Template(
                template_contents, trim_blocks=True, lstrip_blocks=True
            )
            result: str = template.render(
                resource=resource_name, properties=properties_info
            )

            if resource_name in resources_dict:
                file_path = resources_folder.joinpath(
                    f"{resource_name.lower()}.py"
                )
                print(
                    f"Writing resource: {resource_name.lower()} to {file_path}..."
                )
                # print(result)
                with open(file_path, "w") as file2:
                    file2.write(result)
            else:
                file_path = complex_types_folder.joinpath(
                    f"{resource_name.lower()}.py"
                )
                print(
                    f"Writing complex_type: {resource_name.lower()} to {file_path}..."
                )
                with open(file_path, "w") as file2:
                    file2.write(result)

            # print(result)
    return 0


if __name__ == "__main__":
    exit(main())
