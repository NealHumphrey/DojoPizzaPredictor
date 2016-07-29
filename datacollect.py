# import html accessability
import urllib2

# define static variables
staticUrl = 'https://api.meetup.com/2/events?key=1074395949437b7e6522f50657f5d2a&group_urlname=DCPython'
print(staticUrl)

# request API data
apiData = urllib2.urlopen(staticUrl).read()
print(apiData)

# parse the api data to populate needed variables

# variable results

# call neal's program and pass the collected variable results


