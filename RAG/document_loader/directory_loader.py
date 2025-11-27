import glob
from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader

loader = DirectoryLoader(
    path = "RAG/dir_pdf",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(docs[0].page_content)
print(docs[0].metadata)