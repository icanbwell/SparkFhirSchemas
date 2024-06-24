# SparkFhirSchemas


This project is a collection of [FHIR](https://www.hl7.org/fhir/) schemas for [Apache Spark](https://spark.apache.org/).

## Usage
1. First update the `fhir.schema.json` file with the FHIR schema you want to use.
   2. You can find the FHIR schema in the [FHIR specification](https://hl7.org/fhir/R4B/fhir.schema.json).
3. Run `make schema` to generate the Spark schema for RXX.
4. Run `make schema-stu3` to generate the Spark schema for STU3.
5. Run `make schema-dstu2` to generate the Spark schema for DSTU2.

This will generate the Spark schema in the spark_fhir_schemas directory.