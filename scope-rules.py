# Scope - what variabels do I have access to?

a = 1

def confusion():
    a = 5
    return a 
#1 start with local
print(confusion())
print(a)

# Scope - what variabels do I have access to?

a = 1

def parent():
    a = 10
    def confusion():
        return a
    return confusion() 

print(confusion())
print(a)

#1 start with local
#2 parent local?


# Scope - what variabels do I have access to?

a = 1

def parent():
    def confusion():
        return a
    return confusion() 

print(confusion())
print(a)

#1 start with local
#2 parent local?
#3 global - what ever the file has that is global, the indentation of nothing

  
# Scope - what variabels do I have access to?

a = 1

def parent():
    a = 10
    def confusion():
        return sum
    return confusion()

print(parent())
print(a)

#1 - start with local 
#2 - Parent local?
#3 - Global
#4 - built in python functions. 





 
