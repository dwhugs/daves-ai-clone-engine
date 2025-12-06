import os
import torch
import gradio as gr
from emo.models import EMO
from emo.utils import load_audio, load_image, save_video

# Paths
MODEL_DIR = "models/emo/checkpoints"
CONFIG_DIR = "models/emo/configs"

MODEL_PATH = os.path.join(MODEL_DIR, "emo.pth")
CONFIG_PATH = os.path.join(CONFIG_DIR, "emo_config.yaml")

# Load EMO model
def load_emo_model():
    print("Loading EMO model...")
    model = EMO(config_path=CONFIG_PATH)
    model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
    model.eval()
    print("EMO model loaded.")
    return model

emo_model = None


def generate_talking_video(image_file, audio_file):
    global emo_model

    # Lazy-load model
    if emo_model is None:
        emo_model = load_emo_model()

    # Load inputs
    img = load_image(image_file)
    audio = load_audio(audio_file)

    print("Generating video...")

    # EMO inference
    output = emo_model.generate(img, audio)

    output_path = "output.mp4"
    save_video(output, output_path)

    print("Video created:", output_path)
    return output_path


# Gradio Interface
ui = gr.Interface(
    fn=generate_talking_video,
    inputs=[
        gr.Image(type="filepath", label="Upload a photo of Dave"),
        gr.Audio(type="filepath", label="Upload audio of Dave speaking")
    ],
    outputs=[
        gr.Video(label="Generated Dave AI Video")
    ],
    title="Dave AI Clone — EMO Edition",
    description="Upload 1 image + 1 audio file. EMO will generate a talking video of Dave."
)

if __name__ == "__main__":
    ui.launch(server_name="0.0.0.0", server_port=7860)

