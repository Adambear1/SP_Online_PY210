#!/usr/bin/env python3

import sys

donors = {'Alexander Pushkin' : [200, 100, 340],
          'Mikhail Lermontov' : [300, 100],
          'Leo Tolstoy' : [150, 250, 100],
          'Fyodor Dostoevsky' : [125],
          'Anton Chekhov' : [100, 250],
          'Nikolai Gogol' : [325, 150]
          }

def menu_options(): 
    print( "\n".join (("Please select from the following options:",
          "1 - Send a Thank You letter to a single donar.",
          "2 - Create a Report.",
          "3 - Send letters to all donors.",
          "4 - Quit",
          " >>> ")))
    prompt = input('')
    return prompt


def thank_you_message(donor):
    message = (f'\nDear {donor},'
               f'\n\nThank you for your generous donation of ${sum(donors.get(donor)):,.2f}.' 
               '\nWe value your contribution and support.' 
               '\n\nSincerely,\n\nNew Horizon Charity Director\n')   
    return message

                                      
def send_thank_you():
    mail_to = input ("Enter the full name of a donor or 'list' for current donors ")
    while mail_to.lower() == "list":
        for name in donors:
            print(name)
        mail_to = input ("Please enter a  full name of a donor ")        
    amount = float(input ("Enter the donation amount "))
    if mail_to not in donors:
        donors[mail_to] = [amount]
    else: 
        donors[mail_to] += [amount]
    print(thank_you_message(mail_to))


def summation(arg):
    return sum(donors.get(arg))


def create_report():
    header ='\n{:<20}|{:^15}|{:^15}|{:>15}'.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print("Donation Report")
    print(header)
    print('-'*len(header))
    donors_sorted = sorted(donors, key = summation, reverse = True)
    for donor in donors_sorted:
        total = sum(donors.get(donor))
        num = len(donors.get(donor))
        avg = total/num
        print('{:<20} ${:>14,.2f}{:>14}  ${:>16,.2f}'.format(donor,total,num,avg))
    print('')    
    
    
def send_letters_to_all():
    for donor in donors:
        #print(entry)
        filename = donor + '.txt'
        with open(filename, 'w') as f:
            f.write(thank_you_message(donor))

            
def quit_now():
    print("Good bye and see you next time!")
    sys.exit()       

    
def main():
    options_dict = {1: send_thank_you, 2: create_report, 3: send_letters_to_all, 4: quit_now }
    while True:
        option = int(menu_options())
        if option not in options_dict:
            print("Not a valid option. Please select one of the available options!")
        else: 
           options_dict.get(option)()

if __name__ == "__main__":
    main()  