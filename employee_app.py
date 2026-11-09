
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
import os

# --- CONFIGURATION ---
DB_NAME = "company_employees.db"

# --- DATABASE SETUP ---
def setup_database():
    """Creates the database and inserts the SQL data if it doesn't already exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            department TEXT NOT NULL,
            role TEXT NOT NULL,
            salary REAL NOT NULL,
            hire_date TEXT NOT NULL
        )
    """)

    # Check if data already exists to prevent duplicates
    cursor.execute("SELECT COUNT(*) FROM employees")
    if cursor.fetchone()[0] == 0:
        # Insert the SQL Data
        sample_data = [
            ('John', 'Doe', 'Engineering', 'Software Engineer', 85000.00, '2021-03-15'),
            ('Jane', 'Smith', 'Human Resources', 'HR Manager', 75000.00, '2019-07-22'),
            ('Alice', 'Johnson', 'Engineering', 'Data Scientist', 95000.00, '2022-01-10'),
            ('Bob', 'Williams', 'Marketing', 'Marketing Specialist', 65000.00, '2020-11-05'),
            ('Charlie', 'Brown', 'Finance', 'Financial Analyst', 80000.00, '2018-05-30'),
            ('Diana', 'Prince', 'Engineering', 'Project Manager', 92000.00, '2020-08-14'),
            ('Evan', 'Wright', 'Sales', 'Account Executive', 70000.00, '2023-02-01')
        ]
        cursor.executemany("""
            INSERT INTO employees (first_name, last_name, department, role, salary, hire_date) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, sample_data)
        conn.commit()
        print("Database created and populated with sample data.")
    else:
        print("Database already exists. Loading existing data.")
    
    conn.close()

# --- DATA FETCHING ---
def get_employee_data():
    """Connects to SQL and fetches all employee records."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, first_name, last_name, department, role, salary, hire_date FROM employees")
    records = cursor.fetchall()
    conn.close()
    return records

# --- GUI APPLICATION ---
def create_app():
    """Builds the Tkinter Desktop App and the Data Table."""
    # Initialize Main Window
    root = tk.Tk()
    root.title("Employee Management Dashboard")
    root.geometry("950x500")
    root.configure(bg="#f0f0f0")

    # Title Label
    title_label = tk.Label(root, text="Company Employee Directory", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
    title_label.pack(pady=15)

    # Frame for the Table and Scrollbars
    table_frame = tk.Frame(root)
    table_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

    # Define Columns for the Treeview (Table)
    columns = ("ID", "First Name", "Last Name", "Department", "Role", "Salary", "Hire Date")
    
    # Create the Treeview (Table) widget
    tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
    
    # Configure Column Headings and Widths
    tree.heading("ID", text="ID")
    tree.heading("First Name", text="First Name")
    tree.heading("Last Name", text="Last Name")
    tree.heading("Department", text="Department")
    tree.heading("Role", text="Role")
    tree.heading("Salary", text="Salary ($)")
    tree.heading("Hire Date", text="Hire Date")

    tree.column("ID", width=40, anchor=tk.CENTER)
    tree.column("First Name", width=100, anchor=tk.W)
    tree.column("Last Name", width=100, anchor=tk.W)
    tree.column("Department", width=130, anchor=tk.W)
    tree.column("Role", width=160, anchor=tk.W)
    tree.column("Salary", width=100, anchor=tk.E)
    tree.column("Hire Date", width=100, anchor=tk.CENTER)

    # Add Scrollbars
    vsb = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(table_frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # Grid layout for table and scrollbars
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    
    table_frame.grid_columnconfigure(0, weight=1)
    table_frame.grid_rowconfigure(0, weight=1)

    # Function to load data into the table
    def load_data():
        # Clear existing data in the table
        for item in tree.get_children():
            tree.delete(item)
        
        # Fetch from SQL and insert into table
        records = get_employee_data()
        for row in records:
            # Format salary to include commas and 2 decimal places
            formatted_salary = f"${row[5]:,.2f}"
            # Insert row into Treeview (we use row[0] as the unique ID for the tree item)
            tree.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4], formatted_salary, row[6]))

    # Refresh Button
    btn_frame = tk.Frame(root, bg="#f0f0f0")
    btn_frame.pack(pady=10)
    
    refresh_btn = tk.Button(btn_frame, text="Refresh Data from SQL", command=load_data, 
                            font=("Helvetica", 12), bg="#007acc", fg="white", relief=tk.FLAT, padx=10, pady=5)
    refresh_btn.pack()

    # Load data on startup
    load_data()

    # Start the GUI event loop
    root.mainloop()

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # 1. Setup the SQL Database
    setup_database()
    # 2. Launch the Python App
    create_app()
    