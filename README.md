# Using Boto3 with Myota bucketZero Storage

This repository provides an example of how to configure [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), the AWS SDK for Python, to work with **Myota bucketZero Storage**.

Myota bucketZero is **S3-compatible**, so you can use it with your existing Boto3-based applications by specifying a custom `endpoint_url`. No other code changes are needed.

---

## 🛠️ Prerequisites

- Python 3.6 or later
- Access credentials for your Myota bucketZero account

We recommend using a **Python virtual environment** to manage dependencies.

---

## 🚀 Getting Started

### 1. Set Up Virtual Environment (Recommended)

```bash
python3 -m venv ./venv
source ./venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configure the Example

Open the `example.py` file and update the following variables with your Myota access information:

```python
BUCKET = "YOUR_MYOTA_BUCKET_NAME"
AWS_ACCESS_KEY_ID = "YOUR_MYOTA_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY = "YOUR_MYOTA_SECRET_ACCESS_KEY"
ENDPOINT_URL = "YOUR_MYOTA_ENDPOINT_URL"

...

# Make S3 client using Myota bZs credentials and endpoint.
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,  # Replace this into Myota access key ID.
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,  # Replace this into Myota secret access key.
    endpoint_url=ENDPOINT_URL,  # Add this to your existing app.
    config=client_config,  # Add config.
)
```

---

## ▶️ Run the Example

Once configured, run the script:

```bash
python example.py
```

The script will:

1. Upload a test file to your Myota bucket using `put_object`
2. Retrieve it using `get_object`
3. List it with `list_objects_v2`
4. Delete the test file using `delete_object`

---

## 📬 Need Help?

If you have any questions or need assistance, feel free to contact our support team at [services@myota.io](mailto:services@myota.io).

---
