import random
from collections import Counter

ROLL_NO = "1024170089"

print("=" * 60)
print("QUESTION 1: LISTS")
print("=" * 60)

# Extract individual digits of roll number and multiply each by 10
digits = [int(d) for d in ROLL_NO]           # [1,0,2,4,1,7,0,0,8,9]
L = [d * 10 for d in digits]                 # multiply each digit by 10

# i. Print L
print("i. L =", L)

# ii. Add two numbers - one using append(), one using insert()
L.append(100)                                # append() adds element at the END of the list
print("\nii. After append(100):", L)

L.insert(3, 55)                              # insert() adds element at a SPECIFIC index (here index 3)
print("    After insert(3, 55):", L)

# iii. Remove two elements - one using remove(), one using pop()
L.remove(0)                                  # remove() deletes the FIRST occurrence of the given VALUE
print("\niii. After remove(0):", L)

popped = L.pop()                             # pop() removes and returns element at given INDEX (default: last)
print(f"     After pop() -> removed {popped}:", L)

# iv. Sort ascending, then descending
L.sort()
print("\niv. Ascending  :", L)
L.sort(reverse=True)
print("    Descending :", L)

# v. Slicing - first three and last three elements
print("\nv. First three:", L[:3])
print("   Last three :", L[-3:])

# vi. List comprehension - elements greater than the average of L
avg_L = sum(L) / len(L)
above_avg = [x for x in L if x > avg_L]
print(f"\nvi. Average of L = {avg_L:.2f}")
print("    Elements greater than average:", above_avg)


print("\n" + "=" * 60)
print("QUESTION 2: TUPLES")
print("=" * 60)

# scores = first 8 values from the ORIGINAL list L computed in Q1 (before append/insert/remove/pop)
base_L = [d * 10 for d in digits]
scores = tuple(base_L[:8])
print("scores =", scores)

# i. Highest score + index, lowest score + frequency
highest = max(scores)
highest_index = scores.index(highest)
lowest = min(scores)
lowest_count = scores.count(lowest)
print(f"\ni. Highest score = {highest} at index {highest_index}")
print(f"   Lowest score  = {lowest}, appears {lowest_count} time(s)")

# ii. Reverse the tuple, return as a list
reversed_list = list(reversed(scores))
print("\nii. Reversed (as list):", reversed_list)
# Tuples are immutable, so they have no in-place reverse() method like lists do;
# reversed() must instead build a NEW sequence rather than modifying the tuple itself.

# iii. Ask user to input a score, find first occurrence index
user_score = int(input("\niii. Enter a score to search for: "))
if user_score in scores:
    print(f"     {user_score} found at index {scores.index(user_score)}")
else:
    print(f"     {user_score} not present in scores")

# iv. Attempt to change an element directly -> catch the error
print("\niv. Attempting scores[0] = 100 ...")
try:
    scores[0] = 100
except TypeError as e:
    print(f"     Error raised: {e}")
    # Tuples are immutable (cannot be changed after creation), unlike lists which are
    # mutable, so item assignment on a tuple raises a TypeError.

# v. Unpack into first, second, and remaining using *
first_score, second_score, *remaining_scores = scores
print("\nv. first_score =", first_score, "| second_score =", second_score, "| remaining_scores =", remaining_scores)


print("\n" + "=" * 60)
print("QUESTION 3: RANDOM LIST OPERATIONS")
print("=" * 60)

random.seed(1024170089)                      # seed = your own roll number
random_list = [random.randint(100, 900) for _ in range(100)]
print("i. Generated 100 random numbers (seeded).")

# ii. Odd numbers
odds = [n for n in random_list if n % 2 != 0]
print(f"\nii. Odd numbers count  = {len(odds)}")

# iii. Even numbers
evens = [n for n in random_list if n % 2 == 0]
print(f"iii. Even numbers count = {len(evens)}")

# iv. Prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [n for n in random_list if is_prime(n)]   # list comprehension building actual primes
print(f"\niv. Prime numbers count = {len(primes)}")
print("    Prime numbers list    =", primes)

