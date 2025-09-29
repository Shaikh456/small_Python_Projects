# Patterns



# s = 5

# Prints the entire elements one by one
# for i in range(s):
#     print("*" )


# prints the no of s in a row with multiple of s in column
# for i in range(s):
#     print("*" * s)


# Print the stars starting from 1 increment by 1 in each row till the nth no in s variable    
# s = 5    
# for i in range(s):
#      print("*" * (i + 1))


# Print the starts starting from nth no. by decrementing star by 1 in each row until it reaches to 1
# s = 5
# for i in range(s):
#     count = s - i
#     print("*" * count)

# s = 5
# for i in range(s):
#     count = s - i
#     print (' ' * i)
#     print('*' * count)


s = 5
for i in range(s):
    count = s - i
    print('' * count)
    print('*' * (i+1))


