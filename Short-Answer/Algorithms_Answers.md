#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)


b) O(n*log(n))


c) O(n)

## Exercise II

This should be treated a binary sort problem. If you start at floor one and increase upwards if the dropped egg does not break, that minimizes the number of broken eggs, but at a cost of potentially very many dropped eggs. In order to minimize both:

-  I would initialize low and high floor variables, which, on the first iteration, are the ground floor and the highest floor. Drop an egg from the floor that is the midway floor between the high and the low. 
  -If the egg breaks, update the high floor variable to the current floor, and go down to the floor that is the midway point between the high and the low and drop another egg. 
  - If the first egg did not break, instead update the low floor to the current floor, and go up to the floor that is the midway point between the current floor and the high. 

- Repeat this process until the low and high floor are adjacent floors, (make sure to test both of the last high and low floors) and return the highest floor in which the egg did not break.
