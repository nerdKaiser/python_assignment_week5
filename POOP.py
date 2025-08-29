# Activity 1
# Phone class
# Represents a smartphone with attributes & methods

# Base class: Phone (generic blueprint)
class Phone:
    def __init__(self, brand, model, storage):
        # initialize common attributes
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = 100  # default battery percentage

    def charge(self, amount):
        # increase battery level, max 100
        self.battery = min(100, self.battery + amount)
        print(f"🔋 {self.model} charged to {self.battery}%")

    def use(self, hours):
        # reduce battery when phone is used
        self.battery = max(0, self.battery - hours * 10)
        print(f"📱 {self.model} battery now {self.battery}%")


# Derived class: Samsung (inherits from Phone)
class Samsung(Phone):
    def __init__(self, model, storage, has_s_pen):
        # call parent constructor (brand is fixed as Samsung)
        super().__init__("Samsung", model, storage)
        self.has_s_pen = has_s_pen

    def use_s_pen(self):
        # unique Samsung feature
        if self.has_s_pen:
            print(f"🖊️ Using the S-Pen on {self.model}!")
        else:
            print(f"⚠️ {self.model} has no S-Pen.")


# Create objects with unique values
note20 = Samsung("Note 20", "256GB", True)
s22 = Samsung("Galaxy S22", "128GB", False)

# Try methods
note20.charge(20)
note20.use(3)
note20.use_s_pen()

s22.use(2)
s22.use_s_pen()

#Activity 2
# Vehicles with polymorphic move() method

# Base class: Vehicle
class Vehicle:
    def move(self):
        # generic move (to be overridden by subclasses)
        print("The vehicle is moving...")

# Derived class: Car
class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")

# Derived class: Plane
class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")

# Derived class: Train
class Train(Vehicle):
    def move(self):
        print("🚆 Running on the tracks...")

# Demonstrate polymorphism
vehicles = [Car(), Plane(), Train()]

for v in vehicles:
    v.move()  # same method name, different behavior

