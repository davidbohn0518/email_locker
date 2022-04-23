import tkinter


def write_account():
    email_file = open("email.txt", 'a')
    data = f"{nameEntry.get()}, {emailEntry.get()}, {passwordEntry.get()}\n"
    email_file.writelines(data)
    email_file.close()


mainWindow = tkinter.Tk()

mainWindow.title("Email Locker")
mainWindow.geometry("320x320")
mainWindow['padx'] = 20

label = tkinter.Label(mainWindow, text="Add Email Address")
label.grid(row=0, column=1)

nameVar = tkinter.StringVar()

nameLabel = tkinter.Label(mainWindow, text="Name: ")
nameLabel.grid(row=1, column=0)
nameEntry = tkinter.Entry(mainWindow)
nameEntry.grid(row=1, column=1, columnspan=2)

emailVar = tkinter.StringVar()

emailLabel = tkinter.Label(mainWindow, text="Email: ")
emailLabel.grid(row=2, column=0)
emailEntry = tkinter.Entry(mainWindow)
emailEntry.grid(row=2, column=1, columnspan=2)

passwordVar = tkinter.StringVar()

passwordLabel = tkinter.Label(mainWindow, text="Password: ")
passwordLabel.grid(row=3, column=0)
passwordEntry = tkinter.Entry(mainWindow)
passwordEntry.grid(row=3, column=1, columnspan=2)


addButton = tkinter.Button(mainWindow, text="Add Email", command=write_account)
addButton.grid(row=4, column=1)

resultNameLabel = tkinter.Label(mainWindow, text="Name: ")
resultNameLabel.grid(row=5, column=0, sticky='ew')
resultEmailLabel = tkinter.Label(mainWindow, text="Email: ")
resultEmailLabel.grid(row=5, column=1)
resultPasswordLabel = tkinter.Label(mainWindow, text="Password: ")
resultPasswordLabel.grid(row=5, column=2, sticky='we')

emailList = tkinter.Listbox(mainWindow)
emailList.grid(row=6, column=0, columnspan=3, sticky='nesw', ipadx=0)
emailList.config(border=2, relief='sunken')

with open("email.txt", 'r') as input_file:
    for line in input_file:
        emailList.insert(tkinter.END, line)


mainWindow.mainloop()

