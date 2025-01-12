# Password-Manager
🌟 Overview Welcome to the Password Manager! This secure and user-friendly desktop app is your ultimate solution for managing passwords like a pro. With top-notch encryption and seamless authentication, your passwords are in safe hands. 🛡️✨
✨ Features
👤 User Authentication: Register and log in with peace of mind. Your master password is encrypted and safe.
🔑 Password Management:
➕ Add, 🔍 Retrieve, and ❌ Delete passwords for your favorite services.
🧊 Advanced encryption ensures your data stays secure.
🔄 Change Master Password: Easily update your account's master password whenever you like.
🖥️ User-Friendly GUI: Simple and sleek interface built with Tkinter. No command-line hassle! 🎨
🧪 Robust Testing: Comprehensive unit tests keep the app reliable and bug-free. ✅
🛠️ Technology Stack
Language: 🐍 Python
Libraries:
🔒 bcrypt for hashing passwords.
🔐 cryptography for encryption.
🗄️ sqlite3 for database management.
🎨 Tkinter for the GUI.
Database: SQLite 📂
🚀 How It Works
🗄️ Database Setup: Initialize the database with a single command. It’s quick and easy!

bash
Copy code
python db_setup.py
👥 User Authentication: Register and log in to manage your passwords. All data is encrypted for ultimate safety. 🛡️

🔐 Password Encryption: Passwords are encrypted using Fernet encryption. Your encryption key (key.key) ensures only you can access your data.

📋 Password Management:

Add: Securely store encrypted passwords.
Retrieve: Easily decrypt and view passwords.
Delete: Remove stored passwords with a click.
🖥️ GUI Application: Launch the app and enjoy the seamless experience:

bash
Copy code
python main.py
🧪 Running Tests
Run unit tests to ensure everything works perfectly! 🛠️

bash
Copy code
python -m unittest discover

🔒 Security Notes
Keep your key.key file safe! It’s the magic key 🔑 to your encrypted data.
Never share your master password or encryption key. It’s yours and yours alone. 🤫
❤️ Contributing
We love contributions! 🎉 Found a bug? Got an idea? Open an issue or submit a pull request. Let’s make this even better together! 🚀

