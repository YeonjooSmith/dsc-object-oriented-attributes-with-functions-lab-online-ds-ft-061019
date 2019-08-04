class School:
    def __init__(self, name = None, roster ={}):
        self.name = name
        self.roster = roster
    def add_student(self,st_name, st_gradelevel):
        if str(st_gradelevel) in self.roster.keys():
            self.roster[str(st_gradelevel)].append(st_name)
        else:
            self.roster[str(st_gradelevel)] = [st_name]
        #rosterself[str(st_gradelevel)]= roster.get(str(st_gradelevel),[]).append(st_name)
    def grade(self, st_gradelevel):
        return(self.roster.get(str(st_gradelevel),[]))
    def sort_roster(self):
        for grade in self.roster.keys():
            self.roster[grade].sort()