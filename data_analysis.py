import pandas as pd
from matplotlib import pyplot as plt

with open("result.txt") as f:
    content = f.readlines()

df = pd.DataFrame(content)

plt.plot([i for i in range(10000)], [float(i.replace("\n", ""))
         for i in df[0]])
plt.show()

df.to_csv("result.csv")
