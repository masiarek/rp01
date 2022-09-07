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


# use pytest (fixture or yiled?)

file *after* being processed:

[config]
config1 = true

[content]
data = '''
aaa, aa, aaaa
a, aaa, aaa'''


# Example

The file [`test_from_config.py`](tests/test_from_config.py) will read TOML files in the [`tests/config`](tests/config/) directory and run all the tests within the files.

Each TOML file should define the name of the function to be tested and can then define any number of tests. For each test, all necessary parameters should be listed together with `expected` which describes the expected result.

You can run tests from the main (`rp01`) directory as follows:

```console
$ pytest -v
```

The `-v` option adds a little more information about each test, describing the function name, the parameters, and the expected value.
