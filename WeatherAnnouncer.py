def weatherAnnouncer(temp, clearSkies, windy):
    #try to combine these two statements into one if statement!
    tempClass = temperatureClassification(temp)
    if(tempClass == 'HOT' and clearSkies and windy):
        return 'Wear summer clothes today.'
    if(tempClass == 'HOT' and clearSkies and not windy):
        return 'Wear summer clothes today.'
    if(tempClass == 'HOT' and not clearSkies and windy):
        return 'Wear summer clothes today, but bring a rain jacket just in case.'
    if(tempClass == 'HOT' and not clearSkies and not windy):
        return 'Wear summer clothes today, but bring an umbrella just in case.'
    if(tempClass == 'FAIR' and clearSkies and windy):
        return 'Wear a jacket today.'
    if(tempClass == 'FAIR' and clearSkies and not windy):
        return 'Wear whatever you would like today.'
    if(tempClass == 'FAIR' and not clearSkies and windy):
        return 'Wear a jacket today.'
    if(tempClass == 'FAIR' and not clearSkies and not windy):
        return 'Wear a jacket today.'
    if(tempClass == 'COLD' and clearSkies and windy):
        return 'Wear winter gear today.'
    if(tempClass == 'COLD' and clearSkies and not windy):
        return 'Wear winter gear today.'
    if(tempClass == 'COLD' and not clearSkies and windy):
        return 'Just stay inside today.'
    if(tempClass == 'COLD' and not clearSkies and not windy):
        return 'Wear winter gear today.'


def temperatureClassification(temp):
    if temp < 40:
        return "COLD"
    elif temp < 75:
        return "FAIR"
    else:
        return "HOT"


#if hot and clear and not windy: 'Wear summer clothes today. 
print('TESTING', weatherAnnouncer(77, True, False))
# if hot and not clear and windy: 'Wear summer clothes today, but bring a rain jacket just in case.'
print('TESTING', weatherAnnouncer(95, False, True))
# if hot and not clear and not windy: 'Wear summer clothes today, but bring an umbrella just in case.'
print('TESTING', weatherAnnouncer(95, False, False))

# if fair AND clear AND not windy: 'Wear whatever you would like today.'
print('TESTING', weatherAnnouncer(56, True, False))
# if fair AND otherwise: 'Wear a jacket today.'
print('TESTING', weatherAnnouncer(56, False, False))

# if cold AND windy AND PC: 'Just stay inside today.'
print('TESTING', weatherAnnouncer(22, False, True))
# if cold AND otherwise: 'Wear winter gear today.'
print('TESTING', weatherAnnouncer(2, True, True)) 
