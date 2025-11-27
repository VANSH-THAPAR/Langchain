from langchain_text_splitters import RecursiveCharacterTextSplitter

code = """
class TextBasedTextSplitter:
    def __init__(self, chunk_size=100, chunk_overlap=0):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
    def split_text(self, text):
        return self.splitter.split_text(text)
"""
splitter = RecursiveCharacterTextSplitter.from_language(
    # here we get more methods not just for code but for markdown, json etc.
    language = "python",
    chunk_size = 300,
    chunk_overlap = 0
)

chunks = splitter.split_text(code)

print(chunks[0])
print("-----")
print(chunks[1])