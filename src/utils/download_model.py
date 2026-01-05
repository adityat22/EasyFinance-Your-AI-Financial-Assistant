from huggingface_hub import hf_hub_download
import os

def download_model():
    # Switching to Mistral 7B Instruct v0.2 - A much more capable model
    model_name = "TheBloke/Mistral-7B-Instruct-v0.2-GGUF"
    filename = "mistral-7b-instruct-v0.2.Q4_K_M.gguf"
    
    print(f"Downloading {filename} from {model_name}...")
    try:
        # Download to data/models
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        models_dir = os.path.join(base_dir, "data", "models")
        
        model_path = hf_hub_download(repo_id=model_name, filename=filename, local_dir=models_dir)
        print(f"Model downloaded successfully to: {model_path}")
    except Exception as e:
        print(f"Error downloading model: {e}")

if __name__ == "__main__":
    # Ensure data/models exists
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    models_dir = os.path.join(base_dir, "data", "models")
    
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
    download_model()
