# Solving LeetCode problems in Python

# Python specific tools
* `map`: Apply a function to every elements in an iterable object and return an iterable object.
* `reduce`: Apply a function to every adjacency pairs through an iterable object and return an object (can be iterable or non-iterable, depends on the function you applied to.)
* `yield`:
* `zip`: Generate a iterable object by grouping the elements in order.
* Parallel assignment: Pack the values on right hand side in a tuple and assign it to the values on left hand side element by element. Note that the value is changing during the assignment. For example, `nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]` in (`041-FirstMissingPositive.py`). When the first assignment of left hand side is done, `nums[i]` has been changed and therefore the `nums[nums[i] - 1]` might refer to other positions.