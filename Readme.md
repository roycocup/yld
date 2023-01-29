We are building a data processor in Python. The destiny of the data is a legacy system that doesn't support nested dictionaries.

We need to develop a custom normalisation to interact with that destiny.

# Instructions

Take a dictionary of the form:

```
{
  "d": 2,
  "a": {
    "b": {
      "c": 1
    }
  }
}
```

And return a dictionary where properties are only one level deep, with their depth represented in dot notation.

`{ "a.b.c": 1, "d": 2 }`

For the exercise:

* Do not concern yourself with primitives, edge cases, securty, or performance;
* Assume you have safe valid (but arbitrarily nested) objects;
* Assume there are no circular references in the objects you receive;
* You can search things online, as long as you're not searching for a solution;
* Do not use Github Copilot or similar tool;
* You can use any editor you feel comfortable with.

```
def challenge(d):
    res = dict()
    return res
```
