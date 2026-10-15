# Lets try to make some plots for finding the conditions that can help the predicitons

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data_train = pd.read_csv("Dataset/train.csv")
print(data_train.info(),"\n")




# Replotting the updated the unique models


side_a = data_train.groupby('model_a').agg(
    a_responses=('id', 'count'),
    a_wins=('winner_model_a', 'sum'),
    a_losses=('winner_model_b', 'sum'),
    a_ties=('winner_tie', 'sum'),
)

side_b = data_train.groupby('model_b').agg(
    b_responses=('id', 'count'),
    b_wins=('winner_model_b', 'sum'),
    b_losses=('winner_model_a', 'sum'),
    b_ties=('winner_tie', 'sum'),
)

unique_models = side_a.join(side_b, how='outer').astype(int)
unique_models.index.name = 'model'

unique_models['combined_both_responses'] = unique_models['a_responses'] + unique_models['b_responses']
unique_models['wins']   = unique_models['a_wins']   + unique_models['b_wins']
unique_models['losses'] = unique_models['a_losses'] + unique_models['b_losses']
unique_models['ties']   = unique_models['a_ties']   + unique_models['b_ties']
unique_models['win_rate'] = unique_models['wins'] / unique_models['combined_both_responses']
unique_models['a_win_rate'] = unique_models['a_wins'] / unique_models['a_responses']
unique_models['b_win_rate'] = unique_models['b_wins'] / unique_models['b_responses']

dist = unique_models.reset_index()





count_cols = ['a_wins', 'a_losses', 'a_ties', 'b_wins', 'b_losses', 'b_ties']
rate_cols  = ['win_rate', 'a_win_rate', 'b_win_rate']

# Sort by total games, so the busiest models are on top
order = unique_models['combined_both_responses'].sort_values(ascending=False).index

counts = unique_models.loc[order, count_cols]
rates  = unique_models.loc[order, rate_cols]

fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(16, 22),
    gridspec_kw={'width_ratios': [2, 1]}
)

sns.heatmap(counts, annot=True, fmt=',d', cmap='YlGnBu',
            linewidths=0.5, cbar_kws={'label': 'Count'}, ax=ax1)
ax1.set_title('Wins, Losses, Ties by Position (A / B)')
ax1.set_xlabel('Outcome')
ax1.set_ylabel('Model')

sns.heatmap(rates, annot=True, fmt='.2f', cmap='RdYlGn', vmin=0, vmax=1,
            linewidths=0.5, cbar_kws={'label': 'Win rate'}, ax=ax2)
ax2.set_title('Win Rates')
ax2.set_xlabel('')
ax2.set_ylabel('')
ax2.set_yticklabels([])   # model names already shown on the left

plt.tight_layout()
fig.savefig('unique_model_distribution.png', dpi=200, bbox_inches='tight')
plt.show()




# Failed Plot 

# Saving the plot of unique model distributions
# a = data_train.groupby('model_a').agg(  
#     win_count=('winner_model_a', 'sum'),
#     lose_count=('winner_model_b', 'sum'),
#     tie_count=('winner_tie', 'sum')
# )
# b = data_train.groupby('model_b').agg(
#     win_count=('winner_model_b', 'sum'),
#     lose_count=('winner_model_a', 'sum'),
#     tie_count=('winner_tie', 'sum')
# )

# plot_data = a.add(b).astype(int)
# plot_data.index.name = 'model'
# plot_data = plot_data.loc[
#     plot_data.sum(axis=1).sort_values(ascending=False).index
# ]

# fig, ax = plt.subplots(figsize=(10, 20))
# sns.heatmap(
#     plot_data,
#     annot=True,
#     fmt=',d',
#     cmap='YlGnBu',
#     linewidths=0.5,
#     cbar_kws={'label': 'Count'},
#     ax=ax
# )

# ax.set_title('Unique Model Distributions')
# ax.set_xlabel('Outcome')
# ax.set_ylabel('Model')
# plt.tight_layout()
# plt.savefig("unique_model_distribution.png", dpi=300, bbox_inches="tight")
# plt.show()