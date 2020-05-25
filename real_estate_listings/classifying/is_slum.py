#!/usr/bin/env python
# coding: utf-8

# In[28]:


from PIL import Image, ImageColor, ImageOps, ImageFilter
from skimage import color
import os
import imageio
import numpy as np
import pandas as pd
from geopy.distance import geodesic, pi, EARTH_RADIUS, cos, sin


# In[25]:


# making a list of map images and map arrays
maps = {}

for name in os.listdir('Slum Maps/original'):
    
    image = Image.open(f'Slum Maps/original/{name}')
    

    maps[f"{name.split('_')[0]}_original"] = image
  

    


for name in os.listdir('Slum Maps/grayscale'):
    
    image = Image.open(f'Slum Maps/grayscale/{name}')
    
    maps[f"{name.split('_')[0]}_grayscale"] = image


# In[32]:


# defining a distance function
def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**.5

# top left
# 22°43'51.40"S
# 43°50'9.60"W
# (-22.73094444, -43.83611111)


# bottom right
# 23°10'41.09"S
# 43° 1'58.18"W
# (23.17808056, 43.03277778)



# lattitude and Longitude reference points
rio_origin_lat_long = (-22.73094444, -43.83611111)
rio_edge_lat_long = (-23.17808056, -43.03277778)
# Pixel coordinate refrence points
rio_origin_coords = (0, 0)
rio_edge_coords = (536, 960)

# getting real world component and total distances between refrence points
rio_total_dist_lat_long = geodesic(rio_origin_lat_long, rio_edge_lat_long).kilometers
rio_y_dist_lat_long = geodesic(rio_origin_lat_long, (rio_edge_lat_long[0], rio_origin_lat_long[1])).kilometers
rio_x_dist_lat_long = geodesic(rio_origin_lat_long, (rio_origin_lat_long[0], rio_edge_lat_long[1])).kilometers

# getting pixel coordinate component and total distances between refrence points
rio_total_dist_coords = distance(rio_origin_coords,rio_edge_coords)
rio_y_dist_coords = distance(rio_origin_coords, (rio_edge_coords[0], rio_origin_coords[1]))
rio_x_dist_coords = distance(rio_origin_coords, (rio_origin_coords[0], rio_edge_coords[1]))

# getting conversion between x distance in pixels to km
rio_x_factor = rio_x_dist_lat_long / rio_x_dist_coords
# getting conversion between y distance in pixels to km
rio_y_factor = -rio_y_dist_lat_long / rio_y_dist_coords

rio_total_factor = rio_total_dist_lat_long/rio_total_dist_coords


# In[7]:


# defining a function to get lattitude and longitude prom pixel coordinates
def rio_get_lat_long(coord):
    
    y = coord[1] * rio_y_factor
    x = coord[0] * rio_x_factor
    
    lat  = rio_origin_lat_long[0] + (y / EARTH_RADIUS) * (180 / pi)
    long = rio_origin_lat_long[1] + (x / EARTH_RADIUS) * (180 / pi) / cos(rio_origin_lat_long[0] * pi/180)

    return (lat, long)




# (556,304) (266, 744)


# In[33]:


# top left
# 19°16'51.71"N
# 72°46'15.42"E
# (19.28103056, 72.77083333)


# bottom right
# 18°53'4.20"N
# 72°59'2.39"E
# (18.88450000, 72.98388889)



# lattitude and Longitude reference points
mumbai_origin_lat_long = (19.28103056, 72.77083333)
mumbai_edge_lat_long = (18.88450000, 72.98388889)
# Pixel coordinate refrence points
mumbai_origin_coords = (0, 0)
mumbai_edge_coords = (8000, 4000)

# getting real world component and total distances between refrence points
mumbai_total_dist_lat_long = geodesic(mumbai_origin_lat_long, mumbai_edge_lat_long).kilometers
mumbai_y_dist_lat_long = geodesic(mumbai_origin_lat_long, (mumbai_edge_lat_long[0], mumbai_origin_lat_long[1])).kilometers
mumbai_x_dist_lat_long = geodesic(mumbai_origin_lat_long, (mumbai_origin_lat_long[0], mumbai_edge_lat_long[1])).kilometers

