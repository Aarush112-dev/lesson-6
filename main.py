from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Pizza app")
window.geometry("500x400")

def show_order():
    order_text = "You have ordered {} {} {}".format(quantity_name.get(),size,pizza_name)
    your_order.config(text=order_text)
    your_order.place(x=150,y=300)


pizza_hut = Label(window,text="Welcome to Pizza Hut",font=("aerial",12))
pizza_hut.place(x=175,y=50)

fav_pizza = Label(window,text="Select your Fav Pizza",font=("aerial",12))
fav_pizza.place(x=20,y=100)

pizza_name = "Chicago Style"
pizza_box = Combobox(window,textvariable=pizza_name,width=15,height=10)
pizza_box["values"] = ["Chicago Style","Brick Oven Pizza","Italian Pizza","Neapolitan Pizza","California Pizza","New York Style Pizza","Sicilian Pizza","Greek Pizza"]
pizza_box.place(x=200,y=100)

qty_pizza = Label(window,text="Select the qty of pizza",font=("aerial",12))
qty_pizza.place(x=20,y=150)

quantity_name = IntVar()
quantity_pizza = Combobox(window,textvariable=quantity_name,width=15,height=10)
quantity_pizza["values"] = tuple(range(10))
quantity_pizza.place(x=200,y=150)

size = "S"
small = Radiobutton(window,text="S",variable=size,value="S")
medium = Radiobutton(window,text="M",variable=size,value="M")
large = Radiobutton(window,text="L",variable=size,value="L")
small.place(x=350,y=100)
medium.place(x=350,y=125)
large.place(x=350,y=150)

order = Button(window,text="Order",width=25,command=show_order)
order.place(x=150,y=200,height=30)

your_order = Label(window,text="Your order:",font=("aerial",12))
your_order.place(x=50,y=250)

small_cost = Label(window,text="cost of small pizza: £9.99",font=("aerial",12))
small_cost.place(x=450,y=100)
medium_cost = Label(window,text="cost of medium pizza: £19.99",font=("aerial",12))
medium_cost.place(x=450,y=125)
large_cost = Label(window,text="cost of large pizza: £29.99",font=("aerial",12))
large_cost.place(x=450,y=150)


window.mainloop()