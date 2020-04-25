import re,csv,ctypes
from collections import Counter
from nltk.corpus import stopwords
from os import listdir
from os.path import isfile,join
path = r"C:\Users\akash\OneDrive\Desktop\Projects\Master Proj\Phishing Dataset\Parsed Phishing mails"
files = [f for f in listdir(path) if isfile(join(path, f))]
csvfile = open(r"C:\Users\akash\OneDrive\Desktop\Projects\Master Proj\Phishing Dataset\Phishing_paper1.csv","a",newline="")
writer = csv.writer(csvfile)
writer.writerow(['Total Number of Characters C', 'Vocabulary richness W/C',
              'Account','Access','Bank','Credit','Click','Identity','Inconvenience',
               'Information','Limited','Minutes','Password','Recently','Risk','Social',
              'Security','Service','Suspended', 'Total number of Function words/W','Unique Words','Phishing Status'])
for f in files:
    ch = path + "\\" + f
    with open(ch, "r", errors="ignore", encoding="ascii") as file:
        contents = file.read()
    cnt,line_num = 0,[]
    for i in contents.splitlines():
        if("From " in i):
            line_num.append(cnt)
        cnt+=1
    con,ind,cont = contents.splitlines(),0,""
    tot = []
    for i in range(len(line_num)-1):
        cont = ""
        for j in range(line_num[i],line_num[i+1]):
            cont = cont + con[j] + "\n"
        cont = cont.split()
        cont = [i for i in cont if len(i)>2]
        res = []
        C,W = 0,0
        Func_words = ["account","access","bank","credit","click","identity","inconvenience","information","limited"
                  ,"minutes","password","recently","risk","social","security","service","suspended"]
        for i in cont:
            C = C + len(i)
            W = W + 1
        res.append(C)
        res.append(W/C)
        No_funwd = 0
        for i in Func_words:
            cnt = 0
            for j in cont:
                if(i==j.lower()):
                    cnt+=1
            res.append(cnt)
            No_funwd = No_funwd + cnt
        res.append(No_funwd/W)
#    stwords = stopwords.words('english')
#    cont = [i for i in cont if i not in stwords]
        count = Counter(cont)
        res.append((len([i for i in count if count[i]==1])))
        res.append(1)
        writer.writerow(res)
csvfile.close()

# Appending the values of the features from the enron mails
L = []
csv.field_size_limit(int(ctypes.c_ulong(-1).value // 2))
csvfile1 = open(r"C:\Users\akash\OneDrive\Desktop\Projects\Master Proj\Phishing Dataset\Phishing_paper1.csv","a",newline='')
writer = csv.writer(csvfile1)
with open(r"C:\Users\akash\OneDrive\Desktop\Projects\Master Proj\enron-email-dataset\emails.csv",newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        st = " "
        st = row[0] + st +row[1]
        st = st.split()
        st = [i for i in st if len(i)>2]
        res = []
        C, W = 0, 0
        Func_words = ["account", "access", "bank", "credit", "click", "identity", "inconvenience", "information",
                      "limited"
            , "minutes", "password", "recently", "risk", "social", "security", "service", "suspended"]
        for i in st:
            C = C + len(i)
            W = W + 1
        res.append(C)
        res.append(W / C)
        No_funwd = 0
        for i in Func_words:
            cnt = 0
            for j in st:
                if (i == j.lower()):
                    cnt += 1
            res.append(cnt)
            No_funwd = No_funwd + cnt
        res.append(No_funwd / W)
        #    stwords = stopwords.words('english')
        #    cont = [i for i in cont if i not in stwords]
        count = Counter(st)
        res.append((len([i for i in count if count[i] == 1])))
        res.append(0)
        writer.writerow(res)
# ***************************************************************************************
csvfile.close()
csvfile1.close()


