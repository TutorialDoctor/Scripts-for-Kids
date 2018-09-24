import re

deweyreg = re.compile(r'(\d\d\d)\s(\w.*)')

with open('dewey.txt','r') as infile:
  text = infile.read()
  found = deweyreg.findall(text)

organized = {
  '0': {},
  '1': {},
  '2': {},
  '3': {},
  '4': {},
  '5': {},
  '6': {},
  '7': {},
  '8': {},
  '9': {}
}

# if first digit is 1, group into key of digit ... if h[0]==1 then...
for h,k in found:
  #print(h+':',k) #if needed later
  if h[0] in organized:
    organized[h[0]][h] = k

# Implement
print(organized['0']['010'])
print(organized['1']['104'])
print(organized['2']['201'])
print(organized['3']['370'])
print(organized['4']['430'])
print(organized['5']['510'])
print(organized['7']['740'])
print(organized['8']['806'])
print(organized['9']['909'])

