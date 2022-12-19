from tkinter import CENTER

from customtkinter import CTk, CTkLabel, CTkButton


def show_msg(title: str, description: str):
    noti = CTk()
    noti.geometry("200x100+200+200")
    noti.title(title)
    noti.resizable(False, False)
    CTkLabel(noti, text=description).place(anchor='n', relx=0.5)
    CTkButton(noti, text="OK", command=lambda: noti.destroy()).place(relx=0.5, rely=0.5, anchor=CENTER)
    noti.mainloop()

