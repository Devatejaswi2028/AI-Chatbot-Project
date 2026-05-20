import re
import random
from datetime import datetime

# Simple patterns and responses
INTENTS = [
    (re.compile(r"\b(hi|hello|hey)\b", re.I), [
        "Hey! How can I help you today?",
        "Hello there! What can I do for you?",
        "Hi! What’s on your mind?"
    ]),
    (re.compile(r"\b(thank(s)?|thanks a lot)\b", re.I), [
        "You’re welcome!",
        "Happy to help!",
        "Anytime!"
    ]),
    (re.compile(r"\b(time|date)\b", re.I), [
        lambda: f"The current date and time is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
    ]),
    (re.compile(r"\b(name)\b.*\b(you)\b", re.I), [
        "I’m your Python chatbot."
    ]),
    (re.compile(r"\b(help|support|assist)\b", re.I), [
        "I can chat, tell you the time, and answer basic questions. Try saying 'hello' or ask 'what time is it?'"
    ]),
]

FALLBACKS = [
    "I’m not sure I got that. Could you rephrase?",
    "Hmm, I don’t know that yet. Try asking something else.",
    "Interesting! I don’t have an answer for that—want to try another question?"
]

def respond(user_input: str) -> str:
    text = user_input.strip()
    if not text:
        return "Say something and I’ll respond. 🙂"
    for pattern, replies in INTENTS:
        if pattern.search(text):
            # Support callable replies (like time)
            reply = random.choice(replies)
            return reply() if callable(reply) else reply
    return random.choice(FALLBACKS)

def chat():
    print("Chatbot ready. Type 'quit' to exit.")
    while True:
        user = input("You: ")
        if user.lower().strip() in {"quit", "exit", "bye"}:
            print("Bot: Bye! 👋")
            break
        print("Bot:", respond(user))

if __name__ == "__main__":
    chat()
