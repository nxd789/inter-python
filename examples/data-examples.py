# print("hello")

numbers = [12,3,5,34,6]

# print(numbers)

#print(numbers[0:3])
#print(numbers[3:6])

#print(numbers[1:3])

print(numbers[::-1])

animal_sounds={"dog":"arf","cat":"meow"}
print(animal_sounds)
animal_sounds["cow"] = "moo"
print(animal_sounds)
animal_sounds[14]="huh?"
print(animal_sounds)

xy = (12,4)
print(xy)

x,y = xy

print(x)
print(y)

t = (1,)

"select a,b from data where a > &t",(5,)
print(t)


print([n*n for n in numbers if n > 5][::-1])

x = set()
x.add(1)
x.add(2)
x.add(2)
x.add(3)

print(x)

n = [12,3,5,34,6,3,8,6]
print(n)
print(set(n))
print(list(set(n)))

z = {n:n*n for n in numbers}
print(z)


#z = {}
#for n in numbers:
#    z[n] = n*n

print(n)
print(sorted(n))
print(n)
n.sort()
print(n)

n = [[1,2,3],
     [4,5,6],
     [7,8,9]]

print([ v for inner in n for v in inner ])

result = []
for inner in n:
    for v in inner:
        result.append(v)

print(result)