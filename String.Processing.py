### String Processing

# String literals
s1 = "Connie is funny"
s2 = 'Jeth wears nice ties!'
s3 = " t-shirts!"
#print s1, s2
#print s3

# Combining strings
a = ' and '
s4 = "Guy" + a + "Jeth" + ' are nuts!'
print s4

# Characters and slices
print s1[3]
print len(s1)
print s1[0:7]  + s2[6:]
print s2[:10] + s1[9:] + s3

# Converting strings
s5 = str(375)
print s5[1:]
i1 = int(s5[1:])
print i1 + 38
