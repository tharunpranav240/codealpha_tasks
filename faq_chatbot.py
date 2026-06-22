faq = {
    "what is your name": "I am an FAQ chatbot.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "who developed python": "Python was developed by Guido van Rossum.",
    "what is machine learning": "Machine Learning is a branch of AI."
}

print("FAQ Chatbot (type 'exit' to quit)")

while True:
    user = input("You: ").lower()

    if user == "exit":
        print("Bot: Goodbye!")
        break

    if user in faq:
        print("Bot:", faq[user])
    else:
        print("Bot: Sorry, I don't know the answer.")