# getting pixel coordinate component and total distances between refrence points
mumbai_total_dist_coords = distance(mumbai_origin_coords,mumbai_edge_coords)
mumbai_y_dist_coords = distance(mumbai_origin_coords, (mumbai_edge_coords[0], mumbai_origin_coords[1]))
mumbai_x_dist_coords = distance(mumbai_origin_coords, (mumbai_origin_coords[0], mumbai_edge_coords[1]))

# getting conversion between x distance in pixels to km
mumbai_x_factor = mumbai_x_dist_lat_long / mumbai_x_dist_coords
# getting conversion between y distance in pixels to km
mumbai_y_factor = -mumbai_y_dist_lat_long / mumbai_y_dist_coords

mumbai_total_factor = mumbai_total_dist_lat_long/mumbai_total_dist_coords


# In[10]:


def mumbai_get_lat_long(coord):
    
    y = coord[1] * mumbai_y_factor
    x = coord[0] * mumbai_x_factor
    
    lat  = mumbai_origin_lat_long[0] + (y / EARTH_RADIUS) * (180 / pi)
    long = mumbai_origin_lat_long[1] + (x / EARTH_RADIUS) * (180 / pi) / cos(mumbai_origin_lat_long[0] * pi/180)

    return (lat, long)


# In[34]:


# top left
# 17°34'45.79"N
# 78°13'0.72"E
# (17.57938611, 78.21666667)


# bottom right
# 17°15'52.42"N
# 78°39'2.54"E
# (17.26456111, 78.65083333)


# lattitude and Longitude reference points
hyderabad_origin_lat_long = (17.57938611, 78.21666667)
hyderabad_edge_lat_long = (17.26456111, 78.65083333)
# Pixel coordinate refrence points
hyderabad_origin_coords = (0, 0)
hyderabad_edge_coords = (1283, 1800)

# getting real world component and total distances between refrence points
hyderabad_total_dist_lat_long = geodesic(hyderabad_origin_lat_long, hyderabad_edge_lat_long).kilometers
hyderabad_y_dist_lat_long = geodesic(hyderabad_origin_lat_long, (hyderabad_edge_lat_long[0],hyderabad_origin_lat_long[1])).kilometers
hyderabad_x_dist_lat_long = geodesic(hyderabad_origin_lat_long, (hyderabad_origin_lat_long[0], hyderabad_edge_lat_long[1])).kilometers

# getting pixel coordinate component and total distances between refrence points
hyderabad_total_dist_coords = distance(hyderabad_origin_coords,hyderabad_edge_coords)
hyderabad_y_dist_coords = distance(hyderabad_origin_coords, (hyderabad_edge_coords[0], hyderabad_origin_coords[1]))
hyderabad_x_dist_coords = distance(hyderabad_origin_coords, (hyderabad_origin_coords[0], hyderabad_edge_coords[1]))

# getting conversion between x distance in pixels to km
hyderabad_x_factor = hyderabad_x_dist_lat_long / hyderabad_x_dist_coords
# getting conversion between y distance in pixels to km
hyderabad_y_factor = -hyderabad_y_dist_lat_long / hyderabad_y_dist_coords

hyderabad_total_factor = hyderabad_total_dist_lat_long/hyderabad_total_dist_coords


# In[12]:


def hyderabad_get_lat_long(coord):
    
    y = coord[1] * hyperbad_y_factor
    x = coord[0] * hyperbad_x_factor
    
    lat  = hyderabad_origin_lat_long[0] + (y / EARTH_RADIUS) * (180 / pi)
    long = hyderabad_origin_lat_long[1] + (x / EARTH_RADIUS) * (180 / pi) / cos(hyderabad_origin_lat_long[0] * pi/180)

    return (lat, long)


# In[35]:


# top left
#  13°11'50.67"N
#  80° 0'42.37"E
# (13.19740833, 80.01166667)


# bottom right
#  12°47'6.59"N
#  80°18'19.24"E
# (12.78516389, 80.30527778)


# lattitude and Longitude reference points
chennai_origin_lat_long = (13.19740833, 80.01166667)
chennai_edge_lat_long = (12.78516389, 80.30527778)
# Pixel coordinate refrence points
chennai_origin_coords = (0, 0)
chennai_edge_coords = (1074, 745)

# getting real world component and total distances between refrence points
chennai_total_dist_lat_long = geodesic(chennai_origin_lat_long, chennai_edge_lat_long).kilometers
chennai_y_dist_lat_long = geodesic(chennai_origin_lat_long, (chennai_edge_lat_long[0],chennai_origin_lat_long[1])).kilometers
chennai_x_dist_lat_long = geodesic(chennai_origin_lat_long, (chennai_origin_lat_long[0], chennai_edge_lat_long[1])).kilometers

