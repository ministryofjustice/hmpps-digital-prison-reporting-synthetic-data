import sys
import subprocess

def main():
    # Step 1: Generate mock data
    print("Generating mock data...")
    subprocess.run(["python", "generate_mock_data.py"], check=True)

    # Step 2: Validate generated data
    print("\nValidating data...")
    try:
        subprocess.run(["python", "validate_data.py"], check=True)
    except subprocess.CalledProcessError:
        print("Validation failed. Aborting pipeline.")
        sys.exit(1)

    # Step 3: Upload to S3
    print("\nUploading files to S3...")
    subprocess.run(["python", "utils/s3_utils.py"], check=True)

    print("\nPipeline complete.")

if __name__ == "__main__":
    main()