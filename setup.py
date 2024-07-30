'''
    ---注意可以运行
    # python install_libraries.py
'''

import subprocess

# Define the libraries to install
libraries = ['tensorflow', 'torch', 'matplotlib', 'pandas', 'numpy']

# Install each library using pip
for lib in libraries:
    subprocess.check_call(['pip', 'install', lib])

print("Libraries installed successfully!")

import collections

point = collections.namedtuple('Points', ['x', 'y'])
p1 = point(2, 3)
p2 = point(4, 2)

print(p1) # Points(x=2, y=3)
print(p2) # Points(x=4, y=2)
# 用 isinstance 判断其类型
print(isinstance(p1, point)) # True
print(isinstance(p1, tuple)) # True
