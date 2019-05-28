responses=["welcome","my name is calci","thanku","sorry,this is beyond my reach"]

def extract_no_from_txt(text):
    L=[]
    for x in text.split(' '):
        try:
            L.append(float(x))
        except ValueError:
            pass
    return L

def lcm(a,b):
    m=a if a>b else b
    while m<=a*b:
        if m%a==0 and m%b==0:
            return m
        m+=1
def hcf(a,b):
    m=a if a<b else b
    h=1
    while m>=1:
        if a%m==0 and b%m==0:
            return m
        m-=1

def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
def end():
    print(responses[2])
    input("press enter to exit")
    exit()
def name():
    print(responses[1])
def sorry():
    print(responses[3])

operators={"HCF":hcf,"LCM":lcm,"PLUS":add,"ADD":add,"ADDITION":add,"SUBTRACT":sub
           ,"SUBTRACTION":sub,"SUB":sub,"MULTIPLY":mul,"MULTIPLICATION":mul,
           "MUL":mul,"DIVIDE":div,"DIVISION":div,"DIV":div}

commands={"END":end,"EXIT":end,"CLOSE":end,"NAME":name,"SORRY":sorry}
