print(10 > 9)
print(10 == 9)
print (10 < 9)

a = 200
b = 3

if b > a: 
    print("Sim. b é maior que a.")
else: 
    print("Não. b não é maior que a.")

print(bool("Olá"))
print(bool(15))
print(bool([3,2,4]))
print(bool(False))
print(bool(True))
print(bool([]))
print(bool(""))
print(bool(0))
print(bool())

def myFunction():
    return 10 > 5

print(myFunction())

# o if conta como ''se for verdadeiro''.
if myFunction():
    print("Sim!")
else:
    print("Não!")
    
# isinstance para verificar se X é do tipo INT     // se a variável é do tipo tal
x = 200
print(isinstance(x, float))