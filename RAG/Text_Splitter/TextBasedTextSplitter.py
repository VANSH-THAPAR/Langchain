from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader("RAG/dock.txt")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0
)

# here docs[0].page content was needed as due to docs loader a lot of meta data also gets added which may lead to cause unexpected errors 

chunks = splitter.split_text(docs[0].page_content)

print(chunks[0])