import time
import random
from datetime import datetime
import math
import re

# ==================================== Storage =================================
# 
#
# 
#
#
# Lists of horoscope messages for love life, career, and money

lovelife_list = [
    "Go on a romantic date once a month if you have a partner",
    "Communicate more openly and honestly with your partner",
    "Love has always been in your heart, just need to look for the right person to unlock it",
    "Learn to resolve conflicts peacefully",
    "Prioritize self-love, self-care and set boundaries",
    "Is your partner toxic?",
    "Your family is everything, please love them",
    "Your parents\' time is limited, spend your time with them",
    "Show some gratitute towards your love ones, they secretly love it!",
    "Give love to received love!"

]

career_list = [
    "Pursue what you've been putting off!",
    "Set clear career goals for the next five years",
    "Improve time management and productivity at work or school!",
    "Work harder and GET that PROMOTION!",
    "If you're not happy with your job, find a new one.",
    "How is your current job?",
    "Not everyone could become who you\'ve become now",
    "Leave your job if you don\'t like it!",
    "Staying in a toxic environment is not good for your mental health..."
]

money_list = [
    "Create a monthly budget and stick to it",
    "Start saving for an emergency fund, travel and families",
    "Find a good place to invest your money now",
    "Stop buying luxury items to keep up with the trends",
    "Explore additional income sources (side hustles, investments...)",
    "Spend money on Holiday, Trips with Family and Friends!",
    "Spend money on Experience not luxury",
    "It\'s time you write down your daily expenses"
]
# Loading Function
def loading():
    for i in range(0,3):
        guide5 = "..."
        print(guide5)
        time.sleep(2)
# ==================================== End of Storage ===================================

class zodiac_reading:
    welcome = print('''     ================================================= ***** ================================================
                                Welcome to Daily Uplifting life Quotes to improve your Life! \n
    We're going to predict your Zodiac sign & collect the message from the stars to send you a special message!
        ''')
    time.sleep(4)
    print("But first, let's find your Zodiac Sign amongst the stars")
    print("(^-^)")
    time.sleep(1)
    print("...")
    time.sleep(4)
    print("..")
    time.sleep(8)
    print(".")
    time.sleep(2)

    def is_valid_date(date_str):
        try:
            datetime.strptime(date_str, '%d-%m-%Y')
            return True
        except ValueError:
            return False

    while True:
        print("------------------------")
        date_input = input("Enter your birthday in (DD-MM-YYYY) : ")
        if is_valid_date(date_input):
            break

    # Step 2 - Guess the Zodiac Sign
    def get_zodiac_sign(day, month):
        zodiac_signs = [
            ("Aquarius", (1, 20), (2, 18)),
            ("Pisces", (2, 19), (3, 20)),
            ("Aries", (3, 21), (4, 19)),
            ("Taurus", (4, 20), (5, 20)),
            ("Gemini", (5, 21), (6, 20)),
            ("Cancer", (6, 21), (7, 22)),
            ("Leo", (7, 23), (8, 22)),
            ("Virgo", (8, 23), (9, 22)),
            ("Libra", (9, 23), (10, 22)),
            ("Scorpio", (10, 23), (11, 21)),
            ("Sagittarius", (11, 22), (12, 21)),
            ("Capricorn",  (12, 22),(1, 19) )
        ]

        for sign, (start_month, start_day), (end_month, end_day) in zodiac_signs:
            if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
                return sign

        return "Invalid Date"  # Return this if the date does not match any sign


    print("Calculating to find your Zodiac Sign...")

    day, month, year = map(int, date_input.split('-'))
    zodiac_sign = get_zodiac_sign(day, month)

    loading()
    print(f"Your zodiac sign is: {zodiac_sign}")
    print("------------------------")
    time.sleep(2)
    time.sleep(2)
    # Step 3 - Generate random numbers and compare it to birthday --> Give an uplifting message

    print("Now, let's generate your lucky 6 digits number")
    time.sleep(3)

            # Number generating
    random_number = ""
    digits = [i for i in range(0,10)]
    for i in range(6):
        index = math.floor(random.random() * 10)
        random_number += str(digits[index])
    loading()
    print("This is your lucky number: " + str(random_number))
            
            # Turning it into its own single digit
    list1 = [int(random_number) for random_number in str(random_number)]
    time.sleep(3)
    print("Display as separated digits: " + str(list1))
    time.sleep(3)

            # Turning Birthday into a list
    birthday = ""
    bday = day, month, year
    birthday = bday
    list2 = list(birthday)
    time.sleep(3)
    print("Your birthday:", list2)
    print("------------------------")
    time.sleep(3)

            # Sum 2 lists into 2 individual numbers
    print("Now, let's compare " + str(list1) + " & " + str(list2) +" to see what you need to do to improve your life")
    time.sleep(10)
    list3 = sum(list1 * 100)
    print("Your total lucky number combined = " , list3)
    time.sleep(5)
    list4 = sum(list2)
    print("Your birthday numbers combined = ", list4)
    print("------------------------")

    if (list3 != list4):
        print("It seems like the star does not align perfectly tonight...")
        time.sleep(10)
        print("Your numbers are not a match! ", "'", list3, "'" , " != " , list4)
        time.sleep(10)
        print("Nevertheless, the message is still received!")
        time.sleep(5)
        print("------------------------")
        print("1 - Start improving your love life today: " + random.choice(lovelife_list))
        time.sleep(10)
        print("2 - Improving your career: " + random.choice(career_list))
        time.sleep(10)
        print("3 - You could earn more: " + random.choice(money_list))
        time.sleep(5)
        print("The End! Please come again! That will be $50 :D")
        time.sleep(5)
    else: 
        print("Your birthday and Your lucky numbers are the same???")
        time.sleep(10)
        print("Congrats! There's not quotes for you")


#
# This is the end of our Mini-Horocope, We'd love to received any feedback you may have
#                       Python Instructor: Professor Oum Saokosal
#                             Project Lead: Hav MengHeng
#                 Members: Un Veasna, Seang Sopanha & Chhun Chhaylay
#             We're from NPIC - Computer Science (Group B), Generation 16 
#                              Thank you for using

user = zodiac_reading()

