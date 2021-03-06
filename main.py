# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 08:58:23 2020

@author: timot
"""

import matplotlib.pyplot as plt


import tkinter
import math


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
        y.append(u_max * math.sin(2 * math.pi * f * t + o))
    plt.plot(x, y, label="u=f(t)")
    plt.xlim(-20, 20)
    plt.xlabel("temps (ms)")
    plt.ylabel("tension u (V)")
    plt.title("u = f(t)")
    plt.grid()
    plt.savefig("figure.png")
    plt.close()


def refreshaaaaa():
    global scale_amplitude, scale_phase, img_cnv, caneva
    graph(scale_amplitude.get(), scale_phase.get())
    caneva.delete("all")
    img_cnv = tkinter.PhotoImage(file="figure.png")
    caneva.create_image(250, 200, image=img_cnv)


def quit_app():
    global window
    window.quit()


# Définition de la fenêtre
window = tkinter.Tk()
window.geometry(
    "500x500+{}+{}".format(
        window.winfo_screenwidth()//3,
        window.winfo_screenheight()//3
    )
)
window.minsize(500, 500)
window.maxsize(500, 500)
window.title("Graphique")

# frame principal
master_frame = tkinter.Frame(window)

# =============================================================================
# frame qui contient les curseur et bouton
frame_2 = tkinter.Frame(master_frame)

# curseur phase
scale_phase = tkinter.Scale(
    frame_2,
    from_=-2,
    to=2,
    orient="horizontal",
    label="Phase (rad)"
)
scale_phase.set(1)
scale_phase.grid(row=0, column=1, sticky=tkinter.W)

# curseur amplictude
scale_amplitude = tkinter.Scale(
    frame_2,
    from_=0,
    to=10,
    orient="horizontal",
    label="amplitude"

)
scale_amplitude.set(3)
scale_amplitude.grid(row=0, column=2, sticky=tkinter.W)

# bouton update
update_button = tkinter.Button(
    frame_2,
    text="Update",
    command=refreshaaaaa
)
update_button.grid(row=0, column=0, sticky= tkinter.W)
quit_button = tkinter.Button(
    frame_2,
    text="quitter",
    command=quit_app
)
quit_button.grid(row=0, column=3, sticky=tkinter.W)

frame_2.grid(row=1, column=0, sticky=tkinter.W)
# =============================================================================

# =============================================================================
# frame qui contient le graph

frame_1 = tkinter.Frame(master_frame, width=500, height=400)
caneva = tkinter.Canvas(frame_1, width=500, height=400)
refreshaaaaa()
caneva.create_image(250, 250, image=img_cnv)
caneva.pack()

frame_1.grid(row=0,column=0, sticky=tkinter.W, expand=tkinter.YES)
# =============================================================================
# lancement de la fenêtre
master_frame.pack()
window.mainloop()
