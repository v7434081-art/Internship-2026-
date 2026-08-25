import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

resume = """
Python developer with two years of experience.
I build REST APIs with Flask, write SQL queries,
and analyse data with pandas. BCA graduate.
"""

job = """
Python developer wanted. Build REST APIs with Flask,
write SQL queries, and analyse data with pandas.
Train machine learning models with scikit-learn
and deploy machine learning services to AWS.
"""

def check_resume(resume, job):

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume, job])

    score = cosine_similarity(vectors[0], vectors[1])[0][0]

    words = vectorizer.get_feature_names_out()
    job_weights = vectors[1].toarray()[0]

    resume_words = set(re.findall(r"[a-z0-9]+", resume.lower()))

    missing = []

    for word, weight in zip(words, job_weights):

        if weight > 0.1 and word not in resume_words:
            missing.append((word, weight))

    missing.sort(key=lambda x: x[1], reverse=True)

    return score, missing

score, missing = check_resume(resume, job)

print("Resume Match Score:", round(score * 100, 2), "%")

print("\nMissing Keywords:")

for word, weight in missing:
    print(word, "->", round(weight, 2))

print("\nTotal Missing Keywords:", len(missing))