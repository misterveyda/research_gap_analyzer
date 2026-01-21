def identify_gaps(topic_model, feature_names, top_n=10):
    gaps = {}
    for idx, topic in enumerate(topic_model.components_):
        gaps[f"Topic {idx+1}"] = [
            feature_names[i]
            for i in topic.argsort()[:-top_n - 1:-1]
        ]
    return gaps

