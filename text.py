#נקלוט למשתנה את המילה הראשונה בקובץ-
# נוכל להגיד לו שהמילה הראשונה בקובץ
#מתחילה במשהו ונגמרת ברווח הראשון
#Letter(1):' '
#[:' ']
#אפשר להשתמש בin
def revword(word:str) ->str:
    return word[::-1].lower()

def countword() ->int:
    count=0
    i=0
    fhand=open('text.txt','r')
    readfile= fhand.read()
    word1= readfile.split()[0] #אולי צריך להוסיף פה lower
    numofwords= len(readfile.split())
    while i <= numofwords:
        if word1 == revword(readfile[i-1]):
            count=count+1
            i=i+1
    print(count)

        
        
    
    
    
    
    
    
    



        