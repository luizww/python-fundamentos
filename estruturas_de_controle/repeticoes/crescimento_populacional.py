pa=80000
pb=200000
anos=0
while pa < pb:
    pa=pa + (3*pa/100)
    pb=pb + (1.5*pb/100)
    anos += 1
print(f'levara {anos} anos para a população A ultrapassar a população B')
