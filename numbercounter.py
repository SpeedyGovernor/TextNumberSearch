import re
total = 0
#starts at a total of zero
fhand = open("sample.txt")
#opens the file mbox.txt
for line in fhand:
  #loops through the lines
  numbers = re.findall( '[0-9]+', line)
  #finds the numbers
  if numbers != [""]:
    #if there are numbers on the` line
    for items in numbers:
      #incase there is more than one number
      total = total + int(items)
      #add up all the numbers
print(total)
#print the total vaue of all the numberst
