from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk

con = mysql.connector.connect(host = 'localhost',
                              user = 'root',
                              password = 'aditi13',
                              database = 'db1')
cur = con.cursor()

                                                                                #Admin page

lwindow = Tk()
lwindow.configure(bg = '#FFF9C7')
lwindow.state("zoomed")

e = []
def sub():
    p = pE.get()
    cur.execute("SELECT * FROM entries")
    data = cur.fetchall()
    for item in data:
        e.append(item)
    print(e)
    print(p)
    x = p
    print(x)
    for i in range(len(e)):
        if x==e[i][1]:
            awindow = Tk()
            awindow.state("zoomed")

            notebooka = ttk.Notebook(awindow)

            lwindow.destroy()
            uwindow.destroy()

            #Check customer's history
            hist = Frame(notebooka)
            hist.configure(bg = '#9E5E6F')
            heading_h = Label (hist, text = "HISTORY OF CUSTOMERS", font = ("Times New Roman", 23))
            heading_h.pack(padx = 10, pady = 45)
            table3 = ttk.Treeview(hist, columns = ('uname', 'name', 'date'), show = 'headings')
            table3.heading ('uname', text = "Name of Customer")
            table3.heading ('name', text = "Name of Book")
            table3.heading ('date', text = "Date")

            table3.pack(padx = 30, pady = 50)

            cur.execute("SELECT * FROM T1")

            i = 0
            for ro in cur:
                table3.insert(parent = '', index = i, iid = None, values = (ro[2], ro[0], ro[1]))
                i = i + 1



            #Packing tabs
            notebooka.add(hist, text = "History")

            notebooka.pack(expand = True, fill = 'both')
            break

    else:
        messagebox.showwarning(title='WARNING!',message='The Password Entered is Wrong')

def swwb():
    lwindow.destroy()


    
#Creating the structure
Label(lwindow, text = '            ', bg = '#FFF9C7').grid(row = 0, column = 0)
logo = Image.open(r"C:\Comp pics\Logo.png")
resize_image = logo.resize((400,250))
imglogo = ImageTk.PhotoImage(resize_image)
labello = Label(lwindow, image=imglogo)
labello.grid(row = 1, column = 3)
Label(lwindow, text = '           ', font = (30), bg = '#FFF9C7').grid(row = 2, column = 4)
Label(lwindow, text = '           ', font = (30), bg = '#FFF9C7').grid(row = 3, column = 4)
headadmin = Label(lwindow, text = 'Only for Admins : ', font = ("Modern No. 20", 30))
headadmin.grid(row = 4, column = 2)
for hh in range(2, 6):   
    Label(lwindow, text = '                    ', bg = '#FFF9C7').grid(row = hh, column = hh)


Label(lwindow, text = '           ', bg = '#FFF9C7').grid(row = 7, column = 4)

uL = Label(lwindow, text = "Username : ", bg = '#FFF9C7', font = ("Algerian", 18, "bold"))
uL.grid(row = 7, column = 1)
uE = Entry(lwindow, font = ("Times New Roman", 20))
uE.grid(row = 7, column = 2)
Label(lwindow, text = '        ', bg = '#FFF9C7').grid(row = 8, column = 1)
pL = Label(lwindow, text = "Password : ",bg = '#FFF9C7', font = ("Algerian", 18, "bold"))
pL.grid(row = 10, column = 1)
pE = Entry(lwindow, show = "*",font = ("Times New Roman", 20))
pE.grid(row = 10, column = 2)
sb = Label(lwindow, text = '       ',bg = '#FFF9C7', font = ("Times New Roman", 20))
sb.grid(row = 11, column = 4)
sb = Button(lwindow, text = "Submit", command = sub, font = ("Modern No. 20", 20))
sb.grid(row = 12, column = 2)
Label(lwindow, text = '         ', bg = '#FFF9C7', font = (30)).grid(row = 13, column = 1)
swb = Button(lwindow, text = "Go to Customer Page ", command = swwb, font = ("Modern No. 20", 25))
swb.grid(row = 10, column = 4)



                                                                                    #Customer page
 
    
