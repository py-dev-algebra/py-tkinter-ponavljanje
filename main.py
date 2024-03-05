import tkinter as tk
from tkinter import IntVar, BooleanVar



def show_pin_panel():
    pin_panel.pack(padx=20, pady=10)


def hide_pin_panel(panel):
    panel.pack_forget() # Ako se koristi grid: button_panel.grid_remove(); Ako se koristi place: button_panel.place_forget()
    panel.tkraise() # opcija ako su okviri jedan ispod drugog kao karte


main_window = tk.Tk()
main_window.title('Smart Key')
main_window.geometry('600x1000')



#region Button Panel
button_lbl_frame = tk.LabelFrame(main_window, text='Button frame', padx=30, pady=30)
button_lbl_frame.pack(padx=20, pady=(20, 10))

lbl_welcome_message = tk.Label(button_lbl_frame,
                               text='Dobro dosli')
lbl_welcome_message.grid(row=0, column=0, columnspan=2)
ring_buton = tk.Button(button_lbl_frame,
                       text='Pozvoni - sakrij',
                       command=lambda : hide_pin_panel(pin_panel))
ring_buton.grid(row=1, column=0)
unlock_buton = tk.Button(button_lbl_frame,
                       text='Otkljucaj',
                       command=show_pin_panel)
unlock_buton.grid(row=1, column=1)
#endregion



#region PIN Panel
pin_panel = tk.Frame(main_window)

# CheckBox
cb_expand_var = IntVar()
lbl_expand = tk.Label(pin_panel, text="Expand")
lbl_expand.grid(row=0, column=0)
cb_expand = tk.Checkbutton(pin_panel, variable=cb_expand_var)
cb_expand.grid(row=0, column=1)


lbl_pin = tk.Label(pin_panel,
                   textvariable=cb_expand_var)
lbl_pin.grid(row=1, column=0)


lbl_name = tk.Label(pin_panel, text="Ime")
lbl_name.grid(row=2, column=0)
entry_name = tk.Entry(pin_panel)
entry_name.grid(row=2, column=1)




#endregion







admin_panel = tk.Frame(main_window)
admin_panel.pack(padx=20, pady=(10, 20))



main_window.mainloop()
