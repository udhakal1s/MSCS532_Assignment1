#Umesh Dhakal
#MSCS532A1
#Insertion sort that sorts in Monotonically decreasing order
#insertionsort function 
def insertionsort(Arraylist):

    for a in range (1,len(Arraylist)):
        key =Arraylist[a]
        b= a-1
        #Moving the element that are smaller than key to one step to right
        while b>=0 and key > Arraylist[b]:
            Arraylist[b+1]=Arraylist[b]
            b =b -1
            #Placing the key in the correct position
        Arraylist[b+1]=key

#user input separated by comma
MyNumbers = input("Enter the numbers separated by commas: ")
numbers = [int(x.strip()) for x in MyNumbers.split(',')]

insertionsort(numbers)
#Print statement to print the number after they are sorted
print("List of numbers in decreasing order after insertion sort:", numbers)
