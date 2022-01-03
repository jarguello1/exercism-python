"""
For example, if it's told that the garden looks like so:

[window][window][window]
VRCGVVRVCGGCCGVRGCVCGCGV
VRCCCGCRRGVCGCRVVCVGCGCV

Then if asked for Alice's plants, it should provide:

    Violets, radishes, violets, radishes

While asking for Bob's plants would yield:

    Clover, grass, clover, clover
"""

class Garden:
    
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David",
    "Eve", "Fred", "Ginny", "Harriet",
    "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.diagram = diagram
        #sort the students according to alphabetically order
        self.students = sorted(students)

    def plants(self, name):
        self.plants = {"G":"Grass", "C":"Clover", "R":"Radishes", "V":"Violets"}
        chart = self.diagram.replace("\n","")
        
        #Equations to get the values that are used to locate each plant
        #Increase all index values by 1 for the equations
        n = self.students.index(name)*2
        divisor = int(len(chart)/2)
        plant_list = [self.plants[x] for x in chart]
        return [
            plant_list[n],
            plant_list[n+1],
            plant_list[n+divisor],
            plant_list[n+1+divisor]
        ]
