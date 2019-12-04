def fuel_calc(mass):
  return max(0,(mass / 3) - 2)

filepath = 'input'
with open(filepath) as fp:
   line = fp.readline()
   fuel_total = 0
   while line:
       mass = int(line.strip())
       fuel_reqd = fuel_calc(mass)
       fuel_total += fuel_reqd
       while(fuel_reqd > 0):
         fuel_reqd = fuel_calc(fuel_reqd)
         fuel_total += fuel_reqd
       line = fp.readline()

print(fuel_total)
