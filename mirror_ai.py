import google.generativeai as genai
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import gradio as gr

# Gemini API
genai.configure(api_key="API_KEY")  # Replace with your actual API key

# Stable Diffusion 2.1
pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1",
    torch_dtype=torch.float16
).to("cuda")

pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

def generate_future_description(prompt):
    """Generates a short futuristic description using Gemini AI."""
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(
            f"You are from the future (20 years ahead) and describing '{prompt}'. "
            "Focus only on its physical appearance, be direct, and use fewer than 40 tokens."
        )
        return response.text.strip() if response and response.text else "No response from Gemini."
    except Exception as e:
        return f"Error generating description: {e}"

def generate_image(text):
    """Generates an AI image of the futuristic object/person."""
    enhanced_prompt = f"A full-body futuristic {text}, highly detailed, cinematic lighting, wide frame."
    negative_prompt = "cropped, cut-off, blurry, out of frame, missing parts, bad anatomy, disfigured"

    image = pipe(
        enhanced_prompt,
        negative_prompt=negative_prompt
    ).images[0]

    return image

def show_future(user_input):
    """Generates both a description and an image."""
    future_description = generate_future_description(user_input)

    if "Error" in future_description:
        return future_description, None  # If Gemini fails, don't generate an image

    image = generate_image(f"{user_input}. {future_description}")

    return future_description, image

# Gradio Interface
interface = gr.Interface(
    fn=show_future,
    inputs=
        gr.Textbox(label="Enter an object/person to see in the future", placeholder="Example: A plane, A car, A human..."),
    outputs=[
        gr.Textbox(label="Future Description"),
        gr.Image(label="Generated Image")
    ],
    title="🔮 Future Predictor AI 🔮",
    description="Enter an object/person (or use voice input), and AI will predict how it will look in 20 years!"
)

interface.launch(share=True)
