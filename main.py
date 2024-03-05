import tkinter as tk
from tkinter import IntVar, StringVar

from databse_manager import get_names_from_db, get_user


def show_pin_panel():
    pin_panel.pack(padx=20, pady=10)


def hide_pin_panel(panel):
    panel.pack_forget() # Ako se koristi grid: button_panel.grid_remove(); Ako se koristi place: button_panel.place_forget()
    panel.tkraise() # opcija ako su okviri jedan ispod drugog kao karte


def leave(event):
    print(f'Mis nije iznad gumba. {event}')


def on_element_clicked(event):
    index = lbox_names.curselection()
    value = lbox_names.get(index)
    user = get_user(value.split(' ')[0])
    # TODO popuniti vrijednosti u widgetima preko Vars (StringVar, IntVar ...)

    print(f'Index {index}; Value: {value}')


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

#region CheckBox
cb_expand_var = IntVar()
lbl_expand = tk.Label(pin_panel, text="Expand")
lbl_expand.grid(row=0, column=0)
cb_expand = tk.Checkbutton(pin_panel, variable=cb_expand_var)
cb_expand.grid(row=0, column=1)
#endregion


lbl_pin = tk.Label(pin_panel,
                   textvariable=cb_expand_var)
lbl_pin.grid(row=1, column=0)


lbl_name = tk.Label(pin_panel, text="Ime")
lbl_name.grid(row=2, column=0)
entry_name = tk.Entry(pin_panel)
entry_name.grid(row=2, column=1)


#region ListBox
lbox_names = tk.Listbox(pin_panel)
lbox_names.grid(row=3,column=0)
# lbox_names.insert(tk.END, 'Pero Peric')
# lbox_names.insert(tk.END, 'Ana Anic')

# names = ['Pero Peric', 'Ana Anic', 'Marko Maric', 'Iva Ivic', 'Vinko Vinic']
names = get_names_from_db()
for name in names:
    lbox_names.insert(tk.END, name)
lbox_names.bind('<ButtonRelease-1>', on_element_clicked)
#endregion


btn_demo = tk.Button(pin_panel,
                     text='Demo',
                     font=('Segoe UI', 15))
btn_demo.grid(row=4, column=0, pady=20)
btn_demo.bind('<Leave>', leave)

lbl_demo_var = StringVar()
lbl_demo_var.set('Pocetna vrijednost')
lbl_demo = tk.Label(pin_panel,
                    textvariable=lbl_demo_var,
                    font=('Segoe UI', 15))
lbl_demo.grid(row=5, column=0, pady=20)

#endregion



admin_panel = tk.Frame(main_window)
admin_panel.pack(padx=20, pady=(10, 20))




if __name__ == '__main__':
    # funkcija koja ce kreirati bazu i napuniti je inicijalnim podacima
    # create_tables()
    # database_seed()
    main_window.mainloop()
