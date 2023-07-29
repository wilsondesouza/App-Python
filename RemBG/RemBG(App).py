# Programa simples, com GUI, para retirar o fundo de imagens com boas resoluções #

from tkinter import *
from rembg import remove
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title ('RemBG')
root.geometry ('800x600')

# Funções 
def open_thing():
    global input_path, my_img
    input_path = filedialog.askopenfilename(title='Selecionar Imagem', filetype=(("JPEG", ".jpeg"), ("Todos os tipos", "*.*")))
    if input_path:
        my_img = ImageTk.PhotoImage(Image.open(input_path))
        pic_label.config(image=my_img, bg='black')

def remove_thing():   
    output_path = filedialog.asksaveasfilename(title='Salvar', filetype=(("PNG", ".png"), ("Todos os tipos", "*.*")))
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path, 'png')
    global my_img
    my_img = ImageTk.PhotoImage(Image.open(output_path))
    pic_label.config(image=my_img)


# Janela

pic_label = Label (root, text='')
pic_label.pack(pady=20)

open_button = Button(root, text="Abrir Imagem", command=open_thing)
open_button.pack(pady=20)

remove_button = Button(root, text='Remover Background', command=remove_thing)
remove_button.pack(pady=20)

root.mainloop()
