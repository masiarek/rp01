# open files in 'tests' directory

process all files (using TOML configuration)

if config1 = true 
  remove digits in data
  
  
example - original file - *before* being processed :

[config]
config1 = true

[content]
data = '''
aaa1, aa1, aaaa1
a2, aaa2, aaa2'''


use pytest (fixture or yiled?)

file *after* being processed:

[config]
config1 = true

[content]
data = '''
aaa, aa, aaaa
a, aaa, aaa'''
