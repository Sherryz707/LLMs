# LangChain API with Streamlit Client

This project sets up a **FastAPI server** using LangChain and a **Streamlit-based client** to interact with it. You need to run two separate command prompts: one for the API server and another for the client.

---

## **Installation**
### **1. Clone the Repository**
```sh
git clone <repository-url>
cd <project-folder>
```

### **2. Create and Activate a Virtual Environment**
```sh
# Windows
python -m venv llmenv
llmenv\Scripts\activate

# macOS/Linux
python -m venv llmenv
source llmenv/bin/activate
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## **Running the Project**
### **Step 1: Start the FastAPI Server**
In the first terminal, run:
```sh
python app.py
```
This will start the API server on **http://localhost:8000**.

### **Step 2: Start the Streamlit Client**
In the second terminal, run:
```sh
streamlit run client.py
```
This will start the Streamlit web app in your browser.

---

## **Project Structure**
```
📂 project-folder
│-- app.py         # FastAPI server with LangChain
│-- client.py      # Streamlit frontend to interact with API
│-- requirements.txt # List of dependencies
│-- README.md      # Project documentation
```

---

## **Endpoints**
| Endpoint  | Description |
|-----------|------------|
| `/ollama` | Direct access to the Ollama LLM |
| `/essay`  | Generates an essay based on a given topic |
| `/poem`   | Generates a poem based on a given topic |

---

## **Troubleshooting**
1. **If `app.py` is not running:**  
   - Ensure **port 8000** is free.
   - Check Python version (`python --version`).

2. **If `client.py` is not working:**  
   - Make sure **app.py is running first**.
   - Restart the Streamlit server after making changes (`Ctrl+C` then rerun `streamlit run client.py`).

---

## **Contributing**
Feel free to submit issues or pull requests to improve this project.

---

## **License**
This project is licensed under the MIT License.

