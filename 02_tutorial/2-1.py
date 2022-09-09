import pulp

# 数理モデルの定義
# 第１引数、'SLE', 任意の名前、ここではは連立一次方程式(Simultaneous Linear Equations
# 第２引数、最大化問題を解くという引数
problem = pulp.LpProblem('SLE', pulp.LpMaximize)
# >>> print(problem)
# SLE:
# MAXIMIZE
# None
# VARIABLES

# 変数の定義
# 第１引数、'x', 'y' 任意の名前
# 第２引数、連続変数であることを指定
x = pulp.LpVariable('x', cat='Continuous')
y = pulp.LpVariable('y', cat='Continuous')

# 連立一次方程式を定義
# 制約条件を数理モデルに追加している += 演算子で

problem += 120 * x + 150 * y == 1440
# 別の書き方
# problem.addConstratint(120 * x + 150 * y == 1440)
problem += x + y == 10
# >>> print(problem)
# SLE:
# MAXIMIZE
# None
# SUBJECT TO
# _C1: 120 x + 150 y = 1440
#
# _C2: x + y = 10
#
# VARIABLES
# x free Continuous
# y free Continuous

status = problem.solve()

# solve() の結果の表示
print('Status:', pulp.LpStatus[status])
# 値の取り出し
print('x=', x.value(), 'y=', y.value())


# Welcome to the CBC MILP Solver 
# Version: 2.10.3 
# Build Date: Dec 15 2019 
# 
# command line - /home/ysaito/.pyenv/versions/anaconda3-2022.05/lib/python3.9/site-packages/pulp/apis/../solverdir/cbc/linux/64/cbc /tmp/09f41
# 44e1d764da7bf28db68e00e1e8d-pulp.mps max timeMode elapsed branch printingOptions all solution /tmp/09f4144e1d764da7bf28db68e00e1e8d-pulp.sol
#  (default strategy 1)
# At line 2 NAME          MODEL
# At line 3 ROWS
# At line 7 COLUMNS
# At line 13 RHS
# At line 16 BOUNDS
# At line 20 ENDATA
# Problem MODEL has 2 rows, 3 columns and 4 elements
# Coin0008I MODEL read with 0 errors
# Option for timeMode changed from cpu to elapsed
# Presolve 0 (-2) rows, 0 (-3) columns and 0 (-4) elements
# Empty problem - 0 rows, 0 columns and 0 elements
# Optimal - objective value -0
# After Postsolve, objective 0, infeasibilities - dual 0 (0), primal 0 (0)
# Optimal objective 0 - 0 iterations time 0.002, Presolve 0.00
# Option for printingOptions changed from normal to all
# Total time (CPU seconds):       0.00   (Wallclock seconds):       0.00
# 
# Status: Optimal
# x= 2.0 y= 8.0
