warrior_name="Thor"
warrior_health=100
warrior_attack=50

mage_name="Natsu"
mage_health=80
mage_attack=70

def attack_warrior():
    print(f"warrior attacks with power",warrior_attack)
def attack_mage():
     print(f"mage attacks with power",mage_attack)

attack_warrior()
attack_mage()

"""
The problems of the code above are:
1/Redundency(every charecter needs unique functions ,variable)
2/Hard to maintain and read
3/Doesnt matches real world

For solving the problem we need oops
1/For large scale project
2/security
3/reusability
4/Matches real world so easy to understand
"""

