from sentence_transformers import SentenceTransformer, util
import numpy as np

# Load the pre-trained model
model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')

def grade_answer(answer_text, answer_key):
    
    answer_embedding = model.encode(answer_text, convert_to_tensor=True)
    key_embedding = model.encode(answer_key, convert_to_tensor=True)
    
    
    similarity = util.pytorch_cos_sim(answer_embedding, key_embedding).item()

    
    grade = similarity * 10

    if grade<9:
        grade=0
        
    
    return grade


