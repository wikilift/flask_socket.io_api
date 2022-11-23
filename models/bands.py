from .band_model import Band
class Bands:
    def __init__(self):
        self.__bands=[]
    def addBand(self,band=Band()):
        self.__bands.append(band)
    def getBands(self):
        return self.__bands
    def deleteBand(self,id):
        self.__bands=[x for x in self.__bands if x.id != id]
        return self.__bands
        # for i,o in enumerate(self.bands):
        #     if o.id == id:
        #         del self.bands[i]
        #         break
    def voteBand(self,id):
        for x in self.__bands:
            if x.id==id:
                x.votes+=1
    def addBand(self,band):
        self.__bands.append(band)
            
    
     
        
# b=Bands()
# b.addBand(Band('paco',votes=0))
# b.addBand(Band('yes',votes=0))
# b.addBand(Band('si',votes=0))
# b.addBand(Band('no',votes=0))
# #print([x.name for x in b.getBands()])
# print([x.votes for x in b.getBands()])
# #b.deleteBand(b.getBands()[0].id)
# print(b.getBands()[0].id)
# b.voteBand(b.getBands()[0].id)
# b.voteBand(b.getBands()[0].id)
# b.voteBand(b.getBands()[0].id)
# b.voteBand(b.getBands()[0].id)
# b.voteBand(b.getBands()[0].id)
# b.voteBand(b.getBands()[0].id)
# print([x.votes for x in b.getBands()])

# import json
# k=[json.dumps(x.__dict__) for x in b.getBands()]
# print(k)
# #print([x.id for x in b.getBands()])
# #print([x.votes for x in b.getBands()])
# #print([x.name for x in b.getBands()])