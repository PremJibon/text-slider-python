from tkinter import *
root = Tk()
root.geometry("900x600")
root.title("Sliding text animation")
txt = "Herokhor"

index = 0
text =''
label =Label(root,text=txt,font=("Arial",30,'bold'),fg='red')
label.pack(pady=100)

def slider():
    global index,text
    if index >=len(txt):
        index=-1
        text=''
        label.config(text=text)
    else:
        text = text+txt[index]
        label.config(text=text)
        index+=1
        label.after(100,slider)
slider()
root.mainloop()