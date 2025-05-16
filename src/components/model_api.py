# from langchain_openai import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from dotenv import load_dotenv
# import os

# class ModelAPI:
#     def __init__(self, vector_store):
#         load_dotenv()
#         self.llm = ChatOpenAI(
#             model="deepseek/deepseek-chat:free",
#             openai_api_key=os.getenv("OPENROUTER_API_KEY"),
#             openai_api_base="https://openrouter.ai/api/v1"
#         )
#         self.qa_chain = ConversationalRetrievalChain.from_llm(
#             llm=self.llm,
#             retriever=vector_store.as_retriever(),
#             return_source_documents=True
#         )

#     def get_response(self, question, chat_history):
#         result = self.qa_chain({"question": question, "chat_history": chat_history})
#         return result["answer"]

#     def check_symptoms(self, symptoms):
#         query = f"I have the following symptoms: {symptoms}. What might this indicate based on medical guidelines? Please provide general information and recommend consulting a doctor."
#         result = self.qa_chain({"question": query, "chat_history": []})
#         return result["answer"]

#Final
# from langchain_openai import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from dotenv import load_dotenv
# import os
# import re


# class ModelAPI:
#     def __init__(self, vector_store):
#         load_dotenv()
#         self.llm = ChatOpenAI(
#             model="deepseek/deepseek-chat:free",
#             openai_api_key=os.getenv("OPENROUTER_API_KEY"),
#             openai_api_base="https://openrouter.ai/api/v1"
#         )
#         self.qa_chain = ConversationalRetrievalChain.from_llm(
#             llm=self.llm,
#             retriever=vector_store.as_retriever(),
#             return_source_documents=True
#         )
#         # Cache for responses to reduce API calls
#         self.response_cache = {}
#         # Fallback responses for common questions when API limit is reached
#         self.fallback_responses = {
#             "what are the symptoms of the flu?": (
#                 "The symptoms of the flu (influenza) typically include:\n"
#                 "- Fever (often high, 100°F to 104°F or higher)\n"
#                 "- Chills and sweats\n"
#                 "- Cough (usually dry)\n"
#                 "- Sore throat\n"
#                 "- Muscle aches or body aches\n"
#                 "- Headache\n"
#                 "- Fatigue or weakness\n"
#                 "- Runny or stuffy nose\n"
#                 "- Nausea, vomiting, or diarrhea (more common in children)\n\n"
#                 "Symptoms often come on suddenly and can range from mild to severe. If you suspect you have the flu, especially if you are at high risk for complications (e.g., young children, elderly, or those with chronic conditions), it’s important to consult a healthcare provider."
#             ),
#             "what causes high blood pressure?": (
#                 "High blood pressure (hypertension) can be caused by a variety of factors, including:\n"
#                 "- Lifestyle factors: Poor diet (high salt intake), obesity, lack of physical activity, excessive alcohol consumption, and smoking.\n"
#                 "- Underlying medical conditions: Conditions such as diabetes, kidney disease, and hormonal disorders.\n"
#                 "- Genetic predisposition: A family history of hypertension increases your risk.\n"
#                 "- Stress: Chronic stress can contribute to elevated blood pressure.\n"
#                 "- Aging: Blood pressure often increases with age.\n\n"
#                 "Treatment often involves lifestyle changes (like a healthier diet and exercise) and medications if needed. Would you like to know more about managing high blood pressure?"
#             ),
#             "what is anemia?": (
#                 "## What is Anemia?\n"
#                 "Anemia is a condition where you have abnormally low levels of healthy red blood cells or hemoglobin, which carries oxygen to your body’s tissues. This can lead to symptoms like:\n"
#                 "- Fatigue or weakness\n"
#                 "- Shortness of breath\n"
#                 "- Pale skin\n"
#                 "- Dizziness or lightheadedness\n\n"
#                 "## Types of Anemia\n"
#                 "- Iron-deficiency anemia: Caused by a lack of iron, often due to poor diet or blood loss.\n"
#                 "- Vitamin B12 deficiency anemia: Due to insufficient B12, often linked to diet or absorption issues.\n"
#                 "- Sickle cell anemia: A genetic condition where red blood cells are abnormally shaped.\n\n"
#                 "If you suspect anemia, a doctor can diagnose it with a blood test and recommend treatment, such as iron supplements or dietary changes."
#             ),
#             "what are symptoms of heart attack?": (
#                 "## Symptoms of a Heart Attack\n"
#                 "Common signs of a heart attack include:\n"
#                 "- Chest pain or discomfort: Often described as pressure, squeezing, or pain in the center or left side of the chest. It may last for minutes or come and go.\n"
#                 "- Upper body discomfort: Pain in one or both arms, the jaw, neck, back, or stomach.\n"
#                 "- Shortness of breath: This can occur with or without chest pain.\n"
#                 "- Cold sweat, nausea, or lightheadedness: These symptoms may accompany chest discomfort.\n\n"
#                 "If you experience these symptoms, especially chest pain or shortness of breath, seek emergency medical attention immediately."
#             ),
#             "what causes kidney stones?": (
#                 "## Causes of Kidney Stones\n"
#                 "Kidney stones form due to a combination of factors, including:\n"
#                 "- Dehydration: Not drinking enough water leads to concentrated urine, increasing stone formation risk.\n"
#                 "- Diet: High intake of sodium, oxalate (found in foods like spinach), or animal protein.\n"
#                 "- Medical conditions: Conditions like hyperparathyroidism, gout, or urinary tract infections (UTIs).\n"
#                 "- Family history: A genetic predisposition to kidney stones.\n"
#                 "- Obesity: Higher body weight increases the risk.\n"
#                 "- Certain medications: Some diuretics or calcium-based antacids can contribute.\n\n"
#                 "Kidney stones can be made of different materials, like calcium oxalate or uric acid, depending on the cause."
#             ),
#             "how can i prevent them?": (
#                 "## Preventing Kidney Stones\n"
#                 "To prevent kidney stones, you can:\n"
#                 "- Stay hydrated: Drink plenty of water (aim for 2-3 liters daily) to dilute your urine.\n"
#                 "- Adjust your diet: Reduce sodium, oxalate-rich foods (like spinach), and animal protein. Eat more citrus fruits, which contain citrate that helps prevent stones.\n"
#                 "- Maintain a healthy weight: Obesity increases the risk, so regular exercise and a balanced diet can help.\n"
#                 "- Monitor medical conditions: Manage conditions like gout or UTIs that can contribute to stones.\n"
#                 "- Talk to your doctor: If you have a history of kidney stones, they may recommend specific dietary changes or medications."
#             )
#         }

#     def is_greeting(self, question):
#         greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
#         question_lower = question.lower().strip()
#         words = question_lower.split()
#         return any(word in greetings for word in words)

#     def check_repetitive_question(self, question, chat_history):
#         """Check if the question is similar to a previous one in chat history."""
#         question_lower = question.lower().strip()
#         if "blood pressure" in question_lower and ("cause" in question_lower or "what causes" in question_lower):
#             for prev_question, prev_answer in chat_history:
#                 prev_question_lower = prev_question.lower().strip()
#                 if "blood pressure" in prev_question_lower and (
#                         "cause" in prev_question_lower or "what causes" in prev_question_lower):
#                     return (
#                         f"I previously explained the causes of high blood pressure. To recap briefly: it can be due to lifestyle factors (like high salt intake, obesity, and smoking), medical conditions (like kidney disease or diabetes), genetics, stress, and aging. "
#                         "Would you like to know more about managing high blood pressure, or do you have a different question?"
#                     )
#         return None

#     def enforce_heading_format(self, response):
#         """Post-process the response to ensure section titles use ## for headings."""
#         # Common section title patterns (e.g., "Symptoms:", "Risk Factors:", "1. Causes:")
#         section_patterns = [
#             r'(\d+\.\s*(?:Symptoms|Risk Factors|Causes|Treatments|Prevention|Possible Conditions|Types of [A-Za-z\s]+):)',
#             r'(-?\s*(?:Symptoms|Risk Factors|Causes|Treatments|Prevention|Possible Conditions|Types of [A-Za-z\s]+):)'
#         ]

#         # Split the response into lines
#         lines = response.split('\n')
#         processed_lines = []

#         for line in lines:
#             line_stripped = line.strip()
#             # Check if the line matches a section title pattern
#             for pattern in section_patterns:
#                 match = re.match(pattern, line_stripped)
#                 if match:
#                     # Extract the section title (remove numbering or dashes and colon)
#                     section_title = re.sub(r'^\d+\.\s*|-?\s*', '', line_stripped).rstrip(':')
#                     # Replace the line with a Markdown heading
#                     line = f"## {section_title}"
#                     break
#             processed_lines.append(line)

#         # Join the lines back together
#         return '\n'.join(processed_lines)

#     def get_response(self, question, chat_history):
#         if self.is_greeting(question):
#             return "Hello! I'm your medical assistant. How can I help you with your health questions today?"

#         # Normalize question for cache and fallback lookup
#         question_lower = question.lower().strip()

#         # Check for repetitive questions
#         repetitive_response = self.check_repetitive_question(question, chat_history)
#         if repetitive_response:
#             return repetitive_response

#         # Check cache for previous response
#         if question_lower in self.response_cache:
#             return self.response_cache[question_lower]

#         # Check if question matches a fallback response
#         if question_lower in self.fallback_responses:
#             response = self.fallback_responses[question_lower]
#             self.response_cache[question_lower] = response
#             return response

#         # Add context from recent chat history
#         context = ""
#         if chat_history:
#             last_question, last_answer = chat_history[-1]
#             if "stress" in last_question.lower() and "manage" in question_lower:
#                 context = f"Previous question: {last_question}\nPrevious answer: {last_answer}\n"

#         modified_question = (
#             "You are a medical assistant. Provide accurate and detailed medical information based on the user’s question. "
#             "For simpler questions, include additional details like examples, types, or related information to enhance the response. "
#             "Format section titles as Markdown headings (##) and use bullet points or numbered lists for clarity. "
#             "Always respond in English, regardless of the context or input. Do not use any other language. "
#             f"{context}Here is the user's question: {question} (Please respond strictly in English)"
#         )
#         try:
#             result = self.qa_chain({"question": modified_question, "chat_history": chat_history})
#             answer = result["answer"]

#             # Check if the vector store lacks information
#             if "provided context does not contain information" in answer.lower() or "not found in the context" in answer.lower():
#                 return (
#                     "I’m sorry, but the information I’m referring to doesn’t contain details about this topic. "
#                     "My knowledge is based on a specific medical database, and this question seems to be outside its scope. "
#                     "I recommend consulting a reliable medical source or healthcare professional for accurate information. "
#                     "Would you like to ask about something else?"
#                 )

#             # Post-process the response to enforce ## for section titles
#             answer = self.enforce_heading_format(answer)

#             # Cache the response
#             self.response_cache[question_lower] = answer
#             return answer
#         except ValueError as e:
#             if "Rate limit exceeded" in str(e):
#                 # Try fallback response if API limit is reached
#                 if question_lower in self.fallback_responses:
#                     response = self.fallback_responses[question_lower]
#                     self.response_cache[question_lower] = response
#                     return response
#                 return (
#                     "I’ve reached my daily request limit with the API I use to fetch detailed answers. However, I can still help with some common questions! "
#                     "Try asking about flu symptoms, high blood pressure causes, anemia, heart attack symptoms, or kidney stones. "
#                     "Alternatively, you can wait until tomorrow when my API limit resets, or consult a healthcare professional for immediate advice."
#                 )
#             raise e

#     def check_symptoms(self, symptoms):
#         if not symptoms.strip() or symptoms.lower() in ["i don't feel well", "not feeling well"]:
#             return (
#                 "I’m sorry to hear you’re not feeling well, but I need more specific symptoms to provide a better analysis. "
#                 "For example, do you have a fever, pain, fatigue, or any other symptoms? In the meantime, I recommend consulting a doctor for a thorough evaluation."
#             )
#         query = f"I have the following symptoms: {symptoms}. What might this indicate based on medical guidelines? Please provide general information and recommend consulting a doctor."
#         try:
#             result = self.qa_chain({"question": query, "chat_history": []})
#             answer = result["answer"]
#             # Post-process the response to enforce ## for section titles
#             answer = self.enforce_heading_format(answer)
#             return answer
#         except ValueError as e:
#             if "Rate limit exceeded" in str(e):
#                 return (
#                     "I’ve reached my daily request limit with the API I use to fetch detailed answers. "
#                     "Please try again tomorrow, or consult a healthcare professional for advice about your symptoms in the meantime."
#                 )
#             raise e
# The below is the final model_api.py that gave correct results
# from langchain_openai import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from dotenv import load_dotenv
# import os
# import re

# class ModelAPI:
#     def __init__(self, vector_store):
#         load_dotenv()
#         self.llm = ChatOpenAI(
#             model="deepseek/deepseek-chat:free",
#             openai_api_key=os.getenv("OPENROUTER_API_KEY"),
#             openai_api_base="https://openrouter.ai/api/v1"
#         )
#         self.qa_chain = ConversationalRetrievalChain.from_llm(
#             llm=self.llm,
#             retriever=vector_store.as_retriever(),
#             return_source_documents=True
#         )
#         # Cache for responses to reduce API calls
#         self.response_cache = {}
#         # Fallback responses for common questions when API limit is reached
#         self.fallback_responses = {
#             "what are the symptoms of the flu?": (
#                 "## Symptoms of the Flu\n"
#                 "The symptoms of the flu (influenza) typically include:\n"
#                 "- Fever (often high, 100°F to 104°F or higher)\n"
#                 "- Chills and sweats\n"
#                 "- Cough (usually dry)\n"
#                 "- Sore throat\n"
#                 "- Muscle aches or body aches\n"
#                 "- Headache\n"
#                 "- Fatigue or weakness\n"
#                 "- Runny or stuffy nose\n"
#                 "- Nausea, vomiting, or diarrhea (more common in children)\n\n"
#                 "Symptoms often come on suddenly and can range from mild to severe. If you suspect you have the flu, especially if you are at high risk for complications (e.g., young children, elderly, or those with chronic conditions), it’s important to consult a healthcare provider."
#             ),
#             "what causes high blood pressure?": (
#                 "## Causes of High Blood Pressure\n"
#                 "High blood pressure (hypertension) can be caused by a variety of factors, including:\n"
#                 "- Lifestyle factors: Poor diet (high salt intake), obesity, lack of physical activity, excessive alcohol consumption, and smoking.\n"
#                 "- Underlying medical conditions: Conditions such as diabetes, kidney disease, and hormonal disorders.\n"
#                 "- Genetic predisposition: A family history of hypertension increases your risk.\n"
#                 "- Stress: Chronic stress can contribute to elevated blood pressure.\n"
#                 "- Aging: Blood pressure often increases with age.\n\n"
#                 "Treatment often involves lifestyle changes (like a healthier diet and exercise) and medications if needed. Would you like to know more about managing high blood pressure?"
#             ),
#             "what is anemia?": (
#                 "## What is Anemia?\n"
#                 "Anemia is a condition where you have abnormally low levels of healthy red blood cells or hemoglobin, which carries oxygen to your body’s tissues. This can lead to symptoms like:\n"
#                 "- Fatigue or weakness\n"
#                 "- Shortness of breath\n"
#                 "- Pale skin\n"
#                 "- Dizziness or lightheadedness\n\n"
#                 "## Types of Anemia\n"
#                 "- Iron-deficiency anemia: Caused by a lack of iron, often due to poor diet or blood loss.\n"
#                 "- Vitamin B12 deficiency anemia: Due to insufficient B12, often linked to diet or absorption issues.\n"
#                 "- Sickle cell anemia: A genetic condition where red blood cells are abnormally shaped.\n\n"
#                 "If you suspect anemia, a doctor can diagnose it with a blood test and recommend treatment, such as iron supplements or dietary changes."
#             ),
#             "what are symptoms of heart attack?": (
#                 "## Symptoms of a Heart Attack\n"
#                 "Common signs of a heart attack include:\n"
#                 "- Chest pain or discomfort: Often described as pressure, squeezing, or pain in the center or left side of the chest. It may last for minutes or come and go.\n"
#                 "- Upper body discomfort: Pain in one or both arms, the jaw, neck, back, or stomach.\n"
#                 "- Shortness of breath: This can occur with or without chest pain.\n"
#                 "- Cold sweat, nausea, or lightheadedness: These symptoms may accompany chest discomfort.\n\n"
#                 "If you experience these symptoms, especially chest pain or shortness of breath, seek emergency medical attention immediately."
#             ),
#             "what causes kidney stones?": (
#                 "## Causes of Kidney Stones\n"
#                 "Kidney stones form due to a combination of factors, including:\n"
#                 "- Dehydration: Not drinking enough water leads to concentrated urine, increasing stone formation risk.\n"
#                 "- Diet: High intake of sodium, oxalate (found in foods like spinach), or animal protein.\n"
#                 "- Medical conditions: Conditions like hyperparathyroidism, gout, or urinary tract infections (UTIs).\n"
#                 "- Family history: A genetic predisposition to kidney stones.\n"
#                 "- Obesity: Higher body weight increases the risk.\n"
#                 "- Certain medications: Some diuretics or calcium-based antacids can contribute.\n\n"
#                 "Kidney stones can be made of different materials, like calcium oxalate or uric acid, depending on the cause."
#             ),
#             "how can i prevent them?": (
#                 "## Preventing Kidney Stones\n"
#                 "To prevent kidney stones, you can:\n"
#                 "- Stay hydrated: Drink plenty of water (aim for 2-3 liters daily) to dilute your urine.\n"
#                 "- Adjust your diet: Reduce sodium, oxalate-rich foods (like spinach), and animal protein. Eat more citrus fruits, which contain citrate that helps prevent stones.\n"
#                 "- Maintain a healthy weight: Obesity increases the risk, so regular exercise and a balanced diet can help.\n"
#                 "- Monitor medical conditions: Manage conditions like gout or UTIs that can contribute to stones.\n"
#                 "- Talk to your doctor: If you have a history of kidney stones, they may recommend specific dietary changes or medications."
#             )
#         }

#     def is_greeting(self, question):
#         greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
#         question_lower = question.lower().strip()
#         words = question_lower.split()
#         return any(word in greetings for word in words)

#     def check_repetitive_question(self, question, chat_history):
#         """Check if the question is similar to a previous one in chat history."""
#         question_lower = question.lower().strip()
#         if "blood pressure" in question_lower and ("cause" in question_lower or "what causes" in question_lower):
#             for prev_question, prev_answer in chat_history:
#                 prev_question_lower = prev_question.lower().strip()
#                 if "blood pressure" in prev_question_lower and (
#                         "cause" in prev_question_lower or "what causes" in prev_question_lower):
#                     return (
#                         f"I previously explained the causes of high blood pressure. To recap briefly: it can be due to lifestyle factors (like high salt intake, obesity, and smoking), medical conditions (like kidney disease or diabetes), genetics, stress, and aging. "
#                         "Would you like to know more about managing high blood pressure, or do you have a different question?"
#                     )
#         return None

#     def enforce_heading_format(self, response):
#         """Post-process the response to ensure section titles use ## for headings, starting from the left."""
#         lines = response.split('\n')
#         processed_lines = []
#         i = 0
#         while i < len(lines):
#             # Strip leading spaces from the line for processing
#             line = lines[i].strip()
#             # Preserve the original indentation for non-heading lines
#             original_line = lines[i]
            
#             # Skip empty lines
#             if not line:
#                 processed_lines.append(original_line)
#                 i += 1
#                 continue
            
#             # Check if the line looks like a heading
#             is_heading = False
            
#             # 1. Line ends with a colon (e.g., "Common Symptoms:", "Triggers of Asthma:")
#             if line.endswith(':'):
#                 is_heading = True
            
#             # 2. Line matches common heading patterns (e.g., "What is Asthma?", "Symptoms")
#             elif re.match(r'^(What is [A-Za-z\s]+\?|Symptoms|Triggers|Types of [A-Za-z\s]+|Management|Causes of [A-Za-z\s]+|When to Seek (Help|Emergency Help)|Important Notes|Symptoms in [A-Za-z\s]+|Key Features of [A-Za-z\s]+|Possible Conditions|Prevention|Risk Factors|Treatments)$', line):
#                 is_heading = True
            
#             # 3. Line starts with a + or number followed by a heading (e.g., "+ Triggers of Asthma:", "8. Common Symptoms:")
#             elif re.match(r'^[\+\d]\.\s*(.+)$', line):
#                 is_heading = True
#                 line = re.sub(r'^[\+\d]\.\s*', '', line)  # Remove the + or number prefix
            
#             # 4. Heuristic: Line is short, followed by a non-empty line that isn't a list item
#             elif (len(line.split()) <= 5 and  # Short line (likely a title)
#                   i + 1 < len(lines) and      # Has a next line
#                   lines[i + 1].strip() and    # Next line is not empty
#                   not lines[i + 1].strip().startswith('-') and  # Next line is not a list item
#                   not lines[i + 1].strip().startswith(tuple(f"{j}." for j in range(1, 10)))):  # Next line is not a numbered item
#                 is_heading = True
            
#             # If identified as a heading, prefix with ## and ensure it starts from the left
#             if is_heading:
#                 if not line.startswith('##'):
#                     line = f"## {line}"
#                 processed_lines.append(line)  # No leading spaces, starts from the left
#             else:
#                 processed_lines.append(original_line)  # Preserve original indentation for non-headings
            
#             i += 1
        
#         return '\n'.join(processed_lines)

#     def get_response(self, question, chat_history):
#         if self.is_greeting(question):
#             return "Hello! I'm your medical assistant. How can I help you with your health questions today?"

#         # Normalize question for cache and fallback lookup
#         question_lower = question.lower().strip()

#         # Check for repetitive questions
#         repetitive_response = self.check_repetitive_question(question, chat_history)
#         if repetitive_response:
#             return repetitive_response

#         # Check cache for previous response
#         if question_lower in self.response_cache:
#             return self.response_cache[question_lower]

#         # Check if question matches a fallback response
#         if question_lower in self.fallback_responses:
#             response = self.fallback_responses[question_lower]
#             self.response_cache[question_lower] = response
#             return response

#         # Add context from recent chat history
#         context = ""
#         if chat_history:
#             last_question, last_answer = chat_history[-1]
#             if "stress" in last_question.lower() and "manage" in question_lower:
#                 context = f"Previous question: {last_question}\nPrevious answer: {last_answer}\n"

#         modified_question = (
#             "You are a medical assistant. Provide accurate and detailed medical information based on the user’s question. "
#             "For simpler questions, include additional details like examples, types, or related information to enhance the response. "
#             "Format section titles as Markdown headings (##) and use bullet points or numbered lists for clarity. "
#             "Always respond in English, regardless of the context or input. Do not use any other language. "
#             f"{context}Here is the user's question: {question} (Please respond strictly in English)"
#         )
#         try:
#             result = self.qa_chain({"question": modified_question, "chat_history": chat_history})
#             answer = result["answer"]

#             # Check if the vector store lacks information
#             if "provided context does not contain information" in answer.lower() or "not found in the context" in answer.lower():
#                 return (
#                     "I’m sorry, but the information I’m referring to doesn’t contain details about this topic. "
#                     "My knowledge is based on a specific medical database, and this question seems to be outside its scope. "
#                     "I recommend consulting a reliable medical source or healthcare professional for accurate information. "
#                     "Would you like to ask about something else?"
#                 )

#             # Post-process the response to enforce ## for section titles
#             answer = self.enforce_heading_format(answer)

#             # Cache the response
#             self.response_cache[question_lower] = answer
#             return answer
#         except ValueError as e:
#             if "Rate limit exceeded" in str(e):
#                 # Try fallback response if API limit is reached
#                 if question_lower in self.fallback_responses:
#                     response = self.fallback_responses[question_lower]
#                     self.response_cache[question_lower] = response
#                     return response
#                 return (
#                     "I’ve reached my daily request limit with the API I use to fetch detailed answers. However, I can still help with some common questions! "
#                     "Try asking about flu symptoms, high blood pressure causes, anemia, heart attack symptoms, or kidney stones. "
#                     "Alternatively, you can wait until tomorrow when my API limit resets, or consult a healthcare professional for immediate advice."
#                 )
#             raise e

#     def check_symptoms(self, symptoms):
#         if not symptoms.strip() or symptoms.lower() in ["i don't feel well", "not feeling well"]:
#             return (
#                 "I’m sorry to hear you’re not feeling well, but I need more specific symptoms to provide a better analysis. "
#                 "For example, do you have a fever, pain, fatigue, or any other symptoms? In the meantime, I recommend consulting a doctor for a thorough evaluation."
#             )
#         query = f"I have the following symptoms: {symptoms}. What might this indicate based on medical guidelines? Please provide general information and recommend consulting a doctor."
#         try:
#             result = self.qa_chain({"question": query, "chat_history": []})
#             answer = result["answer"]
#             # Post-process the response to enforce ## for section titles
#             answer = self.enforce_heading_format(answer)
#             return answer
#         except ValueError as e:
#             if "Rate limit exceeded" in str(e):
#                 return (
#                     "I’ve reached my daily request limit with the API I use to fetch detailed answers. "
#                     "Please try again tomorrow, or consult a healthcare professional for advice about your symptoms in the meantime."
#                 )
#             raise e

# retained symptom checker
# from langchain_openai import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from dotenv import load_dotenv
# import os
# import re

