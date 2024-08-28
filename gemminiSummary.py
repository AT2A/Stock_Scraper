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
    response = model.generate_content([sample_file, "The following text is the day info, anaylst ratings, and etc. of a stock, I want you to summarize the file and go to the urls and summarize the news articles."])

    print(response)
    
