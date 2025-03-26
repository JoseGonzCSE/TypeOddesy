#⌨️TypeOddesy⌨️


Welcome to the **Quote Typing Speed Test**, a fun and interactive way to test your typing speed and accuracy! This project allows you to type famous quotes, calculate your typing performance, and learn more about the quote's origin.

## 🛠️ Features
- **Random Quotes**: Each test presents a random quote from a CSV file.
- **Typing Performance**: Get instant feedback on your typing speed and accuracy, measured in WPM (Words Per Minute).
- **Quote Info**: After the test, get a brief summary of the quote and its author using Google Gemini AI.
- **Streamlit UI**: The app uses Streamlit for an easy-to-use interface with real-time progress updates.

## 🤖 Technologies Used
- **Python**: Main programming language.
- **Streamlit**: Used for building the interactive web app.
- **Google Gemini**: Provides AI-generated summaries of quotes and authors.
- **CSV**: Source of quotes and authors for the typing test.
- **dotenv**: Manages environment variables for API keys.

## 🚀 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/quote-typing-speed-test.git

2. Navigate to the project directory:
   ```bash
    cd quote-typing-speed-test 

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt

4. Set up your environment variables:
    
    Create a .env file and add your Google Gemini API key:
   ```bash
    API_KEY=your_gemini_api_key

5. Run the app using Streamlit:
   ```bash
    streamlit run app.py
## 📚 Project Structure
  ```bash
   ├── app.py               # Main application file containing the Streamlit UI and game logic.
   ├── data.csv             # A CSV file containing quotes and authors.
   ├── .env                 # Environment variables file (not included in the repo, must be created).
   ├── requirements.txt     # A list of required packages for the project.

