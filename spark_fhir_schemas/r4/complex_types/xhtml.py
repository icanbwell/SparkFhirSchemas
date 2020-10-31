from pyspark.sql.types import StructType


# noinspection PyPep8Naming
class xhtml:
    @staticmethod
    def get_schema(recursion_depth: int = 0) -> StructType:
        # from https://hl7.org/FHIR/patient.html
        if recursion_depth > 3:
            return StructType([])
        schema = StructType([])

        return schema
