# Programa simples, com GUI, para retirar o fundo de imagens com boas resoluções #

from tkinter import *
from tkinter import ttk
from rembg import remove
from PIL import Image, ImageTk
from tkinter import filedialog

# Configurações da Interface #
gui = Tk()
gui.title ('RemBG')
gui.geometry ('400x150')
mainFrame = Frame(gui)
mainFrame.pack(fill=BOTH, expand=1)
myCanvas = Canvas(mainFrame)
myCanvas.pack(side=LEFT, fill=BOTH, expand=1)
scroll = ttk.Scrollbar(mainFrame, orient=VERTICAL, command=myCanvas.yview)
scroll.pack(side=RIGHT, fill=Y)
myCanvas.configure(yscrollcommand=scroll.set)
myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox("all")))
segundoFrame = Frame(myCanvas)
myCanvas.create_window((0,0), window=segundoFrame, anchor="nw")

# Configurações da Interface #

# Funções 'Backend' #
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
# Funções 'Backend' #

# Interface Gráfica #

pic_label = Label (segundoFrame, text='')
pic_label.pack(pady=20, padx=200)
open_button = Button(segundoFrame, text="Abrir Imagem", command=open_thing)
open_button.pack(pady=10, padx=50)

remove_button = Button(segundoFrame, text='Remover Background', command=remove_thing)
remove_button.pack(pady=5, padx=50)
# Interface Gráfica #

gui.mainloop()