# class ModelAPI:
#     def __init__(self, vector_store):
#         load_dotenv()
#         self.llm = ChatOpenAI(
#             model="deepseek/deepseek-chat:free",
#             openai_api_key=os.getenv("OPENROUTER_API_KEY"),
#             openai_api_base="https://openrouter.ai/api/v1"
#         )
#         self.qa_chain = ConversationalRetrievalChain.from_llm(
#             llm=self.llm,
#             retriever=vector_store.as_retriever(),
#             return_source_documents=True
#         )
#         # Cache for responses to reduce API calls
#         self.response_cache = {}
#         # Fallback responses for common questions when API limit is reached
#         self.fallback_responses = {
#             "what are the symptoms of the flu?": (
#                 "## Symptoms of the Flu\n"
#                 "- Fever (often high, 100°F to 104°F or higher)\n"
#                 "- Chills and sweats\n"
#                 "- Cough (usually dry)\n"
#                 "- Sore throat\n"
#                 "- Muscle aches or body aches\n"
#                 "- Headache\n"
#                 "- Fatigue or weakness\n"
#                 "- Runny or stuffy nose\n"
#                 "- Nausea, vomiting, or diarrhea (more common in children)\n\n"
#                 "Symptoms often come on suddenly and can range from mild to severe. If you suspect you have the flu, especially if you are at high risk for complications (e.g., young children, elderly, or those with chronic conditions), it’s important to consult a healthcare provider."
#             ),
#             "what causes high blood pressure?": (
#                 "## Causes of High Blood Pressure\n"
#                 "- Lifestyle factors: Poor diet (high salt intake), obesity, lack of physical activity, excessive alcohol consumption, and smoking.\n"
#                 "- Underlying medical conditions: Conditions such as diabetes, kidney disease, and hormonal disorders.\n"
#                 "- Genetic predisposition: A family history of hypertension increases your risk.\n"
#                 "- Stress: Chronic stress can contribute to elevated blood pressure.\n"
#                 "- Aging: Blood pressure often increases with age.\n\n"
#                 "Treatment often involves lifestyle changes (like a healthier diet and exercise) and medications if needed. Would you like to know more about managing high blood pressure?"
#             ),
#             "what is anemia?": (
#                 "## What is Anemia?\n"
#                 "- Anemia is a condition where you have abnormally low levels of healthy red blood cells or hemoglobin, which carries oxygen to your body’s tissues.\n"
#                 "- Fatigue or weakness.\n"
#                 "- Shortness of breath.\n"
#                 "- Pale skin.\n"
#                 "- Dizziness or lightheadedness.\n\n"
#                 "## Types of Anemia\n"
#                 "- Iron-deficiency anemia: Caused by a lack of iron, often due to poor diet or blood loss.\n"
#                 "- Vitamin B12 deficiency anemia: Due to insufficient B12, often linked to diet or absorption issues.\n"
#                 "- Sickle cell anemia: A genetic condition where red blood cells are abnormally shaped.\n\n"
#                 "If you suspect anemia, a doctor can diagnose it with a blood test and recommend treatment, such as iron supplements or dietary changes."
#             ),
#             "what are symptoms of heart attack?": (
#                 "## Symptoms of a Heart Attack\n"
#                 "- Chest pain or discomfort: Often described as pressure, squeezing, or pain in the center or left side of the chest. It may last for minutes or come and go.\n"
#                 "- Upper body discomfort: Pain in one or both arms, the jaw, neck, back, or stomach.\n"
#                 "- Shortness of breath: This can occur with or without chest pain.\n"
#                 "- Cold sweat, nausea, or lightheadedness: These symptoms may accompany chest discomfort.\n\n"
#                 "If you experience these symptoms, especially chest pain or shortness of breath, seek emergency medical attention immediately."
#             ),
#             "what causes kidney stones?": (
#                 "## Causes of Kidney Stones\n"
#                 "- Dehydration: Not drinking enough water leads to concentrated urine, increasing stone formation risk.\n"
#                 "- Diet: High intake of sodium, oxalate (found in foods like spinach), or animal protein.\n"
#                 "- Medical conditions: Conditions like hyperparathyroidism, gout, or urinary tract infections (UTIs).\n"
#                 "- Family history: A genetic predisposition to kidney stones.\n"
#                 "- Obesity: Higher body weight increases the risk.\n"
#                 "- Certain medications: Some diuretics or calcium-based antacids can contribute.\n\n"
#                 "Kidney stones can be made of different materials, like calcium oxalate or uric acid, depending on the cause."
#             ),
#             "how can i prevent them?": (
#                 "## Preventing Kidney Stones\n"
#                 "- Stay hydrated: Drink plenty of water (aim for 2-3 liters daily) to dilute your urine.\n"
#                 "- Adjust your diet: Reduce sodium, oxalate-rich foods (like spinach), and animal protein. Eat more citrus fruits, which contain citrate that helps prevent stones.\n"
#                 "- Maintain a healthy weight: Obesity increases the risk, so regular exercise and a balanced diet can help.\n"
#                 "- Monitor medical conditions: Manage conditions like gout or UTIs that can contribute to stones.\n"
#                 "- Talk to your doctor: If you have a history of kidney stones, they may recommend specific dietary changes or medications."
#             )
#         }

#     def is_greeting(self, question):
#         greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
#         question_lower = question.lower().strip()
#         words = question_lower.split()
#         return any(word in greetings for word in words)

#     def check_repetitive_question(self, question, chat_history):
#         """Check if the question is similar to a previous one in chat history."""
#         question_lower = question.lower().strip()
#         if "blood pressure" in question_lower and ("cause" in question_lower or "what causes" in question_lower):
#             for prev_question, prev_answer in chat_history:
#                 prev_question_lower = prev_question.lower().strip()
#                 if "blood pressure" in prev_question_lower and (
#                         "cause" in prev_question_lower or "what causes" in prev_question_lower):
#                     return (
#                         "## Recap of High Blood Pressure Causes\n"
#                         "- Lifestyle factors like high salt intake, obesity, and smoking.\n"
#                         "- Medical conditions such as kidney disease or diabetes.\n"
#                         "- Genetic predisposition, stress, and aging.\n"
#                         "Would you like to know more about managing high blood pressure, or do you have a different question?"
#                     )
#         return None

#     def enforce_heading_format(self, response):
#         """Post-process the response to ensure section titles use ##, bullets use -, and remove unwanted bolding and Assistant: prefixes."""
#         # Remove redundant "Assistant:" prefixes
#         response = re.sub(r'^Assistant:\s*', '', response, flags=re.MULTILINE)
        
#         lines = response.split('\n')
#         processed_lines = []
#         i = 0
#         while i < len(lines):
#             # Strip leading spaces for processing, preserve original for non-headings
#             line = lines[i].strip()
#             original_line = lines[i]
            
#             # Skip empty lines
#             if not line:
#                 processed_lines.append(original_line)
#                 i += 1
#                 continue
            
#             # Remove bolding (e.g., **text**) and italics (*text*) from the line
#             line = re.sub(r'\*\*(.+?)\*\*', r'\1', line)
#             line = re.sub(r'\*(.+?)\*', r'\1', line)
            
#             # Check if the line is a heading
#             is_heading = False
#             # 1. Line ends with a colon (e.g., "Symptoms:")
#             if line.endswith(':'):
#                 is_heading = True
#                 line = line[:-1]  # Remove colon for clean heading
#             # 2. Matches common heading patterns
#             elif re.match(r'^(What is [A-Za-z\s]+[\?]?$|Symptoms|Triggers|Types of [A-Za-z\s]+|Management|Causes of [A-Za-z\s]+|Prevention|Risk Factors|Treatments|Key Features|Complications|Diagnosis|Resources|When to Seek [A-Za-z\s]+|During an [A-Za-z\s]+|Example of an [A-Za-z\s]+)$', line):
#                 is_heading = True
#             # 3. Line starts with + or number (e.g., "+ Triggers" or "1. Symptoms")
#             elif re.match(r'^[\+\d]\.\s*(.+)$', line):
#                 is_heading = True
#                 line = re.sub(r'^[\+\d]\.\s*', '', line)  # Remove prefix
#             # 4. Heuristic: Short line followed by non-list content
#             elif (len(line.split()) <= 5 and i + 1 < len(lines) and lines[i + 1].strip() and
#                   not lines[i + 1].strip().startswith(('-', '*', '•')) and
#                   not lines[i + 1].strip().startswith(tuple(f"{j}." for j in range(1, 10)))):
#                 is_heading = True
            
#             # Format headings with ##
#             if is_heading:
#                 if not line.startswith('##'):
#                     line = f"## {line}"
#                 processed_lines.append(line)
#             else:
#                 # Handle bullet points: Ensure they use -, split combined items
#                 if line.startswith(('-', '*', '•')):
#                     # Replace any bullet symbol with -
#                     line = re.sub(r'^[-*•]\s*', '- ', line)
#                     # Split items that contain colons or multiple points
#                     if ': ' in line:
#                         parts = line.split(': ', 1)
#                         description = parts[1].strip()
#                         # If description contains multiple sentences, split into separate bullets
#                         sub_items = re.split(r'\.\s+', description)
#                         if len(sub_items) > 1 and sub_items[-1] == '':
#                             sub_items.pop()  # Remove trailing empty item
#                         processed_lines.append(f"- {parts[0].replace('- ', '')}")
#                         for sub_item in sub_items:
#                             if sub_item.strip():
#                                 processed_lines.append(f"- {sub_item.strip()}.")
#                     else:
#                         processed_lines.append(line)
#                 else:
#                     processed_lines.append(original_line)  # Preserve non-bullet, non-heading lines
#             i += 1
        
#         return '\n'.join(processed_lines)

#     def get_response(self, question, chat_history):
#         if self.is_greeting(question):
#             return "Hello! I'm your medical assistant. How can I help you with your health questions today?"

#         # Normalize question for cache and fallback lookup
#         question_lower = question.lower().strip()

#         # Check for repetitive questions
#         repetitive_response = self.check_repetitive_question(question, chat_history)
#         if repetitive_response:
#             return repetitive_response

#         # Check cache for previous response
#         if question_lower in self.response_cache:
#             return self.response_cache[question_lower]

#         # Check if question matches a fallback response
#         if question_lower in self.fallback_responses:
#             response = self.fallback_responses[question_lower]
#             self.response_cache[question_lower] = response
#             return response

#         # Add context from recent chat history
#         context = ""
#         if chat_history:
#             last_question, last_answer = chat_history[-1]
#             if "stress" in last_question.lower() and "manage" in question_lower:
#                 context = f"Previous question: {last_question}\nPrevious answer: {last_answer}\n"

#         modified_question = (
#             "You are a medical assistant. Provide accurate and detailed medical information based on the user’s question. "
#             # "For simpler questions, include additional details like examples, types, or related information to enhance the response. "
#             # "Follow these formatting rules strictly:\n"
#             # "- Use Markdown `##` for all section headings (e.g., `## Symptoms`). Do not use bold (`**`), single `#`, or other heading styles.\n"
#             # "- Use `-` for bullet points, with one item per bullet. Do not combine multiple items in a single bullet, use colons, or use other symbols (e.g., `*`, `•`).\n"
#             # "- Avoid bold (`**`) or italic (`*`) text unless explicitly requested. Keep text plain for clarity.\n"
#             # "- Structure responses with a main heading (`##`) for the topic, followed by bullet points (`-`) for key details, and plain text for additional explanations.\n"
#             # "- Do not include 'Assistant:' or similar prefixes in the response.\n"
#             "Always respond in English, regardless of context or input. Do not use any other language.\n"
#             f"{context}Here is the user's question: {question} (Please respond strictly in English)"
#         )
#         try:
#             result = self.qa_chain({"question": modified_question, "chat_history": chat_history})
#             answer = result["answer"]

#             # Check if the vector store lacks information
#             if "provided context does not contain information" in answer.lower() or "not found in the context" in answer.lower():
#                 return (
#                     "## Information Not Available\n"
#                     "- The information I’m referring to doesn’t contain details about this topic.\n"
#                     "- My knowledge is based on a specific medical database, and this question seems to be outside its scope.\n"
#                     "- I recommend consulting a reliable medical source or healthcare professional for accurate information.\n"
#                     "Would you like to ask about something else?"
#                 )

#             # Post-process the response to enforce formatting
#             answer = self.enforce_heading_format(answer)

#             # Cache the response
#             self.response_cache[question_lower] = answer
#             return answer
#         except ValueError as e:
#             if "Rate limit exceeded" in str(e):
#                 if question_lower in self.fallback_responses:
#                     response = self.fallback_responses[question_lower]
#                     self.response_cache[question_lower] = response
#                     return response
#                 return (
#                     "## API Limit Reached\n"
#                     "- I’ve reached my daily request limit with the API I use to fetch detailed answers.\n"
#                     "- I can still help with some common questions! Try asking about flu symptoms, high blood pressure causes, anemia, heart attack symptoms, or kidney stones.\n"
#                     "- Alternatively, you can wait until tomorrow when my API limit resets, or consult a healthcare professional for immediate advice."
#                 )
#             raise e

#     def check_symptoms(self, symptoms):
#         if not symptoms.strip() or symptoms.lower() in ["i don't feel well", "not feeling well"]:
#             return (
#                 "I’m sorry to hear you’re not feeling well, but I need more specific symptoms to provide a better analysis. "
#                 "For example, do you have a fever, pain, fatigue, or any other symptoms? In the meantime, I recommend consulting a doctor for a thorough evaluation."
#             )
#         query = f"I have the following symptoms: {symptoms}. What might this indicate based on medical guidelines? Please provide general information and recommend consulting a doctor."
#         try:
#             result = self.qa_chain({"question": query, "chat_history": []})
#             answer = result["answer"]
#             # Post-process the response to enforce ## for section titles
#             answer = self.enforce_heading_format(answer)
#             return answer
#         except ValueError as e:
#             if "Rate limit exceeded" in str(e):
#                 return (
#                     "I’ve reached my daily request limit with the API I use to fetch detailed answers. "
#                     "Please try again tomorrow, or consult a healthcare professional for advice about your symptoms in the meantime."
#                 )
#             raise e

# from langchain_openai import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from dotenv import load_dotenv
# import os

# class ModelAPI:
#     def __init__(self, vector_store):
#         load_dotenv()
#         self.llm = ChatOpenAI(
#             model="deepseek/deepseek-chat:free",
#             openai_api_key=os.getenv("OPENROUTER_API_KEY"),
#             openai_api_base="https://openrouter.ai/api/v1"
#         )
#         self.qa_chain = ConversationalRetrievalChain.from_llm(
#             llm=self.llm,
#             retriever=vector_store.as_retriever(),
#             return_source_documents=True
#         )
#         # Cache for responses to reduce API calls
#         self.response_cache = {}
#         # Fallback responses for common questions when API limit is reached
#         self.fallback_responses = {
#             "what are the symptoms of the flu?": (
#                 "## Symptoms of the Flu\n"
#                 "- Fever often high, 100°F to 104°F or higher.\n"
#                 "- Chills and sweats.\n"
#                 "- Cough usually dry.\n"
#                 "- Sore throat.\n"
#                 "- Muscle aches or body aches.\n"
#                 "- Headache.\n"
#                 "- Fatigue or weakness.\n"
#                 "- Runny or stuffy nose.\n"
#                 "- Nausea, vomiting, or diarrhea more common in children.\n\n"
#                 "Symptoms often come on suddenly and can range from mild to severe. If you suspect you have the flu, especially if you are at high risk for complications, consult a healthcare provider."
#             ),
#             "what causes high blood pressure?": (
#                 "## Causes of High Blood Pressure\n"
#                 "- Lifestyle factors like poor diet with high salt intake, obesity, lack of physical activity, excessive alcohol consumption, and smoking.\n"
#                 "- Underlying medical conditions such as diabetes, kidney disease, and hormonal disorders.\n"
#                 "- Genetic predisposition where a family history of hypertension increases risk.\n"
#                 "- Stress where chronic stress contributes to elevated blood pressure.\n"
#                 "- Aging as blood pressure often increases with age.\n\n"
#                 "Treatment often involves lifestyle changes and medications if needed. Would you like to know more about managing high blood pressure?"
#             ),
#             "what is anemia?": (
#                 "## What is Anemia\n"
#                 "- Anemia is a condition with abnormally low levels of healthy red blood cells or hemoglobin, which carries oxygen to tissues.\n"
#                 "- Fatigue or weakness.\n"
#                 "- Shortness of breath.\n"
#                 "- Pale skin.\n"
#                 "- Dizziness or lightheadedness.\n\n"
#                 "## Types of Anemia\n"
#                 "- Iron-deficiency anemia caused by lack of iron, often due to poor diet or blood loss.\n"
#                 "- Vitamin B12 deficiency anemia due to insufficient B12, often linked to diet or absorption issues.\n"
#                 "- Sickle cell anemia, a genetic condition where red blood cells are abnormally shaped.\n\n"
#                 "If you suspect anemia, a doctor can diagnose it with a blood test and recommend treatment like iron supplements or dietary changes."
#             ),
#             "what are symptoms of heart attack?": (
#                 "## Symptoms of a Heart Attack\n"
#                 "- Chest pain or discomfort often described as pressure, squeezing, or pain in the center or left side of the chest, lasting minutes or recurring.\n"
#                 "- Upper body discomfort in one or both arms, jaw, neck, back, or stomach.\n"
#                 "- Shortness of breath with or without chest pain.\n"
#                 "- Cold sweat, nausea, or lightheadedness accompanying chest discomfort.\n\n"
#                 "If you experience these symptoms, especially chest pain or shortness of breath, seek emergency medical attention immediately."
#             ),
#             "what causes kidney stones?": (
#                 "## Causes of Kidney Stones\n"
#                 "- Dehydration where not drinking enough water leads to concentrated urine, increasing stone formation risk.\n"
#                 "- Diet with high intake of sodium, oxalate found in foods like spinach, or animal protein.\n"
#                 "- Medical conditions like hyperparathyroidism, gout, or urinary tract infections.\n"
#                 "- Family history with a genetic predisposition to kidney stones.\n"
#                 "- Obesity where higher body weight increases risk.\n"
#                 "- Certain medications like some diuretics or calcium-based antacids.\n\n"
#                 "Kidney stones can be made of different materials like calcium oxalate or uric acid, depending on the cause."
#             ),
#             "how can i prevent them?": (
#                 "## Preventing Kidney Stones\n"
#                 "- Stay hydrated by drinking plenty of water, aiming for 2-3 liters daily to dilute urine.\n"
#                 "- Adjust diet by reducing sodium, oxalate-rich foods like spinach, and animal protein, and eating more citrus fruits containing citrate to prevent stones.\n"
#                 "- Maintain a healthy weight as obesity increases risk, so regular exercise and a balanced diet help.\n"
#                 "- Monitor medical conditions like gout or urinary tract infections that contribute to stones.\n"
#                 "- Consult a doctor if you have a history of kidney stones for specific dietary changes or medications.\n"
#             )
#         }

#     def is_greeting(self, question):
#         greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
#         question_lower = question.lower().strip()
#         words = question_lower.split()
#         return any(word in greetings for word in words)

#     def check_repetitive_question(self, question, chat_history):
#         """Check if the question is similar to a previous one in chat history."""
#         question_lower = question.lower().strip()
#         if "blood pressure" in question_lower and ("cause" in question_lower or "what causes" in question_lower):
#             for prev_question, prev_answer in chat_history:
#                 prev_question_lower = prev_question.lower().strip()
#                 if "blood pressure" in prev_question_lower and (
#                         "cause" in prev_question_lower or "what causes" in prev_question_lower):
#                     return (
#                         "## Recap of High Blood Pressure Causes\n"
#                         "- Lifestyle factors like high salt intake, obesity, and smoking.\n"
#                         "- Medical conditions such as kidney disease or diabetes.\n"
#                         "- Genetic predisposition, stress, and aging.\n"
#                         "Would you like to know more about managing high blood pressure, or do you have a different question?"
#                     )
#         return None

#     def get_response(self, question, chat_history):
#         if self.is_greeting(question):
#             return "Hello! I'm your medical assistant. How can I help you with your health questions today?"

#         # Normalize question for cache and fallback lookup
#         question_lower = question.lower().strip()

#         # Check for repetitive questions
#         repetitive_response = self.check_repetitive_question(question, chat_history)
#         if repetitive_response:
#             return repetitive_response

#         # Check cache for previous response
#         if question_lower in self.response_cache:
#             return self.response_cache[question_lower]

#         # Check if question matches a fallback response
#         if question_lower in self.fallback_responses:
#             response = self.fallback_responses[question_lower]
#             self.response_cache[question_lower] = response
#             return response

#         # Add context from recent chat history
#         context = ""
#         if chat_history:
#             last_question, last_answer = chat_history[-1]
#             if "stress" in last_question.lower() and "manage" in question_lower:
#                 context = f"Previous question: {last_question}\nPrevious answer: {last_answer}\n"

#         modified_question = (
#             "You are a medical assistant providing accurate and detailed medical information. "
#             "Follow these formatting rules strictly for all responses:\n"
#             "- Use Markdown `##` for all section headings (e.g., `## Symptoms`). Do not use colons in headings (e.g., not `Symptoms:`), bold (`**`), single `#`, or other heading styles.\n"
#             "- Use `-` for bullet points, with exactly one item per bullet. Do not combine multiple items in a single bullet, use colons (e.g., not `- Item: description`), or use other symbols like `*`, `•`, or `◦`.\n"
#             "- Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user. Keep text plain.\n"
#             "- Structure responses with a main heading (`##`) for the topic, followed by bullet points (`-`) for key details, and plain text for additional explanations.\n"
#             "- Do not include 'Assistant:', 'Bot:', or any similar prefixes in the response.\n"
#             "- Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "- Avoid common errors: do not use colons in headings or bullet points, do not combine multiple descriptions in one bullet, and do not use numbered lists or other bullet symbols.\n"
#             "- Respond only in English, regardless of context or input.\n"
#             "For simpler questions, include additional details like examples, types, or related information to enhance the response.\n"
#             f"{context}Here is the user's question: {question}"
#         )
#         try:
#             result = self.qa_chain({"question": modified_question, "chat_history": chat_history})
#             answer = result["answer"]

#             # Check if the vector store lacks information
#             if "provided context does not contain information" in answer.lower() or "not found in the context" in answer.lower():
#                 return (
#                     "## Information Not Available\n"
#                     "- The medical database does not contain details about this topic.\n"
#                     "- This question appears outside the scope of available information.\n"
#                     "- Consult a reliable medical source or healthcare professional for accurate information.\n"
#                     "Would you like to ask about something else?"
#                 )

#             # Cache the response
#             self.response_cache[question_lower] = answer
#             return answer
#         except ValueError as e:
#             if "Rate limit exceeded" in str(e):
#                 if question_lower in self.fallback_responses:
#                     response = self.fallback_responses[question_lower]
#                     self.response_cache[question_lower] = response
#                     return response
#                 return (
#                     "## API Limit Reached\n"
#                     "- The daily request limit for the API has been reached.\n"
#                     "- Try common questions like flu symptoms, high blood pressure causes, anemia, heart attack symptoms, or kidney stones.\n"
#                     "- Wait until tomorrow when the API limit resets, or consult a healthcare professional for immediate advice.\n"
#                 )
#             raise e

#     def check_symptoms(self, symptoms):
#         if not symptoms.strip() or symptoms.lower() in ["i don't feel well", "not feeling well"]:
#             return (
#                 "## Symptom Information Needed\n"
#                 "- Specific symptoms are needed to provide a better analysis.\n"
#                 "- Examples include fever, pain, or fatigue.\n"
#                 "- Consult a doctor for a thorough evaluation.\n"
#             )
#         query = (
#             "You are a medical assistant providing general medical information based on reported symptoms. "
#             "Follow these formatting rules strictly for all responses:\n"
#             "- Use Markdown `##` for all section headings (e.g., `## Possible Conditions`). Do not use colons in headings (e.g., not `Possible Conditions:`), bold (`**`), single `#`, or other heading styles.\n"
#             "- Use `-` for bullet points, with exactly one item per bullet. Do not combine multiple items in a single bullet, use colons (e.g., not `- Condition: description`), or use other symbols like `*`, `•`, or `◦`.\n"
#             "- Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user. Keep text plain.\n"
#             "- Structure responses with a main heading (`##`) for the topic, followed by bullet points (`-`) for key details, and plain text for additional explanations.\n"
#             "- Do not include 'Assistant:', 'Bot:', or any similar prefixes in the response.\n"
#             "- Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "- Avoid common errors: do not use colons in headings or bullet points, do not combine multiple descriptions in one bullet, and do not use numbered lists or other bullet symbols.\n"
#             "- Respond only in English, regardless of context or input.\n"
#             "- Always recommend consulting a doctor for a professional diagnosis.\n"
#             f"Here are the user's symptoms: {symptoms}. What might this indicate based on medical guidelines? Provide general information and recommend consulting a doctor."
#         )
#         try:
#             result = self.qa_chain({"question": query, "chat_history": []})
#             answer = result["answer"]
#             return answer
#         except ValueError as e:
#             if "Rate limit exceeded" in str(e):
#                 return (
#                     "## API Limit Reached\n"
#                     "- The daily request limit for the API has been reached.\n"
#                     "- Try again tomorrow, or consult a healthcare professional for advice about your symptoms.\n"
#                 )
#             raise e

