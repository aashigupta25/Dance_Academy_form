'''Registration form'''
import datetime as dt
from datetime import datetime
from dateutil.relativedelta import relativedelta
import random
import string
import json

while True:
    welcome_Msg = '''
    ==== Welcome to Our Dance Academy ====
    please choose an option:
    1. press 1 for New Registration
    2. press 2 for Show Entries
    3. press 3 for Show Specific detail of user
    4. press 4 to show filter entries
    5. press 5 to exit
    '''
    print(welcome_Msg)
    a = input("Enter the Choice")
    if a == '1':
        for j in range(0, 1):
            userinfo_list = []

            while True:
                user_name = input("Enter the Learner Name: ")
                user_name.isalpha() == True
                user_namee = user_name.replace(" ","")
                if user_namee.isalpha():
                    print("Hello", user_name)
                    break
                else:
                    print("\nPlease enter the correct detail, please try again.\n")

            '''Valid Date
            Date should be today or after the today's date'''
            def valid_date(user_date_of_joining):
                while True:
                    try:
                        dt.datetime.strptime(user_date_of_joining, '%Y/%m/%d')
                        break
                    except ValueError:
                        print("\nSorry!")
                        print("Please! Enter the date in Format, YYYY/MM/DD")
                        valid_date = input("Enter the Joining Date in format, YYYY/MM/DD:")
                        user_date_of_joining = valid_date
                        break
                return user_date_of_joining
            valid_date = input("Enter the date Joining Date, YYYY/MM/DD:")
            user_date_of_joining = valid_date
            print("The date you entered is:", user_date_of_joining)

            # upper case or lowercase alphabets
            while True:
                user_fresher_experience = input("Are you Fresher or Experienced?")
                if user_fresher_experience == "fresher" or user_fresher_experience == "Fresher":
                    print(user_name.capitalize() + " " + "is Fresher")
                    break
                elif user_fresher_experience == "Experienced" or user_fresher_experience == "Experienced":
                    print(user_name.capitalize() +" "+ "is Experienced")
                    while True:
                        user_experience_month = input("Please enter the number of months of experience! ")
                        if user_experience_month.isnumeric() == True:
                            print("You have great Experience!!")
                            userinfo_list.insert(3, user_experience_month)
                            break
                        else:
                            print("\nPlease enter the correct detail!\n")
                            print("The enter detail should be in no. of months, please try again.")
                    break
                else:
                    print("please write the Fresher or Experienced Accordingly")

            # Valid Duration time
            # float Issue

            while True:
                user_duration = input("Enter the Duration of Learning that you want (in months): ")
                user_duration.isdigit() == True
                if user_duration.isdigit():
                    print("You want to join for", user_duration, "month. Great!!")
                    break
                else:
                    print("\nPlease enter the correct detail!\n")
                    print("The enter detail should be in months, please try again.")

            # uppercase or lowercase
            while True:
                user_dance_type = input("Enter the Type of Dance which you want: ")
                if user_dance_type == "Khatak":
                    print("You want to learn the Dance form", user_dance_type.capitalize())
                    break
                elif user_dance_type == "Hiphop":
                    print("You want to learn the Dance form", user_dance_type.capitalize())
                    break
                elif user_dance_type == "Western":
                    print("You want to learn the Dance form", user_dance_type.capitalize())
                    break
                elif user_dance_type == "Bharatnatyam":
                    print("You want to learn the Dance form", user_dance_type.capitalize())
                    break
                elif user_dance_type == "Kucipudi":
                    print("You want to learn the Dance form", user_dance_type.capitalize())
                    break
                elif user_dance_type == "Freestyle":
                    print("You want to learn the Dance form", user_dance_type.capitalize())
                    break
                elif user_dance_type == "Salsa":
                    print("You want to learn the Dance form", user_dance_type.capitalize())
                    break
                elif user_dance_type == "RajasthaniFolk":
                    print("You want to learn the Dance form", user_dance_type.capitalize())
                    break
                else:
                    print("Our Acedmy teaches the dance forms :")
                    print("\nKhatak \nHiphop \nWestern \nBharatnatyam ")
                    print("Kucipudi \nFreestyle \nSalsa \nRajasthaniFolk")
                    print("\nSorry, We don't have the dance form ", user_dance_type )
                    print("\nplease Enter the Dance Form from the list: ")

            # Generate Unique ID
            # ID should be in the form of 1, 2, 3, 4, 5, 6 and so on
            def ran_gen(size, chars=string.ascii_uppercase + string.digits):
                return ''.join(random.choice(chars) for x in range(size))
            user_id = ran_gen(8, "ABCD1234")
            print ("Your User ID is:" , user_id)

            userinfo_list.append(user_name.capitalize())
            userinfo_list.append(user_date_of_joining)
            userinfo_list.append(user_fresher_experience)
            userinfo_list.append(user_duration)
            userinfo_list.append(user_dance_type)
            ## ID should be 1, 2, 3, 4, 5,6, 7 and so on
            userinfo_list.append(user_id)

            print(userinfo_list)

        data_list = []
        user_data = {
                    user_id:
                        {
                        "Name": userinfo_list[0],
                        "DOJ": userinfo_list[1],
                        "fORe": userinfo_list[2],
                        "Duration":  userinfo_list[3],
                        "typeOfDance": userinfo_list[4],
                        "ID": userinfo_list[5]
                        }
        }

        data_list.append(user_data)

        with open("userdata_file.json", "r") as file:
            data = json.load(file)
            data.append(user_data)

        with open("userdata_file.json", "w") as file:
            json.dump(data, file, indent = 4)

        # data_list1 = json.dumps(data_list, indent=4)

        # with open("userdata_file.json", "w") as outfile:
        #     outfile.write(data_list1)

        # json_object = json.dumps(user_data, indent=4)

        # # Writing to sample.json
        # with open("userdata_file.json", "a") as outfile:
        #     outfile.write(json_object)
        #     outfile.write(",")


    elif a == '2':
        with open("userdata_file.json", "r") as file:
            data = json.load(file)
            # print(type(data))
            print(data)

    elif a == '3':
        user_given_id = input("Enter the user ID:")
        with open("userdata_file.json", "r") as file:
            data = json.load(file)

        for i in range(0, len(data)):
            if user_given_id == list(data[i].keys())[0]:
                print(data[i][user_given_id])
        else:
            print("Please enter the correct User ID!")

    elif a == '4':
        # filter entries
        while True:
            press_button = '''
            ==== Press Button ====
            please choose an option:
            1. Press 1 to see entries by dance type
            2. Press 2 to see Expired Entries
            3. Press 3 to see filter entries Durationwise
            4. Press 4 to see current entries
            5. Press 5 to get data by Name
            6. Press 6 to exit form filter menu
            '''
            print(press_button)
            b = input("Enter the Choice")

            if b == '1':
                with open("userdata_file.json", "r") as file:
                    data = json.load(file)

                user_display_typedance = input("Enter the type of Dance which you want to see the details!")

                for i in range(0, len(data)):
                    user_dict = data[i]

                    keyname = list(user_dict.keys())[0]
                    user_dance = user_dict[keyname]['typeOfDance']

                    if user_display_typedance == user_dance:
                        print(user_dict[keyname])
                else:
                    print("Please enter the Dance form!")

        # Press2 to see Expired Entries
            elif b == '2':
                with open("userdata_file.json", "r") as file:
                    data = json.load(file)
                for i in range(0, len(data)):
                    user_dict = data[i]

                    keyname = list(user_dict.keys())[0]
                    user_DOJ = user_dict[keyname]['DOJ']
                    user_expired_duration = user_dict[keyname]['Duration']
                    d1 = datetime.strptime(user_DOJ, "%Y/%m/%d")
                    future_date = d1 - relativedelta(months= int(user_expired_duration))
                    today = datetime.today()
                    if future_date > today:
                        print(user_dict[keyname])

            elif b == '3':
                # Press3 to see filter entries Durationwise
                with open("userdata_file.json", "r") as file:
                    data = json.load(file)

                user_input_duration = input("Enter the Duration of which you want to see the details!")

                for i in range(0, len(data)):
                    user_dict = data[i]

                    keyname = list(user_dict.keys())[0]
                    user_duration = user_dict[keyname]['Duration']

                    if user_input_duration == user_duration:
                        print(user_dict[keyname])
                else:
                    print("Sorry! here is no entries for this duration time!")

            # Press4 to see current entries
            # Current Enteries = Today's entries
            # Json files with date wise fill up the forms
            elif b == '4':
                with open("userdata_file.json", "r") as file:
                    data = json.load(file)
                for i in range(0, len(data)):
                    user_dict = data[i]

                    keyname = list(user_dict.keys())[0]
                    user_DOJ = user_dict[keyname]['DOJ']
                    user_current_duration = user_dict[keyname]['Duration']
                    d1 = datetime.strptime(user_DOJ, "%Y/%m/%d")
                    current_date = d1 - relativedelta(months= int(user_current_duration))
                    today = datetime.today()
                    if current_date < today:
                        print(user_dict[keyname])        

            # Press5 to get data by Name
            elif b == '5':
                with open("userdata_file.json", "r") as file:
                    data = json.load(file)

                user_input_name = input("Enter the name whose detail you want to see!")

                for i in range(0, len(data)):
                    user_dict = data[i]

                    keyname = list(user_dict.keys())[0]
                    user_data_name = user_dict[keyname]['Name']

                    if user_input_name == user_data_name:
                        print(user_dict[keyname])
                else:
                    print("Please enter the Correct Name!")

            elif b =='6':
                print("Now you get exit form filter menu!")
                exit()

            else:
                print("Invalid Choice! please check the menu")

    elif a == '5':
        print("Thanks for Visiting!")
        exit()

    else:
        print("Invalid Choice! please check the menu")
