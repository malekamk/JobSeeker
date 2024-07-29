class RecommendationEngine:
    def __init__(self, matching_algorithm):
        self.matching_algorithm = matching_algorithm

    def recommend_jobs(self, resume_skills, job_descriptions):
        similarities = self.matching_algorithm.match_jobs(resume_skills, job_descriptions)

        # Debugging information
        print(f"Similarities Type: {type(similarities)}")
        print(f"Similarities Values: {similarities}")

        # Ensure similarities is a valid list of numbers
        if not isinstance(similarities, list) or not all(isinstance(score, (int, float)) for score in similarities):
            raise ValueError("Expected similarities to be a list of numbers")

        # Sort job recommendations based on similarity scores
        recommended_jobs = sorted(enumerate(similarities), key=lambda x: x[1], reverse=True)
        return recommended_jobs


