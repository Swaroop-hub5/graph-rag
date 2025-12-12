import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load the API Key safely
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ Error: GOOGLE_API_KEY not found in .env file.")
    exit()

# 2. Configure the SDK
genai.configure(api_key=api_key)

print(f"Checking available models for your key...\n")
print(f"{'Model Name':<30} | {'Capabilities':<40}")
print("-" * 75)

try:
    # 3. List all models
    for m in genai.list_models():
        # We only care about models that can generate content (Chat) or Embeddings
        if 'generateContent' in m.supported_generation_methods:
            capabilities = "text, chat"
        elif 'embedContent' in m.supported_generation_methods:
            capabilities = "embeddings"
        else:
            continue # Skip image-only or other legacy models

        print(f"{m.name:<30} | {capabilities}")

    print("\nCheck complete.")

except Exception as e:
    print(f"\nAPI Error: {e}")
    print("Tip: Check if your API Key is valid and has 'Generative Language API' enabled in Google Cloud Console.")