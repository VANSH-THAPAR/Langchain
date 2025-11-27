from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('RAG/CSSNotesForProfessionals.pdf')

pdf = loader.lazy_load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 10,
    separator = ''
)

result = splitter.split_documents(pdf)

print(result[1].page_content)