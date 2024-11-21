from PIL import Image
import os
import pillow_avif

print("1 de AVIF para PNG \n2 de WEBP para PNG")

comando = int(input("Converter para qual formato: "))

if comando == 2:
    arquivo = input("Qual o nome do arquivo: ")
    conveter_png = f"{arquivo}"
    Image  = Image.open(f"imagens/{conveter_png}.webp")
    Image.save(f"PNG/{conveter_png}.png")
if comando == 1:
    arquivo = input("Qual o nome do arquivo: ")
    conveter_de_avif = f"{arquivo}"
    Image  = Image.open(f"imagens/{conveter_de_avif}.avif")
    Image.save(f"PNG/{conveter_de_avif}.png")
print("Sucesso!")