

vowels = "aeiouAEIOU"

# infinite loop
while True:
   v = input("Enter a vowel: ")
   # condition in the middle
   if v in vowels:
       break
   print("That is not a vowel. Try again!")

print("Thank you!")
