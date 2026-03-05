import google.generativeai as genai

# Gemini AI Setup
API_KEY = "AIzaSyAMcAbhmjgTha_5KPnTwzId8lhj6E0dcBc"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

# J.A.R.V.I.S. Introduction
def jarvis_intro():
    intro_text = "Good day, Sir. I am J.A.R.V.I.S., your personal assistant. How may I assist you today?"
    print("J.A.R.V.I.S.:", intro_text)

# Main Chat Loop
def jarvis_chat():
    jarvis_intro()
    print("Chat with J.A.R.V.I.S.! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            farewell_text = "Goodbye, Sir. Have a great day."
            print("J.A.R.V.I.S.:", farewell_text)
            break
        try:
            response = chat.send_message(user_input)
            jarvis_response = response.text
            print("J.A.R.V.I.S.:", jarvis_response)
        except Exception as e:
            error_text = "I'm sorry, Sir. I encountered an error processing your request."
            print("J.A.R.V.I.S.:", error_text)
            print(f"Error: {e}")

if __name__ == "__main__":
    jarvis_chat()