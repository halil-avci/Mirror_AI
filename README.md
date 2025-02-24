# Mirror_AI
A Small AI project that creates a futuristic image of a given text.

## System Strengths

### Accurate and Descriptive Text Generation for Common Objects
The system excels at generating short yet informative descriptions for well-defined, physical objects. The Gemini AI model is effective in capturing essential details while maintaining clarity.

### Produces Visually Detailed Images for Clear, Physical Concepts
For simple and well-known objects, the generated images are generally highly detailed and visually appealing. Even if it is a bit old, Stable Diffusion 2.1 captures textures, lighting, and form, making the outputs mostly consistent with user expectations.

### Simple Interface with Real-Time Processing
The integration with Gradio ensures a smooth user experience with minimal setup.

### Handles Multiple Input Formats, Including Text Variations
The system is designed to process up to a couple of words. This flexibility allows users to experiment with all types of objects without requiring strict formatting, making it adaptable to a wide range of applications.

---

## System Weaknesses

### Struggles with Abstract or Conceptual Prompts
When given abstract inputs like "love" or "emotion," the system fails to generate meaningful responses.

### Generated Images Sometimes Include Artifacts or Missing Details
While simple objects are generally well-represented, complex concepts or multi-word inputs sometimes lead to inconsistent or incomplete images. Although Stable Diffuser is given a negative prompt like this: 

### Longer or Complex Prompts May Be Truncated or Misinterpreted
The system has difficulty processing detailed or long-form inputs. The model may cut off essential elements, leading to partial or vague descriptions. This occurs because Stable Diffusion enforces a maximum of 77 tokens as input and ignores the end parts of the prompt.

### Occasional Delays in Response Time, Especially for Large Inputs
For more complex image generation tasks, processing time increases significantly. This is due to the computational load on the GPU, which can slow down response times. Additionally, API calls to Gemini AI sometimes introduce latency, leading to intermittent performance drops. However, the bottleneck of the system is generating the AI image, which took **2 minutes with a GTX 1660 Ti**. In **Google Colab, the total execution time may drop to 10-15 seconds**.

### Errors Caused by Third-Party Apps
Since the system relies on third-party AI models (**Gemini AI and Stable Diffusion**), errors can occur due to external dependencies. Common issues include API downtime, rate limits, and inconsistencies in the responses.

- **Gemini AI Errors:** Occasionally, Gemini AI may return vague or incomplete responses, especially for abstract prompts. In some cases, API requests may time out, resulting in no response. After a couple of tries, due to an unknown reason, the **Google Colab platform may fail to get a response from the Gemini API**.
- **Stable Diffusion Issues:** Image generation may fail if the model runs out of VRAM, leading to blank or corrupted outputs. Additionally, updates to the `diffusers` library can introduce unexpected changes in model behavior.
- **Gradio Performance Concerns:** As the system runs through **Gradio**, network latency or server load can slow down response times, especially when multiple users are accessing the application simultaneously.

