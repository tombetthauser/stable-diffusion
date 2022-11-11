# pip install -Uq diffusers transformers fastcore PIL

from PIL import Image
from fastcore.all import concat
import torch, logging
from pathlib import Path
from huggingface_hub import notebook_login
from diffusers import StableDiffusionPipeline
from PIL import Image
import matplotlib.pyplot as plt
logging.disable(logging.WARNING)

torch.manual_seed(1)


# Use the huggingface-cli login command-line tool in your terminal and paste your token when prompted. It will be saved in a file in your computer.
if not (Path.home()/'.huggingface'/'token').exists(): notebook_login()

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", revision="fp16", torch_dtype=torch.float16).to("cuda")

# make sure the weights are cached in here
# !ls ~/.cache/huggingface/diffusers/
  # models--CompVis--stable-diffusion-v1-4	models--pcuenq--jh_dreambooth_1000
  # models--google--ddpm-celebahq-256	models--runwayml--stable-diffusion-v1-5
  # models--google--ddpm-church-256

# If your GPU is not big enough to use pipe, run pipe.enable_attention_slicing()
pipe.enable_attention_slicing()

prompt = "a photograph of an astronaut riding a horse"

image = pipe(prompt).images[0]

# output image somehow?