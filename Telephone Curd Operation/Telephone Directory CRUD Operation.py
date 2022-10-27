#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install dnspython')
get_ipython().system('pip install pymongo[srv]')


# In[3]:


import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client.TelephoneDirectory
record = db.contacts


# In[7]:


# Sample inputs

"""trial=[
       {"name":"Ravi Chandran","ph":9865326598,"_id":"ravi@gmail.com","Place":"Delhi"},
       {"name":"Alex velu","ph":7845124512,"_id":"alex@gmail.com","Place":"Pune"},
       {"name":"Rahul Madhu","ph":8954785476,"_id":"ahul@gmail.com","Place":"Bangalore"},
       {"name":"Vinish Vivek","ph":9854786532,"_id":"vinish@gmail.com","Place":"Mumbai"}]  
record.insert_many(trial) """


# In[ ]:


# Function to add new contacts


# In[11]:


def details():
    g=0
    while g==0:
        name=' '.join([i.capitalize() for i in input("Name: ",).split()])
        ph=str(input("Phone Number: ",))
        try:
            check=[int(i) for i in ph]
        except:
            continue
        if len(check)==10:
            pass
        else:
            print("ERROR : Phone number should contain 10 digits, please try again.")
            continue
            
        mail_id=input("Mail id: ",)
        if mail_id.endswith("@gmail.com")==True or mail_id.endswith("@yahoo.in")==True:
            pass
        else:
            print("ERROR : mail id should end with @gmail.com, please try again.")
            continue
        place=input("Place: ",).capitalize()
        g=1
    return {"name":name,"ph":int(ph),"_id":mail_id,"Place":place}


# In[ ]:


## Funtion to Insert the record into the collection


# In[12]:


def add_contacts():
    people = details()
    record.insert_one(people)


# In[ ]:


## Code to find the records that are already created.
## Function to Retrieve all contacts in alphabetical order


# In[13]:


def all_contacts():
    import pandas as pd
    docs=record.find().sort("name",1)
    ds=pd.DataFrame(docs)
    print(ds)


# In[ ]:


## Function to get the data of the contact by name.


# In[14]:


def get_contact():
    k=0
    names=' '.join([i.capitalize() for i in input("Name: ",).split()])
    for i in record.find({"name":names},{"_id":1, "name":1,"ph":1,"mail_id":1,"Place":1}):
        k=1
        print(i)
    if k==0:
        import pandas as pd
        data=record.find()
        ds=pd.DataFrame(data)
        val=ds["name"].str.startswith(names,na=False)
        for i in val:
            if i ==True:
                print("Contact ",names," is not found. Are you searching for \n ", ds[val])
                break
            else:
                print("Contact ",names," is not found!")


# In[ ]:


## Modifying the phone number or places or both using names already recorded by the user.


# In[15]:


def modify():
    print("To change Phone number, Please Type 1")
    print("To change Place, Please Type 2")
    print("To chage Both, Please Type 3")
    modd=int(input())
    if modd==1:
        
        #By name change phone no
        name1=' '.join([i.capitalize() for i in input("Name: ",).split()])
        my_query={'name':name1}
        ph1=str(input("Phone Number: ",))
        new_value={"$set":{"ph":ph1}}
        record.update_one(my_query,new_value)
        
    elif modd==2:
        
        #by name change place
        name1=' '.join([i.capitalize() for i in input("Name: ",).split()])
        my_query={'name':name1}
        place1=' '.join([i.capitalize() for i in input(" ",).split()])
        new_value={"$set":{"Place":place1}}
        record.update_one(my_query,new_value)
        
    elif modd==3:
        
        #by name change ph no
        name1=' '.join([i.capitalize() for i in input("Name: ",).split()])
        my_query={'name':name1}
        ph1=str(input("Phone Number: ",))
        new_value={"$set":{"ph":ph1}}
        record.update_one(my_query,new_value)
        
        #by name change place
        place1=' '.join([i.capitalize() for i in input("Place name: ",).split()])
        new_value={"$set":{"Place":place1}}
        record.update_one(my_query,new_value)


# In[ ]:


## Function to delete the contact by name using delete_one() Method:


# In[16]:


def delete():
    name2=' '.join([i.capitalize() for i in input("Type the name that has to be deleted ",).split()])
    for i in record.find():
        if i['name']==name2:
            idd=i['_id']
            break
        else:
            pass
    db.contacts.delete_one({'_id':idd})


# In[ ]:


## Main Function


# In[17]:


def tele_func():
    print("To add your contacts ,Please Type A.")
    print("To get a contact detail,Please Type B")
    print("To get all the contacts in view, Please Type C")
    print("To update phone number or place, Please Type D")
    print("To delete a contact using name as input, Please Type E")
    mark=input().capitalize()
    if mark=="A":
        add_contacts()
    elif mark=="B":
        get_contact()
    elif mark=="C":
        all_contacts()
    elif mark=="D":
        modify()
    elif mark=="E":
        delete()    
    else:
        print("ERROR : Please try again!")


# In[ ]:


## To execute the program run the tele_func()


# In[18]:


# Creating new contact
tele_func()


# In[19]:


## Display All data
tele_func()


# In[20]:


## Retrieving a contact information
tele_func()


# In[21]:


## Updating new phone no and place to a contact
tele_func()


# In[22]:


## Udated record (vinish vivek --> phone number and place has been updated)
## Display updated record
tele_func()


# In[23]:


## Deleting contact details in record
tele_func()


# In[24]:


## Records after deleting Rahul Mudhu
## Display updated record after deletion
tele_func()


# In[ ]:





# In[ ]:




