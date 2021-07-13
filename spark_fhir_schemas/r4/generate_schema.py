import json
import os
from pathlib import Path
import shutil
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

from attr import dataclass


@dataclass
class PropertyInfo:
    Name: str
    Type: Optional[str]
    UnderlyingDataType: Optional[str]
    IsUniqueUnderlyingDataType: bool
    Description: Optional[str]
    IsResourceType: bool
    IsSimpleType: bool
    IsComplexType: bool
    HideExtension: bool

    def __str__(self) -> str:
        return f"property_name:{self.Name}, type={self.Type}, underlying_type={self.UnderlyingDataType}"


@dataclass
class ResourceInfo:
    Name: str
    Type: Optional[str]
    Description: Optional[str]


def get_parent_properties(
    definitions: Dict[str, Any], parent_resource_reference: Dict[str, Any]
) -> Dict[str, Any]:
    parent_ref: str = parent_resource_reference["$ref"]
    parent_resource_name: str = parent_ref.split("/")[-1]
    parent_resource = definitions[parent_resource_name]
    parent_resource_references1 = [r for r in parent_resource["allOf"] if "$ref" in r]
    parent_properties1: Dict[str, Any] = {}
    for parent_resource_reference1 in parent_resource_references1:
        parent_properties1.update(
            get_parent_properties(
                definitions=definitions,
                parent_resource_reference=parent_resource_reference1,
            )
        )
    # now add in any properties
    propertyContainer: Dict[str, Any]
    for propertyContainer in [r for r in parent_resource["allOf"] if "properties" in r]:
        parent_properties1.update(propertyContainer["properties"])
    return parent_properties1