def dis1():
    b = []
    def add1():
        n = names.get()
        for index in listbox1.curselection():
            b.insert(index, listbox1.get(index))

        for i in range(len(b)):
            cur.execute("INSERT INTO T1 (UNAME, Name, Date) VALUES ('{}', '{}', curdate())".format(n, b[i]))
            con.commit()

            
    def switch1():
        window2.destroy()
    
    window2 = Tk()
    window2.configure(bg='LavenderBlush2')
    window2.state("zoomed")

    SF = Frame(window2)
    SF.configure(bg='LavenderBlush2')

    title = Label(SF, text = "Science Fiction", bg = 'LavenderBlush2', font = ("Algerian", 40))
    title.grid(row = 0, column = 5)

    Label(SF, text = '', bg = 'LavenderBlush2', font = ("Arial", 15)).grid(row = 1, column = 0)

    listbox1 = Listbox(SF, bg = '#98FF98', font = ("Bodoni MT", 18), width = 14, selectmode = MULTIPLE)
    listbox1.grid(row = 2, column = 0)
    scrollbar = Scrollbar(SF)
    scrollbar.grid(row = 2, column = 1, sticky = 'ns')

    listbox1.insert(1, 'The kill order')
    listbox1.insert(2, 'Sea of Tranquility')
    listbox1.insert(3, 'The Martian')
    listbox1.insert(4, 'Hyperion')
    listbox1.insert(5, 'Brave New World')
    listbox1.insert(6, 'Enders Game')
    listbox1.insert(7, 'Red Rising')
    listbox1.insert(8, 'Kindred')
    listbox1.insert(9, 'Foundation')
    listbox1.insert(10, 'The Left Hand of Darkness')
    listbox1.insert(11, 'The Time Machine')
    listbox1.insert(12, 'Exhalation')
    listbox1.insert(13, 'The War of the Worlds')
    listbox1.insert(14, 'The Three-Body Problem')
    listbox1.insert(15, 'The Stand')
    listbox1.insert(16, 'A Memory called Empire')
    listbox1.insert(17, 'Binti')
    listbox1.insert(18, 'Red Mars')
    listbox1.insert(19, 'Nineteen Eighty-Four')
    listbox1.insert(20, 'Station Elevan')

    listbox1.config(height = 18, width = 35, yscrollcommand = scrollbar.set)
    scrollbar.config(command = listbox1.yview)
    
    Label(SF, text = ' ', bg = 'LavenderBlush2', font = ("Arial", 15)).grid(row = 3, column = 0)

        
    image1 = Image.open(r"C:\Comp pics\SF pic.png")
    resize_image = image1.resize((450,450))
    img = ImageTk.PhotoImage(resize_image)
    labelp = Button(SF, image=img)
    labelp.grid(row = 2, column = 6)

    image2 = Image.open(r"C:\Comp pics\SF pic 2.png")
    resize_image = image2.resize((450,450))
    img2 = ImageTk.PhotoImage(resize_image)
    labels = Button(SF, image=img2)
    labels.grid(row = 2, column = 5)


    bag = Button(SF, text = "Issue the selected books", command = add1, font = ("Arial", 14))
    bag.grid(row = 0, column = 6)


    H1 = Button(SF, text = "Return to Home", command = switch1, font = ("Arial", 14))
    H1.grid(row = 1, column = 6)


    
    SF.grid()
    
    window2.mainloop()


                                                                    #M page
    
def dis2():
    a = []
    n = names.get()
    def add2():
        for index in listbox2.curselection():
            a.insert(index, listbox2.get(index))

        for i in range(len(a)):
            cur.execute("INSERT INTO T1 (UNAME, Name, Date) VALUES ('{}', '{}', curdate())".format(n, a[i]))
            con.commit()

        
    def switch2():
        window3.destroy()
    
    window3 = Tk()
    window3.configure(bg='lightcyan')
    window3.state("zoomed")

    M = Frame(window3)
    M.configure(bg='lightcyan')

    title = Label(M, text = "Mythology", bg='lightcyan', font = ("Algerian", 40))
    title.grid(row = 0, column = 5)

    Label(M, text = ' ', bg='lightcyan', font = ("Arial", 15)).grid(row = 1, column = 0)

    listbox2 = Listbox(M, bg = '#98FF98', font = ("Bodoni MT", 18), width = 14, selectmode = MULTIPLE)
    listbox2.grid(row = 2, column = 0)
    scrollbar1 = Scrollbar(M)
    scrollbar1.grid(row = 2, column = 1, sticky = 'ns')

    listbox2.insert(1, 'Mahabharat vol1')
    listbox2.insert(2, 'Ramayan vol2')
    listbox2.insert(3, 'The Greek Myths')
    listbox2.insert(4, 'Circe')
    listbox2.insert(5, 'Lanka Princess')
    listbox2.insert(6, 'The Pregnant King')
    listbox2.insert(7, 'Ahalya')
    listbox2.insert(8, 'The Palace of Illusions')
    listbox2.insert(9, 'Ariadne')
    listbox2.insert(10, '365 Tales of Indian Mythology')
    listbox2.insert(11, 'Metamorphoses')
    listbox2.insert(12, 'The Hidden Hindu')
    listbox2.insert(13, 'The Silence of the Girls')
    listbox2.insert(14, 'My Gita')
    listbox2.insert(15, 'The King must Die')
    listbox2.insert(16, 'The Penelopiad')
    listbox2.insert(17, 'The Shiva Triology')
    listbox2.insert(18, 'Norse Mythology')
    listbox2.insert(19, 'Mythos')
    listbox2.insert(20, 'The Immortals of Meluha')

    listbox2.config(height = 18, width = 35, yscrollcommand = scrollbar1.set)
    scrollbar1.config(command = listbox2.yview)
    
    Label(M, text = ' ', bg='lightcyan', font = ("Arial", 15)).grid(row = 3, column = 0)
    Label(M, text = ' ', bg='lightcyan', font = ("Arial", 15)).grid(row = 4, column = 8)

    image3 = Image.open(r"C:\Comp pics\M1.png")
    resize_image = image3.resize((450,450))
    img3 = ImageTk.PhotoImage(resize_image)
    labelm3 = Button(M, image=img3)
    labelm3.grid(row = 2, column = 6)

    image4 = Image.open(r"C:\Comp pics\M2.png")
    resize_image = image4.resize((450,450))
    img4 = ImageTk.PhotoImage(resize_image)
    labelm4 = Button(M, image=img4)
    labelm4.grid(row = 2, column = 5)


    bag1 = Button(M, text = "Issue the selected books", command = add2, font = ("Arial", 14))
    bag1.grid(row = 0, column = 6)

    H2 = Button(M, text = "Return to Home", command = switch2, font = ("Arial", 14))
    H2.grid(row = 1, column = 6)


    M.grid()
    window3.mainloop()

    
