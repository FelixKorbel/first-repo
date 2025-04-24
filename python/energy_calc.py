# REad from yaml file
# Calculate KE and PE
# Output result to console
import math
import yaml

with open ("params.yaml", "r") as file : 
    data= yaml.safe_load(file)


v = data["vel"]
m = data ["mass"]
g = data ["grav"]
h = data ["height"]
#calculate e_kin
e_kin = 1/2 * m * v**2

#calculate e_pot
e_pot = m * g * h

#calculate total energy 
e_t = e_kin + e_pot

print(e_kin,"kinetic energy")
print(e_pot,"potential energy")
print(e_t,"total energy")
      

