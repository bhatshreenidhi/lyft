from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 3956 # Radius of earth in miles
    return c * r


'''
Assuming the input to this method - latitude and longitude are the lists containing the latitude and longitude values of 4 points A B C D in order

Problem:
Calculate the detour distance between two different rides. 
Given four latitude / longitude pairs, where driver one is traveling from point A to point B and driver two is traveling from point C to point D, 
Calculate the shorter of the detour distances the drivers would need to take to pick-up and drop-off the other driver.

Solution:
The detour paths possible are A->C->D->B or C->A->B->D. Here the probelm is to find the minimum possible detour distance. What we can see from the possible paths
is that :

1. if distance between A and B is greater that that of C and D, then driver1 traveling from A to B can make the detour with minimum extra distance being covered
1. if distance between C and D is greater that that of A and B, then driver2 traveling from C to D can make the detour with minimum extra distance being covered

For the purpose of this problem, I have considered haversine distance 
'''
def getDetourPath(A,B,C,D):
    
    distAB = haversine(A[0],A[1],B[0],B[1])
    distCD = haversine(C[0],C[1],D[0],D[1])
    detourDist = abs(distAB-distCD)

    if(distAB>distCD):
        print('Driver1 can make a detour to cover driver2\'s route -> A C D B')
    else:
        print('Driver2 can make a detour to cover driver1\'s route -> C A B D')

    print('Detour distance in miles :'+str(detourDist))

    return detourDist



if(__name__ == "__main__"):

    # Get the various tuples
    A = (1,1)
    B = (2,5)
    C = (5,8)
    D = (13,18)

    getDetourPath(A,B,C,D)