from rembg import remove
from PIL import Image
input_path = 'img.jpg'
output_path = 'img.png'
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)