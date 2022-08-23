class NEODatabase:

    def __init__(self, neos, approaches):

        self._neos = neos   # A collection of `NearEarthObject`s
        self._approaches = approaches  # A collection of `CloseApproach`es.

        self.neoByName = {}
        self.neoByDes = {}

        for neo in self._neos:
            self.neoByName[neo.name] = neo  # name: class NearEarthObject
            self.neoByDes[neo.designation] = neo  # des : class NearEarthObject

        for approach in self._approaches:
            # connect NearEarthObject with CloseApproach
            approach.neo = self.neoByDes[approach._designation]
            approach.neo.approaches.append(approach)

    def get_neo_by_designation(self, designation):

        try:
            return self.neoByDes[designation]
        except:
            return None

    def get_neo_by_name(self, name):

        try:
            return self.neoByName[name]
        except:
            return None

    def query(self, filters=()):

        if filters:
            for approach in self._approaches:
                allTrue = all(fil(approach) for fil in filters)
                if allTrue:
                    yield approach
        else:
            for approach in self._approaches:
                yield approach
