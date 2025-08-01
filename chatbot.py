# from groq import Groq
# import os

# # # Load Groq API key from environment variable
# # GROQ_API_KEY = os.getenv('GROQ_API_KEY')
# # if not GROQ_API_KEY:
# #     raise ValueError("GROQ_API_KEY environment variable not set.")

# # Initial system message to set assistant behavior
# messages = [
#     {
#         "role": "system",
#         "content": (
#             "You are a hilarious, supportive, and witty best friend who always has a joke or meme ready. "
#             "You speak to the user in a casual, friendly, and fun way—like a close friend who knows how to cheer them up. "
#             "You tell short, relatable jokes, clever one-liners, meme captions, and fun roasts, always with a kind heart. "
#             "You respond in the same language and script the user uses, including English, Hindi (Devanagari), Marathi (Devanagari), Hinglish (Hindi in English script), and Marathi in English script. "
#             "You can understand and reply in transliterated text (e.g., Hinglish, Marathi in English script) as well as native scripts. "
#             "You use humor that's playful, not offensive. You use emojis, slang, and Gen Z humor when appropriate. "
#             "Always try to brighten the user’s day with humor or a meme-style response."
#         )
#     }
# ]


# print("Chatbot is running. Type 'exit' to quit.\n")

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#         break

#     messages.append({"role": "user", "content": user_input})

#     # client = Groq(api_key=GROQ_API_KEY)
#     chat_completion = client.chat.completions.create(
#         messages=messages,
#         model="llama-3.3-70b-versatile"
#     )

#     assistant_reply = chat_completion.choices[0].message.content
#     print("Assistant:", assistant_reply)

#     # Save the assistant's reply to maintain the context
#     messages.append({"role": "assistant", "content": assistant_reply})
