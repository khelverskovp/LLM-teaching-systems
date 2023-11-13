import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a given PDF file using the PdfReader class.
    
    Args:
    pdf_path (str): Path to the PDF file.

    Returns:
    str: Extracted text from the PDF.
    """
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file) 
        text = ''
        for page in reader.pages: 
            text += page.extract_text()  
        return text

if __name__ == "__main__":
    # Get the absolute path of the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the relative path to the PDF in the raw data folder
    pdf_path = os.path.join(script_dir, '..', '..', 'data', 'raw', 'Chemistry2e-WEB.pdf')
    
    # Extract text
    textbook_text = extract_text_from_pdf(pdf_path)
    
    # Define the relative path to save the extracted text within the processed data folder
    save_path = os.path.join(script_dir, '..', '..', 'data', 'processed', 'Chemistry_2e_extracted_text.txt')
    
    # Make sure the processed directory exists, create it if not
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Save the extracted text to a file
    with open(save_path, 'w', encoding='utf-8') as text_file:
        text_file.write(textbook_text)
