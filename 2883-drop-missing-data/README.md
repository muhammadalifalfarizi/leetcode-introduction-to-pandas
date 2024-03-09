# 2883. Drop Missing Data

```python
   student_id     name  age
0          32    Piper    5
1         217     None   19
2         779  Georgia   20
3         849   Willow   14
```

There are some rows having missing values in the **``name``** column.
Write a solution to remove the rows with missing values. The result format is in the following example. 

### Explanation
**Input:**
```python
   student_id     name  age
0          32    Piper    5
1         217     None   19
2         779  Georgia   20
3         849   Willow   14
```
**Output:**
```python
   student_id     name  age
0          32    Piper    5
2         779  Georgia   20
3         849   Willow   14
```
### Explanation:

Student with id 217 have empty value in the same column, so it will be removed.