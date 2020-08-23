def check(x, y, val, sudoku):
	for i in range(9):
		if(sudoku[x][i] == val or sudoku[i][y]==val):
			return False

	x = (x//3)*3
	y = (y//3)*3

	for i in range(3):
		for j in range(3):
			if(sudoku[x+i][y+j]==val):
				return False

	return True


def solve(sudoku):
	for i in range(9):
		for j in range(9):
			if(sudoku[i][j]==0):
				for k in range(1,10):
					if(check(i,j,k,sudoku)==True):
						sudoku[i][j] = k
						solve(sudoku)
						sudoku[i][j] = 0
				return 			
	printGrid(sudoku)

def printGrid(sudoku):
	for i in range(9):
		for j in range(9):
			if j == 8:
				print("|" + str(sudoku[i][j]), end = "|\n")
			else:
				print("|" + str(sudoku[i][j]), end = "")
