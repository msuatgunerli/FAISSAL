def run_llm(llm, question, context, context_dependency):
    if context_dependency == "low":
        output = llm(f"### Instruction: Answer the question based on the provided context. ### Question: {question} ### Context: {context} ### Answer:",
            temperature= 0.7, top_k = 10000, repeat_penalty = 1.1, max_tokens = 2048, echo=True) # for 7B
    elif context_dependency == "high":
        output = llm(f"### Instruction: Answer the question based only on the provided context, if the information is not provided in the context you must answer the question by saying that the required information cannot be found in the context. ### Question: {question} ### Context: {context} ### Answer:",
                     temperature= 0.3, top_k = 10000, repeat_penalty = 1.1, max_tokens = 2048, echo=True) # for 13B
    elif context_dependency == "medium":
        output = llm(f"### Instruction: Answer the question based only on the provided context, you are allowed to use external information as a last resort, if and only if the the required information cannot be found in the context. ### Question: {question} ### Context: {context} ### Answer:",
                     temperature= 0.5, top_k = 10000, repeat_penalty = 1.1, max_tokens = 2048, echo=True) # experimental prompt
    else:
        raise ValueError("Invalid prompt style: {}".format(context_dependency))
    return output