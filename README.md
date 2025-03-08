📌 Medical AI Chatbot with RAG (Retrieval-Augmented Generation)

A Medical AI Chatbot built using LangChain, ChromaDB, and LlamaCpp that leverages Retrieval-Augmented Generation (RAG) to provide accurate and contextual medical responses based on uploaded medical documents.



🚀 Features

✅ Retrieval-Augmented Generation (RAG): Combines document retrieval with LLM-based response generation.
✅ Medical Knowledge Base: Uses PubMedBERT embeddings to retrieve relevant medical information.
✅ PDF Document Processing: Automatically extracts and splits medical PDFs for better query handling.
✅ ChromaDB for Vector Storage: Efficiently stores and retrieves document embeddings.
✅ LlamaCpp Model for LLM Responses: Uses BioMistral-7B for medical text generation.
✅ Interactive Chat Interface: Allows users to query medical information in real-time.



📂 Project Structure

📦 medical-ai-chatbot
 ┣ 📂 data/                   # Folder for storing medical PDFs
 ┣ 📜 medical_ai_bot.py        # Main Python script
 ┣ 📜 requirements.txt         # List of required dependencies
 ┣ 📜 README.md                # Project documentation
 ┗ 📜 .env                     # Stores API keys (not shared in GitHub)



🛠 Installation

Step 1: Clone the Repository

git clone https://github.com/Varun0818/Medical-AI-Chatbot-with-RAG.git
cd Medical-AI-Chatbot-with-RAG

Step 2: Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows

Step 3: Install Dependencies

pip install -r requirements.txt




📌 Usage

1️⃣ Prepare Medical Documents

Place medical research papers (PDFs) in the data/ folder.


2️⃣ Run the Chatbot

python medical_ai_bot.py

3️⃣ Ask Questions

Type your medical-related query and get AI-powered responses.

Type "exit" to stop the chatbot.





⚙ Configuration

Set Up Environment Variables

1. Create a .env file in the root directory.


2. Add your Hugging Face API key securely:

HUGGINGFACEHUB_API_TOKEN=your-huggingface-api-key




🖥 Technologies Used

LangChain - For building AI pipelines

LlamaCpp - For running the BioMistral-7B model

ChromaDB - For storing and retrieving embeddings

Sentence-Transformers - For medical text embeddings

PyPDF - For extracting text from medical PDFs



📜 License

This project is licensed under the MIT License.



🤝 Contributing

We welcome contributions! If you'd like to improve the chatbot:

1. Fork the repository


2. Create a new branch (git checkout -b feature-name)


3. Commit changes (git commit -m "Added new feature")


4. Push to GitHub (git push origin feature-name)


5. Submit a Pull Request



📧 Contact

For any issues or suggestions, feel free to contact:
📌 Varun – [Github](https://github.com/Varun0818)
