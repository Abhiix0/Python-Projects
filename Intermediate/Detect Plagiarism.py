from tkinter import *

with open('File_1.txt') as f1:
    s1 = f1.read().lower().split()
    l1 = [i for i in s1 if i.isalnum()]

with open('File_2.txt') as f2:
    s2 = f2.read().lower().split()
    l2 = [i for i in s2 if i.isalnum()]

plag_words = len(set(l1).intersection(set(l2)))
total_words = len(l1) + len(l2)
plag_percent = 100 - round((total_words - plag_words * 2) / total_words * 100)

result = "The Plagiarized Content Percent among two files is " + str(plag_percent) + "%"

if plag_percent >= 30 and plag_percent <= 60:
    win = Tk()
    win.geometry("800x200")
    canvas = Canvas(win, width=700, height=650, bg="Yellow")
    canvas.create_text(300, 100, text=result, fill="black", font=('Helvetica', 15, 'bold'))
    canvas.pack()
    win.mainloop()
else:
    win = Tk()
    win.geometry("800x200")
    canvas = Canvas(win, width=700, height=650, bg="Red")
    canvas.create_text(300, 100, text=result, fill="black", font=('Helvetica', 15, 'bold'))
    canvas.pack()
    win.mainloop()
