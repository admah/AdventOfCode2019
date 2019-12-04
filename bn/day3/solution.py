filepath = 'input'
with open(filepath) as fp:
   line = fp.readline().strip()
   wire_1 = line.split(',')
   line = fp.readline().strip()
   wire_2 = line.split(',')

   grid_dim = 50001
   grid = {}
   for i in range(grid_dim):
     grid[i]  = {}

   current_x = grid_dim/2
   current_y = grid_dim/2
   while len(wire_1) > 0:
     instruction = wire_1.pop(0)
     direction = instruction[0:1]
     distance = int(instruction[1:])
     while distance > 0:
       if direction == 'U':
         current_y -= 1
       if direction == 'D':
         current_y += 1
       if direction == 'L':
         current_x -= 1
       if direction == 'R':
         current_x += 1
       grid[current_x][current_y] = 1
       distance -= 1

   min_dist = 100000
   current_x = grid_dim/2
   current_y = grid_dim/2
   while len(wire_2) > 0:
     instruction = wire_2.pop(0)
     direction = instruction[0:1]
     distance = int(instruction[1:])
     while distance > 0:
       if direction == 'U':
         current_y -= 1
       if direction == 'D':
         current_y += 1
       if direction == 'L':
         current_x -= 1
       if direction == 'R':
         current_x += 1
       if current_y in grid[current_x]:
         cross_distance = abs(current_x - (grid_dim/2)) + abs(current_y - (grid_dim/2))
         min_dist = min(cross_distance, min_dist)
       distance -= 1

   print(min_dist)
