## Hook Exercises

### 1. Debugging 
Directory 
```
./increment_dictionary_values
```
Command
```
python ./main.py
```

### 2. Write a function & tests 
Directory 
```
./largest_lost
```
Command
```
python ./main.py
```
#### Assumption
Prices are all integer type

We don't need to buy and sell if no lost.

### 2. Design a set of classes
Directory 
```
./hook_sql
```
Command
```
python ./main.py
```
#### Description
It has a main class HookTable which contains four fields (id, date, rating, url) queries,
the fields query can be chained in any combinations. However, the combination only supports
'AND' relationship for now. 

With splitting the query utils and data_access, we are free from mocking the database all the time,
and it's easy to extend the query functions by adding more query utilities.