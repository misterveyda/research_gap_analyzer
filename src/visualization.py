import matplotlib.pyplot as plt

def plot_topic_distribution(model):
    plt.bar(range(len(model.components_)), 
            [sum(topic) for topic in model.components_])
    plt.xlabel("Topics")
    plt.ylabel("Weight")
    plt.title("Topic Distribution")
    plt.show()

