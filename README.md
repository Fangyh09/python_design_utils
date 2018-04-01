# python_design_utils
some useful python patterns

## Cache Pattern

At 1st call, it will store the object persistently.

From 2nd call, it will return the stored object.

[cache.py](https://github.com/Fangyh09/python_design_utils/blob/master/cache.py)

Example:
```python
class TrainDatabase(DataBase):
    def get_data(self):
        ...
        return data
cache = Cache("/home/persistent/")
cache.fetch("train", TrainDatabase())
```


## Parameter Pattern

Add several parameters without using dict.

Dict has to add multiple `"`s.

[parameter.py](https://github.com/Fangyh09/python_design_utils/blob/master/parameter.py)

Example: 
```python
para_list = ParameterList()
para_list.add_item(foo=1, bar=2)
fun(**para_list.get_item())
```
