import os
import chromadb
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_transformers import (
    LongContextReorder,
)
from langchain.chains import StuffDocumentsChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

# This is a playground for testing the langchain module
from langchain.document_loaders import PyPDFLoader
from PyPDF2 import PdfWriter

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