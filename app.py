# # import streamlit as st
# # from src.components.data_ingestion import DataIngestion
# # from src.components.embedding import Embedding
# # from src.components.model_api import ModelAPI
# # from reportlab.lib.pagesizes import letter
# # from reportlab.platypus import SimpleDocTemplate, Paragraph
# # from reportlab.lib.styles import getSampleStyleSheet
# # import io
# #
# # # Initialize Streamlit
# # st.set_page_config(page_title="Medical Chatbot", initial_sidebar_state="expanded")
# # st.title("Medical Chatbot with DeepSeek V3")
# # st.markdown("Ask medical questions or check symptoms (not a doctor, just info).")
# #
# # # Custom CSS for boxy chat UI
# # st.markdown(
# #     """
# #     <style>
# #     .user-message {
# #         background-color: #ADD8E6; /* Light blue for user */
# #         padding: 10px;
# #         border-radius: 10px;
# #         margin: 5px 0;
# #         max-width: 70%;
# #         display: inline-block;
# #     }
# #     .assistant-message {
# #         background-color: #90EE90; /* Light green for chatbot */
# #         padding: 10px;
# #         border-radius: 10px;
# #         margin: 5px 0;
# #         max-width: 70%;
# #         display: inline-block;
# #     }
# #     .chat-container {
# #         border: 1px solid #ccc;
# #         padding: 10px;
# #         border-radius: 10px;
# #         margin-bottom: 20px;
# #     }
# #     </style>
# #     """,
# #     unsafe_allow_html=True
# # )
# #
# # # Initialize components (run once to populate Pinecone, then comment out)
# # # ingestion = DataIngestion(pdf_path="data/Medical_book.pdf")
# # # documents = ingestion.ingest()
# # # embedding = Embedding(index_name="medical-index")
# # # vector_store = embedding.create_vector_store(documents)
# #
# # # Load vector store
# # embedding = Embedding(index_name="medical-index")
# # vector_store = embedding.get_vector_store()
# #
# # # Initialize model
# # model_api = ModelAPI(vector_store)
# #
# # # Symptom Checker Tool
# # st.sidebar.title("Symptom Checker")
# # symptoms = st.sidebar.text_area("Enter symptoms (e.g., fever, cough)", "")
# # if st.sidebar.button("Check Symptoms"):
# #     if symptoms:
# #         with st.spinner("Analyzing symptoms..."):
# #             response = model_api.check_symptoms(symptoms)
# #             st.sidebar.markdown(f"**Analysis**: {response}")
# #     else:
# #         st.sidebar.error("Please enter symptoms.")
# #
# # # Chat History Export
# # def export_chat_history():
# #     buffer = io.BytesIO()
# #     doc = SimpleDocTemplate(buffer, pagesize=letter)
# #     styles = getSampleStyleSheet()
# #     story = []
# #     for msg in st.session_state.messages:
# #         role = "User" if msg["role"] == "user" else "Assistant"
# #         story.append(Paragraph(f"{role}: {msg['content']}", styles["Normal"]))
# #     doc.build(story)
# #     buffer.seek(0)
# #     return buffer
# #
# # if st.sidebar.button("Export Chat History as PDF"):
# #     pdf_buffer = export_chat_history()
# #     st.sidebar.download_button(
# #         label="Download Chat History",
# #         data=pdf_buffer,
# #         file_name="chat_history.pdf",
# #         mime="application/pdf"
# #     )
# #
# # # Chat container with boxy UI
# # st.markdown('<div class="chat-container">', unsafe_allow_html=True)
# # # Initialize session state
# # if "chat_history" not in st.session_state:
# #     st.session_state.chat_history = []
# # if "messages" not in st.session_state:
# #     st.session_state.messages = [{"role": "assistant", "content": "How can I help with medical info today?"}]
# #
# # # Display chat messages
# # for msg in st.session_state.messages:
# #     with st.chat_message(msg["role"]):
# #         st.markdown(f'<div class="{msg["role"]}-message">{msg["content"]}</div>', unsafe_allow_html=True)
# #
# # # Handle user input
# # if prompt := st.chat_input("Ask a medical question"):
# #     st.session_state.messages.append({"role": "user", "content": prompt})
# #     with st.chat_message("user"):
# #         st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)
# #
# #     # Get response
# #     answer = model_api.get_response(prompt, st.session_state.chat_history)
# #     st.session_state.chat_history.append((prompt, answer))
# #     st.session_state.messages.append({"role": "assistant", "content": answer})
# #
# #     with st.chat_message("assistant"):
# #         st.markdown(f'<div class="assistant-message">{answer}</div>', unsafe_allow_html=True)
# #
# # st.markdown('</div>', unsafe_allow_html=True)
# #
#
# import streamlit as st
# from src.components.data_ingestion import DataIngestion
# from src.components.embedding import Embedding
# from src.components.model_api import ModelAPI
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet
# import io
#
# # Initialize Streamlit
# st.set_page_config(page_title="Medical Chatbot", initial_sidebar_state="expanded")
#
# # Custom CSS for enhanced UI
# st.markdown(
#     """
#     <style>
#     /* Full pastel background for the entire app */
#     .stApp {
#         background-color: #f3e5f5; /* Pastel lavender */
#         color: #333333;
#     }
#     /* Header styling */
#     h1 {
#         color: #ab47bc; /* Pastel purple */
#         text-align: center;
#         font-family: 'Arial', sans-serif;
#         text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
#     }
#     /* Markdown text below title */
#     .stMarkdown p {
#         color: #6d4c41; /* Pastel brown */
#         font-family: 'Arial', sans-serif;
#         text-align: center;
#     }
#     /* Sidebar styling for Symptom Checker */
#     .stSidebar {
#         background-color: #ffe0b2; /* Pastel peach for Symptom Checker */
#         border-right: 2px solid #ffcc80;
#         padding: 10px;
#     }
#     .stSidebar h1 {
#         color: #ef6c00; /* Bright peach for title */
#         font-size: 1.5em;
#         text-align: center;
#     }
#     /* Chat container styling */
#     .chat-container {
#         border: 2px solid #ce93d8; /* Pastel purple border */
#         padding: 15px;
#         border-radius: 15px;
#         background-color: #ffffff; /* White for contrast */
#         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#         margin: 0 !important; /* Remove extra margin */
#     }
#     /* Chat message styling */
#     .user-message {
#         background-color: #b3e5fc; /* Pastel blue for user */
#         padding: 12px;
#         border-radius: 15px;
#         margin: 5px 0;
#         max-width: 70%;
#         display: inline-block;
#         border: 1px solid #81d4fa;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
#         color: #0288d1;
#     }
#     .assistant-message {
#         background-color: #c8e6c9; /* Pastel green for chatbot */
#         padding: 12px;
#         border-radius: 15px;
#         margin: 5px 0;
#         max-width: 70%;
#         display: inline-block;
#         border: 1px solid #a5d6a7;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
#         color: #2e7d32;
#     }
#     /* Chat input styling to match background */
#     .stChatInput {
#         background-color: #f3e5f5; /* Match app background */
#         border: none;
#         padding: 10px;
#     }
#     .stChatInput input {
#         border: 2px solid #ce93d8;
#         border-radius: 8px;
#         font-family: 'Arial', sans-serif;
#         background-color: #ffffff;
#     }
#     /* Button styling */
#     .stButton>button {
#         background-color: #ce93d8; /* Pastel purple */
#         color: white;
#         border-radius: 8px;
#         border: none;
#         padding: 8px 16px;
#         font-family: 'Arial', sans-serif;
#         transition: background-color 0.3s;
#     }
#     .stButton>button:hover {
#         background-color: #ba68c8;
#     }
#     /* Text area styling */
#     .stTextArea textarea {
#         border: 2px solid #ffcc80; /* Pastel peach border */
#         border-radius: 8px;
#         font-family: 'Arial', sans-serif;
#         background-color: #ffffff;
#     }
#     /* Remove extra spacing to eliminate empty bar */
#     .stMarkdown, .stSpinner, .stError, .stChatContainer {
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
#
# # Header
# st.title("Medical Chatbot")
# st.markdown("Ask medical questions or check symptoms (not a doctor, just info).")
#
# # Load vector store
# embedding = Embedding(index_name="medical-index")
# vector_store = embedding.get_vector_store()
#
# # Initialize model
# model_api = ModelAPI(vector_store)
#
# # Symptom Checker Tool
# st.sidebar.title("Symptom Checker")
# symptoms = st.sidebar.text_area("Enter symptoms (e.g., fever, cough)", "")
# if st.sidebar.button("Check Symptoms"):
#     if symptoms:
#         with st.spinner("Analyzing symptoms..."):
#             response = model_api.check_symptoms(symptoms)
#             st.sidebar.markdown(f"**Analysis**: {response}")
#     else:
#         st.sidebar.error("Please enter symptoms.")
#
# # Chat History Export
# def export_chat_history():
#     buffer = io.BytesIO()
#     doc = SimpleDocTemplate(buffer, pagesize=letter)
#     styles = getSampleStyleSheet()
#     story = []
#     for msg in st.session_state.messages:
#         role = "User" if msg["role"] == "user" else "Assistant"
#         story.append(Paragraph(f"{role}: {msg['content']}", styles["Normal"]))
#     doc.build(story)
#     buffer.seek(0)
#     return buffer
#
# if st.sidebar.button("Export Chat History as PDF"):
#     pdf_buffer = export_chat_history()
#     st.sidebar.download_button(
#         label="Download Chat History",
#         data=pdf_buffer,
#         file_name="chat_history.pdf",
#         mime="application/pdf"
#     )
#
# # Chat container with boxy UI
# st.markdown('<div class="chat-container">', unsafe_allow_html=True)
# # Initialize session state
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
# if "messages" not in st.session_state:
#     st.session_state.messages = [{"role": "assistant", "content": "How can I help with medical info today?"}]
#
# # Display chat messages
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(f'<div class="{msg["role"]}-message">{msg["content"]}</div>', unsafe_allow_html=True)
#
# # Handle user input
# if prompt := st.chat_input("Ask a medical question"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)
#
#     # Get response
#     answer = model_api.get_response(prompt, st.session_state.chat_history)
#     st.session_state.chat_history.append((prompt, answer))
#     st.session_state.messages.append({"role": "assistant", "content": answer})
#
#     with st.chat_message("assistant"):
#         st.markdown(f'<div class="assistant-message">{answer}</div>', unsafe_allow_html=True)
#
# st.markdown('</div>', unsafe_allow_html=True)
import streamlit as st
from src.components.data_ingestion import DataIngestion
from src.components.embedding import Embedding
from src.components.model_api import ModelAPI
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import io

