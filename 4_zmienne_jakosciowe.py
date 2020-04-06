import pandas
import collections
import matplotlib.pyplot as plt

sign_names = pandas.read_csv("sign_names.csv")
training_data = pandas.read_pickle("train.p")

labels = training_data["labels"]
cnt = collections.Counter(labels).most_common()
x = [sign_names.iloc[f[0]]['b'] for f in cnt]
y = [f[1] for f in cnt]

plt.figure(figsize=(35, 20), dpi=300)
plt.yticks(range(len(x)), x)
plt.xticks(range(0, max(y), 250))
plt.barh(x, y)
for i in range(len(x)):
    plt.text(y[i] + 10, x[i], str(y[i]), fontdict={'color': 'blue', 'size': 12})
plt.title("Częstość występowania poszczególnych znaków w zestawie danych treningowych", fontdict={'size': 20})
plt.ylabel("Znak")
plt.xlabel("Częstość")
plt.savefig('analiza_czestosci_znaki_drogowe.png')
