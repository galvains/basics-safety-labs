import json
from tkinter import *
from tkinter.messagebox import showinfo


def create_json():
    with open('data.json', 'w') as file:

        data = {}
        data['users'] = []
        json.dump(data, file, indent=4, ensure_ascii=False)


def confirm():

    def get_info():

        if ent_repeat.get() == ent_pass.get():
            if showinfo(message='Connection is successful!'):
                window.destroy()

        try:
            with open('data.json') as file:

                data = json.load(file)
                name = ent_name.get()
                password = ent_pass.get()

                new_user = {'username': name, 'password': password}
                data['users'].append(new_user)

                with open('data.json', 'w') as outfile:
                    json.dump(data, outfile,  indent=4, ensure_ascii=False)

        except FileNotFoundError:
            print('[ERROR] json-file not found')

        else:
            count = int(lbl_count['text'][-1])
            if count > 1:
                count -= 1
                lbl_count['text'] = f'Left to try: {str(count)}'
            else:
                if showinfo(message='Connection closed.'):
                    window.destroy()


    try:
        if not ent_name.get() and not ent_pass.get():
            raise KeyError

        window = Tk()
        window.title('Repeat')
        window.resizable(width=False, height=False)

        x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2 + 20
        y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2 - 20
        window.wm_geometry("+%d+%d" % (x, y))

        frame = Frame(window)
        frame.pack()

        lbl_repeat = Label(frame, text='Repeat password:')
        lbl_repeat.grid(column=0, row=0, sticky='w')

        ent_repeat = Entry(frame, show='*')
        ent_repeat.grid(column=0, row=1)

        lbl_count = Label(frame, text='Left to try: 3')
        lbl_count.grid(column=0, row=2, sticky='w', padx=10)

        btn_repeat = Button(frame, text='Ok', command=get_info)
        btn_repeat.grid(column=0, row=2, sticky='e', padx=10, pady=4)

        window.protocol("WM_DELETE_WINDOW", get_info)
        window.mainloop()

    except KeyError:
        showinfo(message='Login or pass error...')


window = Tk()
window.title('sign in')
window.resizable(width=False, height=False)
# window.geometry('250x150')

x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
window.wm_geometry("+%d+%d" % (x, y))

frame_pass = Frame(window, borderwidth=2, relief=SUNKEN)
frame_btn = Frame(window)

frame_pass.pack(side=TOP, fill=BOTH)
frame_btn.pack(side=BOTTOM)

lbl_name = Label(frame_pass, text='name:')
lbl_pass = Label(frame_pass, text='pass:')

lbl_name.grid(column=0, row=0, sticky='w')
lbl_pass.grid(column=0, row=2, sticky='w')

ent_name = Entry(frame_pass)
ent_pass = Entry(frame_pass, show='*')

ent_name.grid(column=1, row=0, sticky='e')
ent_pass.grid(column=1, row=2, sticky='e')

btn_ok = Button(frame_btn, text='Ok', command=confirm)
btn_cancel = Button(frame_btn, text='Cancel', command=window.destroy)
btn_create_json = Button(frame_btn, text='Create json', command=create_json)

btn_ok.grid(row=4, column=0, pady=4)
btn_cancel.grid(row=4, column=1, padx=3)
btn_create_json.grid(row=4, column=2)

window.mainloop()