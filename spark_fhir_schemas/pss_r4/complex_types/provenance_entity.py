from typing import Union, List, Optional, Any
from spark_auto_mapper.data_types.complex.complex_base import (
    AutoMapperDataTypeComplexBase,
)

from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DataType

# noinspection PyPep8Naming
class AutoMapperElasticSearchProvenance_Entity(AutoMapperDataTypeComplexBase):
    """
    Provenance of a resource is a record that describes entities and processes
    involved in producing and delivering or otherwise influencing that resource.
    Provenance provides a critical foundation for assessing authenticity, enabling
    trust, and allowing reproducibility. Provenance assertions are a form of
    contextual metadata and can themselves become important records with their own
    provenance. Provenance statement indicates clinical significance in terms of
    confidence in authenticity, reliability, and trustworthiness, integrity, and
    stage in lifecycle (e.g. Document Completion - has the artifact been legally
    authenticated), all of which may impact security, privacy, and trust policies.
    """

    # noinspection PyDefaultArgument
    def __init__(
        self,
        id_: Optional[Any] = None,
        extension: Optional[Any] = None,
        role: Optional[Any] = None,
        what: Optional[Any] = None,
        agent: Optional[Any] = None,
    ) -> None:
        super().__init__(
            id_=id_,
            extension=extension,
            role=role,
            what=what,
            agent=agent,
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
        Provenance of a resource is a record that describes entities and processes
        involved in producing and delivering or otherwise influencing that resource.
        Provenance provides a critical foundation for assessing authenticity, enabling
        trust, and allowing reproducibility. Provenance assertions are a form of
        contextual metadata and can themselves become important records with their own
        provenance. Provenance statement indicates clinical significance in terms of
        confidence in authenticity, reliability, and trustworthiness, integrity, and
        stage in lifecycle (e.g. Document Completion - has the artifact been legally
        authenticated), all of which may impact security, privacy, and trust policies.


        id: Unique id for the element within a resource (for internal references). This
            may be any string value that does not contain spaces.

        extension: May be used to represent additional information that is not part of the basic
            definition of the element. To make the use of extensions safe and manageable,
            there is a strict set of governance  applied to the definition and use of
            extensions. Though any implementer can define an extension, there is a set of
            requirements that SHALL be met as part of the definition of the extension.

        role: How the entity was used during the activity.

        what: Identity of the  Entity used. May be a logical or physical uri and maybe
            absolute or relative.

        agent: The entity is attributed to an agent to express the agent's responsibility for
            that entity, possibly along with other agents. This description can be
            understood as shorthand for saying that the agent was responsible for the
            activity which generated the entity.

        """
        from spark_fhir_schemas.pss_r4.complex_types.extension import (
            AutoMapperElasticSearchExtension as ExtensionSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.reference import (
            AutoMapperElasticSearchReference as ReferenceSchema,
        )
        from spark_fhir_schemas.pss_r4.complex_types.provenance_agent import (
            AutoMapperElasticSearchProvenance_Agent as Provenance_AgentSchema,
        )

        if (
            max_recursion_limit
            and nesting_list.count("Provenance_Entity") >= max_recursion_limit
        ) or (max_nesting_depth and nesting_depth >= max_nesting_depth):
            return StructType([StructField("id", StringType(), True)])
        # add my name to recursion list for later
        my_nesting_list: List[str] = nesting_list + ["Provenance_Entity"]
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
                # How the entity was used during the activity.
                StructField("role", StringType(), True),
                # Identity of the  Entity used. May be a logical or physical uri and maybe
                # absolute or relative.
                StructField(
                    "what",
                    ReferenceSchema.schema(
                        max_nesting_depth=max_nesting_depth,
                        nesting_depth=nesting_depth + 1,
                        nesting_list=my_nesting_list,
                        max_recursion_limit=max_recursion_limit,
                        include_extension=include_extension,
                    ),
                    True,
                ),
                # The entity is attributed to an agent to express the agent's responsibility for
                # that entity, possibly along with other agents. This description can be
                # understood as shorthand for saying that the agent was responsible for the
                # activity which generated the entity.
                StructField(
                    "agent",
                    ArrayType(
                        Provenance_AgentSchema.schema(
                            max_nesting_depth=max_nesting_depth,
                            nesting_depth=nesting_depth + 1,
                            nesting_list=my_nesting_list,
                            max_recursion_limit=max_recursion_limit,
                            include_extension=include_extension,
                        )
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