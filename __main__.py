# __main__.py

# Import all of our functions
from transform_scripts import *

# This Determines number of Prezidents generated
iteration_count = 10

#Generate Backgrounds
generate_bg(iteration_count)

#Insert Base Prez
insert_prez(iteration_count)

#Apply random Transformations/Effects
transform_1(iteration_count)

#10% Chance to flip horizontally / add text
transform_flip_text(iteration_count)

#Place Frame over everything
transform_frame(iteration_count)


print("ALL DONE!! Generated "+str(iteration_count)+" deadprezidents yo")
