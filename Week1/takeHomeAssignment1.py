# 1) Count vowels in a word (a, e, i, o, u)
def count_vowels(word: str) -> int:
    vowels = set("aeiou")
    return sum(1 for ch in word.lower() if ch in vowels)

# Demo:
print("1) Vowel count:", count_vowels(input("Enter a word: ")))


# 2) Print each animal in ALL CAPS
animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
print("2) Animals in caps:")
for animal in animals:
    print(animal.upper())


# 3) 1..20 with odd/even
print("3) Odd/Even from 1 to 20:")
for n in range(1, 21):
    kind = "even" if n % 2 == 0 else "odd"
    print(f"{n} -> {kind}")


# 4) Palindrome check (ignores case and non-alphanumerics)
import re

def is_palindrome(s: str) -> bool:
    cleaned = re.sub(r"[^A-Za-z0-9]", "", s).lower()
    return cleaned == cleaned[::-1]

# Demo:
text = input("Enter a string to check palindrome: ")
print("4) Palindrome?", is_palindrome(text))


# 5) (Optional) Sum of two integers from user input
def sum_of_integers(a: int, b: int) -> int:
    return a + b

# Demo:
try:
    a = int(input("Enter integer a: "))
    b = int(input("Enter integer b: "))
    print("5) Sum:", sum_of_integers(a, b))
except ValueError:
    print("Please enter valid integers.")
