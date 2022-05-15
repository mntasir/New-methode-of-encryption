t=input('Type the text to be decoded\n')
code={'c' : 'a','d' : 'b','e' : 'c','f' : 'd','g' : 'e','h' : 'f','i' : 'g','j' : 'h','k' : 'i','l' : 'j','m' : 'k',
      'n' : 'l','o' : 'm','p' : 'n','q' : 'o','r' : 'p','s' : 'q','t' : 'r','u' : 's','v' : 't',
      'w' : 'u','x' : 'v','y' : 'w','z' : 'x','a' : 'y','b' : 'z'}
r=''

for i in t:
    if i.isalpha:
        if i==' ':
            result = r + ' '
            r = result
        else:
            result = r + str(code[i])
            r = result
final=result[::-1]
print(final)
