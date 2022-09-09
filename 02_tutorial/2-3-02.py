# 整数計画問題
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
problem = pulp.LpProblem('IP', pulp.LpMaximize)

# 変数の定義
x = pulp.LpVariable.dicts('x', P, cat='Integer')

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
# command line - /home/ysaito/.pyenv/versions/anaconda3-2022.05/lib/python3.9/site-packages/pulp/apis/../solverdir/cbc/linux/64/cbc /tmp/8ea51
# 63e2360433bbd6c5e93edc44cc6-pulp.mps max timeMode elapsed branch printingOptions all solution /tmp/8ea5163e2360433bbd6c5e93edc44cc6-pulp.sol
#  (default strategy 1)
# At line 2 NAME          MODEL
# At line 3 ROWS
# At line 12 COLUMNS
# At line 38 RHS
# At line 46 BOUNDS
# At line 51 ENDATA
# Problem MODEL has 7 rows, 4 columns and 13 elements
# Coin0008I MODEL read with 0 errors
# Option for timeMode changed from cpu to elapsed
# Continuous objective value is 80.4286 - 0.00 seconds
# Cgl0004I processed model has 3 rows, 4 columns (4 integer (0 of which binary)) and 9 elements
# Cutoff increment increased from 1e-05 to 0.9999
# Cbc0012I Integer solution of -76 found by DiveCoefficient after 0 iterations and 0 nodes (0.00 seconds)
# Cbc0038I Full problem 3 rows 4 columns, reduced to 3 rows 3 columns
# Cbc0012I Integer solution of -79 found by DiveCoefficient after 1 iterations and 0 nodes (0.00 seconds)
# Cbc0031I 1 added rows had average density of 4
# Cbc0013I At root node, 1 cuts changed objective from -80.428571 to -79 in 2 passes
# Cbc0014I Cut generator 0 (Probing) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
# Cbc0014I Cut generator 1 (Gomory) - 2 row cuts average 4.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is 1
# Cbc0014I Cut generator 2 (Knapsack) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
# Cbc0014I Cut generator 3 (Clique) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
# Cbc0014I Cut generator 4 (MixedIntegerRounding2) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequen
# cy is -100
# Cbc0014I Cut generator 5 (FlowCover) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
# Cbc0001I Search completed - best objective -79, took 1 iterations and 0 nodes (0.00 seconds)
# Cbc0035I Maximum depth 0, 0 variables fixed on reduced cost
# Cuts at root node changed objective from -80.4286 to -79
# Probing was tried 2 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
# Gomory was tried 2 times and created 2 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
# Knapsack was tried 2 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
# Clique was tried 2 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
# MixedIntegerRounding2 was tried 2 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
# FlowCover was tried 2 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
# TwoMirCuts was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
# ZeroHalf was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
# 
# Result - Optimal solution found
# 
# Objective value:                79.00000000
# Enumerated nodes:               0
# Total iterations:               1
# Time (CPU seconds):             0.00
# Time (Wallclock seconds):       0.00
# 
# Option for printingOptions changed from normal to all
# Total time (CPU seconds):       0.00   (Wallclock seconds):       0.00
# 
# Status: Optimal
# p1 13.0
# p2 3.0
# p3 7.0
# p4 -0.0
# obj= 79.0
