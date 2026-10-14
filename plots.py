# Lets try to make some plots for finding the conditions that can help the predicitons

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data_train = pd.read_csv("Dataset/train.csv")
print(data_train.info(),"\n")



# Saving the plot of unique model distributions
a = data_train.groupby('model_a').agg(  
    win_count=('winner_model_a', 'sum'),
    lose_count=('winner_model_b', 'sum'),
    tie_count=('winner_tie', 'sum')
)
b = data_train.groupby('model_b').agg(
    win_count=('winner_model_b', 'sum'),
    lose_count=('winner_model_a', 'sum'),
    tie_count=('winner_tie', 'sum')
)

plot_data = a.add(b).astype(int)
plot_data.index.name = 'model'
plot_data = plot_data.loc[
    plot_data.sum(axis=1).sort_values(ascending=False).index
]

fig, ax = plt.subplots(figsize=(10, 20))
sns.heatmap(
    plot_data,
    annot=True,
    fmt=',d',
    cmap='YlGnBu',
    linewidths=0.5,
    cbar_kws={'label': 'Count'},
    ax=ax
)

ax.set_title('Unique Model Distributions')
ax.set_xlabel('Outcome')
ax.set_ylabel('Model')
plt.tight_layout()
plt.savefig("unique_model_distribution.png", dpi=300, bbox_inches="tight")
plt.show()