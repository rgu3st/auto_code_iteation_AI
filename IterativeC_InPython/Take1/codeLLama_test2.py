from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

#model_name = "codellama/CodeLlama-7b-instruct-hf"
#model = AutoModelForCausalLM.from_pretrained(model_name)
#tokenizer = AutoTokenizer.from_pretrained(model_name)
model_path = "S:\\repos\\CodeLlama-7b-Instruct-hf"
model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

#Set to GPU if possible:
#device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#device = torch.device("cpu")
device = torch.device("cuda")
model.to(device)

def generate_code(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
    output = model.generate(input_ids, max_length=500, num_return_sequences=1)
    generate_code = tokenizer.decode(output[0], skip_special_tokens=True)
    return generate_code


# Should I create a REPL here, so I can try a bunch of prompts and generations
prompt_in = "Write a C file to print 'Hello World of local LLMs!'"
generate_code = generate_code(prompt_in)
print(f"Generated code:\n{generate_code}")
