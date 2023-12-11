#
# Generates a file with a list of integers for a bit-flag representation of noughts and crosses win positions
#

from enum import IntFlag

class Grid(IntFlag):
    M11 = 1
    M12 = 2
    M13 = 4
    M21 = 8
    M22 = 16
    M23 = 32
    M31 = 64
    M32 = 128
    M33 = 256

winning_positions = []

# Horizontal Wins
winning_positions.append( Grid.M11 | Grid.M12 | Grid.M13 )
winning_positions.append( Grid.M21 | Grid.M22 | Grid.M23 )
winning_positions.append( Grid.M31 | Grid.M32 | Grid.M13 )

# Vertical Wins
winning_positions.append( Grid.M11 | Grid.M21 | Grid.M31 )
winning_positions.append( Grid.M12 | Grid.M22 | Grid.M32 )
winning_positions.append( Grid.M13 | Grid.M23 | Grid.M33 )

# Diagonal Wins
winning_positions.append( Grid.M11 | Grid.M22 | Grid.M33)
winning_positions.append( Grid.M31 | Grid.M22 | Grid.M13)

outfile = open("wins.txt", "w")

strings = [str(grid.value) for grid in winning_positions]

outfile.writelines("\n".join(strings))
outfile.close()