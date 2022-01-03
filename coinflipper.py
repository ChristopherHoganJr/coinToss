import random

def coinflipper(coins, points=[0,0]):
    # If coins < 1 (0) return points - end game
    if coins < 1:
        print('Flipping coins has been completed')
        return points
    else:
        # Receive a random number between 0 and 1 inclusively
        coinside = random.randint(0, 1)
        # If the random number is 0, the outcome is heads
        if coinside == 0:
            points[0] += 1
        # Else the random number is 1, the outcome is tails
        else:
            points[1] += 1
        # Subtract 1 from the total coins
        coins -= 1
        # Call the function again to continue flipping the rest of the coins
        coinflipper(coins, points)
        # return points with the recursive function, else will return 'none'
        return points