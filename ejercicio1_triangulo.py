# Determinar si se puede formar un triangulo 

#input 
print("------------------------------------------------")
print("---DETERMINAR-SI-SE-PUEDE-FORMAR-UN-TRIANGULO---")
print("------------------------------------------------")

a=int(input("\n Digite el valor de a: "))
b=int(input("\n Digite el valor de b: "))
c=int(input("\n Digite el valor de c: "))

#process

if(a+b>c and a+c>b):
    print("\nSi se puede formar un triangulo")
else:
    print("\nNo se puede formar un triangulo")


#fin 
