from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("data/raw/Chemistry2e-WEB.pdf")
pages = loader.load_and_split()

print(pages[0])


