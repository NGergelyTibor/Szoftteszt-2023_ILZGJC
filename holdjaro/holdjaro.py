class Holdjaro:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

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

            # térkép szélei
            self.x = max(0, min(self.x, 100))  # Térkép szélessége 100 egység
            self.y = max(0, min(self.y, 100))  # Térkép magassága 100 egység


        return self.x, self.y, self.direction