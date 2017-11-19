import json, string, re, math,time
from sklearn.ensemble import RandomForestClassifier
"""get all files and append dictionaries"""
reuters=[]
with open("reuters-000.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-001.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-002.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-003.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-004.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-005.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-006.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-007.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-008.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-009.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-010.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-011.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-012.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-013.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-014.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-015.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-016.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-017.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-018.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-019.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-020.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()
with open("reuters-021.json") as reuters_file:
    reuters=reuters+json.load(reuters_file)
    reuters_file.close()

"""kick out all dictionaries which have no body or no topic"""
i=0
while i < len(reuters):
    if ('body' not in reuters[i]):
        reuters.remove(reuters[i])
        i=i-1
    elif ('topics' not in reuters[i]):
        reuters.remove(reuters[i])
        i=i-1
    elif reuters[i]['topics']==[]:
        reuters.remove(reuters[i])
        i=i-1
    elif reuters[i]['body']=='':
        reuters.remove(reuters[i])
        i=i-1
    i=i+1

"""find all distinct words, count them, save them in a list and their indexes in a dict"""
N=len(reuters)
print(N)
t1=time.time()
S=set()
for i in range (0,N):       #get all distinct words
    s=(reuters[i])['body'].lower()
    S=S.union(set(s.split()))
S=list(S)                   #make a sorted list
S.sort()
M=len(S)
textdict={}
for i in range(0,M):        #add a dictionary which for every word contains its index in S
    textdict[S[i]]=i        #which will be its index in the bag of words

"""create bag of words"""
BOW=[]
for i in range (0,N):
    st=reuters[i]['body'].lower()
    Spl=st.split()
    Line=[]
    for j in range (0, M):
        Line.append(0)
    for j in range (0,len(Spl)):
        Line[textdict[Spl[j]]]+=1
    BOW.append(Line)

"""classify articles"""
y=[]
for i in range(N):
    if 'earn' in reuters[i]['topics']:
        y.append(1)
    else:
        y.append(0)
cut = math.floor(N * 0.8)
BOW_train = BOW[0:cut]
y_train=y[0:cut]
BOW_test=BOW[cut:N]
y_test=y[cut:N]

"""train classifier"""
clf=RandomForestClassifier(n_estimators=50)
clf.fit(BOW_train,y_train)
prediction=clf.predict(BOW_test)

"""test prediction"""
c=0
for i in range(N-cut):
    if y[i+cut]==prediction[i]:
        c+=1
prob=c/(N-cut)
print(prob)
t2=time.time()
print(t2-t1)