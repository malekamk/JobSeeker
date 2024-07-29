import spacy

class JobDescriptionParser:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def parse_job_description(self, job_description):
        doc = self.nlp(job_description)
        required_skills = self.extract_required_skills(doc)
        return required_skills

    def extract_required_skills(self, doc):
        # Example: Extract required skills using keyword matching or NER
        required_skills = []
        for token in doc:
            if token.pos_ == 'NOUN':
                required_skills.append(token.text)
        return required_skills

