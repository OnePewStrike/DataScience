import pandas as pd
import matplotlib.pyplot as plt 

cols = ["fLength", "fWidth", "fSize", "fCone", "fCone1", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]
data = pd.read_csv("../../data/MagicGammaDataset/magic04.data", names=cols)

print(data.head())

def data_transformation(data):
    data["class"] = (data["class"] == "g").astype(int)
    return data

data = data_transformation(data)

for label in cols[:-1]:
    plt.hist(data[data["class"] == 1][label], color="blue", label="gamma", alpha=0.7, density=True)
    plt.hist(data[data["class"] == 0][label], color="red", label="hadron", alpha=0.7, density=True)
    plt.title(label)
    plt.ylabel("Probability")
    plt.xlabel(label)
    plt.legend()
    plt.show()
