#!/usr/bin/env python3
import os
path = input("Enter Directory Path: ")
 
directories=[r for r in os.listdir(path) if os.path.isdir(os.path.join(path, r))]
print(directories)
