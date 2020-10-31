from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class Dosage:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        Indicates how the medication is/was taken or should be taken by the patient.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the element and that modifies the understanding of the element
            in which it is contained and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer can define an extension, there is a set of requirements that SHALL
            be met as part of the definition of the extension. Applications processing a
            resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

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
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.simple_types.integer import integer
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.timing import Timing
        from spark_fhir_schemas.r4.complex_types.dosage_doseandrate import Dosage_DoseAndRate
        from spark_fhir_schemas.r4.complex_types.ratio import Ratio
        from spark_fhir_schemas.r4.complex_types.quantity import Quantity
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
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
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the element and that modifies the understanding of the element
                # in which it is contained and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer can define an extension, there is a set of requirements that SHALL
                # be met as part of the definition of the extension. Applications processing a
                # resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # Indicates the order in which the dosage instructions should be applied or
                # interpreted.
                StructField(
                    "sequence", integer.get_schema(recursion_depth + 1), True
                ),
                # Free text dosage instructions e.g. SIG.
                StructField("text", StringType(), True),
                # Supplemental instructions to the patient on how to take the medication  (e.g.
                # "with meals" or"take half to one hour before food") or warnings for the
                # patient about the medication (e.g. "may cause drowsiness" or "avoid exposure
                # of skin to direct sunlight or sunlamps").
                StructField(
                    "additionalInstruction",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Instructions in terms that are understood by the patient or consumer.
                StructField("patientInstruction", StringType(), True),
                # When medication should be administered.
                StructField(
                    "timing", Timing.get_schema(recursion_depth + 1), True
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
                    CodeableConcept.get_schema(recursion_depth + 1), True
                ),
                # Body site to administer to.
                StructField(
                    "site", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # How drug should enter body.
                StructField(
                    "route", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # Technique for administering medication.
                StructField(
                    "method", CodeableConcept.get_schema(recursion_depth + 1),
                    True
                ),
                # The amount of medication administered.
                StructField(
                    "doseAndRate",
                    ArrayType(
                        Dosage_DoseAndRate.get_schema(recursion_depth + 1)
                    ), True
                ),
                # Upper limit on medication per unit of time.
                StructField(
                    "maxDosePerPeriod", Ratio.get_schema(recursion_depth + 1),
                    True
                ),
                # Upper limit on medication per administration.
                StructField(
                    "maxDosePerAdministration",
                    Quantity.get_schema(recursion_depth + 1), True
                ),
                # Upper limit on medication per lifetime of the patient.
                StructField(
                    "maxDosePerLifetime",
                    Quantity.get_schema(recursion_depth + 1), True
                ),
            ]
        )
        return schema
