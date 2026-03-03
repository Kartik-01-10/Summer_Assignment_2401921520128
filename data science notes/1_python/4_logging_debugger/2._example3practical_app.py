# wap to make seperate integer and string
l=[1,2,3,4,[2,3,4], "kartik", "yadav"]
l1_int =[]
l2_str =[]
for i in l :
    if type(i)== list:
        for j in i :
            if type(j) == int:
                l1_int.append(j)
    elif type(i) == int :
        l1_int.append(i)
    else :
        l2_str.append(i)

print (l1_int)
print (l2_str)


# now here we have to use logging module
l=[1,2,3,4,[2,3,4], "kartik", "yadav"]
l1_int =[]
l2_str =[]
import logging
logging.basicConfig(filename="test3.log" , level= logging.DEBUG ,format='%(asctime)s %(name)s %(levelname)s %(message)s')

for i in l :
    logging.info("we are iterating throught list")
    if type(i)== list:
        logging.info("i am inside if statement ")
        for j in i :
            logging.info("i am in for loop list inside list ")
            if type(j) == int:
                logging.info("i am inside if state.")
                l1_int.append(j)
    elif type(i) == int :
        l1_int.append(i)
    else :
        l2_str.append(i)

print (l1_int)
print (l2_str)

# o/p of this code is test3.log file 



l=[1,2,3,4,[2,3,4], "kartik", "yadav"]
l1_int =[]
l2_str =[]
import logging
logging.basicConfig(filename="test3.log" , level= logging.DEBUG ,format='%(asctime)s %(name)s %(levelname)s %(message)s')

for i in l :
    logging.info("we are iterating throught list"+ l )   #  if we do this we get logging error 
    if type(i)== list:
        logging.info("i am inside if statement ")
        for j in i :
            logging.info("i am in for loop list inside list ")
            if type(j) == int:
                logging.info("i am inside if state.")
                l1_int.append(j)
    elif type(i) == int :
        l1_int.append(i)
    else :
        l2_str.append(i)



l=[1,2,3,4,[2,3,4], "kartik", "yadav"]
l1_int =[]
l2_str =[]
import logging
logging.basicConfig(filename="test3.log" , level= logging.DEBUG ,format='%(asctime)s %(name)s %(levelname)s %(message)s')

for i in l :
    logging.info("we are iterating throught list" + str(l) )  #  but this will get logging
    if type(i)== list:
        logging.info("i am inside if statement " +str(i))
        for j in i :
            logging.info("i am in for loop list inside list " + str(j))
            if type(j) == int:
                logging.info("i am inside if state.")
                l1_int.append(j)
    elif type(i) == int :
        l1_int.append(i)
    else :
        l2_str.append(i)

# l=[1,2,3,4,[2,3,4], "kartik", "yadav"]
l1_int =[]
l2_str =[]
import logging
logging.basicConfig(filename="test3.log" , level= logging.DEBUG ,format='%(asctime)s %(name)s %(levelname)s %(message)s')

for i in l :
    logging.info("we are iterating throught list" + str(l) )  #  but this will get logging
    if type(i)== list:
        logging.info("i am inside if statement " +str(i))
        for j in i :
            logging.info("i am in for loop list inside list " + str(j))
            if type(j) == int:
                logging.info("i am inside if state.")
                l1_int.append(j)
    elif type(i) == int :
        l1_int.append(i)
    else :
        l2_str.append(i)


#l=[1,2,3,4,[2,3,4], "kartik", "yadav"]
l1_int =[]
l2_str =[]
import logging
logging.basicConfig(filename="test3.log" , level= logging.DEBUG ,format='%(asctime)s %(name)s %(levelname)s %(message)s')

for i in l :
    logging.info("we are iterating throught list" + str(l) )  #  but this will get logging
    if type(i)== list:
        logging.info("i am inside if statement " +str(i))
        for j in i :
            logging.info("i am in for loop list inside list " + str(j))
            if type(j) == int:
                logging.info("i am inside if state.")
                l1_int.append(j)
    elif type(i) == int :
        l1_int.append(i)
    else :
        l2_str.append(i)

# here str is converting entire list into string  
str(l) == "[1, 2, 3, 4, [2, 3, 4], 'kartik', 'yadav']"
# Effect on Logging
# - This stringified version of the list is appended to your log message.
# - So the log entry becomes:
# we are iterating through list: [1, 2, 3, 4, [2, 3, 4], 'kartik', 'yadav']
# Result
# - You get repetitive log entries showing the same full list multiple times.
# - It doesn’t tell you which element is being processed in that iteration.

# if we want to place list at the last also then we have do
#l=[1,2,3,4,[2,3,4], "kartik", "yadav"]
l1_int =[]
l2_str =[]
import logging
logging.basicConfig(filename="test3.log" , level= logging.DEBUG ,format='%(asctime)s %(name)s %(levelname)s %(message)s')

for i in l :
    logging.info("we are iterating throught list{}" .format(l) )  # help to place list
    if type(i)== list:
        logging.info("i am inside if statement " +str(i))
        for j in i :
            logging.info("i am in for loop list inside list " + str(j))
            if type(j) == int:
                logging.info("i am inside if state.")
                l1_int.append(j)
    elif type(i) == int :
        l1_int.append(i)
    else :
        l2_str.append(i)

    # In the line below, we are using the .format() method to insert the value of 'l' into the log message
logging.info("we are iterating through list{}".format(l))

# ✅ What .format(l) does:
# - The .format() method replaces the curly braces {} with the string representation of the variable 'l'
# - If l = [1, 2, 3, 4, [2, 3, 4], "kartik", "yadav"], then:
#   "we are iterating through list{}".format(l)
#   becomes:
#   "we are iterating through list[1, 2, 3, 4, [2, 3, 4], 'kartik', 'yadav']"

# 🔁 Comparison with string concatenation:
# - Using "text" + str(l):
#   logging.info("we are iterating through list" + str(l))
#   also produces the same result, but requires manual conversion using str()

# ✅ Why .format() is useful:
# - It provides cleaner syntax, especially when inserting multiple variables
#   Example: "Item {} is of type {}".format(i, type(i))
# - It avoids manual concatenation and is easier to read and maintain

# ⚠️ Note:
# - In your loop, this message is logged every time, even though the list 'l' doesn't change
# - For better logging, consider logging the current item 'i' instead:
#   logging.info("Currently processing item: {}".format(i))



# at lat of code we can also logging the final result

logging.info("my final result for int is {l1} and str is {l2}".format( l1= l1_int , l2= l2_str))
