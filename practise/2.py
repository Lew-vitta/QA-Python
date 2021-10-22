devs_money = 11
dev_can_play_smash = True

if devs_money > 10 and dev_can_play_smash:
    print("Dev enters a smash tournament!")

elif devs_money <= 10 and dev_can_play_smash:
    print("Dev is too poor to enter")

else:
    print("Dev just can't play smash")