import pulp

problem = pulp.LpProblem('LP', pulp.LpMaximize)

x = pulp.LpVariable('x', cat='Continuous')
y = pulp.LpVariable('y', cat='Continuous')

problem += 1 * x + 3 * y <= 30
problem += 2 * x + 1 * y <= 40
problem += x >= 0
problem += y >= 0
# 目的関数、制約条件はない
problem += x + 2 * y

status = problem.solve()

print('Status:', pulp.LpStatus[status])
print('x=', x.value(), 'y=', y.value(), 'obj=', problem.objective.value())

# Welcome to the CBC MILP Solver 
# Version: 2.10.3 
# Build Date: Dec 15 2019 
# 
# command line - /home/ysaito/.pyenv/versions/anaconda3-2022.05/lib/python3.9/site-packages/pulp/apis/../solverdir/cbc/linux/64/cbc /tmp/f49fc
# 1551766400091901f296e0ab32a-pulp.mps max timeMode elapsed branch printingOptions all solution /tmp/f49fc1551766400091901f296e0ab32a-pulp.sol
#  (default strategy 1)
# At line 2 NAME          MODEL
# At line 3 ROWS
# At line 9 COLUMNS
# At line 18 RHS
# At line 23 BOUNDS
# At line 26 ENDATA
# Problem MODEL has 4 rows, 2 columns and 6 elements
# Coin0008I MODEL read with 0 errors
# Option for timeMode changed from cpu to elapsed
# Presolve 2 (-2) rows, 2 (0) columns and 4 (-2) elements
# 0  Obj -0 Dual inf 2.999998 (2)
# 2  Obj 26
# Optimal - objective value 26
# After Postsolve, objective 26, infeasibilities - dual 0 (0), primal 0 (0)
# Optimal objective 26 - 2 iterations time 0.002, Presolve 0.00
# Option for printingOptions changed from normal to all
# Total time (CPU seconds):       0.00   (Wallclock seconds):       0.00
# 
# Status: Optimal
# x= 18.0 y= 4.0 obj= 26.0
