import tkinter as tk
import wantgoo

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("簡單的GUI應用程式")
        # self.root.geometry("800x600")
        self.stock_codes:list[dict] = wantgoo.get_stocks_with_twstock()
        # print(self.stock_codes)
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="即時股票資訊", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)
        #建立一個widgets可以顯示股票資訊
        #讓使用者可以選擇股票代碼
        #股票代碼可以複選
        #使用self.stock_codes來建立選項
        #在右邊建立捲動軸
        #下面出現click鈕後, 右邊會出現選擇的股票代號及名稱  
        # self.confirm_button = tk.Button(self.root, text="確定", command=self.on_confirm)
        # self.confirm_button.pack(pady=10)
        
        self.stock_list = tk.Listbox(self.root, selectmode=tk.MULTIPLE, width=15,height=20)
        self.stock_list.insert(tk.END, "請選擇股票代碼:")   
        for stock in self.stock_codes:
            self.stock_list.insert(tk.END, f"{stock['code']} - {stock['name']} "    )

        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.stock_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.stock_list.yview)

        self.stock_list.pack(pady=10)

        confirm_button = tk.Button(self.root, text="確認", command=self.on_confirm)
        confirm_button.pack(padx=20, pady=20)

    def on_confirm(self):
        selected_indices = self.stock_list.curselection()
        selected_stocks = [self.stock_codes[i] for i in selected_indices]
        print("選擇的股票:", selected_stocks)


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()