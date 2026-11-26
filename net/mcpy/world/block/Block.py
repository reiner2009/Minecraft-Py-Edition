class Block:
    def __init__(self, id):
        self.id = id
        self.pos = (0,0,0)
        self.state_id=""
        self.block_state = {"":"", "all":[""]}
    def __eq__(self, other):
        return self.id==other.id
    def __hash__(self):
        return hash(self.id)
    def create(self, x, y, z):
        block = self.__class__.__new__(self.__class__)
        block.__init__(self.id)
        block.pos = (x, y, z)
        block.state_id = self.state_id
        block.block_state = self.block_state
        return block
    def getState(self):
        return self.block_state[self.state_id]
    def getBlockState(self):
        return self.block_state
    def getStates(self):
        return self.block_state["all"]