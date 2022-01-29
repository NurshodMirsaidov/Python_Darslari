from datetime import datetime
from tkinter import *

oyna = Tk()
oyna.title("Dasturcha :)")
oyna.geometry("300x300")

natija = Label(text = "Natija", bg="grey")
natija.place(x = 100, y = 145, width = 130, height = 50)

yil = Entry()
yil.place(x = 85, y = 60, width = 160, height = 40)

def farq():
    bugun = datetime.today()
    natija.config(text = bugun.year - int(yil.get())) 

tugma = Button(text = "Hisoblash", command = farq, bg="green")
tugma.place(x = 100, y = 100, width = 130, height = 50)

oyna.mainloop()


# def farq(yil):
#     bugun = datetime.today()
#     natija = bugun.year - int(yil)
#     return natija

# tugilgan_yil = input("Tug`ilgan yilni kiriting: ")
# natija_f =farq(tugilgan_yil)

# print("Natija: ", natija_f)

# maktab_yil = int(input("Yilni kiriting: "))
# natija_f =farq(maktab_yil)
# print("Natija: ", natija_f)