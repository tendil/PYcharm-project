from base_class import *

Ad = Directory()

Jo = Cleaning_Master()

print(isinstance(Jo, Cleaning_Master))
print(isinstance(Jo, Person))


Ad.who_i_am()
Ad.my_job()
Jo.who_i_am()
Jo.my_job()

print()
print()

Jo.give_up_my_job()

Ad.who_i_am()
Ad.my_job()
Jo.who_i_am()
Jo.my_job()

print(isinstance(Jo, Cleaning_Master))
print(isinstance(Jo, Person))


