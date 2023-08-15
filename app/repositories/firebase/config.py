import json
import firebase_admin
from firebase_admin import storage, credentials, firestore, initialize_app
from app.config import config


FIRE_BUCKET_NAME: str = config.get("FIRE_BUCKET_NAME", "defaultbucket")
private_key = config.get("FIRE_PRIVATE_KEY", '{"key": "rsa"}')
private_key = json.loads(private_key)
private_key = private_key.get("key")


credentials_dict = {
    "type":
    config.get("FIRE_TYPE", "service_account"),
    "project_id":
    config.get("FIRE_PROJECT_ID", ""),
    "private_key_id":
    config.get("FIRE_PRIVATE_KEY_ID", ""),
    "private_key":
    private_key,
    "client_email":
    config.get("FIRE_CLIENT_EMAIL", ""),
    "client_id":
    config.get("FIRE_CLIENT_ID", ""),
    "auth_uri":
    config.get("FIRE_AUTH_URI", ""),
    "token_uri":
    config.get("FIRE_TOKEN_URI", ""),
    "auth_provider_x509_cert_url":
    config.get("FIRE_PROVIDER_X509_CERT_URL", ""),
    "client_x509_cert_url":
    config.get("FIRE_CLIENT_X509_CERT_URL", ""),
    "universe_domain":
    config.get("FIRE_UNIVERSE_DOMAIN", "")
}

bucket_name = config.get("FIRE_STORAGE", "storage")
options = {"storageBucket": bucket_name}

certificated_credentials = credentials.Certificate(credentials_dict)

app = initialize_app(certificated_credentials, options)
db = firestore.client()
bucket = storage.bucket(bucket_name)
