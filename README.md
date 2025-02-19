# KleeSync - Project Template Manager

KleeSync is a lightweight and powerful repository that hosts multiple project templates, enabling developers to quickly bootstrap new projects with predefined structures and configurations.

## 🚀 Features
- Multiple project templates in a single repository
- Clone only the necessary template without pulling the entire repo
- Pre-configured Flask, SQLAlchemy, and more
- Simple and intuitive structure

## 📌 How to Use
1. **Install Git** if you haven't already:
   ```sh
   sudo apt install git  # For Debian/Ubuntu
   sudo pacman -S git    # For Arch Linux
   ```
2. **Clone only the template you need**:
   ```sh
   git clone --depth 1 --filter=blob:none --sparse <repo_url>
   cd KleeSync
   git sparse-checkout set flask-template  # Replace with the desired template name
   ```
3. **Follow the README inside the template folder** for further setup instructions.

## 📂 Available Templates
- **Flask-SQLAlchemy Template** (`flask-template`)
- More templates coming soon!

## ⚙️ Contributing
Want to add more templates or improve existing ones? Feel free to fork and submit a PR!

## 📜 License
This repository is licensed under the MIT License.


