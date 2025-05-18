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
# import streamlit as st
# from src.components.data_ingestion import DataIngestion
# from src.components.embedding import Embedding
# from src.components.model_api import ModelAPI
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet
# import io

# # Initialize Streamlit
# st.set_page_config(page_title="Medical Chatbot", initial_sidebar_state="expanded")

# # Custom CSS for enhanced UI
# st.markdown(
#     """
#     <style>
#     /* Gradient background with pink, white, and cream */
#     .stApp {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%); /* Pink, white, cream */
#         color: #333333;
#         margin: 0 !important;
#         padding: 0 !important;
#         overflow: hidden !important;
#     }
#     .main-content {
#         padding: 0 !important;
#         margin: 0 !important;
#         width: 100%;
#     }
#     /* Header styling */
#     h1 {
#         color: #f06292; /* Muted pink */
#         text-align: center;
#         font-family: 'Arial', sans-serif;
#         text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
#         margin-bottom: 5px !important;
#     }
#     /* Markdown text below title */
#     .stMarkdown p {
#         color: #5d4037; /* Muted brown */
#         font-family: 'Arial', sans-serif;
#         text-align: center;
#         margin: 0 !important;
#         padding: 5px 0 !important;
#     }
#     /* Sidebar styling for Symptom Checker with gradient */
#     .stSidebar {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%); /* Same gradient as app */
#         border-right: 2px solid #f48fb1; /* Soft pink border */
#         padding: 10px;
#     }
#     .stSidebar h1 {
#         color: #f06292; /* Muted pink */
#         font-size: 1.5em;
#         text-align: center;
#     }
#     /* Chat container styling */
#     .chat-container {
#         border: 2px solid #f48fb1; /* Soft pink border */
#         padding: 15px;
#         border-radius: 15px;
#         background-color: #ffffff; /* White for contrast */
#         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#         margin: 0 !important;
#         padding: 0 0 10px 0 !important;
#     }
#     /* Chat message styling */
#     .user-message {
#         background-color: #f06292; /* Pink for user */
#         padding: 12px;
#         border-radius: 15px;
#         margin: 5px 0;
#         max-width: 70%;
#         display: inline-block;
#         border: 1px solid #ec407a;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
#         color: #ffffff; /* White text for contrast */
#     }
#     .assistant-message {
#         background-color: #ffffff; /* White for chatbot */
#         padding: 12px;
#         border-radius: 15px;
#         margin: 5px 0;
#         max-width: 70%;
#         display: inline-block;
#         border: 1px solid #eeeeee;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
#         color: #5d4037; /* Muted brown text */
#     }
#     /* Chat input styling to match background */
#     .stChatInput {
#         background: transparent; /* Transparent to blend with gradient */
#         border: none;
#         padding: 0 !important;
#         margin: 0 !important;
#     }
#     .stChatInput input {
#         border: 2px solid #f48fb1;
#         border-radius: 8px;
#         font-family: 'Arial', sans-serif;
#         background-color: #ffffff;
#         padding: 5px;
#     }
#     /* Button styling */
#     .stButton>button {
#         background-color: #f48fb1; /* Soft pink */
#         color: white;
#         border-radius: 8px;
#         border: none;
#         padding: 8px 16px;
#         font-family: 'Arial', sans-serif;
#         transition: background-color 0.3s;
#     }
#     .stButton>button:hover {
#         background-color: #f06292;
#     }
#     /* Text area styling */
#     .stTextArea textarea {
#         border: 2px solid #f48fb1; /* Soft pink border */
#         border-radius: 8px;
#         font-family: 'Arial', sans-serif;
#         background-color: #ffffff;
#     }
#     /* Remove extra spacing to eliminate empty bar */
#     .stApp, .stChatContainer, .stChatInputContainer, .stChatMessage, .stChatInput, .stMarkdown, .stSpinner, .stError {
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     div[data-testid="stVerticalBlock"], div[data-testid="stHorizontalBlock"] {
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     div[data-testid="stAppViewContainer"] {
#         padding: 0 !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Wrap content in custom container
# st.markdown('<div class="main-content">', unsafe_allow_html=True)

# # Header
# st.title("Medical Chatbot")
# st.markdown("Ask medical questions or check symptoms (not a doctor, just info).")

# # Load vector store
# embedding = Embedding(index_name="medical-index")
# vector_store = embedding.get_vector_store()

# # Initialize model
# model_api = ModelAPI(vector_store)

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

# if st.sidebar.button("Export Chat History as PDF"):
#     pdf_buffer = export_chat_history()
#     st.sidebar.download_button(
#         label="Download Chat History",
#         data=pdf_buffer,
#         file_name="chat_history.pdf",
#         mime="application/pdf"
#     )

# # Chat container with boxy UI
# st.markdown('<div class="chat-container">', unsafe_allow_html=True)
# # Initialize session state
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
# if "messages" not in st.session_state:
#     st.session_state.messages = [{"role": "assistant", "content": "How can I help with medical info today?"}]

# # Display chat messages
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(f'<div class="{msg["role"]}-message">{msg["content"]}</div>', unsafe_allow_html=True)

# # Handle user input
# if prompt := st.chat_input("Ask a medical question"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)

#     # Get response
#     answer = model_api.get_response(prompt, st.session_state.chat_history)
#     st.session_state.chat_history.append((prompt, answer))
#     st.session_state.messages.append({"role": "assistant", "content": answer})

#     with st.chat_message("assistant"):
#         st.markdown(f'<div class="assistant-message">{answer}</div>', unsafe_allow_html=True)

# st.markdown('</div>', unsafe_allow_html=True)
# st.markdown('</div>', unsafe_allow_html=True)

#Final 
# import streamlit as st
# from src.components.data_ingestion import DataIngestion
# from src.components.embedding import Embedding
# from src.components.model_api import ModelAPI
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet
# import io
# import re

# # Initialize Streamlit with sidebar always expanded
# st.set_page_config(
#     page_title="Medical Chatbot",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS with theme consistency fixes and subheading styling
# st.markdown(
#     """
#     <style>
#     /* Gradient background with pink, white, and cream */
#     .stApp {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important; /* Pink, white, cream */
#         color: #333333 !important;
#         margin: 0 !important;
#         padding: 0 !important;
#         overflow: hidden !important;
#     }
#     .main-content {
#         padding: 0 !important;
#         margin: 0 !important;
#         width: 100%;
#     }
#     /* Header styling */
#     h1 {
#         color: #f06292 !important; /* Muted pink */
#         text-align: center;
#         font-family: 'Arial', sans-serif;
#         text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
#         margin-bottom: 5px !important;
#     }
#     /* Ensure header color in both themes */
#     [data-theme="dark"] h1,
#     [data-theme="light"] h1 {
#         color: #f06292 !important;
#     }
#     /* Markdown text below title */
#     .stMarkdown p {
#         color: #5d4037 !important; /* Muted brown */
#         font-family: 'Arial', sans-serif;
#         text-align: center;
#         margin: 0 !important;
#         padding: 5px 0 !important;
#     }
#     /* Ensure Markdown text color in both themes */
#     [data-theme="dark"] .stMarkdown p,
#     [data-theme="light"] .stMarkdown p {
#         color: #5d4037 !important;
#     }
#     /* Sidebar styling for Symptom Checker with gradient */
#     .stSidebar {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important; /* Same gradient as app */
#         border-right: 2px solid #f48fb1; /* Soft pink border */
#         padding: 10px;
#     }
#     /* Ensure sidebar background in both themes */
#     [data-theme="dark"] .stSidebar,
#     [data-theme="light"] .stSidebar {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important;
#     }
#     .stSidebar h1 {
#         color: #f06292 !important; /* Muted pink */
#         font-size: 1.5em;
#         text-align: center;
#     }
#     /* Ensure sidebar heading color in both themes */
#     [data-theme="dark"] .stSidebar h1,
#     [data-theme="light"] .stSidebar h1 {
#         color: #f06292 !important;
#     }
#     /* Subheading styling for "Enter symptoms" */
#     h4 {
#         color: #f06292 !important; /* Muted pink to match Symptom Checker heading */
#         font-family: 'Arial', sans-serif;
#         font-size: 1.1em;
#         margin-bottom: 5px !important;
#     }
#     /* Ensure subheading color in both themes */
#     [data-theme="dark"] h4,
#     [data-theme="light"] h4 {
#         color: #f06292 !important;
#     }
#     /* Chat container styling */
#     .chat-container {
#         border: 2px solid #f48fb1; /* Soft pink border */
#         padding: 15px;
#         border-radius: 15px;
#         background-color: #ffffff !important; /* White for contrast */
#         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#         margin: 0 !important;
#         padding: 0 0 10px 0 !important;
#     }
#     /* Ensure chat container background in both themes */
#     [data-theme="dark"] .chat-container,
#     [data-theme="light"] .chat-container {
#         background-color: #ffffff !important;
#     }
#     /* Override Streamlit's default chat message styling to remove black bar */
#     [data-testid="stChatMessage"] {
#         background: transparent !important; /* Remove any default background */
#         border: none !important; /* Remove any default border */
#         box-shadow: none !important; /* Remove any default shadow */
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     /* Ensure no theme conflicts for chat messages */
#     [data-theme="dark"] [data-testid="stChatMessage"],
#     [data-theme="light"] [data-testid="stChatMessage"] {
#         background: transparent !important;
#         border: none !important;
#         box-shadow: none !important;
#     }
#     /* Chat message styling */
#     .user-message {
#         background-color: #f06292 !important; /* Pink for user */
#         padding: 12px;
#         border-radius: 15px;
#         margin: 5px 0 10px 0; /* Increased bottom margin to create gap */
#         max-width: 70%;
#         display: inline-block;
#         border: 1px solid #ec407a;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.05); /* Lighter shadow to avoid dark bar effect */
#         color: #ffffff !important; /* White text for contrast */
#     }
#     /* Ensure user message styles in both themes */
#     [data-theme="dark"] .user-message,
#     [data-theme="light"] .user-message {
#         background-color: #f06292 !important;
#         color: #ffffff !important;
#     }
#     .assistant-message {
#         background-color: #ffffff !important; /* White for chatbot */
#         padding: 12px;
#         border-radius: 15px;
#         margin: 5px 0;
#         max-width: 70%;
#         display: inline-block;
#         border: 1px solid #eeeeee;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
#         color: #5d4037 !important; /* Muted brown text */
#     }
#     /* Ensure assistant message styles in both themes */
#     [data-theme="dark"] .assistant-message,
#     [data-theme="light"] .assistant-message {
#         background-color: #ffffff !important;
#         color: #5d4037 !important;
#     }
#     /* Chat input styling with white background */
#     .stChatInput {
#         background: #ffffff !important; /* White background for the chat input container */
#         border: none;
#         padding: 5px !important;
#         margin: 0 !important;
#     }
#     /* Ensure chat input background in both themes */
#     [data-theme="dark"] .stChatInput,
#     [data-theme="light"] .stChatInput {
#         background: #ffffff !important;
#     }
#     .stChatInput input {
#         border: 2px solid #f48fb1;
#         border-radius: 8px;
#         font-family: 'Arial', sans-serif;
#         background-color: #ffffff !important; /* Ensure input field is white */
#         color: #333333 !important; /* Dark text for visibility */
#         padding: 5px;
#     }
#     /* Ensure chat input text color in both themes */
#     [data-theme="dark"] .stChatInput input,
#     [data-theme="light"] .stChatInput input {
#         background-color: #ffffff !important;
#         color: #333333 !important;
#     }
#     /* Button styling */
#     .stButton>button {
#         background-color: #f48fb1 !important; /* Soft pink */
#         color: white !important;
#         border-radius: 8px;
#         border: none;
#         padding: 8px 16px;
#         font-family: 'Arial', sans-serif;
#         transition: background-color 0.3s;
#     }
#     .stButton>button:hover {
#         background-color: #f06292 !important;
#     }
#     /* Ensure button styles in both themes */
#     [data-theme="dark"] .stButton>button,
#     [data-theme="light"] .stButton>button {
#         background-color: #f48fb1 !important;
#         color: white !important;
#     }
#     [data-theme="dark"] .stButton>button:hover,
#     [data-theme="light"] .stButton>button:hover {
#         background-color: #f06292 !important;
#     }
#     /* Text area styling */
#     .stTextArea textarea {
#         border: 2px solid #f48fb1; /* Soft pink border */
#         border-radius: 8px;
#         font-family: 'Arial', sans-serif;
#         background-color: #ffffff !important;
#         color: #333333 !important; /* Dark text for visibility */
#     }
#     /* Ensure text area styles in both themes */
#     [data-theme="dark"] .stTextArea textarea,
#     [data-theme="light"] .stTextArea textarea {
#         background-color: #ffffff !important;
#         color: #333333 !important;
#     }
#     /* Placeholder styling for text area */
#     .stTextArea textarea::placeholder {
#         color: #666666 !important; /* Medium-dark gray for placeholder */
#         font-family: 'Arial', sans-serif;
#         font-size: 14px; /* Slightly smaller */
#         opacity: 1; /* Ensure full visibility */
#     }
#     /* Ensure placeholder styles in both themes */
#     [data-theme="dark"] .stTextArea textarea::placeholder,
#     [data-theme="light"] .stTextArea textarea::placeholder {
#         color: #666666 !important;
#     }
#     /* Ensure Symptom Checker response text color in both themes */
#     [data-theme="dark"] .stSidebar .stMarkdown,
#     [data-theme="light"] .stSidebar .stMarkdown {
#         color: #5d4037 !important;
#     }
#     /* Remove extra spacing to eliminate empty bar */
#     .stApp, .stChatContainer, .stChatInputContainer, .stChatMessage, .stChatInput, .stMarkdown, .stSpinner, .stError {
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     div[data-testid="stVerticalBlock"], div[data-testid="stHorizontalBlock"] {
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     div[data-testid="stAppViewContainer"] {
#         padding: 0 !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Wrap content in custom container
# st.markdown('<div class="main-content">', unsafe_allow_html=True)

# # Header
# st.title("Medical Chatbot")
# st.markdown("Ask medical questions or check symptoms (not a doctor, just info).")

# # Load vector store
# embedding = Embedding(index_name="medical-index")
# vector_store = embedding.get_vector_store()

# # Initialize model
# model_api = ModelAPI(vector_store)

# # Sidebar (always expanded)
# with st.sidebar:
#     st.title("Symptom Checker")
#     st.markdown('<h4>Enter symptoms (e.g., fever, cough)</h4>', unsafe_allow_html=True)
#     symptoms = st.text_area("", placeholder="Type here...")
#     if st.button("Check Symptoms"):
#         if symptoms:
#             with st.spinner("Analyzing symptoms..."):
#                 response = model_api.check_symptoms(symptoms)
#                 st.markdown(f"**Analysis**: {response}")
#         else:
#             st.error("Please enter symptoms.")

#     # Chat History Export with Markdown Preprocessing
#     def export_chat_history():
#         buffer = io.BytesIO()
#         doc = SimpleDocTemplate(buffer, pagesize=letter)
#         styles = getSampleStyleSheet()
#         story = []

#         # Define styles for headings and normal text
#         heading_style = styles["Heading2"]  # Use Heading2 for ## headings
#         normal_style = styles["Normal"]

#         for msg in st.session_state.messages:
#             role = "User" if msg["role"] == "user" else "Assistant"
#             content = msg["content"]

#             # Preprocess Markdown for assistant messages
#             if role == "Assistant":
#                 # Replace Markdown headings (## Heading) with plain text for PDF
#                 content = re.sub(r'##\s*(.+)', r'\1', content)  # Remove ## and keep the heading text
#                 # Replace Markdown bold (**text**) with plain text (remove **)
#                 content = re.sub(r'\*\*(.+?)\*\*', r'\1', content)  # Remove ** and keep the text

#                 # Split content into lines to handle headings
#                 lines = content.split('\n')
#                 for line in lines:
#                     if line in ["Causes of Anemia", "Iron-Deficiency Anemia", "Sickle Cell Anemia"]:  # Example headings
#                         story.append(Paragraph(f"{role}: {line}", heading_style))
#                     else:
#                         story.append(Paragraph(f"{role}: {line}", normal_style))
#             else:
#                 # User messages can be added as-is
#                 story.append(Paragraph(f"{role}: {content}", normal_style))

#         doc.build(story)
#         buffer.seek(0)
#         return buffer

#     if st.button("Export Chat History as PDF"):
#         pdf_buffer = export_chat_history()
#         st.download_button(
#             label="Download Chat History",
#             data=pdf_buffer,
#             file_name="chat_history.pdf",
#             mime="application/pdf"
#         )

#     # Clear Chat Button
#     if st.button("Clear Chat"):
#         st.session_state.chat_history = []
#         st.session_state.messages = [{"role": "assistant", "content": "How can I help with medical info today?"}]
#         st.rerun()

# # Chat container with boxy UI
# st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# # Initialize session state
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
# if "messages" not in st.session_state:
#     st.session_state.messages = [{"role": "assistant", "content": "How can I help with medical info today?"}]

# # Function to preprocess assistant response for proper heading and bold rendering
# def preprocess_response(content):
#     # Convert Markdown headings (## Heading) to HTML <h2> for rendering in UI
#     content = re.sub(r'##\s*(.+)', r'<h2>\1</h2>', content)
#     # Convert Markdown bold (**text**) to HTML <strong> for rendering in UI
#     content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
#     return content

# # Display chat messages
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         if msg["role"] == "assistant":
#             # Preprocess assistant message to handle headings and bold text
#             processed_content = preprocess_response(msg["content"])
#             st.markdown(f'<div class="{msg["role"]}-message">{processed_content}</div>', unsafe_allow_html=True)
#         else:
#             # User messages don't need preprocessing
#             st.markdown(f'<div class="{msg["role"]}-message">{msg["content"]}</div>', unsafe_allow_html=True)

# # Handle user input
# if prompt := st.chat_input("Ask a medical question"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)

#     # Get response
#     answer = model_api.get_response(prompt, st.session_state.chat_history)
#     st.session_state.chat_history.append((prompt, answer))
#     st.session_state.messages.append({"role": "assistant", "content": answer})

#     with st.chat_message("assistant"):
#         # Preprocess the assistant response to render headings and bold text
#         processed_answer = preprocess_response(answer)
#         st.markdown(f'<div class="assistant-message">{processed_answer}</div>', unsafe_allow_html=True)

# st.markdown('</div>', unsafe_allow_html=True)
# st.markdown('</div>', unsafe_allow_html=True)


# the below code is the final code that give the correct results
# import streamlit as st
# from src.components.data_ingestion import DataIngestion
# from src.components.embedding import Embedding
# from src.components.model_api import ModelAPI
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet
# import io
# import re

# # Initialize Streamlit with sidebar always expanded
# st.set_page_config(
#     page_title="Medical Chatbot",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS with theme consistency fixes and subheading styling
# st.markdown(
#     """
#     <style>
#     /* Gradient background with pink, white, and cream */
#     .stApp {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important; /* Pink, white, cream */
#         color: #333333 !important;
#         margin: 0 !important;
#         padding: 0 !important;
#         overflow: hidden !important;
#     }
#     .main-content {
#         padding: 0 !important;
#         margin: 0 !important;
#         width: 100%;
#     }
#     /* Header styling */
#     h1 {
#         color: #f06292 !important; /* Muted pink */
#         text-align: center;
#         font-family: 'Arial', sans-serif;
#         text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
#         margin-bottom: 5px !important;
#     }
#     /* Ensure header color in both themes */
#     [data-theme="dark"] h1,
#     [data-theme="light"] h1 {
#         color: #f06292 !important;
#     }
#     /* Markdown text below title */
#     .stMarkdown p {
#         color: #5d4037 !important; /* Muted brown */
#         font-family: 'Arial', sans-serif;
#         text-align: center;
#         margin: 0 !important;
#         padding: 5px 0 !important;
#     }
#     /* Ensure Markdown text color in both themes */
#     [data-theme="dark"] .stMarkdown p,
#     [data-theme="light"] .stMarkdown p {
#         color: #5d4037 !important;
#     }
#     /* Sidebar styling for Symptom Checker with gradient */
#     .stSidebar {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important; /* Same gradient as app */
#         border-right: 2px solid #f48fb1; /* Soft pink border */
#         padding: 10px;
#     }
#     /* Ensure sidebar background in both themes */
#     [data-theme="dark"] .stSidebar,
#     [data-theme="light"] .stSidebar {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important;
#     }
#     .stSidebar h1 {
#         color: #f06292 !important; /* Muted pink */
#         font-size: 1.5em;
#         text-align: center;
#     }
#     /* Ensure sidebar heading color in both themes */
#     [data-theme="dark"] .stSidebar h1,
#     [data-theme="light"] .stSidebar h1 {
#         color: #f06292 !important;
#     }
#     /* Subheading styling for "Enter symptoms" */
#     h4 {
#         color: #f06292 !important; /* Muted pink to match Symptom Checker heading */
#         font-family: 'Arial', sans-serif;
#         font-size: 1.1em;
#         margin-bottom: 5px !important;
#     }
#     /* Ensure subheading color in both themes */
#     [data-theme="dark"] h4,
#     [data-theme="light"] h4 {
#         color: #f06292 !important;
#     }
#     /* Chat container styling */
#     .chat-container {
#         border: 2px solid #f48fb1; /* Soft pink border */
#         padding: 15px;
#         border-radius: 15px;
#         background-color: #ffffff !important; /* White for contrast */
#         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#         margin: 0 !important;
#         padding: 0 0 10px 0 !important;
#     }
#     /* Ensure chat container background in both themes */
#     [data-theme="dark"] .chat-container,
#     [data-theme="light"] .chat-container {
#         background-color: #ffffff !important;
#     }
#     /* Override Streamlit's default chat message styling to remove black bar */
#     [data-testid="stChatMessage"] {
#         background: transparent !important; /* Remove any default background */
#         border: none !important; /* Remove any default border */
#         box-shadow: none !important; /* Remove any default shadow */
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     /* Ensure no theme conflicts for chat messages */
#     [data-theme="dark"] [data-testid="stChatMessage"],
#     [data-theme="light"] [data-testid="stChatMessage"] {
#         background: transparent !important;
#         border: none !important;
#         box-shadow: none !important;
#     }
#     /* Chat message styling */
#     .user-message {
#         background-color: #f06292 !important; /* Pink for user */
#         padding: 12px;
#         border-radius: 15px;
#         margin: 5px 0 10px 0; /* Increased bottom margin to create gap */
#         max-width: 70%;
#         display: inline-block;
#         border: 1px solid #ec407a;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.05); /* Lighter shadow to avoid dark bar effect */
#         color: #ffffff !important; /* White text for contrast */
#     }
#     /* Ensure user message styles in both themes */
#     [data-theme="dark"] .user-message,
#     [data-theme="light"] .user-message {
#         background-color: #f06292 !important;
#         color: #ffffff !important;
#     }
#     .assistant-message {
#         background-color: #ffffff !important; /* White for chatbot */
#         padding: 12px;
#         border-radius: 15px;
#         margin: 5px 0;
#         max-width: 70%;
#         display: inline-block;
#         border: 1px solid #eeeeee;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
#         color: #5d4037 !important; /* Muted brown text */
#     }
#     /* Ensure assistant message styles in both themes */
#     [data-theme="dark"] .assistant-message,
#     [data-theme="light"] .assistant-message {
#         background-color: #ffffff !important;
#         color: #5d4037 !important;
#     }
#     /* Chat input styling with white background */
#     .stChatInput {
#         background: #ffffff !important; /* White background for the chat input container */
#         border: none;
#         padding: 5px !important;
#         margin: 0 !important;
#     }
#     /* Ensure chat input background in both themes */
#     [data-theme="dark"] .stChatInput,
#     [data-theme="light"] .stChatInput {
#         background: #ffffff !important;
#     }
#     .stChatInput input {
#         border: 2px solid #f48fb1;
#         border-radius: 8px;
#         font-family: 'Arial', sans-serif;
#         background-color: #ffffff !important; /* Ensure input field is white */
#         color: #333333 !important; /* Dark text for visibility */
#         padding: 5px;
#     }
#     /* Ensure chat input text color in both themes */
#     [data-theme="dark"] .stChatInput input,
#     [data-theme="light"] .stChatInput input {
#         background-color: #ffffff !important;
#         color: #333333 !important;
#     }
#     /* Button styling */
#     .stButton>button {
#         background-color: #f48fb1 !important; /* Soft pink */
#         color: white !important;
#         border-radius: 8px;
#         border: none;
#         padding: 8px 16px;
#         font-family: 'Arial', sans-serif;
#         transition: background-color 0.3s;
#     }
#     .stButton>button:hover {
#         background-color: #f06292 !important;
#     }
#     /* Ensure button styles in both themes */
#     [data-theme="dark"] .stButton>button,
#     [data-theme="light"] .stButton>button {
#         background-color: #f48fb1 !important;
#         color: white !important;
#     }
#     [data-theme="dark"] .stButton>button:hover,
#     [data-theme="light"] .stButton>button:hover {
#         background-color: #f06292 !important;
#     }
#     /* Text area styling */
#     .stTextArea textarea {
#         border: 2px solid #f48fb1; /* Soft pink border */
#         border-radius: 8px;
#         font-family: 'Arial', sans-serif;
#         background-color: #ffffff !important;
#         color: #333333 !important; /* Dark text for visibility */
#     }
#     /* Ensure text area styles in both themes */
#     [data-theme="dark"] .stTextArea textarea,
#     [data-theme="light"] .stTextArea textarea {
#         background-color: #ffffff !important;
#         color: #333333 !important;
#     }
#     /* Placeholder styling for text area */
#     .stTextArea textarea::placeholder {
#         color: #666666 !important; /* Medium-dark gray for placeholder */
#         font-family: 'Arial', sans-serif;
#         font-size: 14px; /* Slightly smaller */
#         opacity: 1; /* Ensure full visibility */
#     }
#     /* Ensure placeholder styles in both themes */
#     [data-theme="dark"] .stTextArea textarea::placeholder,
#     [data-theme="light"] .stTextArea textarea::placeholder {
#         color: #666666 !important;
#     }
#     /* Ensure Symptom Checker response text color in both themes */
#     [data-theme="dark"] .stSidebar .stMarkdown,
#     [data-theme="light"] .stSidebar .stMarkdown {
#         color: #5d4037 !important;
#     }
#     /* Remove extra spacing to eliminate empty bar */
#     .stApp, .stChatContainer, .stChatInputContainer, .stChatMessage, .stChatInput, .stMarkdown, .stSpinner, .stError {
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     div[data-testid="stVerticalBlock"], div[data-testid="stHorizontalBlock"] {
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     div[data-testid="stAppViewContainer"] {
#         padding: 0 !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Wrap content in custom container
# st.markdown('<div class="main-content">', unsafe_allow_html=True)

# # Header
# st.title("Medical Chatbot")
# st.markdown("Ask medical questions or check symptoms (not a doctor, just info).")

# # Load vector store
# embedding = Embedding(index_name="medical-index")
# vector_store = embedding.get_vector_store()

# # Initialize model
# model_api = ModelAPI(vector_store)

# # Sidebar (always expanded)
# with st.sidebar:
#     st.title("Symptom Checker")
#     st.markdown('<h4>Enter symptoms (e.g., fever, cough)</h4>', unsafe_allow_html=True)
#     symptoms = st.text_area("", placeholder="Type here...")
#     if st.button("Check Symptoms"):
#         if symptoms:
#             with st.spinner("Analyzing symptoms..."):
#                 response = model_api.check_symptoms(symptoms)
#                 st.markdown(f"**Analysis**: {preprocess_response(response)}")
#         else:
#             st.error("Please enter symptoms.")

#     # Chat History Export with Markdown Preprocessing
#     def export_chat_history():
#         buffer = io.BytesIO()
#         doc = SimpleDocTemplate(buffer, pagesize=letter)
#         styles = getSampleStyleSheet()
#         story = []

#         # Define styles for headings and normal text
#         heading_style = styles["Heading2"]  # Use Heading2 for ## headings
#         normal_style = styles["Normal"]

#         for msg in st.session_state.messages:
#             role = "User" if msg["role"] == "user" else "Assistant"
#             content = msg["content"]

#             # Preprocess Markdown for assistant messages
#             if role == "Assistant":
#                 # Replace Markdown headings (## Heading) with plain text for PDF
#                 content = re.sub(r'##\s*(.+)', r'\1', content)  # Remove ## and keep the heading text
#                 # Replace Markdown bold (**text**) with plain text (remove **)
#                 content = re.sub(r'\*\*(.+?)\*\*', r'\1', content)  # Remove ** and keep the text

#                 # Split content into lines to handle headings
#                 lines = content.split('\n')
#                 for line in lines:
#                     if line in ["Causes of Anemia", "Iron-Deficiency Anemia", "Sickle Cell Anemia"]:  # Example headings
#                         story.append(Paragraph(f"{role}: {line}", heading_style))
#                     else:
#                         story.append(Paragraph(f"{role}: {line}", normal_style))
#             else:
#                 # User messages can be added as-is
#                 story.append(Paragraph(f"{role}: {content}", normal_style))

#         doc.build(story)
#         buffer.seek(0)
#         return buffer

#     if st.button("Export Chat History as PDF"):
#         pdf_buffer = export_chat_history()
#         st.download_button(
#             label="Download Chat History",
#             data=pdf_buffer,
#             file_name="chat_history.pdf",
#             mime="application/pdf"
#         )

#     # Clear Chat Button
#     if st.button("Clear Chat"):
#         st.session_state.chat_history = []
#         st.session_state.messages = [{"role": "assistant", "content": "How can I help with medical info today?"}]
#         st.rerun()

# # Chat container with boxy UI
# st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# # Initialize session state
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
# if "messages" not in st.session_state:
#     st.session_state.messages = [{"role": "assistant", "content": "How can I help with medical info today?"}]

# # Function to preprocess assistant response for proper heading and bold rendering
# def preprocess_response(content):
#     # Convert Markdown headings (# Heading or ## Heading) to HTML <h2> for rendering in UI
#     content = re.sub(r'#+\s*(.+)', r'<h2>\1</h2>', content)
#     # Convert Markdown bold (**text**) to HTML <strong> for rendering in UI
#     content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
#     return content

# # Display chat messages
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         if msg["role"] == "assistant":
#             # Preprocess assistant message to handle headings and bold text
#             processed_content = preprocess_response(msg["content"])
#             st.markdown(f'<div class="{msg["role"]}-message">{processed_content}</div>', unsafe_allow_html=True)
#         else:
#             # User messages don't need preprocessing
#             st.markdown(f'<div class="{msg["role"]}-message">{msg["content"]}</div>', unsafe_allow_html=True)

# # Handle user input
# if prompt := st.chat_input("Ask a medical question"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)

#     # Get response
#     answer = model_api.get_response(prompt, st.session_state.chat_history)
#     st.session_state.chat_history.append((prompt, answer))
#     st.session_state.messages.append({"role": "assistant", "content": answer})

#     with st.chat_message("assistant"):
#         # Preprocess the assistant response to render headings and bold text
#         processed_answer = preprocess_response(answer)
#         st.markdown(f'<div class="assistant-message">{processed_answer}</div>', unsafe_allow_html=True)

# st.markdown('</div>', unsafe_allow_html=True)
# st.markdown('</div>', unsafe_allow_html=True)
#retained symptom checker
# import streamlit as st
# from src.components.data_ingestion import DataIngestion
# from src.components.embedding import Embedding
# from src.components.model_api import ModelAPI
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet
# import io
# import re

# # Initialize Streamlit with sidebar always expanded
# st.set_page_config(
#     page_title="Medical Chatbot",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS with theme consistency fixes and subheading styling
# st.markdown(
#     """
#     <style>
#     /* Gradient background with pink, white, and cream */
#     .stApp {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important; /* Pink, white, cream */
#         color: #333333 !important;
#         margin: 0 !important;
#         padding: 0 !important;
#         overflow: hidden !important;
#     }
#     .main-content {
#         padding: 0 !important;
#         margin: 0 !important;
#         width: 100%;
#     }
#     /* Header styling */
#     h1 {
#         color: #f06292 !important; /* Muted pink */
#         text-align: center;
#         font-family: 'Arial', sans-serif;
#         text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
#         margin-bottom: 5px !important;
#     }
#     /* Ensure header color in both themes */
#     [data-theme="dark"] h1,
#     [data-theme="light"] h1 {
#         color: #f06292 !important;
#     }
#     /* Markdown text below title */
#     .stMarkdown p {
#         color: #5d4037 !important; /* Muted brown */
#         font-family: 'Arial', sans-serif;
#         text-align: center;
#         margin: 0 !important;
#         padding: 5px 0 !important;
#     }
#     /* Ensure Markdown text color in both themes */
#     [data-theme="dark"] .stMarkdown p,
#     [data-theme="light"] .stMarkdown p {
#         color: #5d4037 !important;
#     }
#     /* Sidebar styling for Symptom Checker with gradient */
#     .stSidebar {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important; /* Same gradient as app */
#         border-right: 2px solid #f48fb1; /* Soft pink border */
#         padding: 10px;
#     }
#     /* Ensure sidebar background in both themes */
#     [data-theme="dark"] .stSidebar,
#     [data-theme="light"] .stSidebar {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important;
#     }
#     .stSidebar h1 {
#         color: #f06292 !important; /* Muted pink */
#         font-size: 1.5em;
#         text-align: center;
#     }
#     /* Ensure sidebar heading color in both themes */
#     [data-theme="dark"] .stSidebar h1,
#     [data-theme="light"] .stSidebar h1 {
#         color: #f06292 !important;
#     }
#     /* Subheading styling for "Enter symptoms" */
#     h4 {
#         color: #f06292 !important; /* Muted pink to match Symptom Checker heading */
#         font-family: 'Arial', sans-serif;
#         font-size: 1.1em;
#         margin-bottom: 5px !important;
#     }
#     /* Ensure subheading color in both themes */
#     [data-theme="dark"] h4,
#     [data-theme="light"] h4 {
#         color: #f06292 !important;
#     }
#     /* Chat container styling */
#     .chat-container {
#         border: 2px solid #f48fb1; /* Soft pink border */
#         padding: 15px;
#         border-radius: 15px;
#         background-color: #ffffff !important; /* White for contrast */
#         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#         margin: 0 !important;
#         padding: 0 0 10px 0 !important;
#     }
#     /* Ensure chat container background in both themes */
#     [data-theme="dark"] .chat-container,
#     [data-theme="light"] .chat-container {
#         background-color: #ffffff !important;
#     }
#     /* Override Streamlit's default chat message styling to remove black bar */
#     [data-testid="stChatMessage"] {
#         background: transparent !important; /* Remove any default background */
#         border: none !important; /* Remove any default border */
#         box-shadow: none !important; /* Remove any default shadow */
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     /* Ensure no theme conflicts for chat messages */
#     [data-theme="dark"] [data-testid="stChatMessage"],
#     [data-theme="light"] [data-testid="stChatMessage"] {
#         background: transparent !important;
#         border: none !important;
#         box-shadow: none !important;
#     }
#     /* Chat message styling */
#     .user-message {
#         background-color: #f06292 !important; /* Pink for user */
#         padding: 12px;
#         border-radius: 15px;
#         margin: 5px 0 10px 0; /* Increased bottom margin to create gap */
#         max-width: 70%;
#         display: inline-block;
#         border: 1px solid #ec407a;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.05); /* Lighter shadow to avoid dark bar effect */
#         color: #ffffff !important; /* White text for contrast */
#     }
#     /* Ensure user message styles in both themes */
#     [data-theme="dark"] .user-message,
#     [data-theme="light"] .user-message {
#         background-color: #f06292 !important;
#         color: #ffffff !important;
#     }
#     .assistant-message {
#         background-color: #ffffff !important; /* White for chatbot */
#         padding: 12px;
#         border-radius: 15px;
#         margin: 5px 0;
#         max-width: 70%;
#         display: inline-block;
#         border: 1px solid #eeeeee;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
#         color: #5d4037 !important; /* Muted brown text */
#     }
#     /* Ensure assistant message styles in both themes */
#     [data-theme="dark"] .assistant-message,
#     [data-theme="light"] .assistant-message {
#         background-color: #ffffff !important;
#         color: #5d4037 !important;
#     }
#     /* Bullet point styling */
#     ul {
#         list-style-type: disc;
#         margin: 10px 0;
#         padding-left: 20px;
#     }
#     li {
#         color: #5d4037 !important; /* Match assistant message text color */
#         margin-bottom: 5px;
#     }
#     [data-theme="dark"] ul, [data-theme="light"] ul {
#         list-style-type: disc;
#     }
#     [data-theme="dark"] li, [data-theme="light"] li {
#         color: #5d4037 !important;
#     }
#     /* Chat input styling with white background */
#     .stChatInput {
#         background: #ffffff !important; /* White background for the chat input container */
#         border: none;
#         padding: 5px !important;
#         margin: 0 !important;
#     }
#     /* Ensure chat input background in both themes */
#     [data-theme="dark"] .stChatInput,
#     [data-theme="light"] .stChatInput {
#         background: #ffffff !important;
#     }
#     .stChatInput input {
#         border: 2px solid #f48fb1;
#         border-radius: 8px;
#         font-family: 'Arial', sans-serif;
#         background-color: #ffffff !important; /* Ensure input field is white */
#         color: #333333 !important; /* Dark text for visibility */
#         padding: 5px;
#     }
#     /* Ensure chat input text color in both themes */
#     [data-theme="dark"] .stChatInput input,
#     [data-theme="light"] .stChatInput input {
#         background-color: #ffffff !important;
#         color: #333333 !important;
#     }
#     /* Button styling */
#     .stButton>button {
#         background-color: #f48fb1 !important; /* Soft pink */
#         color: white !important;
#         border-radius: 8px;
#         border: none;
#         padding: 8px 16px;
#         font-family: 'Arial', sans-serif;
#         transition: background-color 0.3s;
#     }
#     .stButton>button:hover {
#         background-color: #f06292 !important;
#     }
#     /* Ensure button styles in both themes */
#     [data-theme="dark"] .stButton>button,
#     [data-theme="light"] .stButton>button {
#         background-color: #f48fb1 !important;
#         color: white !important;
#     }
#     [data-theme="dark"] .stButton>button:hover,
#     [data-theme="light"] .stButton>button:hover {
#         background-color: #f06292 !important;
#     }
#     /* Text area styling */
#     .stTextArea textarea {
#         border: 2px solid #f48fb1; /* Soft pink border */
#         border-radius: 8px;
#         font-family: 'Arial', sans-serif;
#         background-color: #ffffff !important;
#         color: #333333 !important; /* Dark text for visibility */
#     }
#     /* Ensure text area styles in both themes */
#     [data-theme="dark"] .stTextArea textarea,
#     [data-theme="light"] .stTextArea textarea {
#         background-color: #ffffff !important;
#         color: #333333 !important;
#     }
#     /* Placeholder styling for text area */
#     .stTextArea textarea::placeholder {
#         color: #666666 !important; /* Medium-dark gray for placeholder */
#         font-family: 'Arial', sans-serif;
#         font-size: 14px; /* Slightly smaller */
#         opacity: 1; /* Ensure full visibility */
#     }
#     /* Ensure placeholder styles in both themes */
#     [data-theme="dark"] .stTextArea textarea::placeholder,
#     [data-theme="light"] .stTextArea textarea::placeholder {
#         color: #666666 !important;
#     }
#     /* Ensure Symptom Checker response text color in both themes */
#     [data-theme="dark"] .stSidebar .stMarkdown,
#     [data-theme="light"] .stSidebar .stMarkdown {
#         color: #5d4037 !important;
#     }
#     /* Remove extra spacing to eliminate empty bar */
#     .stApp, .stChatContainer, .stChatInputContainer, .stChatMessage, .stChatInput, .stMarkdown, .stSpinner, .stError {
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     div[data-testid="stVerticalBlock"], div[data-testid="stHorizontalBlock"] {
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     div[data-testid="stAppViewContainer"] {
#         padding: 0 !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Function to preprocess assistant response for proper heading and bullet rendering
# def preprocess_response(content):
#     # Convert Markdown headings (## Heading) to HTML <h2> for rendering in UI
#     content = re.sub(r'##\s*(.+)', r'<h2>\1</h2>', content)
#     # Ensure bullet points are styled consistently
#     content = re.sub(r'-\s*(.+)', r'<li>\1</li>', content)
#     # Wrap bullet points in an unordered list
#     content = re.sub(r'(<li>.+?</li>\n?)+', r'<ul>\g<0></ul>', content)
#     return content

# # Wrap content in custom container
# st.markdown('<div class="main-content">', unsafe_allow_html=True)

# # Header
# st.title("Medical Chatbot")
# st.markdown("Ask medical questions or check symptoms (not a doctor, just info).")

# # Load vector store
# embedding = Embedding(index_name="medical-index")
# vector_store = embedding.get_vector_store()

# # Initialize model
# model_api = ModelAPI(vector_store)

# # Sidebar (always expanded)
# with st.sidebar:
#     st.title("Symptom Checker")
#     st.markdown('<h4>Enter symptoms (e.g., fever, cough)</h4>', unsafe_allow_html=True)
#     symptoms = st.text_area("", placeholder="Type here...")
#     if st.button("Check Symptoms"):
#         if symptoms:
#             with st.spinner("Analyzing symptoms..."):
#                 response = model_api.check_symptoms(symptoms)
#                 st.markdown(f"**Analysis**: {response}")
#         else:
#             st.error("Please enter symptoms.")

#     # Chat History Export with Markdown Preprocessing
#     def export_chat_history():
#         buffer = io.BytesIO()
#         doc = SimpleDocTemplate(buffer, pagesize=letter)
#         styles = getSampleStyleSheet()
#         story = []

#         # Define styles for headings and normal text
#         heading_style = styles["Heading2"]  # Use Heading2 for ## headings
#         normal_style = styles["Normal"]

#         for msg in st.session_state.messages:
#             role = "User" if msg["role"] == "user" else "Assistant"
#             content = msg["content"]

#             # Preprocess Markdown for assistant messages
#             if role == "Assistant":
#                 # Replace Markdown headings (## Heading) with plain text for PDF
#                 content = re.sub(r'##\s*(.+)', r'\1', content)  # Remove ## and keep the heading text
#                 # Replace Markdown bold (**text**) with plain text (remove **)
#                 content = re.sub(r'\*\*(.+?)\*\*', r'\1', content)  # Remove ** and keep the text

#                 # Split content into lines to handle headings
#                 lines = content.split('\n')
#                 for line in lines:
#                     if line in ["Causes of Anemia", "Iron-Deficiency Anemia", "Sickle Cell Anemia"]:  # Example headings
#                         story.append(Paragraph(f"{role}: {line}", heading_style))
#                     else:
#                         story.append(Paragraph(f"{role}: {line}", normal_style))
#             else:
#                 # User messages can be added as-is
#                 story.append(Paragraph(f"{role}: {content}", normal_style))

#         doc.build(story)
#         buffer.seek(0)
#         return buffer

#     if st.button("Export Chat History as PDF"):
#         pdf_buffer = export_chat_history()
#         st.download_button(
#             label="Download Chat History",
#             data=pdf_buffer,
#             file_name="chat_history.pdf",
#             mime="application/pdf"
#         )

#     # Clear Chat Button
#     if st.button("Clear Chat"):
#         st.session_state.chat_history = []
#         st.session_state.messages = [{"role": "assistant", "content": "How can I help with medical info today?"}]
#         st.rerun()

# # Chat container with boxy UI
# st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# # Initialize session state
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
# if "messages" not in st.session_state:
#     st.session_state.messages = [{"role": "assistant", "content": "How can I help with medical info today?"}]

# # Display chat messages
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         if msg["role"] == "assistant":
#             # Preprocess assistant message to handle headings and bullet points
#             processed_content = preprocess_response(msg["content"])
#             st.markdown(f'<div class="{msg["role"]}-message">{processed_content}</div>', unsafe_allow_html=True)
#         else:
#             # User messages don't need preprocessing
#             st.markdown(f'<div class="{msg["role"]}-message">{msg["content"]}</div>', unsafe_allow_html=True)

# # Handle user input
# if prompt := st.chat_input("Ask a medical question"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)

#     # Get response
#     answer = model_api.get_response(prompt, st.session_state.chat_history)
#     st.session_state.chat_history.append((prompt, answer))
#     st.session_state.messages.append({"role": "assistant", "content": answer})

#     with st.chat_message("assistant"):
#         # Preprocess the assistant response to render headings and bullet points
#         processed_answer = preprocess_response(answer)
#         st.markdown(f'<div class="assistant-message">{processed_answer}</div>', unsafe_allow_html=True)

# st.markdown('</div>', unsafe_allow_html=True)
# st.markdown('</div>', unsafe_allow_html=True)

# import streamlit as st
# from src.components.data_ingestion import DataIngestion
# from src.components.embedding import Embedding
# from src.components.model_api import ModelAPI
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet
# import io
# import re

# # Initialize Streamlit with sidebar always expanded
# st.set_page_config(
#     page_title="Medical Chatbot",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS with theme consistency fixes and subheading styling
# st.markdown(
#     """
#     <style>
#     /* Gradient background with pink, white, and cream */
#     .stApp {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important; /* Pink, white, cream */
#         color: #333333 !important;
#         margin: 0 !important;
#         padding: 0 !important;
#         overflow: hidden !important;
#     }
#     .main-content {
#         padding: 0 !important;
#         margin: 0 !important;
#         width: 100%;
#     }
#     /* Header styling */
#     h1 {
#         color: #f06292 !important; /* Muted pink */
#         text-align: center;
#         font-family: 'Arial', sans-serif;
#         text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
#         margin-bottom: 5px !important;
#     }
#     /* Ensure header color in both themes */
#     [data-theme="dark"] h1,
#     [data-theme="light"] h1 {
#         color: #f06292 !important;
#     }
#     /* Markdown text below title */
#     .stMarkdown p {
#         color: #5d4037 !important; /* Muted brown */
#         font-family: 'Arial', sans-serif;
#         text-align: center;
#         margin: 0 !important;
#         padding: 5px 0 !important;
#     }
#     /* Ensure Markdown text color in both themes */
#     [data-theme="dark"] .stMarkdown p,
#     [data-theme="light"] .stMarkdown p {
#         color: #5d4037 !important;
#     }
#     /* Sidebar styling for Symptom Checker with gradient */
#     .stSidebar {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important; /* Same gradient as app */
#         border-right: 2px solid #f48fb1; /* Soft pink border */
#         padding: 10px;
#     }
#     /* Ensure sidebar background in both themes */
#     [data-theme="dark"] .stSidebar,
#     [data-theme="light"] .stSidebar {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important;
#     }
#     .stSidebar h1 {
#         color: #f06292 !important; /* Muted pink */
#         font-size: 1.5em;
#         text-align: center;
#     }
#     /* Ensure sidebar heading color in both themes */
#     [data-theme="dark"] .stSidebar h1,
#     [data-theme="light"] .stSidebar h1 {
#         color: #f06292 !important;
#     }
#     /* Subheading styling for "Enter symptoms" */
#     h4 {
#         color: #f06292 !important; /* Muted pink to match Symptom Checker heading */
#         font-family: 'Arial', sans-serif;
#         font-size: 1.1em;
#         margin-bottom: 5px !important;
#     }
#     /* Ensure subheading color in both themes */
#     [data-theme="dark"] h4,
#     [data-theme="light"] h4 {
#         color: #f06292 !important;
#     }
#     /* Chat container styling */
#     .chat-container {
#         border: 2px solid #f48fb1; /* Soft pink border */
#         padding: 15px;
#         border-radius: 15px;
#         background-color: #ffffff !important; /* White for contrast */
#         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#         margin: 0 !important;
#         padding: 0 0 10px 0 !important;
#     }
#     /* Ensure chat container background in both themes */
#     [data-theme="dark"] .chat-container,
#     [data-theme="light"] .chat-container {
#         background-color: #ffffff !important;
#     }
#     /* Override Streamlit's default chat message styling to remove black bar */
#     [data-testid="stChatMessage"] {
#         background: transparent !important; /* Remove any default background */
#         border: none !important; /* Remove any default border */
#         box-shadow: none !important; /* Remove any default shadow */
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     /* Ensure no theme conflicts for chat messages */
#     [data-theme="dark"] [data-testid="stChatMessage"],
#     [data-theme="light"] [data-testid="stChatMessage"] {
#         background: transparent !important;
#         border: none !important;
#         box-shadow: none !important;
#     }
#     /* Chat message styling */
#     .user-message {
#         background-color: #f06292 !important; /* Pink for user */
#         padding: 12px;
#         border-radius: 15px;
#         margin: 5px 0 10px 0; /* Increased bottom margin to create gap */
#         max-width: 70%;
#         display: inline-block;
#         border: 1px solid #ec407a;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.05); /* Lighter shadow to avoid dark bar effect */
#         color: #ffffff !important; /* White text for contrast */
#     }
#     /* Ensure user message styles in both themes */
#     [data-theme="dark"] .user-message,
#     [data-theme="light"] .user-message {
#         background-color: #f06292 !important;
#         color: #ffffff !important;
#     }
#     .assistant-message {
#         background-color: #ffffff !important; /* White for chatbot */
#         padding: 12px;
#         border-radius: 15px;
#         margin: 5px 0;
#         max-width: 70%;
#         display: inline-block;
#         border: 1px solid #eeeeee;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
#         color: #5d4037 !important; /* Muted brown text */
#     }
#     /* Ensure assistant message styles in both themes */
#     [data-theme="dark"] .assistant-message,
#     [data-theme="light"] .assistant-message {
#         background-color: #ffffff !important;
#         color: #5d4037 !important;
#     }
#     /* Chat input styling with white background */
#     .stChatInput {
#         background: #ffffff !important; /* White background for the chat input container */
#         border: none;
#         padding: 5px !important;
#         margin: 0 !important;
#     }
#     /* Ensure chat input background in both themes */
#     [data-theme="dark"] .stChatInput,
#     [data-theme="light"] .stChatInput {
#         background: #ffffff !important;
#     }
#     .stChatInput input {
#         border: 2px solid #f48fb1;
#         border-radius: 8px;
#         font-family: 'Arial', sans-serif;
#         background-color: #ffffff !important; /* Ensure input field is white */
#         color: #333333 !important; /* Dark text for visibility */
#         padding: 5px;
#     }
#     /* Ensure chat input text color in both themes */
#     [data-theme="dark"] .stChatInput input,
#     [data-theme="light"] .stChatInput input {
#         background-color: #ffffff !important;
#         color: #333333 !important;
#     }
#     /* Button styling */
#     .stButton>button {
#         background-color: #f48fb1 !important; /* Soft pink */
#         color: white !important;
#         border-radius: 8px;
#         border: none;
#         padding: 8px 16px;
#         font-family: 'Arial', sans-serif;
#         transition: background-color 0.3s;
#     }
#     .stButton>button:hover {
#         background-color: #f06292 !important;
#     }
#     /* Ensure button styles in both themes */
#     [data-theme="dark"] .stButton>button,
#     [data-theme="light"] .stButton>button {
#         background-color: #f48fb1 !important;
#         color: white !important;
#     }
#     [data-theme="dark"] .stButton>button:hover,
#     [data-theme="light"] .stButton>button:hover {
#         background-color: #f06292 !important;
#     }
#     /* Text area styling */
#     .stTextArea textarea {
#         border: 2px solid #f48fb1; /* Soft pink border */
#         border-radius: 8px;
#         font-family: 'Arial', sans-serif;
#         background-color: #ffffff !important;
#         color: #333333 !important; /* Dark text for visibility */
#     }
#     /* Ensure text area styles in both themes */
#     [data-theme="dark"] .stTextArea textarea,
#     [data-theme="light"] .stTextArea textarea {
#         background-color: #ffffff !important;
#         color: #333333 !important;
#     }
#     /* Placeholder styling for text area */
#     .stTextArea textarea::placeholder {
#         color: #666666 !important; /* Medium-dark gray for placeholder */
#         font-family: 'Arial', sans-serif;
#         font-size: 14px; /* Slightly smaller */
#         opacity: 1; /* Ensure full visibility */
#     }
#     /* Ensure placeholder styles in both themes */
#     [data-theme="dark"] .stTextArea textarea::placeholder,
#     [data-theme="light"] .stTextArea textarea::placeholder {
#         color: #666666 !important;
#     }
#     /* Ensure Symptom Checker response text color in both themes */
#     [data-theme="dark"] .stSidebar .stMarkdown,
#     [data-theme="light"] .stSidebar .stMarkdown {
#         color: #5d4037 !important;
#     }
#     /* Remove extra spacing to eliminate empty bar */
#     .stApp, .stChatContainer, .stChatInputContainer, .stChatMessage, .stChatInput, .stMarkdown, .stSpinner, .stError {
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     div[data-testid="stVerticalBlock"], div[data-testid="stHorizontalBlock"] {
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     div[data-testid="stAppViewContainer"] {
#         padding: 0 !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Wrap content in custom container
# st.markdown('<div class="main-content">', unsafe_allow_html=True)

# # Header
# st.title("Medical Chatbot")
# st.markdown("Ask medical questions or check symptoms (not a doctor, just info).")

# # Load vector store
# embedding = Embedding(index_name="medical-index")
# vector_store = embedding.get_vector_store()

# # Initialize model
# model_api = ModelAPI(vector_store)

# # Sidebar (always expanded)
# with st.sidebar:
#     st.title("Symptom Checker")
#     st.markdown('<h4>Enter symptoms (e.g., fever, cough)</h4>', unsafe_allow_html=True)
#     symptoms = st.text_area("", placeholder="Type here...")
#     if st.button("Check Symptoms"):
#         if symptoms:
#             with st.spinner("Analyzing symptoms..."):
#                 response = model_api.check_symptoms(symptoms)
#                 st.markdown(f"**Analysis**: {response}")
#         else:
#             st.error("Please enter symptoms.")

#     # Chat History Export with Markdown Preprocessing
#     def export_chat_history():
#         buffer = io.BytesIO()
#         doc = SimpleDocTemplate(buffer, pagesize=letter)
#         styles = getSampleStyleSheet()
#         story = []

#         # Define styles for headings and normal text
#         heading_style = styles["Heading2"]  # Use Heading2 for ## headings
#         normal_style = styles["Normal"]

#         for msg in st.session_state.messages:
#             role = "User" if msg["role"] == "user" else "Assistant"
#             content = msg["content"]

#             # Preprocess Markdown for assistant messages
#             if role == "Assistant":
#                 # Replace Markdown headings (## Heading) with plain text for PDF
#                 content = re.sub(r'##\s*(.+)', r'\1', content)  # Remove ## and keep the heading text
#                 # Replace Markdown bold (**text**) with plain text (remove **)
#                 content = re.sub(r'\*\*(.+?)\*\*', r'\1', content)  # Remove ** and keep the text

#                 # Split content into lines to handle headings
#                 lines = content.split('\n')
#                 for line in lines:
#                     if line in ["Causes of Anemia", "Iron-Deficiency Anemia", "Sickle Cell Anemia"]:  # Example headings
#                         story.append(Paragraph(f"{role}: {line}", heading_style))
#                     else:
#                         story.append(Paragraph(f"{role}: {line}", normal_style))
#             else:
#                 # User messages can be added as-is
#                 story.append(Paragraph(f"{role}: {content}", normal_style))

#         doc.build(story)
#         buffer.seek(0)
#         return buffer

#     if st.button("Export Chat History as PDF"):
#         pdf_buffer = export_chat_history()
#         st.download_button(
#             label="Download Chat History",
#             data=pdf_buffer,
#             file_name="chat_history.pdf",
#             mime="application/pdf"
#         )

#     # Clear Chat Button
#     if st.button("Clear Chat"):
#         st.session_state.chat_history = []
#         st.session_state.messages = [{"role": "assistant", "content": "How can I help with medical info today?"}]
#         st.rerun()

# # Chat container with boxy UI
# st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# # Initialize session state
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
# if "messages" not in st.session_state:
#     st.session_state.messages = [{"role": "assistant", "content": "How can I help with medical info today?"}]

# # Display chat messages
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(f'<div class="{msg["role"]}-message">{msg["content"]}</div>', unsafe_allow_html=True)

# # Handle user input
# if prompt := st.chat_input("Ask a medical question"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)

#     # Get response
#     answer = model_api.get_response(prompt, st.session_state.chat_history)
#     st.session_state.chat_history.append((prompt, answer))
#     st.session_state.messages.append({"role": "assistant", "content": answer})

#     with st.chat_message("assistant"):
#         st.markdown(f'<div class="assistant-message">{answer}</div>', unsafe_allow_html=True)

# st.markdown('</div>', unsafe_allow_html=True)
# st.markdown('</div>', unsafe_allow_html=True)

# import streamlit as st
# from src.components.data_ingestion import DataIngestion
# from src.components.embedding import Embedding
# from src.components.model_api import ModelAPI
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet
# import io
# import re

# # Initialize Streamlit with sidebar always expanded
# st.set_page_config(
#     page_title="Medical Chatbot",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS with theme consistency fixes and subheading styling
# st.markdown(
#     """
#     <style>
#     /* Gradient background with pink, white, and cream */
#     .stApp {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important; /* Pink, white, cream */
#         color: #333333 !important;
#         margin: 0 !important;
#         padding: 0 !important;
#         overflow: hidden !important;
#     }
#     .main-content {
#         padding: 0 !important;
#         margin: 0 !important;
#         width: 100%;
#     }
#     /* Header styling */
#     h1 {
#         color: #f06292 !important; /* Muted pink */
#         text-align: center;
#         font-family: 'Arial', sans-serif;
#         text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
#         margin-bottom: 5px !important;
#     }
#     /* Ensure header color in both themes */
#     [data-theme="dark"] h1,
#     [data-theme="light"] h1 {
#         color: #f06292 !important;
#     }
#     /* Markdown text below title */
#     .stMarkdown p {
#         color: #5d4037 !important; /* Muted brown */
#         font-family: 'Arial', sans-serif;
#         text-align: center;
#         margin: 0 !important;
#         padding: 5px 0 !important;
#     }
#     /* Ensure Markdown text color in both themes */
#     [data-theme="dark"] .stMarkdown p,
#     [data-theme="light"] .stMarkdown p {
#         color: #5d4037 !important;
#     }
#     /* Sidebar styling for Symptom Checker with gradient */
#     .stSidebar {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important; /* Same gradient as app */
#         border-right: 2px solid #f48fb1; /* Soft pink border */
#         padding: 10px;
#     }
#     /* Ensure sidebar background in both themes */
#     [data-theme="dark"] .stSidebar,
#     [data-theme="light"] .stSidebar {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important;
#     }
#     .stSidebar h1 {
#         color: #f06292 !important; /* Muted pink */
#         font-size: 1.5em;
#         text-align: center;
#     }
#     /* Ensure sidebar heading color in both themes */
#     [data-theme="dark"] .stSidebar h1,
#     [data-theme="light"] .stSidebar h1 {
#         color: #f06292 !important;
#     }
#     /* Subheading styling for "Enter symptoms" */
#     h4 {
#         color: #f06292 !important; /* Muted pink to match Symptom Checker heading */
#         font-family: 'Arial', sans-serif;
#         font-size: 1.1em;
#         margin-bottom: 5px !important;
#     }
#     /* Ensure subheading color in both themes */
#     [data-theme="dark"] h4,
#     [data-theme="light"] h4 {
#         color: #f06292 !important;
#     }
#     /* Chat container styling */
#     .chat-container {
#         border: 2px solid #f48fb1; /* Soft pink border */
#         padding: 15px;
#         border-radius: 15px;
#         background-color: #ffffff !important; /* White for contrast */
#         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#         margin: 0 !important;
#         padding: 0 0 10px 0 !important;
#     }
#     /* Ensure chat container background in both themes */
#     [data-theme="dark"] .chat-container,
#     [data-theme="light"] .chat-container {
#         background-color: #ffffff !important;
#     }
#     /* Override Streamlit's default chat message styling to remove black bar */
#     [data-testid="stChatMessage"] {
#         background: transparent !important; /* Remove any default background */
#         border: none !important; /* Remove any default border */
#         box-shadow: none !important; /* Remove any default shadow */
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     /* Ensure no theme conflicts for chat messages */
#     [data-theme="dark"] [data-testid="stChatMessage"],
#     [data-theme="light"] [data-testid="stChatMessage"] {
#         background: transparent !important;
#         border: none !important;
#         box-shadow: none !important;
#     }
#     /* Chat message styling */
#     .user-message {
#         background-color: #f06292 !important; /* Pink for user */
#         padding: 12px;
#         border-radius: 15px;
#         margin: 5px 0 10px 0; /* Increased bottom margin to create gap */
#         max-width: 70%;
#         display: inline-block;
#         border: 1px solid #ec407a;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.05); /* Lighter shadow to avoid dark bar effect */
#         color: #ffffff !important; /* White text for contrast */
#     }
#     /* Ensure user message styles in both themes */
#     [data-theme="dark"] .user-message,
#     [data-theme="light"] .user-message {
#         background-color: #f06292 !important;
#         color: #ffffff !important;
#     }
#     .assistant-message {
#         background-color: #ffffff !important; /* White for chatbot */
#         padding: 12px;
#         border-radius: 15px;
#         margin: 5px 0;
#         max-width: 70%;
#         display: inline-block;
#         border: 1px solid #eeeeee;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
#         color: #5d4037 !important; /* Muted brown text */
#     }
#     /* Ensure assistant message styles in both themes */
#     [data-theme="dark"] .assistant-message,
#     [data-theme="light"] .assistant-message {
#         background-color: #ffffff !important;
#         color: #5d4037 !important;
#     }
#     /* Chat input styling with white background */
#     .stChatInput {
#         background: #ffffff !important; /* White background for the chat input container */
#         border: none;
#         padding: 5px !important;
#         margin: 0 !important;
#     }
#     /* Ensure chat input background in both themes */
#     [data-theme="dark"] .stChatInput,
#     [data-theme="light"] .stChatInput {
#         background: #ffffff !important;
#     }
#     .stChatInput input {
#         border: 2px solid #f48fb1;
#         border-radius: 8px;
#         font-family: 'Arial', sans-serif;
#         background-color: #ffffff !important; /* Ensure input field is white */
#         color: #333333 !important; /* Dark text for visibility */
#         padding: 5px;
#     }
#     /* Ensure chat input text color in both themes */
#     [data-theme="dark"] .stChatInput input,
#     [data-theme="light"] .stChatInput input {
#         background-color: #ffffff !important;
#         color: #333333 !important;
#     }
#     /* Button styling */
#     .stButton>button {
#         background-color: #f48fb1 !important; /* Soft pink */
#         color: white !important;
#         border-radius: 8px;
#         border: none;
#         padding: 8px 16px;
#         font-family: 'Arial', sans-serif;
#         transition: background-color 0.3s;
#     }
#     .stButton>button:hover {
#         background-color: #f06292 !important;
#     }
#     /* Ensure button styles in both themes */
#     [data-theme="dark"] .stButton>button,
#     [data-theme="light"] .stButton>button {
#         background-color: #f48fb1 !important;
#         color: white !important;
#     }
#     [data-theme="dark"] .stButton>button:hover,
#     [data-theme="light"] .stButton>button:hover {
#         background-color: #f06292 !important;
#     }
#     /* Text area styling */
#     .stTextArea textarea {
#         border: 2px solid #f48fb1; /* Soft pink border */
#         border-radius: 8px;
#         font-family: 'Arial', sans-serif;
#         background-color: #ffffff !important;
#         color: #333333 !important; /* Dark text for visibility */
#     }
#     /* Ensure text area styles in both themes */
#     [data-theme="dark"] .stTextArea textarea,
#     [data-theme="light"] .stTextArea textarea {
#         background-color: #ffffff !important;
#         color: #333333 !important;
#     }
#     /* Placeholder styling for text area */
#     .stTextArea textarea::placeholder {
#         color: #666666 !important; /* Medium-dark gray for placeholder */
#         font-family: 'Arial', sans-serif;
#         font-size: 14px; /* Slightly smaller */
#         opacity: 1; /* Ensure full visibility */
#     }
#     /* Ensure placeholder styles in both themes */
#     [data-theme="dark"] .stTextArea textarea::placeholder,
#     [data-theme="light"] .stTextArea textarea::placeholder {
#         color: #666666 !important;
#     }
#     /* Ensure Symptom Checker response text color in both themes */
#     [data-theme="dark"] .stSidebar .stMarkdown,
#     [data-theme="light"] .stSidebar .stMarkdown {
#         color: #5d4037 !important;
#     }
#     /* Remove extra spacing to eliminate empty bar */
#     .stApp, .stChatContainer, .stChatInputContainer, .stChatMessage, .stChatInput, .stMarkdown, .stSpinner, .stError {
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     div[data-testid="stVerticalBlock"], div[data-testid="stHorizontalBlock"] {
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     div[data-testid="stAppViewContainer"] {
#         padding: 0 !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Wrap content in custom container
# st.markdown('<div class="main-content">', unsafe_allow_html=True)

# # Header
# st.title("Medical Chatbot")
# st.markdown("Ask medical questions or check symptoms (not a doctor, just info).")

# # Load vector store
# embedding = Embedding(index_name="medical-index")
# vector_store = embedding.get_vector_store()

# # Initialize model
# model_api = ModelAPI(vector_store)

# # Sidebar (always expanded)
# with st.sidebar:
#     st.title("Symptom Checker")
#     st.markdown('<h4>Enter symptoms (e.g., fever, cough)</h4>', unsafe_allow_html=True)
#     symptoms = st.text_area("", placeholder="Type here...")
#     if st.button("Check Symptoms"):
#         if symptoms:
#             with st.spinner("Analyzing symptoms..."):
#                 response = model_api.check_symptoms(symptoms)
#                 st.markdown(f"**Analysis**: {response}")
#         else:
#             st.error("Please enter symptoms.")

#     # Chat History Export with Markdown Preprocessing
#     def export_chat_history():
#         buffer = io.BytesIO()
#         doc = SimpleDocTemplate(buffer, pagesize=letter)
#         styles = getSampleStyleSheet()
#         story = []

#         # Define styles for headings and normal text
#         heading_style = styles["Heading2"]  # Use Heading2 for ## headings
#         normal_style = styles["Normal"]

#         for msg in st.session_state.messages:
#             role = "User" if msg["role"] == "user" else "Assistant"
#             content = msg["content"]

#             # Preprocess Markdown for assistant messages
#             if role == "Assistant":
#                 # Replace Markdown headings (## Heading) with plain text for PDF
#                 content = re.sub(r'##\s*(.+)', r'\1', content)  # Remove ## and keep the heading text
#                 # Replace Markdown bold (**text**) with plain text (remove **)
#                 content = re.sub(r'\*\*(.+?)\*\*', r'\1', content)  # Remove ** and keep the text

#                 # Split content into lines to handle headings
#                 lines = content.split('\n')
#                 for line in lines:
#                     if line in ["Causes of Anemia", "Iron-Deficiency Anemia", "Sickle Cell Anemia"]:  # Example headings
#                         story.append(Paragraph(f"{role}: {line}", heading_style))
#                     else:
#                         story.append(Paragraph(f"{role}: {line}", normal_style))
#             else:
#                 # User messages can be added as-is
#                 story.append(Paragraph(f"{role}: {content}", normal_style))

#         doc.build(story)
#         buffer.seek(0)
#         return buffer

#     if st.button("Export Chat History as PDF"):
#         pdf_buffer = export_chat_history()
#         st.download_button(
#             label="Download Chat History",
#             data=pdf_buffer,
#             file_name="chat_history.pdf",
#             mime="application/pdf"
#         )

#     # Clear Chat Button
#     if st.button("Clear Chat"):
#         st.session_state.chat_history = []
#         st.session_state.messages = [{"role": "assistant", "content": "How can I help with medical info today?"}]
#         st.rerun()

# # Chat container with boxy UI
# st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# # Initialize session state
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
# if "messages" not in st.session_state:
#     st.session_state.messages = [{"role": "assistant", "content": "How can I help with medical info today?"}]

# # Display chat messages
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(f'<div class="{msg["role"]}-message">{msg["content"]}</div>', unsafe_allow_html=True)

# # Handle user input
# if prompt := st.chat_input("Ask a medical question"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)

#     # Get response
#     answer = model_api.get_response(prompt, st.session_state.chat_history)
#     st.session_state.chat_history.append((prompt, answer))
#     st.session_state.messages.append({"role": "assistant", "content": answer})

#     with st.chat_message("assistant"):
#         st.markdown(f'<div class="assistant-message">{answer}</div>', unsafe_allow_html=True)

# st.markdown('</div>', unsafe_allow_html=True)
# st.markdown('</div>', unsafe_allow_html=True)

# import streamlit as st
# from src.components.data_ingestion import DataIngestion
# from src.components.embedding import Embedding
# from src.components.model_api import ModelAPI
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet
# import io
# import re

# # Initialize Streamlit with sidebar always expanded
# st.set_page_config(
#     page_title="Medical Chatbot",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS with theme consistency fixes, subheading styling, and justified text
# st.markdown(
#     """
#     <style>
#     /* Gradient background with pink, white, and cream */
#     .stApp {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important; /* Pink, white, cream */
#         color: #333333 !important;
#         margin: 0 !important;
#         padding: 0 !important;
#         overflow: hidden !important;
#     }
#     .main-content {
#         padding: 0 !important;
#         margin: 0 !important;
#         width: 100%;
#     }
#     /* Header styling */
#     h1 {
#         color: #f06292 !important; /* Muted pink */
#         text-align: center;
#         font-family: 'Arial', sans-serif;
#         text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
#         margin-bottom: 5px !important;
#     }
#     /* Ensure header color in both themes */
#     [data-theme="dark"] h1,
#     [data-theme="light"] h1 {
#         color: #f06292 !important;
#     }
#     /* Markdown text below title */
#     .stMarkdown p {
#         color: #5d4037 !important; /* Muted brown */
#         font-family: 'Arial', sans-serif;
#         text-align: center;
#         margin: 0 !important;
#         padding: 5px 0 !important;
#     }
#     /* Ensure Markdown text color in both themes */
#     [data-theme="dark"] .stMarkdown p,
#     [data-theme="light"] .stMarkdown p {
#         color: #5d4037 !important;
#     }
#     /* Sidebar styling for Symptom Checker with gradient */
#     .stSidebar {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important; /* Same gradient as app */
#         border-right: 2px solid #f48fb1; /* Soft pink border */
#         padding: 10px;
#     }
#     /* Ensure sidebar background in both themes */
#     [data-theme="dark"] .stSidebar,
#     [data-theme="light"] .stSidebar {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important;
#     }
#     .stSidebar h1 {
#         color: #f06292 !important; /* Muted pink */
#         font-size: 1.5em;
#         text-align: center;
#     }
#     /* Ensure sidebar heading color in both themes */
#     [data-theme="dark"] .stSidebar h1,
#     [data-theme="light"] .stSidebar h1 {
#         color: #f06292 !important;
#     }
#     /* Subheading styling for "Enter symptoms" */
#     h4 {
#         color: #f06292 !important; /* Muted pink to match Symptom Checker heading */
#         font-family: 'Arial', sans-serif;
#         font-size: 1.1em;
#         margin-bottom: 5px !important;
#     }
#     /* Ensure subheading color in both themes */
#     [data-theme="dark"] h4,
#     [data-theme="light"] h4 {
#         color: #f06292 !important;
#     }
#     /* Chat container styling */
#     .chat-container {
#         border: 2px solid #f48fb1; /* Soft pink border */
#         padding: 15px;
#         border-radius: 15px;
#         background-color: #ffffff !important; /* White for contrast */
#         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#         margin: 0 !important;
#         padding: 0 0 10px 0 !important;
#     }
#     /* Ensure chat container background in both themes */
#     [data-theme="dark"] .chat-container,
#     [data-theme="light"] .chat-container {
#         background-color: #ffffff !important;
#     }
#     /* Override Streamlit's default chat message styling to remove black bar */
#     [data-testid="stChatMessage"] {
#         background: transparent !important; /* Remove any default background */
#         border: none !important; /* Remove any default border */
#         box-shadow: none !important; /* Remove any default shadow */
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     /* Ensure no theme conflicts for chat messages */
#     [data-theme="dark"] [data-testid="stChatMessage"],
#     [data-theme="light"] [data-testid="stChatMessage"] {
#         background: transparent !important;
#         border: none !important;
#         box-shadow: none !important;
#     }
#     /* Chat message styling with justified text */
#     .user-message {
#         background-color: #f06292 !important; /* Pink for user */
#         padding: 12px;
#         border-radius: 15px;
#         margin: 5px 0 10px 0; /* Increased bottom margin to create gap */
#         max-width: 70%;
#         display: inline-block;
#         border: 1px solid #ec407a;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.05); /* Lighter shadow to avoid dark bar effect */
#         color: #ffffff !important; /* White text for contrast */
#         text-align: justify !important; /* Justified text */
#     }
#     .assistant-message {
#         background-color: #ffffff !important; /* White for chatbot */
#         padding: 12px;
#         border-radius: 15px;
#         margin: 5px 0;
#         max-width: 70%;
#         display: inline-block;
#         border: 1px solid #eeeeee;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
#         color: #5d4037 !important; /* Muted brown text */
#         text-align: justify !important; /* Justified text */
#     }
#     /* Ensure message styles in both themes */
#     [data-theme="dark"] .user-message,
#     [data-theme="light"] .user-message {
#         background-color: #f06292 !important;
#         color: #ffffff !important;
#         text-align: justify !important;
#     }
#     [data-theme="dark"] .assistant-message,
#     [data-theme="light"] .assistant-message {
#         background-color: #ffffff !important;
#         color: #5d4037 !important;
#         text-align: justify !important;
#     }
#     /* Chat input styling with white background */
#     .stChatInput {
#         background: #ffffff !important; /* White background for the chat input container */
#         border: none;
#         padding: 5px !important;
#         margin: 0 !important;
#     }
#     /* Ensure chat input background in both themes */
#     [data-theme="dark"] .stChatInput,
#     [data-theme="light"] .stChatInput {
#         background: #ffffff !important;
#     }
#     .stChatInput input {
#         border: 2px solid #f48fb1;
#         border-radius: 8px;
#         font-family: 'Arial', sans-serif;
#         background-color: #ffffff !important; /* Ensure input field is white */
#         color: #333333 !important; /* Dark text for visibility */
#         padding: 5px;
#     }
#     /* Ensure chat input text color in both themes */
#     [data-theme="dark"] .stChatInput input,
#     [data-theme="light"] .stChatInput input {
#         background-color: #ffffff !important;
#         color: #333333 !important;
#     }
#     /* Button styling */
#     .stButton>button {
#         background-color: #f48fb1 !important; /* Soft pink */
#         color: white !important;
#         border-radius: 8px;
#         border: none;
#         padding: 8px 16px;
#         font-family: 'Arial', sans-serif;
#         transition: background-color 0.3s;
#     }
#     .stButton>button:hover {
#         background-color: #f06292 !important;
#     }
#     /* Ensure button styles in both themes */
#     [data-theme="dark"] .stButton>button,
#     [data-theme="light"] .stButton>button {
#         background-color: #f48fb1 !important;
#         color: white !important;
#     }
#     [data-theme="dark"] .stButton>button:hover,
#     [data-theme="light"] .stButton>button:hover {
#         background-color: #f06292 !important;
#     }
#     /* Text area styling */
#     .stTextArea textarea {
#         border: 2px solid #f48fb1; /* Soft pink border */
#         border-radius: 8px;
#         font-family: 'Arial', sans-serif;
#         background-color: #ffffff !important;
#         color: #333333 !important; /* Dark text for visibility */
#     }
#     /* Ensure text area styles in both themes */
#     [data-theme="dark"] .stTextArea textarea,
#     [data-theme="light"] .stTextArea textarea {
#         background-color: #ffffff !important;
#         color: #333333 !important;
#     }
#     /* Placeholder styling for text area */
#     .stTextArea textarea::placeholder {
#         color: #666666 !important; /* Medium-dark gray for placeholder */
#         font-family: 'Arial', sans-serif;
#         font-size: 14px; /* Slightly smaller */
#         opacity: 1; /* Ensure full visibility */
#     }
#     /* Ensure placeholder styles in both themes */
#     [data-theme="dark"] .stTextArea textarea::placeholder,
#     [data-theme="light"] .stTextArea textarea::placeholder {
#         color: #666666 !important;
#     }
#     /* Symptom Checker response text color and justified text */
#     [data-theme="dark"] .stSidebar .stMarkdown,
#     [data-theme="light"] .stSidebar .stMarkdown {
#         color: #5d4037 !important;
#         text-align: justify !important;
#     }
#     /* Remove extra spacing to eliminate empty bar */
#     .stApp, .stChatContainer, .stChatInputContainer, .stChatMessage, .stChatInput, .stMarkdown, .stSpinner, .stError {
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     div[data-testid="stVerticalBlock"], div[data-testid="stHorizontalBlock"] {
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     div[data-testid="stAppViewContainer"] {
#         padding: 0 !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Wrap content in custom container
# st.markdown('<div class="main-content">', unsafe_allow_html=True)

# # Header
# st.title("Medical Chatbot")
# st.markdown("Ask medical questions or check symptoms (not a doctor, just info).")

# # Load vector store
# embedding = Embedding(index_name="medical-index")
# vector_store = embedding.get_vector_store()

# # Initialize model
# model_api = ModelAPI(vector_store)

# # Sidebar (always expanded)
# with st.sidebar:
#     st.title("Symptom Checker")
#     st.markdown('<h4>Enter symptoms (e.g., fever, cough)</h4>', unsafe_allow_html=True)
#     symptoms = st.text_area("", placeholder="Type here...")
#     if st.button("Check Symptoms"):
#         if symptoms:
#             with st.spinner("Analyzing symptoms..."):
#                 response = model_api.check_symptoms(symptoms)
#                 # Ensure the first heading is bolded for consistency
#                 response = response.replace("**Possible Conditions**", "**Possible Conditions**")
#                 # Wrap response in justified div
#                 st.markdown(f'<div style="text-align: justify"><b>Analysis</b>: {response}</div>', unsafe_allow_html=True)
#         else:
#             st.error("Please enter symptoms.")

#     # Chat History Export with Markdown Preprocessing
#     def export_chat_history():
#         buffer = io.BytesIO()
#         doc = SimpleDocTemplate(buffer, pagesize=letter)
#         styles = getSampleStyleSheet()
#         story = []

#         # Define styles for headings and normal text
#         heading_style = styles["Heading2"]  # Use Heading2 for ## headings
#         normal_style = styles["Normal"]

#         for msg in st.session_state.messages:
#             role = "User" if msg["role"] == "user" else "Assistant"
#             content = msg["content"]

#             # Preprocess Markdown for assistant messages
#             if role == "Assistant":
#                 # Replace Markdown headings (## Heading) with plain text for PDF
#                 content = re.sub(r'##\s*(.+)', r'\1', content)  # Remove ## and keep the heading text
#                 # Replace Markdown bold (**text**) with plain text (remove **)
#                 content = re.sub(r'\*\*(.+?)\*\*', r'\1', content)  # Remove ** and keep the text

#                 # Split content into lines to handle headings
#                 lines = content.split('\n')
#                 for line in lines:
#                     if line in ["Causes of Anemia", "Iron-Deficiency Anemia", "Sickle Cell Anemia"]:  # Example headings
#                         story.append(Paragraph(f"{role}: {line}", heading_style))
#                     else:
#                         story.append(Paragraph(f"{role}: {line}", normal_style))
#             else:
#                 # User messages can be added as-is
#                 story.append(Paragraph(f"{role}: {content}", normal_style))

#         doc.build(story)
#         buffer.seek(0)
#         return buffer

#     if st.button("Export Chat History as PDF"):
#         pdf_buffer = export_chat_history()
#         st.download_button(
#             label="Download Chat History",
#             data=pdf_buffer,
#             file_name="chat_history.pdf",
#             mime="application/pdf"
#         )

#     # Clear Chat Button
#     if st.button("Clear Chat"):
#         st.session_state.chat_history = []
#         st.session_state.messages = [{"role": "assistant", "content": "How can I help with medical info today?"}]
#         st.rerun()

# # Chat container with boxy UI
# st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# # Initialize session state
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
# if "messages" not in st.session_state:
#     st.session_state.messages = [{"role": "assistant", "content": "How can I help with medical info today?"}]

# # Display chat messages
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(f'<div style="text-align: justify" class="{msg["role"]}-message">{msg["content"]}</div>', unsafe_allow_html=True)

# # Handle user input
# if prompt := st.chat_input("Ask a medical question"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(f'<div style="text-align: justify" class="user-message">{prompt}</div>', unsafe_allow_html=True)

#     # Get response
#     answer = model_api.get_response(prompt, st.session_state.chat_history)
#     st.session_state.chat_history.append((prompt, answer))
#     st.session_state.messages.append({"role": "assistant", "content": answer})

#     with st.chat_message("assistant"):
#         st.markdown(f'<div style="text-align: justify" class="assistant-message">{answer}</div>', unsafe_allow_html=True)

# st.markdown('</div>', unsafe_allow_html=True)
# st.markdown('</div>', unsafe_allow_html=True)

# import streamlit as st
# from src.components.data_ingestion import DataIngestion
# from src.components.embedding import Embedding
# from src.components.model_api import ModelAPI
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet
# import io
# import re

# # Initialize Streamlit with sidebar always expanded
# st.set_page_config(
#     page_title="Medical Chatbot",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS with theme consistency fixes, subheading styling, and justified text
# st.markdown(
#     """
#     <style>
#     /* Gradient background with pink, white, and cream */
#     .stApp {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important; /* Pink, white, cream */
#         color: #333333 !important;
#         margin: 0 !important;
#         padding: 0 !important;
#         overflow: hidden !important;
#     }
#     .main-content {
#         padding: 0 !important;
#         margin: 0 !important;
#         width: 100%;
#     }
#     /* Header styling */
#     h1 {
#         color: #f06292 !important; /* Muted pink */
#         text-align: center;
#         font-family: 'Arial', sans-serif;
#         text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
#         margin-bottom: 5px !important;
#     }
#     /* Ensure header color in both themes */
#     [data-theme="dark"] h1,
#     [data-theme="light"] h1 {
#         color: #f06292 !important;
#     }
#     /* Markdown text below title */
#     .stMarkdown p {
#         color: #5d4037 !important; /* Muted brown */
#         font-family: 'Arial', sans-serif;
#         text-align: center;
#         margin: 0 !important;
#         padding: 5px 0 !important;
#     }
#     /* Ensure Markdown text color in both themes */
#     [data-theme="dark"] .stMarkdown p,
#     [data-theme="light"] .stMarkdown p {
#         color: #5d4037 !important;
#     }
#     /* Sidebar styling for Symptom Checker with gradient */
#     .stSidebar {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important; /* Same gradient as app */
#         border-right: 2px solid #f48fb1; /* Soft pink border */
#         padding: 10px;
#     }
#     /* Ensure sidebar background in both themes */
#     [data-theme="dark"] .stSidebar,
#     [data-theme="light"] .stSidebar {
#         background: linear-gradient(135deg, #fce4ec 30%, #ffffff 60%, #fffde7 100%) !important;
#     }
#     .stSidebar h1 {
#         color: #f06292 !important; /* Muted pink */
#         font-size: 1.5em;
#         text-align: center;
#     }
#     /* Ensure sidebar heading color in both themes */
#     [data-theme="dark"] .stSidebar h1,
#     [data-theme="light"] .stSidebar h1 {
#         color: #f06292 !important;
#     }
#     /* Subheading styling for "Enter symptoms" */
#     h4 {
#         color: #f06292 !important; /* Muted pink to match Symptom Checker heading */
#         font-family: 'Arial', sans-serif;
#         font-size: 1.1em;
#         margin-bottom: 5px !important;
#     }
#     /* Ensure subheading color in both themes */
#     [data-theme="dark"] h4,
#     [data-theme="light"] h4 {
#         color: #f06292 !important;
#     }
#     /* Chat container styling */
#     .chat-container {
#         border: 2px solid #f48fb1; /* Soft pink border */
#         padding: 15px;
#         border-radius: 15px;
#         background-color: #ffffff !important; /* White for contrast */
#         box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#         margin: 0 !important;
#         padding: 0 0 10px 0 !important;
#     }
#     /* Ensure chat container background in both themes */
#     [data-theme="dark"] .chat-container,
#     [data-theme="light"] .chat-container {
#         background-color: #ffffff !important;
#     }
#     /* Override Streamlit's default chat message styling to remove black bar */
#     [data-testid="stChatMessage"] {
#         background: transparent !important; /* Remove any default background */
#         border: none !important; /* Remove any default border */
#         box-shadow: none !important; /* Remove any default shadow */
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     /* Ensure no theme conflicts for chat messages */
#     [data-theme="dark"] [data-testid="stChatMessage"],
#     [data-theme="light"] [data-testid="stChatMessage"] {
#         background: transparent !important;
#         border: none !important;
#         box-shadow: none !important;
#     }
#     /* Chat message styling with justified text */
#     .user-message {
#         background-color: #f06292 !important; /* Pink for user */
#         padding: 12px;
#         border-radius: 15px;
#         margin: 5px 0 10px 0; /* Increased bottom margin to create gap */
#         max-width: 70%;
#         display: inline-block;
#         border: 1px solid #ec407a;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.05); /* Lighter shadow to avoid dark bar effect */
#         color: #ffffff !important; /* White text for contrast */
#         text-align: justify !important; /* Justified text */
#     }
#     .assistant-message {
#         background-color: #ffffff !important; /* White for chatbot */
#         padding: 12px;
#         border-radius: 15px;
#         margin: 5px 0;
#         max-width: 70%;
#         display: inline-block;
#         border: 1px solid #eeeeee;
#         box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
#         color: #5d4037 !important; /* Muted brown text */
#         text-align: justify !important; /* Justified text */
#     }
#     /* Ensure message styles in both themes */
#     [data-theme="dark"] .user-message,
#     [data-theme="light"] .user-message {
#         background-color: #f06292 !important;
#         color: #ffffff !important;
#         text-align: justify !important;
#     }
#     [data-theme="dark"] .assistant-message,
#     [data-theme="light"] .assistant-message {
#         background-color: #ffffff !important;
#         color: #5d4037 !important;
#         text-align: justify !important;
#     }
#     /* Chat input styling with white background */
#     .stChatInput {
#         background: #ffffff !important; /* White background for the chat input container */
#         border: none;
#         padding: 5px !important;
#         margin: 0 !important;
#     }
#     /* Ensure chat input background in both themes */
#     [data-theme="dark"] .stChatInput,
#     [data-theme="light"] .stChatInput {
#         background: #ffffff !important;
#     }
#     .stChatInput input {
#         border: 2px solid #f48fb1;
#         border-radius: 8px;
#         font-family: 'Arial', sans-serif;
#         background-color: #ffffff !important; /* Ensure input field is white */
#         color: #333333 !important; /* Dark text for visibility */
#         padding: 5px;
#     }
#     /* Ensure chat input text color in both themes */
#     [data-theme="dark"] .stChatInput input,
#     [data-theme="light"] .stChatInput input {
#         background-color: #ffffff !important;
#         color: #333333 !important;
#     }
#     /* Button styling */
#     .stButton>button {
#         background-color: #f48fb1 !important; /* Soft pink */
#         color: white !important;
#         border-radius: 8px;
#         border: none;
#         padding: 8px 16px;
#         font-family: 'Arial', sans-serif;
#         transition: background-color 0.3s;
#     }
#     .stButton>button:hover {
#         background-color: #f06292 !important;
#     }
#     /* Ensure button styles in both themes */
#     [data-theme="dark"] .stButton>button,
#     [data-theme="light"] .stButton>button {
#         background-color: #f48fb1 !important;
#         color: white !important;
#     }
#     [data-theme="dark"] .stButton>button:hover,
#     [data-theme="light"] .stButton>button:hover {
#         background-color: #f06292 !important;
#     }
#     /* Text area styling */
#     .stTextArea textarea {
#         border: 2px solid #f48fb1; /* Soft pink border */
#         border-radius: 8px;
#         font-family: 'Arial', sans-serif;
#         background-color: #ffffff !important;
#         color: #333333 !important; /* Dark text for visibility */
#     }
#     /* Ensure text area styles in both themes */
#     [data-theme="dark"] .stTextArea textarea,
#     [data-theme="light"] .stTextArea textarea {
#         background-color: #ffffff !important;
#         color: #333333 !important;
#     }
#     /* Placeholder styling for text area */
#     .stTextArea textarea::placeholder {
#         color: #666666 !important; /* Medium-dark gray for placeholder */
#         font-family: 'Arial', sans-serif;
#         font-size: 14px; /* Slightly smaller */
#         opacity: 1; /* Ensure full visibility */
#     }
#     /* Ensure placeholder styles in both themes */
#     [data-theme="dark"] .stTextArea textarea::placeholder,
#     [data-theme="light"] .stTextArea textarea::placeholder {
#         color: #666666 !important;
#     }
#     /* Symptom Checker response text color and justified text */
#     [data-theme="dark"] .stSidebar .stMarkdown,
#     [data-theme="light"] .stSidebar .stMarkdown {
#         color: #5d4037 !important;
#         text-align: justify !important;
#     }
#     /* Remove extra spacing to eliminate empty bar */
#     .stApp, .stChatContainer, .stChatInputContainer, .stChatMessage, .stChatInput, .stMarkdown, .stSpinner, .stError {
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     div[data-testid="stVerticalBlock"], div[data-testid="stHorizontalBlock"] {
#         margin: 0 !important;
#         padding: 0 !important;
#     }
#     div[data-testid="stAppViewContainer"] {
#         padding: 0 !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Wrap content in custom container
# st.markdown('<div class="main-content">', unsafe_allow_html=True)

# # Header
# st.title("Medical Chatbot")
# st.markdown("Ask medical questions or check symptoms (not a doctor, just info).")

# # Load vector store
# embedding = Embedding(index_name="medical-index")
# vector_store = embedding.get_vector_store()

# # Initialize model
# model_api = ModelAPI(vector_store)

# # Sidebar (always expanded)
# with st.sidebar:
#     st.title("Symptom Checker")
#     st.markdown('<h4>Enter symptoms (e.g., fever, cough)</h4>', unsafe_allow_html=True)
#     # Initialize symptoms_input in session_state if not present
#     if "symptoms_input" not in st.session_state:
#         st.session_state.symptoms_input = ""
#     # Bind text_area to session_state.symptoms_input
#     st.session_state.symptoms_input = st.text_area("", value=st.session_state.symptoms_input, placeholder="Type here...")
#     if st.button("Check Symptoms"):
#         if st.session_state.symptoms_input:
#             with st.spinner("Analyzing symptoms..."):
#                 response = model_api.check_symptoms(st.session_state.symptoms_input)
#                 # Ensure the first heading is bolded for consistency
#                 response = response.replace("**Possible Conditions**", "**Possible Conditions**")
#                 # Wrap response in justified div
#                 st.markdown(f'<div style="text-align: justify"><b>Analysis</b>: {response}</div>', unsafe_allow_html=True)
#         else:
#             st.error("Please enter symptoms.")

#     # Chat History Export with Markdown Preprocessing
#     def export_chat_history():
#         buffer = io.BytesIO()
#         doc = SimpleDocTemplate(buffer, pagesize=letter)
#         styles = getSampleStyleSheet()
#         story = []

#         # Define styles for headings and normal text
#         heading_style = styles["Heading2"]  # Use Heading2 for ## headings
#         normal_style = styles["Normal"]

#         for msg in st.session_state.messages:
#             role = "User" if msg["role"] == "user" else "Assistant"
#             content = msg["content"]

#             # Preprocess Markdown for assistant messages
#             if role == "Assistant":
#                 # Replace Markdown headings (## Heading) with plain text for PDF
#                 content = re.sub(r'##\s*(.+)', r'\1', content)  # Remove ## and keep the heading text
#                 # Replace Markdown bold (**text**) with plain text (remove **)
#                 content = re.sub(r'\*\*(.+?)\*\*', r'\1', content)  # Remove ** and keep the text

#                 # Split content into lines to handle headings
#                 lines = content.split('\n')
#                 for line in lines:
#                     if line in ["Causes of Anemia", "Iron-Deficiency Anemia", "Sickle Cell Anemia"]:  # Example headings
#                         story.append(Paragraph(f"{role}: {line}", heading_style))
#                     else:
#                         story.append(Paragraph(f"{role}: {line}", normal_style))
#             else:
#                 # User messages can be added as-is
#                 story.append(Paragraph(f"{role}: {content}", normal_style))

#         doc.build(story)
#         buffer.seek(0)
#         return buffer

#     if st.button("Export Chat History as PDF"):
#         pdf_buffer = export_chat_history()
#         st.download_button(
#             label="Download Chat History",
#             data=pdf_buffer,
#             file_name="chat_history.pdf",
#             mime="application/pdf"
#         )

#     # Clear Chat Button
#     if st.button("Clear Chat"):
#         st.session_state.chat_history = []
#         st.session_state.messages = [{"role": "assistant", "content": "How can I help with medical info today?"}]
#         st.session_state.symptoms_input = ""  # Clear Symptom Checker input
#         st.rerun()

# # Chat container with boxy UI
# st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# # Initialize session state
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
# if "messages" not in st.session_state:
#     st.session_state.messages = [{"role": "assistant", "content": "How can I help with medical info today?"}]

# # Display chat messages
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(f'<div style="text-align: justify" class="{msg["role"]}-message">{msg["content"]}</div>', unsafe_allow_html=True)

# # Handle user input
# if prompt := st.chat_input("Ask a medical question"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(f'<div style="text-align: justify" class="user-message">{prompt}</div>', unsafe_allow_html=True)

#     # Get response
#     answer = model_api.get_response(prompt, st.session_state.chat_history)
#     st.session_state.chat_history.append((prompt, answer))
#     st.session_state.messages.append({"role": "assistant", "content": answer})

#     with st.chat_message("assistant"):
#         st.markdown(f'<div style="text-align: justify" class="assistant-message">{answer}</div>', unsafe_allow_html=True)

# st.markdown('</div>', unsafe_allow_html=True)
# st.markdown('</div>', unsafe_allow_html=True)

from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv
import os
import logging

# Setup logging for Streamlit Cloud
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ModelAPI:
    def __init__(self, vector_store):
        load_dotenv()
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            logger.error("OPENROUTER_API_KEY is not set in .env file")
            raise ValueError("Missing OPENROUTER_API_KEY. Please set it in the .env file.")
        
        self.llm = ChatOpenAI(
            model="deepseek/deepseek-chat:free",
            openai_api_key=api_key,
            openai_api_base="https://openrouter.ai/api/v1"
        )
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=vector_store.as_retriever(),
            return_source_documents=True
        )
        # Cache for responses to reduce API calls
        self.response_cache = {}

    def is_greeting(self, question):
        question_lower = question.lower().strip()
        greeting_responses = {
            "good morning": "Good morning! How can I assist with your medical questions today?",
            "good afternoon": "Good afternoon! Ready to help with any health concerns you have.",
            "good evening": "Good evening! Here to answer your medical questions before you wind down.",
            "good night": "Good night! Feel free to ask any medical questions before you rest.",
            "thank you": "You're welcome! Happy to help with any more health questions.",
            "thanks": "You're welcome! Let me know if you have more medical queries."
        }
        for greeting, response in greeting_responses.items():
            if greeting in question_lower:
                return response
        generic_greetings = ["hello", "hi", "hey"]
        words = question_lower.split()
        if any(word in generic_greetings for word in words):
            return "Hello! I'm your medical assistant. How can I help you with your health questions today?"
        return None

    def check_repetitive_question(self, question, chat_history):
        question_lower = question.lower().strip()
        if "blood pressure" in question_lower and ("cause" in question_lower or "what causes" in question_lower):
            for prev_question, prev_answer in chat_history:
                prev_question_lower = prev_question.lower().strip()
                if "blood pressure" in prev_question_lower and (
                        "cause" in prev_question_lower or "what causes" in prev_question_lower):
                    return (
                        "## Recap of High Blood Pressure Causes\n"
                        "• Lifestyle factors like high salt intake, obesity, and smoking.\n"
                        "• Medical conditions such as kidney disease or diabetes.\n"
                        "• Genetic predisposition, stress, and aging.\n\n"
                        "## Additional Information\n"
                        "• Blood pressure screenings are recommended annually.\n"
                        "• Medications like ACE inhibitors can manage hypertension.\n"
                        "Would you like to know more about managing high blood pressure, or do you have a different question?"
                    )
        return None

    def get_response(self, question, chat_history):
        # Check for greetings first
        greeting_response = self.is_greeting(question)
        if greeting_response:
            return greeting_response

        # Normalize question for cache and fallback lookup
        question_lower = question.lower().strip()

        # Check for repetitive questions
        repetitive_response = self.check_repetitive_question(question, chat_history)
        if repetitive_response:
            return repetitive_response

        # Check cache for previous response
        if question_lower in self.response_cache:
            return self.response_cache[question_lower]

        # Add context from recent chat history
        context = ""
        if chat_history:
            last_question, last_answer = chat_history[-1]
            if "stress" in last_question.lower() and "manage" in question_lower:
                context = f"Previous question: {last_question}\nPrevious answer: {last_answer}\n"

        modified_question = (
            f"""You are a medical assistant. Answer in English only with proper formatting or alignment of the response to the user."

Question: {question}

Answer:"""
        )
        try:
            result = self.qa_chain({"question": modified_question, "chat_history": chat_history})
            answer = result["answer"]

            # Check if the vector store lacks information
            if "provided context does not contain information" in answer.lower() or "not found in the context" in answer.lower():
                return (
                    "## Information Not Available\n"
                    "• The medical database does not contain details about this topic.\n"
                    "• This question appears outside the scope of available information.\n"
                    "• Consult a reliable medical source or healthcare professional for accurate information.\n\n"
                    "## Additional Information\n"
                    "• Online medical resources like WebMD can provide general guidance.\n"
                    "• Local clinics offer consultations for personalized advice.\n"
                    "Would you like to ask about something else?"
                )

            # Cache the response
            self.response_cache[question_lower] = answer
            return answer
        except ValueError as e:
            logger.error(f"API error in get_response: {str(e)}")
            error_str = str(e).lower()
            if "no instances available" in error_str or "503" in error_str:
                return (
                    "## Model Unavailable\n"
                    "• The medical database is temporarily unavailable due to high demand.\n"
                    "• Try again later or with a different question.\n"
                    "• Consult a healthcare professional for urgent needs.\n\n"
                    "## Additional Information\n"
                    "• Free models may have limited availability.\n"
                    "• Check OpenRouter.ai for model status.\n"
                )
            raise e

    def check_symptoms(self, symptoms):
        if not symptoms.strip() or symptoms.lower() in ["i don't feel well", "not feeling well"]:
            return (
                "**Symptom Information Needed**\n"
                "• Specific symptoms are needed to provide a better analysis.\n"
                "• Examples include fever, pain, or fatigue.\n"
                "• Consult a doctor for a thorough evaluation.\n\n"
                "## Additional Information\n"
                "• Keeping a symptom diary can help doctors diagnose issues.\n"
                "• Urgent symptoms like chest pain require immediate attention.\n"
            )
        query = (
            f"""You are a medical assistant. Answer in English only carefully analyse the symptoms of the user and provide the infromation according to that with proper formatting and at the end according severity of the symptoms advice them to consult a doctor.
Symptoms: {symptoms}

Answer:"""
        )
        try:
            result = self.qa_chain({"question": query, "chat_history": []})
            answer = result["answer"]
            return answer
        except ValueError as e:
            logger.error(f"API error in check_symptoms: {str(e)}")
            error_str = str(e).lower()
            if "no instances available" in error_str or "503" in error_str:
                return (
                    "**Model Unavailable**\n"
                    "• The medical database is temporarily unavailable due to high demand.\n"
                    "• Try again later or with different symptoms.\n"
                    "• Consult a healthcare professional for urgent needs.\n\n"
                    "## Additional Information\n"
                    "• Free models may have limited availability.\n"
                    "• Check OpenRouter.ai for model status.\n"
                )
            raise e
