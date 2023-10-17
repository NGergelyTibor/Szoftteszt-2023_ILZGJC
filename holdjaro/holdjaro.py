class Holdjaro:
    def __init__(self, x, y, direction, obstacles, planet_radius):
        self.x = x
        self.y = y
        self.direction = direction
        self.obstacles = obstacles
        self.planet_radius = planet_radius

    def move(self, commands):
        for command in commands:
            if command == 'f':
                if self.direction == 'N':
                    self.y += 1
                elif self.direction == 'E':
                    self.x += 1
                elif self.direction == 'S':
                    self.y -= 1
                elif self.direction == 'W':
                    self.x -= 1
            elif command == 'b':
                if self.direction == 'N':
                    self.y -= 1
                elif self.direction == 'E':
                    self.x -= 1
                elif self.direction == 'S':
                    self.y += 1
                elif self.direction == 'W':
                    self.x += 1
            elif command == 'l':
                if self.direction == 'N':
                    self.direction = 'W'
                elif self.direction == 'E':
                    self.direction = 'N'
                elif self.direction == 'S':
                    self.direction = 'E'
                elif self.direction == 'W':
                    self.direction = 'S'
            elif command == 'r':
                if self.direction == 'N':
                    self.direction = 'E'
                elif self.direction == 'E':
                    self.direction = 'S'
                elif self.direction == 'S':
                    self.direction = 'W'
                elif self.direction == 'W':
                    self.direction = 'N'
            else:
                raise ValueError("Invalid command")

            # térkép szélei (a gömb alakú bolygó esetében)
            distance_from_center = (self.x ** 2 + self.y ** 2) ** 0.5
            if distance_from_center > self.planet_radius:
                angle = math.atan2(self.y, self.x)
                self.x = self.planet_radius * math.cos(angle)
                self.y = self.planet_radius * math.sin(angle)

            # Akadályok ellenőrzése
            if (self.x, self.y) in self.obstacles:
                return "Akadály!"

        return self.x, self.y, self.direction