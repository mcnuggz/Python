#copied from classes.py for packages/modules practice
class Planet:
    
    shape = 'round'

    #constructor function
    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system
    
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'
    
    
    @classmethod #this is a decorator
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity'

    @staticmethod #this is a decorator
    def spin(speed = '2000 miles per hour'):
        return f'The planet spins at {speed}!'