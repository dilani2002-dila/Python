motorbike = ['honda', 'yamaha', 'suzuki', 'bajaj'];
print(motorbike);

motorbike[0]='ducati';
print(motorbike);

#add item at last
motorbike.append('honda');
print(motorbike);

#insert item at specific index
motorbike.insert(2, 'tvs');
print(motorbike);

#remove item
motorbike.remove('honda');
print(motorbike);

#pop item 
motorbike.pop(2);
print(motorbike);

#all item pop
motorbike.clear();
print(motorbike);