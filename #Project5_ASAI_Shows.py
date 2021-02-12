
# shows
shows = {'Avengers':[12],
        'Divergent':[16],
        'Iron Man':[12],
        }

# print(type(shows))

# define seats
seats = 3


# loop
while True:
        # welcome
        print('Welcome To ASAI Shows Inc. ')

        # take input()
        choice = input('Enter The Name Of The Show, Which You Want To Watch; ').strip().title()
        
        # verify show
        if choice in shows:
                print('Yes, Show Available!\n')

                # ask for age
                age = int(input('Kindly Verify Your Age; '))

                # shows age limit
                show_age = shows[choice][0]

                # verify age
                if age >= show_age:
                        print('Age {}, Verified!\n'.format(age))

                        # update seats
                        seats = seats - 1
                        
                        # verify seats
                        if seats >= 0:
                                print('Yehh! Seats Available.')
                                print('{} Seats Left!\n'.format(seats))

                                # confirmation
                                username = input('Kindly Enter Your Name; ').strip().capitalize()
                                print('Congratulations! {} You Can Now Watch The Show_\n'.format(username))

                        # seats unavailable
                        else:
                                print('Sorry! Seats Unavailable.\n')

                # young error
                else:
                        print('You Are Too Young For This Show!\n')

        # show Unavailable
        else:
                print('Sorry Show Unavailable!\n')










