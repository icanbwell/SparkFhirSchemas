from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchMedicationAdministration_Dosage(
    AutoMapperDataTypeComplexBase
):
    """
    Describes the event of a patient consuming or otherwise being administered a
    medication.  This may be as simple as swallowing a tablet or it may be a long
    running infusion.  Related resources tie this event to the authorizing
    prescription, and the specific encounter between patient and health care
    practitioner.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        text: Optional[Any] = None,
        site: Optional[Any] = None,
        route: Optional[Any] = None,
        method: Optional[Any] = None,
        dose: Optional[Any] = None,
        rateRatio: Optional[Any] = None,
        rateQuantity: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            text=text,
            site=site,
            route=route,
            method=method,
            dose=dose,
            rateRatio=rateRatio,
            rateQuantity=rateQuantity,
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
        Describes the event of a patient consuming or otherwise being administered a
        medication.  This may be as simple as swallowing a tablet or it may be a long
        running infusion.  Related resources tie this event to the authorizing
        prescription, and the specific encounter between patient and health care
        practitioner.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        text: Free text dosage can be used for cases where the dosage administered is too
            complex to code. When coded dosage is present, the free text dosage may still
            be present for display to humans.

            The dosage instructions should reflect the dosage of the medication that was
            administered.

        site: A coded specification of the anatomic site where the medication first entered
            the body.  For example, "left arm".

        route: A code specifying the route or physiological path of administration of a
            therapeutic agent into or onto the patient.  For example, topical,
            intravenous, etc.

        method: A coded value indicating the method by which the medication is intended to be
            or was introduced into or on the body.  This attribute will most often NOT be
            populated.  It is most commonly used for injections.  For example, Slow Push,
            Deep IV.

        dose: The amount of the medication given at one administration event.   Use this
            value when the administration is essentially an instantaneous event such as a
            swallowing a tablet or giving an injection.

        rateRatio: Identifies the speed with which the medication was or will be introduced into
            the patient.  Typically, the rate for an infusion e.g. 100 ml per 1 hour or
            100 ml/hr.  May also be expressed as a rate per unit of time, e.g. 500 ml per
            2 hours.  Other examples:  200 mcg/min or 200 mcg/1 minute; 1 liter/8 hours.

        rateQuantity: Identifies the speed with which the medication was or will be introduced into
            the patient.  Typically, the rate for an infusion e.g. 100 ml per 1 hour or
            100 ml/hr.  May also be expressed as a rate per unit of time, e.g. 500 ml per
            2 hours.  Other examples:  200 mcg/min or 200 mcg/1 minute; 1 liter/8 hours.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.codeableconcept import (
            AutoMapperElasticSearchCodeableConcept as CodeableConceptSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.quantity import (
            AutoMapperElasticSearchQuantity as QuantitySchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.ratio import (
            AutoMapperElasticSearchRatio as RatioSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("MedicationAdministration_Dosage")
            >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["MedicationAdministration_Dosage"]
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
                # Free text dosage can be used for cases where the dosage administered is too
                # complex to code. When coded dosage is present, the free text dosage may still
                # be present for display to humans.
                #
                # The dosage instructions should reflect the dosage of the medication that was
                # administered.
                StructField("text", StringType(), True),
                # A coded specification of the anatomic site where the medication first entered
                # the body.  For example, "left arm".
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
                # A code specifying the route or physiological path of administration of a
                # therapeutic agent into or onto the patient.  For example, topical,
                # intravenous, etc.
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
                # A coded value indicating the method by which the medication is intended to be
                # or was introduced into or on the body.  This attribute will most often NOT be
                # populated.  It is most commonly used for injections.  For example, Slow Push,
                # Deep IV.
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
                # The amount of the medication given at one administration event.   Use this
                # value when the administration is essentially an instantaneous event such as a
                # swallowing a tablet or giving an injection.
                StructField(
                    "dose",
                    QuantitySchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies the speed with which the medication was or will be introduced into
                # the patient.  Typically, the rate for an infusion e.g. 100 ml per 1 hour or
                # 100 ml/hr.  May also be expressed as a rate per unit of time, e.g. 500 ml per
                # 2 hours.  Other examples:  200 mcg/min or 200 mcg/1 minute; 1 liter/8 hours.
                StructField(
                    "rateRatio",
                    RatioSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # Identifies the speed with which the medication was or will be introduced into
                # the patient.  Typically, the rate for an infusion e.g. 100 ml per 1 hour or
                # 100 ml/hr.  May also be expressed as a rate per unit of time, e.g. 500 ml per
                # 2 hours.  Other examples:  200 mcg/min or 200 mcg/1 minute; 1 liter/8 hours.
                StructField(
                    "rateQuantity",
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