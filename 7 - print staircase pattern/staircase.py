# Staircase
#This is a staircase of size : n = 4

   #
  ##
 ###
####


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
            for j in range(n):
                print(('#' if j >= n-1-i else ' ') , end="")
            print()
