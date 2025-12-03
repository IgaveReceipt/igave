# Igave

Igave is a modern receipt scanning and management system designed to help customers organize their expenses efficiently. The application features a robust Django backend and a dynamic Next.js frontend.

## 🚀 Tech Stack

- **Backend:** Django 5 (Python), Django REST Framework
- **Frontend:** Next.js 15 (React, TypeScript), Tailwind CSS
- **Database:** SQLite (Development) / PostgreSQL (Production ready)
- **Styling:** Tailwind CSS

## 📂 Project Structure

The project is organized into two main directories:

```
Igave/
├── backend/            # Django API and business logic
│   ├── igave/          # Project configuration (settings, urls)
│   ├── igaveapp/       # Main application (models, views, migrations)
│   └── manage.py       # Django management script
├── frontend/           # Next.js User Interface
│   └── igave_receipts/ # Next.js application source
└── requirements.txt    # Python dependencies
```

## 🛠️ Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- npm or yarn

### 1. Backend Setup

Navigate to the backend directory and set up the Python environment.

```bash
cd backend
# Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r ../requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```
The backend API will be available at `http://localhost:8000`.

### 2. Frontend Setup

Navigate to the frontend directory and install dependencies.

```bash
cd frontend/igave_receipts

# Install Node modules
npm install

# Start the development server
npm run dev
```
The frontend application will be available at `http://localhost:3000`.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
