# python_design_utils
some smart python classes

## Cache Pattern
`cache.py`
At 1st call, it will store the object persistently.
From 2nd call, it will return the stored object.

Example:
```python
class TrainDatabase(DataBase):
    def get_data(self):
        ...
        return data
cache = Cache("/home/persistent/")
cache.fetch("train", TrainDatabase())
```