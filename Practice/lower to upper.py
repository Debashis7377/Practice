iterable= input("enter rthe string")
# if 'a'<= iterable <= 'z' :
#     print(iterable.upper())
# elif iterable.isupper():
#     print(iterable.lower())
# else :
#     print("write alphabets")

if 'a'<= iterable <= 'z' or "A"<=iterable<="Z":
    print(iterable.swapcase())
else :
    print("write alphabets")