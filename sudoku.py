from copy import deepcopy as dc

class Sudoku():
	def __init__(self, game):
		if type(game) == list:
			self.game = game
		else:
			raise ValueError("use list")
	
	def solve(self):
		sols = []
		
		def recr(oldtmp):
			tmp = dc(oldtmp)
			sw = False
			for i in range(len(tmp)):
				if None in tmp[i]:
					sw = True
					unusedhor = [x for x in range(1, 10) if x not in tmp[i]]
					for j in range(len(tmp[i])):
						if tmp[i][j] is None:
							vert = getVert(tmp, j)
							unusedvert = [x for x in range(1, 10) if x not in vert]
							grp = getGroup(tmp, i, j)
							unusedgrp = [x for x in range(1, 10) if x not in grp]
							validsols = [x for x in unusedhor if x in unusedvert and x in unusedgrp]
							for k in validsols:
								tmp[i][j] = k
								recr(dc(tmp))
							break
					break
			if not sw:
				sols.append(tmp)
		
		recr(dc(self.game))
		return [Sudoku(x) for x in sols]

def getVert(game, wh):
	vert = []
	for i in game:
		vert.append(i[wh])
	return vert
	
def getGroup(game, whi, whj):
	grp = []
	for i in range(int(whi/3)*3, int(whi/3)*3+3):
		for j in game[i][int(whj/3)*3:int(whj/3)*3+3]:
			grp.append(j)
	return grp