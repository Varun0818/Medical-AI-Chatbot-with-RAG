!pip install langchain sentence-transformers chromadb llama-cpp-python langchain_community pypdf

from  langchain_community.document_loaders import PyPDFDirectoryLoader 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings 
from langchain.vectorstores import Chroma 
from langchain_community.llms import LlamaCpp
from langchain.chains import RetrievalQA, LLMChain
import os 

# Import the document
loader = PyPDFDirectoryLoader("/content/drive/MyDrive") 
docs =loader.load()

# Chunking
text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=50) 
chunks = text_splitter.split_documents(docs)

# Embeddings Creations
os.environ['HUGGINGFACEHUB_API_TOKEN'] = "your_token"
embeddings = SentenceTransformerEmbeddings (model_name="NeuML/pubmedbert-base-embeddings")

# Vector Store Creation
vectorstore = Chroma.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# LLM model loading
llm= LlamaCpp(
     model_path="/content/drive/MyDrive/BioMistral-7B.Q4_K_S.gguf",
     temperature=0.2,
     max_tokens =2048,
     top_p=1
    )

# Use LLM and retriver and query, to generate final response
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate

template= """
<|context|> 
You are an Medical Assistant that follows the instructions and generate the accurate response based on the query and the context provided.
 Please be truthful and give direct answers. 
</s>
 <[user|>
 {query} 
</s>
 <[assistant|>
"""

prompt = ChatPromptTemplate.from_template(template)

rag_chain = (
    {"context": retriever, "query": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Interactive loop
import sys

while True:
  user_input= input(f"Input query: ")
  if user_input == 'exit':
    print("Exiting...")
    break
  if user_input=="":
    continue
  result = rag_chain.invoke(user_input) 
  print("Answer: ",result)`
