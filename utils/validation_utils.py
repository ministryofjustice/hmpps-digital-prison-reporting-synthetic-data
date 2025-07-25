import json
import pandas as pd
from jsonschema import validate, ValidationError
from pathlib import Path

SCHEMAS_DIR = Path("schemas")

def load_schema(schema_filename):
    """Load and return a JSON schema dict from a file in schemas/"""
    schema_path = SCHEMAS_DIR / schema_filename
    with open(schema_path, "r") as f:
        schema = json.load(f)
    return schema

def validate_csv_against_schema(csv_path, schema_filename):
    """
    Validate each row in a CSV file against the JSON schema.
    Returns a list of error messages (empty if no errors).
    """
    schema = load_schema(schema_filename)
    df = pd.read_csv(csv_path)
    errors = []

    for index, row in df.iterrows():
        # Convert row (Series) to dict, handling NaNs
        row_dict = row.dropna().to_dict()

        # JSON schema expects certain types, convert where needed:
        # For example, integers may be floats if empty cells present;
        # here we keep it simple and rely on CSV content matching schema.

        try:
            validate(instance=row_dict, schema=schema)
        except ValidationError as ve:
            errors.append(f"Row {index + 2}: {ve.message}")  # +2 because pandas rows are 0-based and header is row 1

    return errors

if __name__ == "__main__":
    # Example usage - adjust filenames as needed:
    csv_and_schema_pairs = [
        ("data/prisoner_prisoner.csv", "prisoner_prisoner_schema.json"),
        ("data/establishment_establishment.csv", "establishment_establishment_schema.json"),
        ("data/establishment_living_unit.csv", "establishment_living_unit_schema.json"),
        ("data/movement_movement.csv", "movement_movement_schema.json"),
    ]

    all_errors = {}
    for csv_file, schema_file in csv_and_schema_pairs:
        print(f"Validating {csv_file} against {schema_file}...")
        errors = validate_csv_against_schema(csv_file, schema_file)
        if errors:
            print(f"Found {len(errors)} errors in {csv_file}:")
            for error in errors:
                print(f"  - {error}")
            all_errors[csv_file] = errors
        else:
            print(f"No validation errors in {csv_file}.")

    if all_errors:
        print("\nValidation completed with errors.")
    else:
        print("\nAll files validated successfully without errors.")