# from langchain_openai import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from dotenv import load_dotenv
# import os

# class ModelAPI:
#     def __init__(self, vector_store):
#         load_dotenv()
#         self.llm = ChatOpenAI(
#             model="deepseek/deepseek-chat:free",
#             openai_api_key=os.getenv("OPENROUTER_API_KEY"),
#             openai_api_base="https://openrouter.ai/api/v1"
#         )
#         self.qa_chain = ConversationalRetrievalChain.from_llm(
#             llm=self.llm,
#             retriever=vector_store.as_retriever(),
#             return_source_documents=True
#         )
#         # Cache for responses to reduce API calls
#         self.response_cache = {}
#         # Fallback responses for common questions when API limit is reached
#         self.fallback_responses = {
#             "what are the symptoms of the flu?": (
#                 "## Symptoms of the Flu\n"
#                 "- Fever often high, 100°F to 104°F or higher.\n"
#                 "- Chills and sweats.\n"
#                 "- Cough usually dry.\n"
#                 "- Sore throat.\n"
#                 "- Muscle aches or body aches.\n"
#                 "- Headache.\n"
#                 "- Fatigue or weakness.\n"
#                 "- Runny or stuffy nose.\n"
#                 "- Nausea, vomiting, or diarrhea more common in children.\n\n"
#                 "## Additional Information\n"
#                 "- Influenza affects 5-20% of the population annually.\n"
#                 "- Antiviral medications can reduce severity if taken early.\n"
#                 "Symptoms often come on suddenly and can range from mild to severe. If you suspect you have the flu, especially if you are at high risk for complications, consult a healthcare provider."
#             ),
#             "what causes high blood pressure?": (
#                 "## Causes of High Blood Pressure\n"
#                 "- Lifestyle factors like poor diet with high salt intake, obesity, lack of physical activity, excessive alcohol consumption, and smoking.\n"
#                 "- Underlying medical conditions such as diabetes, kidney disease, and hormonal disorders.\n"
#                 "- Genetic predisposition where a family history of hypertension increases risk.\n"
#                 "- Stress where chronic stress contributes to elevated blood pressure.\n"
#                 "- Aging as blood pressure often increases with age.\n\n"
#                 "## Additional Information\n"
#                 "- Hypertension affects over 1 billion people globally.\n"
#                 "- Regular monitoring can prevent complications like heart attack.\n"
#                 "Treatment often involves lifestyle changes and medications if needed. Would you like to know more about managing high blood pressure?"
#             ),
#             "what is anemia?": (
#                 "## What is Anemia\n"
#                 "- Anemia is a condition with abnormally low levels of healthy red blood cells or hemoglobin, which carries oxygen to tissues.\n"
#                 "- Fatigue or weakness.\n"
#                 "- Shortness of breath.\n"
#                 "- Pale skin.\n"
#                 "- Dizziness or lightheadedness.\n\n"
#                 "## Types of Anemia\n"
#                 "- Iron-deficiency anemia caused by lack of iron, often due to poor diet or blood loss.\n"
#                 "- Vitamin B12 deficiency anemia due to insufficient B12, often linked to diet or absorption issues.\n"
#                 "- Sickle cell anemia, a genetic condition where red blood cells are abnormally shaped.\n\n"
#                 "## Additional Information\n"
#                 "- Anemia affects about 25% of the global population.\n"
#                 "- Blood tests like CBC can confirm diagnosis.\n"
#                 "If you suspect anemia, a doctor can diagnose it with a blood test and recommend treatment like iron supplements or dietary changes."
#             ),
#             "what are symptoms of heart attack?": (
#                 "## Symptoms of a Heart Attack\n"
#                 "- Chest pain or discomfort often described as pressure, squeezing, or pain in the center or left side of the chest, lasting minutes or recurring.\n"
#                 "- Upper body discomfort in one or both arms, jaw, neck, back, or stomach.\n"
#                 "- Shortness of breath with or without chest pain.\n"
#                 "- Cold sweat, nausea, or lightheadedness accompanying chest discomfort.\n\n"
#                 "## Additional Information\n"
#                 "- Heart attacks are a leading cause of death worldwide.\n"
#                 "- Immediate treatment like aspirin can improve outcomes.\n"
#                 "If you experience these symptoms, especially chest pain or shortness of breath, seek emergency medical attention immediately."
#             ),
#             "what causes kidney stones?": (
#                 "## Causes of Kidney Stones\n"
#                 "- Dehydration where not drinking enough water leads to concentrated urine, increasing stone formation risk.\n"
#                 "- Diet with high intake of sodium, oxalate found in foods like spinach, or animal protein.\n"
#                 "- Medical conditions like hyperparathyroidism, gout, or urinary tract infections.\n"
#                 "- Family history with a genetic predisposition to kidney stones.\n"
#                 "- Obesity where higher body weight increases risk.\n"
#                 "- Certain medications like some diuretics or calcium-based antacids.\n\n"
#                 "## Additional Information\n"
#                 "- Kidney stones affect about 10% of people in their lifetime.\n"
#                 "- Imaging tests like CT scans can detect stones.\n"
#                 "Kidney stones can be made of different materials like calcium oxalate or uric acid, depending on the cause."
#             ),
#             "how can i prevent them?": (
#                 "## Preventing Kidney Stones\n"
#                 "- Stay hydrated by drinking plenty of water, aiming for 2-3 liters daily to dilute urine.\n"
#                 "- Adjust diet by reducing sodium, oxalate-rich foods like spinach, and animal protein, and eating more citrus fruits containing citrate to prevent stones.\n"
#                 "- Maintain a healthy weight as obesity increases risk, so regular exercise and a balanced diet help.\n"
#                 "- Monitor medical conditions like gout or urinary tract infections that contribute to stones.\n"
#                 "- Consult a doctor if you have a history of kidney stones for specific dietary changes or medications.\n\n"
#                 "## Additional Information\n"
#                 "- Citrate supplements may reduce stone formation.\n"
#                 "- Regular check-ups can catch stones early.\n"
#             )
#         }

#     def is_greeting(self, question):
#         greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
#         question_lower = question.lower().strip()
#         words = question_lower.split()
#         return any(word in greetings for word in words)

#     def check_repetitive_question(self, question, chat_history):
#         """Check if the question is similar to a previous one in chat history."""
#         question_lower = question.lower().strip()
#         if "blood pressure" in question_lower and ("cause" in question_lower or "what causes" in question_lower):
#             for prev_question, prev_answer in chat_history:
#                 prev_question_lower = prev_question.lower().strip()
#                 if "blood pressure" in prev_question_lower and (
#                         "cause" in prev_question_lower or "what causes" in prev_question_lower):
#                     return (
#                         "## Recap of High Blood Pressure Causes\n"
#                         "- Lifestyle factors like high salt intake, obesity, and smoking.\n"
#                         "- Medical conditions such as kidney disease or diabetes.\n"
#                         "- Genetic predisposition, stress, and aging.\n\n"
#                         "## Additional Information\n"
#                         "- Blood pressure screenings are recommended annually.\n"
#                         "- Medications like ACE inhibitors can manage hypertension.\n"
#                         "Would you like to know more about managing high blood pressure, or do you have a different question?"
#                     )
#         return None

#     def get_response(self, question, chat_history):
#         if self.is_greeting(question):
#             return "Hello! I'm your medical assistant. How can I help you with your health questions today?"

#         # Normalize question for cache and fallback lookup
#         question_lower = question.lower().strip()

#         # Check for repetitive questions
#         repetitive_response = self.check_repetitive_question(question, chat_history)
#         if repetitive_response:
#             return repetitive_response

#         # Check cache for previous response
#         if question_lower in self.response_cache:
#             return self.response_cache[question_lower]

#         # Check if question matches a fallback response
#         if question_lower in self.fallback_responses:
#             response = self.fallback_responses[question_lower]
#             self.response_cache[question_lower] = response
#             return response

#         # Add context from recent chat history
#         context = ""
#         if chat_history:
#             last_question, last_answer = chat_history[-1]
#             if "stress" in last_question.lower() and "manage" in question_lower:
#                 context = f"Previous question: {last_question}\nPrevious answer: {last_answer}\n"

#         modified_question = (
#             "You are a medical assistant providing accurate and detailed medical information. "
#             "Follow these formatting rules strictly for all responses:\n"
#             "- Use Markdown `##` for all section headings (e.g., `## Symptoms`). Do not use colons in headings (e.g., not `Symptoms:`), bold (`**`), single `#`, or other heading styles.\n"
#             "- Use `-` for bullet points, with exactly one item per bullet. Do not combine multiple items in a single bullet, use colons (e.g., not `- Item: description`), or use other symbols like `*`, `•`, or `◦`.\n"
#             "- Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user. Keep text plain.\n"
#             "- Structure responses with a main heading (`##`) for the topic, followed by bullet points (`-`) for key details, and plain text for additional explanations.\n"
#             "- Do not include 'Assistant:', 'Bot:', or any similar prefixes in the response.\n"
#             "- Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "- Avoid common errors: do not use colons in headings or bullet points, do not combine multiple descriptions in one bullet, and do not use numbered lists or other bullet symbols.\n"
#             "- Add some more medical information from your own knowledge and provide that information in a clear format to users.\n"
#             "- Respond only in English, regardless of context or input.\n"
#             "For simpler questions, include additional details like examples, types, or related information to enhance the response.\n"
#             f"{context}Here is the user's question: {question}"
#         )
#         try:
#             result = self.qa_chain({"question": modified_question, "chat_history": chat_history})
#             answer = result["answer"]

#             # Check if the vector store lacks information
#             if "provided context does not contain information" in answer.lower() or "not found in the context" in answer.lower():
#                 return (
#                     "## Information Not Available\n"
#                     "- The medical database does not contain details about this topic.\n"
#                     "- This question appears outside the scope of available information.\n"
#                     "- Consult a reliable medical source or healthcare professional for accurate information.\n\n"
#                     "## Additional Information\n"
#                     "- Online medical resources like WebMD can provide general guidance.\n"
#                     "- Local clinics offer consultations for personalized advice.\n"
#                     "Would you like to ask about something else?"
#                 )

#             # Cache the response
#             self.response_cache[question_lower] = answer
#             return answer
#         except ValueError as e:
#             if "Rate limit exceeded" in str(e):
#                 if question_lower in self.fallback_responses:
#                     response = self.fallback_responses[question_lower]
#                     self.response_cache[question_lower] = response
#                     return response
#                 return (
#                     "## API Limit Reached\n"
#                     "- The daily request limit for the API has been reached.\n"
#                     "- Try common questions like flu symptoms, high blood pressure causes, anemia, heart attack symptoms, or kidney stones.\n"
#                     "- Wait until tomorrow when the API limit resets, or consult a healthcare professional for immediate advice.\n\n"
#                     "## Additional Information\n"
#                     "- Many pharmacies offer free health screenings.\n"
#                     "- Emergency services are available for urgent concerns.\n"
#                 )
#             raise e

#     def check_symptoms(self, symptoms):
#         if not symptoms.strip() or symptoms.lower() in ["i don't feel well", "not feeling well"]:
#             return (
#                 "**Symptom Information Needed**\n"
#                 "- Specific symptoms are needed to provide a better analysis.\n"
#                 "- Examples include fever, pain, or fatigue.\n"
#                 "- Consult a doctor for a thorough evaluation.\n\n"
#                 "## Additional Information\n"
#                 "- Keeping a symptom diary can help doctors diagnose issues.\n"
#                 "- Urgent symptoms like chest pain require immediate attention.\n"
#             )
#         query = (
#             "You are a medical assistant providing general medical information based on reported symptoms. "
#             "Follow these formatting rules strictly for all responses:\n"
#             "- For the first section heading, use `**Possible Conditions**` (bolded) instead of `## Possible Conditions`. Use `##` for all subsequent section headings (e.g., `## Recommendations`). Do not use colons in headings (e.g., not `Possible Conditions:`), single `#`, or other heading styles.\n"
#             "- Use `-` for bullet points, with exactly one item per bullet. Do not combine multiple items in a single bullet, use colons (e.g., not `- Condition: description`), or use other symbols like `*`, `•`, or `◦`.\n"
#             "- Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user, except for the `**Possible Conditions**` heading.\n"
#             "- Structure responses with `**Possible Conditions**` as the first heading, followed by bullet points (`-`) for key details, subsequent headings with `##`, and plain text for additional explanations.\n"
#             "- Do not include 'Assistant:', 'Bot:', or any similar prefixes in the response.\n"
#             "- Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "- Avoid common errors: do not use colons in headings or bullet points, do not combine multiple descriptions in one bullet, and do not use numbered lists or other bullet symbols.\n"
#             "- Add some more medical information from your own knowledge and provide that information in a clear format to users.\n"
#             "- Respond only in English, regardless of context or input.\n"
#             "- Always recommend consulting a doctor for a professional diagnosis.\n"
#             f"Here are the user's symptoms: {symptoms}. What might this indicate based on medical guidelines? Provide general information and recommend consulting a doctor."
#         )
#         try:
#             result = self.qa_chain({"question": query, "chat_history": []})
#             answer = result["answer"]
#             return answer
#         except ValueError as e:
#             if "Rate limit exceeded" in str(e):
#                 return (
#                     "**API Limit Reached**\n"
#                     "- The daily request limit for the API has been reached.\n"
#                     "- Try again tomorrow, or consult a healthcare professional for advice about your symptoms.\n\n"
#                     "## Additional Information\n"
#                     "- Telemedicine services can provide quick consultations.\n"
#                     "- Local health clinics offer walk-in assessments.\n"
#                 )
#             raise e

# from langchain_openai import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from dotenv import load_dotenv
# import os

# class ModelAPI:
#     def __init__(self, vector_store):
#         load_dotenv()
#         self.llm = ChatOpenAI(
#             model="deepseek/deepseek-chat:free",
#             openai_api_key=os.getenv("OPENROUTER_API_KEY"),
#             openai_api_base="https://openrouter.ai/api/v1"
#         )
#         self.qa_chain = ConversationalRetrievalChain.from_llm(
#             llm=self.llm,
#             retriever=vector_store.as_retriever(),
#             return_source_documents=True
#         )
#         # Cache for responses to reduce API calls
#         self.response_cache = {}
#         # Fallback responses for common questions when API limit is reached
#         self.fallback_responses = {
#             "what are the symptoms of the flu?": (
#                 "## Symptoms of the Flu\n"
#                 "- Fever often high, 100°F to 104°F or higher.\n"
#                 "- Chills and sweats.\n"
#                 "- Cough usually dry.\n"
#                 "- Sore throat.\n"
#                 "- Muscle aches or body aches.\n"
#                 "- Headache.\n"
#                 "- Fatigue or weakness.\n"
#                 "- Runny or stuffy nose.\n"
#                 "- Nausea, vomiting, or diarrhea more common in children.\n\n"
#                 "## Additional Information\n"
#                 "- Influenza affects 5-20% of the population annually.\n"
#                 "- Antiviral medications can reduce severity if taken early.\n"
#                 "Symptoms often come on suddenly and can range from mild to severe. If you suspect you have the flu, especially if you are at high risk for complications, consult a healthcare provider."
#             ),
#             "what causes high blood pressure?": (
#                 "## Causes of High Blood Pressure\n"
#                 "- Lifestyle factors like poor diet with high salt intake, obesity, lack of physical activity, excessive alcohol consumption, and smoking.\n"
#                 "- Underlying medical conditions such as diabetes, kidney disease, and hormonal disorders.\n"
#                 "- Genetic predisposition where a family history of hypertension increases risk.\n"
#                 "- Stress where chronic stress contributes to elevated blood pressure.\n"
#                 "- Aging as blood pressure often increases with age.\n\n"
#                 "## Additional Information\n"
#                 "- Hypertension affects over 1 billion people globally.\n"
#                 "- Regular monitoring can prevent complications like heart attack.\n"
#                 "Treatment often involves lifestyle changes and medications if needed. Would you like to know more about managing high blood pressure?"
#             ),
#             "what is anemia?": (
#                 "## What is Anemia\n"
#                 "- Anemia is a condition with abnormally low levels of healthy red blood cells or hemoglobin, which carries oxygen to tissues.\n"
#                 "- Fatigue or weakness.\n"
#                 "- Shortness of breath.\n"
#                 "- Pale skin.\n"
#                 "- Dizziness or lightheadedness.\n\n"
#                 "## Types of Anemia\n"
#                 "- Iron-deficiency anemia caused by lack of iron, often due to poor diet or blood loss.\n"
#                 "- Vitamin B12 deficiency anemia due to insufficient B12, often linked to diet or absorption issues.\n"
#                 "- Sickle cell anemia, a genetic condition where red blood cells are abnormally shaped.\n\n"
#                 "## Additional Information\n"
#                 "- Anemia affects about 25% of the global population.\n"
#                 "- Blood tests like CBC can confirm diagnosis.\n"
#                 "If you suspect anemia, a doctor can diagnose it with a blood test and recommend treatment like iron supplements or dietary changes."
#             ),
#             "what are symptoms of heart attack?": (
#                 "## Symptoms of a Heart Attack\n"
#                 "- Chest pain or discomfort often described as pressure, squeezing, or pain in the center or left side of the chest, lasting minutes or recurring.\n"
#                 "- Upper body discomfort in one or both arms, jaw, neck, back, or stomach.\n"
#                 "- Shortness of breath with or without chest pain.\n"
#                 "- Cold sweat, nausea, or lightheadedness accompanying chest discomfort.\n\n"
#                 "## Additional Information\n"
#                 "- Heart attacks are a leading cause of death worldwide.\n"
#                 "- Immediate treatment like aspirin can improve outcomes.\n"
#                 "If you experience these symptoms, especially chest pain or shortness of breath, seek emergency medical attention immediately."
#             ),
#             "what causes kidney stones?": (
#                 "## Causes of Kidney Stones\n"
#                 "- Dehydration where not drinking enough water leads to concentrated urine, increasing stone formation risk.\n"
#                 "- Diet with high intake of sodium, oxalate found in foods like spinach, or animal protein.\n"
#                 "- Medical conditions like hyperparathyroidism, gout, or urinary tract infections.\n"
#                 "- Family history with a genetic predisposition to kidney stones.\n"
#                 "- Obesity where higher body weight increases risk.\n"
#                 "- Certain medications like some diuretics or calcium-based antacids.\n\n"
#                 "## Additional Information\n"
#                 "- Kidney stones affect about 10% of people in their lifetime.\n"
#                 "- Imaging tests like CT scans can detect stones.\n"
#                 "Kidney stones can be made of different materials like calcium oxalate or uric acid, depending on the cause."
#             ),
#             "how can i prevent them?": (
#                 "## Preventing Kidney Stones\n"
#                 "- Stay hydrated by drinking plenty of water, aiming for 2-3 liters daily to dilute urine.\n"
#                 "- Adjust diet by reducing sodium, oxalate-rich foods like spinach, and animal protein, and eating more citrus fruits containing citrate to prevent stones.\n"
#                 "- Maintain a healthy weight as obesity increases risk, so regular exercise and a balanced diet help.\n"
#                 "- Monitor medical conditions like gout or urinary tract infections that contribute to stones.\n"
#                 "- Consult a doctor if you have a history of kidney stones for specific dietary changes or medications.\n\n"
#                 "## Additional Information\n"
#                 "- Citrate supplements may reduce stone formation.\n"
#                 "- Regular check-ups can catch stones early.\n"
#             )
#         }

#     def is_greeting(self, question):
#         question_lower = question.lower().strip()
#         # Dictionary of specific greetings and their tailored responses
#         greeting_responses = {
#             "good morning": "Good morning! How can I assist with your medical questions today?",
#             "good afternoon": "Good afternoon! Ready to help with any health concerns you have.",
#             "good evening": "Good evening! Here to answer your medical questions before you wind down.",
#             "good night": "Good night! Feel free to ask any medical questions before you rest.",
#             "thank you": "You're welcome! Happy to help with any more health questions.",
#             "thanks": "You're welcome! Let me know if you have more medical queries."
#         }
#         # Check for specific greetings
#         for greeting, response in greeting_responses.items():
#             if greeting in question_lower:
#                 return response
#         # Generic greetings list
#         generic_greetings = ["hello", "hi", "hey"]
#         words = question_lower.split()
#         # Return generic response for generic greetings
#         if any(word in generic_greetings for word in words):
#             return "Hello! I'm your medical assistant. How can I help you with your health questions today?"
#         return None

#     def check_repetitive_question(self, question, chat_history):
#         """Check if the question is similar to a previous one in chat history."""
#         question_lower = question.lower().strip()
#         if "blood pressure" in question_lower and ("cause" in question_lower or "what causes" in question_lower):
#             for prev_question, prev_answer in chat_history:
#                 prev_question_lower = prev_question.lower().strip()
#                 if "blood pressure" in prev_question_lower and (
#                         "cause" in prev_question_lower or "what causes" in prev_question_lower):
#                     return (
#                         "## Recap of High Blood Pressure Causes\n"
#                         "- Lifestyle factors like high salt intake, obesity, and smoking.\n"
#                         "- Medical conditions such as kidney disease or diabetes.\n"
#                         "- Genetic predisposition, stress, and aging.\n\n"
#                         "## Additional Information\n"
#                         "- Blood pressure screenings are recommended annually.\n"
#                         "- Medications like ACE inhibitors can manage hypertension.\n"
#                         "Would you like to know more about managing high blood pressure, or do you have a different question?"
#                     )
#         return None

#     def get_response(self, question, chat_history):
#         # Check for greetings first
#         greeting_response = self.is_greeting(question)
#         if greeting_response:
#             return greeting_response

#         # Normalize question for cache and fallback lookup
#         question_lower = question.lower().strip()

#         # Check for repetitive questions
#         repetitive_response = self.check_repetitive_question(question, chat_history)
#         if repetitive_response:
#             return repetitive_response

#         # Check cache for previous response
#         if question_lower in self.response_cache:
#             return self.response_cache[question_lower]

#         # Check if question matches a fallback response
#         if question_lower in self.fallback_responses:
#             response = self.fallback_responses[question_lower]
#             self.response_cache[question_lower] = response
#             return response

#         # Add context from recent chat history
#         context = ""
#         if chat_history:
#             last_question, last_answer = chat_history[-1]
#             if "stress" in last_question.lower() and "manage" in question_lower:
#                 context = f"Previous question: {last_question}\nPrevious answer: {last_answer}\n"

#         modified_question = (
#             "You are a medical assistant providing accurate and detailed medical information. "
#             "Follow these formatting rules strictly for all responses:\n"
#             "- Use Markdown `##` for all section headings (e.g., `## Symptoms`). Do not use colons in headings (e.g., not `Symptoms:`), bold (`**`), single `#`, or other heading styles.\n"
#             "- Use `-` for bullet points, with exactly one item per bullet. Do not combine multiple items in a single bullet, use colons (e.g., not `- Item: description`), or use other symbols like `*`, `•`, or `◦`.\n"
#             "- Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user. Keep text plain.\n"
#             "- Structure responses with a main heading (`##`) for the topic, followed by bullet points (`-`) for key details, and plain text for additional explanations.\n"
#             "- Do not include 'Assistant:', 'Bot:', or any similar prefixes in the response.\n"
#             "- Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "- Avoid common errors: do not use colons in headings or bullet points, do not combine multiple descriptions in one bullet, and do not use numbered lists or other bullet symbols.\n"
#             "- Add some more medical information from your own knowledge and provide that information in a clear format to users.\n"
#             "- Respond only in English, regardless of context or input.\n"
#             "For simpler questions, include additional details like examples, types, or related information to enhance the response.\n"
#             f"{context}Here is the user's question: {question}"
#         )
#         try:
#             result = self.qa_chain({"question": modified_question, "chat_history": chat_history})
#             answer = result["answer"]

#             # Check if the vector store lacks information
#             if "provided context does not contain information" in answer.lower() or "not found in the context" in answer.lower():
#                 return (
#                     "## Information Not Available\n"
#                     "- The medical database does not contain details about this topic.\n"
#                     "- This question appears outside the scope of available information.\n"
#                     "- Consult a reliable medical source or healthcare professional for accurate information.\n\n"
#                     "## Additional Information\n"
#                     "- Online medical resources like WebMD can provide general guidance.\n"
#                     "- Local clinics offer consultations for personalized advice.\n"
#                     "Would you like to ask about something else?"
#                 )

#             # Cache the response
#             self.response_cache[question_lower] = answer
#             return answer
#         except ValueError as e:
#             if "Rate limit exceeded" in str(e):
#                 if question_lower in self.fallback_responses:
#                     response = self.fallback_responses[question_lower]
#                     self.response_cache[question_lower] = response
#                     return response
#                 return (
#                     "## API Limit Reached\n"
#                     "- The daily request limit for the API has been reached.\n"
#                     "- Try common questions like flu symptoms, high blood pressure causes, anemia, heart attack symptoms, or kidney stones.\n"
#                     "- Wait until tomorrow when the API limit resets, or consult a healthcare professional for immediate advice.\n\n"
#                     "## Additional Information\n"
#                     "- Many pharmacies offer free health screenings.\n"
#                     "- Emergency services are available for urgent concerns.\n"
#                 )
#             raise e

