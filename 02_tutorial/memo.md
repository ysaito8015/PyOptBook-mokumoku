# Resources
- PuLP document
    - https://coin-or.github.io/pulp
- GitHub
    - https://github.com/coin-or/pulp


# Examples from Document
- check PuLp


```shell
$ pulptest
```

or

```python
>> import pulp
>> pulp.pulpTestAll()
```

- output


```shell
Python 3.9.12 (main, Apr  5 2022, 06:56:58) 
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pulp
>>> pulp.pulpTestAll()
ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
 Test that logic put in place for deprecation handling of indexs works
.        Testing 'indexs' param continues to work for LpVariable.dicts
         Testing 'indexs' param continues to work for LpVariable.matrix
.        Testing 'indices' argument works in LpVariable.dicts
         Testing 'indices' param continues to work for LpVariable.matrix
.        Testing invalid status
.        Testing continuous LP solution - export dict
.        Testing export dict for LP
.        Testing export dict MIP
.        Testing maximize continuous LP solution
.        Testing continuous LP solution - export JSON
.        Testing continuous LP solution - export solver dict
.        Testing continuous LP solution - export solver JSON
..       Testing reading MPS files - binary variable, no constraint names
.        Testing reading MPS files - integer variable
.        Testing reading MPS files - maximize
..       Testing invalid var names
.        Testing logPath argument
.        Testing makeDict general behavior
.        Testing makeDict default value behavior
.        Testing measuring optimization time
.        Testing the availability of the function pulpTestAll
.        Testing zero subtraction
.        Testing inconsistent lp solution
.        Testing continuous LP solution
.        Testing maximize continuous LP solution
.        Testing unbounded continuous LP solution
.        Testing Long Names
.        Testing repeated Names
.        Testing zero constraint
.        Testing zero objective
.        Testing LpVariable (not LpAffineExpression) objective
.        Testing Long lines in LP
.        Testing LpAffineExpression divide
.        Testing MIP solution
.        Testing MIP solution with floats in objective
.        Testing Initial value in MIP solution
.        Testing fixing value in MIP solution
.        Testing MIP relaxation
.        Testing feasibility problem (no objective)
.        Testing an infeasible problem
.        Testing an integer infeasible problem
.        Testing another integer infeasible problem
.        Testing column based modelling
..       Testing dual variables and slacks reporting
...      Testing fractional constraints
.        Testing elastic constraints (no change)
.        Testing elastic constraints (freebound)
.        Testing elastic constraints (penalty unchanged)
.        Testing elastic constraints (penalty unbounded)
.        Testing timeLimit argument
...sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
----------------------------------------------------------------------
Ran 840 tests in 10.928s

OK (skipped=784)
```
