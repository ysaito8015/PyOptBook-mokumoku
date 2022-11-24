import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cust_df = pd.read_csv("./data/customers.csv")

print(cust_df.shape)
print(cust_df.head())  # first five rows
print(cust_df.dtypes)  # data types

# print histogram
cust_df['age_cat'].hist()
plt.savefig('./img/age_cat_hist.png')

cust_df['freq_cat'].hist()
plt.savefig('./img/freq_cat_hist.png')

cust_pivot_df = pd.pivot_table(
    data=cust_df,
    values='customer_id',
    columns='freq_cat',
    index='age_cat',
    aggfunc='count'
)
cust_pivot_df = cust_pivot_df.reindex([
    'age~19',
    'age20~34',
    'age35~49',
    'age50~'
])

print(cust_pivot_df.head())

sns.heatmap(
    cust_pivot_df,
    annot=True,
    fmt='d',
    cmap='Blues'
)

plt.savefig('./img/heatmap_age_vs_freq.png')
