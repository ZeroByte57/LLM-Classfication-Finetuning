# Lets try to make some plots for finding the conditions that can help the predicitons

import matplotlib.pyplot as plt
import pandas as pd

train_data = pd.read_csv("Dataset/train.csv")
print(train_data.info(),"\n")
print(train_data.head(),"\n")
print(train_data.describe(),"\n")


'''
Conditions & data patterns:
    len of the response effects the user preference (more or less).
    most winning model
    impact of tie count models
'''

# input_features = train_data['model_a'],train_data['model_b'],train_data['response_a'],train_data['response_b']
# target_labels = train_data['winner_model_a'],train_data['winner_model_b'],train_data['winner_tie']

# input_features = pd.DataFrame(train_data[['model_a','model_b','response_a','response_b']])
# target_labels = pd.DataFrame(train_data[['winner_model_a','winner_model_b','winner_tie']])

input_fetures = id, prompt, response_a, response_b
output = id, model_a_prob, model_b_prob, tie_prob


'''
Plots:
    for large responses between models
    winning, loosing and tie models
'''

print(target_labels,input_features)
# plt.plot(target_labels)
# plt.plot(input_features)
plt.show()