#     def check_symptoms(self, symptoms):
#         if not symptoms.strip() or symptoms.lower() in ["i don't feel well", "not feeling well"]:
#             return (
#                 "**Symptom Information Needed**\n"
#                 "- Specific symptoms are needed to provide a better analysis.\n"
#                 "- Examples include fever, pain, or fatigue.\n"
#                 "- Consult a doctor for a thorough evaluation.\n\n"
#                 "## Additional Information\n"
#                 "- Keeping a symptom diary can help doctors diagnose issues.\n"
#                 "- Urgent symptoms like chest pain require immediate attention.\n"
#             )
#         query = (
#             "You are a medical assistant providing general medical information based on reported symptoms. "
#             "Follow these formatting rules strictly for all responses:\n"
#             "- For the first section heading, use `**Possible Conditions**` (bolded) instead of `## Possible Conditions`. Use `##` for all subsequent section headings (e.g., `## Recommendations`). Do not use colons in headings (e.g., not `Possible Conditions:`), single `#`, or other heading styles.\n"
#             "- Use `-` for bullet points, with exactly one item per bullet. Do not combine multiple items in a single bullet, use colons (e.g., not `- Condition: description`), or use other symbols like `*`, `•`, or `◦`.\n"
#             "- Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user, except for the `**Possible Conditions**` heading.\n"
#             "- Structure responses with `**Possible Conditions**` as the first heading, followed by bullet points (`-`) for key details, subsequent headings with `##`, and plain text for additional explanations.\n"
#             "- Do not include 'Assistant:', 'Bot:', or any similar prefixes in the response.\n"
#             "- Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "- Avoid common errors: do not use colons in headings or bullet points, do not combine multiple descriptions in one bullet, and do not use numbered lists or other bullet symbols.\n"
#             "- Add some more medical information from your own knowledge and provide that information in a clear format to users.\n"
#             "- Respond only in English, regardless of context or input.\n"
#             "- Always recommend consulting a doctor for a professional diagnosis.\n"
#             f"Here are the user's symptoms: {symptoms}. What might this indicate based on medical guidelines? Provide general information and recommend consulting a doctor."
#         )
#         try:
#             result = self.qa_chain({"question": query, "chat_history": []})
#             answer = result["answer"]
#             return answer
#         except ValueError as e:
#             if "Rate limit exceeded" in str(e):
#                 return (
#                     "**API Limit Reached**\n"
#                     "- The daily request limit for the API has been reached.\n"
#                     "- Try again tomorrow, or consult a healthcare professional for advice about your symptoms.\n\n"
#                     "## Additional Information\n"
#                     "- Telemedicine services can provide quick consultations.\n"
#                     "- Local health clinics offer walk-in assessments.\n"
#                 )
#             raise e

# from langchain_openai import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from dotenv import load_dotenv
# import os

# class ModelAPI:
#     def __init__(self, vector_store):
#         load_dotenv()
#         self.llm = ChatOpenAI(
#             model="deepseek/deepseek-chat:free",
#             openai_api_key=os.getenv("OPENROUTER_API_KEY"),
#             openai_api_base="https://openrouter.ai/api/v1"
#         )
#         self.qa_chain = ConversationalRetrievalChain.from_llm(
#             llm=self.llm,
#             retriever=vector_store.as_retriever(),
#             return_source_documents=True
#         )
#         # Cache for responses to reduce API calls
#         self.response_cache = {}
#         # Fallback responses for common questions when API limit is reached
#         self.fallback_responses = {
#             "what are the symptoms of the flu?": (
#                 "## Symptoms of the Flu\n"
#                 "- Fever often high, 100°F to 104°F or higher.\n"
#                 "- Chills and sweats.\n"
#                 "- Cough usually dry.\n"
#                 "- Sore throat.\n"
#                 "- Muscle aches or body aches.\n"
#                 "- Headache.\n"
#                 "- Fatigue or weakness.\n"
#                 "- Runny or stuffy nose.\n"
#                 "- Nausea, vomiting, or diarrhea more common in children.\n\n"
#                 "## Additional Information\n"
#                 "- Influenza affects 5-20% of the population annually.\n"
#                 "- Antiviral medications can reduce severity if taken early.\n"
#                 "Symptoms often come on suddenly and can range from mild to severe. If you suspect you have the flu, especially if you are at high risk for complications, consult a healthcare provider."
#             ),
#             "what causes high blood pressure?": (
#                 "## Causes of High Blood Pressure\n"
#                 "- Lifestyle factors like poor diet with high salt intake, obesity, lack of physical activity, excessive alcohol consumption, and smoking.\n"
#                 "- Underlying medical conditions such as diabetes, kidney disease, and hormonal disorders.\n"
#                 "- Genetic predisposition where a family history of hypertension increases risk.\n"
#                 "- Stress where chronic stress contributes to elevated blood pressure.\n"
#                 "- Aging as blood pressure often increases with age.\n\n"
#                 "## Additional Information\n"
#                 "- Hypertension affects over 1 billion people globally.\n"
#                 "- Regular monitoring can prevent complications like heart attack.\n"
#                 "Treatment often involves lifestyle changes and medications if needed. Would you like to know more about managing high blood pressure?"
#             ),
#             "what is anemia?": (
#                 "## What is Anemia\n"
#                 "- Anemia is a condition with abnormally low levels of healthy red blood cells or hemoglobin, which carries oxygen to tissues.\n"
#                 "- Fatigue or weakness.\n"
#                 "- Shortness of breath.\n"
#                 "- Pale skin.\n"
#                 "- Dizziness or lightheadedness.\n\n"
#                 "## Types of Anemia\n"
#                 "- Iron-deficiency anemia caused by lack of iron, often due to poor diet or blood loss.\n"
#                 "- Vitamin B12 deficiency anemia due to insufficient B12, often linked to diet or absorption issues.\n"
#                 "- Sickle cell anemia, a genetic condition where red blood cells are abnormally shaped.\n\n"
#                 "## Additional Information\n"
#                 "- Anemia affects about 25% of the global population.\n"
#                 "- Blood tests like CBC can confirm diagnosis.\n"
#                 "If you suspect anemia, a doctor can diagnose it with a blood test and recommend treatment like iron supplements or dietary changes."
#             ),
#             "what are symptoms of heart attack?": (
#                 "## Symptoms of a Heart Attack\n"
#                 "- Chest pain or discomfort often described as pressure, squeezing, or pain in the center or left side of the chest, lasting minutes or recurring.\n"
#                 "- Upper body discomfort in one or both arms, jaw, neck, back, or stomach.\n"
#                 "- Shortness of breath with or without chest pain.\n"
#                 "- Cold sweat, nausea, or lightheadedness accompanying chest discomfort.\n\n"
#                 "## Additional Information\n"
#                 "- Heart attacks are a leading cause of death worldwide.\n"
#                 "- Immediate treatment like aspirin can improve outcomes.\n"
#                 "If you experience these symptoms, especially chest pain or shortness of breath, seek emergency medical attention immediately."
#             ),
#             "what causes kidney stones?": (
#                 "## Causes of Kidney Stones\n"
#                 "- Dehydration where not drinking enough water leads to concentrated urine, increasing stone formation risk.\n"
#                 "- Diet with high intake of sodium, oxalate found in foods like spinach, or animal protein.\n"
#                 "- Medical conditions like hyperparathyroidism, gout, or urinary tract infections.\n"
#                 "- Family history with a genetic predisposition to kidney stones.\n"
#                 "- Obesity where higher body weight increases risk.\n"
#                 "- Certain medications like some diuretics or calcium-based antacids.\n\n"
#                 "## Additional Information\n"
#                 "- Kidney stones affect about 10% of people in their lifetime.\n"
#                 "- Imaging tests like CT scans can detect stones.\n"
#                 "Kidney stones can be made of different materials like calcium oxalate or uric acid, depending on the cause."
#             ),
#             "how can i prevent them?": (
#                 "## Preventing Kidney Stones\n"
#                 "- Stay hydrated by drinking plenty of water, aiming for 2-3 liters daily to dilute urine.\n"
#                 "- Adjust diet by reducing sodium, oxalate-rich foods like spinach, and animal protein, and eating more citrus fruits containing citrate to prevent stones.\n"
#                 "- Maintain a healthy weight as obesity increases risk, so regular exercise and a balanced diet help.\n"
#                 "- Monitor medical conditions like gout or urinary tract infections that contribute to stones.\n"
#                 "- Consult a doctor if you have a history of kidney stones for specific dietary changes or medications.\n\n"
#                 "## Additional Information\n"
#                 "- Citrate supplements may reduce stone formation.\n"
#                 "- Regular check-ups can catch stones early.\n"
#             )
#         }

#     def is_greeting(self, question):
#         question_lower = question.lower().strip()
#         # Dictionary of specific greetings and their tailored responses
#         greeting_responses = {
#             "good morning": "Good morning! How can I assist with your medical questions today?",
#             "good afternoon": "Good afternoon! Ready to help with any health concerns you have.",
#             "good evening": "Good evening! Here to answer your medical questions before you wind down.",
#             "good night": "Good night! Feel free to ask any medical questions before you rest.",
#             "thank you": "You're welcome! Happy to help with any more health questions.",
#             "thanks": "You're welcome! Let me know if you have more medical queries."
#         }
#         # Check for specific greetings
#         for greeting, response in greeting_responses.items():
#             if greeting in question_lower:
#                 return response
#         # Generic greetings list
#         generic_greetings = ["hello", "hi", "hey"]
#         words = question_lower.split()
#         # Return generic response for generic greetings
#         if any(word in generic_greetings for word in words):
#             return "Hello! I'm your medical assistant. How can I help you with your health questions today?"
#         return None

#     def check_repetitive_question(self, question, chat_history):
#         """Check if the question is similar to a previous one in chat history."""
#         question_lower = question.lower().strip()
#         if "blood pressure" in question_lower and ("cause" in question_lower or "what causes" in question_lower):
#             for prev_question, prev_answer in chat_history:
#                 prev_question_lower = prev_question.lower().strip()
#                 if "blood pressure" in prev_question_lower and (
#                         "cause" in prev_question_lower or "what causes" in prev_question_lower):
#                     return (
#                         "## Recap of High Blood Pressure Causes\n"
#                         "- Lifestyle factors like high salt intake, obesity, and smoking.\n"
#                         "- Medical conditions such as kidney disease or diabetes.\n"
#                         "- Genetic predisposition, stress, and aging.\n\n"
#                         "## Additional Information\n"
#                         "- Blood pressure screenings are recommended annually.\n"
#                         "- Medications like ACE inhibitors can manage hypertension.\n"
#                         "Would you like to know more about managing high blood pressure, or do you have a different question?"
#                     )
#         return None

#     def get_response(self, question, chat_history):
#         # Check for greetings first
#         greeting_response = self.is_greeting(question)
#         if greeting_response:
#             return greeting_response

#         # Normalize question for cache and fallback lookup
#         question_lower = question.lower().strip()

#         # Check for repetitive questions
#         repetitive_response = self.check_repetitive_question(question, chat_history)
#         if repetitive_response:
#             return repetitive_response

#         # Check cache for previous response
#         if question_lower in self.response_cache:
#             return self.response_cache[question_lower]

#         # Check if question matches a fallback response
#         if question_lower in self.fallback_responses:
#             response = self.fallback_responses[question_lower]
#             self.response_cache[question_lower] = response
#             return response

#         # Add context from recent chat history
#         context = ""
#         if chat_history:
#             last_question, last_answer = chat_history[-1]
#             if "stress" in last_question.lower() and "manage" in question_lower:
#                 context = f"Previous question: {last_question}\nPrevious answer: {last_answer}\n"

#         modified_question = (
#             "You are a medical assistant providing accurate and detailed medical information. "
#             "Follow these formatting rules strictly for all responses:\n"
#             "- Use Markdown `##` for all section headings (e.g., `## Symptoms`). Do not use colons in headings (e.g., not `Symptoms:`), bold (`**`), single `#`, or other heading styles.\n"
#             "- Use `-` for bullet points, with exactly one item per bullet. Do not combine multiple items in a single bullet, use colons (e.g., not `- Item: description`), or use other symbols like `*`, `•`, or `◦`.\n"
#             "- Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user. Keep text plain.\n"
#             "- Structure responses with a main heading (`##`) for the topic, followed by bullet points (`-`) for key details, and plain text for additional explanations.\n"
#             "- Do not include 'Assistant:', 'Bot:', or any similar prefixes in the response.\n"
#             "- Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "- Avoid common errors: do not use colons in headings or bullet points, do not combine multiple descriptions in one bullet, and do not use numbered lists or other bullet symbols.\n"
#             "- Add some more medical information from your own knowledge and provide that information in a clear format to users.\n"
#             "- Ensure the response is formatted to be displayed in a justified text manner.\n"
#             "- Respond only in English, regardless of context or input.\n"
#             "For simpler questions, include additional details like examples, types, or related information to enhance the response.\n"
#             f"{context}Here is the user's question: {question}"
#         )
#         try:
#             result = self.qa_chain({"question": modified_question, "chat_history": chat_history})
#             answer = result["answer"]

#             # Check if the vector store lacks information
#             if "provided context does not contain information" in answer.lower() or "not found in the context" in answer.lower():
#                 return (
#                     "## Information Not Available\n"
#                     "- The medical database does not contain details about this topic.\n"
#                     "- This question appears outside the scope of available information.\n"
#                     "- Consult a reliable medical source or healthcare professional for accurate information.\n\n"
#                     "## Additional Information\n"
#                     "- Online medical resources like WebMD can provide general guidance.\n"
#                     "- Local clinics offer consultations for personalized advice.\n"
#                     "Would you like to ask about something else?"
#                 )

#             # Cache the response
#             self.response_cache[question_lower] = answer
#             return answer
#         except ValueError as e:
#             if "Rate limit exceeded" in str(e):
#                 if question_lower in self.fallback_responses:
#                     response = self.fallback_responses[question_lower]
#                     self.response_cache[question_lower] = response
#                     return response
#                 return (
#                     "## API Limit Reached\n"
#                     "- The daily request limit for the API has been reached.\n"
#                     "- Try common questions like flu symptoms, high blood pressure causes, anemia, heart attack symptoms, or kidney stones.\n"
#                     "- Wait until tomorrow when the API limit resets, or consult a healthcare professional for immediate advice.\n\n"
#                     "## Additional Information\n"
#                     "- Many pharmacies offer free health screenings.\n"
#                     "- Emergency services are available for urgent concerns.\n"
#                 )
#             raise e

#     def check_symptoms(self, symptoms):
#         if not symptoms.strip() or symptoms.lower() in ["i don't feel well", "not feeling well"]:
#             return (
#                 "**Symptom Information Needed**\n"
#                 "- Specific symptoms are needed to provide a better analysis.\n"
#                 "- Examples include fever, pain, or fatigue.\n"
#                 "- Consult a doctor for a thorough evaluation.\n\n"
#                 "## Additional Information\n"
#                 "- Keeping a symptom diary can help doctors diagnose issues.\n"
#                 "- Urgent symptoms like chest pain require immediate attention.\n"
#             )
#         query = (
#             "You are a medical assistant providing general medical information based on reported symptoms. "
#             "Follow these formatting rules strictly for all responses:\n"
#             "- For the first section heading, use `**Possible Conditions**` (bolded) instead of `## Possible Conditions`. Use `##` for all subsequent section headings (e.g., `## Recommendations`). Do not use colons in headings (e.g., not `Possible Conditions:`), single `#`, or other heading styles.\n"
#             "- Use `-` for bullet points, with exactly one item per bullet. Do not combine multiple items in a single bullet, use colons (e.g., not `- Condition: description`), or use other symbols like `*`, `•`, or `◦`.\n"
#             "- Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user, except for the `**Possible Conditions**` heading.\n"
#             "- Structure responses with `**Possible Conditions**` as the first heading, followed by bullet points (`-`) for key details, subsequent headings with `##`, and plain text for additional explanations.\n"
#             "- Do not include 'Assistant:', 'Bot:', or any similar prefixes in the response.\n"
#             "- Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "- Avoid common errors: do not use colons in headings or bullet points, do not combine multiple descriptions in one bullet, and do not use numbered lists or other bullet symbols.\n"
#             "- Add some more medical information from your own knowledge and provide that information in a clear format to users.\n"
#             "- Ensure the response is formatted to be displayed in a justified text manner.\n"
#             "- Respond only in English, regardless of context or input.\n"
#             "- Always recommend consulting a doctor for a professional diagnosis.\n"
#             f"Here are the user's symptoms: {symptoms}. What might this indicate based on medical guidelines? Provide general information and recommend consulting a doctor."
#         )
#         try:
#             result = self.qa_chain({"question": query, "chat_history": []})
#             answer = result["answer"]
#             return answer
#         except ValueError as e:
#             if "Rate limit exceeded" in str(e):
#                 return (
#                     "**API Limit Reached**\n"
#                     "- The daily request limit for the API has been reached.\n"
#                     "- Try again tomorrow, or consult a healthcare professional for advice about your symptoms.\n\n"
#                     "## Additional Information\n"
#                     "- Telemedicine services can provide quick consultations.\n"
#                     "- Local health clinics offer walk-in assessments.\n"
#                 )
#             raise e
# from langchain_openai import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from dotenv import load_dotenv
# import os

# class ModelAPI:
#     def __init__(self, vector_store):
#         load_dotenv()
#         self.llm = ChatOpenAI(
#             model="deepseek/deepseek-chat:free",
#             openai_api_key=os.getenv("OPENROUTER_API_KEY"),
#             openai_api_base="https://openrouter.ai/api/v1"
#         )
#         self.qa_chain = ConversationalRetrievalChain.from_llm(
#             llm=self.llm,
#             retriever=vector_store.as_retriever(),
#             return_source_documents=True
#         )
#         # Cache for responses to reduce API calls
#         self.response_cache = {}
#         # Fallback responses for common questions when API limit is reached
#         self.fallback_responses = {
#             "what are the symptoms of the flu?": (
#                 "## Symptoms of the Flu\n"
#                 "- Fever often high, 100°F to 104°F or higher.\n"
#                 "- Chills and sweats.\n"
#                 "- Cough usually dry.\n"
#                 "- Sore throat.\n"
#                 "- Muscle aches or body aches.\n"
#                 "- Headache.\n"
#                 "- Fatigue or weakness.\n"
#                 "- Runny or stuffy nose.\n"
#                 "- Nausea, vomiting, or diarrhea more common in children.\n\n"
#                 "## Additional Information\n"
#                 "- Influenza affects 5-20% of the population annually.\n"
#                 "- Antiviral medications can reduce severity if taken early.\n"
#                 "Symptoms often come on suddenly and can range from mild to severe. If you suspect you have the flu, especially if you are at high risk for complications, consult a healthcare provider."
#             ),
#             "what causes high blood pressure?": (
#                 "## Causes of High Blood Pressure\n"
#                 "- Lifestyle factors like poor diet with high salt intake, obesity, lack of physical activity, excessive alcohol consumption, and smoking.\n"
#                 "- Underlying medical conditions such as diabetes, kidney disease, and hormonal disorders.\n"
#                 "- Genetic predisposition where a family history of hypertension increases risk.\n"
#                 "- Stress where chronic stress contributes to elevated blood pressure.\n"
#                 "- Aging as blood pressure often increases with age.\n\n"
#                 "## Additional Information\n"
#                 "- Hypertension affects over 1 billion people globally.\n"
#                 "- Regular monitoring can prevent complications like heart attack.\n"
#                 "Treatment often involves lifestyle changes and medications if needed. Would you like to know more about managing high blood pressure?"
#             ),
#             "what is anemia?": (
#                 "## What is Anemia\n"
#                 "- Anemia is a condition with abnormally low levels of healthy red blood cells or hemoglobin, which carries oxygen to tissues.\n"
#                 "- Fatigue or weakness.\n"
#                 "- Shortness of breath.\n"
#                 "- Pale skin.\n"
#                 "- Dizziness or lightheadedness.\n\n"
#                 "## Types of Anemia\n"
#                 "- Iron-deficiency anemia caused by lack of iron, often due to poor diet or blood loss.\n"
#                 "- Vitamin B12 deficiency anemia due to insufficient B12, often linked to diet or absorption issues.\n"
#                 "- Sickle cell anemia, a genetic condition where red blood cells are abnormally shaped.\n\n"
#                 "## Additional Information\n"
#                 "- Anemia affects about 25% of the global population.\n"
#                 "- Blood tests like CBC can confirm diagnosis.\n"
#                 "If you suspect anemia, a doctor can diagnose it with a blood test and recommend treatment like iron supplements or dietary changes."
#             ),
#             "what are symptoms of heart attack?": (
#                 "## Symptoms of a Heart Attack\n"
#                 "- Chest pain or discomfort often described as pressure, squeezing, or pain in the center or left side of the chest, lasting minutes or recurring.\n"
#                 "- Upper body discomfort in one or both arms, jaw, neck, back, or stomach.\n"
#                 "- Shortness of breath with or without chest pain.\n"
#                 "- Cold sweat, nausea, or lightheadedness accompanying chest discomfort.\n\n"
#                 "## Additional Information\n"
#                 "- Heart attacks are a leading cause of death worldwide.\n"
#                 "- Immediate treatment like aspirin can improve outcomes.\n"
#                 "If you experience these symptoms, especially chest pain or shortness of breath, seek emergency medical attention immediately."
#             ),
#             "what causes kidney stones?": (
#                 "## Causes of Kidney Stones\n"
#                 "- Dehydration where not drinking enough water leads to concentrated urine, increasing stone formation risk.\n"
#                 "- Diet with high intake of sodium, oxalate found in foods like spinach, or animal protein.\n"
#                 "- Medical conditions like hyperparathyroidism, gout, or urinary tract infections.\n"
#                 "- Family history with a genetic predisposition to kidney stones.\n"
#                 "- Obesity where higher body weight increases risk.\n"
#                 "- Certain medications like some diuretics or calcium-based antacids.\n\n"
#                 "## Additional Information\n"
#                 "- Kidney stones affect about 10% of people in their lifetime.\n"
#                 "- Imaging tests like CT scans can detect stones.\n"
#                 "Kidney stones can be made of different materials like calcium oxalate or uric acid, depending on the cause."
#             ),
#             "how can i prevent them?": (
#                 "## Preventing Kidney Stones\n"
#                 "- Stay hydrated by drinking plenty of water, aiming for 2-3 liters daily to dilute urine.\n"
#                 "- Adjust diet by reducing sodium, oxalate-rich foods like spinach, and animal protein, and eating more citrus fruits containing citrate to prevent stones.\n"
#                 "- Maintain a healthy weight as obesity increases risk, so regular exercise and a balanced diet help.\n"
#                 "- Monitor medical conditions like gout or urinary tract infections that contribute to stones.\n"
#                 "- Consult a doctor if you have a history of kidney stones for specific dietary changes or medications.\n\n"
#                 "## Additional Information\n"
#                 "- Citrate supplements may reduce stone formation.\n"
#                 "- Regular check-ups can catch stones early.\n"
#             )
#         }
#         # Dictionary for common medical misspellings
#         self.spelling_corrections = {
#             "diabtes": "diabetes",
#             "diabetis": "diabetes",
#             "fevr": "fever",
#             "feaver": "fever",
#             "coff": "cough",
#             "coughh": "cough",
#             "sorethroat": "sore throat",
#             "sorthroat": "sore throat",
#             "hedache": "headache",
#             "headach": "headache",
#             "vertgo": "vertigo",
#             "vertigo": "vertigo",
#             "hypothyrodism": "hypothyroidism",
#             "hypothyroid": "hypothyroidism",
#             "asma": "asthma",
#             "astma": "asthma",
#             "chrone": "crohn",
#             "crohns": "crohn",
#             "ulcerativecolitis": "ulcerative colitis",
#             "ulcerativ colitis": "ulcerative colitis",
#             "join pain": "joint pain",
#             "jont pain": "joint pain",
#             "pheochromcytoma": "pheochromocytoma",
#             "pheochromocytma": "pheochromocytoma",
#             "fatige": "fatigue",
#             "fatgue": "fatigue",
#             "diziness": "dizziness",
#             "dizzyness": "dizziness",
#             "nausia": "nausea",
#             "nauseau": "nausea",
#             "shortnes of breath": "shortness of breath",
#             "shortnessofbreath": "shortness of breath",
#             "numness": "numbness",
#             "numbnes": "numbness",
#             "blured vision": "blurred vision",
#             "blur vision": "blurred vision"
#         }

#     def correct_spelling(self, text):
#         """Correct common misspellings in the input text."""
#         words = text.lower().split()
#         corrected_words = []
#         for word in words:
#             # Check if the word or a phrase containing it is in the spelling corrections
#             corrected = self.spelling_corrections.get(word, word)
#             for misspelling, correct in self.spelling_corrections.items():
#                 if misspelling in word:
#                     corrected = word.replace(misspelling, correct)
#                     break
#             corrected_words.append(corrected)
#         return " ".join(corrected_words)

#     def is_greeting(self, question):
#         question_lower = question.lower().strip()
#         # Dictionary of specific greetings and their tailored responses
#         greeting_responses = {
#             "good morning": "Good morning! How can I assist with your medical questions today?",
#             "good afternoon": "Good afternoon! Ready to help with any health concerns you have.",
#             "good evening": "Good evening! Here to answer your medical questions before you wind down.",
#             "good night": "Good night! Feel free to ask any medical questions before you rest.",
#             "thank you": "You're welcome! Happy to help with any more health questions.",
#             "thanks": "You're welcome! Let me know if you have more medical queries."
#         }
#         # Check for specific greetings
#         for greeting, response in greeting_responses.items():
#             if greeting in question_lower:
#                 return response
#         # Generic greetings list
#         generic_greetings = ["hello", "hi", "hey"]
#         words = question_lower.split()
#         # Return generic response for generic greetings
#         if any(word in generic_greetings for word in words):
#             return "Hello! I'm your medical assistant. How can I help you with your health questions today?"
#         return None

