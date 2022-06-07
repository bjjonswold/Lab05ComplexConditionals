# conditions: 
#   temp (hot, fair, cold)
#   windy or not windy
#   sky conditions (persperating or cloudy, clear skies)
#
#   temp is a number <40 is cold, <75 is fair, else is hot
#
#
#   hot, windy, clear:          summer clothes
#   hot, not windy, clear:      summer clothes
#   
#   hot, windy, pc:             summer clothes, rain jacket
#   hot, not windy, pc:         summer clothes, umbrella
#   
#   fair, windy, clear:       wear whatever
#   fair, not windy, clear:   wear whatever
#   
#   fair, windy, pc:          wear whatever, rain jacket
#   fair, not windy, pc:      wear whatever, umbrella
#
#   cold, windy, clear:         winter clothes needed
#   cold, not windy, clear:     winter clothes needed
#   
#   cold, windy, pc:            just stay inside
#   cold, not windy, pc:        winter clothes needed


# if hot AND clear: summer clothers
# if hot and pc: summer clothes
        # if/ else for rain jacket/umbrella
# if fair AND clear: wear whatever
# if fair AND PC: wear whatever
        #if/ else for rain jacket/umbrella
# if cold:
        #AND windy AND PC: just stay inside
        #else: winter gear needed

def weatherAnnouncement(temp, windy, clearSkies):
    recommendation = ''
    tempClass = temperatureClassification(temp)
    if(tempClass == 'Hot' and clearSkies):
        return 'Wear summer clothes today'
        #1/2 possible ends of included code for students for this function
    if(tempClass == 'Hot' and not clearSkies):
        gear = rainGearCheck(windy)
        return 'Wear summer clothes today, but ' + gear
        #2/2 possible ends


#This can be deleted if lab is determined to be too difficult
#Can serve as first test in zybooks if kept
def temperatureClassification(temp):
    if(temp < 40):
        return 'Cold'
    elif(temp < 75):
        return 'Fair'
    else:
        return 'Hot'

#optional helper method
def rainGearCheck(windy):
    if(windy):
        return 'rain jacket'
    else:
        return 'umbrella'

def main():
    print('TESTING', weatherAnnouncement(77, False,True))
    #make a real python main