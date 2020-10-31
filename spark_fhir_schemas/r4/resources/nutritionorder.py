from typing import Union

from pyspark.sql.types import ArrayType
from pyspark.sql.types import DataType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class NutritionOrder:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> Union[StructType, DataType]:
        """
        A request to supply a diet, formula feeding (enteral) or oral nutritional
        supplement to a patient/resident.


        resourceType: This is a NutritionOrder resource

        id: The logical id of the resource, as used in the URL for the resource. Once
            assigned, this value never changes.

        meta: The metadata about the resource. This is content that is maintained by the
            infrastructure. Changes to the content might not always be associated with
            version changes to the resource.

        implicitRules: A reference to a set of rules that were followed when the resource was
            constructed, and which must be understood when processing the content. Often,
            this is a reference to an implementation guide that defines the special rules
            along with other profiles etc.

        language: The base language in which the resource is written.

        text: A human-readable narrative that contains a summary of the resource and can be
            used to represent the content of the resource to a human. The narrative need
            not encode all the structured data, but is required to contain sufficient
            detail to make it "clinically safe" for a human to just read the narrative.
            Resource definitions may define what content should be represented in the
            narrative to ensure clinical safety.

        contained: These resources do not have an independent existence apart from the resource
            that contains them - they cannot be identified independently, and nor can they
            have their own independent transaction scope.

        extension: May be used to represent additional information that is not part of the basic
            definition of the resource. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        modifierExtension: May be used to represent additional information that is not part of the basic
            definition of the resource and that modifies the understanding of the element
            that contains it and/or the understanding of the containing element's
            descendants. Usually modifier elements provide negation or qualification. To
            make the use of extensions safe and manageable, there is a strict set of
            governance applied to the definition and use of extensions. Though any
            implementer is allowed to define an extension, there is a set of requirements
            that SHALL be met as part of the definition of the extension. Applications
            processing a resource are required to check for modifier extensions.

            Modifier extensions SHALL NOT change the meaning of any elements on Resource
            or DomainResource (including cannot change the meaning of modifierExtension
            itself).

        identifier: Identifiers assigned to this order by the order sender or by the order
            receiver.

        instantiatesCanonical: The URL pointing to a FHIR-defined protocol, guideline, orderset or other
            definition that is adhered to in whole or in part by this NutritionOrder.

        instantiatesUri: The URL pointing to an externally maintained protocol, guideline, orderset or
            other definition that is adhered to in whole or in part by this
            NutritionOrder.

        instantiates: The URL pointing to a protocol, guideline, orderset or other definition that
            is adhered to in whole or in part by this NutritionOrder.

        status: The workflow status of the nutrition order/request.

        intent: Indicates the level of authority/intentionality associated with the
            NutrionOrder and where the request fits into the workflow chain.

        patient: The person (patient) who needs the nutrition order for an oral diet,
            nutritional supplement and/or enteral or formula feeding.

        encounter: An encounter that provides additional information about the healthcare context
            in which this request is made.

        dateTime: The date and time that this nutrition order was requested.

        orderer: The practitioner that holds legal responsibility for ordering the diet,
            nutritional supplement, or formula feedings.

        allergyIntolerance: A link to a record of allergies or intolerances  which should be included in
            the nutrition order.

        foodPreferenceModifier: This modifier is used to convey order-specific modifiers about the type of
            food that should be given. These can be derived from patient allergies,
            intolerances, or preferences such as Halal, Vegan or Kosher. This modifier
            applies to the entire nutrition order inclusive of the oral diet, nutritional
            supplements and enteral formula feedings.

        excludeFoodModifier: This modifier is used to convey Order-specific modifier about the type of oral
            food or oral fluids that should not be given. These can be derived from
            patient allergies, intolerances, or preferences such as No Red Meat, No Soy or
            No Wheat or  Gluten-Free.  While it should not be necessary to repeat allergy
            or intolerance information captured in the referenced AllergyIntolerance
            resource in the excludeFoodModifier, this element may be used to convey
            additional specificity related to foods that should be eliminated from the
            patient’s diet for any reason.  This modifier applies to the entire nutrition
            order inclusive of the oral diet, nutritional supplements and enteral formula
            feedings.

        oralDiet: Diet given orally in contrast to enteral (tube) feeding.

        supplement: Oral nutritional products given in order to add further nutritional value to
            the patient's diet.

        enteralFormula: Feeding provided through the gastrointestinal tract via a tube, catheter, or
            stoma that delivers nutrition distal to the oral cavity.

        note: Comments made about the {{title}} by the requester, performer, subject or
            other participants.

        """
        from spark_fhir_schemas.r4.simple_types.id import id
        from spark_fhir_schemas.r4.complex_types.meta import Meta
        from spark_fhir_schemas.r4.simple_types.uri import uri
        from spark_fhir_schemas.r4.simple_types.code import code
        from spark_fhir_schemas.r4.complex_types.narrative import Narrative
        from spark_fhir_schemas.r4.complex_types.resourcelist import ResourceList
        from spark_fhir_schemas.r4.complex_types.extension import Extension
        from spark_fhir_schemas.r4.complex_types.identifier import Identifier
        from spark_fhir_schemas.r4.simple_types.canonical import canonical
        from spark_fhir_schemas.r4.complex_types.reference import Reference
        from spark_fhir_schemas.r4.simple_types.datetime import dateTime
        from spark_fhir_schemas.r4.complex_types.codeableconcept import CodeableConcept
        from spark_fhir_schemas.r4.complex_types.nutritionorder_oraldiet import NutritionOrder_OralDiet
        from spark_fhir_schemas.r4.complex_types.nutritionorder_supplement import NutritionOrder_Supplement
        from spark_fhir_schemas.r4.complex_types.nutritionorder_enteralformula import NutritionOrder_EnteralFormula
        from spark_fhir_schemas.r4.complex_types.annotation import Annotation
        if recursion_depth > 3:
            return StructType([])
        schema = StructType(
            [
                StructField("resourceType", StringType(), True),
                # This is a NutritionOrder resource
                StructField("resourceType", StringType(), True),
                # The logical id of the resource, as used in the URL for the resource. Once
                # assigned, this value never changes.
                StructField("id", id.get_schema(recursion_depth + 1), True),
                # The metadata about the resource. This is content that is maintained by the
                # infrastructure. Changes to the content might not always be associated with
                # version changes to the resource.
                StructField(
                    "meta", Meta.get_schema(recursion_depth + 1), True
                ),
                # A reference to a set of rules that were followed when the resource was
                # constructed, and which must be understood when processing the content. Often,
                # this is a reference to an implementation guide that defines the special rules
                # along with other profiles etc.
                StructField(
                    "implicitRules", uri.get_schema(recursion_depth + 1), True
                ),
                # The base language in which the resource is written.
                StructField(
                    "language", code.get_schema(recursion_depth + 1), True
                ),
                # A human-readable narrative that contains a summary of the resource and can be
                # used to represent the content of the resource to a human. The narrative need
                # not encode all the structured data, but is required to contain sufficient
                # detail to make it "clinically safe" for a human to just read the narrative.
                # Resource definitions may define what content should be represented in the
                # narrative to ensure clinical safety.
                StructField(
                    "text", Narrative.get_schema(recursion_depth + 1), True
                ),
                # These resources do not have an independent existence apart from the resource
                # that contains them - they cannot be identified independently, and nor can they
                # have their own independent transaction scope.
                StructField(
                    "contained",
                    ArrayType(ResourceList.get_schema(recursion_depth + 1)),
                    True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource. To make the use of extensions safe and manageable,
                # there is a strict set of governance  applied to the definition and use of
                # extensions. Though any implementer can define an extension, there is a set of
                # requirements that SHALL be met as part of the definition of the extension.
                StructField(
                    "extension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # May be used to represent additional information that is not part of the basic
                # definition of the resource and that modifies the understanding of the element
                # that contains it and/or the understanding of the containing element's
                # descendants. Usually modifier elements provide negation or qualification. To
                # make the use of extensions safe and manageable, there is a strict set of
                # governance applied to the definition and use of extensions. Though any
                # implementer is allowed to define an extension, there is a set of requirements
                # that SHALL be met as part of the definition of the extension. Applications
                # processing a resource are required to check for modifier extensions.
                #
                # Modifier extensions SHALL NOT change the meaning of any elements on Resource
                # or DomainResource (including cannot change the meaning of modifierExtension
                # itself).
                StructField(
                    "modifierExtension",
                    ArrayType(Extension.get_schema(recursion_depth + 1)), True
                ),
                # Identifiers assigned to this order by the order sender or by the order
                # receiver.
                StructField(
                    "identifier",
                    ArrayType(Identifier.get_schema(recursion_depth + 1)), True
                ),
                # The URL pointing to a FHIR-defined protocol, guideline, orderset or other
                # definition that is adhered to in whole or in part by this NutritionOrder.
                StructField(
                    "instantiatesCanonical",
                    ArrayType(canonical.get_schema(recursion_depth + 1)), True
                ),
                # The URL pointing to an externally maintained protocol, guideline, orderset or
                # other definition that is adhered to in whole or in part by this
                # NutritionOrder.
                StructField(
                    "instantiatesUri",
                    ArrayType(uri.get_schema(recursion_depth + 1)), True
                ),
                # The URL pointing to a protocol, guideline, orderset or other definition that
                # is adhered to in whole or in part by this NutritionOrder.
                StructField(
                    "instantiates",
                    ArrayType(uri.get_schema(recursion_depth + 1)), True
                ),
                # The workflow status of the nutrition order/request.
                StructField(
                    "status", code.get_schema(recursion_depth + 1), True
                ),
                # Indicates the level of authority/intentionality associated with the
                # NutrionOrder and where the request fits into the workflow chain.
                StructField(
                    "intent", code.get_schema(recursion_depth + 1), True
                ),
                # The person (patient) who needs the nutrition order for an oral diet,
                # nutritional supplement and/or enteral or formula feeding.
                StructField(
                    "patient", Reference.get_schema(recursion_depth + 1), True
                ),
                # An encounter that provides additional information about the healthcare context
                # in which this request is made.
                StructField(
                    "encounter", Reference.get_schema(recursion_depth + 1),
                    True
                ),
                # The date and time that this nutrition order was requested.
                StructField(
                    "dateTime", dateTime.get_schema(recursion_depth + 1), True
                ),
                # The practitioner that holds legal responsibility for ordering the diet,
                # nutritional supplement, or formula feedings.
                StructField(
                    "orderer", Reference.get_schema(recursion_depth + 1), True
                ),
                # A link to a record of allergies or intolerances  which should be included in
                # the nutrition order.
                StructField(
                    "allergyIntolerance",
                    ArrayType(Reference.get_schema(recursion_depth + 1)), True
                ),
                # This modifier is used to convey order-specific modifiers about the type of
                # food that should be given. These can be derived from patient allergies,
                # intolerances, or preferences such as Halal, Vegan or Kosher. This modifier
                # applies to the entire nutrition order inclusive of the oral diet, nutritional
                # supplements and enteral formula feedings.
                StructField(
                    "foodPreferenceModifier",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # This modifier is used to convey Order-specific modifier about the type of oral
                # food or oral fluids that should not be given. These can be derived from
                # patient allergies, intolerances, or preferences such as No Red Meat, No Soy or
                # No Wheat or  Gluten-Free.  While it should not be necessary to repeat allergy
                # or intolerance information captured in the referenced AllergyIntolerance
                # resource in the excludeFoodModifier, this element may be used to convey
                # additional specificity related to foods that should be eliminated from the
                # patient’s diet for any reason.  This modifier applies to the entire nutrition
                # order inclusive of the oral diet, nutritional supplements and enteral formula
                # feedings.
                StructField(
                    "excludeFoodModifier",
                    ArrayType(CodeableConcept.get_schema(recursion_depth + 1)),
                    True
                ),
                # Diet given orally in contrast to enteral (tube) feeding.
                StructField(
                    "oralDiet",
                    NutritionOrder_OralDiet.get_schema(recursion_depth + 1),
                    True
                ),
                # Oral nutritional products given in order to add further nutritional value to
                # the patient's diet.
                StructField(
                    "supplement",
                    ArrayType(
                        NutritionOrder_Supplement.
                        get_schema(recursion_depth + 1)
                    ), True
                ),
                # Feeding provided through the gastrointestinal tract via a tube, catheter, or
                # stoma that delivers nutrition distal to the oral cavity.
                StructField(
                    "enteralFormula",
                    NutritionOrder_EnteralFormula.
                    get_schema(recursion_depth + 1), True
                ),
                # Comments made about the {{title}} by the requester, performer, subject or
                # other participants.
                StructField(
                    "note",
                    ArrayType(Annotation.get_schema(recursion_depth + 1)), True
                ),
            ]
        )
        return schema
