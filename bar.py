import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

n_peps=[]
n_rep=[]
n_peps_log10=[]
f = open('newTab2.txt', 'r')
for line in f:
    line = line.rstrip()
    n_peps.append(float(line.split(',')[0]))
    n_rep.append(float(line.split(',')[1]))
for elem in n_peps:
    n_peps_log10.append(np.log10(elem))
plt.bar(n_rep,n_peps_log10, color = 'g')
plt.xticks(np.arange(min(n_rep), max(n_rep),50))
plt.xticks(rotation=90)
plt.title("How Many Peptide Sequences Are Repeated Or Unique" + "\n", fontsize = 20,  fontweight="bold", color = "green")
plt.xlabel("\n" + "Number of repeats in peptide sequences" , fontsize = 12, fontweight="bold", color = "green")
plt.ylabel("Number of peptide sequences (log base 10)" + "\n" + "\n", fontsize = 12, fontweight="bold", color = "green")

plt.show()
'''

#input

df = pd.read_csv('newTab2.txt', header=None, index_col=None)
df.columns = ['Number_of_peptides', 'Number_of_repeats']
df = df.sort_values("Number_of_peptides", ascending=False)
index = np.arange(min(df['Number_of_repeats']), max((df['Number_of_repeats']),50))
#df = pd.DataFrame({'How many repeats':['A', 'B', 'C'], 'How many sequences were repeated':[10, 30, 20]})
ax = df[['log10_Number_of_peptides']].plot(kind='bar')
plt.xticks(np.arange)
plt.show()
#    df.plot.bar(x='Number_of_repeats', y='log10_Number_of_peptides', rot=90)
#plt.xticks(np.arange(min(df['log10_Number_of_peptides'], max(df['log10_Number_of_peptides']) + 1, 50)))

plt.show()
'''
'''
# Data
data = {1:20, 2:15, 3:30,4:35, 5:20, 6:15, 7:30, 8:20,9:20, 10:20}

courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))

# Creating the bars
plt.bar(courses , values , color = 'blue' , width = 0.4)

plt.xlabel("How many repeats")
plt.ylabel("How many sequences were repeated")
plt.title("How many sequences repeated how many times")
plt.show()
'''
