import sys

print(sys.version)
print(sys.executable)


def greet(who_to_great):
    greeting = 'Hello, {}'.format(who_to_great)
    return greeting


print(greet('World'))
print(greet('Shuja'))
 