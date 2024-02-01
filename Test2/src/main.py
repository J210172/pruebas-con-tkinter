import tkinter as tk
import tkinter.font

class GameGrid(tk.Frame):
    pass


class Cell(tk.Button):
    """ Button class for the cells of the game grid """
    
    def __init__(self, game_grid: GameGrid, column, rown):
        super(self).__init__(
            game_grid,
            bg="purple",
            width=300,
            height=350, 
        )
        

class App(tk.Frame):
    """Docstring."""

    def __init__(self, window=None):
        super(App, self).__init__(window)
        self.window = window
        
        self.grid_size = 3;
        
        self.init_ui()
        
    def init_ui(self):
        self.window.title("Un titulo para la ventana")
        self.pack()
        
        font1 = tk.font.Font(size=69)
        self.label1 = tk.Label(self, name="label1", text="El tres en raya", font=font1)
        self.label1.pack()
        
        self.play_area = tk.Frame(self, bg="purple", width=300, height=350)
        self.play_area.pack(anchor="c")
        
        self.buttons = []
        
        count = 0 
        
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                num_button = self.grid_size * i + j + 1
                print(f"Button row='{i}' column='{j}' ({num_button})")
                button = ()
                button.grid(row=i,column=j)
                self.buttons.append(button)
        
        
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