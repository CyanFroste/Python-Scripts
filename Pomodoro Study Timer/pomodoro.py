# Pomodoro Study Interval
try :
    import winsound, time
    
    def alarm(breakSpecifier) :
        if breakSpecifier == 'short' :
            winsound.PlaySound("NFF-carillon-1", winsound.SND_FILENAME)         # Start of interval
            time.sleep(600)     # 10 min
            winsound.PlaySound("NFF-carillon-2", winsound.SND_FILENAME)         # End of Interval
        if breakSpecifier == 'long' :
            winsound.PlaySound("NFF-carillon-1", winsound.SND_FILENAME)         # Start of Interval
            time.sleep(3600)    # 1 hr
            winsound.PlaySound("NFF-carillon-2", winsound.SND_FILENAME)         # End of Interval
    loop = 0
    while True :
        # print(loop)
        time.sleep(1200)        # 20 min
        if loop == 2 :  
            alarm('long')       # Long Interval every 3rd break
        else :
            alarm('short')      
        loop = (loop + 1) % 3        
except ImportError :
    print("Only for Windows")