import pratik

print("Get the parent of `src`:", pratik.get_root())
print("`src` doesn't exist then it takes the parent of the current file.")
print("Get the parent of `exemples`:", pratik.get_root(trigger="exemples"))
