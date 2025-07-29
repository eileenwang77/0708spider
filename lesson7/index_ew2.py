import tkinter as tk

root = tk.Tk()
root.title("我的Tkinter窗口")
root.geometry("400x300+200+200")
root.resizable(False, False)  # 不允许调整大小

# 这里可以添加控件，比如一个标签
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

root.mainloop()
