import re
import os
def clear(text):
   return ' '.join([i if ord(i) <= 12000 else ' ' for i in text])


path='../lines_test/'
path2= '../new_lines_test/'
list_articles=os.listdir(path)
for filename in list_articles:
  with open(os.path.join(path, filename), 'r',encoding="utf-8") as f:
    doc=f.read()
    temp = ""
    
    for ch in doc:
      if ch==" " or (ch>=u'\u0980' and ch<=u'\u09FF'):
        temp+= ch

    
    doc = temp
    with open(os.path.join(path2, filename), 'w',encoding="utf-8") as g:
        g.write(doc)

