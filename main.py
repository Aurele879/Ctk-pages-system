import customtkinter


class Window: # Class defining a window and its functions
    def __init__(self): # Class constructor
        self.root = customtkinter.CTk()
        self.root.geometry("1000x600")
        self.root.title("My App")
        self.root.configure(fg_color="#FFFFFF")
        self.num = 0
        self.setupWidgets()
        
    def setupWidgets(self): # Fuction to create all the widgets of the whole window
        self.explButton = customtkinter.CTkButton(self.root,
                                                command=self.nextPage,
                                                fg_color="#348D5C",
                                                bg_color="#FFFFFF",
                                                hover_color="#24512F",
                                                text="NEXT",
                                                width=200,
                                                height=50,
                                                corner_radius=20,
                                                font=("Arial", 25, "bold"))   
                
    def clearUi(self): # Fuction to hide all the widgets from the screen
        self.explButton.place_forget()

    def thirdPage(self): # Fuction to place all the widgets from the page
        self.clearUi()
        self.explButton.place(x=35, y=200)

    def mainPage(self): # Fuction to place all the widgets from the page
        self.clearUi()
        self.explButton.place(x=525, y=470)

    def secondPage(self): # Fuction to place all the widgets from the page
        self.clearUi()
        self.explButton.place(x=500, y=500)

    def nextPage(self): # Fuction to switch pages with an incremented variable
        if self.num < 2:
            self.num +=1
        else:
            self.num = 0
        print(f"Page {self.num+1}")
        if self.num == 0:
            self.mainPage()
        elif self.num == 1:
            self.secondPage()
        elif self.num == 2:
            self.thirdPage()

    def display(self): # Fuction to display the window
        self.mainPage()
        self.root.mainloop()
        
app = Window()
app.display()