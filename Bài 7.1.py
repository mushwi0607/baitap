L = []
for i in range (100):
    x = int(input())
    L.append(x)
Chan = [i for i in L if i % 2 == 0]
Le = [j for j in L if j % 2 == 1]
f = open('sole.txt','w')
f.write(' '.join(map(str, Le)))
f = open('sochan.txt','w')
f.write(' '.join(map(str, Chan)))
