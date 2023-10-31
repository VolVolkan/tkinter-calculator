from tkinter import *
sys = 10

from tktooltip import ToolTip


cWin = Tk()
cWin.geometry("330x460")
cWin.title("the CALC")
cWin.eval('tk::PlaceWindow . center')
cWin.resizable(True, False)

cWin.config(background='#000022')
photo = PhotoImage(file="icon.png")
cWin.iconphoto(False, photo)


change = IntVar()


textin = StringVar()
source = ""







def cl():
    global source

    x = "".join([source[i] for i in range(len(source)-1)])
    source = x
    textin.set(source)


def click(number):
    global source
    source += str(number)
    textin.set(source)
    

def cbuton(number):
    global source
    source = source+str(number)
    textin.set(source)


def convertor(system):
    global sys
    if system is None:
        sys = 10
    else:
        sys = system
        print(sys)
    
    return sys

def equa():
    global source
    input_string = source
    
    system = sys
    if system == 2:
        
        def check_characters_in_string(character_list, input_string,):
                for char in character_list:
                    if char in input_string:
                        
                         
                        index = input_string.find(char)
                        #finding operator
                        operator = (input_string[index:-index])
                        # extracting to two parts
                        first_part = input_string[:index]
                        second_part = input_string[(index+1):]
                        #first_part= int(first_part)
                        #second_part = int(second_part)
                        if char == "+":
                            valuhex = bin(int(first_part,2)+ int(second_part,2))
                            textin.set(valuhex[2:])
                            source = (valuhex[2:])
                        if char == "-":
                           valuhex = bin(int(first_part,2)- int(second_part,2))
                           textin.set(valuhex[2:])
                           source = (valuhex[2:])
                        if char == "*":
                            valuhex = bin(int(first_part,2)* int(second_part,2))
                            textin.set(valuhex[2:])
                            source = (valuhex[2:])
                        if char == "/":
                            valuhex = bin(int(first_part,2)/ int(second_part,2))
                            textin.set(valuhex[2:])
                            source = (valuhex[2:])
        character_list = ['+', '-', '*',"/"]
        #input_string = source

        result = check_characters_in_string(character_list, input_string, )

        print(result)
    if system == 10:
        
        sub = str(eval(source))
        textin.set(sub)
        source = sub
    
    if system == 16:
    
        def check_characters_in_string(character_list, input_string,):
                for char in character_list:
                    if char in input_string:
                        
                         
                        index = input_string.find(char)
                        #finding operator
                        operator = (input_string[index:-index])
                        # extracting to two parts
                        first_part = input_string[:index]
                        second_part = input_string[(index+1):]
                        #first_part= int(first_part)
                        #second_part = int(second_part)
                        if char == "+":
                            valuhex = hex(int(first_part,16)+ int(second_part,16))
                            textin.set(valuhex[2:])
                            source = (valuhex[2:])
                        if char == "-":
                           valuhex = hex(int(first_part,16)- int(second_part,16))
                           textin.set(valuhex[2:])
                           source = (valuhex[2:])
                        if char == "*":
                            valuhex = hex(int(first_part,16)* int(second_part,16))
                            textin.set(valuhex[2:])
                            source = (valuhex[2:])
                        if char == "/":
                            valuhex = hex(int(first_part,16)/ int(second_part,16))
                            textin.set(valuhex[2:])
                            source = (valuhex[2:])
                            
                # using
        character_list = ['+', '-', '*',"/"]
        #input_string = source

        result = check_characters_in_string(character_list, input_string, )

        print(result)


"""

def equa():
    global source
    mul = str(eval(source))
    textin.set(mul)
    source = nul
"""



def modbut():
    global source
    mod = str(eval(source))
    textin.set(mod)
    source = ''


def clrbut():
    global source
    textin.set('EMPTY')
    source = ''


# cWin.bind('<>',lambda event:clrbut())
def tipfortool(button, msg):

    return ToolTip(button, msg, delay=1, fg="cyan", bg="black")


