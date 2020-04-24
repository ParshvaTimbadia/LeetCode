#I executed this file in my IDE please make the required changes as per Leetcode.
***
Problem Statement #
Given an array of points in the a 2D2D plane, find ‘K’ closest points to the origin.

Example 1:

Input: points = [[1,2],[1,3]], K = 1
Output: [[1,2]]
Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
The Euclidean distance between (1, 3) and the origin is sqrt(10).
Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.
Example 2:

Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
Output: [[1, 3], [2, -1]]
***

from __future__ import print_function
from heapq import *


class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def print_point(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

#ADD NOTE HERE
  def __lt__(self, other):
    return self.distance_from_origin() > other.distance_from_origin()  

  def distance_from_origin(self):

    return (self.x*self.x) + (self.y*self.y) 

def find_closest_points(points, k):
  result = []
  for i in range(k):
    heappush(result, points[i] )

  for i in range(k,len(points)):
    if points[i].distance_from_origin() < result[0].distance_from_origin():
      heappop(result)
      heappush(result, points[i])

  return list(result)    
  

    
  





def main():

  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
   point.print_point()


main()


