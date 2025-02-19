# KleeSync - Flask Project Template

Welcome to **KleeSync**! 🎇 This template helps you quickly set up a **Flask** project with **SQLAlchemy** support, structured modules, and a SQLite database.

## 🚀 Features
- Pre-configured **Flask** app with `SQLAlchemy` support
- Organized folder structure for models, routes, and configurations
- SQLite database located at `app/database/database.sqlite`
- **Bootstrap-ready** static files (CSS & JS)
- `.env` file support for environment variables

## 📂 Project Structure
```
.
├── app
│   ├── config.py  # Configuration settings
│   ├── database
│   │   └── database.sqlite  # SQLite database file
│   ├── extensions.py  # Flask extensions (SQLAlchemy, etc.)
│   ├── __init__.py  # Initializes the Flask app
│   ├── models
│   │   └── add_database_models_here  # Place your models here
│   ├── modules
│   │   └── add_modules_here  # Place reusable modules here
│   ├── routes
│   │   ├── __init__.py  # Route initialization
│   │   └── static_routes.py  # Example route file
│   ├── static
│   │   ├── images
│   │   │   └── klee.webp  # Cute Klee image! 🍀
│   │   ├── js
│   │   │   └── script.js  # JavaScript functions
│   │   └── styles
│   │       └── main.css  # CSS styles
│   └── templates
│       └── index.html  # Welcome page
├── .env  # Environment variables
├── requirements.txt  # Python dependencies
├── README.md  # You are here! 📖
└── run.py  # Entry point for running Flask
```

## 🔥 Next Steps
✅ Add models to `app/models/`
✅ Register new routes in `app/routes/`
✅ Customize templates in `app/templates/`
✅ Modify `config.py` for production settings

---

## 🎇 Made with love ❤️ and a sprinkle of Klee's magic! 🍀
