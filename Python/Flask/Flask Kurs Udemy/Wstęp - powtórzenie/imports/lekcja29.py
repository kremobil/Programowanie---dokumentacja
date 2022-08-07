# from mymodule import divide
import mymodule as mm
import sys

# print(divide(10, 2))
print(mm.divide(10, 2))
print(sys.path, sys.modules)
print(mm.myadd(4, 50, 23))