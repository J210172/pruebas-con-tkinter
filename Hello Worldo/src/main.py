import tkinter as tk
import tkinter.font

class App(tk.Frame):
    """Docstring."""

    def __init__(self, window=None):
        tk.Frame.__init__(self, window)
        self.window = window
        self.init_ui()
        self.contador = 0
        
    def init_ui(self):
        self.window.title("Un titulo para la ventana")
        self.pack()
        font1 = tk.font.Font(size=69)
        self.label1 = tk.Label(self, name="label1", text="Hola Mundo!!", font=font1)
        self.label1.pack()
        self.button1 = tk.Button(self, name="btn1", text="Malvado botonoso", command=self.button_action)
        self.button1.pack()

    def button_action(self):
        self.contador += 1
        self.label1['text'] = f"Hola Mundo!!x{self.contador}"
    
def main():
    WINDOW = tk.Tk()
    WINDOW.geometry()
    APP = App(window=WINDOW)
    APP.mainloop()
    WINDOW.destroy()
     
if __name__ == "__main__":
    main()