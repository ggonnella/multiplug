#!/usr/bin/env python3
"""
Does nothing, for test purposes
"""

ID =      "fake7"
VERSION = "0.1.0"
INPUT = "test"
OUTPUT =  ["g3a"]

def compute(filename, **kwargs):
  return [10, 2.3], ["test\tthis is a test by fake7"]

def fake_data():
  for acc in ["A1","A2","A3","A4"]:
    print("\t".join([acc]+[str(e) for e in compute(acc)[0]]))

if __name__ == "__main__":
  fake_data()