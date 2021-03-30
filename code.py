from pynotifier import Notification

import psutil



def test():
    battery=psutil.sensors_battery()
    percent=battery.percent
    return percent



def main():
        with open ('file.txt','w') as f:

                p=test()
                f.write('BATTERY PERCENTAGE IS {}%'.format(p))



if __name__=='__main__':
    main()

