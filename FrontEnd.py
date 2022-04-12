from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from TableWindow import tablewin
'''
Home Screen
'''
root = Tk()
root.title("Gadget Couturier")
root.geometry("1200x800")
b_g = ImageTk.PhotoImage(Image.open("BG.png"))
bg_label = Label(root, image=b_g).grid(row = 0, column = 0, columnspan=1200, rowspan=800)


def casual():
    '''
    Casual Laptop Filtering Screen
    '''
    casual_window = Toplevel()
    casual_window.geometry("800x650")
    bg_label2 = Label(casual_window, image=b_g)
    bg_label2.grid(row = 0, column = 0, columnspan=1200, rowspan=800)
    

    def table():
        '''
        Casual Laptop Table Window and Scatter Generation
        '''
        loadinglabel = Label(casual_window, text="Loading Data...", font=('Helvetica 18'), bg='#000099', fg='yellow').grid(row=370, column=400)

        rrange=rating_range.get()
        prange=price_range.get()
        
        if rrange == 1:
            rmin = 0
        elif rrange == 2:
            rmin = 100
        elif rrange == 3:
            rmin = 500
        elif rrange == 4:
            rmin = 1000
        elif rrange == 5:
            rmin = 5000
        elif rrange == 6:
            rmin = 10000
        
        if prange == 1:
            pmax = 40000
        elif prange == 2:
            pmax = 60000
        elif prange == 3:
            pmax = 80000
        elif prange == 4:
            pmax = 100000
        elif prange == 5:
            pmax = 120000
        elif prange == 6:
            pmax = 1000000

        tablewin(2, pmax, rmin)

    heading = Label(casual_window, text = "CASUAL LAPTOPS", font=('Helvetica 24'), bg='#000099', fg='yellow').grid(row=50, column=400)
    
    subheading1 = Label(casual_window, text = "Ratings Filter", font=('Helvetica 18'), bg='#000099', fg='yellow').grid(row=100, column=400)
    rating_range = IntVar()
    ratingbutton1 = Radiobutton(casual_window, text="0 and above", variable=rating_range, value=1).grid(row=110, column=400)
    ratingbutton2 = Radiobutton(casual_window, text="100 and above", variable=rating_range, value=2).grid(row=120, column=400)
    ratingbutton3 = Radiobutton(casual_window, text="500 and above", variable=rating_range, value=3).grid(row=130, column=400)
    ratingbutton4 = Radiobutton(casual_window, text="1000 and above", variable=rating_range, value=4).grid(row=140, column=400)
    ratingbutton5 = Radiobutton(casual_window, text="5000 and above", variable=rating_range, value=5).grid(row=150, column=400)
    ratingbutton6 = Radiobutton(casual_window, text="10000 and above", variable=rating_range, value=6).grid(row=160, column=400)
    
    subheading2 = Label(casual_window, text = "Price Filter", font=('Helvetica 18'), bg='#000099', fg='yellow').grid(row=210, column=400)
    price_range = IntVar()
    pricebutton1 = Radiobutton(casual_window, text="Upto 40000", variable=price_range, value=1).grid(row=220, column=400)
    pricebutton2 = Radiobutton(casual_window, text="Upto 60000", variable=price_range, value=2).grid(row=230, column=400)
    pricebutton3 = Radiobutton(casual_window, text="Upto 80000", variable=price_range, value=3).grid(row=240, column=400)
    pricebutton4 = Radiobutton(casual_window, text="Upto 100000", variable=price_range, value=4).grid(row=250, column=400)
    pricebutton5 = Radiobutton(casual_window, text="Upto 120000", variable=price_range, value=5).grid(row=260, column=400)
    pricebutton6 = Radiobutton(casual_window, text="Sky's the limit", variable=price_range, value=6).grid(row=270, column=400)

    confirmbutton = Button(casual_window, text="Confirm", padx=20, command=table).grid(row = 320, column = 400)

def gaming():
    '''
    Gaming Laptop FIltering Screen
    '''
    gaming_window = Toplevel()
    gaming_window.geometry("800x650")
    bg_label2 = Label(gaming_window, image=b_g)
    bg_label2.grid(row = 0, column = 0, columnspan=1200, rowspan=800)
    

    def table():
        '''Gaming Laptop Table and Plot Generation'''
        loadinglabel = Label(gaming_window, text="Loading Data...", font=('Helvetica 18'), bg='#000099', fg='yellow').grid(row=370, column=400)

        rrange=rating_range.get()
        prange=price_range.get()
        
        if rrange == 1:
            rmin = 0
        elif rrange == 2:
            rmin = 100
        elif rrange == 3:
            rmin = 500
        elif rrange == 4:
            rmin = 1000
        elif rrange == 5:
            rmin = 2000
        elif rrange == 6:
            rmin = 5000
        
        if prange == 1:
            pmax = 60000
        elif prange == 2:
            pmax = 80000
        elif prange == 3:
            pmax = 100000
        elif prange == 4:
            pmax = 120000
        elif prange == 5:
            pmax = 140000
        elif prange == 6:
            pmax = 10000000

        tablewin(1, pmax, rmin)

    heading = Label(gaming_window, text = "GAMING LAPTOPS", font=('Helvetica 24'), bg='#000099', fg='yellow').grid(row=50, column=400)
    
    subheading1 = Label(gaming_window, text = "Ratings Filter", font=('Helvetica 12'), bg='#000099', fg='yellow').grid(row=100, column=400)
    rating_range = IntVar()
    ratingbutton1 = Radiobutton(gaming_window, text="0 and above", variable=rating_range, value=1).grid(row=110, column=400)
    ratingbutton2 = Radiobutton(gaming_window, text="100 and above", variable=rating_range, value=2).grid(row=120, column=400)
    ratingbutton3 = Radiobutton(gaming_window, text="500 and above", variable=rating_range, value=3).grid(row=130, column=400)
    ratingbutton4 = Radiobutton(gaming_window, text="1000 and above", variable=rating_range, value=4).grid(row=140, column=400)
    ratingbutton5 = Radiobutton(gaming_window, text="2000 and above", variable=rating_range, value=5).grid(row=150, column=400)
    ratingbutton6 = Radiobutton(gaming_window, text="5000 and above", variable=rating_range, value=6).grid(row=160, column=400)
    
    subheading2 = Label(gaming_window, text = "Price Filter", font=('Helvetica 12'), bg='#000099', fg='yellow').grid(row=210, column=400)
    price_range = IntVar()
    pricebutton1 = Radiobutton(gaming_window, text="Upto 60000", variable=price_range, value=1).grid(row=220, column=400)
    pricebutton2 = Radiobutton(gaming_window, text="Upto 80000", variable=price_range, value=2).grid(row=230, column=400)
    pricebutton3 = Radiobutton(gaming_window, text="Upto 100000", variable=price_range, value=3).grid(row=240, column=400)
    pricebutton4 = Radiobutton(gaming_window, text="Upto 120000", variable=price_range, value=4).grid(row=250, column=400)
    pricebutton5 = Radiobutton(gaming_window, text="Upto 140000", variable=price_range, value=5).grid(row=260, column=400)
    pricebutton6 = Radiobutton(gaming_window, text="Sky's the limit", variable=price_range, value=6).grid(row=270, column=400)

    confirmbutton = Button(gaming_window, text="Confirm", padx=20, command=table).grid(row = 320, column = 400)

