# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:33:35 2020

@author: timot
"""

import matplotlib.pyplot as plt

import math
import tkinter

def graph(u_max: int, o: int):
    """fonction qui retourne le graphique
    ----
    :pre:
        - u_max est un int et 0 <= u_max <= 10
        - o est un int et -2 <= o <= 2
    """

    # assertion pre
    assert isinstance(u_max, int), \
        "u_max must be a int, not {}".format(type(u_max))
    assert 0 <= u_max <= 10, \
        "u_max must be in [0, 10], not {}".format(u_max)
    assert isinstance(o, int), \
        "o must be a int, not {}".format(type(o))
    assert -2 <= o <= 2, \
        "o must be in [-2, 2], not {}".format(u_max)

    # graphique
    f = 1 / 10 ** -2  # s
    x = []
    y = []
    for t in range(-20, 21):
        x.append(t)
        y.append(u_max * math.sin(2 * math.pi * t + o))
    plt.plot(x, y, label="u=f(t)")
    plt.xlabel("temps (ms)")
    plt.ylabel("tension u (V)")
    plt.title("u = f(t)")
    plt.grid()
    plt.savefig("figure.png")


def refresh(a):
    global curseur_1, curseur_2, img
    graph(curseur_1.get(), curseur_2.get())
    img_cnv = tkinter.PhotoImage(file="figure.png").zoom(50).subsample(12)


def quit_app():
    global window
    window.quit()


# Définition de la fenêtre
window = tkinter.Tk()
window.geometry("500x500+100+100")
window.minsize(500, 500)
window.maxsize(500, 500)
window.title("Graphique")
window.config(background="#333333")

# frame principal
master_frame = tkinter.Frame(window, bg="#777777")

# =============================================================================
# Frame_2
frame_2 = tkinter.Frame(master_frame, bg="red", width=500, height=500)
texte = tkinter.Label(frame_2, text="texte")
texte.pack(expand=tkinter.YES)

curseur_1 = tkinter.Scale(
    frame_2,
    from_=1,
    to=10,
    orient='horizontal',
    label="curseur"
)
curseur_1.pack(expand=tkinter.YES)
curseur_2 = tkinter.Scale(
    frame_2,
    from_=-2,
    to=2,
    orient='horizontal',
    label="curseur"
)

frame_2.grid(row=1, column=0, sticky=tkinter.W)
# =============================================================================

# =============================================================================
# frame qui contient le graph

frame_1 = tkinter.Frame(master_frame, bg="blue")
img = tkinter.PhotoImage(file="figure.png")
refresh(1)
caneva = tkinter.Canvas(frame_1, width=500, height=400)
caneva.create_image(250, 200, image=img)
caneva.pack(expand=tkinter.YES)

frame_1.grid(row=0,column=0, sticky=tkinter.W)
# =============================================================================
# lancement de la fenêtre
master_frame.pack()
window.mainloop()
