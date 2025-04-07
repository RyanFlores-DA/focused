import tkinter as tk
import tkinter.font as tkfont
import time

class Viewer:
    
    def __init__(self):
        self.tk_state = False
        self.root = tk.Tk()
        
    def which_state(self) -> bool:
        return self.tk_state
        
    def switch_state(self, state) -> None:
        self.tk_state = not self.tk_state
        
    def destroy_viewer(self) -> None:
        if hasattr(self, 'root') and self.root:
            self.root.destroy()
            self.root = None
            self.switch_state(False)
            
    def up_viewer(self) -> None:
        if not hasattr(self, 'root') or not self.root:
            self.root = tk.Tk()
        
    def show_focused_mensage(self) -> None:
        
        self.up_viewer()
        self.switch_state(True)
        
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-transparentcolor", "black")
        self.root.configure(bg='black')
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 455
        window_height = 150
        pos_x = (screen_width // 2) - (window_width // 2)
        pos_y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{pos_x}+{pos_y}")
        
        custom_font = tkfont.Font(family="Arial", size=40, weight="bold")
        label = tk.Label(
            self.root,
            text="FORA DE FOCO!",
            font=custom_font,
            fg="red",
            bg="black",
        )
        label.place(relx=0.5, rely=0.5, anchor="center")
        
        self.root.update()
        