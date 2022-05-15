t=input('Type the text to be encoded\n')
code={'a' : 'c','b' : 'd','c' : 'e','d' : 'f','e' : 'g','f' : 'h','g' : 'i','h' : 'j','i' : 'k','j' : 'l','k' : 'm',
      'l' : 'n','m' : 'o','n' : 'p','o' : 'q','p' : 'r','q' : 's','r' : 't','s' : 'u','t' : 'v',
      'u' : 'w','v' : 'x','w' : 'y','x' : 'z','y' : 'a','z' : 'b'}
r=''

for i in t:
    if i.isalpha:
        if i==' ':
            result = r + ' '
            r = result
        else:
            result = r + code[i]
            r = result
final=result[::-1]
print(final)
