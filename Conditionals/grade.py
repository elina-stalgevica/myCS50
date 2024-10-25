score = int(input("Score:"))

# "In Python you can combine 2 conditions like in example below.
# Instead of score >= 90 and score <= 100: you can type - 90 <= score <= 100:"

# "Also instead of asking 2 questions in one sentence, we can make it even shorter.
# Before: 90 <= score <= 100 and After: score >= 90: ; score >= 80:  "
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
