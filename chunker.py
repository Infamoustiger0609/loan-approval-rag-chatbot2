def chunk_data(df):
    chunks = []
    for _, row in df.iterrows():
        text = " ".join([f"{col}: {row[col]}" for col in df.columns])
        chunks.append(text)
    return chunks