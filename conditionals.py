#!/usr/bin/python3
userReply = input("Do you need to ship a package? (Enter yes or no) ")
if userReply == "yes":
    print("We can help you ship that package!")
else :
    print("please come back when you need help to ship a package. Thank you.")
    
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("we have stamps you can choose from")
elif userReply == "envelope":
    print("We have envelop sizes to choose from.")
elif userReply == "copy":
    copies = input("how many copies")
    print("here are {} copies".format(copies))
else:
    print("Thank you")