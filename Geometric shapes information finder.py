import time
name = input ('please enter your name: ')

print()
print('welcome ' + name)
print()

print('1. Three-dimensional shapes\n'
'2. Two-dimensional shapes')

Shape_type = input('Enter your Shape type(1/2): ')

if Shape_type == '1':
    print( )

    print('1. Cube\n'
    '2. Cube of Rectangle\n'
    '3. Pyramid\n'
    '4. cones\n'
    '5. Cylindrical\n'
    '6. sphere\n')

    name_of_Three_dimensional_shapes = input('Enter your number of Three-dimensional shapes: ')

    if name_of_Three_dimensional_shapes == '1':
        side_c = float (input('Enter cube\'s side: '))
        print()
        Volume_u1 = (side_c*side_c)*side_c
        Area_u1 = (side_c*side_c)*6
        Volume_u = str(round(Volume_u1 ,4))
        Area_u = str(round(Area_u1 ,4))
        print()
        print ('Volume:' + Volume_u +'\n'
        'Area: ' + Area_u)
        
        print()
        time.sleep(10)

    elif name_of_Three_dimensional_shapes == '2':
        first_side_c = float (input('Enter Cube of Rectangle\'s first side: '))
        second_side_c = float (input('Enter Cube of Rectangle\'s second side: '))
        third_side_c = float (input('Enter Cube of Rectangle\'s third side: '))
        print()
        Volume_ur1 = (first_side_c*second_side_c)*third_side_c
        Area_ur1 = (first_side_c*second_side_c)+(first_side_c*third_side_c)+(second_side_c*third_side_c)
        Volume_ur = str(round(Volume_ur1 ,4))
        Area_ur = str(round(Area_ur1, 4))
        print ('Volume:' + Volume_ur +'\n'
        'Area: ' + Area_ur)

        print()
        time.sleep(10)

    elif name_of_Three_dimensional_shapes == '3':
        print('1.Al-Qaeda Square Pyramid]\n''2.Al-Qaeda Triangle Pyramid')
        type_of_pyramid = input('Enter type of your charter: ')
        print()
        if type_of_pyramid == '1':
            side_p = float (input('Enter Triangle base\'s side'))
            height_p = float (input('Enter Triangle\'s height: '))
            Main_height_p = float (input('Enter pyramid\'s height: '))
            print()
            Area_p1 = ((side_p*height_p)/2)*5
            Volume_p1 = (((side_p*height_p)/2)+Main_height_p)/3

            Area_p = str (round(Area_p1,4))
            Volume_p = str (round(Volume_p1,4))

            print('Volume:' + Volume_p +'\n'
            'Area: ' + Area_p)

            print()
            time.sleep(10)

        elif type_of_pyramid == '2':
            side_pt = float (input('Enter square base\'s side: '))
            height_pt = float (input('Enter Triangle\'s height: '))
            Main_height_pt = float (input('Enter pyramid\'s height: '))
            print()

            Area_pt1 = (side_pt*side_pt)+((side_pt*height_pt)/2)
            Volume_pt1 = ((side_pt*side_pt)*Main_height_pt)/3
            Volume_pt = str (round(Volume_pt1,4))
            Area_pt = str (round(Area_pt1,4))

        print ('Volume:' + Volume_pt +'\n'
        'Area: ' + Area_pt)

        print()
        time.sleep(10)

    elif name_of_Three_dimensional_shapes == '4':
        b_Diameter_co = float (input ('Enter your base\' diameter: '))
        Slope_surface_size_co = float (input ('Enter your cones\' slope surface size: '))
        height_co = float (input ('Enter your cones\' height: '))
        print()
        Area_co1 = ((Slope_surface_size_co * (b_Diameter_co*3/14))/2)+ (((b_Diameter_co/2)*(b_Diameter_co/2))*3/14) 
        Volume_co1 = ((((b_Diameter_co/2)*(b_Diameter_co/2))*3/14) * height_co)/3

        Area_co = str(round(Area_co1,4))
        Volume_co = str(round(Volume_co1,4))

        print ('Volume:' + Volume_co +'\n'
        'Area: ' + Area_co)
        print()
        time.sleep(10)

    elif name_of_Three_dimensional_shapes == '5':
        b_Diameter_cy = float (input('Enter your base\' diameter: ')) 
        Length_cy = float (input('Enter your cylindrical\'length : '))
        print()
        Area_cy1 = ((b_Diameter_cy*3.14)*Length_cy) + (((b_Diameter_cy/2*b_Diameter_cy/2)*3.14)*2)
        Volume_cy1 = (((b_Diameter_cy/2*b_Diameter_cy/2)*3.14)*2) * Length_cy
        Area_cy = str (round(Area_cy1,4))
        Volume_cy = str (round(Volume_cy1,4))
        print ('Volume:' + Volume_cy +'\n'
        'Area: ' + Area_cy)
        print()
        time.sleep(10)

    elif name_of_Three_dimensional_shapes == '6':
        Radius_sph = float (input('Enter your sphere\'radius: '))
        print()
        Area_sph1 = ((Radius_sph^2)*3.14)*4
        Volume_sph1 = (((Radius_sph^3)*3.14)/3)*4
        Area_sph = str (round(Area_sph1,4))
        Volume_sph = str (round(Volume_sph1,4))

        print ('Volume:' + Volume_sph +'\n'
        'Area: ' + Area_sph)

        print()
        time.sleep(10)

