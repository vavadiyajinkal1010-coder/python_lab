"""try:
    my_list = [1, 2, 3]
    print(my_list[1])

except IndexError:
    print("Index is out of range!")

else:
    print("Element found succesfully!")

finally:
    print("Pogram finished")"""


try:
    a=int(input("enter a number:"))
    b=int(input("enter another number:"))
    result=a/b
    print("result:",result)
except ZeroDivisionError:
    print(" You cannot divide by zero")
except ValueError:
    print("please enter only integers ")
else:
    print("Divison successfull Result is:",result)
finally:
    print("This block alaways runs.")