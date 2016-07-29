# import html accessability
import urllib2, json

# define static variables
groupName = raw_input('What is the name of the group you wish to retrieve events for?')
eventCount = raw_input('How many events do you want to check?')



def getApiData(groupName, eventCount):
    try:
        eventCount = int(eventCount)
    except:
        print('You entered an invalid number')

    resultDict = {}
    #staticUrl = 'https://api.meetup.com/2/events?key=1074395949437b7e6522f50657f5d2a&group_urlname=DCPython'
    dynUrl = 'https://api.meetup.com/2/events?key=1074395949437b7e6522f50657f5d2a&group_urlname=' + groupName

    # request API data
    apiData = urllib2.urlopen(dynUrl).read()

    # parse the api data to populate needed variables
    content = json.loads(apiData)
    results = content['results']
    resultCount = 0

    # count number of events
    for i in results:
        resultCount += 1
        if resultCount < eventCount:
            eventName = i['name']
            yesRsvp = i['yes_rsvp_count']
            resultDict['event ' + str(resultCount)] = {'name': eventName, 'count': yesRsvp}
            print(eventName + ' - ' + str(yesRsvp))
    print(resultDict)

getApiData(groupName, eventCount)
