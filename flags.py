#impordib tkinter-moodulit nimega tk, mis on vajalik graafilise shell'i loomiseks.
import tkinter as tk
#juhuslike elementide import
from random import choice

#funktsioon ruutude joonistamiseks ringidega
def figures(canvas, x0, y0, x1, y1, depth):
    #kui väärtus on 0, siis funktsioon peatub ja tagastab pildi.
    if depth == 0:
        return
    #joonistab ringi ja ruudu
    canvas.create_rectangle(x0, y0, x1, y1, fill="red")
    canvas.create_oval(x0, y0, x1, y1, fill="yellow")
    
    #Arvutab uued koordinaadid järgmise ristküliku jaoks, mis on 15 piksli võrra väiksem. 
    new_x0 = x0 + 15
    new_y0 = y0 + 15
    new_x1 = x1 - 15
    new_y1 = y1 - 15
    
    #kutsub ennast vähendatud koordinaatidega
    figures(canvas, new_x0, new_y0, new_x1, new_y1, depth - 1)

#funktsioon uue akna loomiseks
def drawing():
    new_window = tk.Toplevel()

    label = tk.Label(new_window, text="numbers:")
    label.pack()

    #Loob tekstivälja numbri sisestamiseks
    entry = tk.Entry(new_window)
    entry.pack()

    #loosib antud numbri alusel ja kustutab eelmise loosimise.
    def draw():
        depth = int(entry.get())
        canvas.delete("all")
        figures(canvas, 50, 50, 550, 550, depth)

    #nupu ja lõuendi lisamine
    button = tk.Button(new_window, text="draw", command=draw)
    button.pack()

    canvas = tk.Canvas(new_window, width=600, height=600, background="white")
    canvas.pack()

#malelaud
def chess():
    new_window = tk.Toplevel()
    #puuri suurus
    cell_size = 60
    #luua tahvel
    canvas = tk.Canvas(new_window, width=8 * cell_size, height=8 * cell_size)
    canvas.pack()

    colors = ["white", "black"]

    #rea ja veeru silmus
    for row in range(8):
        for col in range(8):
            #Värv muutub vastupidiseks, kui liigute järgmisesse lahtrisse.
            color_index = (row + col) % 2
            #jaotab värvid nurkadesse
            x0, y0 = col * cell_size, row * cell_size
            x1, y1 = x0 + cell_size, y0 + cell_size
            #Joonistused
            canvas.create_rectangle(x0, y0, x1, y1, fill=colors[color_index])

def circles():
    OV = tk.Toplevel()
    canvas = tk.Canvas(OV, width=600, height=600, bg="white")
    canvas.pack()
    #värvide nimekiri
    colors = ["red", "orange", "yellow", "green", "blue"]
    #suurenevate ja vähenevate koordinaatide väärtused
    plus = 5
    minus = -5
    #algusringi koordinaadid
    x0, y0 = 0, 0
    x1, y1 = 600, 600
    #60-ringiline joonistustsükkel
    for i in range(60):
        x0 += plus
        y0 += plus
        x1 += minus
        y1 += minus
        canvas.create_oval(x0, y0, x1, y1, fill=choice(colors))

def svetofor():
    svet = tk.Toplevel()
    canvas = tk.Canvas(svet, width=600, height=600, bg="white")
    canvas.pack()
    #valgusfoori jälgimine
    black = canvas.create_rectangle(75, 300, 125, 50, fill="#000000")
    red = canvas.create_rectangle(75, 100, 125, 150, fill="#cfd0d4")
    yellow = canvas.create_rectangle(75, 150, 125, 200, fill="#cfd0d4")
    green = canvas.create_rectangle(75, 200, 125, 250, fill="#cfd0d4")

    #muudab värvid punaseks, kollaseks ja roheliseks
    def changeRed():
        canvas.itemconfig(red, fill="red")
    def changeYellow():
        canvas.itemconfig(yellow, fill="yellow")
    def changeGreen():
        canvas.itemconfig(green, fill="green")
    #ajaintervallid
    canvas.after(4000, changeRed)
    canvas.itemconfig(red, fill="#9e9e9e")
    canvas.after(6000, changeYellow)
    canvas.after(8000, changeGreen)

#peamine aken
raam = tk.Tk()
#Pealkiri
raam.title("Tahvel")
#luua lõuend, millel lipud on
canvas = tk.Canvas(raam, width=600, height=600, background="white")
canvas.grid(row=0, column=0, columnspan=2)

#lipu maalimine
# Estonia
canvas.create_rectangle(30, 50, 300, 100, fill="#1887d6")
canvas.create_rectangle(30, 101, 300, 150, fill="#000000")
canvas.create_rectangle(30, 151, 300, 200, fill="#FFFFFF")

# Bahama lipu
canvas.create_rectangle(30, 250, 300, 300, fill="#078580")
canvas.create_rectangle(30, 301, 300, 350, fill="#e3d002")
canvas.create_rectangle(30, 351, 300, 400, fill="#078580")
canvas.create_polygon(30, 250, 140, 330, 30, 400, fill="black")

# Vengria
canvas.create_rectangle(30, 450, 300, 500, fill="#ff1e00")
canvas.create_rectangle(30, 501, 300, 550, fill="#fcfffa")
canvas.create_rectangle(30, 551, 300, 600, fill="#56cf06")

#loob ribad raadionuppude jaoks
f = tk.Frame(raam)
var = tk.IntVar()
#raadionupu loomine
figur = tk.Radiobutton(f, text="circle and square", variable=var, value=4, command=drawing)
svetofor = tk.Radiobutton(f, text="svetofor", variable=var, value=1, command=svetofor)
circles = tk.Radiobutton(f, text="circles", variable=var, value=2, command=circles)
chess = tk.Radiobutton(f, text="chess", variable=var, value=3, command=chess)

#nupu paigutus
f.grid(row=2, column=0, columnspan=2)
figur.grid(row=0, column=0)
circles.grid(row=1, column=0)
chess.grid(row=2, column=0)
svetofor.grid(row=3, column=0)
#hoiab rakenduse töös
raam.mainloop()
