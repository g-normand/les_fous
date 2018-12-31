
from fla import get_calendar
calendar = get_calendar(2958)

calendar_7 = get_calendar(3041)
calendar.update(calendar_7)

for date in sorted(calendar, reverse=True):
    journee = calendar[date]
    print '%s' % date
    print 'terrain : %s' % journee['Terrain'].encode('utf-8')
    infos = '%s %s' % (journee['Equipedom'].ljust(25, ' '), journee['Equipeext'].ljust(25, ' '))
    if journee['Scoredom'] is not None:
        infos += ': SCORE %s - %s' % (journee['Scoredom'], journee['Scoreext'])
    print (infos)
    print ''