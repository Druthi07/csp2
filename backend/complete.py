import random

import torch
from diffusers import StableDiffusionPipeline
from IPython.display import display  # For displaying image in Colab
from PIL import Image


class CFG:
    device = "cuda"
    seed = 42
    generator = torch.Generator(device).manual_seed(seed)
    image_gen_steps = 35
    image_gen_model_id = "stabilityai/stable-diffusion-2"
    image_gen_size = (400, 400)
    image_gen_guidance_scale = 9


def generate_stable_image(prompt):
    num = random.random()

    image_gen_model = StableDiffusionPipeline.from_pretrained(
        CFG.image_gen_model_id,
        torch_dtype=torch.float16,
        revision="fp16",
        use_auth_token="your_hugging_face_auth_token",
        guidance_scale=CFG.image_gen_guidance_scale,
    )
    image_gen_model = image_gen_model.to(CFG.device)
    image = image_gen_model(
        prompt,
        num_inference_steps=CFG.image_gen_steps,
        generator=CFG.generator,
        guidance_scale=CFG.image_gen_guidance_scale,
    ).images[0]

    image = image.resize(CFG.image_gen_size)

    # Display the image
    display(image)
    image.save("./backend/results/new/" + str(num) + ".jpg")
