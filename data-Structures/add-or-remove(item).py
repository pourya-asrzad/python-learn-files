letters =list("abc")


# Add

letters.append("d")
letters.insert(0,"-")

# remove 
letters.pop(0)
letters.remove('b')
del letters[0:3]
letters.clear()

print(letters)