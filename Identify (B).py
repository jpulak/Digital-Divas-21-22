for i in range(int(input())):  
  things=[]
  name= input().split()
  num= int(name[1])
  for i in range(num):
    object=input()
    things.append(object)
  if name[0]== "Mary-Jane" or name[0]== "Ned" or name[0]== "Happy" or name[0]== "May":
    print("Your secret is safe with me.")
  elif 'Shirt' in things and 'Pants' in things and 'Socks' in things and 'Shoes' in things and 'Jacket' in things:
    print("Your secret is safe with me.")
  else:
    print("Your secret is out.")
    
