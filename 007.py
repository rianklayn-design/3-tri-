names = ["Marcelo", "Laura", "Maria", "João"]

for i, name in enumerate(names):
    print(i, name)

print("---------------------------------")

for i, name in enumerate(names, start=1):
    print(i, name)