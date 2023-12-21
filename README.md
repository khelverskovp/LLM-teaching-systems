To run the app version of the system locally run app_local.py using "streamlit run app_local.py" 

to visit the deployed version of the app visit: https://llm-teaching-system-app.streamlit.app/ 

# Readme for Educational Material Processing Script (assistantAPI.py). 

This is the script that runs GPT Vision and GPT Whisper as well.

## Overview

The provided Python script is designed to assist users in analyzing educational material, generating relevant guidance based on questions, and interacting with an AI assistant to facilitate a Socratic dialogue. The script utilizes OpenAI's API, coupled with HuggingFace embeddings and other natural language processing tools, to extract content from documents, transcribe audio files, and provide tailored responses to user's queries.

## Dependencies

- os
- json
- time
- aspose.words
- openai
- chromadb
- langchain (including vectorstores, embeddings, document_transformers, chains, prompts, and llms modules)
- User-defined modules:
  - gptFunctions
  - utils

Ensure all dependencies are installed using pip:

pip install openai chromadb langchain aspose-words

Replace aspose-words with the appropriate installation method if necessary. The user-defined modules gptFunctions and utils should be present in the same directory as the script or appropriately installed.

## Features

- Transcribes audio from files with extensions .mp4, .wav, .flac, .m4a.
- Splits PDF documents to focus on the most relevant content based on user questions.
- Embeds text using HuggingFaceEmbeddings.
- Interacts with an AI assistant for guided responses.
- Optionally incorporates image content by encoding and analyzing images related to user queries.

## Usage

1. Run the script. You will be prompted to provide input for the educational material's subject and location.

   
   python assistantAPI.py
   

2. If the educational material is in a video or audio format, you will be asked for the file path. The script will then transcribe the audio and convert it to PDF format.

3. Next, the script prompts for a question regarding the educational material, searching within the document to identify the most relevant page.

4. An OpenAI assistant is programmatically created with the description of its purpose, based on the subject provided previously.

5. The script interacts with the user to provide a Socratic-dialogue-based assistance. Users can submit their questions or replies iteratively.

6. The script allows for the optional uploading of a photo related to the question, providing a visual context for the AI's response.

7. Responses from the AI assistant are displayed in the console, providing step-by-step guidance.

## Configuration

1. OpenAI API Key:

   Replace the placeholder API key with your own OpenAI API key:

   
   client = OpenAI(
       api_key='your-api-key-here'
   )
   

2. SSL Context (Optional):

   To bypass SSL verification in a non-production environment, you might uncomment the section-related to SSL context setup. This is not recommended for production use.

## Important Notes

- Always ensure you use your own OpenAI API key.
- The script utilizes paid services (transcription, embedding, OpenAI API); ensure your account is properly configured for billing.
- The script assumes you have access to the relevant API endpoints and model versions.
- The image encoding tool provided in the utils module should be secured and used with caution if handling sensitive information.
- aspose.words offers a free trial, after which you'll need to purchase a license for continued use or use an alternative method for processing documents.

## Disclaimer

This script is provided as-is, and the users are responsible for any costs incurred from API usage or external services. It's important to review and understand the data privacy and retention policies of the services you choose to use with this script.
