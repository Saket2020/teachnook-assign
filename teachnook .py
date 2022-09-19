#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Good evening all")


# In[3]:


a="Hello everyone" 
print(a)
print(type(a))


# In[4]:


num1=3387 
num2=3.47 
print(type(num2))
print(type(num1))

print(num1-num2)


# In[5]:


print(10<9)
add=False
print(add)
print(type(add))


# In[6]:


name="Jerry"
no=3

print("Hello"+name,no)


# In[7]:


mylist=["Data","Details","Access"] 
mylist1=[366,476.0,True,"Data"]
print(mylist1)


# In[8]:


mylist1[2]=False
print(mylist1)


# In[9]:


mylist1.add("data1")  ### list has not any attribute like  add 
print(mylist1)


# In[10]:


mylist1.insert(1000,300)
print(mylist1)


# In[11]:


del mylist1[5] ###indexno.5 has not any data so its show error
print(mylist1)


# In[12]:


mylist1.remove("Data")### remove help the user to delete the data directly 
print(mylist1)


# In[13]:


mylist1=[366,476.0,True,"Data"]
print(mylist1[1])


# In[15]:


tuple=(["dell","Asus","Hp",27,387.87])
print(tuple)
del tuple
print(tuple)


# In[16]:


Dict={
    "Username":["Admin","Admin1"],
      "Password":"Pass",
      "Os":"windows",
      "Ram":"128GB"
    
}
print(Dict["Username"])


# In[17]:


print(Dict["Password"])


# In[18]:


Dict["Password"]=32667
print(Dict)


# In[19]:


del Dict["Os"]
print(Dict)


# In[20]:


a="randomness"
print(a[0:100])
print(a[3:])
print(a[:3])
print(a[-9:-1])


# In[21]:


a="randomness"
print(a[-10:])


# In[24]:


b="Python"
 ##print(b[1])
 ###print(b[2])
print(b[::-2])


# In[25]:


myset={"A","B","C",32465,"A"}
print(myset)
print(len(myset))


# In[26]:


myset.add(True)
print(myset)


# In[27]:


var=set()
print(var)

var.add("Add")
print(var)


# In[28]:


set1={"Data","task","Status"}
set2={0,True,"Data"}
set3=set1|(set2)
print(set3)


# In[29]:


set1={"Data","task","Status"}
set2={0,True,"Data"}
set3=set1&(set2)
print(set3)


# In[30]:


set1.clear()
print(set1)


# In[31]:


set1=100
set2=100
print(set1!=set2)
print((set1)>=(set2))
print(set1==set2)


# In[32]:


myfrozenset= frozenset(["E","F"])
print(myfrozenset)


# In[34]:


myfrozenset.add("add") ### frozen set doesnot support add function
print(myfrozenset)


# In[35]:


print("hello")
print("hello")
print("hello")
print("hello")
print("hello")


# In[36]:


def func():
  for x in range(10):
    print("The task is assigned")
    print("Work is on progress")
func()  


# In[37]:


list1=["Data","Status","Progress",1,1,2 ,3]
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])



# In[38]:


for values in list1:
 print(values)


# In[39]:


def sub(num1,num2): 
  print("The addition of two values are",(num1-num2))
sub(45,55)  


# In[40]:


def a(name, name1):
  print("Hey",name,"and",name1, "good to see you today")
a("Tom","Jerry") 
 


# In[41]:


def user():
  x=input("Enter the name:")
  print("Nice to meet you",x)
user() 


# In[43]:


def addition():
  num1 = int(input("Enter first num: "))
  num2 = int(input("Enter second num: "))
  print("The sum of given two number is:", (num1 + num2))
addition()


# In[44]:


#Advance argument passing
# Positional arguments
def arg(name,batch,year):
  print("Hey this is",name,"from",batch,"in the year",year)
arg("Sep batch",2022,"Tom")  


# In[45]:


def value(a,b,c,d):
  print(a,b,c,d)
value(4,2,1,3)  


# In[ ]:




