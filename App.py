import tkinter as tk
from tkinter import ttk, messagebox, colorchooser
import webbrowser

class TkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MBAPPE IS A GOAT")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = 700
        window_height = 650
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.label_var = tk.StringVar()
        self.label_var.set("Here is your text")
        self.label = tk.Label(root, textvariable=self.label_var)
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.change_text_button = tk.Button(root, text="Поминяти текст", command=self.change_text)
        self.change_text_button.grid(row=0, column=1, padx=10, pady=10)

        self.text_entry = tk.Entry(root, width=20)
        self.text_entry.grid(row=0, column=2, padx=10, pady=10)

        self.listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        for item in ["Налаштування 1", "Налаштування 2", "Налаштування 3"]:
            self.listbox.insert(tk.END, item)
        self.listbox.grid(row=1, column=0, padx=10, pady=10)

        self.radio_var = tk.StringVar()
        self.radio_var.set("Перша")
        self.radio_button1 = tk.Radiobutton(root, text="Перша", variable=self.radio_var, value="Перша")
        self.radio_button2 = tk.Radiobutton(root, text="Друга", variable=self.radio_var, value="Друга")
        self.radio_button3 = tk.Radiobutton(root, text="Третя", variable=self.radio_var, value="Третя")
        self.radio_button1.grid(row=1, column=1, padx=10, pady=10)
        self.radio_button2.grid(row=1, column=2, padx=10, pady=10)
        self.radio_button3.grid(row=1, column=3, padx=10, pady=10)


        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=2, column=0, padx=10, pady=10)

        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Відкрити", command=self.rick_roll)
        self.file_menu.add_command(label="Сохранити", command=self.dummy_function)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Вийти (не виходіть)", command=root.destroy)
        self.menu_bar.add_cascade(label="Файл", menu=self.file_menu)   

        self.color_button = tk.Button(root, text="Вибрати колір", command=self.select_color)
        self.color_button.grid(row=2, column=1, padx=10, pady=10)

        self.progressbar = ttk.Progressbar(root, length=200, mode="indeterminate")
        self.progressbar.grid(row=3, column=0, columnspan=4, pady=10)

        self.message_button = tk.Button(root, text="Покажи messagebox", command=self.show_message)
        self.message_button.grid(row=4, column=0, columnspan=4, pady=10)

        self.scale_var = tk.DoubleVar()
        self.scale = tk.Scale(root, from_=0, to=125, variable=self.scale_var, orient=tk.HORIZONTAL, label="Спидометр")
        self.scale.grid(row=5, column=0, columnspan=4, pady=10)

        self.canvas = tk.Canvas(root, width=200, height=100, bg="white")
        self.canvas.grid(row=6, column=0, columnspan=4, pady=10)
        self.canvas.create_rectangle(50, 25, 150, 75, fill="blue")

        self.notebook = ttk.Notebook(root)
        tab1 = tk.Frame(self.notebook)
        tab2 = tk.Frame(self.notebook)
        self.notebook.add(tab1, text="Вкладка 1")
        self.notebook.add(tab2, text="Вкладка 2")
        self.notebook.grid(row=7, column=0, columnspan=4, pady=10)

    def change_text(self):
        new_text = self.text_entry.get()
        self.label_var.set(new_text)

    def dummy_function(self):
        messagebox.showinfo("Информація", "Ну вона не дуже робоча")

    def rick_roll(self):
        webbrowser.open_new_tab('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley')
        
    


    

    def select_color(self):
        color = colorchooser.askcolor(title="Вибрати колір (ТИК)")[1]
        if color:
            self.root.configure(bg=color)

    def show_message(self):
        selected_options = ', '.join(self.listbox.curselection())
        message = f"Вибрано: {selected_options}\nКнопка вибрана - : {self.radio_var.get()}"
        messagebox.showinfo("Повідомлення", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterApp(root)
    root.mainloop()
