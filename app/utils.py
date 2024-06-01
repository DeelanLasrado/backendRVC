from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
import torch  # Ensure PyTorch is imported

model_name = "sentence-transformers/paraphrase-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
nlp = pipeline("feature-extraction", model=model, tokenizer=tokenizer)

def grade_answer(answer_text, answer_key):
    student_embedding = nlp(answer_text)[0]  # Remove [0][0]
    key_embedding = nlp(answer_key)[0]  # Remove [0][0]

    similarity = cosine_similarity(student_embedding, key_embedding)  # Pass embeddings directly

    grade = similarity * 10
    return grade

def cosine_similarity(embedding1, embedding2):
    dot_product = sum(a * b for a, b in zip(embedding1, embedding2))
    norm_a = sum(a * a for a in embedding1) ** 0.5
    norm_b = sum(b * b for b in embedding2) ** 0.5
    return dot_product / (norm_a * norm_b)

