'''
Created on 2013-7-31

@author: E525649
'''
import threading, time
need_stop_all=False
import Config
from SBPS import ProtocolReactor
from Command.EventDev import CEventDev

setTimer=set()
def patrol():
    ''' # release dead sessions
    if ProtocolReactor.instance_SBProtocolFactory is not None:
        with ProtocolReactor.instance_SBProtocolFactory.lockDict:
            for protocol in ProtocolReactor.instance_SBProtocolFactory.dictSuperbox.items():
                if protocol.isDeadSession():    protocol.releaseFromDict()
            for listProtocol in ProtocolReactor.instance_SBProtocolFactory.dictAccounts.items():
                for protocol in listProtocol:
                    if protocol.isDeadSession():    protocol.releaseFromDict()
    '''
    
    
    
                    
    if need_stop_all==False:
        timer=threading.Timer(Config.interval_patroller, patrol)
        global setTimer
        setTimer.update((timer,))
        timer.start()
        
def DailyPatrol():
    # release buffered state of dead device
    with CEventDev.lockEventBuffer:
        timeNow=time.time()
        for device_code in CEventDev.dictEventBuffer.keys():
            bufferedStates=CEventDev.dictEventBuffer[device_code]
            for i in reversed(range(0,len(bufferedStates))):
                bufferedState=bufferedStates[i]
                if timeNow-bufferedState.time>Config.timeout_buffered_state:
                    bufferedStates.pop(i)
            if len(bufferedStates)<=0:
                CEventDev.dictEventBuffer.pop(device_code)
    
    if need_stop_all==False:
        timer=threading.Timer(60*60*24, patrol)
        global setTimer
        setTimer.update((timer,))
        timer.start()
        
def Run():
    patrol()

def StopAll():
    global need_stop_all,setTimer
    need_stop_all=True
    for timer in setTimer:
        timer.cancel()
    setTimer.clear()
    
    

