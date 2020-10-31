from pyspark.sql.types import ArrayType, StringType, StructField, StructType


# noinspection PyPep8Naming
class DeviceDefinition:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        from spark_fhir_schemas.r4.complex_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.complex_types.uri import uri
        from spark_fhir_schemas.r4.complex_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.complex_types.devicedefinition_udideviceidentifier import DeviceDefinition_UdiDeviceIdentifier
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.complex_types.devicedefinition_devicename import DeviceDefinition_DeviceName
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.devicedefinition_specialization import DeviceDefinition_Specialization
        from spark_fhir_schemas.r4.complex_types.productshelflife import ProductShelfLife
        from spark_fhir_schemas.r4.complex_types.prodcharacteristic import ProdCharacteristic
        from spark_fhir_schemas.r4.complex_types.devicedefinition_capability import DeviceDefinition_Capability
        from spark_fhir_schemas.r4.complex_types.devicedefinition_property import DeviceDefinition_Property
        from spark_fhir_schemas.r4.complex_types.contactpoint import ContactPoint
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        from spark_fhir_schemas.r4.complex_types.devicedefinition_material import DeviceDefinition_Material
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                StructField("id", id.get_schema(recursion_depth + 1), True),
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "udiDeviceIdentifier",
                    ArrayType(
                        DeviceDefinition_UdiDeviceIdentifier.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField("manufacturerString", StringType(), True),
                StructField(
                    "manufacturerReference",
                    Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "deviceName",
                    ArrayType(
                        DeviceDefinition_DeviceName.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField("modelNumber", StringType(), True),
                StructField(
                    "type", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "specialization",
                    ArrayType(
                        DeviceDefinition_Specialization.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField("version", ArrayType(StringType()), True),
                StructField(
                    "safety",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "shelfLifeStorage",
                    ArrayType(
                        ProductShelfLife.get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "physicalCharacteristics",
                    ProdCharacteristic.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "languageCode",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField(
                    "capability",
                    ArrayType(
                        DeviceDefinition_Capability.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "property",
                    ArrayType(
                        DeviceDefinition_Property.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                StructField(
                    "owner", Reference.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "contact",
                    ArrayType(ContactPoint.get_schema(recursion_depth + 1)),
                    True
                ),
                StructField("url", uri.get_schema(recursion_depth + 1), True),
                StructField(
                    "onlineInformation", uri.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
                StructField(
                    "quantity", Quantity.get_schema(recursion_depth + 1), True
                ),
                StructField(
                    "parentDevice", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                StructField(
                    "material",
                    ArrayType(
                        DeviceDefinition_Material.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
            ]
        )

        return schema
