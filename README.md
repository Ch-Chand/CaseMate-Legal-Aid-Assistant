# CaseMate: Legal Aid Assistant  

**CaseMate** is an AI-powered legal chatbot designed to assist users with constitutional law queries. It utilizes **ChromaDB** for efficient document retrieval and **Gemini 1.5 Flash** for generating responses. The project includes data extraction, storage, and a Streamlit-based chatbot interface.

## 🚀 Features  

- **Conversational AI Chatbot**: Interactive chat interface built with Streamlit.  
- **Multiple Conversations**: Users can create and manage different chat sessions.  
- **Legal Document Retrieval**: Uses **ChromaDB** to retrieve relevant legal content.  
- **Gemini AI Integration**: Generates accurate, context-aware responses.  
- **Preprocessing & Embeddings**: Converts legal PDFs into structured embeddings for fast querying.  
- **GitHub Actions Workflow**: Automated CI/CD setup using GitHub Actions.  

---

## 🛠️ Tech Stack  

- **Frontend**: Streamlit  
- **Database**: ChromaDB  
- **LLM**: Gemini 1.5 Flash  
- **CI/CD**: GitHub Actions  
- **Data Processing**: Python, Pandas, SentenceTransformers  

---

## 📁 Repository Structure  

```
CaseMate-Legal-Aid-Assistant/
│── Data/PakistanConstituion/          # Source dataset
│   ├── 1333523681_951.pdf              # PDF file of the Pakistan Constitution
│   ├── chunked_data.csv                # CSV file of processed chunks
│   ├── pdf_data.json                   # Extracted text data in JSON format
│
│── Scripts/                            # Core application scripts
│   ├── app.py                          # Streamlit chatbot application
│   ├── prepare_data.py                 # Preprocessing script for legal documents
│   ├── store_embeddings.py             # Script to store document embeddings in ChromaDB
│
│── chroma_db/                          # ChromaDB persistent storage
```

---

## 🛠️ Installation  

### Prerequisites  
Ensure you have the following installed:  
- Python 3.8+  
- pip  
- Virtual environment (recommended)  

### Steps  

1. **Clone the repository**  

   ```bash
   git clone https://github.com/Ch-Chand/CaseMate-Legal-Aid-Assistant.git
   cd CaseMate-Legal-Aid-Assistant
   ```

2. **Create a virtual environment and activate it**  

   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\\Scripts\\activate  # On Windows
   ```

3. **Install dependencies**  

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**  
   Create a `.env` file and add your **Gemini API Key**:  

   ```
   GEMINI_API_KEY=your_google_gemini_api_key
   ```

5. **Run the application**  

   ```bash
   streamlit run Scripts/app.py
   ```

## 🎯 Usage  

- Open the app in your browser.  
- Start a chat by entering a legal query.  
- Use the **"New Chat"** button to create a new conversation.  
- The AI will fetch relevant legal content and generate responses.  

## 🤝 Contributing  

We welcome contributions! To contribute:  

1. Fork the repository  
2. Create a feature branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m "Added new feature"`)  
4. Push to the branch (`git push origin feature-name`)  
5. Create a Pull Request  

---

## 📜 License  

This project is licensed under the MIT License.  

---

## 📞 Contact  

For any issues or suggestions, open an [issue](https://github.com/Ch-Chand/CaseMate-Legal-Aid-Assistant/issues) or reach out:  

📧 **Your Email Here**  
🔗 [GitHub Repo](https://github.com/Ch-Chand/CaseMate-Legal-Aid-Assistant)  
```
