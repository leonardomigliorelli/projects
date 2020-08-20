import tkinter as tk

while True:  # Inserire il tempo
    try:
        tempo = input("Inserisci il tempo (h:m:s)\n").replace(' ', '').split(':')
        assert len(tempo) in [1, 2, 3]

        while len(tempo) < 3:
            tempo.append(0)

        tempo = [int(tempo[i] or 0) for i in range(3)]

        break
    except():
        print('Il valore inserito è errato, usare la formattazione corretta (ore:minuti:secondi)')


class Mainframe(tk.Frame):  # Mainframe contains the widgets

    def __init__(self, master):

        tk.Frame.__init__(self, master)

        self.hour = tk.StringVar()
        tk.Label(self, font=("Helvetica", 100), textvariable=self.hour).pack()

        self.ore = tempo[0]
        self.minuti = tempo[1]
        self.secondi = tempo[2] + 1

        self.timeScaler()

    def timeScaler(self):
        if self.secondi == 0:
            self.secondi = 59
            if self.minuti == 0:
                self.minuti = 59
                if self.ore != 0:
                    self.ore -= 1
            else:
                self.minuti -= 1
        else:
            self.secondi -= 1

        self.hour.set('{:02,}:{:02,}:{:02,}'.format(self.ore, self.minuti, self.secondi))

        if self.ore != 0 or self.minuti != 0 or self.secondi != 0:
            self.after(1000, self.timeScaler)
        else:
            self.timeBlink()

    def timeBlink(self):
        self.hour.set('    :    :    ')
        self.after(1000, self.timeShow)

    def timeShow(self):
        self.hour.set('00:00:00')
        self.after(1000, self.timeBlink)


self = tk.Tk()
self.title("Timer")
self.geometry("400x100")

Mainframe(self).pack()

self.mainloop()
