# FAISSAL 
## FAISSAL - Document QA Chatbot using LLaMA 2, FAISS, and LangChain:

Welcome to FAISSAL, a Document QA Chatbot that leverages LLaMA 2, FAISS, and LangChain to provide you with accurate answers from uploaded documents.

## About

FAISSAL allows you to upload an individual document, currently limited to PDF or TXT formats, then it extracts pertinent information from the document and generates answers to your questions that are contextually relevant.

## How to Use

0. **Installing the Required Dependencies and Running the Web App**: Ensure that the required dependencies listed on the requirements.txt file are installed on your local machine. Upon installing the dependencies, you can create a new terminal window within the main folder of this repository and run the following command to launch the Web App on your default browser:

   `streamlit run app.py`

1. **Upload a Document**: Begin by uploading a single document in PDF or TXT format using the "Browse files" button or by dragging and dropping a file.

2. **Select Sentence-Transformers Model**: Choose a Sentence-Transformers model to generate the embeddings. This step uses LangChain's HuggingFaceEmbeddings, which relies on the sentence_transformers Python package to function. The available options are as follows, which should be downloaded automatically if not already present on your local machine:
   - `all-MiniLM-L6-v2`
   - `multi-qa-mpnet-base-dot-v1`

3. **Create Search Index**: The uploaded document will be processed to create a search index using the selected model.

4. **Ask a Question**: Input your question in the provided text field. Feel free to guide the model in generating more extensive responses by providing a target word count (e.g. 250) you'd like the answer to contain. If the generated reponse is too long, it will be truncated using ... at the end.

5. **Generate Context**: The system generates a context for your question based on the uploaded document and your input.

6. **Select LLM Type**: Choose an LLM (Language Model) type for generating a response. Available options are:
   - `LLaMA-7B`
   - `LLaMA-13B`

<span style="color:red">**Make sure to the model_path attribute in the load_llm function within the app.py script, with the appropriate directory path for your locally stored model:** </span>
   - `app.py script line 32: llm = load_llm.load_llm(model_type= model_type, model_path= None)`

Recommended Models:
   - `LLaMA-7B: Download llama-2-7b-chat.ggmlv3.q4_0.bin from the ` [Hugging Face Model Hub](https://huggingface.co/TheBloke/Llama-2-7B-GGML/tree/main).
   - `LLaMA-13B: Download llama-2-13b-chat.ggmlv3.q4_0.bin from the ` [Hugging Face Model Hub](https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/tree/main).

7. **Select Context Dependence Level**: Adjust the context dependence level (set to low if the model struggles with generating context-dependent answers). The options are:
   - `low`
   - `medium`
   - `high`

8. **Generate Response**: Click the "Generate Response" button to run the selected LLM and obtain the answer to your question. The duration of this step typically ranges from 30 to 60 seconds, taking into account the question complexity, context length, and length of the response generated.

## Setup and Dependencies

FAISSAL utilizes several tools and libraries to function:
   - Streamlit: A web application framework for building interactive user interfaces.
   - LLaMA 2: A large language model for text generation and understanding.
   - FAISS: An efficient similarity search and clustering library.
   - LangChain: A library for managing language processing tasks, also powering llama-cpp-python.

## Disclaimer

Please note that FAISSAL's performance may vary depending on the uploaded documents and the complexity of the questions asked. It's recommended to review and verify the answers for accuracy.

---

*This document was generated as a part of the FAISSAL project by @msuatgunerli. For more information, you can visit the [GitHub repository](https://github.com/msuatgunerli/FAISSAL).*
