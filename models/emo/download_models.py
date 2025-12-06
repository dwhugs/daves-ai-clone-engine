import os
import requests
import zipfile
from io import BytesIO

# Create directories if missing
os.makedirs("models/emo/checkpoints", exist_ok=True)
os.makedirs("models/emo/configs", exist_ok=True)

MODEL_ZIP_URL = "https://github.com/tnq177/emo/releases/download/v1.0/emo_models.zip"

print("🔽 Downloading EMO model package...")

response = requests.get(MODEL_ZIP_URL)
if response.status_code != 200:
    raise Exception(f"Failed to download EMO model zip: HTTP {response.status_code}")

print("📦 Extracting model files...")
zipfile.ZipFile(BytesIO(response.content)).extractall("models/emo")

print("✅ EMO model setup complete.")
