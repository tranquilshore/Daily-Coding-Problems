'''
Given a function foo() that returns integers from 1 to 5 with equal probability, write a function that returns integers from 1 to 7 with equal probability using foo() only. 

The method mentioned here returns number from 1 to 7 with equal probability, which is 3/25 for each number.
use a 2-D array of 5x5 size. It gives you a number from 1-7 with probability 3/25.


int myrand () 
{
  int arr[][] = {{1,2,3,4,5},
                 {6,7,1,2,3},
                 {4,5,6,7,1},
                 {2,3,4,5,6},
                 {7,0,0,0,0}};


int n1 = foo();
int n2 = foo();


int val = arr[n1][n2];


if (val == 0)
  return myrand();


return val;
}

'''