elif Shape_type == '2':
    print()
    print('1. Square\n'
    '2. Rectangle\n'
    '3. Triangle\n'
    '4. Circle\n'
    '5. Diamond\n'
    '6. Trapezius\n')

    name_of_Two_dimensional_shapes = input('Enter your number of Two-dimensional shapes: ')

    if name_of_Two_dimensional_shapes == '1':
        side = float (input('Enter Square\'s side: '))
        print()
        surrounding_s1 = side*4
        Area_s1 = side*side
        surrounding_s = str(round(surrounding_s1,4))
        Area_s = str(round(Area_s1,4))
        print ('surroundings:' + surrounding_s +'\n'
        'Area: ' + Area_s + '\n'
        'Angle: ' + '360')
        print()
        time.sleep(10)

    elif name_of_Two_dimensional_shapes == '2':
        Length = float (input('Enter Rectangle\'s Length: '))
        width = float (input('Enter Rectangle\'s width: '))
        print()
        surroundings_r1 = (Length + width)*2
        Area_r1 = Length*width
        surroundings_r = str(round(surroundings_r1,4))
        Area_r = str(round(Area_r1,4))
        print ('surroundings:' + surroundings_r +'\n'
        'Area: ' + Area_r + '\n'
        'Angle: ' + '360')
        print()
        time.sleep(10)

    elif name_of_Two_dimensional_shapes == '3':
        base =  float (input('Enter Triangle\'s base: '))
        height = float (input('Enter Triangle\'s height: '))
        print()
        surroundings_r1 = base*3
        Area_t1 = base*height/2
        surroundings_r = str(round(surroundings_r1,4))
        Area_t = str(round(Area_t1,4))

        print ('surroundings:' + surroundings_r +'\n'
        'Area: ' + Area_t + '\n'
        'Angle: ' + '180')
        print()
        time.sleep(10)
    elif name_of_Two_dimensional_shapes == '4':

        radius = float(input('Enter Triangle\'s radius: '))
        print()
        Diameter = (radius*2)
        surroundings_c1 = Diameter*3.14
        Area_c1 = (radius*radius)*3.14
        surroundings_c = str(round(surroundings_c1,4))
        Area_c = str(round(Area_c1,4))

        print ('surroundings:' + surroundings_c +'\n'
        'Area: ' + Area_c + '\n'
        'Angle: ' + '-')
        print()

        time.sleep(10)
    elif name_of_Two_dimensional_shapes == '5':
        side = float (input('Enter Diamond\'s side: '))
        little_Diameter = float (input('Enter Diamond\'s little_Diameter: '))
        big_Diameter = float (input('Enter Diamond\'s big_Diameter: '))
        print()
        surrounding_d1 = side*4
        Area_d1 = (big_Diameter*little_Diameter)/2
        surrounding_d = str(round(surrounding_d1,4))
        Area_d = str(round(Area_d1,4))

        print ('surroundings:' + surrounding_d +'\n'
        'Area: ' + Area_d + '\n'
        'Angle: ' + '360')
        print()

        time.sleep(10)
    elif name_of_Two_dimensional_shapes == '6':
        trapezius_s_height = float (input('Enter Trapezius\'s height: '))
        big_base = float (input('Enter Trapezius\'s big_base: '))
        little_base = float (input('Enter Trapezius\'s little_base: '))
        first_side = float (input('Enter Trapezius\'s first side: '))
        second_side = float (input('Enter Trapezius\'s second side: '))
        third_side = float (input('Enter Trapezius\'s third side: '))
        fourth_side = float (input('Enter Trapezius\'s fourth side: '))
        print()
        surrounding_d1 = (first_side + second_side) + (third_side + fourth_side)
        Area_d1 = ((big_base*little_base)/2)*trapezius_s_height
        surrounding_d = str(round(surrounding_d1,4))
        Area_d = str(round(Area_d1,4))

        print ('surroundings:' + surrounding_d +'\n'
        'Area: ' + Area_d + '\n'
        'Angle: ' + '360')
        print()

        time.sleep(10)
else:
    print('Error!')
    print()
    time.sleep(10)
