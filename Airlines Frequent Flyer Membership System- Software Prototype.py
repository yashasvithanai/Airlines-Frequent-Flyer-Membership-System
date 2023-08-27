# Problem: Python Airlines Rewards System
# Goal: To determine user rewards based on user input


# Part A

# Display a welcome message
print("Welcome to the Python Airlines Prototype Membership System")
print("")



# Part B

# Ask the user to input their annual and lifetime metrics

## First Name
firstName = input("What is your first name?")

## Annual Miles
annualMiles = input("How many miles have you flown this year?")

## Annual Segments
annualSegments = input("How many segments have you flown this year?")

## Annual Dollars
annualDollars = input("How much money have you spent this year (USD)?")

## Lifetime Miles
lifetimeMiles = input("How many lifetime miles have you flown?")


# Ask the user if there next flight is to (or through) Chicago airport
loungeCheck = input("Is your next flight to (or through) the Chicago airport?")

## if the input is not: "YES", "yes", "Yes", "Y", "y", then assume "No"

## Create a list of valid answers 
validAnswers = ["YES", "yes", "Yes", "Y", "y"]

## Create a loop to identify if the answer is Yes or No
temp = int()

for i in range(len(validAnswers)): # for all list items
    if loungeCheck == validAnswers[i]: #check if the input falls in list
        temp = temp + 1 # if input falls in list, temp variable takes the value 1
    else:
            temp = temp + 0 # else it takes 0
    
## assigning user's answer as a logical value where,  yes takes 1 and no takes 0
loungeCheck = temp 
### print(loungeCheck) (testing)

## Ask the user the coach class ticket price for the next flight
ticketPrice = input("How much will a Coach Class ticket for your next flight cost (USD)?")

    
# Print a blank line
print("")




# PART C

# Converting inputs to the appropriate data type and reassign to original variables
firstName = str(firstName) ## first name as string
annualMiles = int(annualMiles) ## annual miles as integer
annualSegments = int(annualSegments) ## annual segments as integer
annualDollars = float(annualDollars) ## annual dollars as decimal
lifetimeMiles = int(lifetimeMiles) ## lifetime miles as integer
ticketPrice = float(ticketPrice) ## ticket price as float to account for cents
loungeCheck = bool(loungeCheck) ## lounge check as a boolean for 'yes' or 'no' 



# PART D

# Determine user's annual membership tier and lifetime membership tier

## Determining the annual membership tier 
annualMembershipTierMiles = int()
## Determing annual membership tier according to annual miles
if (annualMiles >= 100000):
    annualMembershipTierMiles = 4
elif (annualMiles < 100000 and annualMiles >=75000):
    annualMembershipTierMiles = 3
elif (annualMiles < 75000 and annualMiles >=50000):
    annualMembershipTierMiles = 2
elif (annualMiles < 50000 and annualMiles >=25000):
    annualMembershipTierMiles = 1
else:
    annualMembershipTierMiles = 0

## Determining the annual membership tier according to segments and annual dollars metrics
annualMembershipTierSegments = int()

if (annualSegments >= 120):
    if annualDollars >= 24000:
        annualMembershipTierSegments = 4
elif (annualSegments < 120 and annualSegments >= 90):
    if (annualDollars >= 15000 and annualDollars < 24000):
        annualMembershipTierSegments = 3
elif (annualSegments < 90 and annualSegments >= 60):
    if (annualDollars>= 7000 and annualDollars < 15000):
        annualMembershipTierSegments = 2
elif (annualSegments < 60 and annualSegments >= 30):
    if (annualDollars >= 3000 and annualDollars < 7000):
        annualMembershipTierSegments = 1
else:
    annualMembershipTierSegments = 0

### Testing values: print(annualMembershipTierMiles)
### Testing values: print(annualMembershipTierSegments)

# Determing the annual membership tier
annualMembershipTier = int()

if annualMembershipTierMiles >= annualMembershipTierSegments:
    annualMembershipTier = annualMembershipTierMiles
else:
    annualMembershipTier = annualMembershipTierSegments

### Testing values: print(annualMembershipTier)

## Determining the lifetime membership tier using lifetime miles metrics

lifetimeMembership = int()

if (lifetimeMiles >= 3000000):
    lifetimeMembershipTier = 4
elif (lifetimeMiles < 3000000 and lifetimeMiles >=2000000):
    lifetimeMembershipTier = 3
