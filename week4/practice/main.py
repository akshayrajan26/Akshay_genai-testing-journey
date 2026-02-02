from text_processor.config import DEFAULT_MODEL, MAX_TOKENS
from text_processor.utils import count_tokens, truncate
from text_processor.storage import save_to_json

def process_user_input(text):
    print(f"Using model: {DEFAULT_MODEL}")
    tokens = count_tokens(text)
    if tokens > MAX_TOKENS:
        print("Trimming...")
        text = truncate(text, MAX_TOKENS)
    
    result = {
        "original_length": tokens,
        "processed_text": text.upper() # Mock processing
    }
    
    save_to_json(result, "output.json")
    print("Done!")

if __name__ == "__main__":
    process_user_input("Hello, world!")
