# Hungarian Algorithm

Implementation of the Hungarian (Munkres) Algorithm using Python and NumPy.

References can be found at:
- http://www.ams.jhu.edu/~castello/362/Handouts/hungarian.pdf
- http://weber.ucsd.edu/~vcrawfor/hungar.pdf
- http://en.wikipedia.org/wiki/Hungarian_algorithm
- http://www.public.iastate.edu/~ddoty/HungarianAlgorithm.html
- http://www.clapper.org/software/python/munkres/


## Features

- Automatic padding wih zeros if the matrix is not square.

## Requirements

- Core requirements
  - Python 3.x
  - numpy

- To run the tests
  - pytest


## Example

Calling the hungarian class on a cost matrix can be done as follows:
```python
from hungarian import hungarian

hungarian = Hungarian(cost_matrix)
hungarian.calculate()

# or
hungarian = Hungarian()
hungarian.calculate(cost_matrix)
```

If it's a profit matrix you have instead, you could use both:
```python
hungarian = Hungarian(profit_matrix, is_profit_matrix=True)

#or
cost_matrix = Hungarian.make_cost_matrix(profit_matrix)
hungarian   = Hungarian(cost_matrix)
```

Getting the result and total potential after calculation is done with:
```python
hungarian.get_results()
hungarian.get_total_potential()
```
