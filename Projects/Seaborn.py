#%%
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5])

plt.show()
#%%
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()
#%%

import seaborn as sns
df = sns.load_dataset('titanic')
print(df.head())