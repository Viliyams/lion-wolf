import itertools

def brute_force(target, characters, max_length):
    for length in range(1, max_length + 1):
        for attempt in itertools.product(characters, import itertools):

def brute_force(target, characters, max_length):
    for length in range(1, max_length + 1):
        for attempt in itertools.product(characters, repeat=length):
            password = ''.join(attempt)
            if password == target:
                return password

# Example usage
target_password = "password123"
character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
maximum_length = 8

result = brute_force(target_password, character_set, maximum_length)
print("Found password:", result)
