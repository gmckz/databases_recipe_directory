class Recipe:
    def __init__(self, id, name, avg_cook_time, rating):
        self.id = id
        self.name = name
        self.avg_cook_time = avg_cook_time
        self.rating = rating

    def __repr__(self):
        return f"{self.id} - {self.name} - {self.avg_cook_time} - {self.rating}"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__