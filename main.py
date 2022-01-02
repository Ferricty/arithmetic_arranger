# This entrypoint file to be used in development. Start by reading README.md
#from pytest import main

from arithmetic_arranger import arithmetic_arranger


#print(arithmetic_arranger(["32 + 98", "3801 - 2", "45 + 43", "123 + 49", "123 + 9"],True))
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'],True))

# Run unit tests automatically
#main()
