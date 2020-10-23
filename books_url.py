import re
# import pdb
# pdb.set_trace()

fin = ""

f = open("test.txt", "r")
for x in f:
  regex = r'https://elibro-library-production.s3.amazonaws.com/([^"]+)'
  match = re.search(regex, x)
  if match:
    fin = fin + '"https://elibro-library-production.s3.amazonaws.com/' + match.group(1) + '"\n'
f.close()

text_file = open("sample.txt", "wt")
n = text_file.write(fin)
text_file.close()

print(fin)