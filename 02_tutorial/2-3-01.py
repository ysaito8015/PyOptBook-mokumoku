# 線形計画問題
import pandas as pd
import pulp

# データ取得
stock_df = pd.read_csv("./data/stocks.csv")
require_df = pd.read_csv("./data/requires.csv")
gain_df = pd.read_csv("./data/gains.csv")

# リストの定義
P = gain_df['p'].tolist()
M = stock_df['m'].tolist()

# 定数の定義
stock = {row.m: row.stock for row in stock_df.itertuples()}
# stock = dict(zip(stock_df['m'], stock_df['stock']))
# stock = dict((row.m, row.stock) for row in stock_df.itertuples())
# stock = stock_df.set_index('m').to_dict()['stock']

require = {(row.p, row.m): row.require for row in require_df.itertuples()}

gain = {row.p: row.gain for row in gain_df.itertuples()}

# 数理最適化モデルの定義
problem = pulp.LpProblem('LP2', pulp.LpMaximize)

# 変数の定義
x = pulp.LpVariable.dicts('x', P, cat='Continuous')

# 制約式の定義
for p in P:
    problem += x[p] >= 0

for m in M:
    problem += pulp.lpSum([require[p, m] * x[p] for p in P]) <= stock[m]

# 目的関数の定義
problem += pulp.lpSum([gain[p] * x[p] for p in P])

# 求解
status = problem.solve()

print('Status:', pulp.LpStatus[status])

# 計算結果の表示
for p in P:
    print(p, x[p].value())

print('obj=', problem.objective.value())

# Welcome to the CBC MILP Solver 
# Version: 2.10.3 
# Build Date: Dec 15 2019 
# 
# command line - /home/ysaito/.pyenv/versions/anaconda3-2022.05/lib/python3.9/site-packages/pulp/apis/../solverdir/cbc/linux/64/cbc /tmp/60d37
# e8034794350b5ba68f69696d728-pulp.mps max timeMode elapsed branch printingOptions all solution /tmp/60d37e8034794350b5ba68f69696d728-pulp.sol
#  (default strategy 1)
# At line 2 NAME          MODEL
# At line 3 ROWS
# At line 12 COLUMNS
# At line 30 RHS
# At line 38 BOUNDS
# At line 43 ENDATA
# Problem MODEL has 7 rows, 4 columns and 13 elements
# Coin0008I MODEL read with 0 errors
# Option for timeMode changed from cpu to elapsed
# Presolve 3 (-4) rows, 4 (0) columns and 9 (-4) elements
# 0  Obj -0 Dual inf 17.499996 (4)
# 4  Obj 80.428571
# Optimal - objective value 80.428571
# After Postsolve, objective 80.428571, infeasibilities - dual 0 (0), primal 0 (0)
# Optimal objective 80.42857143 - 4 iterations time 0.002, Presolve 0.00
# Option for printingOptions changed from normal to all
# Total time (CPU seconds):       0.00   (Wallclock seconds):       0.00
# 
# Status: Optimal
# p1 12.142857
# p2 3.5714286
# p3 7.4285714
# p4 0.0
# obj= 80.42857099999999