def mobile():
    '''
    Mobiles Filter Window
    '''
    mobile_window = Toplevel()
    mobile_window.geometry("800x650")
    bg_label2 = Label(mobile_window, image=b_g)
    bg_label2.grid(row = 0, column = 0, columnspan=1200, rowspan=800)
    

    def table():
        '''Mobiles table and scatter genration'''
        loadinglabel = Label(mobile_window, text="Loading Data...", font=('Helvetica 18'), bg='#000099', fg='yellow').grid(row=370, column=400)

        rrange=rating_range.get()
        prange=price_range.get()
        
        if rrange == 1:
            rmin = 0
        elif rrange == 2:
            rmin = 100
        elif rrange == 3:
            rmin = 500
        elif rrange == 4:
            rmin = 1000
        elif rrange == 5:
            rmin = 5000
        elif rrange == 6:
            rmin = 10000
        
        if prange == 1:
            pmax = 10000
        elif prange == 2:
            pmax = 15000
        elif prange == 3:
            pmax = 20000
        elif prange == 4:
            pmax = 25000
        elif prange == 5:
            pmax = 30000
        elif prange == 6:
            pmax = 100000

        tablewin(3, pmax, rmin)

    heading = Label(mobile_window, text = "MOBILES", font=('Helvetica 24'), bg='#000099', fg='yellow').grid(row=50, column=400)
    
    subheading1 = Label(mobile_window, text = "Ratings Filter", font=('Helvetica 18'), bg='#000099', fg='yellow').grid(row=100, column=400)
    rating_range = IntVar()
    ratingbutton1 = Radiobutton(mobile_window, text="0 and above", variable=rating_range, value=1).grid(row=110, column=400)
    ratingbutton2 = Radiobutton(mobile_window, text="100 and above", variable=rating_range, value=2).grid(row=120, column=400)
    ratingbutton3 = Radiobutton(mobile_window, text="500 and above", variable=rating_range, value=3).grid(row=130, column=400)
    ratingbutton4 = Radiobutton(mobile_window, text="1000 and above", variable=rating_range, value=4).grid(row=140, column=400)
    ratingbutton5 = Radiobutton(mobile_window, text="5000 and above", variable=rating_range, value=5).grid(row=150, column=400)
    ratingbutton6 = Radiobutton(mobile_window, text="10000 and above", variable=rating_range, value=6).grid(row=160, column=400)
    
    subheading2 = Label(mobile_window, text = "Price Filter", font=('Helvetica 18'), bg='#000099', fg='yellow').grid(row=210, column=400)
    price_range = IntVar()
    pricebutton1 = Radiobutton(mobile_window, text="Upto 10000", variable=price_range, value=1).grid(row=220, column=400)
    pricebutton2 = Radiobutton(mobile_window, text="Upto 15000", variable=price_range, value=2).grid(row=230, column=400)
    pricebutton3 = Radiobutton(mobile_window, text="Upto 20000", variable=price_range, value=3).grid(row=240, column=400)
    pricebutton4 = Radiobutton(mobile_window, text="Upto 25000", variable=price_range, value=4).grid(row=250, column=400)
    pricebutton5 = Radiobutton(mobile_window, text="Upto 30000", variable=price_range, value=5).grid(row=260, column=400)
    pricebutton6 = Radiobutton(mobile_window, text="Upto 100000", variable=price_range, value=6).grid(row=270, column=400)

    confirmbutton = Button(mobile_window, text="Confirm", padx=20, command=table).grid(row = 320, column = 400)

gaming_button = Button(root, text="Gaming Laptop", padx=50, command=gaming).grid(row=300, column=600)
casual_button = Button(root, text="Casual Laptop", padx=50, command=casual).grid(row=350, column=600)
mobile_button = Button(root, text="Mobile", padx=50, command=mobile).grid(row=400, column=600)

title_label = Label(root, text="GADGET COUTURIER", font=("Helvetica 36"), bg="#000099", fg="yellow").grid(row=200, column=600)



root.mainloop()