def Class():
    cWin.geometry("330x460")
    cframe = Frame(cWin)
    cframe.destroy()
    cframe = Frame(cWin, bg="#000022")
    cframe.place(height=460, width=330, y=1)

    title = Menubutton(cframe, text="__--__", bg='#000000', activebackground="black",
                       fg="cyan", font=("Times", 34, 'bold'), width=9, height=1)
    
    title.menu = Menu(title, tearoff=0, bg="black", fg="cyan")
    title["menu"] = title.menu
    title.pack(side=TOP)
    title.menu.add_radiobutton(
        label='Classic', variable=change, value=1, command=Class)
    title.menu.add_radiobutton(
        label='Special', variable=change, value=2, command=Spec)

    metext = Entry(cframe, font=("overstrike", 12, 'bold'), textvar=textin,
                   width=25, bd=6, bg='#333395', fg='#00fff0', cursor="arrow")
    metext.pack(side=TOP)

    textin.set('Emtpy')


    b1 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click(1), text="1", font=("Courier New", 16, 'bold'))
    b1.place(x=10, y=100)

    b2 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click(2), text="2", font=("Courier New", 16, 'bold'))
    b2.place(x=75, y=100)

    b3 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click(3), text="3", font=("Courier New", 16, 'bold'))
    b3.place(x=140, y=100)

    but2 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                  command=lambda: click(4), text="4", font=("Courier New", 16, 'bold'))
    but2.place(x=10, y=170)

    b5 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click(5), text="5", font=("Courier New", 16, 'bold'))
    b5.place(x=75, y=170)

    b6 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click(6), text="6", font=("Courier New", 16, 'bold'))
    b6.place(x=140, y=170)

    b7 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click(7), text="7", font=("Courier New", 16, 'bold'))
    b7.place(x=10, y=240)

    b8 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click(8), text="8", font=("Courier New", 16, 'bold'))
    b8.place(x=75, y=240)

    b9 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click(9), text="9", font=("Courier New", 16, 'bold'))
    b9.place(x=140, y=240)

    b0 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click(0), text="0", font=("Courier New", 16, 'bold'))
    b0.place(x=10, y=310)

    bdot = Button(cframe, padx=48, pady=14, bd=4, bg='#0c1421', fg='cyan',
                  command=lambda: click("."), text=".", font=("Courier New", 16, 'bold'))
    bdot.place(x=75, y=310)
    tipfortool(bdot, "why you looking this text are you want to find my mistakes?")

    bplu = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                  text="+", command=lambda: click("+"), font=("Courier New", 16, 'bold'))
    bplu.place(x=205, y=100)
    tipfortool(bplu, "simple addition")

    sub = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                 text="-", command=lambda: click("-"), font=("Courier New", 16, 'bold'))
    sub.place(x=205, y=170)
    tipfortool(sub, "simple extraction")

    mp = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                text="*", command=lambda: click("*"), font=("Courier New", 16, 'bold'))
    mp.place(x=205, y=240)
    tipfortool(
        mp, "one click(*): muptiply \ntwo click(**): ower expression of first number ")

    div = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                 text="/", command=lambda: click("/"), font=("Courier New", 16, 'bold'))
    div.place(x=205, y=310)
    tipfortool(
        div, "one click(/): simple division \ntwo click(//): division with integer result ")
    butbut = Button(cframe, padx=14, pady=30, bd=4, bg='#0c1421',
                    fg='cyan', text="←", command=cl, font=("Courier New", 16, 'bold'))
    butbut.place(x=270, y=100)
    tipfortool(butbut, "Backspace")
    butclear = Button(cframe, padx=14, pady=100, bd=4, bg='#000000', fg='white', text="C",
                      activeforeground="cyan", activebackground="red", command=clrbut, font=("Courier New", 16, 'bold'))
    butclear.place(x=270, y=208)
    tipfortool(butclear, "Clear all")

    butequal = Button(cframe, padx=48, pady=14, bd=4, bg='#032dff',
                      fg='cyan', command=equa, text="=", font=("Courier New", 16, 'bold'))
    butequal.place(x=140, y=380)

    butw = Button(cframe, padx=35, pady=14, bd=4, bg='#0c1421', fg='#47a2a8',
                  command=lambda: cbuton("%"), text="mod", font=("Courier New", 16, 'bold'))
    butw.place(x=10, y=380)
    alls = cframe.place_slaves()









