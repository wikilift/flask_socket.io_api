class Band:
      def __init__(self, name='',votes=0,id=''):
        import uuid
        if id:
          self.id = id
        else:
            self.id = str(uuid.uuid4())
        self.name = name
        self.votes=votes
      
      def fromMap(map):
          import json
          data=json.loads(map)
          return Band(name=data['name'],votes=data['votes'],id=data['id'])
          
          
