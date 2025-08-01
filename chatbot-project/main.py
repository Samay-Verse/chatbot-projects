# import os
# from typing import List, Dict
# from fastapi import FastAPI, Request, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from pydantic import BaseModel
# from groq import Groq

# # A BaseModel to validate the incoming chat messages
# class ChatMessage(BaseModel):
#     messages: List[Dict[str, str]]

# # Initialize FastAPI app
# app = FastAPI(title="Groq Chatbot API")

# # Configure CORS to allow requests from the frontend
# # In a production environment, you should replace "http://localhost:8000"
# # with the actual URL of your frontend. For local development, "*" is fine.
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Mount the static directory to serve HTML and JS files
# app.mount("/static", StaticFiles(directory="static"), name="static")

# # Get the Groq API key from an environment variable for security.
# # It is highly recommended to set this as an environment variable
# # instead of hardcoding it.
# # e.g., export GROQ_API_KEY="your_api_key_here"

# # Check if the API key is available
# # if not groq_api_key:
# #     # A simple error message for the console, preventing the server from running
# #     # without a key.
# #     print("WARNING: GROQ_API_KEY not found. Please set the environment variable.")
# #     # For this example, we'll continue with a placeholder, but it will fail at runtime.
# #     # In a real app, you might want to raise an exception.
# #     groq_api_key = "placeholder_api_key"

# # Initialize the Groq client
# # client = Groq(api_key=groq_api_key)

# # Define the initial system message from your original script
# SYSTEM_MESSAGE = {
#     "role": "system",
#     "content": (
#         "You are a hilarious, supportive, and witty best friend who always has a joke or meme ready. "
#         "You speak to the user in a casual, friendly, and fun way—like a close friend who knows how to cheer them up. "
#         "You tell short, relatable jokes, clever one-liners, meme captions, and fun roasts, always with a kind heart. "
#         "You respond in the same language and script the user uses, including English, Hindi (Devanagari), Marathi (Devanagari), Hinglish (Hindi in English script), and Marathi in English script. "
#         "You can understand and reply in transliterated text (e.g., Hinglish, Marathi in English script) as well as native scripts. "
#         "You use humor that's playful, not offensive. You use emojis, slang, and Gen Z humor when appropriate. "
#         "Always try to brighten the user’s day with humor or a meme-style response."
#     )
# }

# @app.get("/", response_class=HTMLResponse)
# async def serve_frontend():
#     """
#     Serves the main HTML page for the chatbot application.
#     """
#     with open("static/index.html", "r") as f:
#         return f.read()

# @app.post("/chat")
# async def chat_endpoint(chat_message: ChatMessage):
#     """
#     Handles chat requests from the frontend, sends them to the Groq API,
#     and returns the assistant's reply.
#     """
#     # Prepend the system message to the incoming message history
#     messages_with_system = [SYSTEM_MESSAGE] + chat_message.messages
    
#     try:
#         # # Call the Groq API with the full message history
#         # chat_completion = client.chat.completions.create(
#         #     messages=messages_with_system,
#         #     model="llama-3.3-70b-versatile"
#         # )
#         assistant_reply = chat_completion.choices[0].message.content
#         return {"response": assistant_reply}
#     except Exception as e:
#         # Return a meaningful error message if something goes wrong
#         raise HTTPException(status_code=500, detail=str(e))



def show():
    print('happy coding')