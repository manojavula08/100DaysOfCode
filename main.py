def find_highest_bider(bider_list):
    highest_bidder = 0
    bidder_name = ''
    for user in bider_list:
        current_bidder = bider_list[user]
        if current_bidder > highest_bidder:
            highest_bidder = current_bidder
            bidder_name = user

    print(f"the highest bidder is '{bidder_name}' and value is ${highest_bidder}")


biding = True
biding_list = {}
while biding:
    user_name = input("enter you name: ")
    user_bid = int(input("enter you bid: "))
    biding_list[user_name] = user_bid

    if input("do you want to continue type 'y' or 'n': ").lower() == 'n':
        biding = False
        # clear the screen else
        find_highest_bider(biding_list)



