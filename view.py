import tkinter as tk
from tkinter import ttk, messagebox
from controller import connect, insertDB, selectSV

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database App")

        # Create database connection widgets
        self.create_db_widgets()

    def create_db_widgets(self):
        # Database connection fields
        self.db_name = tk.StringVar(value='dbtest')
        self.user = tk.StringVar(value='postgres')
        self.password = tk.StringVar(value='1704')
        self.host = tk.StringVar(value='localhost')
        self.port = tk.StringVar(value='5432')

        # Create database connection widgets
        db_frame = tk.Frame(self.root)
        db_frame.grid(row=0, columnspan=2, pady=10)

        ttk.Label(db_frame, text="DB Name:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(db_frame, textvariable=self.db_name).grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(db_frame, text="User:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(db_frame, textvariable=self.user).grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(db_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5)
        ttk.Entry(db_frame, textvariable=self.password, show="*").grid(row=2, column=1, padx=5, pady=5)
        ttk.Label(db_frame, text="Host:").grid(row=3, column=0, padx=5, pady=5)
        ttk.Entry(db_frame, textvariable=self.host).grid(row=3, column=1, padx=5, pady=5)
        ttk.Label(db_frame, text="Port:").grid(row=4, column=0, padx=5, pady=5)
        ttk.Entry(db_frame, textvariable=self.port).grid(row=4, column=1, padx=5, pady=5)

        # Connect button
        connect_button = ttk.Button(db_frame, text="Connect", command=self.connect_db)
        connect_button.grid(row=5, columnspan=2, pady=10)

        # Insert data section
        self.column1 = tk.StringVar()
        self.column2 = tk.StringVar()

        ttk.Label(db_frame, text="Ho ten:").grid(row=6, column=0, padx=5, pady=5)
        ttk.Entry(db_frame, textvariable=self.column1).grid(row=6, column=1, padx=5, pady=5)

        ttk.Label(db_frame, text="Dia chi:").grid(row=7, column=0, padx=5, pady=5)
        ttk.Entry(db_frame, textvariable=self.column2).grid(row=7, column=1, padx=5, pady=5)

        ttk.Button(db_frame, text="Insert Data", command=self.insert_data).grid(row=8, columnspan=2, pady=10)

        # Data display section
        self.data_display = tk.Text(self.root, height=10, width=50)
        self.data_display.grid(row=9, columnspan=2, pady=10)

    def connect_db(self):
        try:
            self.conn = connect()
            self.cur = self.conn.cursor()
            messagebox.showinfo("Success", "Connected to the database successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error connecting to the database: {e}")

    def insert_data(self):
        try:
            insertDB(self.conn, self.column1.get(), self.column2.get())
            messagebox.showinfo("Success", "Data inserted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error inserting data: {e}")

    def load_data(self):
        try:
            selectSV(self.cur)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading data: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()
