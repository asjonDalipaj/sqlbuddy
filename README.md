# SQL Chatbot

A Streamlit-based chatbot that helps generate and explain SQL queries using natural language processing.

## Features

- Natural language to SQL query conversion
- Interactive chat interface
- Example-based learning system
- Support for complex database schema
- Real-time query generation and explanation
- PostgreSQL database integration

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd sqlchatbot
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your credentials:
```env
GROQ_API_KEY=your_groq_api_key
```

5. Run the application:
```bash
streamlit run main.py
```

## Usage

1. Start the application using `streamlit run main.py`
2. Enter your question in natural language
3. The chatbot will generate the appropriate SQL query
4. View the results and explanations in the chat interface

## Deployment

The application can be deployed for free using:
- Streamlit Community Cloud
- Railway.app (includes PostgreSQL)
- Render.com

## Tech Stack

- Python 3.11+
- Streamlit
- Groq AI
- PostgreSQL
- LangChain
- Python-dotenv

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.