def dis3():
    c = []
    n = names.get()
    def add3():
        for index in listbox3.curselection():
            c.insert(index, listbox3.get(index))

        for i in range(len(c)):
            cur.execute("INSERT INTO T1 (UNAME, Name, Date) VALUES ('{}', '{}', curdate())".format(n, c[i]))
            con.commit()
            
    def switch3():
        window4.destroy()
    
    window4 = Tk()
    window4.configure(bg='burlywood2')
    window4.state("zoomed")

    D = Frame(window4)
    D.configure(bg='burlywood2')
    
    title = Label(D, text = "Drama", bg='burlywood2', font = ("Algerian", 40))
    title.grid(row = 0, column = 5)

    Label(D, text = '', bg='burlywood2', font = ("Arial", 15)).grid(row = 1, column = 0)

    listbox3 = Listbox(D, bg = '#98FF98', font = ("Bodoni MT", 18), width = 14, selectmode = MULTIPLE)
    listbox3.grid(row = 2, column = 0)
    scrollbar2 = Scrollbar(D)
    scrollbar2.grid(row = 2, column = 1, sticky = 'ns')

    listbox3.insert(1, 'Romeo and Juliet')
    listbox3.insert(2, 'Merchant of Venice')
    listbox3.insert(3, 'Hamlet')
    listbox3.insert(4, 'Othello')
    listbox3.insert(5, 'The Taming of the Shrew')
    listbox3.insert(6, 'My Sisters Keeper')
    listbox3.insert(7, 'Red Rising')
    listbox3.insert(8, 'Macbeth')
    listbox3.insert(9, 'Antigone')
    listbox3.insert(10, 'Jane Eyre')
    listbox3.insert(11, 'The Help')
    listbox3.insert(12, 'Death of a Salesman')
    listbox3.insert(13, 'The Crucible')
    listbox3.insert(14, 'Memoirs of a Geisha')
    listbox3.insert(15, 'King Lear')
    listbox3.insert(16, 'A Dolls house')
    listbox3.insert(17, 'The Tempest')
    listbox3.insert(18, 'A Streetcar Named Desire')
    listbox3.insert(19, 'The Glass Menagerie')
    listbox3.insert(20, 'As you Like it')

    listbox3.config(height = 18, width = 35, yscrollcommand = scrollbar2.set)
    scrollbar2.config(command = listbox3.yview)

    Label(D, text = '    ', bg='lightcyan', font = ("Arial", 15)).grid(row = 3, column = 0)
    Label(D, text = '    ', bg='lightcyan', font = ("Arial", 15)).grid(row = 4, column = 8)

    image5 = Image.open(r"C:\Comp pics\d1.png")
    resize_image = image5.resize((450,450))
    img5 = ImageTk.PhotoImage(resize_image)
    labeld5 = Button(D, image=img5)
    labeld5.grid(row = 2, column = 6)

    image6 = Image.open(r"C:\Comp pics\d2.png")
    resize_image = image6.resize((450,450))
    img6 = ImageTk.PhotoImage(resize_image)
    labeld6 = Button(D, image=img6)
    labeld6.grid(row = 2, column = 5)


    bag2 = Button(D, text = "Issue the selected books", command = add3, font = ("Arial", 14))
    bag2.grid(row = 0, column = 6)

    H3 = Button(D, text = "Return to Home", command = switch3, font = ("Arial", 14))
    H3.grid(row = 1, column = 6)


    D.grid()
    window4.mainloop()
   