# Initialize Streamlit
st.set_page_config(page_title="Medical Chatbot", initial_sidebar_state="expanded")

# Custom CSS for enhanced UI
st.markdown(
    """
    <style>
    /* Gradient background with pink, white, and cream */
    .stApp {
        background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%); /* Pink, white, cream */
        color: #333333;
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
    }
    .main-content {
        padding: 0 !important;
        margin: 0 !important;
        width: 100%;
    }
    /* Header styling */
    h1 {
        color: #f06292; /* Muted pink */
        text-align: center;
        font-family: 'Arial', sans-serif;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        margin-bottom: 5px !important;
    }
    /* Markdown text below title */
    .stMarkdown p {
        color: #5d4037; /* Muted brown */
        font-family: 'Arial', sans-serif;
        text-align: center;
        margin: 0 !important;
        padding: 5px 0 !important;
    }
    /* Sidebar styling for Symptom Checker with gradient */
    .stSidebar {
        background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%); /* Same gradient as app */
        border-right: 2px solid #f48fb1; /* Soft pink border */
        padding: 10px;
    }
    .stSidebar h1 {
        color: #f06292; /* Muted pink */
        font-size: 1.5em;
        text-align: center;
    }
    /* Chat container styling */
    .chat-container {
        border: 2px solid #f48fb1; /* Soft pink border */
        padding: 15px;
        border-radius: 15px;
        background-color: #ffffff; /* White for contrast */
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin: 0 !important;
        padding: 0 0 10px 0 !important;
    }
    /* Chat message styling */
    .user-message {
        background-color: #f06292; /* Pink for user */
        padding: 12px;
        border-radius: 15px;
        margin: 5px 0;
        max-width: 70%;
        display: inline-block;
        border: 1px solid #ec407a;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        color: #ffffff; /* White text for contrast */
    }
    .assistant-message {
        background-color: #ffffff; /* White for chatbot */
        padding: 12px;
        border-radius: 15px;
        margin: 5px 0;
        max-width: 70%;
        display: inline-block;
        border: 1px solid #eeeeee;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        color: #5d4037; /* Muted brown text */
    }
    /* Chat input styling to match background */
    .stChatInput {
        background: transparent; /* Transparent to blend with gradient */
        border: none;
        padding: 0 !important;
        margin: 0 !important;
    }
    .stChatInput input {
        border: 2px solid #f48fb1;
        border-radius: 8px;
        font-family: 'Arial', sans-serif;
        background-color: #ffffff;
        padding: 5px;
    }
    /* Button styling */
    .stButton>button {
        background-color: #f48fb1; /* Soft pink */
        color: white;
        border-radius: 8px;
        border: none;
        padding: 8px 16px;
        font-family: 'Arial', sans-serif;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #f06292;
    }
    /* Text area styling */
    .stTextArea textarea {
        border: 2px solid #f48fb1; /* Soft pink border */
        border-radius: 8px;
        font-family: 'Arial', sans-serif;
        background-color: #ffffff;
    }
    /* Remove extra spacing to eliminate empty bar */
    .stApp, .stChatContainer, .stChatInputContainer, .stChatMessage, .stChatInput, .stMarkdown, .stSpinner, .stError {
        margin: 0 !important;
        padding: 0 !important;
    }
    div[data-testid="stVerticalBlock"], div[data-testid="stHorizontalBlock"] {
        margin: 0 !important;
        padding: 0 !important;
    }
    div[data-testid="stAppViewContainer"] {
        padding: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Wrap content in custom container
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Header
st.title("Medical Chatbot")
st.markdown("Ask medical questions or check symptoms (not a doctor, just info).")

# Load vector store
embedding = Embedding(index_name="medical-index")
vector_store = embedding.get_vector_store()

# Initialize model
model_api = ModelAPI(vector_store)

# Symptom Checker Tool
st.sidebar.title("Symptom Checker")
symptoms = st.sidebar.text_area("Enter symptoms (e.g., fever, cough)", "")
if st.sidebar.button("Check Symptoms"):
    if symptoms:
        with st.spinner("Analyzing symptoms..."):
            response = model_api.check_symptoms(symptoms)
            st.sidebar.markdown(f"**Analysis**: {response}")
    else:
        st.sidebar.error("Please enter symptoms.")

# Chat History Export
def export_chat_history():
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    for msg in st.session_state.messages:
        role = "User" if msg["role"] == "user" else "Assistant"
        story.append(Paragraph(f"{role}: {msg['content']}", styles["Normal"]))
    doc.build(story)
    buffer.seek(0)
    return buffer

if st.sidebar.button("Export Chat History as PDF"):
    pdf_buffer = export_chat_history()
    st.sidebar.download_button(
        label="Download Chat History",
        data=pdf_buffer,
        file_name="chat_history.pdf",
        mime="application/pdf"
    )

# Chat container with boxy UI
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How can I help with medical info today?"}]

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(f'<div class="{msg["role"]}-message">{msg["content"]}</div>', unsafe_allow_html=True)

# Handle user input
if prompt := st.chat_input("Ask a medical question"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)

    # Get response
    answer = model_api.get_response(prompt, st.session_state.chat_history)
    st.session_state.chat_history.append((prompt, answer))
    st.session_state.messages.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.markdown(f'<div class="assistant-message">{answer}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)