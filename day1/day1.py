# python version bc i need practice
# why do i even love C so much...
# fin = open("input.txt", "r")
# print(fin.readline())
# fin.close()

# Update 1: I just realized that rotations can be more than two digits... 

dial = 50 # dial starts pointing at 50
count = 0 # count # of turns that leave the dial at 0
with open("input.txt", "r") as fin:
      for line in fin:
            # line = fin.readline()
            turns = int(line[1:])
            # print(line[0])
            # print(turns)
            # Consider direction
            if (line[0] == "L"):
                  dial -= turns
            elif (line[0] == "R"):
                  dial += turns
            # Circles around
            dial = dial % 100
            if (dial < 0):
                  dial += 100
            elif (dial > 99):
                  dial -= 100
            # Count turns that end in 0
            if (dial == 0):
                  count += 1
            print(dial)
print(count)