def dis4():
    d = []
    n = names.get()
    def add4():
        for index in listbox4.curselection():
            d.insert(index, listbox4.get(index))

        for i in range(len(d)):
            cur.execute("INSERT INTO T1 (UNAME, Name, Date) VALUES ('{}', '{}', curdate())".format(n, d[i]))
            con.commit()
            
    def switch4():
        window5.destroy()
    
    window5 = Tk()
    window5.configure(bg='burlywood2')
    window5.state("zoomed")

    my = Frame(window5)
    my.configure(bg='burlywood2')
    
    title = Label(my, text = "Mystery", bg='burlywood2', font = ("Algerian", 40))
    title.grid(row = 0, column = 5)

    Label(my, text = '', bg='burlywood2', font = ("Arial", 15)).grid(row = 1, column = 0)

    listbox4 = Listbox(my, bg = '#98FF98', font = ("Bodoni MT", 18), width = 14, selectmode = MULTIPLE)
    listbox4.grid(row = 2, column = 0)
    scrollbar3 = Scrollbar(my)
    scrollbar3.grid(row = 2, column = 1, sticky = 'ns')

    listbox4.insert(1, 'Gone Girl')
    listbox4.insert(2, 'Big Little Liars')
    listbox4.insert(3, 'The Big Sleep')
    listbox4.insert(4, 'In the Woods')
    listbox4.insert(5, 'The Alienist')
    listbox4.insert(6, 'One of us is Lying')
    listbox4.insert(7, 'Case Histories')
    listbox4.insert(8, 'Ten')
    listbox4.insert(9, 'Pay Dirt Road')
    listbox4.insert(10, 'The Woman in white')
    listbox4.insert(11, 'The Girl on the Train')
    listbox4.insert(12, 'Killing Floor')
    listbox4.insert(13, 'The Secret History')
    listbox4.insert(14, 'The Moonstone')
    listbox4.insert(15, 'The Detective')
    listbox4.insert(16, 'The Silent Patient')
    listbox4.insert(17, 'Someone had to do it')
    listbox4.insert(18, 'Runner')
    listbox4.insert(19, 'A Dangerous Man')
    listbox4.insert(20, 'The Deep Blue Good-by')


    listbox4.config(height = 18, width = 35, yscrollcommand = scrollbar3.set)
    scrollbar3.config(command = listbox4.yview)

    Label(my, text = '  ', bg='lightcyan', font = ("Arial", 15)).grid(row = 3, column = 0)
    Label(my, text = '  ', bg='lightcyan', font = ("Arial", 15)).grid(row = 4, column = 8)

    image7 = Image.open(r"C:\Comp pics\my1.png")
    resize_image = image7.resize((450,450))
    img7 = ImageTk.PhotoImage(resize_image)
    labelm7 = Button(my, image=img7)
    labelm7.grid(row = 2, column = 6)

    image8 = Image.open(r"C:\Comp pics\my2.png")
    resize_image = image8.resize((450,450))
    img8 = ImageTk.PhotoImage(resize_image)
    labelmy8 = Button(my, image=img8)
    labelmy8.grid(row = 2, column = 5)


    bag3 = Button(my, text = "Issue the selected books", command = add4, font = ("Arial", 14))
    bag3.grid(row = 0, column = 6)

    H4 = Button(my, text = "Return to Home", command = switch4, font = ("Arial", 14))
    H4.grid(row = 1, column = 6)


    my.grid()
    window5.mainloop()

