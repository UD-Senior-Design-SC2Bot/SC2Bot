class SolutionCache:
    def __init__(self, starting_pos):
        self.start = starting_pos
        self.moves = []
    
    def add_move(self, move):
        self.moves.append(move)
    
    def write_to_file(self, filename):
        f = open(filename, "w")
        f.write("Start: " + str(self.start) + "\n")
        f.write("Moves:\n")
        
        for move in moves:
            f.write(move)
    
    def read_file_into_cache(filename):
        # TODO
        pass
