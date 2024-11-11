import tkinter as tk
import time

def show_message(message):
    window = tk.Tk()
    window.title("lời nói tớ muốn dành cho cậu")
    label = tk.Label(window, text=message, font=("Arial", 14), padx=20, pady=20)
    label.pack()
    window.after(5000, lambda: window.destroy())  # Tự động đóng sau 2 giây
    window.mainloop()

def confess_love():
    messages = [
        "Xin chào cậu, đây là một bí mật",
        "tớ đã muốn nói với cậu từ lâu rồi",
        "Nhưng không biết làm sao để cậu hiểu",
        "Thôi thì để Python giúp tớ vậy",
        "Cậu có biết không, mỗi lần gặp cậu",
        "Trái tim tớ như đánh trống liên hồi!",
        "Nói ra hơi ngại, nhưng tớ thích cậu mất rồi! ❤️",
        "Liệu tớ có cơ hội được ở bên cạnh em không?"
    ]
    
    for message in messages:
        show_message(message)
        time.sleep(2)

confess_love()
