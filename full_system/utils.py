import os
import chromadb
import time

from tqdm import tqdm

import whisper
from moviepy.editor import *
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_transformers import (
    LongContextReorder,
)
from langchain.chains import StuffDocumentsChain, LLMChain
from langchain.prompts import PromptTemplate

# This is a playground for testing the langchain module
from langchain.document_loaders import PyPDFLoader
from PyPDF2 import PdfWriter

from pydub import AudioSegment
import math

def getPages(filename):
    '''
    Given a filename, this function returns a list of individual pages from the corresponding PDF. Use pages[i].page_content to access the text of the ith page. The text is stored as a string.

    Parameters: 
    filename (str): A string representation of the PDF file name.
    
    Returns:
    pages list[<class 'langchain.schema.document.Document'>]: A list of langchain schema documents, where each index represents a separate page within the PDF file. Created by using the PyPDFLoader's load_and_split() method on the given filename. You can get the text of each page by accessing the page_content attribute of each index.
    '''
    loader = PyPDFLoader(filename)
    pages = loader.load_and_split()
    return pages

def splitPDF(document_path,relevant_page):
    '''
    Given a filename (to a PDF file) and a page number, this function creates a single page PDF file based on a relevant page number. 
    
    Parameters:
    document_path (str): A string representation of the PDF file name.
    relevant_page (int): An integer representing the page number of the most relevant page.

    Returns:
    Name of the new PDF file.
    '''

    # initialize the merger
    merger = PdfWriter()

    # open the pdf
    pdf_reader = open(document_path, "rb")

    # add the relevant pages to the output file
    merger.append(fileobj=pdf_reader, pages=(relevant_page, relevant_page+1))

    # Write to an output PDF document
    pdf_name = f'{document_path[:-4]}-RAG.pdf'
    output = open(pdf_name, "wb")
    merger.write(output)

    # Close File Descriptors
    merger.close()
    output.close()

    return pdf_name

# transcribe using whisper
def transcribe_whisper(filename):
    """Transcribe a file using the whisper model and 
        return the transcript and the transcript filename"""
    
    os.environ['gptkey'] = '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'
    import openai
    openai.api_key = os.getenv("gptkey")


    audio_file= open(filename, "rb")

    model = whisper.load_model("base")
    transcript = model.transcribe(filename)
    
    #print(transcript['text'])

    with open(f"{filename.split('.')[0]}_transcript.txt", "w") as f:
        f.write(transcript['text'])
    return transcript['text'], f"{filename.split('.')[0]}_transcript.txt"

def makesound(filename):
    video = VideoFileClip(f"{filename}")
    video.audio.write_audiofile(f"{filename.split('.')[0]}.mp3")
    return f"{filename.split('.')[0]}.mp3"

# Function to split audio into chunks in milliseconds
def split_audio(filename, chunk_size=30000):
    """Split an audio file into chunks and return a list of chunks"""
    audio = AudioSegment.from_file(filename)
    chunks = []
    for i in range(0, len(audio), chunk_size):
        chunks.append(audio[i:i+chunk_size])
    return chunks

# function that goes from seconds to hh:mm:ss
def seconds_to_hhmmss(seconds):
    """Convert seconds to hh:mm:ss"""
    return time.strftime('%H:%M:%S', time.gmtime(seconds))

def transcribeTimestamp(filename):
    chunks = split_audio(filename)

    filename = filename.split('/')[1]
    print(filename)

    # save the chunks starting from 1
    for i, chunk in enumerate(chunks):
        chunk_name = f"{filename.split('.')[0]}_{i+1}.wav"
        print("exporting", chunk_name)
        chunk.export(chunk_name, format="wav")

        # save in data/audio_chunks
        os.rename(chunk_name, f"data/audio_chunks/{chunk_name}")

    # for each chunk, transcribe using whisper
    print(f"Transcribing {len(chunks)} audio chunks...")
    for i in tqdm(range(len(chunks))):
       transcribe_whisper(f"data/audio_chunks/{filename.split('.')[0]}_{i+1}.wav")
    
    # for each video ending in _transcript.txt open and add to new txt
    with open(f"data/{filename.split('.')[0]}_transcript.txt", "w") as f:
        for i in range(len(chunks)):
            with open(f"data/audio_chunks/{filename.split('.')[0]}_{i+1}_transcript.txt", "r") as g:
                f.write(seconds_to_hhmmss(i*30)+g.read())
                f.write('\n\n')

# main script for splitting audio
if __name__ == "__main__":
    # get the filename
    filename = input("Enter the filename: ")
    # split the audio
    transcribeTimestamp(filename)
    
