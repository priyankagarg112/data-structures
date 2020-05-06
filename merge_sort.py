
def merge(l,i,m,j):
  l1 = l[i:m+1]
  l2 = l[m+1:j+1]

  x=y=0
  z=i

  while x < len(l1) and y < len(l2):
    if l1[x] < l2[y]:
      l[z]=l1[x]
      x += 1
    else:
      l[z] = l2[y]
      y +=1
    z +=1

  while x < len(l1):
    l[z] = l1[x]
    x +=1
    z +=1

  while y < len(l2):
    l[z] = l2[y]
    y +=1
    z +=1


def merge_sort(l,i,j):
  if i==j:
    return

  m = int(i + ((j-i)/2))
  merge_sort(l,i,m)
  merge_sort(l,m+1,j)

  merge(l,i,m,j)

l = [3,2,5,7,8,9,1,0]
merge_sort(l, 0, len(l)-1)

print(l)
