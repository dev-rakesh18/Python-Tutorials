# tuple data structure
# tuple can store any data type
# most important tuples are immutable , once tuple is created you can`t update
# data inside tuple
# tuples are faster than list
# no append no insert ,no pop,no remove
# tuple methods :  count , index , len , slicing ,

num=('one','two','three','one')

print("#____________ slicing _______________")

print(num[:])            # All elements
print(num[:1])           # 1st elements
print(num[:2])           # 2nd elements
print(num[:3])           # 3rd elements

print(num[::-1])            # reverse the elements

print("#____________ COUNT _______________")

print(num.count('one')) 

print("#____________ INDEXING _______________")
print(num.index('one')) 
print(num.index('one',num.index('one')+1)) 

print("#____________ INDEXING _______________")
print(len(num))