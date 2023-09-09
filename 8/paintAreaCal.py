import math
def can_required(height, width):
    # 1 can cover 5 square m 
    can = math.ceil((height*width)/5)
    print(f"You need to buy {can} can of paints")

can_required(int(input("Input the wall height in m")), int(input("Input the wall width in m")))