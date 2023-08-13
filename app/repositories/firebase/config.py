import json
import firebase_admin
from firebase_admin import storage, credentials, firestore
import firebase
from app.config import config

FIREBASE_BUCKET_NAME: str = config.get("FIREBASE_BUCKET_NAME", "defaultbucket")
private_key = config.get("FIREBASE_PRIVATE_KEY", '{"key": ""}')
private_key = json.loads(private_key)
private_key = private_key.get("key")

credentials_dict = {
    "type":
    config.get("FIREBASE_TYPE", "service_account"),
    "project_id":
    config.get("FIREBASE_PROJECT_ID", ""),
    "private_key_id":
    config.get("FIREBASE_PRIVATE_KEY_ID", ""),
    "private_key":
    private_key,
    "client_email":
    config.get("FIREBASE_CLIENT_EMAIL", ""),
    "client_id":
    config.get("FIREBASE_CLIENT_ID", ""),
    "auth_uri":
    config.get("FIREBASE_AUTH_URI", ""),
    "token_uri":
    config.get("FIREBASE_TOKEN_URI", ""),
    "auth_provider_x509_cert_url":
    config.get("FIREBASE_PROVIDER_X509_CERT_URL", ""),
    "client_x509_cert_url":
    config.get("FIREBASE_CLIENT_X509_CERT_URL", ""),
    "universe_domain":
    config.get("FIREBASE_UNIVERSE_DOMAIN", "")
}

bucket_name = config.get("FIREBASE_STORAGE", "")
options = {"storageBucket": bucket_name}

certificated_credentials = credentials.Certificate(credentials_dict)

app = firebase_admin.initialize_app(certificated_credentials, options)
db = firestore.client()
bucket = storage.bucket(bucket_name)