#     def check_repetitive_question(self, question, chat_history):
#         """Check if the question is similar to a previous one in chat history."""
#         question_lower = question.lower().strip()
#         if "blood pressure" in question_lower and ("cause" in question_lower or "what causes" in question_lower):
#             for prev_question, prev_answer in chat_history:
#                 prev_question_lower = prev_question.lower().strip()
#                 if "blood pressure" in prev_question_lower and (
#                         "cause" in prev_question_lower or "what causes" in prev_question_lower):
#                     return (
#                         "## Recap of High Blood Pressure Causes\n"
#                         "- Lifestyle factors like high salt intake, obesity, and smoking.\n"
#                         "- Medical conditions such as kidney disease or diabetes.\n"
#                         "- Genetic predisposition, stress, and aging.\n\n"
#                         "## Additional Information\n"
#                         "- Blood pressure screenings are recommended annually.\n"
#                         "- Medications like ACE inhibitors can manage hypertension.\n"
#                         "Would you like to know more about managing high blood pressure, or do you have a different question?"
#                     )
#         return None

#     def get_response(self, question, chat_history):
#         # Correct spelling in the question
#         corrected_question = self.correct_spelling(question)

#         # Check for greetings first
#         greeting_response = self.is_greeting(corrected_question)
#         if greeting_response:
#             return greeting_response

#         # Normalize question for cache and fallback lookup
#         question_lower = corrected_question.lower().strip()

#         # Check for repetitive questions
#         repetitive_response = self.check_repetitive_question(corrected_question, chat_history)
#         if repetitive_response:
#             return repetitive_response

#         # Check cache for previous response
#         if question_lower in self.response_cache:
#             return self.response_cache[question_lower]

#         # Check if question matches a fallback response
#         if question_lower in self.fallback_responses:
#             response = self.fallback_responses[question_lower]
#             self.response_cache[question_lower] = response
#             return response

#         # Add context from recent chat history
#         context = ""
#         if chat_history:
#             last_question, last_answer = chat_history[-1]
#             if "stress" in last_question.lower() and "manage" in question_lower:
#                 context = f"Previous question: {last_question}\nPrevious answer: {last_answer}\n"

#         modified_question = (
#             "You are a medical assistant providing accurate and detailed medical information. "
#             "Follow these formatting rules strictly for all responses:\n"
#             "- Use Markdown `##` for all section headings (e.g., `## Symptoms`). Do not use colons in headings (e.g., not `Symptoms:`), bold (`**`), single `#`, or other heading styles.\n"
#             "- Use `-` for bullet points, with exactly one item per bullet. Do not combine multiple items in a single bullet, use colons (e.g., not `- Item: description`), or use other symbols like `*`, `•`, or `◦`.\n"
#             "- Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user. Keep text plain.\n"
#             "- Structure responses with a main heading (`##`) for the topic, followed by bullet points (`-`) for key details, and plain text for additional explanations.\n"
#             "- Do not include 'Assistant:', 'Bot:', or any similar prefixes in the response.\n"
#             "- Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "- Avoid common errors: do not use colons in headings or bullet points, do not combine multiple descriptions in one bullet, and do not use numbered lists or other bullet symbols.\n"
#             "- Add some more medical information from your own knowledge and provide that information in a clear format to users.\n"
#             "- Ensure the response is formatted to be displayed in a justified text manner.\n"
#             "- Respond only in English, regardless of context or input.\n"
#             "For simpler questions, include additional details like examples, types, or related information to enhance the response.\n"
#             f"{context}Here is the user's question: {corrected_question}"
#         )
#         try:
#             result = self.qa_chain({"question": modified_question, "chat_history": chat_history})
#             answer = result["answer"]

#             # Check if the vector store lacks information
#             if "provided context does not contain information" in answer.lower() or "not found in the context" in answer.lower():
#                 return (
#                     "## Information Not Available\n"
#                     "- The medical database does not contain details about this topic.\n"
#                     "- This question appears outside the scope of available information.\n"
#                     "- Consult a reliable medical source or healthcare professional for accurate information.\n\n"
#                     "## Additional Information\n"
#                     "- Online medical resources like WebMD can provide general guidance.\n"
#                     "- Local clinics offer consultations for personalized advice.\n"
#                     "Would you like to ask about something else?"
#                 )

#             # Cache the response
#             self.response_cache[question_lower] = answer
#             return answer
#         except ValueError as e:
#             if "Rate limit exceeded" in str(e):
#                 if question_lower in self.fallback_responses:
#                     response = self.fallback_responses[question_lower]
#                     self.response_cache[question_lower] = response
#                     return response
#                 return (
#                     "## API Limit Reached\n"
#                     "- The daily request limit for the API has been reached.\n"
#                     "- Try common questions like flu symptoms, high blood pressure causes, anemia, heart attack symptoms, or kidney stones.\n"
#                     "- Wait until tomorrow when the API limit resets, or consult a healthcare professional for immediate advice.\n\n"
#                     "## Additional Information\n"
#                     "- Many pharmacies offer free health screenings.\n"
#                     "- Emergency services are available for urgent concerns.\n"
#                 )
#             raise e

#     def check_symptoms(self, symptoms):
#         # Correct spelling in the symptoms
#         corrected_symptoms = self.correct_spelling(symptoms)

#         if not corrected_symptoms.strip() or corrected_symptoms.lower() in ["i don't feel well", "not feeling well"]:
#             return (
#                 "**Symptom Information Needed**\n"
#                 "- Specific symptoms are needed to provide a better analysis.\n"
#                 "- Examples include fever, pain, or fatigue.\n"
#                 "- Consult a doctor for a thorough evaluation.\n\n"
#                 "## Additional Information\n"
#                 "- Keeping a symptom diary can help doctors diagnose issues.\n"
#                 "- Urgent symptoms like chest pain require immediate attention.\n"
#             )
#         query = (
#             "You are a medical assistant providing general medical information based on reported symptoms. "
#             "Follow these formatting rules strictly for all responses:\n"
#             "- For the first section heading, use `**Possible Conditions**` (bolded) instead of `## Possible Conditions`. Use `##` for all subsequent section headings (e.g., `## Recommendations`). Do not use colons in headings (e.g., not `Possible Conditions:`), single `#`, or other heading styles.\n"
#             "- Use `-` for bullet points, with exactly one item per bullet. Do not combine multiple items in a single bullet, use colons (e.g., not `- Condition: description`), or use other symbols like `*`, `•`, or `◦`.\n"
#             "- Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user, except for the `**Possible Conditions**` heading.\n"
#             "- Structure responses with `**Possible Conditions**` as the first heading, followed by bullet points (`-`) for key details, subsequent headings with `##`, and plain text for additional explanations.\n"
#             "- Do not include 'Assistant:', 'Bot:', or any similar prefixes in the response.\n"
#             "- Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "- Avoid common errors: do not use colons in headings or bullet points, do not combine multiple descriptions in one bullet, and do not use numbered lists or other bullet symbols.\n"
#             "- Add some more medical information from your own knowledge and provide that information in a clear format to users.\n"
#             "- Ensure the response is formatted to be displayed in a justified text manner.\n"
#             "- Respond only in English, regardless of context or input.\n"
#             "- Always recommend consulting a doctor for a professional diagnosis.\n"
#             f"Here are the user's symptoms: {corrected_symptoms}. What might this indicate based on medical guidelines? Provide general information and recommend consulting a doctor."
#         )
#         try:
#             result = self.qa_chain({"question": query, "chat_history": []})
#             answer = result["answer"]
#             return answer
#         except ValueError as e:
#             if "Rate limit exceeded" in str(e):
#                 return (
#                     "**API Limit Reached**\n"
#                     "- The daily request limit for the API has been reached.\n"
#                     "- Try again tomorrow, or consult a healthcare professional for advice about your symptoms.\n\n"
#                     "## Additional Information\n"
#                     "- Telemedicine services can provide quick consultations.\n"
#                     "- Local health clinics offer walk-in assessments.\n"
#                 )
#             raise e

# from langchain_openai import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from dotenv import load_dotenv
# import os
# import logging

# # Setup logging for Streamlit Cloud
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# class ModelAPI:
#     def __init__(self, vector_store):
#         load_dotenv()
#         api_key = os.getenv("OPENROUTER_API_KEY")
#         if not api_key:
#             logger.error("OPENROUTER_API_KEY is not set in .env file")
#             raise ValueError("Missing OPENROUTER_API_KEY. Please set it in the .env file.")
        
#         self.llm = ChatOpenAI(
#             model="deepseek/deepseek-chat:free",
#             openai_api_key=api_key,
#             openai_api_base="https://openrouter.ai/api/v1"
#         )
#         self.qa_chain = ConversationalRetrievalChain.from_llm(
#             llm=self.llm,
#             retriever=vector_store.as_retriever(),
#             return_source_documents=True
#         )
#         # Cache for responses to reduce API calls
#         self.response_cache = {}
#         # Fallback responses for common questions
#         self.fallback_responses = {
#             "what are the symptoms of the flu?": (
#                 "## Symptoms of the Flu\n"
#                 "- Fever often high, 100°F to 104°F or higher.\n"
#                 "- Chills and sweats.\n"
#                 "- Cough usually dry.\n"
#                 "- Sore throat.\n"
#                 "- Muscle aches or body aches.\n"
#                 "- Headache.\n"
#                 "- Fatigue or weakness.\n"
#                 "- Runny or stuffy nose.\n"
#                 "- Nausea, vomiting, or diarrhea more common in children.\n\n"
#                 "## Additional Information\n"
#                 "- Influenza affects 5-20% of the population annually.\n"
#                 "- Antiviral medications can reduce severity if taken early.\n"
#                 "Symptoms often come on suddenly and can range from mild to severe. If you suspect you have the flu, especially if you are at high risk for complications, consult a healthcare provider."
#             ),
#             "what causes high blood pressure?": (
#                 "## Causes of High Blood Pressure\n"
#                 "- Lifestyle factors like poor diet with high salt intake, obesity, lack of physical activity, excessive alcohol consumption, and smoking.\n"
#                 "- Underlying medical conditions such as diabetes, kidney disease, and hormonal disorders.\n"
#                 "- Genetic predisposition where a family history of hypertension increases risk.\n"
#                 "- Stress where chronic stress contributes to elevated blood pressure.\n"
#                 "- Aging as blood pressure often increases with age.\n\n"
#                 "## Additional Information\n"
#                 "- Hypertension affects over 1 billion people globally.\n"
#                 "- Regular monitoring can prevent complications like heart attack.\n"
#                 "Treatment often involves lifestyle changes and medications if needed. Would you like to know more about managing high blood pressure?"
#             ),
#             "what is anemia?": (
#                 "## What is Anemia\n"
#                 "- Anemia is a condition with abnormally low levels of healthy red blood cells or hemoglobin, which carries oxygen to tissues.\n"
#                 "- Fatigue or weakness.\n"
#                 "- Shortness of breath.\n"
#                 "- Pale skin.\n"
#                 "- Dizziness or lightheadedness.\n\n"
#                 "## Types of Anemia\n"
#                 "- Iron-deficiency anemia caused by lack of iron, often due to poor diet or blood loss.\n"
#                 "- Vitamin B12 deficiency anemia due to insufficient B12, often linked to diet or absorption issues.\n"
#                 "- Sickle cell anemia, a genetic condition where red blood cells are abnormally shaped.\n\n"
#                 "## Additional Information\n"
#                 "- Anemia affects about 25% of the global population.\n"
#                 "- Blood tests like CBC can confirm diagnosis.\n"
#                 "If you suspect anemia, a doctor can diagnose it with a blood test and recommend treatment like iron supplements or dietary changes."
#             ),
#             "what are symptoms of heart attack?": (
#                 "## Symptoms of a Heart Attack\n"
#                 "- Chest pain or discomfort often described as pressure, squeezing, or pain in the center or left side of the chest, lasting minutes or recurring.\n"
#                 "- Upper body discomfort in one or both arms, jaw, neck, back, or stomach.\n"
#                 "- Shortness of breath with or without chest pain.\n"
#                 "- Cold sweat, nausea, or lightheadedness accompanying chest discomfort.\n\n"
#                 "## Additional Information\n"
#                 "- Heart attacks are a leading cause of death worldwide.\n"
#                 "- Immediate treatment like aspirin can improve outcomes.\n"
#                 "If you experience these symptoms, especially chest pain or shortness of breath, seek emergency medical attention immediately."
#             ),
#             "what causes kidney stones?": (
#                 "## Causes of Kidney Stones\n"
#                 "- Dehydration where not drinking enough water leads to concentrated urine, increasing stone formation risk.\n"
#                 "- Diet with high intake of sodium, oxalate found in foods like spinach, or animal protein.\n"
#                 "- Medical conditions like hyperparathyroidism, gout, or urinary tract infections.\n"
#                 "- Family history with a genetic predisposition to kidney stones.\n"
#                 "- Obesity where higher body weight increases risk.\n"
#                 "- Certain medications like some diuretics or calcium-based antacids.\n\n"
#                 "## Additional Information\n"
#                 "- Kidney stones affect about 10% of people in their lifetime.\n"
#                 "- Imaging tests like CT scans can detect stones.\n"
#                 "Kidney stones can be made of different materials like calcium oxalate or uric acid, depending on the cause."
#             ),
#             "how can i prevent them?": (
#                 "## Preventing Kidney Stones\n"
#                 "- Stay hydrated by drinking plenty of water, aiming for 2-3 liters daily to dilute urine.\n"
#                 "- Adjust diet by reducing sodium, oxalate-rich foods like spinach, and animal protein, and eating more citrus fruits containing citrate to prevent stones.\n"
#                 "- Maintain a healthy weight as obesity increases risk, so regular exercise and a balanced diet help.\n"
#                 "- Monitor medical conditions like gout or urinary tract infections that contribute to stones.\n"
#                 "- Consult a doctor if you have a history of kidney stones for specific dietary changes or medications.\n\n"
#                 "## Additional Information\n"
#                 "- Citrate supplements may reduce stone formation.\n"
#                 "- Regular check-ups can catch stones early.\n"
#             )
#         }

#     def is_greeting(self, question):
#         question_lower = question.lower().strip()
#         greeting_responses = {
#             "good morning": "Good morning! How can I assist with your medical questions today?",
#             "good afternoon": "Good afternoon! Ready to help with any health concerns you have.",
#             "good evening": "Good evening! Here to answer your medical questions before you wind down.",
#             "good night": "Good night! Feel free to ask any medical questions before you rest.",
#             "thank you": "You're welcome! Happy to help with any more health questions.",
#             "thanks": "You're welcome! Let me know if you have more medical queries."
#         }
#         for greeting, response in greeting_responses.items():
#             if greeting in question_lower:
#                 return response
#         generic_greetings = ["hello", "hi", "hey"]
#         words = question_lower.split()
#         if any(word in generic_greetings for word in words):
#             return "Hello! I'm your medical assistant. How can I help you with your health questions today?"
#         return None

#     def check_repetitive_question(self, question, chat_history):
#         question_lower = question.lower().strip()
#         if "blood pressure" in question_lower and ("cause" in question_lower or "what causes" in question_lower):
#             for prev_question, prev_answer in chat_history:
#                 prev_question_lower = prev_question.lower().strip()
#                 if "blood pressure" in prev_question_lower and (
#                         "cause" in prev_question_lower or "what causes" in prev_question_lower):
#                     return (
#                         "## Recap of High Blood Pressure Causes\n"
#                         "- Lifestyle factors like high salt intake, obesity, and smoking.\n"
#                         "- Medical conditions such as kidney disease or diabetes.\n"
#                         "- Genetic predisposition, stress, and aging.\n\n"
#                         "## Additional Information\n"
#                         "- Blood pressure screenings are recommended annually.\n"
#                         "- Medications like ACE inhibitors can manage hypertension.\n"
#                         "Would you like to know more about managing high blood pressure, or do you have a different question?"
#                     )
#         return None

#     def get_response(self, question, chat_history):
#         # Check for greetings first
#         greeting_response = self.is_greeting(question)
#         if greeting_response:
#             return greeting_response

#         # Normalize question for cache and fallback lookup
#         question_lower = question.lower().strip()

#         # Check for repetitive questions
#         repetitive_response = self.check_repetitive_question(question, chat_history)
#         if repetitive_response:
#             return repetitive_response

#         # Check cache for previous response
#         if question_lower in self.response_cache:
#             return self.response_cache[question_lower]

#         # Check if question matches a fallback response
#         if question_lower in self.fallback_responses:
#             response = self.fallback_responses[question_lower]
#             self.response_cache[question_lower] = response
#             return response

#         # Add context from recent chat history
#         context = ""
#         if chat_history:
#             last_question, last_answer = chat_history[-1]
#             if "stress" in last_question.lower() and "manage" in question_lower:
#                 context = f"Previous question: {last_question}\nPrevious answer: {last_answer}\n"

#         modified_question = (
#             "You are a medical assistant providing accurate and detailed medical information. "
#             "Follow these formatting rules strictly for all responses:\n"
#             "- Use Markdown `##` for all section headings (e.g., `## Symptoms`). Headings must be left-aligned with no indentation or centering.\n"
#             "- Do not use colons in headings (e.g., not `Symptoms:`), bold (`**`), single `#`, or other heading styles.\n"
#             "- Use `-` for bullet points, with exactly one item per bullet. Do not combine multiple items in a single bullet, use colons (e.g., not `- Item: description`), or use other symbols like `*`, `•`, or `◦`.\n"
#             "- Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user. Keep text plain.\n"
#             "- Structure responses with a main heading (`##`) for the topic, followed by bullet points (`-`) for key details, and plain text for additional explanations.\n"
#             "- Do not include 'Assistant:', 'Bot:', or any similar prefixes in the response.\n"
#             "- Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "- Avoid common errors: do not use colons in headings or bullet points, do not combine multiple descriptions in one bullet, and do not use numbered lists or other bullet symbols.\n"
#             "- Use the user's exact input without correcting spellings, even if incorrect (e.g., 'diabtes' stays 'diabtes').\n"
#             "- Add some more medical information from your own knowledge and provide that information in a clear format to users.\n"
#             "- Ensure the response is formatted to be displayed in a justified text manner, with headings left-aligned.\n"
#             "- Respond only in English, regardless of context or input.\n"
#             "- For simpler questions, include additional details like examples, types, or related information to enhance the response.\n"
#             f"{context}Here is the user's question: {question}"
#         )
#         try:
#             result = self.qa_chain({"question": modified_question, "chat_history": chat_history})
#             answer = result["answer"]

#             # Check if the vector store lacks information
#             if "provided context does not contain information" in answer.lower() or "not found in the context" in answer.lower():
#                 return (
#                     "## Information Not Available\n"
#                     "- The medical database does not contain details about this topic.\n"
#                     "- This question appears outside the scope of available information.\n"
#                     "- Consult a reliable medical source or healthcare professional for accurate information.\n\n"
#                     "## Additional Information\n"
#                     "- Online medical resources like WebMD can provide general guidance.\n"
#                     "- Local clinics offer consultations for personalized advice.\n"
#                     "Would you like to ask about something else?"
#                 )

#             # Cache the response
#             self.response_cache[question_lower] = answer
#             return answer
#         except ValueError as e:
#             logger.error(f"API error in get_response: {str(e)}")
#             error_str = str(e).lower()
#             if "no instances available" in error_str or "503" in error_str:
#                 return (
#                     "## Model Unavailable\n"
#                     "- The medical database is temporarily unavailable due to high demand.\n"
#                     "- Try again later or with a different question.\n"
#                     "- Consult a healthcare professional for urgent needs.\n\n"
#                     "## Additional Information\n"
#                     "- Free models may have limited availability.\n"
#                     "- Check OpenRouter.ai ...(line truncated)
#             raise e

#     def check_symptoms(self, symptoms):
#         if not symptoms.strip() or symptoms.lower() in ["i don't feel well", "not feeling well"]:
#             return (
#                 "**Symptom Information Needed**\n"
#                 "- Specific symptoms are needed to provide a better analysis.\n"
#                 "- Examples include fever, pain, or fatigue.\n"
#                 "- Consult a doctor for a thorough evaluation.\n\n"
#                 "## Additional Information\n"
#                 "- Keeping a symptom diary can help doctors diagnose issues.\n"
#                 "- Urgent symptoms like chest pain require immediate attention.\n"
#             )
#         query = (
#             "You are a medical assistant providing general medical information based on reported symptoms. "
#             "Follow these formatting rules strictly for all responses:\n"
#             "- For the first section heading, use `**Possible Conditions**` (bolded) instead of `## Possible Conditions`. Use `##` for all subsequent section headings (e.g., `## Recommendations`). Headings must be left-aligned with no indentation or centering.\n"
#             "- Do not use colons in headings (e.g., not `Possible Conditions:`), single `#`, or other heading styles.\n"
#             "- Use `-` for bullet points, with exactly one item per bullet. Do not combine multiple items in a single bullet, use colons (e.g., not `- Condition: description`), or use other symbols like `*`, `•`, or `◦`.\n"
#             "- Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user, except for the `**Possible Conditions**` heading.\n"
#             "- Structure responses with `**Possible Conditions**` as the first heading, followed by bullet points (`-`) for key details, subsequent headings with `##`, and plain text for additional explanations.\n"
#             "- Do not include 'Assistant:', 'Bot:', or any similar prefixes in the response.\n"
#             "- Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "- Avoid common errors: do not use colons in headings or bullet points, do not combine multiple descriptions in one bullet, and do not use numbered lists or other bullet symbols.\n"
#             "- Use the user's exact input without correcting spellings, even if incorrect (e.g., 'fevr' stays 'fevr').\n"
#             "- Add some more medical information from your own knowledge and provide that information in a clear format to users.\n"
#             "- Ensure the response is formatted to be displayed in a justified text manner, with headings left-aligned.\n"
#             "- Respond only in English, regardless of context or input.\n"
#             "- Always recommend consulting a doctor for a professional diagnosis.\n"
#             f"Here are the user's symptoms: {symptoms}. What might this indicate based on medical guidelines? Provide general information and recommend consulting a doctor."
#         )
#         try:
#             result = self.qa_chain({"question": query, "chat_history": []})
#             answer = result["answer"]
#             return answer
#         except ValueError as e:
#             logger.error(f"API error in check_symptoms: {str(e)}")
#             error_str = str(e).lower()
#             if "no instances available" in error_str or "503" in error_str:
#                 return (
#                     "**Model Unavailable**\n"
#                     "- The medical database is temporarily unavailable due to high demand.\n"
#                     "- Try again later or with different symptoms.\n"
#                     "- Consult a healthcare professional for urgent needs.\n\n"
#                     "## Additional Information\n"
#                     "- Free models may have limited availability.\n"
#                     "- Check OpenRouter.ai for model status.\n"
#                 )
#             raise e

# from langchain_openai import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from dotenv import load_dotenv
# import os
# import logging

# # Setup logging for Streamlit Cloud
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# class ModelAPI:
#     def __init__(self, vector_store):
#         load_dotenv()
#         api_key = os.getenv("OPENROUTER_API_KEY")
#         if not api_key:
#             logger.error("OPENROUTER_API_KEY is not set in .env file")
#             raise ValueError("Missing OPENROUTER_API_KEY. Please set it in the .env file.")
        
