# This file is used to format the output of waypoints.txt into a format that can be used by the flight controller.

# Read the waypoints.txt file and turn it into a list of tuples of x, y, z
def read_waypoints(filename="./output/waypoints.txt"):
    with open(filename, 'r') as f:
        lines = f.read().split('\n')
        #print(line)
        #read each line and turn into tuple of x, y, z
    lines = lines[0:-1]
    waypoints = []
    for line in lines:
        line = line.replace('(', '').replace(')', '')
        points = line.split(',')
        x = float(points[0])
        y = float(points[1])
        z = 1.0
        pos =[x, y, z]
        waypoints.append(pos)
    return waypoints

# Function to transport the waypoints by a certain amount in x, y, and z directions
def transport_waypoints(waypoints,delta_x=-15,delta_y=0,delta_z=0):
    new_waypoints = []
    for waypoint in waypoints:
        x = waypoint[0] + delta_x
        y = waypoint[1] + delta_y
        z = waypoint[2] + delta_z
        x = round(x,2)
        y = round(y,2)
        z = round(z,2)
        new_waypoint = [x, y, z]
        new_waypoints.append(new_waypoint)
    return new_waypoints

# Function to scale the waypoints by a certain factor
def scale_waypoints(waypoints,scale_factor=1.0):
    new_waypoints = []
    for waypoint in waypoints:
        x = round(waypoint[0] * scale_factor,2)
        y = round(waypoint[1] * scale_factor,2)
        z = waypoint[2] # * scale_factor
        new_waypoint = [x, y, z]
        new_waypoints.append(new_waypoint)
    return new_waypoints

def list_to_xml_waypoints(points_list):
    # Number of waypoints
    point_num = len(points_list)
    

    xml_start = '''<arg name="flight_type" value="2" />\n<!-- global waypoints -->\n<!-- It generates a piecewise min-snap traj passing all waypoints -->\n<arg name="point_num" value="{}" />\n'''.format(point_num)
    xml_body = ""
    for i, point in enumerate(points_list):
    
        point_x, point_y, point_z = point
        xml_point = '''<arg name="point{}_x" value="{}" />\n<arg name="point{}_y" value="{}" />\n<arg name="point{}_z" value="{}" />\n'''.format(i, point_x, i, point_y, i, point_z)
        xml_body += xml_point
    
    xml_waypoints = xml_start + xml_body
    
    return xml_waypoints

def add_spaces_to_xml(xml_string):
    lines = xml_string.split('\n')
    lines = lines[0:-1]
    spaced_lines = ['        ' + line for line in lines]
    formatted_xml = '\n'.join(spaced_lines)
    return formatted_xml



if __name__ == '__main__':
    # Read the waypoints.txt file and turn it into a list of tuples of x, y, z
    waypoints = read_waypoints("./output/waypoints.txt")
    new_waypoints = scale_waypoints(waypoints,scale_factor=0.12)
    new_waypoints = transport_waypoints(new_waypoints,delta_x=-15,delta_y=0,delta_z=0)

    #print(new_waypoints)
    points_list = new_waypoints
    xml_output = list_to_xml_waypoints(points_list)
    formatted_xml_output = add_spaces_to_xml(xml_output)
    print(formatted_xml_output)
    with open('./output/final_waypoints.txt', 'w') as f:
        f.write(formatted_xml_output)