#forloop
motorBike=['TVS','Bajaj','Yamaha','Honda','Suzuki','BMW'];
for i in motorBike:
    print(i);

#print letters
bird='Peacock';
for i in  bird:
    print(i);

#break
print(motorBike);
for i in motorBike:
    print(i)
    if i == "Honda":
     break;

print();
print(motorBike);
for i in motorBike:
    if i == "Honda":
       continue;
    print(i);