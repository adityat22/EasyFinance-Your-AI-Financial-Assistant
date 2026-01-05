from langchain_community.llms import CTransformers
import os
import time

def test_model():
    model_path = "models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"
    if not os.path.exists(model_path):
        print(f"Model not found at {model_path}")
        return

    print(f"Loading model from {model_path}...")
    start_time = time.time()
    try:
        llm = CTransformers(
            model=model_path,
            model_type="mistral",
            config={'max_new_tokens': 100, 'temperature': 0.7}
        )
        print(f"Model loaded in {time.time() - start_time:.2f}s")
        
        print("Generating response...")
        start_time = time.time()
        response = llm.invoke("Hello, are you working?")
        print(f"Response generated in {time.time() - start_time:.2f}s")
        print("Response:", response)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_model()