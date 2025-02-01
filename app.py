import subprocess

def run_deepseek(prompt):
    result = subprocess.run(['ollama', 'run', 'deepseek-r1', prompt], capture_output=True, text=True)
    return result.stdout

def chat_with_deepseek():
    print("Chat with DeepSeek-R1! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Ending chat with DeepSeek-R1. Goodbye!")
            break
        response = run_deepseek(user_input)
        print("DeepSeek-R1: " + response)

if __name__ == "__main__":
    chat_with_deepseek()
