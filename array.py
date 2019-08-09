import json
import uuid

arr = {'id':1, 'nama': 'Ahadian Akbar'},{'id':2, 'nama': 'GTA San Andreas'}

for index in range(len(arr)):
  print(arr[index])

arrN = [0,3,36,4]

arrN.append(100)

for i in range(len(arrN)):
  print(arrN[i])

arrList = []

for i in range(0,10):
  arrList.append({'id': str(uuid.uuid4()),'nama' : 'Ahadian Akbar','jadwal':[{'no':1,'hari':'senen','jadwal':'Matakuliah ABC'},{'no':1,'hari':'senen','jadwal':'Matakuliah ABC'}] })

for c in range(len(arrList)):
  print(arrList[c]['jadwal'])

json = json.dumps(arrList)

#print(json)


