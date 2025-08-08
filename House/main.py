class Room:
    length = 0.0
    height = 0.0
    total = 0.0

    def calculation(self):
        print("The area of study room is = " , self.length *  self.height)


study_room = Room()
study_room.length = 54.0
study_room.height = 20.0
students = Room()
students.total = 100

study_room.calculation()
print("total Students In The Class"students.total)