#         self.llm = ChatOpenAI(
#             model="deepseek/deepseek-chat:free",
#             openai_api_key=api_key,
#             openai_api_base="https://openrouter.ai/api/v1"
#         )
#         self.qa_chain = ConversationalRetrievalChain.from_llm(
#             llm=self.llm,
#             retriever=vector_store.as_retriever(),
#             return_source_documents=True
#         )
#         # Cache for responses to reduce API calls
#         self.response_cache = {}
#         # Fallback responses for common questions
#         self.fallback_responses = {
#             "what are the symptoms of the flu?": (
#                 "## Symptoms of the Flu\n"
#                 "- Fever often high, 100°F to 104°F or higher.\n"
#                 "- Chills and sweats.\n"
#                 "- Cough usually dry.\n"
#                 "- Sore throat.\n"
#                 "- Muscle aches or body aches.\n"
#                 "- Headache.\n"
#                 "- Fatigue or weakness.\n"
#                 "- Runny or stuffy nose.\n"
#                 "- Nausea, vomiting, or diarrhea more common in children.\n\n"
#                 "## Additional Information\n"
#                 "- Influenza affects 5-20% of the population annually.\n"
#                 "- Antiviral medications can reduce severity if taken early.\n"
#                 "Symptoms often come on suddenly and can range from mild to severe. If you suspect you have the flu, especially if you are at high risk for complications, consult a healthcare provider."
#             ),
#             "what causes high blood pressure?": (
#                 "## Causes of High Blood Pressure\n"
#                 "- Lifestyle factors like poor diet with high salt intake, obesity, lack of physical activity, excessive alcohol consumption, and smoking.\n"
#                 "- Underlying medical conditions such as diabetes, kidney disease, and hormonal disorders.\n"
#                 "- Genetic predisposition where a family history of hypertension increases risk.\n"
#                 "- Stress where chronic stress contributes to elevated blood pressure.\n"
#                 "- Aging as blood pressure often increases with age.\n\n"
#                 "## Additional Information\n"
#                 "- Hypertension affects over 1 billion people globally.\n"
#                 "- Regular monitoring can prevent complications like heart attack.\n"
#                 "Treatment often involves lifestyle changes and medications if needed. Would you like to know more about managing high blood pressure?"
#             ),
#             "what is anemia?": (
#                 "## What is Anemia\n"
#                 "- Anemia is a condition with abnormally low levels of healthy red blood cells or hemoglobin, which carries oxygen to tissues.\n"
#                 "- Fatigue or weakness.\n"
#                 "- Shortness of breath.\n"
#                 "- Pale skin.\n"
#                 "- Dizziness or lightheadedness.\n\n"
#                 "## Types of Anemia\n"
#                 "- Iron-deficiency anemia caused by lack of iron, often due to poor diet or blood loss.\n"
#                 "- Vitamin B12 deficiency anemia due to insufficient B12, often linked to diet or absorption issues.\n"
#                 "- Sickle cell anemia, a genetic condition where red blood cells are abnormally shaped.\n\n"
#                 "## Additional Information\n"
#                 "- Anemia affects about 25% of the global population.\n"
#                 "- Blood tests like CBC can confirm diagnosis.\n"
#                 "If you suspect anemia, a doctor can diagnose it with a blood test and recommend treatment like iron supplements or dietary changes."
#             ),
#             "what are symptoms of heart attack?": (
#                 "## Symptoms of a Heart Attack\n"
#                 "- Chest pain or discomfort often described as pressure, squeezing, or pain in the center or left side of the chest, lasting minutes or recurring.\n"
#                 "- Upper body discomfort in one or both arms, jaw, neck, back, or stomach.\n"
#                 "- Shortness of breath with or without chest pain.\n"
#                 "- Cold sweat, nausea, or lightheadedness accompanying chest discomfort.\n\n"
#                 "## Additional Information\n"
#                 "- Heart attacks are a leading cause of death worldwide.\n"
#                 "- Immediate treatment like aspirin can improve outcomes.\n"
#                 "If you experience these symptoms, especially chest pain or shortness of breath, seek emergency medical attention immediately."
#             ),
#             "what causes kidney stones?": (
#                 "## Causes of Kidney Stones\n"
#                 "- Dehydration where not drinking enough water leads to concentrated urine, increasing stone formation risk.\n"
#                 "- Diet with high intake of sodium, oxalate found in foods like spinach, or animal protein.\n"
#                 "- Medical conditions like hyperparathyroidism, gout, or urinary tract infections.\n"
#                 "- Family history with a genetic predisposition to kidney stones.\n"
#                 "- Obesity where higher body weight increases risk.\n"
#                 "- Certain medications like some diuretics or calcium-based antacids.\n\n"
#                 "## Additional Information\n"
#                 "- Kidney stones affect about 10% of people in their lifetime.\n"
#                 "- Imaging tests like CT scans can detect stones.\n"
#                 "Kidney stones can be made of different materials like calcium oxalate or uric acid, depending on the cause."
#             ),
#             "how can i prevent them?": (
#                 "## Preventing Kidney Stones\n"
#                 "- Stay hydrated by drinking plenty of water, aiming for 2-3 liters daily to dilute urine.\n"
#                 "- Adjust diet by reducing sodium, oxalate-rich foods like spinach, and animal protein, and eating more citrus fruits containing citrate to prevent stones.\n"
#                 "- Maintain a healthy weight as obesity increases risk, so regular exercise and a balanced diet help.\n"
#                 "- Monitor medical conditions like gout or urinary tract infections that contribute to stones.\n"
#                 "- Consult a doctor if you have a history of kidney stones for specific dietary changes or medications.\n\n"
#                 "## Additional Information\n"
#                 "- Citrate supplements may reduce stone formation.\n"
#                 "- Regular check-ups can catch stones early.\n"
#             )
#         }

#     def is_greeting(self, question):
#         question_lower = question.lower().strip()
#         greeting_responses = {
#             "good morning": "Good morning! How can I assist with your medical questions today?",
#             "good afternoon": "Good afternoon! Ready to help with any health concerns you have.",
#             "good evening": "Good evening! Here to answer your medical questions before you wind down.",
#             "good night": "Good night! Feel free to ask any medical questions before you rest.",
#             "thank you": "You're welcome! Happy to help with any more health questions.",
#             "thanks": "You're welcome! Let me know if you have more medical queries."
#         }
#         for greeting, response in greeting_responses.items():
#             if greeting in question_lower:
#                 return response
#         generic_greetings = ["hello", "hi", "hey"]
#         words = question_lower.split()
#         if any(word in generic_greetings for word in words):
#             return "Hello! I'm your medical assistant. How can I help you with your health questions today?"
#         return None

#     def check_repetitive_question(self, question, chat_history):
#         question_lower = question.lower().strip()
#         if "blood pressure" in question_lower and ("cause" in question_lower or "what causes" in question_lower):
#             for prev_question, prev_answer in chat_history:
#                 prev_question_lower = prev_question.lower().strip()
#                 if "blood pressure" in prev_question_lower and (
#                         "cause" in prev_question_lower or "what causes" in prev_question_lower):
#                     return (
#                         "## Recap of High Blood Pressure Causes\n"
#                         "- Lifestyle factors like high salt intake, obesity, and smoking.\n"
#                         "- Medical conditions such as kidney disease or diabetes.\n"
#                         "- Genetic predisposition, stress, and aging.\n\n"
#                         "## Additional Information\n"
#                         "- Blood pressure screenings are recommended annually.\n"
#                         "- Medications like ACE inhibitors can manage hypertension.\n"
#                         "Would you like to know more about managing high blood pressure, or do you have a different question?"
#                     )
#         return None

#     def get_response(self, question, chat_history):
#         # Check for greetings first
#         greeting_response = self.is_greeting(question)
#         if greeting_response:
#             return greeting_response

#         # Normalize question for cache and fallback lookup
#         question_lower = question.lower().strip()

#         # Check for repetitive questions
#         repetitive_response = self.check_repetitive_question(question, chat_history)
#         if repetitive_response:
#             return repetitive_response

#         # Check cache for previous response
#         if question_lower in self.response_cache:
#             return self.response_cache[question_lower]

#         # Check if question matches a fallback response
#         if question_lower in self.fallback_responses:
#             response = self.fallback_responses[question_lower]
#             self.response_cache[question_lower] = response
#             return response

#         # Add context from recent chat history
#         context = ""
#         if chat_history:
#             last_question, last_answer = chat_history[-1]
#             if "stress" in last_question.lower() and "manage" in question_lower:
#                 context = f"Previous question: {last_question}\nPrevious answer: {last_answer}\n"

#         modified_question = (
#             "You are a medical assistant providing accurate and detailed medical information. "
#             "Follow these formatting rules strictly for all responses:\n"
#             "- Use Markdown `##` for all section headings (e.g., `## Symptoms`). Headings must be left-aligned with no indentation or centering.\n"
#             "- Do not use colons in headings (e.g., not `Symptoms:`), bold (`**`), single `#`, or other heading styles.\n"
#             "- Use `-` for bullet points, with exactly one item per bullet. Do not combine multiple items in a single bullet, use colons (e.g., not `- Item: description`), or use other symbols like `*`, `•`, or `◦`.\n"
#             "- Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user. Keep text plain.\n"
#             "- Structure responses with a main heading (`##`) for the topic, followed by bullet points (`-`) for key details, and plain text for additional explanations.\n"
#             "- Do not include 'Assistant:', 'Bot:', or any similar prefixes in the response.\n"
#             "- Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "- Avoid common errors: do not use colons in headings or bullet points, do not combine multiple descriptions in one bullet, and do not use numbered lists or other bullet symbols.\n"
#             "- Use the user's exact input without correcting spellings, even if incorrect (e.g., 'diabtes' stays 'diabtes').\n"
#             "- Add some more medical information from your own knowledge and provide that information in a clear format to users.\n"
#             "- Ensure the response is formatted to be displayed in a justified text manner, with headings left-aligned.\n"
#             "- Respond only in English, regardless of context or input.\n"
#             "- For simpler questions, include additional details like examples, types, or related information to enhance the response.\n"
#             f"{context}Here is the user's question: {question}"
#         )
#         try:
#             result = self.qa_chain({"question": modified_question, "chat_history": chat_history})
#             answer = result["answer"]

#             # Check if the vector store lacks information
#             if "provided context does not contain information" in answer.lower() or "not found in the context" in answer.lower():
#                 return (
#                     "## Information Not Available\n"
#                     "- The medical database does not contain details about this topic.\n"
#                     "- This question appears outside the scope of available information.\n"
#                     "- Consult a reliable medical source or healthcare professional for accurate information.\n\n"
#                     "## Additional Information\n"
#                     "- Online medical resources like WebMD can provide general guidance.\n"
#                     "- Local clinics offer consultations for personalized advice.\n"
#                     "Would you like to ask about something else?"
#                 )

#             # Cache the response
#             self.response_cache[question_lower] = answer
#             return answer
#         except ValueError as e:
#             logger.error(f"API error in get_response: {str(e)}")
#             error_str = str(e).lower()
#             if "no instances available" in error_str or "503" in error_str:
#                 return (
#                     "## Model Unavailable\n"
#                     "- The medical database is temporarily unavailable due to high demand.\n"
#                     "- Try again later or with a different question.\n"
#                     "- Consult a healthcare professional for urgent needs.\n\n"
#                     "## Additional Information\n"
#                     "- Free models may have limited availability.\n"
#                     "- Check OpenRouter.ai for model status.\n"
#                 )
#             raise e

#     def check_symptoms(self, symptoms):
#         if not symptoms.strip() or symptoms.lower() in ["i don't feel well", "not feeling well"]:
#             return (
#                 "**Symptom Information Needed**\n"
#                 "- Specific symptoms are needed to provide a better analysis.\n"
#                 "- Examples include fever, pain, or fatigue.\n"
#                 "- Consult a doctor for a thorough evaluation.\n\n"
#                 "## Additional Information\n"
#                 "- Keeping a symptom diary can help doctors diagnose issues.\n"
#                 "- Urgent symptoms like chest pain require immediate attention.\n"
#             )
#         query = (
#             "You are a medical assistant providing general medical information based on reported symptoms. "
#             "Follow these formatting rules strictly for all responses:\n"
#             "- For the first section heading, use `Possible Conditions` (bolded) instead of `## Possible Conditions`. Use `##` for all subsequent section headings (e.g., `## Recommendations`). Headings must be left-aligned with no indentation or centering.\n"
#             "- Do not use colons in headings (e.g., not `Possible Conditions:`), single `#`, or other heading styles.\n"
#             "- Use `-` for bullet points, with exactly one item per bullet. Do not combine multiple items in a single bullet, use colons (e.g., not `- Condition: description`), or use other symbols like `*`, `•`, or `◦`.\n"
#             "- Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user, except for the `**Possible Conditions**` heading.\n"
#             "- Structure responses with `**Possible Conditions**` as the first heading, followed by bullet points (`-`) for key details, subsequent headings with `##`, and plain text for additional explanations.\n"
#             "- Do not include 'Assistant:', 'Bot:', or any similar prefixes in the response.\n"
#             "- Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "- Avoid common errors: do not use colons in headings or bullet points, do not combine multiple descriptions in one bullet, and do not use numbered lists or other bullet symbols.\n"
#             "- Use the user's exact input without correcting spellings, even if incorrect (e.g., 'fevr' stays 'fevr').\n"
#             "- Add some more medical information from your own knowledge and provide that information in a clear format to users.\n"
#             "- Ensure the response is formatted to be displayed in a justified text manner, with headings left-aligned.\n"
#             "- Respond only in English, regardless of context or input.\n"
#             "- Always recommend consulting a doctor for a professional diagnosis.\n"
#             f"Here are the user's symptoms: {symptoms}. What might this indicate based on medical guidelines? Provide general information and recommend consulting a doctor."
#         )
#         try:
#             result = self.qa_chain({"question": query, "chat_history": []})
#             answer = result["answer"]
#             return answer
#         except ValueError as e:
#             logger.error(f"API error in check_symptoms: {str(e)}")
#             error_str = str(e).lower()
#             if "no instances available" in error_str or "503" in error_str:
#                 return (
#                     "**Model Unavailable**\n"
#                     "- The medical database is temporarily unavailable due to high demand.\n"
#                     "- Try again later or with different symptoms.\n"
#                     "- Consult a healthcare professional for urgent needs.\n\n"
#                     "## Additional Information\n"
#                     "- Free models may have limited availability.\n"
#                     "- Check OpenRouter.ai for model status.\n"
#                 )
#             raise e

# from langchain_openai import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from dotenv import load_dotenv
# import os
# import logging

# # Setup logging for Streamlit Cloud
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# class ModelAPI:
#     def __init__(self, vector_store):
#         load_dotenv()
#         api_key = os.getenv("OPENROUTER_API_KEY")
#         if not api_key:
#             logger.error("OPENROUTER_API_KEY is not set in .env file")
#             raise ValueError("Missing OPENROUTER_API_KEY. Please set it in the .env file.")
        
#         self.llm = ChatOpenAI(
#             model="deepseek/deepseek-chat:free",
#             openai_api_key=api_key,
#             openai_api_base="https://openrouter.ai/api/v1"
#         )
#         self.qa_chain = ConversationalRetrievalChain.from_llm(
#             llm=self.llm,
#             retriever=vector_store.as_retriever(),
#             return_source_documents=True
#         )
#         # Cache for responses to reduce API calls
#         self.response_cache = {}
#         # Fallback responses for common questions
#         self.fallback_responses = {
#             "what are the symptoms of the flu?": (
#                 "## Symptoms of the Flu\n"
#                 "- Fever often high, 100°F to 104°F or higher.\n"
#                 "- Chills and sweats.\n"
#                 "- Cough usually dry.\n"
#                 "- Sore throat.\n"
#                 "- Muscle aches or body aches.\n"
#                 "- Headache.\n"
#                 "- Fatigue or weakness.\n"
#                 "- Runny or stuffy nose.\n"
#                 "- Nausea, vomiting, or diarrhea more common in children.\n\n"
#                 "## Additional Information\n"
#                 "- Influenza affects 5-20% of the population annually.\n"
#                 "- Antiviral medications can reduce severity if taken early.\n"
#                 "Symptoms often come on suddenly and can range from mild to severe. If you suspect you have the flu, especially if you are at high risk for complications, consult a healthcare provider."
#             ),
#             "what causes high blood pressure?": (
#                 "## Causes of High Blood Pressure\n"
#                 "- Lifestyle factors like poor diet with high salt intake, obesity, lack of physical activity, excessive alcohol consumption, and smoking.\n"
#                 "- Underlying medical conditions such as diabetes, kidney disease, and hormonal disorders.\n"
#                 "- Genetic predisposition where a family history of hypertension increases risk.\n"
#                 "- Stress where chronic stress contributes to elevated blood pressure.\n"
#                 "- Aging as blood pressure often increases with age.\n\n"
#                 "## Additional Information\n"
#                 "- Hypertension affects over 1 billion people globally.\n"
#                 "- Regular monitoring can prevent complications like heart attack.\n"
#                 "Treatment often involves lifestyle changes and medications if needed. Would you like to know more about managing high blood pressure?"
#             ),
#             "what is anemia?": (
#                 "## What is Anemia\n"
#                 "- Anemia is a condition with abnormally low levels of healthy red blood cells or hemoglobin, which carries oxygen to tissues.\n"
#                 "- Fatigue or weakness.\n"
#                 "- Shortness of breath.\n"
#                 "- Pale skin.\n"
#                 "- Dizziness or lightheadedness.\n\n"
#                 "## Types of Anemia\n"
#                 "- Iron-deficiency anemia caused by lack of iron, often due to poor diet or blood loss.\n"
#                 "- Vitamin B12 deficiency anemia due to insufficient B12, often linked to diet or absorption issues.\n"
#                 "- Sickle cell anemia, a genetic condition where red blood cells are abnormally shaped.\n\n"
#                 "## Additional Information\n"
#                 "- Anemia affects about 25% of the global population.\n"
#                 "- Blood tests like CBC can confirm diagnosis.\n"
#                 "If you suspect anemia, a doctor can diagnose it with a blood test and recommend treatment like iron supplements or dietary changes."
#             ),
#             "what are symptoms of heart attack?": (
#                 "## Symptoms of a Heart Attack\n"
#                 "- Chest pain or discomfort often described as pressure, squeezing, or pain in the center or left side of the chest, lasting minutes or recurring.\n"
#                 "- Upper body discomfort in one or both arms, jaw, neck, back, or stomach.\n"
#                 "- Shortness of breath with or without chest pain.\n"
#                 "- Cold sweat, nausea, or lightheadedness accompanying chest discomfort.\n\n"
#                 "## Additional Information\n"
#                 "- Heart attacks are a leading cause of death worldwide.\n"
#                 "- Immediate treatment like aspirin can improve outcomes.\n"
#                 "If you experience these symptoms, especially chest pain or shortness of breath, seek emergency medical attention immediately."
#             ),
#             "what causes kidney stones?": (
#                 "## Causes of Kidney Stones\n"
#                 "- Dehydration where not drinking enough water leads to concentrated urine, increasing stone formation risk.\n"
#                 "- Diet with high intake of sodium, oxalate found in foods like spinach, or animal protein.\n"
#                 "- Medical conditions like hyperparathyroidism, gout, or urinary tract infections.\n"
#                 "- Family history with a genetic predisposition to kidney stones.\n"
#                 "- Obesity where higher body weight increases risk.\n"
#                 "- Certain medications like some diuretics or calcium-based antacids.\n\n"
#                 "## Additional Information\n"
#                 "- Kidney stones affect about 10% of people in their lifetime.\n"
#                 "- Imaging tests like CT scans can detect stones.\n"
#                 "Kidney stones can be made of different materials like calcium oxalate or uric acid, depending on the cause."
#             ),
#             "how can i prevent them?": (
#                 "## Preventing Kidney Stones\n"
#                 "- Stay hydrated by drinking plenty of water, aiming for 2-3 liters daily to dilute urine.\n"
#                 "- Adjust diet by reducing sodium, oxalate-rich foods like spinach, and animal protein, and eating more citrus fruits containing citrate to prevent stones.\n"
#                 "- Maintain a healthy weight as obesity increases risk, so regular exercise and a balanced diet help.\n"
#                 "- Monitor medical conditions like gout or urinary tract infections that contribute to stones.\n"
#                 "- Consult a doctor if you have a history of kidney stones for specific dietary changes or medications.\n\n"
#                 "## Additional Information\n"
#                 "- Citrate supplements may reduce stone formation.\n"
#                 "- Regular check-ups can catch stones early.\n"
#             )
#         }

#     def is_greeting(self, question):
#         question_lower = question.lower().strip()
#         greeting_responses = {
#             "good morning": "Good morning! How can I assist with your medical questions today?",
#             "good afternoon": "Good afternoon! Ready to help with any health concerns you have.",
#             "good evening": "Good evening! Here to answer your medical questions before you wind down.",
#             "good night": "Good night! Feel free to ask any medical questions before you rest.",
#             "thank you": "You're welcome! Happy to help with any more health questions.",
#             "thanks": "You're welcome! Let me know if you have more medical queries."
#         }
#         for greeting, response in greeting_responses.items():
#             if greeting in question_lower:
#                 return response
#         generic_greetings = ["hello", "hi", "hey"]
#         words = question_lower.split()
#         if any(word in generic_greetings for word in words):
#             return "Hello! I'm your medical assistant. How can I help you with your health questions today?"
#         return None

#     def check_repetitive_question(self, question, chat_history):
#         question_lower = question.lower().strip()
#         if "blood pressure" in question_lower and ("cause" in question_lower or "what causes" in question_lower):
#             for prev_question, prev_answer in chat_history:
#                 prev_question_lower = prev_question.lower().strip()
#                 if "blood pressure" in prev_question_lower and (
#                         "cause" in prev_question_lower or "what causes" in prev_question_lower):
#                     return (
#                         "## Recap of High Blood Pressure Causes\n"
#                         "- Lifestyle factors like high salt intake, obesity, and smoking.\n"
#                         "- Medical conditions such as kidney disease or diabetes.\n"
#                         "- Genetic predisposition, stress, and aging.\n\n"
#                         "## Additional Information\n"
#                         "- Blood pressure screenings are recommended annually.\n"
#                         "- Medications like ACE inhibitors can manage hypertension.\n"
#                         "Would you like to know more about managing high blood pressure, or do you have a different question?"
#                     )
#         return None

#     def get_response(self, question, chat_history):
#         # Check for greetings first
#         greeting_response = self.is_greeting(question)
#         if greeting_response:
#             return greeting_response

#         # Normalize question for cache and fallback lookup
#         question_lower = question.lower().strip()

#         # Check for repetitive questions
#         repetitive_response = self.check_repetitive_question(question, chat_history)
#         if repetitive_response:
#             return repetitive_response

#         # Check cache for previous response
#         if question_lower in self.response_cache:
#             return self.response_cache[question_lower]

#         # Check if question matches a fallback response
#         if question_lower in self.fallback_responses:
#             response = self.fallback_responses[question_lower]
#             self.response_cache[question_lower] = response
#             return response

#         # Add context from recent chat history
#         context = ""
#         if chat_history:
#             last_question, last_answer = chat_history[-1]
#             if "stress" in last_question.lower() and "manage" in question_lower:
#                 context = f"Previous question: {last_question}\nPrevious answer: {last_answer}\n"

#         modified_question = (
#             "You are a medical assistant providing accurate and detailed medical information. "
#             "Follow these formatting rules strictly for all responses:\n"
#             "- Use Markdown `##` for all section headings (e.g., `## Symptoms`). Headings must be left-aligned with no indentation, centering, or right-alignment.\n"
#             "- Do not use colons in headings (e.g., not `Symptoms:`), bold (`**`), single `#`, or other heading styles.\n"
#             "- Use `-` for bullet points, with exactly one item per bullet. Each bullet point MUST start on a new line, with no extra spaces before the `-`. Do not combine multiple items in a single bullet, use colons (e.g., not `- Item: description`), or use other symbols like `*`, `•`, or `◦`.\n"
#             "- Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user.\n"
#             "- Structure responses with a main heading (`##`) for the topic on its own line, followed by a newline, then bullet points (`-`) starting on the next line for key details, and plain text for additional explanations.\n"
#             "- Example of the desired format (note the newline after headings to ensure bullet points are on separate lines, and the response will be rendered as justified text except for headings):\n"
#             "```\n"
#             "## Symptoms of a Cold\n"
#             "- Runny or stuffy nose is common.\n"
#             "- Sore throat may occur early on.\n"
#             "- Cough is usually mild.\n"
#             "- Fatigue can persist for a few days.\n"
#             "## Additional Information\n"
#             "- Colds are caused by viruses like rhinovirus.\n"
#             "```\n"
#             "- Ensure the entire response, including bullet points and additional text, is formatted to be displayed in a justified text manner (except for headings, which remain left-aligned). The rendering system will handle the justification, but structure the response to support this by using proper newlines and bullet points.\n"
#             "- Do not include 'Assistant:', 'Bot:', or any similar prefixes in the response.\n"
#             "- Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "- Avoid common errors: do not use colons in headings or bullet points, do not combine multiple descriptions in one bullet, and do not use numbered lists or other bullet symbols.\n"
#             "- Use the user's exact input without correcting spellings, even if incorrect (e.g., 'diabtes' stays 'diabtes').\n"
#             "- Add some more medical information from your own knowledge and provide that information in a clear format to users.\n"
#             "- Respond only in English, regardless of context or input.\n"
#             "- For simpler questions, include additional details like examples, types, or related information to enhance the response.\n"
#             f"{context}Here is the user's question: {question}"
#         )
#         try:
#             result = self.qa_chain({"question": modified_question, "chat_history": chat_history})
#             answer = result["answer"]

#             # Check if the vector store lacks information
#             if "provided context does not contain information" in answer.lower() or "not found in the context" in answer.lower():
#                 return (
#                     "## Information Not Available\n"
#                     "- The medical database does not contain details about this topic.\n"
#                     "- This question appears outside the scope of available information.\n"
#                     "- Consult a reliable medical source or healthcare professional for accurate information.\n\n"
#                     "## Additional Information\n"
#                     "- Online medical resources like WebMD can provide general guidance.\n"
#                     "- Local clinics offer consultations for personalized advice.\n"
#                     "Would you like to ask about something else?"
#                 )

#             # Cache the response
#             self.response_cache[question_lower] = answer
#             return answer
#         except ValueError as e:
#             logger.error(f"API error in get_response: {str(e)}")
#             error_str = str(e).lower()
#             if "no instances available" in error_str or "503" in error_str:
#                 return (
#                     "## Model Unavailable\n"
#                     "- The medical database is temporarily unavailable due to high demand.\n"
#                     "- Try again later or with a different question.\n"
#                     "- Consult a healthcare professional for urgent needs.\n\n"
#                     "## Additional Information\n"
#                     "- Free models may have limited availability.\n"
#                     "- Check OpenRouter.ai for model status.\n"
#                 )
#             raise e

