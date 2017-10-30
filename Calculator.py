from tkinter import *


def icalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj


class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 40 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calc')

        display = StringVar()
        Entry(self, relief = RIDGE,
              textvariable=display,justify='right', bd=30, bg='powder blue').pack(side=TOP, expand=YES, fill=BOTH)

        for clearbut in (["C"]):
            erase = icalc(self,TOP)
            for char in clearbut:
                button(erase, LEFT, char,
                       lambda storeObj = display, q=char:storeObj.set(''))

        for numbut in("789/", "456*", "123-", "0.+"):
            FunctionNum = icalc(self,TOP)
            for ichar in numbut:
                button(FunctionNum, LEFT, ichar,
                       lambda storeObj = display, q=ichar:storeObj.set(storeObj.get()+q))

        EqualsButton = icalc(self, TOP)
        for equals in "=":
           if equals == '=':
               btnequals = button(EqualsButton, LEFT, equals)
               btnequals.bind('<ButtonRelease-1>',
                               lambda e, s=self, storeObj=display: s.calc(storeObj), '+')
           else:
               btnequals = button(EqualsButton, LEFT, equals,
                                  lambda storeObj=display, s=' %s ' %equals: storeObj.set(storeObj.get()+s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ER")

if __name__ == '__main__':
    app().mainloop()
