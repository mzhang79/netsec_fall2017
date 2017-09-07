from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import UINT32, BOOL, STRING

class ConnectionRequest(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.student_x.MyPacket1"
    DEFINITION_VERSION = "1.0"
    FIELDS = []
#This is the class used in the first step of my protocol: client send ConnectionRequest() to server

class VerifyingInfo(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.student_x.MyPacket2"
    DEFINITION_VERSION = "1.0"
    FIELDS = [
      ("ID", UINT32),
      ("IfPermit", BOOL)
    ]
#This is the class used in the second step of my protocol:server send VerifyingInfo(ID, IfPermit) to client

class ConnectionInfo(PacketType):
    DEFINITION_IDENTIFIER = "lab1b.student_x.MyPacket3"
    DEFINITION_VERSION = "1.0"
    FIELDS = [
      ("ID", UINT32),
      ("Address", STRING)
    ]
#This is the class used in the third step of my protocol:client send ConnectionInfo(ID, address) to server

def basicUnitTest1():
    packetCR = ConnectionRequest()
    packetCRBytes = packetCR.__serialize__()
    packetCRa = ConnectionRequest.Deserialize(packetCRBytes)
    assert packetCR == packetCRa
    #test the first class
    
    packetVI = VerifyingInfo()
    packetVI.ID = 1
    packetVI.IfPermit = True
    packetVIBytes = packetVI.__serialize__()
    packetVIa = VerifyingInfo.Deserialize(packetVIBytes)
    assert packetVI == packetVIa
    #test the second class
    
    packetCI = ConnectionInfo()
    packetCI.ID = 1
    packetCI.Address = "1.1.1.1"
    packetCIBytes = packetCI.__serialize__()
    packetCIa = ConnectionInfo.Deserialize(packetCIBytes)
    assert packetCI == packetCIa
    #test the third class
    
    print("This is UnitTest1. It works!")
    
def basicUnitTest2():
#I use this UnitTest2 to test what will happen when there is an invalid assignment

    packetVI = VerifyingInfo()
    try:
      packetVI.IfPermit = TRUE 
      #This is an invalid assignment because the value of packetVI.IfPermit is a BOOL(True/False)
    except:
      print("OOPS, there is an except in the UnitTest2 because of an invalid value!")
      #Whenever there is a invalid assignment, a except will be thrown out
    else:
      print("This is UnitTest2. It works too!")
      #If there is no except, it will execute this statement
   
if __name__ == "__main__":
    basicUnitTest1()
    basicUnitTest2()
  
    
    
    
    