def dis5():
    e = []
    n = names.get()
    def add5():
        for index in listbox5.curselection():
            e.insert(index, listbox5.get(index))

        for i in range(len(e)):
            cur.execute("INSERT INTO T1 (UNAME, Name, Date) VALUES ('{}', '{}', curdate())".format(n, e[i]))
            con.commit()
            
    def switch5():
        window6.destroy()
    
    window6 = Tk()
    window6.configure(bg='burlywood2')
    window6.state("zoomed")

    H = Frame(window6)
    H.configure(bg='burlywood2')
    
    title = Label(H, text = "True Crime", bg='burlywood2', font = ("Algerian", 40))
    title.grid(row = 0, column = 5)

    Label(H, text = '', bg='burlywood2', font = ("Arial", 15)).grid(row = 1, column = 0)

    listbox5 = Listbox(H, bg = '#98FF98', font = ("Bodoni MT", 18), width = 14, selectmode = MULTIPLE)
    listbox5.grid(row = 2, column = 0)
    scrollbar4 = Scrollbar(H)
    scrollbar4.grid(row = 2, column = 1, sticky = 'ns')

    listbox5.insert(1, 'Zodiac')
    listbox5.insert(2, 'In Cold Blood')
    listbox5.insert(3, 'American Predator')
    listbox5.insert(4, 'Helter Skelter')
    listbox5.insert(5, 'Bad Blood')
    listbox5.insert(6, 'Columbine')
    listbox5.insert(7, 'People who eat Darkness')
    listbox5.insert(8, 'Shot in the Heart')
    listbox5.insert(9, 'Killers of the Flower Moon')
    listbox5.insert(10, 'The Red Parts')
    listbox5.insert(11, 'The Devil in the White City')
    listbox5.insert(12, 'Scoundrel')
    listbox5.insert(13, 'The Executioners Song')
    listbox5.insert(14, 'The Stranger Beside Me')
    listbox5.insert(15, 'The Dead Girl')
    listbox5.insert(16, 'I will be Gone in the Dark')
    listbox5.insert(17, 'American Heiress')
    listbox5.insert(18, 'Black Klansman')
    listbox5.insert(19, 'The Fact of a Body')
    listbox5.insert(20, 'The Innocent Man')


    listbox5.config(height = 18, width = 35, yscrollcommand = scrollbar4.set)
    scrollbar4.config(command = listbox5.yview)

    Label(H, text = '  ', bg='lightcyan', font = ("Arial", 15)).grid(row = 3, column = 0)
    Label(H, text = '  ', bg='lightcyan', font = ("Arial", 15)).grid(row = 4, column = 8)

    image9 = Image.open(r"C:\Comp pics\t1.png")
    resize_image = image9.resize((450,450))
    img9 = ImageTk.PhotoImage(resize_image)
    labelH9 = Button(H, image=img9)
    labelH9.grid(row = 2, column = 6)

    image10 = Image.open(r"C:\Comp pics\t2.png")
    resize_image = image10.resize((450,450))
    img10 = ImageTk.PhotoImage(resize_image)
    labelH10 = Button(H, image=img10)
    labelH10.grid(row = 2, column = 5)


    bag4 = Button(H, text = "Issue the selected books", command = add5, font = ("Arial", 14))
    bag4.grid(row = 0, column = 6)

    H5 = Button(H, text = "Return to Home", command = switch5, font = ("Arial", 14))
    H5.grid(row = 1, column = 6)


    H.grid()
    window6.mainloop()


def dis6():
    f = []
    n = names.get()
    def add6():
        for index in listbox6.curselection():
            f.insert(index, listbox6.get(index))

        for i in range(len(f)):
            cur.execute("INSERT INTO T1 (UNAME, Name, Date) VALUES ('{}', '{}', curdate())".format(n, f[i]))
            con.commit()
            
    def switch6():
        window7.destroy()
    
    window7 = Tk()
    window7.configure(bg='burlywood2')
    window7.state("zoomed")

    af = Frame(window7)
    af.configure(bg='burlywood2')
    
    title = Label(af, text = "Adventure Fiction", bg='burlywood2', font = ("Algerian", 40))
    title.grid(row = 0, column = 5)

    Label(af, text = '', bg='burlywood2', font = ("Arial", 15)).grid(row = 1, column = 0)

    listbox6 = Listbox(af, bg = '#98FF98', font = ("Bodoni MT", 18), width = 14, selectmode = MULTIPLE)
    listbox6.grid(row = 2, column = 0)
    scrollbar5 = Scrollbar(af)
    scrollbar5.grid(row = 2, column = 1, sticky = 'ns')

    listbox6.insert(1, 'Journey to the Center of the Earth')
    listbox6.insert(2, 'Life of Pi')
    listbox6.insert(3, 'Treasure of Island')
    listbox6.insert(4, 'Congo')
    listbox6.insert(5, 'Tarzan of the Apes')
    listbox6.insert(6, 'Flashman')
    listbox6.insert(7, 'Lost Horizon')
    listbox6.insert(8, 'Kidnapped')
    listbox6.insert(9, 'Shantaram')
    listbox6.insert(10, 'The Swiss Family of Robinson')
    listbox6.insert(11, 'The Riddle of the Sands')
    listbox6.insert(12, 'The Alchemist')
    listbox6.insert(13, 'The Cruel Sea')
    listbox6.insert(14, 'The Princess Bride')
    listbox6.insert(15, 'The Long Ships')
    listbox6.insert(16, 'The Walking Dream')
    listbox6.insert(17, 'The Call of the Wild')
    listbox6.insert(18, 'The Curse of the Capistrano')
    listbox6.insert(19, 'The Road')
    listbox6.insert(20, 'Hatchet')


    listbox6.config(height = 18, width = 35, yscrollcommand = scrollbar5.set)
    scrollbar5.config(command = listbox6.yview)

    Label(af, text = '  ', bg='lightcyan', font = ("Arial", 15)).grid(row = 3, column = 0)
    Label(af, text = '  ', bg='lightcyan', font = ("Arial", 15)).grid(row = 4, column = 8)

    image11 = Image.open(r"C:\Comp pics\af1.png")
    resize_image = image11.resize((450,450))
    img11 = ImageTk.PhotoImage(resize_image)
    labela11 = Button(af, image=img11)
    labela11.grid(row = 2, column = 6)

    image12 = Image.open(r"C:\Comp pics\af2.png")
    resize_image = image12.resize((450,450))
    img12 = ImageTk.PhotoImage(resize_image)
    labela12 = Button(af, image=img12)
    labela12.grid(row = 2, column = 5)


    bag5 = Button(af, text = "Issue the selected books", command = add6, font = ("Arial", 14))
    bag5.grid(row = 0, column = 6)

    H6 = Button(af, text = "Return to Home", command = switch6, font = ("Arial", 14))
    H6.grid(row = 1, column = 6)


    af.grid()
    window7.mainloop()


