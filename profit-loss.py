from tkinter import *

def cal():
    if buyvar.get() < sellvar.get():
        result = sellvar.get() - buyvar.get()
        output_display.config(text=f"You Are In Profit Of = Ruppes {result}", fg="Forest Green")
    elif buyvar.get() == sellvar.get():
        result = sellvar.get() - buyvar.get()
        output_display.config(text=f"No Profit, No Loss - You Broke EVEN = Ruppes {result}", fg="Royal Blue")
    else:
        result = buyvar.get() - sellvar.get()
        output_display.config(text=f"You Are In Loss Of = Ruppes {result}", fg="Red")

root = Tk()
root.title("Profit and Loss")
root.geometry("777x888")
root.minsize(333, 444)
root.maxsize(1222, 1333)

f0 = Frame(root, bg="black", borderwidth="10")
f0.pack(expand=True)

f1 = Frame(f0, bg="Light Sky Blue")
f1.pack(expand=True, fill=BOTH)

l1 = Label(f1, text="Either you are In Profit Or Loss", font="comicsansms 30 bold", fg="black", bg="yellow")
l1.grid(row=0, column=0, columnspan=2, pady=20)

buyprice = Label(f1, text="Enter Buying cost", relief=SUNKEN, font="10")
buyprice.grid(row=1, column=0, pady=10)

sellprice = Label(f1, text="Enter Selling Price", relief=SUNKEN, font="10")
sellprice.grid(row=2, column=0, pady=5)

buyvar = IntVar()
sellvar = IntVar()

buy_entry = Entry(f1, textvariable=buyvar)
buy_entry.grid(row=1, column=1, pady=10)

sell_entry = Entry(f1, textvariable=sellvar)
sell_entry.grid(row=2, column=1, pady=5)

Button(f1, text="Calculate", bg="black", fg="white", command=cal).grid(row=3, column=1, pady=5)

output_display = Label(f1, text="", bg="pink", font="comicsansms 15 bold", width=40, relief=GROOVE)
output_display.grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()
