import os

directorio = "/var/www/html/ceac2627dam1"

for x,y,z in os.walk(directorio):
  print(x)
  print(y)
  print(z)