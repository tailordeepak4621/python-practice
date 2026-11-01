distance_mi = 5
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = False

if distance_mi == 0:
    print("False")
elif distance_mi <= 1:
    if is_raining :
        print("False")
    else:
        print("True")        
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print("True")
    else:
        print("False")
else :
    if has_car or has_ride_share_app :
        print("True")
    else:
        print("False")    