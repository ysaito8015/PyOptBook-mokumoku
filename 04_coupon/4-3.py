import pandas as pd
import pulp
import time

cust_df = pd.read_csv('./data/customers.csv')
prob_df = pd.read_csv('./data/visit_probability.csv')

problem = pulp.LpProblem(
    name='DiscountCouponProblem1',
    sense=pulp.LpMaximize
)

# 会員 ID をリストとして抽出
I = cust_df['customer_id'].to_list()

# ダイレクトメールのパターンのリスト
M = [1, 2, 3]

# 各会員に対してどのパターンのダイレクトメールを送付するか決定
xim = {}  # x_{im} の定義
for i in I:
    for m in M:
        xim[i, m] = pulp.LpVariable(
            name=f'xim({i}, {m})',
            cat='Binary'
        )  # {(1, 1): xim(1, _1) ...


print(len(xim))  # 15000 = 5000 * 3

# 要件２
for i in I:
    problem += pulp.lpSum(xim[i, m] for m in M) == 1

# 来店率 P_{im} の定義準備
# 会員リストと昨年度来店回数を結合する
keys = ['age_cat', 'freq_cat']
cust_prob_df = pd.merge(cust_df, prob_df, on=keys)
print(cust_prob_df.head())

# 縦持ちのデータセットにする
cust_prob_ver_df = cust_prob_df.rename(
    columns={'prob_dm1': 1, 'prob_dm2': 2, 'prob_dm3': 3}
).melt(
    id_vars=['customer_id'],
    value_vars=[1, 2, 3],
    var_name='dm',
    value_name='prob'
)
print(cust_prob_ver_df['customer_id'] == 1)

# 来店率 P_{im} の辞書化
Pim = cust_prob_ver_df.set_index(['customer_id', 'dm'])['prob'].to_dict()
print("Pim[1, 1]:")
print(Pim[1, 1])

# 目的関数の実装
problem += pulp.lpSum((Pim[i, m] - Pim[i, 1]) * xim[i, m] for i in I for m in [2, 3])

# 要件4 会員の予算消費期待値の合計は１００万円以下
# dm のパターンとクーポンの金額の辞書
Cm = {1: 0, 2: 1000, 3: 2000}

problem += pulp.lpSum(Cm[m] * Pim[i, m] * xim[i, m] for i in I for m in [2, 3]) <= 1000000

# 要件5 各パターンのダイレクトメールをそれぞれのセグメントに属する会員１０％以上に送付
# N_s: それぞれのセグメントに属する会員数
# Z_is: 会員 i がセグメントに属するか
# S: セグメントのリスト

S = prob_df['segment_id'].to_list()
print(S)

# 各セグメントとそのセグメントに属する顧客数を対応させる辞書の作成
Ns = cust_prob_df.groupby('segment_id')['customer_id'].count().to_dict()
print(Ns)
print()

# Z_is 会員がセグメントに属するかどうかを表す定数
# if 文で使う Si 辞書を定義
# ある会員 i がセグメント s に属するかどうか
Si = cust_prob_df.set_index('customer_id')['segment_id'].to_dict()

# 制約条件の実装
for s in S:
    for m in M:
        problem += pulp.lpSum(xim[i, m] for i in I if Si[i] == s) >= 0.1 * Ns[s]


# 求解
time_start = time.time()
status = problem.solve()
time_stop = time.time()

print(f'ステータス:{pulp.LpStatus[status]}')
print(f'目的関数値:{pulp.value(problem.objective):.4}')
print(f'計算時間:{(time_stop - time_start):.3}（秒）')