# v. Most frequently occurring number
freq = Counter(random_list)
most_common_num, most_common_count = freq.most_common(1)[0]
print(f"\nv. Most frequent number = {most_common_num}, occurs {most_common_count} time(s)")


print("\n" + "=" * 60)
print("QUESTION 4: SETS")
print("=" * 60)

# Same 8 digits from Q1, BEFORE multiplying by 10
digits8 = digits[:8]                          # [1,0,2,4,1,7,0,0]
A = {d * 7 for d in digits8}
B = {d * 9 for d in digits8}
print("A =", A)
print("B =", B)

# vi. Union
print("\nvi. Union (A | B)        :", A | B)

# vii. Intersection
print("vii. Intersection (A & B):", A & B)

# viii. Difference A-B and B-A
print(f"\nviii. A - B = {A.difference(B)}")
print(f"      B - A = {B.difference(A)}")
# difference() is one-directional (only elements in the first set but not the second),
# while symmetric_difference() combines BOTH directions (elements in either set but not both).

# ix. Symmetric difference
print("\nix. Symmetric difference (A ^ B):", A.symmetric_difference(B))

# x. Subset / superset checks
print(f"\nx. Is A a subset of B?   {A.issubset(B)}")
print(f"   Is B a superset of A? {B.issuperset(A)}")

# xi. Discard user input value from A
X = int(input("\nxi. Enter a value X to discard from set A: "))
A.discard(X)
print(f"    Set A after discard({X}):", A)
# discard() does NOT raise an error if the value is missing, whereas remove() raises
# a KeyError - so discard() is safer when you're unsure the value exists.


print("\n" + "=" * 60)
print("QUESTION 5: DICTIONARIES")
print("=" * 60)

my_dict = {
    "name": "Jaskaran Singh",
    "roll_no": ROLL_NO,
    "branch": "COPC",
    "age": 20,          # placeholder - edit to your actual age
    "city": "Patiala"   # placeholder - edit to your actual home city
}

# i. Rename "city" -> "location" without hand-recreating the dict
my_dict["location"] = my_dict.pop("city")
print("i. After renaming city -> location:", my_dict)

# ii. Add "cgpa"
my_dict["cgpa"] = 8.5   # placeholder - edit to your actual CGPA
print("\nii. After adding cgpa:", my_dict)

# iii. Update age by increasing it by 1
my_dict["age"] += 1
print("\niii. After incrementing age:", my_dict)

# iv. Delete "branch" using pop() in one copy, del in another copy
dict_pop_copy = my_dict.copy()
popped_value = dict_pop_copy.pop("branch")
print(f"\niv. pop('branch') removed and RETURNED the value: {popped_value}")
print("    Dict after pop:", dict_pop_copy)

dict_del_copy = my_dict.copy()
del dict_del_copy["branch"]
print("    del keyword removed the key but returns NOTHING (None)")
print("    Dict after del:", dict_del_copy)

# v. Iterate using .items()
print("\nv. Iterating with .items():")
for key, value in my_dict.items():
    print(f"    {key} → {value}")

# vi. Safely check for "email" key before accessing
print("\nvi. Checking for 'email' key:")
if "email" in my_dict:
    print("    Email:", my_dict["email"])
else:
    print("    Email not available.")

# vii. Merge with friend_dict using {**dict1, **dict2}
friend_dict = {
    "name": "Rohan Mehta",
    "roll_no": "1024170099",
    "branch": "CSE",
    "age": 21,
    "city": "Ludhiana"
}
merged_dict = {**my_dict, **friend_dict}
print("\nvii. Merged dictionary:", merged_dict)
# When both dictionaries share a key, the value from the SECOND dictionary (friend_dict)
# overwrites the first, since later keys win in the {**a, **b} unpacking order.

# viii. Dictionary comprehension - keep only string-valued pairs
string_only_dict = {k: v for k, v in my_dict.items() if isinstance(v, str)}
print("\nviii. Only string-valued key-value pairs:", string_only_dict)
