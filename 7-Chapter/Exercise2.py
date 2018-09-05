# Write a program to prompt for a file name, and then read
# through the file and look for lines of the form: X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:”
# pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence
# values from these lines. When you reach the end of the file, print out
# the average spam confidence.

# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745
# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519

try:
    fname = input('Enter a file name: ')
    fhandle = open(fname)
except:
    print('File not found')
    exit()

total = 0
average = 0
count = 0

for line in fhandle:
    line = line.strip()
    if line.startswith('X-DSPAM-Confidence:'):
         colon_pos = line.find(':')
         extracted_num = float(line[colon_pos+1:])
         total += extracted_num
         count += 1

average = total/count
print('Average spam confidence:',round(average,4))



