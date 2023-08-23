import re

def clean_text(text):
    # Remove leading and trailing whitespace
    text = text.strip()
    
    # Remove bullet points and special characters
    text = re.sub(r'•', '', text)  # Replace bullet points with an empty string
    text = re.sub(r'[^\w\s@.-]', '', text)  # Remove non-alphanumeric characters except @ and .
    
    # Remove emojis using regex (you may need to expand this list)
    emoji_pattern = re.compile("["
                               "\U0001F600-\U0001F64F"  # Emojis
                               "\U0001F300-\U0001F5FF"  # Symbols & Pictographs
                               "\U0001F680-\U0001F6FF"  # Transport & Map Symbols
                               "\U0001F700-\U0001F77F"  # Alchemical Symbols
                               "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                               "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                               "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                               "\U0001FA00-\U0001FA6F"  # Chess Symbols
                               "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                               "\U00002702-\U000027B0"  # Dingbats
                               "\U000024C2"  # Enclosed Alphanumeric Supplement
                               "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)
    #text = text.lower()

    # Testing cleanup
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text