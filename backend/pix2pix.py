from PIL import Image
from diffusers import StableDiffusionInstructPix2PixPipeline
import torch
import random

def image_edit(image_path,prompt):

    # Load the model (assuming it's already downloaded)
    model_id = "timbrooks/instruct-pix2pix"
    pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(model_id, torch_dtype=torch.float16, revision="fp16", safety_checker=None)
    pipe.to("cuda")
    pipe.enable_attention_slicing()
    num=random.random()

    # Open the image
    try:
        image = Image.open(image_path)  # Keep original format
    except FileNotFoundError:
        print("Error: Image file not found. Please check the path and try again.")
        return

    # Display the original image
    image.save("./backend/results/modify/"+str(num)+".jpg")
    

    # Perform image editing
    edited_image = pipe(prompt, image=image, num_inference_steps=20, image_guidance_scale=1).images[0]

    # Display the edited image
    edited_image.save("./backend/results/modify/"+str(num)+"_edited.jpg")
    
    
    return ["./backend/results/modify/"+str(num)+".jpg","./backend/results/modify/"+str(num)+"_edited.jpg"]


