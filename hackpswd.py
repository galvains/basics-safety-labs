import json
from tkinter import *
from tkinter.messagebox import showinfo

def brute_force():
    try:
        result['text'] = ''
        with open('pswrds.txt') as file:
            data = file.read().split()

            for line in data:
                if ent_pass.get() == line:
                    result['text'] = line
                    break
            else:
                raise KeyError
    except KeyError:
        showinfo(message='Sorry, my dictionary is too stupid for that password 😕')
        # window.destroy()

def dict_hack():
    try:
        with open('data.json') as file:
            data = json.load(file)

            # if ent_pass.get() in data['users']['password']:
            #     result['text'] = data['users']['password']
        for user in data['users']:
            if user['password'] == ent_pass.get():
                result['text'] = user['password']
                break
        else:
            raise KeyError

    except KeyError:
        showinfo(message='Sorry, my dictionary is too stupid for that password 😕')


window = Tk()
window.resizable(False, False)

x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
window.wm_geometry("+%d+%d" % (x, y))

# window.geometry('270x90')

frame = Frame(window, borderwidth=2, relief=GROOVE)
frame.pack(fill=BOTH)

frame_btn = Frame(window)
frame_btn.pack(side=BOTTOM)

lbl_pass = Label(frame, text='Input pass:')
lbl_pass.grid(row=0, column=0, sticky='e')

ent_pass = Entry(frame, show='*')
ent_pass.grid(row=0, column=1)

lbl_res = Label(frame, text='Password: ')
lbl_res.grid(row=2, column=0, sticky='e', pady=2)

result = Label(frame,)
result.grid(row=2, column=1, sticky='w', pady=2)

btn_force = Button(frame_btn, text='brute force', command=brute_force)
btn_dict = Button(frame_btn, text='dict', command=dict_hack)

btn_force.grid(row=3, column=0, pady=3)
btn_dict.grid(row=3, column=1, pady=3)

window.mainloop()