def Spec():
    cWin.geometry("530x460")
    cframe = Frame(cWin)
    cframe.destroy()
    cframe = Frame(cWin, bg="#090925")
    cframe.place(width=530, height=460, y=1)
    
    title = Menubutton(cframe, text="__--__", bg='#000000', activebackground="black",
                       fg="cyan", font=("Times", 34, 'bold'), width=9, height=1)
    title.place()
    title.menu = Menu(title, tearoff=0, bg="black", fg="cyan")
    title["menu"] = title.menu
    title.place(x=164, y=0)
    title.menu.add_radiobutton(
        label='Classic', variable=change, value=1, command=Class)
    title.menu.add_radiobutton(
        label='Special', variable=change, value=2, command=Spec)



    
    def octa():
        convertor(10)
    def hexa():
        convertor(16)
    def bina():
        convertor(2)

    typ = IntVar()
    title.menu.add_radiobutton(label='Oct', variable=typ,value = 1,command=octa)
    title.menu.add_radiobutton(label='Bin', variable=typ,value = 2,command=bina)
    title.menu.add_radiobutton(label='Hex', variable=typ,value= 3,command=hexa)
    metext = Entry(cframe, font=("overstrike", 12, 'bold'), textvar=textin,
                   width=33, bd=6, bg='#333395', fg='#00fff0', cursor="arrow")
    metext.place(y=55, x=20)
    xetext = Entry(cframe, font=("overstrike", 12, 'bold'), textvar=textin,
                   width=10, bd=6, bg='#933395', fg='#00fff0', cursor="arrow")
    xetext.place(y=55, x=406)
    
    textin.set('Emtpy')

    b1 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click(1), text="1", font=("Courier New", 16, 'bold'))
    b1.place(x=10, y=100)

    b2 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click(2), text="2", font=("Courier New", 16, 'bold'))
    b2.place(x=75, y=100)

    b3 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click(3), text="3", font=("Courier New", 16, 'bold'))
    b3.place(x=140, y=100)

    but2 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                  command=lambda: click(4), text="4", font=("Courier New", 16, 'bold'))
    but2.place(x=10, y=170)

    b5 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click(5), text="5", font=("Courier New", 16, 'bold'))
    b5.place(x=75, y=170)

    b6 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click(6), text="6", font=("Courier New", 16, 'bold'))
    b6.place(x=140, y=170)

    b7 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click(7), text="7", font=("Courier New", 16, 'bold'))
    b7.place(x=10, y=240)

    b8 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click(8), text="8", font=("Courier New", 16, 'bold'))
    b8.place(x=75, y=240)

    b9 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click(9), text="9", font=("Courier New", 16, 'bold'))
    b9.place(x=140, y=240)

    b0 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click(0), text="0", font=("Courier New", 16, 'bold'))
    b0.place(x=205, y=310)
    b0 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click('a'), text="A", font=("Courier New", 16, 'bold'))
    b0.place(x=10, y=310)
    b0 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click('b'), text="B", font=("Courier New", 16, 'bold'))
    b0.place(x=75, y=310)
    b0 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click('c'), text="C", font=("Courier New", 16, 'bold'))
    b0.place(x=140, y=310)
    b0 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click('d'), text="D", font=("Courier New", 16, 'bold'))
    b0.place(x=10, y=380)
    b0 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click('e'), text="E", font=("Courier New", 16, 'bold'))
    b0.place(x=75, y=380)
    b0 = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                command=lambda: click('f'), text="F", font=("Courier New", 16, 'bold'))
    b0.place(x=140, y=380)

    bdot = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                  command=lambda: click("."), text=".", font=("Courier New", 16, 'bold'))
    bdot.place(x=205, y=240)
    tipfortool(bdot, "why you looking this text are you want to find my mistakes?")

    bplu = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                  text="+", command=lambda: click("+"), font=("Courier New", 16, 'bold'))
    bplu.place(x=205, y=100)
    tipfortool(bplu, "simple addition")

    sub = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                 text="-", command=lambda: click("-"), font=("Courier New", 16, 'bold'))
    sub.place(x=205+65, y=100)
    tipfortool(sub, "simple extraction")

    mp = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                text="*", command=lambda: click("*"), font=("Courier New", 16, 'bold'))
    mp.place(x=335, y=100)
    tipfortool(
        mp, "one click(*): muptiply \ntwo click(**): ower expression of first number ")

    div = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                 text="/", command=lambda: click("/"), font=("Courier New", 16, 'bold'))
    div.place(x=400, y=100)
    tipfortool(
        div, "one click(/): simple division \ntwo click(//): division with integer result ")
    butbut = Button(cframe, padx=14, pady=30, bd=4, bg='#0c1421',
                    fg='cyan', text="←", command=cl, font=("Courier New", 16, 'bold'))
    butbut.place(x=470, y=100)
    tipfortool(butbut, "Backspace")
    butclear = Button(cframe, padx=14, pady=100, bd=4, bg='#000000', fg='white', text="C",
                      activeforeground="cyan", activebackground="red", command=clrbut, font=("Courier New", 16, 'bold'))
    butclear.place(x=470, y=208)
    tipfortool(butclear, "Clear all")

    butequal = Button(cframe, padx=48, pady=14, bd=4, bg='#032dff',
                      fg='cyan', command=equa, text="=", font=("Courier New", 16, 'bold'))
    butequal.place(x=335, y=380)

    butw = Button(cframe, padx=35, pady=14, bd=4, bg='#0c1421', fg='#47a2a8',
                  command=lambda: cbuton("%"), text="mod", font=("Courier New", 16, 'bold'))
    butw.place(x=205, y=170)
    butkok = Button(cframe, padx=14, pady=14, bd=4,  bg='#0c1421', fg='#47a2a8',text="√", font=("Courier New",16,'bold'))
    butkok.place(x=335, y=170)
    tipfortool(butkok, "Not working now")
    butpar = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                  text="(", command=lambda: click("("), font=("Courier New", 16, 'bold'))
    butpar.place(x=335, y=170)
    butpar = Button(cframe, padx=14, pady=14, bd=4, bg='#0c1421', fg='cyan',
                  text=")", command=lambda: click(")"), font=("Courier New", 16, 'bold'))
    butpar.place(x=400, y=170)
    alls = cframe.place_slaves()


Class()


cWin.mainloop()