def dis7():
    g = []
    n = names.get()
    def add7():
        for index in listbox7.curselection():
            g.insert(index, listbox7.get(index))

        for i in range(len(g)):
            cur.execute("INSERT INTO T1 (UNAME, Name, Date) VALUES ('{}', '{}', curdate())".format(n, g[i]))
            con.commit()
            
    def switch7():
        window8.destroy()
    
    window8 = Tk()
    window8.configure(bg='burlywood2')
    window8.state("zoomed")

    t = Frame(window8)
    t.configure(bg='burlywood2')
    
    title = Label(t, text = "Thriller", bg='burlywood2', font = ("Algerian", 40))
    title.grid(row = 0, column = 5)

    Label(t, text = '', bg='burlywood2', font = ("Arial", 15)).grid(row = 1, column = 0)

    listbox7 = Listbox(t, bg = '#98FF98', font = ("Bodoni MT", 18), width = 14, selectmode = MULTIPLE)
    listbox7.grid(row = 2, column = 0)
    scrollbar6 = Scrollbar(t)
    scrollbar6.grid(row = 2, column = 1, sticky = 'ns')

    listbox7.insert(1, 'Lock Every Door')
    listbox7.insert(2, 'Behind Closed Doors')
    listbox7.insert(3, 'The Girl on the Train')
    listbox7.insert(4, 'Verity')
    listbox7.insert(5, 'The Shining')
    listbox7.insert(6, '400 Days')
    listbox7.insert(7, 'People Like Her')
    listbox7.insert(8, 'Out')
    listbox7.insert(9, 'One by One')
    listbox7.insert(10, 'The Housemaid')
    listbox7.insert(11, 'The Disappearing Act')
    listbox7.insert(12, 'As Good As Dead')
    listbox7.insert(13, 'The Last Thing He Told Me')
    listbox7.insert(14, 'In a Dark, Dark Wood')
    listbox7.insert(15, 'Sharp Objects')
    listbox7.insert(16, 'An Untamed State')
    listbox7.insert(17, 'Stillhouse Lake')
    listbox7.insert(18, 'In Cold Blood')
    listbox7.insert(19, 'Home Before Dark')
    listbox7.insert(20, 'A Flicker in the Dark')


    listbox7.config(height = 18, width = 35, yscrollcommand = scrollbar6.set)
    scrollbar6.config(command = listbox7.yview)

    Label(t, text = '  ', bg='lightcyan', font = ("Arial", 15)).grid(row = 3, column = 0)
    Label(t, text = '  ', bg='lightcyan', font = ("Arial", 15)).grid(row = 4, column = 8)

    image13 = Image.open(r"C:\Comp pics\th1.png")
    resize_image = image13.resize((450,450))
    img13 = ImageTk.PhotoImage(resize_image)
    labelth13 = Button(t, image=img13)
    labelth13.grid(row = 2, column = 6)

    image14 = Image.open(r"C:\Comp pics\th2.png")
    resize_image = image14.resize((450,450))
    img14= ImageTk.PhotoImage(resize_image)
    labelt14 = Button(t, image=img14)
    labelt14.grid(row = 2, column = 5)


    bag6 = Button(t, text = "Issue the selected books", command = add7, font = ("Arial", 14))
    bag6.grid(row = 0, column = 6)

    H7 = Button(t, text = "Return to Home", command = switch7, font = ("Arial", 14))
    H7.grid(row = 1, column = 6)


    t.grid()
    window8.mainloop()


