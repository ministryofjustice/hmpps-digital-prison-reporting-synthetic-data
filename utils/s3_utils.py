import boto3
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

s3 = boto3.client('s3',
                  aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                  aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
                  region_name=os.getenv("AWS_REGION"))

def upload_file(file_path, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_path)
    s3.upload_file(str(file_path), bucket, object_name)
    print(f"Uploaded {file_path} to s3://{bucket}/{object_name}")

def upload_directory(directory_path, bucket, s3_prefix=""):
    directory_path = Path(directory_path)
    for file_path in directory_path.glob("*.csv"):
        object_name = f"{s3_prefix.rstrip('/')}/{file_path.name}" if s3_prefix else file_path.name
        upload_file(file_path, bucket, object_name)

if __name__ == "__main__":
    bucket_name = os.getenv("BUCKET_NAME")
    if not bucket_name:
        raise ValueError("BUCKET_NAME not set in environment variables")

    data_dir = Path("data")
    upload_directory(data_dir, bucket_name, s3_prefix="file-transfer-in")