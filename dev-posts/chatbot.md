---
layout: page
title: Building an FAQ Chatbot Using the ChatGPT API
description: Let's create a more advanced FAQ chatbot by combining our previous approach with OpenAI's ChatGPT API. This will give us the flexibility of our predef...
keywords: faq, messages, our, your, answer
---
# Building an FAQ Chatbot Using the ChatGPT API

Let's create a more advanced FAQ chatbot by combining our previous approach with OpenAI's ChatGPT API. This will give us the flexibility of our predefined FAQs while leveraging ChatGPT's natural language understanding for more complex queries.

## Step 1: Set Up Your Environment

1. Install required packages:
```bash
pip install openai python-dotenv
```

2. Create a `.env` file for your API key:
```env
OPENAI_API_KEY=your_api_key_here
```

## Step 2: Create the Hybrid Chatbot

```python
import os
import openai
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load FAQ knowledge base
faq_knowledge_base = {
    "store_hours": {
        "question": "What are your store hours?",
        "answer": "We're open Monday-Friday 9am-9pm, Saturday 10am-8pm, and Sunday 11am-6pm."
    },
    "returns": {
        "question": "What is your return policy?",
        "answer": "You can return items within 30 days with a receipt for a full refund."
    },
    "contact": {
        "question": "How can I contact support?",
        "answer": "You can reach us at support@example.com or call 1-800-EXAMPLE."
    }
}

# System message to guide ChatGPT's behavior
SYSTEM_MESSAGE = """
You are a helpful FAQ assistant for a retail store. Your primary knowledge comes from the FAQ knowledge base.
If a question matches one in the knowledge base, respond with JUST the answer from the knowledge base.
For questions not in the knowledge base, provide a helpful response based on your general knowledge.
Be concise and professional in your responses.
"""

def get_chatgpt_response(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"I'm sorry, I encountered an error: {str(e)}"

def generate_faq_context():
    """Generate a context string from our FAQ knowledge base"""
    faq_list = []
    for key, item in faq_knowledge_base.items():
        faq_list.append(f"Q: {item['question']}\nA: {item['answer']}")
    return "\n\n".join(faq_list)

def chat():
    print("FAQ Bot: Hello! I'm here to answer your questions about our store.")
    print("Type 'quit' to end the conversation.")
    
    # Initial system message with FAQ context
    messages = [
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "system", "content": f"FAQ Knowledge Base:\n{generate_faq_context()}"}
    ]
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() == 'quit':
            print("FAQ Bot: Goodbye! Have a great day!")
            break
            
        # Add user message to conversation history
        messages.append({"role": "user", "content": user_input})
        
        # Get response from ChatGPT
        response = get_chatgpt_response(messages)
        
        # Add assistant response to conversation history
        messages.append({"role": "assistant", "content": response})
        
        print(f"FAQ Bot: {response}")

if __name__ == "__main__":
    chat()
```

## How This Hybrid Approach Works

1. **FAQ Knowledge Base**: We maintain our structured FAQs for precise answers to common questions.

2. **ChatGPT Integration**: For questions that don't match our FAQs exactly, ChatGPT provides intelligent responses.

3. **System Messages**: We guide ChatGPT's behavior with:
   - Instructions to prioritize our FAQ answers
   - Context about our specific business
   - Tone guidelines (concise, professional)

4. **Conversation Memory**: The chat maintains context by keeping the message history.

## Advanced Enhancements

1. **Add Semantic Search**:
```python
from sentence_transformers import SentenceTransformer
import numpy as np

# Initialize model (run once)
model = SentenceTransformer('all-MiniLM-L6-v2')

def find_most_similar_faq(user_question):
    # Encode all FAQ questions
    faq_questions = [item["question"] for item in faq_knowledge_base.values()]
    question_embeddings = model.encode(faq_questions)
    
    # Encode user question
    user_embedding = model.encode([user_question])
    
    # Calculate similarities
    similarities = np.inner(user_embedding, question_embeddings)[0]
    most_similar_index = np.argmax(similarities)
    
    if similarities[most_similar_index] > 0.7:  # similarity threshold
        key = list(faq_knowledge_base.keys())[most_similar_index]
        return faq_knowledge_base[key]["answer"]
    return None
```

2. **Add Logging**:
```python
import datetime

def log_conversation(user_input, bot_response):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("chat_logs.txt", "a") as f:
        f.write(f"{timestamp} - User: {user_input}\n")
        f.write(f"{timestamp} - Bot: {bot_response}\n\n")
```

3. **Add Multi-turn FAQ Handling**:
```python
def handle_faq_followup(messages):
    last_two = messages[-2:]
    if last_two[0]["role"] == "user" and last_two[1]["role"] == "assistant":
        # Check if the assistant's response came from our FAQ
        for faq in faq_knowledge_base.values():
            if last_two[1]["content"] == faq["answer"]:
                return f"Would you like more information about {faq['question'].lower()}?"
    return None
```

## Cost Optimization Tips

1. **Cache Responses**: Store frequent answers to avoid API calls
2. **Token Limits**: Keep system messages concise
3. **Fallback Logic**: Try your FAQ matching before calling the API

## Example Usage

```
FAQ Bot: Hello! I'm here to answer your questions about our store.
You: What time do you close on weekdays?
FAQ Bot: We're open Monday-Friday 9am-9pm, Saturday 10am-8pm, and Sunday 11am-6pm.

You: Do you have a student discount?
FAQ Bot: While we don't currently have a standard student discount program, we do offer seasonal promotions
that students can take advantage of. I recommend signing up for our newsletter to stay informed about
these special offers.
```

This hybrid approach gives you the best of both worlds - precise control over FAQ answers with the flexibility of ChatGPT for unexpected questions. Would you like me to elaborate on any specific aspect of this implementation?