def dis8():
    h = []
    n = names.get()
    def add8():
        for index in listbox8.curselection():
            h.insert(index, listbox8.get(index))

        for i in range(len(h)):
            cur.execute("INSERT INTO T1 (UNAME, Name, Date) VALUES ('{}', '{}', curdate())".format(n, h[i]))
            con.commit()
            
    def switch8():
        window9.destroy()
    
    window9 = Tk()
    window9.configure(bg='burlywood2')
    window9.state("zoomed")

    ft = Frame(window9)
    ft.configure(bg='burlywood2')
    
    title = Label(ft, text = "Fairy Tales", bg='burlywood2', font = ("Algerian", 40))
    title.grid(row = 0, column = 5)

    Label(ft, text = '', bg='burlywood2', font = ("Arial", 15)).grid(row = 1, column = 0)

    listbox8 = Listbox(ft, bg = '#98FF98', font = ("Bodoni MT", 18), width = 14, selectmode = MULTIPLE)
    listbox8.grid(row = 2, column = 0)
    scrollbar7 = Scrollbar(ft)
    scrollbar7.grid(row = 2, column = 1, sticky = 'ns')

    listbox8.insert(1, 'Little Red Riding Hood')
    listbox8.insert(2, '365 Fairy Tales')
    listbox8.insert(3, 'Rapunzel')
    listbox8.insert(4, 'Cinderella')
    listbox8.insert(5, 'Scarlet')
    listbox8.insert(6, 'Puss in Boots')
    listbox8.insert(7, 'Ella Enchanted')
    listbox8.insert(8, 'Woven by Gold')
    listbox8.insert(9, 'Foundation')
    listbox8.insert(10, 'The Princess and the Pea')
    listbox8.insert(11, 'The Green Fairy Book ')
    listbox8.insert(12, 'Exhalation')
    listbox8.insert(13, 'The Ugly Duckling')
    listbox8.insert(14, 'The Hanging City')
    listbox8.insert(15, 'The Fairy-Tale Detectives')
    listbox8.insert(16, 'A Splinder Splintered')
    listbox8.insert(17, 'Fairest of All')
    listbox8.insert(18, 'The Little Blue Bridge')
    listbox8.insert(19, 'Gilded')
    listbox8.insert(20, 'The Seventh Bride')


    listbox8.config(height = 18, width = 35, yscrollcommand = scrollbar7.set)
    scrollbar7.config(command = listbox8.yview)

    Label(ft, text = '  ', bg='lightcyan', font = ("Arial", 15)).grid(row = 3, column = 0)
    Label(ft, text = '  ', bg='lightcyan', font = ("Arial", 15)).grid(row = 4, column = 8)

    image15 = Image.open(r"C:\Comp pics\ft1.png")
    resize_image = image15.resize((450,450))
    img15 = ImageTk.PhotoImage(resize_image)
    labelf1 = Button(ft, image=img15)
    labelf1.grid(row = 2, column = 6)

    image16 = Image.open(r"C:\Comp pics\ft2.png")
    resize_image = image16.resize((450,450))
    img16 = ImageTk.PhotoImage(resize_image)
    labelf2 = Button(ft, image=img16)
    labelf2.grid(row = 2, column = 5)


    bag7 = Button(ft, text = "Issue the selected books", command = add8, font = ("Arial", 14))
    bag7.grid(row = 0, column = 6)

    H8 = Button(ft, text = "Return to Home", command = switch8, font = ("Arial", 14))
    H8.grid(row = 1, column = 6)


    ft.grid()
    window9.mainloop()

 
uwindow = Tk()
uwindow.state("zoomed")

notebook = ttk.Notebook(uwindow)             


def submit():
    n = names.get()
    messagebox.showinfo(title='Entry',message='You have Entered Successfully \n   (Go to Home Tab)')


#Into page
In = Frame(notebook)
In.configure(bg = 'LightSteelBlue3')

Label(In, text = '    ', bg = 'LightSteelBlue3', font = ("Arial", 10)).grid(row = 0, column = 1)
lbl_un = Label(In, text = "VAIVIDYA", font = ('Algerian', 50))
lbl_un.grid(row = 1, column = 5)
Label(In, text = '         ', bg = 'LightSteelBlue3', font = ("Arial", 40)).grid(row = 2, column = 1)
Label(In, text = '        ', bg = 'LightSteelBlue3', font = ("Arial", 40)).grid(row = 3, column = 2)
nameL = Label(In, text = "Name: ", bg = 'LightSteelBlue3', font = ("Algerian", 28))
nameL.grid(row = 5, column = 4)
names = Entry(In, font = ("Bookman Old Style", 25))
names.grid(row = 5, column =5)
Label(In, text = '    ', bg = 'LightSteelBlue3', font = ("Arial", 40)).grid(row = 6, column = 1)
sub = Button(In, text = "SUBMIT", command = submit, font = ("Bookman Old Style", 18))
sub.grid(row = 7, column = 5)

#Home page
hm = Frame(notebook)
hm.configure(bg='LightSteelBlue3')

Label(hm, text = '    ', bg='LightSteelBlue3', font = ("Arial", 20)).grid(row = 0, column = 1)

lbl_hm = Label(hm, text = "HOME PAGE", font = ('Forte', 45, 'bold'))
lbl_hm.grid(row = 1, column = 2)

Label(hm, text = '       ', bg='LightSteelBlue3', font = ("Forte", 30)).grid(row = 2, column = 1)
Label(hm, text = '       ', bg='LightSteelBlue3', font = ("Forte", 30)).grid(row = 3, column = 1)

