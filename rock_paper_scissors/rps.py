#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  options = [['rock'], ['paper'], ['scissors']] 

  if n == 0:
    return [[]]
    
  if n == 1:
    return options
  
  final = []

  first = rock_paper_scissors(n - 1)

  for i in first:
    for m in options:
      rounds = i + m
      final.append(rounds)
  return final


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')