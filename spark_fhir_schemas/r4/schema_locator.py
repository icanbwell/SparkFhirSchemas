from pyspark.sql.types import StructType


class SchemaLocator:
    @staticmethod
    def get_schema_by_name(resource_type: str) -> StructType:
        module_name: str = f"{resource_type}Schema"
