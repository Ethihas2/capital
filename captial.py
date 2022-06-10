from tkinter import *
import random

root = Tk()
root.title("Random country and capital")
root.geometry("700x800")

country_entry = Entry(root)
capital_entry = Entry(root)

country_entry.place(relx=0.5,rely=0.2,anchor=CENTER)
capital_entry.place(relx=0.5,rely=0.3,anchor=CENTER)

country_name_label = Label(root)
capital_name_label = Label(root)

random_country_name = Label(root)
random_capital_label= Label(root)

countries = []
capitals = []


def country_add():
    country = country_entry.get()
    capital = capital_entry.get()
    
    countries.append(country)
    capitals.append(capital)
    
    country_name_label["text"]="Country name: " + str(countries)
    capital_name_label["text"]="Capital name: " + str(capitals)
    
    
def random_country():
    
    country_len = len(countries)
    capital_len =len(capitals)
    
    random_countries = random.randint(0,country_len-1)
    random_capital = random.randint(0,capital_len-1)
    
    random_country_name["text"]="Random Country: "+str(countries[random_countries])
    random_capital_label["text"]="Random Capital: "+str(capitals[random_capital])
    
button1=Button(root,text="Display Country and Capital",command=country_add,bg="SteelBlue1")
button1.place(relx=0.5,rely=0.4,anchor=CENTER)
    
country_name_label.place(relx=0.5,rely=0.5,anchor=CENTER)
capital_name_label.place(relx=0.5,rely=0.6,anchor=CENTER)

button2=Button(root,text="Display Country and capital name randomly",command=random_country,bg="SteelBlue1")
button2.place(relx=0.5,rely=0.7,anchor=CENTER)

random_country_name.place(relx=0.5,rely=0.8,anchor=CENTER)
random_capital_label.place(relx=0.5,rely=0.9,anchor=CENTER)

root.mainloop()