genre1 = Button(hm, text = "Science Fiction", command = dis1, font = ('Georgia', 30))
genre1.grid(row = 4, column = 0)
Label(hm, text = '    ', bg='LightSteelBlue3', font = ("Arial", 20)).grid(row = 4, column = 1)

genre2 = Button(hm, text = "Mythology", command = dis2, font = ('Georgia', 30))
genre2.grid(row = 4, column = 2)
Label(hm, text = '    ', bg='LightSteelBlue3', font = ("Arial", 20)).grid(row = 4, column = 3)

genre3 = Button(hm, text = "Drama", command = dis3, font = ('Georgia', 30))
genre3.grid(row = 4, column = 4)
Label(hm, text = '    ', bg='LightSteelBlue3', font = ("Arial", 20)).grid(row = 4, column = 5)

genre4 = Button(hm, text = "Mystery", command = dis4, font = ('Georgia', 30))
genre4.grid(row = 4, column = 6)

Label(hm, text = '    ', bg='LightSteelBlue3', font = ("Arial", 30)).grid(row = 5, column = 0)
Label(hm, text = '    ', bg='LightSteelBlue3', font = ("Arial", 30)).grid(row = 6, column = 0)

genre5 = Button(hm, text = "True Crime", command = dis5, font = ('Georgia', 30))
genre5.grid(row = 7, column = 0)

genre6 = Button(hm, text = "Adventure Fiction", command = dis6, font = ('Georgia', 30))
genre6.grid(row = 7, column = 2)


genre7 = Button(hm, text = "Thriller", command = dis7, font = ('Georgia', 30))
genre7.grid(row = 7, column = 4)


genre8 = Button(hm, text = "Fairy Tale", command = dis8, font = ('Georgia', 30))
genre8.grid(row = 7, column = 6)




    
#Bag tab
def table():
    n = names.get()
    table = ttk.Treeview(Bag, columns = ('name', 'date'), show = 'headings')
    table.heading ('name', text = "Name of the Bookz")
    table.heading ('date', text = "Date")
    table.pack(padx = 30, pady = 50)

    cur.execute("SELECT * FROM T1 WHERE UNAME = ('{}')".format(n))

    i = 0
    for ro in cur:
        table.insert(parent = '', index = i, iid = None, values = (ro[1], ro[2]))
        i = i + 1


Bag = Frame(notebook)
Bag.configure(bg='LightSteelBlue3')

t = Button(Bag, text = "THE BOOKS ISSUED:", command = table, font = ('Times New Roman', 24), width = 40, height = 0)
t.pack(padx = 10, pady = 10)
Label(Bag, bg='LightSteelBlue3', width = 60, height = 0).pack()




#Function
def table2():
    n = names.get()
    
    table2 = ttk.Treeview(ret, columns = ('name', 'date'), show = 'headings')
    table2.heading ('name', text = "Name of the Book")
    table2.heading ('date', text = "Date")

    table2.grid(row = 6, column = 4)

    cur.execute("SELECT * FROM T1 WHERE UNAME = ('{}')".format(n))

    if cur == None:
        print("All returned")
    else:
        ii = 0
        for ro in cur:
            table2.insert(parent = '', index = ii, iid = None, values = (ro[1], ro[2]))
            ii = ii + 1
    
lst = []
def exe():
    lst.append(etr.get())
    st = "DELETE FROM T1 WHERE Name = %s"
    cur.execute(st, lst)
    con.commit()
    messagebox.showinfo(title='Return message',message='Successfully returned')
            

        
#Return tab
ret = Frame(notebook)
ret.configure(bg = 'LightSteelBlue3')
Label(ret, text = '                  ', bg = 'LightSteelBlue3', font = ("Arial", 10)).grid(row = 0, column = 0)
lbl = Button(ret, text = "Enter the book to return", font = ("Algerian", 20))
lbl.grid(row = 1, column = 2)
Label(ret, text = '                  ', bg = 'LightSteelBlue3', font = ("Arial", 10)).grid(row = 2, column = 3)
etr = Entry(ret, width = 40, font = ("Bodoni MT", 20))
etr.grid(row = 3, column = 2)
Label(ret, text = '                  ', bg = 'LightSteelBlue3', font = ("Arial", 10)).grid(row = 4, column = 3)
btn = Button(ret, text = "Update", font = ("Bodoni MT", 18), command = exe)
btn.grid(row = 5, column = 2)
Label(ret, text = '                      ', bg = 'LightSteelBlue3', font = ("Arial", 10)).grid(row = 1, column = 3)

btn2 = Button(ret, text = "Show the pending books to return", font = ("Times New Roman", 20), command = table2)
btn2.grid(row = 3, column = 4)


#Packing tabs
notebook.add(In, text = "Introduction")
notebook.add(hm, text = "Home")
notebook.add(Bag, text = "Bag")
notebook.add(ret, text = "Return")


notebook.pack(expand = True, fill = 'both')





