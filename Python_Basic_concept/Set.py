s1 = {1,4,'der',1,6,2} # Set do not take duplicate values
print(s1)
print(type(s1))
s1.add(4) # Set do not take duplicates
print(s1)

s = set()    # creating empty set
s.add(2)     #adding elements to set
s.add('dc')
s.add(7)
print(s)
print(type(s1))

s2 = s.union(s1)  #Return a set containing the union of sets
print(s2)

s4 = s.intersection(s1)   #Returns a set, that is the intersection of two or more sets
print(s4)

s5 = s.isdisjoint(s1)  #Returns whether two sets have a intersection or not
print(s5)


s6 = s.difference(s1)   #Returns a set containing the difference between two or more sets
print(s6)


s1.remove(4)  # Removes the element in set
print(s1)