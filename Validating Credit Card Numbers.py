# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for i in range(n):
    card = input()
    card = str(card)
    
    x = re.findall("^4", card)
    x += (re.findall("^5", card))
    x += (re.findall("^6", card))
    
    # Not start with 4,5,6
    if len(x) == 0:
        print("Invalid")
        continue
    
    pattern = True if re.match('[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]', card) and len(card) == 19 else False

    if((card.isnumeric() and len(re.findall('[0-9]', card)) == 16) or pattern):
        card = card.replace('-','')
        # check continuous occurrence
        prev = card[0]
        count = 0
        for i in range(1, len(card)):
            if (card[i] == prev):
                count += 1
                if count >= 3:
                    print("Invalid")
                    break
            else:
                prev = card[i]
                count = 0
        
        if count >= 3:
            continue
        print("Valid")

    else:
        print("Invalid")
                