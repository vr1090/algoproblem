# solving recursion
- BRI .. big recursion idea
- direct recursion, call of function ada di dalam body
- a base case and a recursive call
- ada processing ada recursive
- head .. recursive dulu, baru processing
- tail .. processing dulu, baru recursive
- postpone action, until the lower has been calculated

# Big recursion idea
- bikin solusi iterative
- bikin dispactcher, kurangin satu aja
- the dispatcher somewhat halfway the solution
- the dispatcher:
    - solve the most trivial case
    - call the iterative, the smaller parameter
    - remove the iterative

# backtrack
- you make a decision, the decision is wrong, then you need to backtrack
- how to implement this in the code?
- choose the path
- keep track of visited point
- 