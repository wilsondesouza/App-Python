# Programa simples em code line,  para retirar o fundo de imagens com boas resoluções #

from rembg import remove
from PIL import Image
from time import sleep as s
print ('Este programa permite retirar o fundo(background) de imagens' '\n' 'Favor deixar as imagens no mesmo diretório em que este programa se encontra.')
s(1)
input_path = input('Digite o nome exato(declarando o formato) da imagem a ter o fundo retirado: ''\n')
s(1)
output_path = input('Digite o nome exato(declarando o formato recomendado "png") onde a nova imagem sem fundo será salva: ''\n')
input = Image.open(input_path)
output = remove(input)
s(1)
output.save(output_path)
print ('O fundo (background) foi retirado com sucesso' '\n' 'Este programa será finalizado em breve')
s(1)
