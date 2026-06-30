# Class random

Before each use of the `random` module, add the statement `import random` to the top of the Python file.

- **`randint(start, end)`**: Randomly generates an integer between `start` and `end`.
  - `start`: Starting value of the range (included).
  - `end`: Ending value of the range (included).
- **`random()`**: Randomly generates a floating point number between 0 and 1.
- **`random.uniform(start, end)`**: Randomly generates a floating point number between `start` and `end`.
  - `start`: Starting value of the range (included).
  - `end`: Ending value of the range (included).
- **`random.getrandbits(size)`**: Generates an integer with `size` random bits.
  - For example: `size = 4` generates an integer in the range 0 to `0b1111`; `size = 8` generates an integer in the range 0 to `0b11111111`.
- **`random.randrange(start, end, step)`**: Randomly generates a positive integer in the range from `start` to `end`, incrementing by `step`.
  - `start`: Starting value of the range (included).
  - `end`: Ending value of the range (included).
  - `step`: An integer specifying the increment.
- **`random.seed(sed)`**: Specifies a random seed, usually applied in conjunction with other random number generators.
  - `sed`: Random seed — a starting point for generating random numbers.
- **`random.choice(obj)`**: Randomly generates an element from the object `obj`.
  - `obj`: A list of elements.

> random is a standard module included with python run time,

> Adapted from [Python_Tutorial.pdf](../Python_Tutorial.pdf) — Chapter 5, RGB LED