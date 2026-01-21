from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def extract_topics(documents, num_topics=5):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(documents)

    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(tfidf)

    return lda, vectorizer

