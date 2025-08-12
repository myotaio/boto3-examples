from botocore.config import Config
import boto3
import datetime

import logging

# Enable debug logging for boto3 and botocore
# logging.basicConfig(level=logging.DEBUG)

# Limit to botocore (avoids too much noise from other libraries)
# logging.getLogger("botocore").setLevel(logging.DEBUG)
# logging.getLogger("boto3").setLevel(logging.DEBUG)
# logging.getLogger("urllib3").setLevel(logging.DEBUG)


# Set Myota bZs credentials and endpoint.
BUCKET = "PUT_YOUR_MYOTA_BUCKET_NAME"
AWS_ACCESS_KEY_ID = "PUT_YOUR_MYOTA_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY = "PUT_YOUR_MYOTA_SECRET_ACCESS_KEY"
ENDPOINT_URL = "PUT_YOUR_MYOTA_ENDPOINT_URL"


def put_object(s3_client, local_file, object_key):
    with open(local_file, "rb") as f:
        s3_client.put_object(Bucket=BUCKET, Key=object_key, Body=f)
    print(f"Uploaded {local_file} to {object_key}")


def get_object(s3_client, object_key):
    response = s3_client.get_object(Bucket=BUCKET, Key=object_key)
    body = response["Body"].read()
    print(f"Downloaded content: {body.decode()}")


def list_objects_v2(s3_client):
    response = s3_client.list_objects_v2(Bucket=BUCKET, MaxKeys=1000)
    print("Objects in bucket:")
    for obj in response.get("Contents", []):
        print(f" - {obj['Key']}")


def delete_object(s3_client, object_key):
    s3_client.delete_object(Bucket=BUCKET, Key=object_key)
    print(f"Deleted {object_key}")


if __name__ == "__main__":

    # Configuration if put-object returns an error, MissingContentLength.
    # https://github.com/aws/aws-cli/issues/9214
    # Possibly it depends on boto3 >= 1.24.0 and botocore >= 1.27.0
    client_config = Config(
        region_name="us-east-1",
        request_checksum_calculation="when_required",
        response_checksum_validation="when_required",
        s3={"addressing_style": "path"},
    )

    # Make S3 client using Myota bZs credentials and endpoint.
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,  # Replace this into Myota access key ID.
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,  # Replace this into Myota secret access key.
        endpoint_url=ENDPOINT_URL,  # Add this to your existing app.
        config=client_config,  # Add config.
    )

    # Make a test file.
    file_to_upload = "sample_file.txt"
    object_key = "sample_object.txt"

    now = datetime.datetime.now(datetime.UTC).isoformat()
    content = f"This is a test file. {now}"

    with open(file_to_upload, "w") as f:
        f.write(content)

    # Object operations
    put_object(s3_client, file_to_upload, object_key)
    list_objects_v2(s3_client)
    get_object(s3_client, object_key)
    delete_object(s3_client, object_key)