#     def check_symptoms(self, symptoms):
#         if not symptoms.strip() or symptoms.lower() in ["i don't feel well", "not feeling well"]:
#             return (
#                 "**Symptom Information Needed**\n"
#                 "- Specific symptoms are needed to provide a better analysis.\n"
#                 "- Examples include fever, pain, or fatigue.\n"
#                 "- Consult a doctor for a thorough evaluation.\n\n"
#                 "## Additional Information\n"
#                 "- Keeping a symptom diary can help doctors diagnose issues.\n"
#                 "- Urgent symptoms like chest pain require immediate attention.\n"
#             )
#         query = (
#             "You are a medical assistant providing general medical information based on reported symptoms. "
#             "Follow these formatting rules strictly for all responses:\n"
#             "- For the first section heading, use exactly `**Possible Conditions**` (Markdown bolded) instead of `## Possible Conditions` or any other variation. This heading must render as bold text in the output, with no visible Markdown asterisks (`**`). Use `##` for all subsequent section headings (e.g., `## Recommendations`). All headings must be left-aligned with no indentation, centering, or right-alignment.\n"
#             "- After the first heading `**Possible Conditions**`, you MUST insert a newline (`\n`) to ensure bullet points start on the next line. Bullet points must never appear on the same line as the heading. This is critical for proper formatting.\n"
#             "- Do not use colons in headings (e.g., not `Possible Conditions:`), single `#`, or other heading styles.\n"
#             "- Use `-` for bullet points, with exactly one item per bullet. Each bullet point MUST start on a new line, with no extra spaces before the `-`. Do not combine multiple items in a single bullet, use colons (e.g., not `- Condition: description`), or use other symbols like `*`, `•`, or `◦`.\n"
#             "- Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user, except for the `**Possible Conditions**` heading.\n"
#             "- Structure responses with `**Possible Conditions**` as the first heading on its own line, followed by a newline, then bullet points (`-`) starting on the next line for key details, subsequent headings with `##`, and plain text for additional explanations.\n"
#             "- Example of the desired format (note the newline after `**Possible Conditions**` to ensure bullet points are on separate lines, and the response will be rendered as justified text except for headings):\n"
#             "```\n"
#             "**Possible Conditions**\n"
#             "- These symptoms could indicate a common cold, which is a viral infection of the upper respiratory tract.\n"
#             "- They might also suggest influenza (flu), a more severe viral illness that often includes fever and cough.\n"
#             "- In some cases, these symptoms could be related to a respiratory infection such as bronchitis or pneumonia.\n"
#             "- COVID-19, caused by the SARS-CoV-2 virus, can also present with fever, cough, and cold-like symptoms.\n"
#             "## Recommendations\n"
#             "- Rest and stay hydrated to support recovery.\n"
#             "```\n"
#             "- Ensure the entire response, including bullet points and additional text, is formatted to be displayed in a justified text manner (except for headings, which remain left-aligned). The rendering system will handle the justification, but structure the response to support this by using proper newlines and bullet points.\n"
#             "- Do not include 'Assistant:', 'Bot:', or any similar prefixes in the response.\n"
#             "- Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "- Avoid common errors: do not use colons in headings or bullet points, do not combine multiple descriptions in one bullet, and do not use numbered lists or other bullet symbols.\n"
#             "- Use the user's exact input without correcting spellings, even if incorrect (e.g., 'fevr' stays 'fevr').\n"
#             "- Add some more medical information from your own knowledge and provide that information in a clear format to users.\n"
#             "- Respond only in English, regardless of context or input.\n"
#             "- Always recommend consulting a doctor for a professional diagnosis.\n"
#             f"Here are the user's symptoms: {symptoms}. What might this indicate based on medical guidelines? Provide general information and recommend consulting a doctor."
#         )
#         try:
#             result = self.qa_chain({"question": query, "chat_history": []})
#             answer = result["answer"]
#             return answer
#         except ValueError as e:
#             logger.error(f"API error in check_symptoms: {str(e)}")
#             error_str = str(e).lower()
#             if "no instances available" in error_str or "503" in error_str:
#                 return (
#                     "**Model Unavailable**\n"
#                     "- The medical database is temporarily unavailable due to high demand.\n"
#                     "- Try again later or with different symptoms.\n"
#                     "- Consult a healthcare professional for urgent needs.\n\n"
#                     "## Additional Information\n"
#                     "- Free models may have limited availability.\n"
#                     "- Check OpenRouter.ai for model status.\n"
#                 )
#             raise e

# from langchain_openai import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from dotenv import load_dotenv
# import os
# import logging

# # Setup logging for Streamlit Cloud
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# class ModelAPI:
#     def __init__(self, vector_store):
#         load_dotenv()
#         api_key = os.getenv("OPENROUTER_API_KEY")
#         if not api_key:
#             logger.error("OPENROUTER_API_KEY is not set in .env file")
#             raise ValueError("Missing OPENROUTER_API_KEY. Please set it in the .env file.")
        
#         self.llm = ChatOpenAI(
#             model="deepseek/deepseek-chat:free",
#             openai_api_key=api_key,
#             openai_api_base="https://openrouter.ai/api/v1"
#         )
#         self.qa_chain = ConversationalRetrievalChain.from_llm(
#             llm=self.llm,
#             retriever=vector_store.as_retriever(),
#             return_source_documents=True
#         )
#         # Cache for responses to reduce API calls
#         self.response_cache = {}
#         # Fallback responses for common questions
#         self.fallback_responses = {
#             "what are the symptoms of the flu?": (
#                 "## Symptoms of the Flu\n"
#                 "• Fever often high, 100°F to 104°F or higher.\n"
#                 "• Chills and sweats.\n"
#                 "• Cough usually dry.\n"
#                 "• Sore throat.\n"
#                 "• Muscle aches or body aches.\n"
#                 "• Headache.\n"
#                 "• Fatigue or weakness.\n"
#                 "• Runny or stuffy nose.\n"
#                 "• Nausea, vomiting, or diarrhea more common in children.\n\n"
#                 "## Additional Information\n"
#                 "• Influenza affects 5-20% of the population annually.\n"
#                 "• Antiviral medications can reduce severity if taken early.\n"
#                 "Symptoms often come on suddenly and can range from mild to severe. If you suspect you have the flu, especially if you are at high risk for complications, consult a healthcare provider."
#             ),
#             "what causes high blood pressure?": (
#                 "## Causes of High Blood Pressure\n"
#                 "• Lifestyle factors like poor diet with high salt intake, obesity, lack of physical activity, excessive alcohol consumption, and smoking.\n"
#                 "• Underlying medical conditions such as diabetes, kidney disease, and hormonal disorders.\n"
#                 "• Genetic predisposition where a family history of hypertension increases risk.\n"
#                 "• Stress where chronic stress contributes to elevated blood pressure.\n"
#                 "• Aging as blood pressure often increases with age.\n\n"
#                 "## Additional Information\n"
#                 "• Hypertension affects over 1 billion people globally.\n"
#                 "• Regular monitoring can prevent complications like heart attack.\n"
#                 "Treatment often involves lifestyle changes and medications if needed. Would you like to know more about managing high blood pressure?"
#             ),
#             "what is anemia?": (
#                 "## What is Anemia\n"
#                 "• Anemia is a condition with abnormally low levels of healthy red blood cells or hemoglobin, which carries oxygen to tissues.\n"
#                 "• Fatigue or weakness.\n"
#                 "• Shortness of breath.\n"
#                 "• Pale skin.\n"
#                 "• Dizziness or lightheadedness.\n\n"
#                 "## Types of Anemia\n"
#                 "• Iron-deficiency anemia caused by lack of iron, often due to poor diet or blood loss.\n"
#                 "• Vitamin B12 deficiency anemia due to insufficient B12, often linked to diet or absorption issues.\n"
#                 "• Sickle cell anemia, a genetic condition where red blood cells are abnormally shaped.\n\n"
#                 "## Additional Information\n"
#                 "• Anemia affects about 25% of the global population.\n"
#                 "• Blood tests like CBC can confirm diagnosis.\n"
#                 "If you suspect anemia, a doctor can diagnose it with a blood test and recommend treatment like iron supplements or dietary changes."
#             ),
#             "what are symptoms of heart attack?": (
#                 "## Symptoms of a Heart Attack\n"
#                 "• Chest pain or discomfort often described as pressure, squeezing, or pain in the center or left side of the chest, lasting minutes or recurring.\n"
#                 "• Upper body discomfort in one or both arms, jaw, neck, back, or stomach.\n"
#                 "• Shortness of breath with or without chest pain.\n"
#                 "• Cold sweat, nausea, or lightheadedness accompanying chest discomfort.\n\n"
#                 "## Additional Information\n"
#                 "• Heart attacks are a leading cause of death worldwide.\n"
#                 "• Immediate treatment like aspirin can improve outcomes.\n"
#                 "If you experience these symptoms, especially chest pain or shortness of breath, seek emergency medical attention immediately."
#             ),
#             "what causes kidney stones?": (
#                 "## Causes of Kidney Stones\n"
#                 "• Dehydration where not drinking enough water leads to concentrated urine, increasing stone formation risk.\n"
#                 "• Diet with high intake of sodium, oxalate found in foods like spinach, or animal protein.\n"
#                 "• Medical conditions like hyperparathyroidism, gout, or urinary tract infections.\n"
#                 "• Family history with a genetic predisposition to kidney stones.\n"
#                 "• Obesity where higher body weight increases risk.\n"
#                 "• Certain medications like some diuretics or calcium-based antacids.\n\n"
#                 "## Additional Information\n"
#                 "• Kidney stones affect about 10% of people in their lifetime.\n"
#                 "• Imaging tests like CT scans can detect stones.\n"
#                 "Kidney stones can be made of different materials like calcium oxalate or uric acid, depending on the cause."
#             ),
#             "how can i prevent them?": (
#                 "## Preventing Kidney Stones\n"
#                 "• Stay hydrated by drinking plenty of water, aiming for 2-3 liters daily to dilute urine.\n"
#                 "• Adjust diet by reducing sodium, oxalate-rich foods like spinach, and animal protein, and eating more citrus fruits containing citrate to prevent stones.\n"
#                 "• Maintain a healthy weight as obesity increases risk, so regular exercise and a balanced diet help.\n"
#                 "• Monitor medical conditions like gout or urinary tract infections that contribute to stones.\n"
#                 "• Consult a doctor if you have a history of kidney stones for specific dietary changes or medications.\n\n"
#                 "## Additional Information\n"
#                 "• Citrate supplements may reduce stone formation.\n"
#                 "• Regular check-ups can catch stones early.\n"
#             )
#         }

#     def is_greeting(self, question):
#         question_lower = question.lower().strip()
#         greeting_responses = {
#             "good morning": "Good morning! How can I assist with your medical questions today?",
#             "good afternoon": "Good afternoon! Ready to help with any health concerns you have.",
#             "good evening": "Good evening! Here to answer your medical questions before you wind down.",
#             "good night": "Good night! Feel free to ask any medical questions before you rest.",
#             "thank you": "You're welcome! Happy to help with any more health questions.",
#             "thanks": "You're welcome! Let me know if you have more medical queries."
#         }
#         for greeting, response in greeting_responses.items():
#             if greeting in question_lower:
#                 return response
#         generic_greetings = ["hello", "hi", "hey"]
#         words = question_lower.split()
#         if any(word in generic_greetings for word in words):
#             return "Hello! I'm your medical assistant. How can I help you with your health questions today?"
#         return None

#     def check_repetitive_question(self, question, chat_history):
#         question_lower = question.lower().strip()
#         if "blood pressure" in question_lower and ("cause" in question_lower or "what causes" in question_lower):
#             for prev_question, prev_answer in chat_history:
#                 prev_question_lower = prev_question.lower().strip()
#                 if "blood pressure" in prev_question_lower and (
#                         "cause" in prev_question_lower or "what causes" in prev_question_lower):
#                     return (
#                         "## Recap of High Blood Pressure Causes\n"
#                         "• Lifestyle factors like high salt intake, obesity, and smoking.\n"
#                         "• Medical conditions such as kidney disease or diabetes.\n"
#                         "• Genetic predisposition, stress, and aging.\n\n"
#                         "## Additional Information\n"
#                         "• Blood pressure screenings are recommended annually.\n"
#                         "• Medications like ACE inhibitors can manage hypertension.\n"
#                         "Would you like to know more about managing high blood pressure, or do you have a different question?"
#                     )
#         return None

#     def get_response(self, question, chat_history):
#         # Check for greetings first
#         greeting_response = self.is_greeting(question)
#         if greeting_response:
#             return greeting_response

#         # Normalize question for cache and fallback lookup
#         question_lower = question.lower().strip()

#         # Check for repetitive questions
#         repetitive_response = self.check_repetitive_question(question, chat_history)
#         if repetitive_response:
#             return repetitive_response

#         # Check cache for previous response
#         if question_lower in self.response_cache:
#             return self.response_cache[question_lower]

#         # Check if question matches a fallback response
#         if question_lower in self.fallback_responses:
#             response = self.fallback_responses[question_lower]
#             self.response_cache[question_lower] = response
#             return response

#         # Add context from recent chat history
#         context = ""
#         if chat_history:
#             last_question, last_answer = chat_history[-1]
#             if "stress" in last_question.lower() and "manage" in question_lower:
#                 context = f"Previous question: {last_question}\nPrevious answer: {last_answer}\n"

#         modified_question = (
#             "Role:\n"
#             "You are a medical assistant providing accurate and detailed medical information.\n\n"
#             "Formatting Rules:\n"
#             "• Use Markdown `##` for all section headings (e.g., `## Symptoms`). Headings must start from the left side only, with no indentation, centering, or right-alignment.\n"
#             "• Insert a newline (`\n`) after each heading to ensure content (bullet points or text) starts on the next line. Content must not be on the same line as the heading.\n"
#             "• Use `•` for bullet points, with one item per bullet. Each bullet point must start on a new line, with no extra spaces before the `•`. Insert a newline (`\n`) after each bullet point to ensure they do not combine (e.g., not `• Item 1. • Item 2.`). Do not combine multiple items in a single bullet, use colons (e.g., not `• Item: description`), or use other symbols like `-`, `*`, or `◦`.\n"
#             "• Ensure the entire response, including bullet points and additional text, is formatted to be displayed in a justified text manner (except for headings, which must start from the left side only). The rendering system will handle justification, but structure the response with proper newlines and bullet points.\n"
#             "• Apply these formatting rules consistently to all responses, whether generated using the vector database, the model's own knowledge, or a combination of both.\n"
#             "• Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user.\n"
#             "• Do not use colons in headings (e.g., not `Symptoms:`), single `#`, or other heading styles.\n"
#             "• Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "• Do not include 'Assistant:', 'Bot:', or similar prefixes in the response.\n"
#             "• Avoid errors: do not use colons in bullet points, combine multiple descriptions in one bullet, or use numbered lists.\n\n"
#             "Example:\n"
#             "```\n"
#             "## Symptoms of a Cold\n"
#             "• Runny or stuffy nose is common.\n"
#             "• Sore throat may occur early on.\n"
#             "• Cough is usually mild.\n"
#             "• Fatigue can persist for a few days.\n"
#             "## Additional Information\n"
#             "• Colds are caused by viruses like rhinovirus.\n"
#             "Consult a doctor if symptoms worsen.\n"
#             "```\n\n"
#             "Instructions:\n"
#             "• Use the user's exact input without correcting spellings, even if incorrect (e.g., 'diabtes' stays 'diabtes').\n"
#             "• Add extra medical information from your knowledge in a clear format, following the formatting rules above.\n"
#             "• Respond only in English, regardless of context or input.\n"
#             "• For simpler questions, include additional details like examples, types, or related information.\n"
#             f"{context}Here is the user's question: {question}"
#         )
#         try:
#             result = self.qa_chain({"question": modified_question, "chat_history": chat_history})
#             answer = result["answer"]

#             # Check if the vector store lacks information
#             if "provided context does not contain information" in answer.lower() or "not found in the context" in answer.lower():
#                 return (
#                     "## Information Not Available\n"
#                     "• The medical database does not contain details about this topic.\n"
#                     "• This question appears outside the scope of available information.\n"
#                     "• Consult a reliable medical source or healthcare professional for accurate information.\n\n"
#                     "## Additional Information\n"
#                     "• Online medical resources like WebMD can provide general guidance.\n"
#                     "• Local clinics offer consultations for personalized advice.\n"
#                     "Would you like to ask about something else?"
#                 )

#             # Cache the response
#             self.response_cache[question_lower] = answer
#             return answer
#         except ValueError as e:
#             logger.error(f"API error in get_response: {str(e)}")
#             error_str = str(e).lower()
#             if "no instances available" in error_str or "503" in error_str:
#                 return (
#                     "## Model Unavailable\n"
#                     "• The medical database is temporarily unavailable due to high demand.\n"
#                     "• Try again later or with a different question.\n"
#                     "• Consult a healthcare professional for urgent needs.\n\n"
#                     "## Additional Information\n"
#                     "• Free models may have limited availability.\n"
#                     "• Check OpenRouter.ai for model status.\n"
#                 )
#             raise e

#     def check_symptoms(self, symptoms):
#         if not symptoms.strip() or symptoms.lower() in ["i don't feel well", "not feeling well"]:
#             return (
#                 "**Symptom Information Needed**\n"
#                 "• Specific symptoms are needed to provide a better analysis.\n"
#                 "• Examples include fever, pain, or fatigue.\n"
#                 "• Consult a doctor for a thorough evaluation.\n\n"
#                 "## Additional Information\n"
#                 "• Keeping a symptom diary can help doctors diagnose issues.\n"
#                 "• Urgent symptoms like chest pain require immediate attention.\n"
#             )
#         query = (
#             "Role:\n"
#             "You are a medical assistant providing general medical information based on reported symptoms.\n\n"
#             "Formatting Rules:\n"
#             "• Use exactly `**Possible Conditions**` (Markdown bolded) for the first section heading. This must render as bold text, with no visible Markdown asterisks (`**`). Use `##` for all subsequent section headings (e.g., `## Recommendations`). All headings must start from the left side only, with no indentation, centering, or right-alignment.\n"
#             "• Insert a newline (`\n`) after each heading to ensure content (bullet points or text) starts on the next line. Content must not be on the same line as the heading.\n"
#             "• Use `•` for bullet points, with one item per bullet. Each bullet point must start on a new line, with no extra spaces before the `•`. Insert a newline (`\n`) after each bullet point to ensure they do not combine (e.g., not `• Item 1. • Item 2.`). Do not combine multiple items in a single bullet, use colons (e.g., not `• Condition: description`), or use other symbols like `-`, `*`, or `◦`.\n"
#             "• Ensure the entire response, including bullet points and additional text, is formatted to be displayed in a justified text manner (except for headings, which must start from the left side only). The rendering system will handle justification, but structure the response with proper newlines and bullet points.\n"
#             "• Apply these formatting rules consistently to all responses, whether generated using the vector database, the model's own knowledge, or a combination of both.\n"
#             "• Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user, except for the `**Possible Conditions**` heading.\n"
#             "• Do not use colons in headings (e.g., not `Possible Conditions:`), single `#`, or other heading styles.\n"
#             "• Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "• Do not include 'Assistant:', 'Bot:', or similar prefixes in the response.\n"
#             "• Avoid errors: do not use colons in bullet points, combine multiple descriptions in one bullet, or use numbered lists.\n\n"
#             "Example:\n"
#             "```\n"
#             "**Possible Conditions**\n"
#             "• These symptoms could indicate a common cold, which is a viral infection of the upper respiratory tract.\n"
#             "• They might also suggest influenza (flu), a more severe viral illness that often includes fever and cough.\n"
#             "• In some cases, these symptoms could be related to a respiratory infection such as bronchitis or pneumonia.\n"
#             "• COVID-19, caused by the SARS-CoV-2 virus, can also present with fever, cough, and cold-like symptoms.\n"
#             "## Recommendations\n"
#             "• Rest and stay hydrated to support recovery.\n"
#             "Consult a doctor for a professional diagnosis.\n"
#             "```\n\n"
#             "Instructions:\n"
#             "• Use the user's exact input without correcting spellings, even if incorrect (e.g., 'fevr' stays 'fevr').\n"
#             "• Add extra medical information from your knowledge in a clear format, following the formatting rules above.\n"
#             "• Respond only in English, regardless of context or input.\n"
#             "• Always recommend consulting a doctor for a professional diagnosis.\n"
#             f"Here are the user's symptoms: {symptoms}. What might this indicate based on medical guidelines? Provide general information and recommend consulting a doctor."
#         )
#         try:
#             result = self.qa_chain({"question": query, "chat_history": []})
#             answer = result["answer"]
#             return answer
#         except ValueError as e:
#             logger.error(f"API error in check_symptoms: {str(e)}")
#             error_str = str(e).lower()
#             if "no instances available" in error_str or "503" in error_str:
#                 return (
#                     "**Model Unavailable**\n"
#                     "• The medical database is temporarily unavailable due to high demand.\n"
#                     "• Try again later or with different symptoms.\n"
#                     "• Consult a healthcare professional for urgent needs.\n\n"
#                     "## Additional Information\n"
#                     "• Free models may have limited availability.\n"
#                     "• Check OpenRouter.ai for model status.\n"
#                 )
#             raise e

# from langchain_openai import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from dotenv import load_dotenv
# import os
# import logging

# # Setup logging for Streamlit Cloud
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# class ModelAPI:
#     def __init__(self, vector_store):
#         load_dotenv()
#         api_key = os.getenv("OPENROUTER_API_KEY")
#         if not api_key:
#             logger.error("OPENROUTER_API_KEY is not set in .env file")
#             raise ValueError("Missing OPENROUTER_API_KEY. Please set it in the .env file.")
        
#         self.llm = ChatOpenAI(
#             model="deepseek/deepseek-chat:free",
#             openai_api_key=api_key,
#             openai_api_base="https://openrouter.ai/api/v1"
#         )
#         self.qa_chain = ConversationalRetrievalChain.from_llm(
#             llm=self.llm,
#             retriever=vector_store.as_retriever(),
#             return_source_documents=True
#         )
#         # Cache for responses to reduce API calls
#         self.response_cache = {}
#         # Fallback responses for common questions
#         self.fallback_responses = {
#             "what are the symptoms of the flu?": (
#                 "## Symptoms of the Flu\n"
#                 "• Fever often high, 100°F to 104°F or higher.\n"
#                 "• Chills and sweats.\n"
#                 "• Cough usually dry.\n"
#                 "• Sore throat.\n"
#                 "• Muscle aches or body aches.\n"
#                 "• Headache.\n"
#                 "• Fatigue or weakness.\n"
#                 "• Runny or stuffy nose.\n"
#                 "• Nausea, vomiting, or diarrhea more common in children.\n\n"
#                 "## Additional Information\n"
#                 "• Influenza affects 5-20% of the population annually.\n"
#                 "• Antiviral medications can reduce severity if taken early.\n"
#                 "Symptoms often come on suddenly and can range from mild to severe. If you suspect you have the flu, especially if you are at high risk for complications, consult a healthcare provider."
#             ),
#             "what causes high blood pressure?": (
#                 "## Causes of High Blood Pressure\n"
#                 "• Lifestyle factors like poor diet with high salt intake, obesity, lack of physical activity, excessive alcohol consumption, and smoking.\n"
#                 "• Underlying medical conditions such as diabetes, kidney disease, and hormonal disorders.\n"
#                 "• Genetic predisposition where a family history of hypertension increases risk.\n"
#                 "• Stress where chronic stress contributes to elevated blood pressure.\n"
#                 "• Aging as blood pressure often increases with age.\n\n"
#                 "## Additional Information\n"
#                 "• Hypertension affects over 1 billion people globally.\n"
#                 "• Regular monitoring can prevent complications like heart attack.\n"
#                 "Treatment often involves lifestyle changes and medications if needed. Would you like to know more about managing high blood pressure?"
#             ),
#             "what is anemia?": (
#                 "## What is Anemia\n"
#                 "• Anemia is a condition with abnormally low levels of healthy red blood cells or hemoglobin, which carries oxygen to tissues.\n"
#                 "• Fatigue or weakness.\n"
#                 "• Shortness of breath.\n"
#                 "• Pale skin.\n"
#                 "• Dizziness or lightheadedness.\n\n"
#                 "## Types of Anemia\n"
#                 "• Iron-deficiency anemia caused by lack of iron, often due to poor diet or blood loss.\n"
#                 "• Vitamin B12 deficiency anemia due to insufficient B12, often linked to diet or absorption issues.\n"
#                 "• Sickle cell anemia, a genetic condition where red blood cells are abnormally shaped.\n\n"
#                 "## Additional Information\n"
#                 "• Anemia affects about 25% of the global population.\n"
#                 "• Blood tests like CBC can confirm diagnosis.\n"
#                 "If you suspect anemia, a doctor can diagnose it with a blood test and recommend treatment like iron supplements or dietary changes."
#             ),
#             "what are symptoms of heart attack?": (
#                 "## Symptoms of a Heart Attack\n"
#                 "• Chest pain or discomfort often described as pressure, squeezing, or pain in the center or left side of the chest, lasting minutes or recurring.\n"
#                 "• Upper body discomfort in one or both arms, jaw, neck, back, or stomach.\n"
#                 "• Shortness of breath with or without chest pain.\n"
#                 "• Cold sweat, nausea, or lightheadedness accompanying chest discomfort.\n\n"
#                 "## Additional Information\n"
#                 "• Heart attacks are a leading cause of death worldwide.\n"
#                 "• Immediate treatment like aspirin can improve outcomes.\n"
#                 "If you experience these symptoms, especially chest pain or shortness of breath, seek emergency medical attention immediately."
#             ),
#             "what causes kidney stones?": (
#                 "## Causes of Kidney Stones\n"
#                 "• Dehydration where not drinking enough water leads to concentrated urine, increasing stone formation risk.\n"
#                 "• Diet with high intake of sodium, oxalate found in foods like spinach, or animal protein.\n"
#                 "• Medical conditions like hyperparathyroidism, gout, or urinary tract infections.\n"
#                 "• Family history with a genetic predisposition to kidney stones.\n"
#                 "• Obesity where higher body weight increases risk.\n"
#                 "• Certain medications like some diuretics or calcium-based antacids.\n\n"
#                 "## Additional Information\n"
#                 "• Kidney stones affect about 10% of people in their lifetime.\n"
#                 "• Imaging tests like CT scans can detect stones.\n"
#                 "Kidney stones can be made of different materials like calcium oxalate or uric acid, depending on the cause."
#             ),
#             "how can i prevent them?": (
#                 "## Preventing Kidney Stones\n"
#                 "• Stay hydrated by drinking plenty of water, aiming for 2-3 liters daily to dilute urine.\n"
#                 "• Adjust diet by reducing sodium, oxalate-rich foods like spinach, and animal protein, and eating more citrus fruits containing citrate to prevent stones.\n"
#                 "• Maintain a healthy weight as obesity increases risk, so regular exercise and a balanced diet help.\n"
#                 "• Monitor medical conditions like gout or urinary tract infections that contribute to stones.\n"
#                 "• Consult a doctor if you have a history of kidney stones for specific dietary changes or medications.\n\n"
#                 "## Additional Information\n"
#                 "• Citrate supplements may reduce stone formation.\n"
#                 "• Regular check-ups can catch stones early.\n"
#             )
#         }

