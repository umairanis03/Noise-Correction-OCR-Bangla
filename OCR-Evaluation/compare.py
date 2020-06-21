import os
from jiwer import wer
import jiwer
path_gt = './lines_test/' # Ground truth- Original Text
path_trans = './noisy_lines_test_output/' # Text from OCR


list_articles=os.listdir(path_gt)
e=0
trans = jiwer.Compose([
    jiwer.RemoveMultipleSpaces(),
    jiwer.RemoveWhiteSpace(replace_by_space=False)
]) 

l = len(list_articles)

print('Total Number of lines are : '+str(l))
i = 0
for filename in list_articles:
  f_gt = open(os.path.join(path_gt, filename), 'r',encoding="utf-8")
  f_tr = open(os.path.join(path_trans, filename), 'r',encoding="utf-8")
  
  doc_gt = f_gt.read()
  doc_tr = f_tr.read()
  #print(filename +' ....' + str(i))
  if(i%1000):
    print(i, e/i)
  i+=1
  if ( os.path.getsize(os.path.join(path_gt,filename)) <=1 or len(doc_gt)==0):
     continue
  if (len(doc_tr)==0):
    e+=1
    continue
  #print(doc_gt)
  if(not doc_gt):
    continue
  #x =wer(doc_gt,doc_tr,trans,trans)
  #print(x)
  e+=wer(doc_gt,doc_tr,trans,trans)
  
  
print(e/l)