elif (lifetimeMiles < 2000000 and lifetimeMiles >=1000000):
    lifetimeMembershipTier = 2
else:
    lifetimeMembershipTier = 0

### Testing values: print(lifetimeMembershipTier)



# PART E

# Determine the highest membership tier available
membershipTier = ()

if annualMembershipTier >= lifetimeMembershipTier:
    membershipTier = annualMembershipTier
else:
    membershipTier = lifetimeMembershipTier


# Defining Tier levels
tierLevels = [ "No Tier", "Sapphire", "Emerald", "Ruby", "Diamond"]

annualMembershipTierLevel = tierLevels[annualMembershipTier]
lifetimeMembershipTierLevel = tierLevels[lifetimeMembershipTier]

   
# Based on user's tier, correctly determine user's rewards

# Creating Rewards list starting from no rewards (tier 0) to highest tier(4) 
tierRewardsBags = [0, 0, 1, 2, 3]
tierRewardsUpgrades = ["No Upgrade", "Business Class", "Business Class", "First Class", "First Class"]
tierRewardsLounge = [0, 0, 0, 0, 1]
tierRewardsDiscount = [0, 15, 20, 25, 30]

# Determing rewards unlocked by the user
rewardsUnlockedBags = tierRewardsBags[membershipTier] ## Bags
rewardsUnlockedUpgrades = tierRewardsUpgrades[membershipTier] ## Seat Upgrades
rewardsUnlockedLounge = tierRewardsUpgrades[membershipTier] ## Lounge Access
rewardsUnlockedDiscount = tierRewardsDiscount[membershipTier] ## Discount Offered

### Testing Values: print(rewardsUnlockedBags)



# PART F
inputSummary = print("{}, this year, you have flown {} flights for {:,} miles and spent ${:,.2f} USD with Python Airlines. Lifetime, you have flown {:,} miles.".format(firstName,annualSegments,annualMiles, annualDollars, lifetimeMiles))
print("")



# PART G

if annualMembershipTierLevel == "No Tier" and lifetimeMembershipTierLevel == "No Tier":
    print("You are on your way to achieving annual frequent-flier status with Python Airlines!")
elif lifetimeMembershipTierLevel != "No Tier" and annualMembershipTierLevel == "No Tier":
    print("You have achieved lifetime frequent-flier status at the {} level!".format(lifetimeMembershipTierLevel))
elif lifetimeMembershipTierLevel == "No Tier" and annualMembershipTierLevel != "No Tier":
    print( "This year, you have also achieved annual frequent-flier status at the {} level!".format(annualMembershipTierLevel))
else:
    print("You have achieved lifetime frequent-flier status at the {} level!".format(lifetimeMembershipTierLevel))
    print( "This year, you have also achieved annual frequent-flier status at the {} level!".format(annualMembershipTierLevel))

print("")

# PART H

if membershipTier == 0:
    print("")
elif membershipTier ==1:
    print("You have unlocked the following rewards:")
    print("- Free seat upgrades to {}".format(rewardsUnlockedUpgrades))
    print("- You upcoming flight of ${:,.2f} USD was reduced by {} to ${:,.2f} USD.".format(ticketPrice, rewardsUnlockedDiscount, ((100-rewardsUnlockedDiscount)*ticketPrice)/100)) 
elif membershipTier ==2 or membershipTier == 3:
    print("You have unlocked the following rewards:")
    print("- {} free checked bags per flight".format(rewardsUnlockedBags))
    print("- Free seat upgrades to {}".format(rewardsUnlockedUpgrades))
    print("- You upcoming flight of ${:,.2f} USD was reduced by {} to ${:,.2f} USD.".format(ticketPrice, rewardsUnlockedDiscount, ((100-rewardsUnlockedDiscount)*ticketPrice)/100))
else:
    print("You have unlocked the following rewards:")
    print("- {} free checked bags per flight".format(rewardsUnlockedBags))
    print("- Free seat upgrades to {}".format(rewardsUnlockedUpgrades))
    print("- Your upcoming flight of ${:,.2f} USD was reduced by {}% to ${:,.2f} USD.".format(ticketPrice, rewardsUnlockedDiscount, ((100-rewardsUnlockedDiscount)*ticketPrice)/100))
    if loungeCheck == 0:
        print("- Free access to the club lounge next time flying to/through in Chicago")
    else:
        print(" - Enjoy free access to the club lounge in Chicago on your next/upcoming flight!")










































