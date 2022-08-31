############# opening the file in read mode ############

z= open('mydata', 'r')  ## It will print the details of file
print(z)


y = open('mydata', 'r')
print(y.read())       ## this will read us the data in file

x = open('mydata', 'r')
print(x.readline())    ## this will print only first line from file

w = open('mydata', 'r')
print(w.readline(3))   ## this will print the given number of characters

############# opening the file in write mode ############
z1 = open('data', 'w')
z1.write(" Start writing") ## this will write in file but delete all after writing new things in file



############# opening the file in append mode ############
y1 = open('data', 'a')
y1.write("Now with append previous data will still remain")


############### copy all data from mydata and copy paste in data##############

f=open('mydata', 'r')


f1 = open('data', 'w')

for i in f:  ## for will fetch every line from mydata and paste it in data
    f1.write(i)


####################Printing image data##################
a =open('D.jpg', 'rb')
for i in a:
    print(i)  ## it will print all hexa-values of image

############# to copy image into another file and show the image##################

r = open('D.jpg', 'rb')

b = open('D1.jpg', 'wb')
for i in r:
    b.write(i)




