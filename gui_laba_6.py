from tkinter import *
from tkinter.messagebox import showinfo


def confirm():

    def get_info():


        # counter = 2
        # while counter > 0:
        #     if ent_conf.get() == ent_pass.get():
        #         showinfo(message='Welcome!')
        #         window.quit()
        #         break
        #     else:
        #         lbl_count['text'] = f'Left to try: {counter}'
        #
        #     counter -= 1


    if ent_name.get() and ent_pass.get():
        window = Tk()
        window.title('confirm')
        window.resizable(width=False, height=False)

        x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2 + 20
        y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2 - 20
        window.wm_geometry("+%d+%d" % (x, y))

        frame = Frame(window)
        frame.pack()

        lbl_conf = Label(frame, text='Repeat password:')
        lbl_conf.grid(column=0, row=0, sticky='w')

        ent_conf = Entry(frame, show='*')
        ent_conf.grid(column=0, row=1)

        lbl_count = Label(frame)
        lbl_count.grid(column=0, row=2, sticky='w', padx=10)

        btn_okk = Button(frame, text='Ok', command=get_info)
        btn_okk.grid(column=0, row=2, sticky='e', padx=10, pady=4)

        window.mainloop()
    else:
        showinfo(message='Login or password error')

window = Tk()
window.title('sign in')
window.resizable(width=False, height=False)

x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
window.wm_geometry("+%d+%d" % (x, y))

window.rowconfigure([0, 1, 2, 3, 4], minsize=1)

frame_pass = Frame(window, borderwidth=2, relief=SUNKEN)
frame_btn = Frame(window)

frame_pass.pack(side=TOP)
frame_btn.pack(side=BOTTOM)

lbl_name = Label(frame_pass, text='Enter name:')
lbl_pass = Label(frame_pass, text='Enter pass:')

lbl_name.grid(column=0, row=0, sticky='w')
lbl_pass.grid(column=0, row=2, sticky='w')

ent_name = Entry(frame_pass)
ent_pass = Entry(frame_pass, show='*')

ent_name.grid(column=0, row=1)
ent_pass.grid(column=0, row=3)

btn_ok = Button(frame_btn, text='Ok', command=confirm)
btn_cancel = Button(frame_btn, text='Cancel', command=exit)

btn_ok.grid(row=4, column=0, pady=3)
btn_cancel.grid(row=4, column=1)

window.mainloop()