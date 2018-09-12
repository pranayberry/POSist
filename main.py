import base64
from hashlib import md5
import time
import random
#I have used hashlib library to perform md5 hashing, time library for datetime operations, random library to generate random data and base64 library for encoding and decoding the data

def computeKey(value):
    return md5(str(value).encode('utf-8')).hexdigest()

def decode(key, string):
    decoded = base64.b64decode(string).decode("utf-8")
    finalOP = decoded.replace(key,"")
    return finalOP        
def encode(key, string):
    string = key+string
    return base64.b64encode(string.encode())

class Node:
   def __init__(self,
   timestamp,
   ownerId,
   ownerName,
   nodeNumber,
   nodeId,
   referenceNodeId,
   childReferenceNodeId,
   genesisReferenceNodeId,
   HashValue,
   data
   ):
       self.timestamp = timestamp
       self.nodeNumber = nodeNumber
       self.nodeId = nodeId
       self.ownerId = ownerId
       self.ownerName = ownerName
       self.referenceNodeId = referenceNodeId
       self.childReferenceNodeId = childReferenceNodeId
       self.genesisReferenceNodeId = genesisReferenceNodeId
       self.HashValue = HashValue
       self.data = data

   def getHashKey(self):
       return self.dataHashKey
   def setHashKey(self,val):
       self.dataHashKey = val
   def getOwnerId(self):
       return self.ownerId
   def setOwnerId(self,val):
       self.ownerId = val
   def getOwnerName(self):
       return self.ownerName
   def setOwnerName(self,val):
       self.ownerName = val
   def getTimeStamp(self):
       return self.timestamp
   def setTimeStamp(self,val):
       self.timestamp = val
   def getNodeNumber(self):
       return self.nodeNumber
   def setNodeNumber(self,val):
       self.nodeNumber = val
   def getNodeId(self):
       return self.nodeId
   def setNodeId(self,val):
       self.nodeId = val
   def getReferenceNodeId(self):
       return self.referenceNodeId
   def setReferenceNodeId(self,val):
       self.referenceNodeId = val
   def getChildReferenceNodeId(self):
       return self.childReferenceNodeId
   def setChildReferenceNodeId(self,val):
       self.childReferenceNodeId = val
   def getGenesisReferenceNodeId(self):
       return self.genesisReferenceNodeId
   def setGenesisReferenceNodeId(self,val):
       self.genesisReferenceNodeId = val
   def getHashValue(self):
       return self.HashValue
   def setHashValue(self,val):
       self.HashValue = val 
   def getData(self):
       return self.data
   def setData(self,val):
       self.data = val
   def __str__(self):
       strNode = ""
       strNode+= "timestamp : "+str(self.timestamp)+"\n"
       strNode+= "nodeNumber : "+str(self.nodeNumber)+"\n"
       strNode+= "nodeId : "+str(self.nodeId)+"\n"
       strNode+= "ownerId : "+str(self.ownerId)+"\n"
       strNode+= "ownerName : "+str(self.ownerName)+"\n"
       strNode+= "referenceNodeId : "+str(self.referenceNodeId)+"\n"
       strNode+= "childReferenceNodeId : "+str(self.childReferenceNodeId)+"\n"
       strNode+= "genesisReferenceNodeId : "+str(self.genesisReferenceNodeId)+"\n"
       strNode+= "HashValue : "+str(self.HashValue)+"\n"
       strNode+= "data : "+str(self.data)+"\n"
       return strNode
    
class Tree:
    def __init__(self, node=None):
        self.node = node
        self.left = None
        self.right = None

    def getNode(self):
        return self.node

    def computeKey(self,value):
        return md5(str(value).encode('utf-8')).hexdigest()

    def decode(self,key, string):
        decoded = base64.b64decode(string).decode("utf-8")
        return decoded.replace(key,"")
            
    def encode(self,key, string):
        string = key+string
        return base64.b64encode(string.encode())

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        decodedNode = decode(self.node.getHashKey(),self.node.getData())
        print(decodedNode,end=' ')
        if self.right is not None:
            self.right.inorder()

    def set_root(self, node):
        self.node = node
 
    def insertLeft(self, new_node):
        self.left = new_node
 
    def insertRight(self, new_node):
        self.right = new_node

def buildNode(data,genesisId,ownerId,ownerName,currentNodeNumber):
    timestamp = time.time()
    nodeNumber = currentNodeNumber
    nodeId = computeKey(nodeNumber)
    referenceNodeId = ownerId
    childReferenceNodeId = []
    genesisReferenceNodeId = genesisId
    HashValueSet = str([timestamp, data,nodeNumber, nodeId, referenceNodeId,childReferenceNodeId, genesisReferenceNodeId])
    HashValue = computeKey(encode(computeKey(HashValueSet),HashValueSet).decode('utf-8'))
    dataHashSet = str([ownerId,data,ownerName])
    data = encode(computeKey(dataHashSet),str(data)).decode('utf-8')
    newNode = Node(timestamp,ownerId,ownerName,nodeNumber,nodeId,referenceNodeId,childReferenceNodeId,genesisReferenceNodeId,HashValue,data)
    newNode.setHashKey(computeKey(dataHashSet))
    return newNode

currentNodeNumber = 0
genesisId = computeKey(random.random())
_Tree = Tree()

_Tree.set_root(buildNode(30,genesisId,genesisId,"Root",currentNodeNumber))
LeftNode = Tree(buildNode(17,genesisId,genesisId,"Genesis",currentNodeNumber))
_Tree.insertLeft(LeftNode)
currentNodeNumber+=1
RightNode = Tree(buildNode(10,genesisId,genesisId,"Genesis",currentNodeNumber))
_Tree.insertRight(RightNode)

currentNodeNumber+=1
LeftNode_Child1 = Tree(buildNode(6,genesisId,LeftNode.getNode().getNodeId(),LeftNode.getNode().getNodeNumber(),currentNodeNumber))
currentNodeNumber+=1
LeftNode_Child2 = Tree(buildNode(3,genesisId,LeftNode.getNode().getNodeId(),LeftNode.getNode().getNodeNumber(),currentNodeNumber))
currentNodeNumber+=1
LeftNode.getNode().setChildReferenceNodeId([LeftNode_Child1.getNode().getNodeId(),LeftNode_Child2.getNode().getNodeId()])

LeftNode.insertLeft(LeftNode_Child1)
LeftNode.insertRight(LeftNode_Child2)

currentNodeNumber+=1
RightNode_Child1 = Tree(buildNode(2,genesisId,RightNode.getNode().getNodeId(),RightNode.getNode().getNodeNumber(),currentNodeNumber))
currentNodeNumber+=1
RightNode_Child2 = Tree(buildNode(3,genesisId,RightNode.getNode().getNodeId(),RightNode.getNode().getNodeNumber(),currentNodeNumber))
currentNodeNumber+=1
RightNode.getNode().setChildReferenceNodeId([RightNode_Child1.getNode().getNodeId(),RightNode_Child2.getNode().getNodeId()])

RightNode.insertLeft(RightNode_Child1)
RightNode.insertRight(RightNode_Child2)

_Tree.inorder()