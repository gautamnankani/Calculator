import sys
sys.path.append('/myModules/')
import myModules
from myModules.mathy import *
print(responses[0])
print(responses[1])

while True:
    print()
    txt=input('enter query:')
    for wrd in txt.split(' '):
        if wrd.upper() in operators.keys():
            try:
                L=extract_no_from_txt(txt)
                ANS=operators[wrd.upper()](L[0],L[1])
                print(ANS)
                break
            except:
                print("something went wrong")
                break
        elif wrd.upper() in commands.keys():
            commands[wrd.upper()]()
            break
    else:
        sorry()
    
        
