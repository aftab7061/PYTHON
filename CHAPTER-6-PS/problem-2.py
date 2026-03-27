sub1=int(input("enter marks :"))
sub2=int(input("enter marks :"))
sub3=int(input("enter marks :"))
total_percentage=(100*(sub1+sub2+sub3))/300

if(total_percentage>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("you are passed, ",total_percentage)
else:
    print("you are not passed, ",total_percentage)