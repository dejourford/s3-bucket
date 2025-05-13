from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()

# Access keys from environment
access_key = os.getenv("AWS_ACCESS_KEY_ID")
secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")


print("Access Key: ", access_key)
print("Secret Key: ", secret_key)