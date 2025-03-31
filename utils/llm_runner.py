from llama_cpp import Llama

llm = Llama(
    model_path="/Users/dushyantsharma/Desktop/awsfreetier/OpensourceLLMs/Mistral-AI/mistral-7b-instruct-v0.1.Q5_K_M.gguf",
    n_ctx=2048,
    n_threads=8,
    use_mlock=True
)

def run_llm(prompt):
    output = llm(prompt=prompt, max_tokens=256, stop=["</s>"])
    return output["choices"][0]["text"].strip()


