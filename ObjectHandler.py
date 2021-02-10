# Description: This is the object handler file for the python game template
# Created By: Jacob Maughan

class ObjectHandler:
    _objects = []

    @classmethod
    def render(cls, screen):
        for tmpObject in cls._objects:
            tmpObject.render(screen)

    @classmethod
    def tick(cls, stateHandler):
        for tmpObject in cls._objects:
            tmpObject.tick(stateHandler)

    @classmethod
    def addObject(cls, newObject):
        cls._objects.append(newObject)

    @classmethod
    def removeObject(cls, objectToRemove):
        for i in range(len(cls._objects)):
            if cls._objects[i] == objectToRemove:
                print(cls._objects[i].ID)
                cls._objects.pop(i)

    @classmethod
    def clearObjects(cls):
        cls._objects = []

    @classmethod
    def getObjectByID(cls, objectID):
        for tmpObject in cls._objects:
            if tmpObject.ID == objectID:
                return tmpObject

    @classmethod
    def getObjects(cls):
        return cls._objects
