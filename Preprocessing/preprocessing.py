import re
import os
def clear(text):
   return ' '.join([i if ord(i) <= 12000 else ' ' for i in text])


path='../lines_test/' #Corpus Path
path2= '../new_lines_test/' # Pre-processed Corpus
list_articles=os.listdir(path)
for filename in list_articles:
  with open(os.path.join(path, filename), 'r',encoding="utf-8") as f:
    doc=f.read()
    #print(filename)
    english_check = re.compile(r'[a-z]')
    eCapital = re.compile(r'[A-Z]')
    nums=re.compile(r'[0-9]')
    #re.sub(r'[^\u0980-\u9FF]+',' ', doc)
    whitespace = re.compile(u"[\s\u0020\u00a0\u1680\u180e\u202f\u205f\u3000\u2000-\u200a]+", re.UNICODE)
    punctSeq   = u"['\"“”‘’]+|[.?!,…]+|[:;]+"
    punc = u"[(),$%^&*+={}\[\]:\"|\'\~`<>/,^`¦!?½£¶^y¼©⅐⅑⅒⅓⅔⅕⅖⅗⅘⅙⅚⅛⅜⅝⅞⅟↉¤¿º;-]+"
    bangla_fullstop = u"\u0964"
    doc=english_check.sub("",doc).strip()
    doc = eCapital.sub("",doc).strip()
    doc = nums.sub("",doc).strip()
    doc= whitespace.sub(" ",doc).strip()
    doc = re.sub("\s\s+"," ",doc)
    doc = re.sub(punctSeq, " ", doc)
    #doc = re.sub(bangla_fullstop, " ",doc)
    doc = re.sub(punc, " ", doc)
    #print(doc)
    doc = clear(doc)
    with open(os.path.join(path2, filename), 'w',encoding="utf-8") as g:
        g.write(doc)

