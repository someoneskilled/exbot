from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the fine-tuned model and tokenizer
model_name = "someoneskilled/fine-tuned-distilgpt2-exbot"  # Replace with your model's username and name
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Function to generate response
def generate_response(prompt, max_length=50, temperature=0.7):
    inputs = tokenizer.encode(prompt, return_tensors="pt", add_special_tokens=True)
    response_ids = model.generate(inputs, max_length=max_length, temperature=temperature, pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(response_ids[0], skip_special_tokens=True)

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        print("Goodbye!")
        break
    response = generate_response(user_input)
    print("Chatbot:", response)
