import tkinter as tk
def new_file():
     text.delete('1.0' , tk.END)


def open_file():
    file_path = filedialog.askopenfile(defaultextension=".txt" ,filetypes=[("Text Files","*.txt")])
    if file_path:
        with open(file_path,'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
     file_path = filedialog.askfile(defaultextension= ".txt", filetypes=[("Text Files","*.txt")])
     if file_path:
         with open(file_path,'w') as file:
             file.write(text.get(1.0, tk.END))
             messagebox.showinfo("SUCCESS"," File saved")
root = tk.Tk()
root.title("simple text editor")


menu = tk.Menu(root)
menu.add_cascade(label="File")
menu.add_command(label="New", command=new_file)
menu.add_command(label="Open", command=open_file)
menu.add_command(label="Save", command=save_file)
menu.add_command(label="Exit", command=root.quit)

text = tk.Text(root, wrap=tk.WORD, font=("Helvetica",12), fg="blue")
text.pack(expand=tk.YES, fill=tk.BOTH)
root.mainloop()
