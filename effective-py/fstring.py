key = 'key'
value = 12.22222
f_string = f'{key:<10} = {value:.2f}'
print(f_string)
# Two conversion flags are currently supported: '!s' which calls str() on the value, and '!r' which calls repr().
num = "ness"
f_string = f'{num!r}'
print(f_string)
f_string = f'{num!s}'
print(f_string)