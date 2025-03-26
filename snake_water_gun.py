# Import the random module to let the computer make random choices
import random

# Get the user's choice (snake, water, or gun)
# We use lower() to handle uppercase inputs and strip() to remove extra spaces
user = input("Choose s (snake), w (water), or g (gun): ").lower().strip()

# Computer randomly selects one option from the list ['s', 'w', 'g']
comp = random.choice(['s', 'w', 'g'])

# Show what the computer chose (this helps make the game transparent)
print(f"Computer chose {comp}")

# Game logic starts here:

# 1. First check if it's a tie (both chose the same option)
if user == comp:
    print("It's a draw!")
    
# 2. Check all winning combinations:
#    - Snake(s) drinks Water(w)
#    - Water(w) drowns Gun(g)
#    - Gun(g) shoots Snake(s)
elif (user == 's' and comp == 'w') or (user == 'w' and comp == 'g') or (user == 'g' and comp == 's'):
    print("You win!")
    
# 3. If user entered a valid choice but didn't win (must have lost)
elif user in ['s', 'w', 'g']:
    print("You lose!")
    
# 4. Handle invalid inputs (when user enters something other than s/w/g)
else:
    print("Invalid input! Please choose only s, w, or g next time.")