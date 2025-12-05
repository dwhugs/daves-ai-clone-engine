# Dave's AI Clone Engine - Backend Skeleton (Working)

from fastapi import FastAPI, File, UploadFile
import uuid, os, shutil

app = FastAPI()

# Ensure folders exist
os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)

@app.get("/")
def home():
    return {"status": "Backend running"}

@app.post("/start")
async def start(face: UploadFile = File(...), audio: UploadFile = File(...), engine: str = "wav2lip"):
    job_id = str(uuid.uuid4())
    job_input = f"input/{job_id}"
    job_output = f"output/{job_id}"
    os.makedirs(job_input, exist_ok=True)
    os.makedirs(job_output, exist_ok=True)

    face_path = f"{job_input}/face.png"
    audio_path = f"{job_input}/audio.wav"

    # Save inputs
    with open(face_path, "wb") as f:
        f.write(await face.read())

    with open(audio_path, "wb") as f:
        f.write(await audio.read())

    # TODO: Insert your AI model code here
    # Example:
    # run_wav2lip(face_path, audio_path, f"{job_output}/result.mp4")

    # PLACEHOLDER: no model yet
    shutil.copy("placeholder.mp4", f"{job_output}/result.mp4")

    return {"job_id": job_id}

@app.get("/status/{job_id}")
def status(job_id: str):
    result_path = f"output/{job_id}/result.mp4"
    if os.path.exists(result_path):
        return {"status": "done"}
    return {"status": "processing"}

@app.get("/download/{job_id}")
def download(job_id: str):
    result_path = f"output/{job_id}/result.mp4"
    if not os.path.exists(result_path):
        return {"error": "not ready"}

    return {"download_url": f"/output/{job_id}/result.mp4"}
