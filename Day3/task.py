# num = int(input("Enter a number: "))

# if num > 0:
#     if num % 2 == 0:
#         print("Positive even number")
#     else:
#         print("Positive odd number")
# else:
#     print("Not a positive number")

# # a = int(input("Enter first number: "))
# # b = int(input("Enter second number: "))

# # if a > b:
# #     print("A is greater")
# # else:   
# #     print("B is greater or equal")


# A (>= 90), B (>= 75), C (>= 60), Fail (else)
score = int(input("Enter your score: "))

if score >= 90:
    print("Congrats! You scored Grade 1")
elif score >= 75:
    print("Congrats! You scored Grade 2")
elif score >= 60:
    print("Congrats! You scored Grade 3")
else:
    print("Oops! Failed. Better try again.")