def main() -> int:
    data_dir: Path = Path(__file__).parent.joinpath("./")

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

    simple_types_folder = data_dir.joinpath("simple_types")
    if os.path.exists(simple_types_folder):
        shutil.rmtree(simple_types_folder)
    os.mkdir(simple_types_folder)
    simple_types_folder.joinpath("__init__.py").touch()

    fhir_schema = json.loads(contents)
    resources_dict: Dict[str, str] = fhir_schema["discriminator"]["mapping"]
    definitions = fhir_schema["definitions"]
    # print(definitions)
    # print(type(definitions))
    # for key, value in definitions.items():
    #     print(f"{key}:{value}")
    # print(definitions["Patient"])
    simple_types: List[str] = [
        "number",
        "array",
    ]  # number is not defined in fhir schema
    # extensions_allowed_for_resources: List[str] = ["Patient", "Identifier"]
    extensions_blocked_for_resources: List[str] = []
    properties_blocked: List[str] = []
    complex_types: List[str] = []
    resource_types: List[str] = []

    # first pass, decide which items are resources or simple_types or complex_types
    # have to do two passes since an item at the beginning of the file may refer to an item at the end
    for resource_name, resource in definitions.items():
        # resource_name: str = "Patient"
        # resource = definitions[resource_name]
        if resource_name in []:
            continue

        if resource_name in resources_dict:
            print(f"Added Resource: {resource_name}")
            resource_types.append(resource_name.lower())
        elif "properties" not in resource and "oneOf" not in resource:
            print(f"Added Simple Type: {resource_name}")
            simple_types.append(resource_name.lower())
        else:
            print(f"Added Complex Type: {resource_name}")
            complex_types.append(resource_name.lower())

    # 2nd Pass
    # Create the entities
    for resource_name, resource in definitions.items():
        # resource_name: str = "Patient"
        # resource = definitions[resource_name]
        if resource_name in []:
            continue
        print(f"Processing {resource_name}")
        # concat properties from allOf
        parent_resource_references = (
            [r for r in resource["allOf"] if "$ref" in r] if "allOf" in resource else []
        )
        parent_properties: Dict[str, Any] = {}

        # find the properties from parent resources and include those
        for parent_resource_reference in parent_resource_references:
            parent_properties.update(
                get_parent_properties(
                    definitions=definitions,
                    parent_resource_reference=parent_resource_reference,
                )
            )
        resource_type: Optional[str] = resource["type"] if "type" in resource else None
        resource_description: Optional[str] = (
            resource["description"] if "description" in resource else None
        )
        properties: Dict[str, Any] = parent_properties
        properties.update(resource["properties"] if "properties" in resource else {})

        # fix properties that are wrong in fhir schema
        # these are specified as backbone elements in fhir_schema.json but are not
        if resource_name in [
            "DataRequirement_CodeFilter",
            "DataRequirement_DateFilter",
            "DataRequirement_Sort",
        ]:
            properties = {
                k: v for k, v in properties.items() if k not in ["modifierExtension"]
            }

        properties_info: List[PropertyInfo] = []
        # print("---- Properties ----")
        for key, value in {
            k: v for k, v in properties.items() if not k.startswith("_")
        }.items():
            property_name = key
            description: str = value["description"]
            # items: Optional[Dict[str, str]
            #                 ] = value["items"] if "items" in value else None
            type_: Optional[str] = value["type"] if "type" in value else None
            ref_: Optional[str] = (
                value["$ref"]
                if "$ref" in value and type_ != "array"
                else value["items"]["$ref"]
                if "items" in value and "$ref" in value["items"]
                else None
            )
            # print(f"{key}:{value}")
            # type_ == None means string
            reference_type: Optional[str] = (
                ref_[ref_.rfind("/") + 1 :] if ref_ else None
            )

            if not type_ and not reference_type:
                type_ = "string"  # typically an enum
            # print(f"property_name:{property_name}, type={type_}, ref={ref_}, reference_type={reference_type}")
            property_info = PropertyInfo(
                Name=property_name,
                Type=type_,
                UnderlyingDataType=reference_type,
                IsUniqueUnderlyingDataType=not any(
                    [pi.UnderlyingDataType == reference_type for pi in properties_info]
                ),
                Description=description,
                IsResourceType=reference_type.lower() in resources_dict
                if reference_type
                else False,
                IsSimpleType=reference_type.lower() in simple_types
                if reference_type
                else (type_.lower() in simple_types if type_ else False),
                IsComplexType=reference_type.lower() in complex_types
                if reference_type
                else False,
                HideExtension=reference_type.lower() == "extension"
                and resource_name in extensions_blocked_for_resources
                if reference_type
                else False,
            )
            if resource_name.lower() == "extension":
                properties_info.append(property_info)
            elif property_name not in properties_blocked:
                properties_info.append(property_info)
            assert (
                property_info.IsResourceType
                or property_info.IsSimpleType
                or property_info.IsComplexType
            ), f"{resource_name}.{property_name}[{type_}] reference_type:{reference_type}"
            # print(properties_info[-1])
            # print("")

        # use template to generate new code files
        with open(data_dir.joinpath("template.jinja2"), "r") as file:
            template_contents: str = file.read()
            from jinja2 import Template

            template = Template(template_contents, trim_blocks=True, lstrip_blocks=True)
            result: str = template.render(
                resource=ResourceInfo(
                    Name=resource_name,
                    Type=resource_type,
                    Description=resource_description,
                ),
                properties=properties_info,
            )

            if resource_name in resources_dict:
                file_path = resources_folder.joinpath(f"{resource_name.lower()}.py")
                print(f"Writing resource: {resource_name.lower()} to {file_path}...")
                # print(result)
                with open(file_path, "w") as file2:
                    file2.write(result)
            elif "properties" not in resource and "oneOf" not in resource:
                file_path = simple_types_folder.joinpath(f"{resource_name.lower()}.py")
                print(
                    f"Writing simple_types_folder: {resource_name.lower()} to {file_path}..."
                )
                with open(file_path, "w") as file2:
                    file2.write(result)
            else:
                file_path = complex_types_folder.joinpath(f"{resource_name.lower()}.py")
                print(
                    f"Writing complex_type: {resource_name.lower()} to {file_path}..."
                )
                with open(file_path, "w") as file2:
                    file2.write(result)

            # print(result)
    return 0


if __name__ == "__main__":
    exit(main())