#     def is_greeting(self, question):
#         question_lower = question.lower().strip()
#         greeting_responses = {
#             "good morning": "Good morning! How can I assist with your medical questions today?",
#             "good afternoon": "Good afternoon! Ready to help with any health concerns you have.",
#             "good evening": "Good evening! Here to answer your medical questions before you wind down.",
#             "good night": "Good night! Feel free to ask any medical questions before you rest.",
#             "thank you": "You're welcome! Happy to help with any more health questions.",
#             "thanks": "You're welcome! Let me know if you have more medical queries."
#         }
#         for greeting, response in greeting_responses.items():
#             if greeting in question_lower:
#                 return response
#         generic_greetings = ["hello", "hi", "hey"]
#         words = question_lower.split()
#         if any(word in generic_greetings for word in words):
#             return "Hello! I'm your medical assistant. How can I help you with your health questions today?"
#         return None

#     def check_repetitive_question(self, question, chat_history):
#         question_lower = question.lower().strip()
#         if "blood pressure" in question_lower and ("cause" in question_lower or "what causes" in question_lower):
#             for prev_question, prev_answer in chat_history:
#                 prev_question_lower = prev_question.lower().strip()
#                 if "blood pressure" in prev_question_lower and (
#                         "cause" in prev_question_lower or "what causes" in prev_question_lower):
#                     return (
#                         "## Recap of High Blood Pressure Causes\n"
#                         "• Lifestyle factors like high salt intake, obesity, and smoking.\n"
#                         "• Medical conditions such as kidney disease or diabetes.\n"
#                         "• Genetic predisposition, stress, and aging.\n\n"
#                         "## Additional Information\n"
#                         "• Blood pressure screenings are recommended annually.\n"
#                         "• Medications like ACE inhibitors can manage hypertension.\n"
#                         "Would you like to know more about managing high blood pressure, or do you have a different question?"
#                     )
#         return None

#     def get_response(self, question, chat_history):
#         # Check for greetings first
#         greeting_response = self.is_greeting(question)
#         if greeting_response:
#             return greeting_response

#         # Normalize question for cache and fallback lookup
#         question_lower = question.lower().strip()

#         # Check for repetitive questions
#         repetitive_response = self.check_repetitive_question(question, chat_history)
#         if repetitive_response:
#             return repetitive_response

#         # Check cache for previous response
#         if question_lower in self.response_cache:
#             return self.response_cache[question_lower]

#         # Check if question matches a fallback response
#         if question_lower in self.fallback_responses:
#             response = self.fallback_responses[question_lower]
#             self.response_cache[question_lower] = response
#             return response

#         # Add context from recent chat history
#         context = ""
#         if chat_history:
#             last_question, last_answer = chat_history[-1]
#             if "stress" in last_question.lower() and "manage" in question_lower:
#                 context = f"Previous question: {last_question}\nPrevious answer: {last_answer}\n"

#         modified_question = (
#             "Role:\n"
#             "You are a medical assistant providing accurate and detailed medical information.\n\n"
#             "Formatting Rules:\n"
#             "• Use Markdown `##` for all section headings (e.g., `## Symptoms`). Headings must start from the left side only, with no indentation, centering, or right-alignment.\n"
#             "• Insert a newline (`\n`) after each heading to ensure content (bullet points or text) starts on the next line. Content must not be on the same line as the heading.\n"
#             "• Use `•` for bullet points, with one item per bullet. Each bullet point must start on a new line, with no extra spaces before the `•`. Insert a newline (`\n`) after each bullet point to ensure they do not combine (e.g., not `• Item 1. • Item 2.`). Do not combine multiple items in a single bullet, use colons (e.g., not `• Item: description`), or use other symbols like `-`, `*`, or `◦`.\n"
#             "• Ensure the entire response, including bullet points and additional text, is formatted to be displayed in a justified text manner (except for headings, which must start from the left side only). The rendering system will handle justification, but structure the response with proper newlines and bullet points.\n"
#             "• Apply these formatting rules consistently to all responses, whether generated using the vector database, the model's own knowledge, or a combination of both.\n"
#             "• Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user.\n"
#             "• Do not use colons in headings (e.g., not `Symptoms:`), single `#`, or other heading styles.\n"
#             "• Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "• Do not include 'Assistant:', 'Bot:', or similar prefixes in the response.\n"
#             "• Avoid errors: do not use colons in bullet points, combine multiple descriptions in one bullet, or use numbered lists.\n\n"
#             "Example:\n"
#             "```\n"
#             "## Symptoms of a Cold\n"
#             "• Runny or stuffy nose is common.\n"
#             "• Sore throat may occur early on.\n"
#             "• Cough is usually mild.\n"
#             "• Fatigue can persist for a few days.\n"
#             "## Additional Information\n"
#             "• Colds are caused by viruses like rhinovirus.\n"
#             "Consult a doctor if symptoms worsen.\n"
#             "```\n\n"
#             "Instructions:\n"
#             "• Use the user's exact input without correcting spellings, even if incorrect (e.g., 'diabtes' stays 'diabtes').\n"
#             "• Add extra medical information from your knowledge in a clear format, following the formatting rules above.\n"
#             "• Respond only in English, regardless of context or input.\n"
#             "• For simpler questions, include additional details like examples, types, or related information.\n"
#             f"{context}Here is the user's question: {question}"
#         )
#         try:
#             result = self.qa_chain({"question": modified_question, "chat_history": chat_history})
#             answer = result["answer"]

#             # Check if the vector store lacks information
#             if "provided context does not contain information" in answer.lower() or "not found in the context" in answer.lower():
#                 return (
#                     "## Information Not Available\n"
#                     "• The medical database does not contain details about this topic.\n"
#                     "• This question appears outside the scope of available information.\n"
#                     "• Consult a reliable medical source or healthcare professional for accurate information.\n\n"
#                     "## Additional Information\n"
#                     "• Online medical resources like WebMD can provide general guidance.\n"
#                     "• Local clinics offer consultations for personalized advice.\n"
#                     "Would you like to ask about something else?"
#                 )

#             # Cache the response
#             self.response_cache[question_lower] = answer
#             return answer
#         except ValueError as e:
#             logger.error(f"API error in get_response: {str(e)}")
#             error_str = str(e).lower()
#             if "no instances available" in error_str or "503" in error_str:
#                 return (
#                     "## Model Unavailable\n"
#                     "• The medical database is temporarily unavailable due to high demand.\n"
#                     "• Try again later or with a different question.\n"
#                     "• Consult a healthcare professional for urgent needs.\n\n"
#                     "## Additional Information\n"
#                     "• Free models may have limited availability.\n"
#                     "• Check OpenRouter.ai for model status.\n"
#                 )
#             raise e

#     def check_symptoms(self, symptoms):
#         if not symptoms.strip() or symptoms.lower() in ["i don't feel well", "not feeling well"]:
#             return (
#                 "**Symptom Information Needed**\n"
#                 "• Specific symptoms are needed to provide a better analysis.\n"
#                 "• Examples include fever, pain, or fatigue.\n"
#                 "• Consult a doctor for a thorough evaluation.\n\n"
#                 "## Additional Information\n"
#                 "• Keeping a symptom diary can help doctors diagnose issues.\n"
#                 "• Urgent symptoms like chest pain require immediate attention.\n"
#             )
#         query = (
#             "Role:\n"
#             "You are a medical assistant providing general medical information based on reported symptoms.\n\n"
#             "Formatting Rules:\n"
#             "• Use exactly `**Possible Conditions**` (Markdown bolded) for the first section heading. This must render as bold text, with no visible Markdown asterisks (`**`). Use `## Recommendations` for the second section heading to provide advice. All headings must start from the left side only, with no indentation, centering, or right-alignment.\n"
#             "• Insert a newline (`\n`) after each heading to ensure content (bullet points or text) starts on the next line. Content must not be on the same line as the heading.\n"
#             "• Use `•` for bullet points, with one item per bullet. Each bullet point must start on a new line, with no extra spaces before the `•`. Ensure each bullet point is followed by a newline (`\n`) to prevent combining (e.g., `• Item 1.\n• Item 2.`), not `• Item 1. • Item 2.`. Do not combine multiple items in a single bullet, use colons (e.g., not `• Condition: description`), or use other symbols like `-`, `*`, or `◦`.\n"
#             "• Ensure the entire response, including bullet points and additional text, is formatted to be displayed in a justified text manner (except for headings, which must start from the left side only). The rendering system will handle justification, but structure the response with proper newlines and bullet points.\n"
#             "• Apply these formatting rules consistently to all responses, whether generated using the vector database, the model's own knowledge, or a combination of both.\n"
#             "• Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user, except for the `**Possible Conditions**` heading.\n"
#             "• Do not use colons in headings (e.g., not `Possible Conditions:`), single `#`, or other heading styles.\n"
#             "• Ensure all bullet points are concise, complete sentences ending with a period.\n"
#             "• Do not include 'Assistant:', 'Bot:', or similar prefixes in the response.\n"
#             "• Avoid errors: do not use colons in bullet points, combine multiple descriptions in one bullet, or use numbered lists.\n\n"
#             "Example:\n"
#             "```\n"
#             "**Possible Conditions**\n"
#             "• These symptoms could indicate a common cold.\n"
#             "• They might also suggest influenza (flu).\n"
#             "• In some cases, these could be related to bronchitis.\n"
#             "• COVID-19 can also present with these symptoms.\n\n"
#             "## Recommendations\n"
#             "• Rest and stay hydrated to support recovery.\n"
#             "Consult a doctor for a professional diagnosis.\n"
#             "```\n\n"
#             "Instructions:\n"
#             "• Use the user's exact input without correcting spellings, even if incorrect (e.g., 'fevr' stays 'fevr').\n"
#             "• Add extra medical information from your knowledge in a clear format, following the formatting rules above.\n"
#             "• Respond only in English, regardless of context or input.\n"
#             "• Always include a `## Recommendations` section with advice, and recommend consulting a doctor for a professional diagnosis.\n"
#             f"Here are the user's symptoms: {symptoms}. What might this indicate based on medical guidelines? Provide general information and recommend consulting a doctor."
#         )
#         try:
#             result = self.qa_chain({"question": query, "chat_history": []})
#             answer = result["answer"]
#             return answer
#         except ValueError as e:
#             logger.error(f"API error in check_symptoms: {str(e)}")
#             error_str = str(e).lower()
#             if "no instances available" in error_str or "503" in error_str:
#                 return (
#                     "**Model Unavailable**\n"
#                     "• The medical database is temporarily unavailable due to high demand.\n"
#                     "• Try again later or with different symptoms.\n"
#                     "• Consult a healthcare professional for urgent needs.\n\n"
#                     "## Additional Information\n"
#                     "• Free models may have limited availability.\n"
#                     "• Check OpenRouter.ai for model status.\n"
#                 )
#             raise e

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
        # Fallback responses for common questions
        self.fallback_responses = {
            "what are the symptoms of the flu?": (
                "## Symptoms of the Flu\n"
                "- Fever often high, 100°F to 104°F or higher.\n"
                "- Chills and sweats.\n"
                "- Cough usually dry.\n"
                "- Sore throat.\n"
                "- Muscle aches or body aches.\n"
                "- Headache.\n"
                "- Fatigue or weakness.\n"
                "- Runny or stuffy nose.\n"
                "- Nausea, vomiting, or diarrhea more common in children.\n\n"
                "## Additional Information\n"
                "- Influenza affects 5-20% of the population annually.\n"
                "- Antiviral medications can reduce severity if taken early.\n"
                "Symptoms often come on suddenly and can range from mild to severe. If you suspect you have the flu, especially if you are at high risk for complications, consult a healthcare provider."
            ),
            "what causes high blood pressure?": (
                "## Causes of High Blood Pressure\n"
                "- Lifestyle factors like poor diet with high salt intake, obesity, lack of physical activity, excessive alcohol consumption, and smoking.\n"
                "- Underlying medical conditions such as diabetes, kidney disease, and hormonal disorders.\n"
                "- Genetic predisposition where a family history of hypertension increases risk.\n"
                "- Stress where chronic stress contributes to elevated blood pressure.\n"
                "- Aging as blood pressure often increases with age.\n\n"
                "## Additional Information\n"
                "- Hypertension affects over 1 billion people globally.\n"
                "- Regular monitoring can prevent complications like heart attack.\n"
                "Treatment often involves lifestyle changes and medications if needed. Would you like to know more about managing high blood pressure?"
            ),
            "what is anemia?": (
                "## What is Anemia\n"
                "- Anemia is a condition with abnormally low levels of healthy red blood cells or hemoglobin, which carries oxygen to tissues.\n"
                "- Fatigue or weakness.\n"
                "- Shortness of breath.\n"
                "- Pale skin.\n"
                "- Dizziness or lightheadedness.\n\n"
                "## Types of Anemia\n"
                "- Iron-deficiency anemia caused by lack of iron, often due to poor diet or blood loss.\n"
                "- Vitamin B12 deficiency anemia due to insufficient B12, often linked to diet or absorption issues.\n"
                "- Sickle cell anemia, a genetic condition where red blood cells are abnormally shaped.\n\n"
                "## Additional Information\n"
                "- Anemia affects about 25% of the global population.\n"
                "- Blood tests like CBC can confirm diagnosis.\n"
                "If you suspect anemia, a doctor can diagnose it with a blood test and recommend treatment like iron supplements or dietary changes."
            ),
            "what are symptoms of heart attack?": (
                "## Symptoms of a Heart Attack\n"
                "- Chest pain or discomfort often described as pressure, squeezing, or pain in the center or left side of the chest, lasting minutes or recurring.\n"
                "- Upper body discomfort in one or both arms, jaw, neck, back, or stomach.\n"
                "- Shortness of breath with or without chest pain.\n"
                "- Cold sweat, nausea, or lightheadedness accompanying chest discomfort.\n\n"
                "## Additional Information\n"
                "- Heart attacks are a leading cause of death worldwide.\n"
                "- Immediate treatment like aspirin can improve outcomes.\n"
                "If you experience these symptoms, especially chest pain or shortness of breath, seek emergency medical attention immediately."
            ),
            "what causes kidney stones?": (
                "## Causes of Kidney Stones\n"
                "- Dehydration where not drinking enough water leads to concentrated urine, increasing stone formation risk.\n"
                "- Diet with high intake of sodium, oxalate found in foods like spinach, or animal protein.\n"
                "- Medical conditions like hyperparathyroidism, gout, or urinary tract infections.\n"
                "- Family history with a genetic predisposition to kidney stones.\n"
                "- Obesity where higher body weight increases risk.\n"
                "- Certain medications like some diuretics or calcium-based antacids.\n\n"
                "## Additional Information\n"
                "- Kidney stones affect about 10% of people in their lifetime.\n"
                "- Imaging tests like CT scans can detect stones.\n"
                "Kidney stones can be made of different materials like calcium oxalate or uric acid, depending on the cause."
            ),
            "how can i prevent them?": (
                "## Preventing Kidney Stones\n"
                "- Stay hydrated by drinking plenty of water, aiming for 2-3 liters daily to dilute urine.\n"
                "- Adjust diet by reducing sodium, oxalate-rich foods like spinach, and animal protein, and eating more citrus fruits containing citrate to prevent stones.\n"
                "- Maintain a healthy weight as obesity increases risk, so regular exercise and a balanced diet help.\n"
                "- Monitor medical conditions like gout or urinary tract infections that contribute to stones.\n"
                "- Consult a doctor if you have a history of kidney stones for specific dietary changes or medications.\n\n"
                "## Additional Information\n"
                "- Citrate supplements may reduce stone formation.\n"
                "- Regular check-ups can catch stones early.\n"
            )
        }

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
                        "- Lifestyle factors like high salt intake, obesity, and smoking.\n"
                        "- Medical conditions such as kidney disease or diabetes.\n"
                        "- Genetic predisposition, stress, and aging.\n\n"
                        "## Additional Information\n"
                        "- Blood pressure screenings are recommended annually.\n"
                        "- Medications like ACE inhibitors can manage hypertension.\n"
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

        # Check if question matches a fallback response
        if question_lower in self.fallback_responses:
            response = self.fallback_responses[question_lower]
            self.response_cache[question_lower] = response
            return response

        # Add context from recent chat history
        context = ""
        if chat_history:
            last_question, last_answer = chat_history[-1]
            if "stress" in last_question.lower() and "manage" in question_lower:
                context = f"Previous question: {last_question}\nPrevious answer: {last_answer}\n"

        modified_question = (
            "Role:\n"
            "You are a medical assistant providing accurate and detailed medical information.\n\n"
            "Formatting Rules:\n"
            "• Use Markdown `##` for all section headings (e.g., `## Symptoms`). Headings must start from the left side only, with no indentation, centering, or right-alignment.\n"
            "• Insert a newline (`\n`) after each heading to ensure content (bullet points or text) starts on the next line. Content must not be on the same line as the heading.\n"
            "• Use `•` for bullet points, with one item per bullet. Each bullet point must start on a new line, with no extra spaces before the `•`. Insert a newline (`\n`) after each bullet point to ensure they do not combine (e.g., not `• Item 1. • Item 2.`). Do not combine multiple items in a single bullet, use colons (e.g., not `• Item: description`), or use other symbols like `-`, `*`, or `◦`.\n"
            "• Ensure the entire response, including bullet points and additional text, is formatted to be displayed in a justified text manner (except for headings, which must start from the left side only). The rendering system will handle justification, but structure the response with proper newlines and bullet points.\n"
            "• Apply these formatting rules consistently to all responses, whether generated using the vector database, the model's own knowledge, or a combination of both.\n"
            "• Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user.\n"
            "• Do not use colons in headings (e.g., not `Symptoms:`), single `#`, or other heading styles.\n"
            "• Ensure all bullet points are concise, complete sentences ending with a period.\n"
            "• Do not include 'Assistant:', 'Bot:', or similar prefixes in the response.\n"
            "• Avoid errors: do not use colons in bullet points, combine multiple descriptions in one bullet, or use numbered lists.\n\n"
            "Example:\n"
            "```\n"
            "## Symptoms of a Cold\n"
            "• Runny or stuffy nose is common.\n"
            "• Sore throat may occur early on.\n"
            "• Cough is usually mild.\n"
            "• Fatigue can persist for a few days.\n"
            "## Additional Information\n"
            "• Colds are caused by viruses like rhinovirus.\n"
            "Consult a doctor if symptoms worsen.\n"
            "```\n\n"
            "Instructions:\n"
            "• Use the user's exact input without correcting spellings, even if incorrect (e.g., 'diabtes' stays 'diabtes').\n"
            "• Add extra medical information from your knowledge in a clear format, following the formatting rules above.\n"
            "• Respond only in English, regardless of context or input.\n"
            "• For simpler questions, include additional details like examples, types, or related information.\n"
            f"{context}Here is the user's question: {question}"
        )
        try:
            result = self.qa_chain({"question": modified_question, "chat_history": chat_history})
            answer = result["answer"]

            # Check if the vector store lacks information
            if "provided context does not contain information" in answer.lower() or "not found in the context" in answer.lower():
                return (
                    "## Information Not Available\n"
                    "- The medical database does not contain details about this topic.\n"
                    "- This question appears outside the scope of available information.\n"
                    "- Consult a reliable medical source or healthcare professional for accurate information.\n\n"
                    "## Additional Information\n"
                    "- Online medical resources like WebMD can provide general guidance.\n"
                    "- Local clinics offer consultations for personalized advice.\n"
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
                    "- The medical database is temporarilyUnavailable due to high demand.\n"
                    "- Try again later or with a different question.\n"
                    "- Consult a healthcare professional for urgent needs.\n\n"
                    "## Additional Information\n"
                    "- Free models may have limited availability.\n"
                    "- Check OpenRouter.ai for model status.\n"
                )
            raise e

    def check_symptoms(self, symptoms):
        if not symptoms.strip() or symptoms.lower() in ["i don't feel well", "not feeling well"]:
            return (
                "**Symptom Information Needed**\n"
                "- Specific symptoms are needed to provide a better analysis.\n"
                "- Examples include fever, pain, or fatigue.\n"
                "- Consult a doctor for a thorough evaluation.\n\n"
                "## Additional Information\n"
                "- Keeping a symptom diary can help doctors diagnose issues.\n"
                "- Urgent symptoms like chest pain require immediate attention.\n"
            )
        query = (
            "Role:\n"
            "You are a medical assistant providing general medical information based on reported symptoms.\n\n"
            "Formatting Rules:\n"
            "• Use exactly `**Possible Conditions**` (Markdown bolded) for the first section heading. This must render as bold text, with no visible Markdown asterisks (`**`). Use `## Recommendations` for the second section heading to provide advice. All headings must start from the left side only, with no indentation, centering, or right-alignment.\n"
            "• Insert a newline (`\n`) after each heading to ensure content (bullet points or text) starts on the next line. Content must not be on the same line as the heading.\n"
            "• Use `•` for bullet points, with one item per bullet. Each bullet point must start on a new line, with no extra spaces before the `•`. Ensure each bullet point is followed by a newline (`\n`) to prevent combining (e.g., `• Item 1.\n• Item 2.`), not `• Item 1. • Item 2.`. Do not combine multiple items in a single bullet, use colons (e.g., not `• Condition: description`), or use other symbols like `-`, `*`, or `◦`.\n"
            "• Ensure the entire response, including bullet points and additional text, is formatted to be displayed in a justified text manner (except for headings, which must start from the left side only). The rendering system will handle justification, but structure the response with proper newlines and bullet points.\n"
            "• Apply these formatting rules consistently to all responses, whether generated using the vector database, the model's own knowledge, or a combination of both.\n"
            "• Do not use bold (`**`) or italic (`*`) text unless explicitly requested by the user, except for the `**Possible Conditions**` heading.\n"
            "• Do not use colons in headings (e.g., not `Possible Conditions:`), single `#`, or other heading styles.\n"
            "• Ensure all bullet points are concise, complete sentences ending with a period.\n"
            "• Do not include 'Assistant:', 'Bot:', or similar prefixes in the response.\n"
            "• Avoid errors: do not use colons in bullet points, combine multiple descriptions in one bullet, or use numbered lists.\n\n"
            "Example:\n"
            "```\n"
            "**Possible Conditions**\n"
            "• These symptoms could indicate a common cold.\n"
            "• They might also suggest influenza (flu).\n"
            "• In some cases, these could be related to bronchitis.\n"
            "• COVID-19 can also present with these symptoms.\n\n"
            "## Recommendations\n"
            "• Rest and stay hydrated to support recovery.\n"
            "Consult a doctor for a professional diagnosis.\n"
            "```\n\n"
            "Instructions:\n"
            "• Use the user's exact input without correcting spellings, even if incorrect (e.g., 'fevr' stays 'fevr').\n"
            "• Add extra medical information from your knowledge in a clear format, following the formatting rules above.\n"
            "• Respond only in English, regardless of context or input.\n"
            "• Always include a `## Recommendations` section with advice, and recommend consulting a doctor for a professional diagnosis.\n"
            f"Here are the user's symptoms: {symptoms}. What might this indicate based on medical guidelines? Provide general information and recommend consulting a doctor."
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
                    "- The medical database is temporarily unavailable due to high demand.\n"
                    "- Try again later or with different symptoms.\n"
                    "- Consult a healthcare professional for urgent needs.\n\n"
                    "## Additional Information\n"
                    "- Free models may have limited availability.\n"
                    "- Check OpenRouter.ai for model status.\n"
                )
            raise e
