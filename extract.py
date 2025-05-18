# extract.py

import boto3
import os

# Setup
BUCKET_NAME = "samhita-etl-data"
KEY = "raw/sales.csv"
LOCAL_PATH = "data/sales.csv"

# Make sure local 'data' folder exists
os.makedirs("data", exist_ok=True)

# Initialize S3 client
s3 = boto3.client("s3")

try:
    s3.download_file(BUCKET_NAME, KEY, LOCAL_PATH)
    print(f"✅ File downloaded successfully to: {LOCAL_PATH}")
except Exception as e:
    print(f"❌ Error downloading file: {e}")
