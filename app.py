import streamlit as st
from utils import df_from_doc, faiss_search, create_search_index, wrap_print, generate_context, load_llm, run_llm
import pathlib
from tempfile import NamedTemporaryFile

st.title("FAISSAL")
st.subheader("Document QA Chatbot using LLaMA 2, FAISS, and LangChain")
st.text("by @msuatgunerli")

st.divider()

uploaded_file = st.file_uploader("Upload a Document:", accept_multiple_files=False, type=['pdf', 'txt'])

if uploaded_file is not None:
    filetype = pathlib.Path(uploaded_file.name).suffix
    with NamedTemporaryFile(dir='.', suffix=filetype) as f:
        f.write(uploaded_file.getbuffer())
        docs = df_from_doc.df_from_doc(f.name, str(filetype).replace(".", ""))
    
    model_name = st.selectbox("Select Sentence-Transformers Model for Embeddings:", ["all-MiniLM-L6-v2", "multi-qa-mpnet-base-dot-v1"])

    pkl = create_search_index.create_search_index(docs, model_name)

    question = st.text_input("Ask a Question:")

    context = generate_context.generate_context(pkl, question, model_name, num_results = 5)

    st.write("Estimated Context Length:", round(4/3*len(context.split())), "tokens", "\n")
    wrap_print.wrap_print(context)

    model_type = st.selectbox("Select LLM Type:", ["LLaMA-7B", "LLaMA-13B"])
    llm = load_llm.load_llm(model_type= model_type)

    context_dependency = st.selectbox("Select Context Dependence Level (set to low if the model is failing to generate context dependent answers):", ["low", "medium", "high"])

    if st.button("Generate Response"):
        st.write("Running, may take up to 60 seconds...")
        with st.spinner(f"Running {model_type}..."):
            output = run_llm.run_llm(llm, question, context, context_dependency)

        if output["choices"][0]["text"].split("###")[4][-1] != ".":
            st.success(output["choices"][0]["text"].split("###")[4] + "...")
        elif output["choices"][0]["text"].split("###")[4][-1] == ".":
            st.success(output["choices"][0]["text"].split("###")[4])