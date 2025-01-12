import tkinter as tk
from tkinter import messagebox, simpledialog
from auth import register, login, change_password
from password_manager import add_password, get_password, delete_password
from encryption import load_key

key = load_key()

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.user_id = None

        self.create_login_frame()

    def create_login_frame(self):
        self.clear_frame()

        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(pady=20)

        tk.Label(self.login_frame, text="Username").grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.login_frame, text="Password").grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.login_frame, text="Register", command=self.register_user).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(self.login_frame, text="Login", command=self.login_user).grid(row=2, column=1, padx=10, pady=10)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def register_user(self):
        username = self.username_entry.get().strip().lower()
        password = self.password_entry.get().strip()
        if register(username, password):
            messagebox.showinfo("Success", "Registration successful")
        else:
            messagebox.showerror("Error", "Registration failed")

    def login_user(self):
        username = self.username_entry.get().strip().lower()
        password = self.password_entry.get().strip()
        self.user_id = login(username, password)
        if self.user_id:
            messagebox.showinfo("Success", "Login successful")
            self.create_main_frame()
        else:
            messagebox.showerror("Error", "Login failed")

    def create_main_frame(self):
        self.clear_frame()

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=20)

        tk.Button(self.main_frame, text="Add Password", command=self.add_password).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(self.main_frame, text="Get Password", command=self.get_password).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.main_frame, text="Delete Password", command=self.delete_password).grid(row=0, column=2, padx=10, pady=10)
        tk.Button(self.main_frame, text="Change Password", command=self.change_password).grid(row=0, column=3, padx=10, pady=10)
        tk.Button(self.main_frame, text="Logout", command=self.logout).grid(row=0, column=4, padx=10, pady=10)

    def add_password(self):
        service = simpledialog.askstring("Service Name", "Enter service name:")
        if service is not None:
            service = service.strip().lower()
            password = simpledialog.askstring("Password", "Enter password:", show="*")
            if password is not None:
                password = password.strip()
                if service and password:
                    add_password(self.user_id, service, password, key)
                    messagebox.showinfo("Success", "Password added")
                else:
                    messagebox.showerror("Error", "Service name and password cannot be empty")
            else:
                messagebox.showerror("Error", "Password cannot be empty")
        else:
            messagebox.showerror("Error", "Service name cannot be empty")

    def get_password(self):
        service = simpledialog.askstring("Service Name", "Enter service name:")
        if service is not None:
            service = service.strip().lower()
            if service:
                password = get_password(self.user_id, service, key)
                if password:
                    messagebox.showinfo("Password", f"Password for {service}: {password}")
                else:
                    messagebox.showerror("Error", "Service not found")
            else:
                messagebox.showerror("Error", "Service name cannot be empty")

    def delete_password(self):
        service = simpledialog.askstring("Service Name", "Enter service name:")
        if service is not None:
            service = service.strip().lower()
            if service:
                delete_password(self.user_id, service)
                messagebox.showinfo("Success", "Password deleted")
            else:
                messagebox.showerror("Error", "Service name cannot be empty")
        else:
            messagebox.showerror("Error", "Service name cannot be empty")

    def change_password(self):
        new_password = simpledialog.askstring("New Password", "Enter new password:", show="*")
        if new_password is not None:
            new_password = new_password.strip()
            if change_password(self.user_id, new_password):
                messagebox.showinfo("Success", "Password changed successfully")
            else:
                messagebox.showerror("Error", "Failed to change password")
        else:
            messagebox.showerror("Error", "New password cannot be empty")

    def logout(self):
        self.user_id = None
        self.create_login_frame()

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()