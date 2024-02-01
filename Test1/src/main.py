import tkinter as tk
import tkinter.font

class App(tk.Frame):
    """Docstring."""

    def __init__(self, window=None):
        tk.Frame.__init__(self, window)
        self.window = window
        self.init_ui()
        
    def init_ui(self):
        self.window.title("Un titulo para la ventana")
        self.pack()
        
        font_label = tk.font.Font(size=69)
        font_button = tk.font.Font(size=32)
        
        self.label1 = tk.Label(self, name="label1", text="El tres en raya", font=font_label)
        self.label1.pack()
        
        self.play_area = tk.Frame(self, bg="purple", width=300, height=350, )
        self.play_area.pack(anchor="c")
        
        self.buttons = []
        self.grid_size = 3;
        
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                num_button = self.grid_size * i + j + 1
                print(f"Button row='{i}' column='{j}' ({num_button})")
                button = tk.Button(
                    self.play_area,
                    name=f"btn{num_button}",
                    text=f"button{num_button}",
                    background="lightgrey",
                    foreground="black",
                    borderwidth=0,
                    font=font_button,
                    command=self.button_action
                )
                button.grid(row=i,column=j)
                self.buttons.append(button)
        
        
    def button_action(self):
        self.label1['text'] = "x" if self.label1['text'] == "o" else "o"
    
def main():
    WINDOW = tk.Tk()
    WINDOW.geometry()
    APP = App(window=WINDOW)
    APP.mainloop()
    WINDOW.destroy()
     
if __name__ == "__main__":
    main()