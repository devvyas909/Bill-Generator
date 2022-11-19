#COMPUTER PROJECT
#Program that generates a bill and prints the bill as output
print('Welcome to Invoice Grocery Store')
import mysql.connector as sqLtor
mycon=sqLtor.connect(host='localhost',user='root',passwd='password123',database='billing_system')
if mycon.is_connected():
    print('Successfully connected to Mysql database')
    print('Sr.no  ItemName   ItemCode    Brand            Price')
cursor=mycon.cursor()   #cursor which fetches the tabe from mysql has been created
st='select*from grocery_store'
cursor.execute(st)
data=cursor.fetchall()  
for row in data:
    print(row[0],'    ',row[1],row[2],'    ',row[3],'    ',row[4])          
lst1=[]
lst2=[]
#the data from Mysql has been fetched
a=int(input('Enter the Item_code of the product that you want to buy:'))      
query="select Item_name from grocery_store where Item_code='%s'"
cursor.execute(query%(a))   
for i in cursor:
    print(i[0])
    lst1.append(i[0])      #name of items purchased are appended into lst1
cursor1=mycon.cursor()
query1="select Price from grocery_store where Item_code=%s"
c=cursor1.execute(query1%(a))
for i in cursor1:
    import functools          #functools is imported to convert tuple into int type
    c=functools.reduce(lambda sub, ele:sub*10+ele,i)
    b=int(input('How many of this product you want to buy?'))  
    print(c*b)
    lst2.append(c*b)        #the total amount to be paid is appended into lst2
while True:
    d=input("Do you want to buy more products,yes or no?")
    if d=='yes':
        a=int(input('Enter the Item_code of the product that you want to buy:'))
        query="select Item_name from grocery_store where Item_code='%s'"
        cursor.execute(query%(a))
        for i in cursor:
            print(i[0])
            lst1.append(i[0])     #name of items purchased are appended into lst1
        cursor1=mycon.cursor()
        query1="select Price from grocery_store where Item_code=%s"
        c=cursor1.execute(query1%(a))
        for i in cursor1:
            import functools   #functools is imported to convert tuple into int type
            c=functools.reduce(lambda sub, ele:sub*10+ele,i)
            b=int(input('How many of this product you want to buy?'))  
            print(c*b)
            lst2.append(c*b)   #the total amount to be paid is appended into lst2
            continue
    elif d=='no':
        print('Ok')
        break
    else:
        print('Your answer is not valid')
        break


print("INVOICE")
print('Item purchased:')
for i in range(len(lst1)):
    print(lst1[i])
print('Total amount of individual items:')
for i in range(len(lst2)):
    print(lst2[i])
sum=0
for i in lst2:
    sum+=i
print('Total amount to be paid:',sum)
print("Thankyou for shopping with us!")
print("GOODBYE!")

    

 
f1=open("bills.txt","w+")
str1=''
str2=''
for i in range(len(lst1)):
    str1+=str(lst1[i])
for i in range(len(lst2)):
    str2+=str(lst2[i])
    str2+=' '
sum1=0
for i in lst2:
    sum1+=i
str3=str(sum1)
w1=["INVOICE",    
    '\n','Item purchased:',
    '\n',str1,
    '\n','Total amount of individual items:',
    '\n',str2,
    '\n','Total amount to be paid:','\n',str3,
    '\n','Thankyou for shopping with us!',
    '\n','GOODBYE!']
f1.writelines(w1)
f1.close()

    
        
