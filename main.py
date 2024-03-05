import tkinter as tk



def show_pin_panel():
    pin_panel.pack(padx=20, pady=10)


def hide_pin_panel():
    pin_panel.pack_forget()
    pin_panel.tkraise() # opcija ako su okviri jedan ispod drugog kao karte


main_window = tk.Tk()
main_window.title('Smart Key')
main_window.geometry('600x1000')

# Button Panel
button_panel = tk.Frame(main_window)
button_panel.pack(padx=20, pady=(20, 10))

lbl_welcome_message = tk.Label(button_panel,
                               text='Dobro dosli')
lbl_welcome_message.grid(row=0, column=0, columnspan=2)
ring_buton = tk.Button(button_panel,
                       text='Pozvoni - sakrij',
                       command=hide_pin_panel)
ring_buton.grid(row=1, column=0)
unlock_buton = tk.Button(button_panel,
                       text='Otkljucaj',
                       command=show_pin_panel)
unlock_buton.grid(row=1, column=1)



# PIN Panel
pin_panel = tk.Frame(main_window)
lbl_pin = tk.Label(pin_panel,
                   text='Ovo je tekst unutar PIN labele')
lbl_pin.grid(row=0, column=0)



admin_panel = tk.Frame(main_window)
admin_panel.pack(padx=20, pady=(10, 20))



main_window.mainloop()