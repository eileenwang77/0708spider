# 建立一個tkinter的基本樣板
# 用物件導向的方式來設計，建立一個簡單的GUI應用程式
import tkinter as tk        
from tkinter import messagebox
class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Application我的APP")
        self.root.geometry("600x700")

        self.label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 20,"bold") ,fg="red",bg="yellow"  )
        self.label.pack(pady=40)

        self.button = tk.Button(root, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        self.label.config(fg="blue")
        messagebox.showinfo("Info", "Button was clicked!")
        self.label.config(fg="red")
        # self.label.config(text="Button clicked!")


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop() 
    
