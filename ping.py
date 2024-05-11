import tkinter as tk
from pythonping import ping


ips = ['8.8.8.8', '4.2.2.4', '1.1.1.1','google.com']
labels = []

class PingApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry('350x200')
        listbox = tk.Listbox( height = 5, 
                  width = 8, 
                  bg = "grey",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "yellow")
        listbox.insert(1, "Nachos")
        listbox.insert(2, "Sandwich")
        listbox.pack()
        self.create_widgets()

    def create_widgets(self):
        for i, ip in enumerate(ips):
            label = tk.Label(self.master, font=('Consolas', 12), bg='yellow')
            label.pack()
            labels.append(label)
        self.update()

    def update(self):
        for i, ip in enumerate(ips):
            s_1 = ping(ip, count=1)
            labels[i].config(text=f'{ip}: {s_1.rtt_avg_ms} ms')
        self.master.after(500, self.update)

root = tk.Tk()
root.configure(background='yellow')
root.title("Ping App")
root.iconbitmap("icon.ico")
app = PingApp(root)
root.mainloop()