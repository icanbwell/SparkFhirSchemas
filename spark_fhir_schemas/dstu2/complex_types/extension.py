from typing import Union, List, Optional

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DateType, BooleanType, IntegerType, \
    DataType, TimestampType, FloatType


# This file is auto-generated by generate_schema so do not edit manually
# noinspection PyPep8Naming
class ExtensionSchema:
    """
    Optional Extensions Element - found in all resources.
    If the element is present, it must have a value for at least one of the
    defined elements, an @id referenced from the Narrative, or extensions
    """
    # noinspection PyDefaultArgument
    @staticmethod
    def get_schema(max_nesting_depth: Optional[int] = 6, nesting_depth: int = 0, nesting_list: List[str] = [], max_recursion_limit: Optional[int] = 2, include_extension: Optional[bool] = False, extension_fields: Optional[List[str]] = ["valueBoolean","valueCode","valueDate","valueDateTime","valueDecimal","valueId","valueInteger","valuePositiveInt","valueString","valueTime","valueUnsignedInt","valueUri", "valueQuantity"], extension_depth: int = 0, max_extension_depth: Optional[int] = 2) -> Union[StructType, DataType]:
        """
    Optional Extensions Element - found in all resources.
    If the element is present, it must have a value for at least one of the
    defined elements, an @id referenced from the Narrative, or extensions


        id: None
        extension: May be used to represent additional information that is not part of the basic
    definition of the element. In order to make the use of extensions safe and
    manageable, there is a strict set of governance  applied to the definition and
    use of extensions. Though any implementer is allowed to define an extension,
    there is a set of requirements that SHALL be met as part of the definition of
    the extension.
        url: None
        valueBoolean: None
        valueInteger: None
        valueDecimal: None
        valueBase64Binary: None
        valueInstant: None
        valueString: None
        valueUri: None
        valueDate: None
        valueDateTime: None
        valueTime: None
        valueCode: None
        valueOid: None
        valueUuid: None
        valueId: None
        valueUnsignedInt: None
        valuePositiveInt: None
        valueMarkdown: None
        valueAnnotation: None
        valueAttachment: None
        valueIdentifier: None
        valueCodeableConcept: None
        valueCoding: None
        valueQuantity: None
        valueRange: None
        valuePeriod: None
        valueRatio: None
        valueReference: None
        valueSampledData: None
        valueSignature: None
        valueHumanName: None
        valueAddress: None
        valueContactPoint: None
        valueTiming: None
        valueMeta: None
        """
            # id
        from spark_fhir_schemas.dstu2.simple_types.id import idSchema
            # url
        from spark_fhir_schemas.dstu2.simple_types.uri import uriSchema
            # valueBoolean
        from spark_fhir_schemas.dstu2.simple_types.boolean import booleanSchema
            # valueInteger
        from spark_fhir_schemas.dstu2.simple_types.integer import integerSchema
            # valueDecimal
        from spark_fhir_schemas.dstu2.simple_types.decimal import decimalSchema
            # valueBase64Binary
        from spark_fhir_schemas.dstu2.simple_types.base64binary import base64BinarySchema
            # valueInstant
        from spark_fhir_schemas.dstu2.simple_types.instant import instantSchema
            # valueString
        from spark_fhir_schemas.dstu2.simple_types.string import stringSchema
            # valueUri
        from spark_fhir_schemas.dstu2.simple_types.uri import uriSchema
            # valueDate
        from spark_fhir_schemas.dstu2.simple_types.date import dateSchema
            # valueDateTime
        from spark_fhir_schemas.dstu2.simple_types.datetime import dateTimeSchema
            # valueTime
        from spark_fhir_schemas.dstu2.simple_types.time import timeSchema
            # valueCode
        from spark_fhir_schemas.dstu2.simple_types.code import codeSchema
            # valueOid
        from spark_fhir_schemas.dstu2.simple_types.oid import oidSchema
            # valueUuid
        from spark_fhir_schemas.dstu2.simple_types.uuid import uuidSchema
            # valueId
        from spark_fhir_schemas.dstu2.simple_types.id import idSchema
            # valueUnsignedInt
        from spark_fhir_schemas.dstu2.simple_types.unsignedint import unsignedIntSchema
            # valuePositiveInt
        from spark_fhir_schemas.dstu2.simple_types.positiveint import positiveIntSchema
            # valueMarkdown
        from spark_fhir_schemas.dstu2.simple_types.markdown import markdownSchema
            # valueAnnotation
        from spark_fhir_schemas.dstu2.complex_types.annotation import AnnotationSchema
            # valueAttachment
        from spark_fhir_schemas.dstu2.complex_types.attachment import AttachmentSchema
            # valueIdentifier
        from spark_fhir_schemas.dstu2.complex_types.identifier import IdentifierSchema
            # valueCodeableConcept
        from spark_fhir_schemas.dstu2.complex_types.codeableconcept import CodeableConceptSchema
            # valueCoding
        from spark_fhir_schemas.dstu2.complex_types.coding import CodingSchema
            # valueQuantity
        from spark_fhir_schemas.dstu2.complex_types.quantity import QuantitySchema
            # valueRange
        from spark_fhir_schemas.dstu2.complex_types.range import RangeSchema
            # valuePeriod
        from spark_fhir_schemas.dstu2.complex_types.period import PeriodSchema
            # valueRatio
        from spark_fhir_schemas.dstu2.complex_types.ratio import RatioSchema
            # valueReference
        from spark_fhir_schemas.dstu2.complex_types.reference import ReferenceSchema
            # valueSampledData
        from spark_fhir_schemas.dstu2.complex_types.sampleddata import SampledDataSchema
            # valueSignature
        from spark_fhir_schemas.dstu2.complex_types.signature import SignatureSchema
            # valueHumanName
        from spark_fhir_schemas.dstu2.complex_types.humanname import HumanNameSchema
            # valueAddress
        from spark_fhir_schemas.dstu2.complex_types.address import AddressSchema
            # valueContactPoint
        from spark_fhir_schemas.dstu2.complex_types.contactpoint import ContactPointSchema
            # valueTiming
        from spark_fhir_schemas.dstu2.complex_types.timing import TimingSchema
            # valueMeta
        from spark_fhir_schemas.dstu2.complex_types.meta import MetaSchema
        if (max_recursion_limit and nesting_list.count("Extension") >= max_recursion_limit) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        if max_extension_depth and extension_depth >= max_extension_depth:
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list+["Extension"]
        schema = StructType(
            [
                # None
                StructField("id", idSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. In order to make the use of extensions safe and
                # manageable, there is a strict set of governance  applied to the definition and
                # use of extensions. Though any implementer is allowed to define an extension,
                # there is a set of requirements that SHALL be met as part of the definition of
                # the extension.
                StructField("extension", ExtensionSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("url", StringType(), True),
                # None
                StructField("valueBoolean", BooleanType(), True),
                # None
                StructField("valueInteger", integerSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueDecimal", decimalSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueBase64Binary", base64BinarySchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueInstant", instantSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueString", StringType(), True),
                # None
                StructField("valueUri", StringType(), True),
                # None
                StructField("valueDate", DateType(), True),
                # None
                StructField("valueDateTime", dateTimeSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueTime", timeSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueCode", codeSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueOid", oidSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueUuid", uuidSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueId", idSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueUnsignedInt", unsignedIntSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valuePositiveInt", positiveIntSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueMarkdown", markdownSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueAnnotation", AnnotationSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueAttachment", AttachmentSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueIdentifier", IdentifierSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueCodeableConcept", CodeableConceptSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueCoding", CodingSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueQuantity", QuantitySchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueRange", RangeSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valuePeriod", PeriodSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueRatio", RatioSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueReference", ReferenceSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueSampledData", SampledDataSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueSignature", SignatureSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueHumanName", HumanNameSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueAddress", AddressSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueContactPoint", ContactPointSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueTiming", TimingSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
                # None
                StructField("valueMeta", MetaSchema.get_schema(max_nesting_depth=max_nesting_depth,nesting_depth=nesting_depth+1,nesting_list=my_nesting_list,max_recursion_limit=max_recursion_limit,include_extension=include_extension,extension_fields=extension_fields, extension_depth=extension_depth+1, max_extension_depth=max_extension_depth), True),
            ]
        )
        if not include_extension:
            schema.fields = [c if c.name != "extension" else StructField("extension", StringType(), True) for c in schema.fields]

        if extension_fields:
            schema.fields = [
                c
                for c in schema.fields
                if c.name in extension_fields or c.name in ["id", "extension", "url"]
            ]
            schema.names = [
                n
                for n in schema.names
                if n in extension_fields or n in ["id", "extension", "url"]
            ]
        return schema