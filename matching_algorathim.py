import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MatchingAlgorithm:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def match_jobs(self, resume_skills, job_descriptions):
        # Combine resume skills and job descriptions for TF-IDF
        all_texts = [' '.join(resume_skills)] + job_descriptions
        tfidf_matrix = self.vectorizer.fit_transform(all_texts)

        # Compute cosine similarities
        similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

        # Debugging information
        print(f"TF-IDF Matrix Shape: {tfidf_matrix.shape}")
        print(f"Similarities: {similarities}")

        # Ensure similarities is a list of numbers
        if not isinstance(similarities, (list, np.ndarray)):
            raise ValueError("Similarities should be a list or numpy array")

        return similarities.tolist() if isinstance(similarities, np.ndarray) else similarities




