from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# First, we will have to import the tokenizer and the language model
tokenizer = AutoTokenizer.from_pretrained("norallm/normistral-7b-scratch")
model = AutoModelForCausalLM.from_pretrained("norallm/normistral-7b-scratch")

# Check if CUDA is available and move the model to the appropriate device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device).eval()

# Now we will define the zero-shot prompt template
prompt = """Engelsk: {0}
Bokmål:"""

# A function that will take care of generating the output
@torch.no_grad()
def generate(text):
    text = prompt.format(text)
    input_ids = tokenizer(text, return_tensors='pt').input_ids.to(device)
    
    # Ensure eos_token_id is properly set
    eos_token_id = tokenizer.eos_token_id if tokenizer.eos_token_id is not None else tokenizer("\n").input_ids[0]
    
    prediction = model.generate(
        input_ids,
        max_new_tokens=64,
        do_sample=False,
        eos_token_id=eos_token_id
    )
    
    return tokenizer.decode(prediction[0, input_ids.size(1):]).strip()

# Now you can simply call the generate function with an English text you want to translate:
translation = generate("I'm super excited about this Norwegian NORA model! Can it translate these sentences?")
print(translation)
