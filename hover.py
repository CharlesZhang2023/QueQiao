from math import cos,sin,radians
# rotate_matrix (x,y,degree)->(new_x_after_rotate,new_y_after_rotate)
def rotate_point(x,y,degree):
    radian=radians(degree)
    new_x=x*cos(radian)-y*sin(radian)
    new_y=x*sin(radian)+y*cos(radian)
    new_x=round(new_x,2)
    new_y=round(new_y,2)
    return (new_x,new_y)

# cycle_trajectory (degree,n,radius)->[(x1,y1),(x2,y2),...,(xn,yn)]
# n is the number of points to segment the cycle
def cycle_points(degree=0,n=4,radius=10):
    points=[]
    n = 4
    delta_degree = 360/n
    for i in range(n):
        degree+=delta_degree
        x,y=rotate_point(radius,0,degree)
        points.append((x,y))
    return points

# waypoint_trajectory (pos, head_degree, radius, number)->[(x1,y1),(x2,y2),...,(xn,yn)]
def waypoint_generate(pos, head_degree, radius=60, number=4):
    waypoints=cycle_points(head_degree,number,radius)
    pos_x,pos_y=pos
    for i in range(len(waypoints)):
        x=waypoints[i][0]+pos_x
        y=waypoints[i][1]+pos_y
        x=round(x,2)
        y=round(y,2)
        waypoints[i]=(x,y)
    return waypoints

if __name__ == '__main__':
    result =waypoint_generate((10,10), 0, 60, 4)
    print(result)