from llama_cpp import Llama

llm = Llama(
    model_path="/Users/dushyantsharma/Desktop/awsfreetier/OpensourceLLMs/Mistral-AI/mistral-7b-instruct-v0.1.Q5_K_M.gguf", #to insight reporter
    n_ctx=2048,         # Context token limit
    n_threads=8,       # Adjust to your CPU (likely 8-core hyperthreaded)
    use_mlock=True     # Locks memory to prevent swap
)

def run_llm(prompt):
    output = llm(prompt=prompt, max_tokens=512, stop=["</s>"]) # max_tokens to generate in
    return output["choices"][0]["text"].strip()
