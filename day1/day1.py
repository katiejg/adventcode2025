# python version bc i need practice
# why do i even love C so much...
# fin = open("input.txt", "r")
# print(fin.readline())
# fin.close()

## Part 1
# dial = 50 # dial starts pointing at 50
# count = 0 # count # of turns that leave the dial at 0
# with open("input.txt", "r") as fin:
#       for line in fin:
#             # line = fin.readline()
#             turns = int(line[1:])
#             # print(line[0])
#             # print(turns)
#             # Consider direction
#             if (line[0] == "L"):
#                   dial -= turns
#             elif (line[0] == "R"):
#                   dial += turns
#             # Circles around
#             dial = dial % 100
#             if (dial < 0):
#                   dial += 100
#             elif (dial > 99):
#                   dial -= 100
#             # Count turns that end in 0
#             if (dial == 0):
#                   count += 1
#             # print(dial)
# print(count)

# Part 2
dial = 50 # dial starts pointing at 50
count = 0 # count # of turns that pass 0
with open("input.txt", "r") as fin:
      for line in fin:
            # line = fin.readline()
            turns = int(line[1:])
            # print(line)
            # print(turns)
            # Will only have effect if turns >= 100
            # Passes 0 every 100 clicks: 
            count = count + (turns // 100)
            # Consider direction
            if (line[0] == "L"):
                  # If I turn left, to pass 0, I must turn it more than the number of starting position
                  if (((turns % 100) > dial) and (dial !=0)):
                        count += 1
                  dial -= turns
            elif (line[0] == "R"):
                  # If I turn right, to pass 0, I must turn it more than 100 - starting position
                  if (((turns % 100) > 100 - dial) and (dial !=0)):
                        count += 1
                  dial += turns
            # Circles around
            dial = dial % 100
            if (dial < 0):
                  dial += 100
            elif (dial > 99):
                  dial -= 100
            # Count turns that end in 0, which is why we do not count it within the L/R handling
            if (dial == 0):
                  count += 1
            # print(dial)
print(count)