# getting pixel coordinate component and total distances between refrence points
chennai_total_dist_coords = distance(chennai_origin_coords,chennai_edge_coords)
chennai_y_dist_coords = distance(chennai_origin_coords, (chennai_edge_coords[0], chennai_origin_coords[1]))
chennai_x_dist_coords = distance(chennai_origin_coords, (chennai_origin_coords[0], chennai_edge_coords[1]))

# getting conversion between x distance in pixels to km
chennai_x_factor = chennai_x_dist_lat_long / chennai_x_dist_coords
# getting conversion between y distance in pixels to km
chennai_y_factor = -chennai_y_dist_lat_long / chennai_y_dist_coords

chennai_total_factor = chennai_total_dist_lat_long/chennai_total_dist_coords


# In[119]:


def chennai_get_lat_long(coord):
    
    y = coord[1] * chennai_y_factor
    x = coord[0] * chennai_x_factor
    
    lat  = chennai_origin_lat_long[0] + (y / EARTH_RADIUS) * (180 / pi)
    long = chennai_origin_lat_long[1] + (x / EARTH_RADIUS) * (180 / pi) / cos(chennai_origin_lat_long[0] * pi/180)

    return (lat, long)


# In[36]:


# top left
#   28°56'17.27"N
#   76°45'57.52"E
# (28.93813056, 76.76611111)


# bottom right
#   28°24'47.67"N
#   77°35'14.60"E
# (28.41324167, 77.58750000)


# lattitude and Longitude reference points
delhi_origin_lat_long = (28.93813056, 76.76611111)
delhi_edge_lat_long = (28.41324167, 77.58750000)
# Pixel coordinate refrence points
delhi_origin_coords = (0, 0)
delhi_edge_coords = (745, 1074)

# getting real world component and total distances between refrence points
delhi_total_dist_lat_long = geodesic(delhi_origin_lat_long, delhi_edge_lat_long).kilometers
delhi_y_dist_lat_long = geodesic(delhi_origin_lat_long, (delhi_edge_lat_long[0],delhi_origin_lat_long[1])).kilometers
delhi_x_dist_lat_long = geodesic(delhi_origin_lat_long, (delhi_origin_lat_long[0], delhi_edge_lat_long[1])).kilometers

# getting pixel coordinate component and total distances between refrence points
delhi_total_dist_coords = distance(delhi_origin_coords,delhi_edge_coords)
delhi_y_dist_coords = distance(delhi_origin_coords, (delhi_edge_coords[0], delhi_origin_coords[1]))
delhi_x_dist_coords = distance(delhi_origin_coords, (delhi_origin_coords[0], delhi_edge_coords[1]))

# getting conversion between x distance in pixels to km
delhi_x_factor = delhi_x_dist_lat_long / delhi_x_dist_coords
# getting conversion between y distance in pixels to km
delhi_y_factor = -delhi_y_dist_lat_long / delhi_y_dist_coords

delhi_total_factor = delhi_total_dist_lat_long/delhi_total_dist_coords


# In[22]:


def delhi_get_lat_long(coord):
    
    y = coord[1] * delhi_y_factor
    x = coord[0] * delhi_x_factor
    
    lat  = delhi_origin_lat_long[0] + (y / EARTH_RADIUS) * (180 / pi)
    long = delhi_origin_lat_long[1] + (x / EARTH_RADIUS) * (180 / pi) / cos(delhi_origin_lat_long[0] * pi/180)

    return (lat, long)


# In[24]:


def get_pixel_coords(city, coord):
    
    if city == 'rio':
        
        y = (coord[0] - rio_origin_lat_long[0]) / (180 / pi) * EARTH_RADIUS 
        x = (coord[1] -  rio_origin_lat_long[1]) * cos(rio_origin_lat_long[0] * pi/180) / (180 / pi) * EARTH_RADIUS
        
        x = int(np.round(x / rio_x_factor))
        y = int(np.round(y / rio_y_factor))
        
        if x < 0:
            x = 0
        if y < 0:
            y = 0
            
        if x > rio_edge_coords[1]-1:
            x =  rio_edge_coords[1]-1
        if y >  rio_edge_coords[0]-1:
            y =  rio_edge_coords[0]-1
            
        return (x,y)
    
    elif city == 'mumbai':
        
        y = (coord[0] - mumbai_origin_lat_long[0]) / (180 / pi) * EARTH_RADIUS 
        x = (coord[1] -  mumbai_origin_lat_long[1]) * cos(mumbai_origin_lat_long[0] * pi/180) / (180 / pi) * EARTH_RADIUS
        
        x = int(np.round(x / mumbai_x_factor))
        y = int(np.round(y / mumbai_y_factor))
        
        if x < 0:
            x = 0
        if y < 0:
            y = 0
            
        if x > mumbai_edge_coords[1]-1:
            x = mumbai_edge_coords[1]-1
        if y > mumbai_edge_coords[0]-1:
            y = mumbai_edge_coords[0]-1
        
        return (x,y)
    elif city == 'hyderabad':
        
        y = (coord[0] - hyderabad_origin_lat_long[0]) / (180 / pi) * EARTH_RADIUS 
        x = (coord[1] -  hyderabad_origin_lat_long[1]) * cos(hyderabad_origin_lat_long[0] * pi/180) / (180 / pi) * EARTH_RADIUS
        
        x = int(np.round(x / hyderabad_x_factor))
        y = int(np.round(y / hyderabad_y_factor))
        
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        
        
        if x > hyderabad_edge_coords[1]-1:
            x = hyderabad_edge_coords[1]-1
        if y > hyderabad_edge_coords[0]-1:
            y = hyderabad_edge_coords[0]-1
        
        return (x,y)
    elif city == 'chennai':
        
        y = (coord[0] - chennai_origin_lat_long[0]) / (180 / pi) * EARTH_RADIUS 
        x = (coord[1] -  chennai_origin_lat_long[1]) * cos(chennai_origin_lat_long[0] * pi/180) / (180 / pi) * EARTH_RADIUS
        
        x = int(np.round(x / chennai_x_factor))
        y = int(np.round(y / chennai_y_factor))
        
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        
        
        if x > chennai_edge_coords[1]-1:
            x = chennai_edge_coords[1]-1
        if y > chennai_edge_coords[0]-1:
            y = chennai_edge_coords[0]-1
        
        return (x,y)
    elif city == 'delhi':
        
        y = (coord[0] - delhi_origin_lat_long[0]) / (180 / pi) * EARTH_RADIUS 
        x = (coord[1] -  delhi_origin_lat_long[1]) * cos(delhi_origin_lat_long[0] * pi/180) / (180 / pi) * EARTH_RADIUS
        
        x = int(np.round(x / delhi_x_factor))
        y = int(np.round(y / delhi_y_factor))
        
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        
        
        if x > delhi_edge_coords[1]-1:
            x = delhi_edge_coords[1]-1
        if y > delhi_edge_coords[0]-1:
            y = delhi_edge_coords[0]-1
        
        return (x,y)
        
    else:
        print("Error Invalid City, Valid Cities are rio, mumbai, delhi, chennai, and hyderabad")


# In[26]:


def get_slum_val(city, coord):
    
    pixel_coords = get_pixel_coords(city=city, coord=coord)
    
    if city == 'rio':
    
        if np.array(maps['rio_grayscale'])[pixel_coords[1], pixel_coords[0]][0] == 255:
            return 0
        else:
            return 1
        
    elif city == 'mumbai':
                                               
        if np.array(maps['mumbai_grayscale'])[pixel_coords[1], pixel_coords[0]][0] == 255:
            return 0
        else:
            return 1
    elif city == 'hyderabad':
        
        if np.array(maps['hyderabad_grayscale'])[pixel_coords[1], pixel_coords[0]][0] == 255:
            return 0
        else:
            return 1
    elif city == 'chennai':
        
        if np.array(maps['chennai_grayscale'])[pixel_coords[1], pixel_coords[0]][0] == 255:
            return 0
        else:
            return 1
    elif city == 'delhi':
        
        if np.array(maps['delhi_grayscale'])[pixel_coords[1], pixel_coords[0]][0] == 255:
            return 0
        else:
            return 1


# In[112]:


