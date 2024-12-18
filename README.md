# Pxolly IRIS Callback

A FastAPI-based callback server for handling Pxolly interactions with VK integration.

## 🚀 Features

- FastAPI-powered callback server
- VK Bot integration
- Command handling system
- Asynchronous request processing
- Logging with Loguru

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pxolly-iris-callback.git
cd pxolly-iris-callback
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with the following variables:
```env
VK_TOKEN=your_vk_token_here
PXOLLY_API_TOKEN=your_pxolly_api_token
PXOLLY_SECRET_KEY=your_pxolly_secret_key
```

## ⚙️ Environment Variables

- `VK_TOKEN`: Your VK bot token for authentication
- `PXOLLY_API_TOKEN`: API token for Pxolly IRIS
- `PXOLLY_SECRET_KEY`: Secret key for Pxolly IRIS authentication

## 🚀 Running the Application

1. Make sure your virtual environment is activated
2. Run the application:
```bash
python -m app.main
```

The server will start on `http://127.0.0.1:8000`

## 🏗️ Project Structure

```
pxolly-iris-callback/
├── app/
│   ├── api/            # API endpoints
│   ├── core/           # Core functionality
│   ├── dependencies/   # Dependency injection
│   ├── handlers/       # Command handlers
│   ├── schemas/        # Pydantic models
│   └── main.py        # Application entry point
├── requirements.txt    # Project dependencies
└── .env               # Environment variables (not in git)
```

## 📦 Dependencies

Key dependencies include:
- FastAPI: Web framework for building APIs
- VKbottle: VK bot framework
- Pydantic: Data validation
- Uvicorn: ASGI server
- Loguru: Logging

For a complete list of dependencies, see `requirements.txt`.

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your API tokens and secret keys secure
- Regularly rotate your security credentials

## 📝 License
- See [LICENSE](LICENSE) for the project license
