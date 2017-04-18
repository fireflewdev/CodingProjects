import tkinter as tk

LARGE_FRONT = ("Verdana",12)
SMALL_FONT = ("Verdana", 8)


        

class CreatePT(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0,weight = 1)
        container.grid_columnconfigure(0,weight = 1)

        self.frames = {}

        for F in (WelcomePage, AAAPage, AASPage, ASAPage, SSAPage, SASPage, SSSPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame(WelcomePage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class WelcomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Welcome to the Triangle Solver", font = LARGE_FRONT)
        label.pack(pady=10,padx=10)

        AAA_Button = tk.Button(self, text = "AAA(Angle-Angle-Angle)",
                           command=lambda: controller.show_frame(AAAPage))
        AAA_Button.pack()

        AAS_Button = tk.Button(self, text = "AAS(Angle-Angle-Side)",
                               command=lambda: controller.show_frame(AASPage))
        AAS_Button.pack()

        ASA_Button = tk.Button(self, text = "ASA(Angle-Side-Angle)",
                               command=lambda: controller.show_frame(ASAPage))
        ASA_Button.pack()

        SSA_Button = tk.Button(self, text = "SSA(Side-Side-Angle)",
                               command=lambda: controller.show_frame(SSAPage))
        SSA_Button.pack()

        SAS_Button = tk.Button(self, text = "SAS(Side-Angle-Side)",
                               command=lambda: controller.show_frame(SAS_Page))
        SAS_Button.pack()

        SSS_Button = tk.Button(self, text = "SSS(Side-Side-Angle)",
                               command=lambda: controller.show_frame(SSSPage))
        SSS_Button.pack()

        label2 = tk.Label(self, text = "Thank you for using the Triangle Solver", font = SMALL_FONT)
        label2.pack()

"""
def angle3():
    angle1 = angle1_entry.get()
    angle2 = angle2_entry.get()
    angle3 = 180-angle2-angle2
    if angle3+angle2+angle1 == 180:
        angle3 = angle3
    else:
        angle3 = "Error"
    
class AAAPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "AAA", font = LARGE_FRONT)
        label.pack(pady=10,padx=10)
        
        angle1_label = tk.Label(self, text = "Angle 1 =")
        angle2_label = tk.Label(self, text = "Angle 2 =")

        angle1_entry = tk.Entry(self)
        angle2_entry = tk.Entry(self)

        calculate_button = tk.Button(self, text ="Calculate",
                                     command="""Should be calling angle3()""")
                                    
        angle1_label.pack()
        angle1_entry.pack()
        angle2_label.pack()
        angle2_entry.pack()
        calculate_button.pack()
"""
    
    
class AASPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "AAS", font = LARGE_FRONT)
        label.pack(pady=10,padx=10)
        
class ASAPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "ASA", font = LARGE_FRONT)
        label.pack(pady=10,padx=10)
        
class SSAPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "SSA", font = LARGE_FRONT)
        label.pack(pady=10,padx=10)

class SASPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "SAS", font = LARGE_FRONT)
        label.pack(pady=10,padx=10)

class SSSPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "SSS", font = LARGE_FRONT)
        label.pack(pady=10,padx=10)
        
create = CreatePT()
create.mainloop()
    
