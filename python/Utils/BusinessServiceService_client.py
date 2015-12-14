##################################################
# file: BusinessServiceService_client.py
# 
# client stubs generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#     /usr/bin/wsdl2py http://www.jianzhou.sh.cn/JianzhouSMSWSServer/services/BusinessService?wsdl
# 
##################################################

from BusinessServiceService_types import *
import urlparse, types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
from ZSI.schema import GED, GTD
import ZSI

# Locator
class BusinessServiceServiceLocator:
    BusinessServicePort_address = "http://www.jianzhou.sh.cn/JianzhouSMSWSServer/services/BusinessService"
    def getBusinessServicePortAddress(self):
        return BusinessServiceServiceLocator.BusinessServicePort_address
    def getBusinessServicePort(self, url=None, **kw):
        return BusinessServiceServiceSoapBindingSOAP(url or BusinessServiceServiceLocator.BusinessServicePort_address, **kw)

# Methods
class BusinessServiceServiceSoapBindingSOAP:
    def __init__(self, url, **kw):
        kw.setdefault("readerclass", None)
        kw.setdefault("writerclass", None)
        # no resource properties
        self.binding = client.Binding(url=url, **kw)
        # no ws-addressing

    # op: getReceivedMsg
    def getReceivedMsg(self, request, **kw):
        if isinstance(request, getReceivedMsg) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="", **kw)
        # no output wsaction
        response = self.binding.Receive(getReceivedMsgResponse.typecode)
        return response

    # op: sendBatchMessageTimelyExt
    def sendBatchMessageTimelyExt(self, request, **kw):
        if isinstance(request, sendBatchMessageTimelyExt) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="", **kw)
        # no output wsaction
        response = self.binding.Receive(sendBatchMessageTimelyExtResponse.typecode)
        return response

    # op: sendPersonalMessages
    def sendPersonalMessages(self, request, **kw):
        if isinstance(request, sendPersonalMessages) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="", **kw)
        # no output wsaction
        response = self.binding.Receive(sendPersonalMessagesResponse.typecode)
        return response

    # op: modifyPassword
    def modifyPassword(self, request, **kw):
        if isinstance(request, modifyPassword) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="", **kw)
        # no output wsaction
        response = self.binding.Receive(modifyPasswordResponse.typecode)
        return response

    # op: getReceipt
    def getReceipt(self, request, **kw):
        if isinstance(request, getReceipt) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="", **kw)
        # no output wsaction
        response = self.binding.Receive(getReceiptResponse.typecode)
        return response

    # op: sendBatchMessage
    def sendBatchMessage(self, request, **kw):
        if isinstance(request, sendBatchMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="", **kw)
        # no output wsaction
        response = self.binding.Receive(sendBatchMessageResponse.typecode)
        return response

    # op: sendGjBatchMessage
    def sendGjBatchMessage(self, request, **kw):
        if isinstance(request, sendGjBatchMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="", **kw)
        # no output wsaction
        response = self.binding.Receive(sendGjBatchMessageResponse.typecode)
        return response

    # op: validateUser
    def validateUser(self, request, **kw):
        if isinstance(request, validateUser) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="", **kw)
        # no output wsaction
        response = self.binding.Receive(validateUserResponse.typecode)
        return response

    # op: sendMessage
    def sendMessage(self, request, **kw):
        if isinstance(request, sendMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="", **kw)
        # no output wsaction
        response = self.binding.Receive(sendMessageResponse.typecode)
        return response

    # op: sendTimelyMessage
    def sendTimelyMessage(self, request, **kw):
        if isinstance(request, sendTimelyMessage) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="", **kw)
        # no output wsaction
        response = self.binding.Receive(sendTimelyMessageResponse.typecode)
        return response

    # op: gxmt
    def gxmt(self, request, **kw):
        if isinstance(request, gxmt) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="", **kw)
        # no output wsaction
        response = self.binding.Receive(gxmtResponse.typecode)
        return response

    # op: sendMmsMessages
    def sendMmsMessages(self, request, **kw):
        if isinstance(request, sendMmsMessages) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="", **kw)
        # no output wsaction
        response = self.binding.Receive(sendMmsMessagesResponse.typecode)
        return response

    # op: getUserInfo
    def getUserInfo(self, request, **kw):
        if isinstance(request, getUserInfo) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="", **kw)
        # no output wsaction
        response = self.binding.Receive(getUserInfoResponse.typecode)
        return response

    # op: sendAudio
    def sendAudio(self, request, **kw):
        if isinstance(request, sendAudio) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="", **kw)
        # no output wsaction
        response = self.binding.Receive(sendAudioResponse.typecode)
        return response

getReceivedMsg = GED("http://service.nineorange.com", "getReceivedMsg").pyclass

getReceivedMsgResponse = GED("http://service.nineorange.com", "getReceivedMsgResponse").pyclass

sendBatchMessageTimelyExt = GED("http://service.nineorange.com", "sendBatchMessageTimelyExt").pyclass

sendBatchMessageTimelyExtResponse = GED("http://service.nineorange.com", "sendBatchMessageTimelyExtResponse").pyclass

sendPersonalMessages = GED("http://service.nineorange.com", "sendPersonalMessages").pyclass

sendPersonalMessagesResponse = GED("http://service.nineorange.com", "sendPersonalMessagesResponse").pyclass

modifyPassword = GED("http://service.nineorange.com", "modifyPassword").pyclass

modifyPasswordResponse = GED("http://service.nineorange.com", "modifyPasswordResponse").pyclass

getReceipt = GED("http://service.nineorange.com", "getReceipt").pyclass

getReceiptResponse = GED("http://service.nineorange.com", "getReceiptResponse").pyclass

sendBatchMessage = GED("http://service.nineorange.com", "sendBatchMessage").pyclass

sendBatchMessageResponse = GED("http://service.nineorange.com", "sendBatchMessageResponse").pyclass

sendGjBatchMessage = GED("http://service.nineorange.com", "sendGjBatchMessage").pyclass

sendGjBatchMessageResponse = GED("http://service.nineorange.com", "sendGjBatchMessageResponse").pyclass

validateUser = GED("http://service.nineorange.com", "validateUser").pyclass

validateUserResponse = GED("http://service.nineorange.com", "validateUserResponse").pyclass

sendMessage = GED("http://service.nineorange.com", "sendMessage").pyclass

sendMessageResponse = GED("http://service.nineorange.com", "sendMessageResponse").pyclass

sendTimelyMessage = GED("http://service.nineorange.com", "sendTimelyMessage").pyclass

sendTimelyMessageResponse = GED("http://service.nineorange.com", "sendTimelyMessageResponse").pyclass

gxmt = GED("http://service.nineorange.com", "gxmt").pyclass

gxmtResponse = GED("http://service.nineorange.com", "gxmtResponse").pyclass

sendMmsMessages = GED("http://service.nineorange.com", "sendMmsMessages").pyclass

sendMmsMessagesResponse = GED("http://service.nineorange.com", "sendMmsMessagesResponse").pyclass

getUserInfo = GED("http://service.nineorange.com", "getUserInfo").pyclass

getUserInfoResponse = GED("http://service.nineorange.com", "getUserInfoResponse").pyclass

sendAudio = GED("http://service.nineorange.com", "sendAudio").pyclass

sendAudioResponse = GED("http://service.nineorange.com", "sendAudioResponse").pyclass
