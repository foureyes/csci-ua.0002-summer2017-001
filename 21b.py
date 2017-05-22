"""
import turtle
t = turtle.Turtle()
wn = turtle.Screen()
"""
points = [[0, 100], [100, 100], [100, 0], [0, 0]]

new_points = []
for p in points:
    if p[1] > 0:
        new_points.append(p)
        #new_points.append(p[1])
print(new_points)

"""
for i in range(len(points)):

    points[i][0] += 50 
    points[i][1] += 50 
print(points)

for p in points:
    t.goto(p[0], p[1])


wn.mainloop()
"""

