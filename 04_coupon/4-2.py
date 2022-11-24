import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

prob_df = pd.read_csv('./data/visit_probability.csv')

print(prob_df.shape)
print(prob_df)

ax = {}
fig, (ax[0], ax[1], ax[2]) = plt.subplots(
    1,
    3,
    figsize=(20, 3)
)

for i, ptn in enumerate(['prob_dm1', 'prob_dm2', 'prob_dm3']):
    prob_pivot_df = pd.pivot_table(
        data=prob_df,
        values=ptn,
        columns='freq_cat',
        index='age_cat'
    )
    prob_pivot_df = prob_pivot_df.reindex([
        'age~19',
        'age20~34',
        'age35~49',
        'age50~'
    ])
    sns.heatmap(
        prob_pivot_df,
        vmin=0,
        vmax=1,
        annot=True,
        fmt='.0%',
        cmap='Blues',
        ax=ax[i]
    )
    ax[i].set_title(f'Visit Probability of {ptn}')

plt.savefig('./img/visit_probability.png')
