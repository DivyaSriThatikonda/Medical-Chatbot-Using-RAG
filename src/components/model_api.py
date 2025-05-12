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

from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv
import os
import re

class ModelAPI:
    def __init__(self, vector_store):
        load_dotenv()
        self.llm = ChatOpenAI(
            model="deepseek/deepseek-chat:free",
            openai_api_key=os.getenv("OPENROUTER_API_KEY"),
            openai_api_base="https://openrouter.ai/api/v1"
        )
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=vector_store.as_retriever(),
            return_source_documents=True
        )
        # Cache for responses to reduce API calls
        self.response_cache = {}
        # Fallback responses for common questions when API limit is reached
        self.fallback_responses = {
            "what are the symptoms of the flu?": (
                "## Symptoms of the Flu\n"
                "The symptoms of the flu (influenza) typically include:\n"
                "- Fever (often high, 100°F to 104°F or higher)\n"
                "- Chills and sweats\n"
                "- Cough (usually dry)\n"
                "- Sore throat\n"
                "- Muscle aches or body aches\n"
                "- Headache\n"
                "- Fatigue or weakness\n"
                "- Runny or stuffy nose\n"
                "- Nausea, vomiting, or diarrhea (more common in children)\n\n"
                "Symptoms often come on suddenly and can range from mild to severe. If you suspect you have the flu, especially if you are at high risk for complications (e.g., young children, elderly, or those with chronic conditions), it’s important to consult a healthcare provider."
            ),
            "what causes high blood pressure?": (
                "## Causes of High Blood Pressure\n"
                "High blood pressure (hypertension) can be caused by a variety of factors, including:\n"
                "- Lifestyle factors: Poor diet (high salt intake), obesity, lack of physical activity, excessive alcohol consumption, and smoking.\n"
                "- Underlying medical conditions: Conditions such as diabetes, kidney disease, and hormonal disorders.\n"
                "- Genetic predisposition: A family history of hypertension increases your risk.\n"
                "- Stress: Chronic stress can contribute to elevated blood pressure.\n"
                "- Aging: Blood pressure often increases with age.\n\n"
                "Treatment often involves lifestyle changes (like a healthier diet and exercise) and medications if needed. Would you like to know more about managing high blood pressure?"
            ),
            "what is anemia?": (
                "## What is Anemia?\n"
                "Anemia is a condition where you have abnormally low levels of healthy red blood cells or hemoglobin, which carries oxygen to your body’s tissues. This can lead to symptoms like:\n"
                "- Fatigue or weakness\n"
                "- Shortness of breath\n"
                "- Pale skin\n"
                "- Dizziness or lightheadedness\n\n"
                "## Types of Anemia\n"
                "- Iron-deficiency anemia: Caused by a lack of iron, often due to poor diet or blood loss.\n"
                "- Vitamin B12 deficiency anemia: Due to insufficient B12, often linked to diet or absorption issues.\n"
                "- Sickle cell anemia: A genetic condition where red blood cells are abnormally shaped.\n\n"
                "If you suspect anemia, a doctor can diagnose it with a blood test and recommend treatment, such as iron supplements or dietary changes."
            ),
            "what are symptoms of heart attack?": (
                "## Symptoms of a Heart Attack\n"
                "Common signs of a heart attack include:\n"
                "- Chest pain or discomfort: Often described as pressure, squeezing, or pain in the center or left side of the chest. It may last for minutes or come and go.\n"
                "- Upper body discomfort: Pain in one or both arms, the jaw, neck, back, or stomach.\n"
                "- Shortness of breath: This can occur with or without chest pain.\n"
                "- Cold sweat, nausea, or lightheadedness: These symptoms may accompany chest discomfort.\n\n"
                "If you experience these symptoms, especially chest pain or shortness of breath, seek emergency medical attention immediately."
            ),
            "what causes kidney stones?": (
                "## Causes of Kidney Stones\n"
                "Kidney stones form due to a combination of factors, including:\n"
                "- Dehydration: Not drinking enough water leads to concentrated urine, increasing stone formation risk.\n"
                "- Diet: High intake of sodium, oxalate (found in foods like spinach), or animal protein.\n"
                "- Medical conditions: Conditions like hyperparathyroidism, gout, or urinary tract infections (UTIs).\n"
                "- Family history: A genetic predisposition to kidney stones.\n"
                "- Obesity: Higher body weight increases the risk.\n"
                "- Certain medications: Some diuretics or calcium-based antacids can contribute.\n\n"
                "Kidney stones can be made of different materials, like calcium oxalate or uric acid, depending on the cause."
            ),
            "how can i prevent them?": (
                "## Preventing Kidney Stones\n"
                "To prevent kidney stones, you can:\n"
                "- Stay hydrated: Drink plenty of water (aim for 2-3 liters daily) to dilute your urine.\n"
                "- Adjust your diet: Reduce sodium, oxalate-rich foods (like spinach), and animal protein. Eat more citrus fruits, which contain citrate that helps prevent stones.\n"
                "- Maintain a healthy weight: Obesity increases the risk, so regular exercise and a balanced diet can help.\n"
                "- Monitor medical conditions: Manage conditions like gout or UTIs that can contribute to stones.\n"
                "- Talk to your doctor: If you have a history of kidney stones, they may recommend specific dietary changes or medications."
            )
        }

    def is_greeting(self, question):
        greetings = ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]
        question_lower = question.lower().strip()
        words = question_lower.split()
        return any(word in greetings for word in words)

    def check_repetitive_question(self, question, chat_history):
        """Check if the question is similar to a previous one in chat history."""
        question_lower = question.lower().strip()
        if "blood pressure" in question_lower and ("cause" in question_lower or "what causes" in question_lower):
            for prev_question, prev_answer in chat_history:
                prev_question_lower = prev_question.lower().strip()
                if "blood pressure" in prev_question_lower and (
                        "cause" in prev_question_lower or "what causes" in prev_question_lower):
                    return (
                        f"I previously explained the causes of high blood pressure. To recap briefly: it can be due to lifestyle factors (like high salt intake, obesity, and smoking), medical conditions (like kidney disease or diabetes), genetics, stress, and aging. "
                        "Would you like to know more about managing high blood pressure, or do you have a different question?"
                    )
        return None

    def enforce_heading_format(self, response):
        """Post-process the response to ensure section titles use ## for headings, starting from the left."""
        lines = response.split('\n')
        processed_lines = []
        i = 0
        while i < len(lines):
            # Strip leading spaces from the line for processing
            line = lines[i].strip()
            # Preserve the original indentation for non-heading lines
            original_line = lines[i]
            
            # Skip empty lines
            if not line:
                processed_lines.append(original_line)
                i += 1
                continue
            
            # Check if the line looks like a heading
            is_heading = False
            
            # 1. Line ends with a colon (e.g., "Common Symptoms:", "Triggers of Asthma:")
            if line.endswith(':'):
                is_heading = True
            
            # 2. Line matches common heading patterns (e.g., "What is Asthma?", "Symptoms")
            elif re.match(r'^(What is [A-Za-z\s]+\?|Symptoms|Triggers|Types of [A-Za-z\s]+|Management|Causes of [A-Za-z\s]+|When to Seek (Help|Emergency Help)|Important Notes|Symptoms in [A-Za-z\s]+|Key Features of [A-Za-z\s]+|Possible Conditions|Prevention|Risk Factors|Treatments)$', line):
                is_heading = True
            
            # 3. Line starts with a + or number followed by a heading (e.g., "+ Triggers of Asthma:", "8. Common Symptoms:")
            elif re.match(r'^[\+\d]\.\s*(.+)$', line):
                is_heading = True
                line = re.sub(r'^[\+\d]\.\s*', '', line)  # Remove the + or number prefix
            
            # 4. Heuristic: Line is short, followed by a non-empty line that isn't a list item
            elif (len(line.split()) <= 5 and  # Short line (likely a title)
                  i + 1 < len(lines) and      # Has a next line
                  lines[i + 1].strip() and    # Next line is not empty
                  not lines[i + 1].strip().startswith('-') and  # Next line is not a list item
                  not lines[i + 1].strip().startswith(tuple(f"{j}." for j in range(1, 10)))):  # Next line is not a numbered item
                is_heading = True
            
            # If identified as a heading, prefix with ## and ensure it starts from the left
            if is_heading:
                if not line.startswith('##'):
                    line = f"## {line}"
                processed_lines.append(line)  # No leading spaces, starts from the left
            else:
                processed_lines.append(original_line)  # Preserve original indentation for non-headings
            
            i += 1
        
        return '\n'.join(processed_lines)

    def get_response(self, question, chat_history):
        if self.is_greeting(question):
            return "Hello! I'm your medical assistant. How can I help you with your health questions today?"

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
            "You are a medical assistant. Provide accurate and detailed medical information based on the user’s question. "
            "For simpler questions, include additional details like examples, types, or related information to enhance the response. "
            "Format section titles as Markdown headings (##) and use bullet points or numbered lists for clarity. "
            "Always respond in English, regardless of the context or input. Do not use any other language. "
            f"{context}Here is the user's question: {question} (Please respond strictly in English)"
        )
        try:
            result = self.qa_chain({"question": modified_question, "chat_history": chat_history})
            answer = result["answer"]

            # Check if the vector store lacks information
            if "provided context does not contain information" in answer.lower() or "not found in the context" in answer.lower():
                return (
                    "I’m sorry, but the information I’m referring to doesn’t contain details about this topic. "
                    "My knowledge is based on a specific medical database, and this question seems to be outside its scope. "
                    "I recommend consulting a reliable medical source or healthcare professional for accurate information. "
                    "Would you like to ask about something else?"
                )

            # Post-process the response to enforce ## for section titles
            answer = self.enforce_heading_format(answer)

            # Cache the response
            self.response_cache[question_lower] = answer
            return answer
        except ValueError as e:
            if "Rate limit exceeded" in str(e):
                # Try fallback response if API limit is reached
                if question_lower in self.fallback_responses:
                    response = self.fallback_responses[question_lower]
                    self.response_cache[question_lower] = response
                    return response
                return (
                    "I’ve reached my daily request limit with the API I use to fetch detailed answers. However, I can still help with some common questions! "
                    "Try asking about flu symptoms, high blood pressure causes, anemia, heart attack symptoms, or kidney stones. "
                    "Alternatively, you can wait until tomorrow when my API limit resets, or consult a healthcare professional for immediate advice."
                )
            raise e

    def check_symptoms(self, symptoms):
        if not symptoms.strip() or symptoms.lower() in ["i don't feel well", "not feeling well"]:
            return (
                "I’m sorry to hear you’re not feeling well, but I need more specific symptoms to provide a better analysis. "
                "For example, do you have a fever, pain, fatigue, or any other symptoms? In the meantime, I recommend consulting a doctor for a thorough evaluation."
            )
        query = f"I have the following symptoms: {symptoms}. What might this indicate based on medical guidelines? Please provide general information and recommend consulting a doctor."
        try:
            result = self.qa_chain({"question": query, "chat_history": []})
            answer = result["answer"]
            # Post-process the response to enforce ## for section titles
            answer = self.enforce_heading_format(answer)
            return answer
        except ValueError as e:
            if "Rate limit exceeded" in str(e):
                return (
                    "I’ve reached my daily request limit with the API I use to fetch detailed answers. "
                    "Please try again tomorrow, or consult a healthcare professional for advice about your symptoms in the meantime."
                )
            raise e
