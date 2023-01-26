from math import pi

# Вывод 2.5 10
# S=pi*a*b

orbits= [(1,3),(2.5,10),(7,2),(6,6),(4,3)]


# def find_farthest_orbit (list_of_orbits):
#     s_max=0
#     index=0
#     list_s=[]
    
#     def square(a,b):
#         return pi*a*b
    
#     for i in range(len(list_of_orbits)):
#         x= list_of_orbits[i][0]
#         y= list_of_orbits[i][1]
#         if x!=y:
#             if square(x, y)>s_max:
#                 s_max=square(x, y)
#                 index=i
#     # list_s.append(pi*list_of_orbits[i][0]*list_of_orbits[i][1])
#     return [list_of_orbits[index], s_max]
    
# print (*find_farthest_orbit(orbits))

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# def find_farthest_orbit(orbits):
#     s = [3.14*max(x)*min(x) if max(x) != min(x) else 0 for x in orbits]
#     print(s)
    
#     return(orbits[s.index(max(s))])
# print(*find_farthest_orbit(orbits))

def find_farthest_orbit(list_of_orbits):
    print('in',list_of_orbits)
    list_of_elliptical_orbits = list(filter(lambda x: x[0]!=x[1], list_of_orbits))
    # [i for i in list_of_orbits if i[0] != i[1]]
    print('only elliptical',list_of_elliptical_orbits)
    list_of_areas = [(pi * i[0] * i[1]) for i in list_of_elliptical_orbits]
    print('list areas', list_of_areas)
    max_area_index = list_of_areas.index(max(list_of_areas))
    print('winner', max_area_index)
    print( list_of_elliptical_orbits[max_area_index])

find_farthest_orbit(orbits)


  
