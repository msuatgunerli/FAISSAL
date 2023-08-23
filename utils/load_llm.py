from llama_cpp import Llama

def load_llm(model_type):
        if model_type == "LLaMA-7B":
                llm = Llama(model_path= "MODEL_PATH", 
                n_ctx= 2048,
                n_parts= -1,
                n_gpu_layers = 32,
                n_threads = 8,
                n_batch= 256,
                last_n_tokens_size = 64)
        
        elif model_type == "LLaMA-13B":
                llm = Llama(model_path= "MODEL_PATH", 
                n_ctx= 2048,
                n_parts= -1,
                n_gpu_layers = 32,
                n_threads = 8,
                n_batch= 256,
                last_n_tokens_size = 64)
        return llm