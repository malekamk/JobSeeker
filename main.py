from ResumeParser import ResumeParser
from job_description import JobDescriptionParser
from matching_algorathim import MatchingAlgorithm
from recommendation_engine import RecommendationEngine

def main():
    resume_skills = ["Python", "Django", "Machine Learning"]
    job_descriptions = [
        "Software Engineer with Python experience",
        "Data Scientist specializing in Machine Learning",
        "Backend Developer with Django expertise"
    ]
    
    # Create instances of the algorithm and recommendation engine
    matching_algorithm = MatchingAlgorithm()
    recommendation_engine = RecommendationEngine(matching_algorithm)
    
    # Get recommended jobs
    recommended_jobs = recommendation_engine.recommend_jobs(resume_skills, job_descriptions)
    
    # Print results
    for job_index, score in recommended_jobs:
        print(f"Job {job_index + 1} with similarity score: {score:.2f}")

if __name__ == '__main__':
    main()

