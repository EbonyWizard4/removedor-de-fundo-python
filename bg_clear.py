'''Remove fundo de imagem'''
from rembg import remove
from PIL import Image
INPUT_PATH = 'img.jpg'
OUTPUT_PATH = 'img.png'
inp = Image.open(INPUT_PATH)
output = remove(inp)
output.save(OUTPUT_PATH)
