from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    ArrayType,
    BooleanType,
    DataType,
)

# noinspection PyPep8Naming
class AutoMapperElasticSearchDosage(AutoMapperDataTypeComplexBase):
    """
    Indicates how the medication is/was taken or should be taken by the patient.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        sequence: Optional[Any] = None,
        text: Optional[Any] = None,
        additionalInstruction: Optional[Any] = None,
        patientInstruction: Optional[Any] = None,
        timing: Optional[Any] = None,
        asNeededBoolean: Optional[Any] = None,
        asNeededCodeableConcept: Optional[Any] = None,
        site: Optional[Any] = None,
        route: Optional[Any] = None,
        method: Optional[Any] = None,
        doseAndRate: Optional[Any] = None,
        maxDosePerPeriod: Optional[Any] = None,
        maxDosePerAdministration: Optional[Any] = None,
        maxDosePerLifetime: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            sequence=sequence,
            text=text,
            additionalInstruction=additionalInstruction,
            patientInstruction=patientInstruction,
            timing=timing,
            asNeededBoolean=asNeededBoolean,
            asNeededCodeableConcept=asNeededCodeableConcept,
            site=site,
            route=route,
            method=method,
            doseAndRate=doseAndRate,
            maxDosePerPeriod=maxDosePerPeriod,
            maxDosePerAdministration=maxDosePerAdministration,
            maxDosePerLifetime=maxDosePerLifetime,
        )
        super().include_null_properties(include_null_properties=True)

    @staticmethod
    def schema(
        max_nesting_depth: Optional[int] = 6,
        nesting_depth: int = 0,
        nesting_list: List[str] = [],
        max_recursion_limit: Optional[int] = 2,
        include_extension: Optional[bool] = False,
    ) -> Union[StructType, DataType]:
        """
        Indicates how the medication is/was taken or should be taken by the patient.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        sequence: Indicates the order in which the dosage instructions should be applied or
            interpreted.

        text: Free text dosage instructions e.g. SIG.

        additionalInstruction: Supplemental instructions to the patient on how to take the medication  (e.g.
            "with meals" or"take half to one hour before food") or warnings for the
            patient about the medication (e.g. "may cause drowsiness" or "avoid exposure
            of skin to direct sunlight or sunlamps").

        patientInstruction: Instructions in terms that are understood by the patient or consumer.

        timing: When medication should be administered.

        asNeededBoolean: Indicates whether the Medication is only taken when needed within a specific
            dosing schedule (Boolean option), or it indicates the precondition for taking
            the Medication (CodeableConcept).

        asNeededCodeableConcept: Indicates whether the Medication is only taken when needed within a specific
            dosing schedule (Boolean option), or it indicates the precondition for taking
            the Medication (CodeableConcept).

        site: Body site to administer to.

        route: How drug should enter body.

        method: Technique for administering medication.

        doseAndRate: The amount of medication administered.

        maxDosePerPeriod: Upper limit on medication per unit of time.

        maxDosePerAdministration: Upper limit on medication per administration.

        maxDosePerLifetime: Upper limit on medication per lifetime of the patient.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.simple_types.integer import (
            AutoMapperElasticSearchinteger as integerSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.timing import (
            AutoMapperElasticSearchTiming as TimingSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.dosage_doseandrate import (
            AutoMapperElasticSearchDosage_DoseAndRate as Dosage_DoseAndRateSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.ratio import (
            AutoMapperElasticSearchRatio as RatioSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )

        if (
            max_recursion_limit and nesting_list.count("Dosage") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Dosage"]
        schema = StructType(
            [
                # Unique id for the element within a resource (for internal references). This
                # may be any string value that does not contain spaces.
                StructField("id", StringType(), True),
                # May be used to represent additional information that is not part of the basic
                # definition of the element. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(
                        ExtensionSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Indicates the order in which the dosage instructions should be applied or
                # interpreted.
                StructField(
                    "sequence",
                    integerSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Free text dosage instructions e.g. SIG.
                StructField("text", StringType(), True),
                # Supplemental instructions to the patient on how to take the medication  (e.g.
                # "with meals" or"take half to one hour before food") or warnings for the
                # patient about the medication (e.g. "may cause drowsiness" or "avoid exposure
                # of skin to direct sunlight or sunlamps").
                StructField(
                    "additionalInstruction",
                    ArrayType(
                        CodeableConceptSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Instructions in terms that are understood by the patient or consumer.
                StructField("patientInstruction", StringType(), True),
                # When medication should be administered.
                StructField(
                    "timing",
                    TimingSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Indicates whether the Medication is only taken when needed within a specific
                # dosing schedule (Boolean option), or it indicates the precondition for taking
                # the Medication (CodeableConcept).
                StructField("asNeededBoolean", BooleanType(), True),
                # Indicates whether the Medication is only taken when needed within a specific
                # dosing schedule (Boolean option), or it indicates the precondition for taking
                # the Medication (CodeableConcept).
                StructField(
                    "asNeededCodeableConcept",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Body site to administer to.
                StructField(
                    "site",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # How drug should enter body.
                StructField(
                    "route",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Technique for administering medication.
                StructField(
                    "method",
                    CodeableConceptSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The amount of medication administered.
                StructField(
                    "doseAndRate",
                    ArrayType(
                        Dosage_DoseAndRateSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
                    ),
                    True,
                ),
                # Upper limit on medication per unit of time.
                StructField(
                    "maxDosePerPeriod",
                    RatioSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Upper limit on medication per administration.
                StructField(
                    "maxDosePerAdministration",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Upper limit on medication per lifetime of the patient.
                StructField(
                    "maxDosePerLifetime",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
            ]
        )
        if not include_extension:
            schema.fields = [
                c
                if c.name != "extension"
                else StructField("extension", StringType(), True)
                for c in schema.fields
            ]
        return schema