def check_suroundings(pixel_coords, image, search_range):
    points = []
    found = False
    for i in range(search_range):
        
        if np.array(image)[pixel_coords[1]+i, pixel_coords[0]][0] != 255:
            
            points.append([pixel_coords[1]+i, pixel_coords[0]])
            
            found = True
            
        elif np.array(image)[pixel_coords[1], pixel_coords[0]+i][0] != 255:
            
            points.append([pixel_coords[1], pixel_coords[0]+i])
                    
            found = True
            
        elif np.array(image)[pixel_coords[1]+i, pixel_coords[0]+i][0] != 255:
            
            points.append([pixel_coords[1]+i, pixel_coords[0]+i])
                        
            found = True
            
        elif np.array(image)[pixel_coords[1]-i, pixel_coords[0]][0] != 255:
            
            points.append([pixel_coords[1]-i, pixel_coords[0]])
                        
            found = True
            
        elif np.array(image)[pixel_coords[1], pixel_coords[0]-i][0] != 255:
            
            points.append([pixel_coords[1], pixel_coords[0]-i])
                        
            found = True
            
        elif np.array(image)[pixel_coords[1]-i, pixel_coords[0]-i][0] != 255:
            
            points.append([pixel_coords[1]-i, pixel_coords[0]-i])
                        
            found = True
            
        elif np.array(image)[pixel_coords[1]-i, pixel_coords[0]+i][0] != 255:
            
            points.append([pixel_coords[1]-i, pixel_coords[0]+i])
                        
            found = True
            
        elif np.array(image)[pixel_coords[1]+i, pixel_coords[0]-i][0] != 255:
            
            points.append([pixel_coords[1]+i, pixel_coords[0]-i])
                   
            found = True
        else:
            pass
        
        if found == True:
            
            
            if image == maps['rio_grayscale']:
                
                vecs = [(distance(pixel_coords, val) * rio_total_factor, ((pixel_coords[0] - val[0])*rio_x_factor, (pixel_coords[1] - val[1]) * rio_y_factor)) for val in points]
                
            elif image == maps['mumbai_grayscale']:
                
                vecs = [(distance(pixel_coords, val) * mumbai_total_factor, ((pixel_coords[0] - val[0])*mumbai_x_factor, (pixel_coords[1] - val[1]) * mumbai_y_factor)) for val in points]
                
            elif image == maps['hyderabad_grayscale']:
                
                vecs = [(distance(pixel_coords, val) * hyderabad_total_factor, ((pixel_coords[0] - val[0])*hyderabad_x_factor, (pixel_coords[1] - val[1]) * hyderabad_y_factor)) for val in points]
                
            elif image == maps['chennai_grayscale']:
                
                vecs = [(distance(pixel_coords, val) * chennai_total_factor, ((pixel_coords[0] - val[0])*chennai_x_factor, (pixel_coords[1] - val[1]) * chennai_y_factor)) for val in points]
                
            elif image == maps['delhi_grayscale']:
                
                vecs = [(distance(pixel_coords, val) * delhi_total_factor, ((pixel_coords[0] - val[0])*delhi_x_factor, (pixel_coords[1] - val[1]) * delhi_y_factor)) for val in points]
        
            return vecs


# In[117]:


def get_distance_from_slum(city, coord, search_range):
    
    pixel_coords = get_pixel_coords(city=city, coord=coord)
    search_range = search_range
    if city == 'rio':
    
        if np.array(maps['rio_grayscale'])[pixel_coords[1], pixel_coords[0]][0] != 255:
            return 0
        else:
            return check_suroundings(pixel_coords, maps['rio_grayscale'], search_range)
        
    elif city == 'mumbai':
                                               
        if np.array(maps['mumbai_grayscale'])[pixel_coords[1], pixel_coords[0]][0] != 255:
            return 0
        else:
            return check_suroundings(pixel_coords, maps['mumbai_grayscale'], search_range)
    elif city == 'hyderabad':
        
        if np.array(maps['hyderabad_grayscale'])[pixel_coords[1], pixel_coords[0]][0] != 255:
            return 0
        else:
            return check_suroundings(pixel_coords, maps['hyderabad_grayscale'], search_range)
    elif city == 'chennai':
        
        if np.array(maps['chennai_grayscale'])[pixel_coords[1], pixel_coords[0]][0] != 255:
            return 0
        else:
            return check_suroundings(pixel_coords, maps['chennai_grayscale'], search_range)
    elif city == 'delhi':
        
        if np.array(maps['delhi_grayscale'])[pixel_coords[1], pixel_coords[0]][0] != 255:
            return 0
        else:
            return check_suroundings(pixel_coords, maps['delhi_grayscale'], search_range)

