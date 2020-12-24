# HealthHero Assignment
Please check `solution1.py` and `solution2.py` for each problem

## Problem 1
The question asks to implement only `my_func` as a generator, so the logic of 
checking if the threshold value was reached is not implemented in the solution. 

A quick example is added to `__main__`, so you can run to print out the 
output of he function.

```bash
python solution1.py

0
2
2
6
6
12
12
20
```


## Problem 2

Please see `solution2.py` for the implementation details


### Usage
In your python function import `count_vowels_and_consonants` and call it with a string argument:

e.g.: 

```python
count_vowels_and_consonants('Potato')
```
that will result in 

```bash
2020-12-24 18:51:59,506 35923 __main__ WARNING: SQlite DB mydb.sqlite doesn't exist, will create a new one
2020-12-24 18:51:59,511 35923 __main__ INFO: Created a new SQlite DB: mydb.sqlite
2020-12-24 18:51:59,511 35923 __main__ DEBUG: Normalizing input word of: Potato
2020-12-24 18:51:59,511 35923 __main__ DEBUG: After normalization result is potato 
2020-12-24 18:51:59,511 35923 __main__ DEBUG: Adding {'word': 'potato', 'numVowels': 3, 'numConsonants': 3, 'createdOn': datetime.datetime(2020, 12, 24, 18, 51, 59, 511354)} to database
Last added 5 items in the DB are

word                  numVowels   numConsonants   createdOn                
potato                3           3               2020-12-24 18:51:59.511354
```

> Notes: 
> - It crates the DB if not already created.
> - Word itself is the primary key, meaning you cannot add the same word twice
> - Any punctuation and whitespace is removed and only lowercased version is saved to DB

