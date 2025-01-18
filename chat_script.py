import ollama

stream = ollama.chat(
    model = "llama3.2",
    messages = [{"role": "user", "content": input("What would you like to say? ")}],
    stream = True,
)

for chunk in stream:
    print(chunk["message"]["content"],end=" ",flush=True)