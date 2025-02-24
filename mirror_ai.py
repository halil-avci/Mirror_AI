import google.generativeai as genai
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

# Set up Gemini API key
genai.configure(api_key="API_KEY")

# Load SD 2.1 
pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1",
    torch_dtype=torch.float32
).to("cuda")

pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)


def generate_future_description(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(f"You come from future, 20 years from now, and describing futuristic version of '{prompt}' in time you came from, in terms of physical appearance, straight into the point. Make sure your response is under 50 tokens.")
        return response.text.strip() if response and response.text else "No response from Gemini."
    except Exception as e:
        return f"Error generating description: {e}"

def generate_image(text, filename="output.png"):
    enhanced_prompt = f"Futuristic concept of {text} Detailed, realistic."
    image = pipe(text).images[0]
    image.save(filename)
    return filename

if __name__ == "__main__":
    user_input = input("Enter an object/person to see in the future: ")
    future_description = generate_future_description(user_input)
    print(future_description)
    #generate_image(f"{user_input}. {future_description}")
