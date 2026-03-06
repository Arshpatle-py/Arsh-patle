class vehicle:
  def move(self):
    print("Vehicle is moving")
    
class Car(vehicle):
  def move(self):
    print("car driving on the road") 
    
class Bicycle(vehicle):
  def move(self):
    print(" bicycle pedalling on the road")    
    
vehicles=[Car(),Bicycle()]

for v in vehicles:
  v.move()