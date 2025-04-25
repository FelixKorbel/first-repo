# REad from yaml file
# Calculate KE and PE
# Output result to console
import math
import yaml

with open ("C:/Users/Internship/Documents/Felix Git/first-repo/python/params.yaml", "r") as file:
    data = yaml.safe_load(file)


v = data ["parameters"] ["vel"]
m = data ["parameters"] ["mass"]
g = data ["parameters"] ["grav"]
h = data ["parameters"] ["height"]
#calculate e_kin
e_kin = 1/2 * m * v**2

#calculate e_pot
e_pot = m * g * h

#calculate total energy 
e_t = e_kin + e_pot

print(e_kin,"kinetic energy")
print(e_pot,"potential energy")
print(e_t,"total energy")
      

