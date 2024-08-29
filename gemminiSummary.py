import google.generativeai as genai
import os

def summarize(name):
    genai.configure(api_key=os.environ["API_KEY"])

    sample_file = genai.upload_file(path=f"{name}.txt",display_name="Gemini 1.5 PDF")

    print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")


    file = genai.get_file(name=sample_file.name)
    print(f"Retrieved file '{file.display_name}' as: {sample_file.uri}")

    # Choose a Gemini model.
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    # Prompt the model with text and the previously uploaded image.
    response = model.generate_content([sample_file, "Read the following file and give me a summary keep it different from the original and make it useful, give a more detailed summary on the news"])

    
        
    return response.text
    
