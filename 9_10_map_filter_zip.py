values = [1, 2, 3]
# map
print("map function")
map = map(lambda x: x + 5, values)
for i in map:
    print(i)
# filter
print("filter function")
filter = filter(lambda x: True if x > 2 else False, values)
for i in filter:
    print(i)
# zip
print("zip function")
name = ['ali', 'jadi', 'hossein']
age = [19, 40, 27]
sex = ['m', 'u', 'm']
zip = zip(name, age, sex)

for i, j, z in zip:
    print(f'name={i},age={j},sex={z}')
