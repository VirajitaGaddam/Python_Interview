import csv
import urllib.request
import codecs
import re

def Read_Csv():
    url = "https://raw.githubusercontent.com/clearinterface/python_interview/master/50-contacts.csv"
    ftpstream = urllib.request.urlopen(url)
    csv_reader = csv.reader(codecs.iterdecode(ftpstream, 'utf-8'))
    next(csv_reader)
    return list(csv_reader)
    
def DisplayData(csv_reader):
    #Main()
        for lines in csv_reader:
    #Displaying the entire data present in 50-contacts.csv
            print(lines)

def Phone(csv_reader):
        for lines in csv_reader:
    #Coverting columns Phone1, Phone to a list   
            list1 = lines[8]
            list2 = lines[9]
            newlist1 = []
            newlist2 = []
    #Removing '-' from the string
            for x in list1:
                newlist1.append(x.replace('-', ''))
            for x in list2:
                newlist2.append(x.replace('-', ''))
            str1 = ""
            str2 = ""
            for ele in newlist1:
                str1 += ele
            for ele2 in newlist2:
                str2 += ele2
    #Phone1 without '-'
            lines[8] = str1
            lines[9] = str2
            print(lines[8:10])
            
def ZipCode(csv_reader):
    for lines in csv_reader:
        list3 = lines[7]
        newlist3 = []
    #Appending 0 for zipcodes with length < 5
        newlist3.append(list3.ljust(5 , '0'))
        lines[7] = newlist3
        print(lines[7])       
        
def Email(csv_reader):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    for lines in csv_reader:
        email1 = lines[10]
    #Validating Email Address
        if(re.search(regex,email1)):
            print("VALID email", email1)
        else:  
            print("INVALID Email", email1)
            
def main():
    csv_reader = Read_Csv()
    print("\n-------------------------------------------------------\n")
    print("\nDisplaying the entire data present in the file\n")
    DisplayData(csv_reader)
    print("\n-------------------------------------------------------\n")
    print("\nThe following are the phone numbers present in the data \n")
    Phone(csv_reader)
    print("\n-------------------------------------------------------\n")
    print("\nThe following is the 5 digit zip Code\n")
    ZipCode(csv_reader)
    print("\n-------------------------------------------------------\n")
    print("\nValidity of Email Address\n")
    Email(csv_reader)

main()
