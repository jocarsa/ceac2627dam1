import os

directorio = "/var/www/html/ceac2627dam1"

for x,y,z in os.walk(directorio):
  print(x)

for x,y,z in os.walk(directorio):
  print(y)
  
for x,y,z in os.walk(directorio):
  print(z)
