@log()
def add(x, y):
return x + y


def test_log_ok(capsys):
result = add(4,5)
assert result == 9
captured = capsys.readouterr()
assert 'add ok. Result: 9' in captured.out




def log(filename=None):
def wrapper(func):
@wraps(func)
def inner(*args, **kwargs):

try:
result = func(*args, **kwargs)
message = f"{func.__name__} ok. Result: {result}"
except Exception as e:
message = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
if filename:
with open(f"{filename}.txt", "a", encoding="utf-8") as file:
file.write(message + "\n")
else:
print(f"{message}")
else:
if filename:
with open(f"{filename}.txt", "a", encoding="utf-8") as file:
file.write(message + "\n")
else:
print(f"{message}")
return result

return inner
return wrapper