from tkinter import *
from tkinter.messagebox import showinfo


def crypt():
    name = [ord(i) for i in ent_name.get()]
    key = [ord(i) for i in ent_key.get()]

    while len(key) < len(name):
        key += key

    result['text'] = ''.join([chr(int(name) ^ int(key)) for name, key in zip(name, key)])

def decrypt():
    d_name = [ord(i) for i in result['text']]
    key = [ord(i) for i in ent_key.get()]

    while len(key) < len(d_name):
        key += key
    result['text'] = ''.join([chr(int(name) ^ int(key)) for name, key in zip(d_name, key)])

def get_info():
    name = [bin(ord(i)) for i in ent_name.get()]
    key = [bin(ord(i)) for i in ent_key.get()]

    info = f'{name[0][2:]}\n{key[0][2:]}\nxor\n{bin(int(name[0][2:], 2) ^ int(key[0][2:], 2))[2:]}'
    showinfo(message=info)

window = Tk()
window.title('calc xor')
window.resizable(width=False, height=False)

x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
window.wm_geometry("+%d+%d" % (x, y))

window.rowconfigure([0, 1, 2], minsize=1)
window.columnconfigure([0, 1], minsize=1)

frm_ent = Frame(window, borderwidth=2, relief=SUNKEN)
frm_ent.pack()

frm_btn = Frame(window)
frm_btn.pack()

ent_name = Entry(frm_ent)
ent_name.grid(row=0, column=1)

ent_key = Entry(frm_ent)
ent_key.grid(row=1, column=1)

lbl_name = Label(frm_ent, text='name:')
lbl_name.grid(row=0, column=0)

lbl_key = Label(frm_ent, text='key:')
lbl_key.grid(row=1, column=0, sticky='e')

lbl_res = Label(frm_ent, text='result:')
lbl_res.grid(row=2, column=0)

result = Label(frm_ent)
result.grid(row=2, column=1, sticky='w')

btn_crypt = Button(frm_btn, text='crypt', command=crypt)
btn_crypt.grid(row=2, column=0, sticky='w', pady=5)

btn_decrypt = Button(frm_btn, text='decrypt', command=decrypt)
btn_decrypt.grid(row=2, column=1, sticky='e')

btn_info = Button(frm_btn, text='info', command=get_info)
btn_info.grid(row=2, column=2, sticky='e')

window.mainloop()