import pyautogui
import time

# To do
# Add input requests for users for inserting group ids
# Add more error handling.
approval = True
while approval is True:
    try:

        groups = []
        num_groups = int(input("Enter the number of groups you want to post in: "))
        for index in range(num_groups):
            while True:
                try:
                    group_id = int(input("Enter the group id :  "))
                    groups.append(group_id)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid group id ")
        

        # Read the file
        dir = input("Please enter the txt file directory:")
        phone = input("Enter your Phone number or email: ")
        data = []
        with open(dir, 'r') as data_file:
            lines = data_file.readlines()

        header = lines[0].strip().split('\t')
        for line in lines[1:]:
            values = line.strip().split('\t')
            data.append(values)

        print(data)
        count = 0
        record = len(data)

        while count != record:  # while loop to go through all the records in the list.
            for i in data:  # for loop to go through all the data in the list
                print("Starting...\nYou have 5 secs to redirect to your browser")
                time.sleep(7)
                
                # Open a new tab
                pyautogui.hotkey('ctrl', 't')
                
                for group_id in groups:
                    print(group_id)
                    link = f'https://facebook.com/groups/{group_id}'
                    pyautogui.typewrite(link)
                    pyautogui.press('enter')
                    print("Waiting for 5 seconds to load the page\n")
                    time.sleep(5)
                    
                    # Type 'p' to start writing the post
                    pyautogui.typewrite('p')
                    time.sleep(2)
                    print("Writing post\n")
                    
                    # Floor
                    # Location
                    # Type
                    # Finishing
                    # Bedrooms
                    # Phase                 
                    # BUA
    
                
                    pyautogui.typewrite(f"Floor: {i[0]}")
                    pyautogui.press('enter')
                    pyautogui.typewrite(f"Location: {i[1]}")
                    pyautogui.press('enter')
                    pyautogui.typewrite(f"Type: {i[2]}")
                    pyautogui.press('enter')
                    pyautogui.typewrite(f"Finishing: {i[3]}")
                    pyautogui.press('enter')
                    pyautogui.typewrite(f"Bedrooms: {i[4]}")
                    pyautogui.press('enter')
                    pyautogui.typewrite(f"Phase: {i[5]}")
                    pyautogui.press('enter')
                    pyautogui.typewrite(f"BUA: {i[6]}")
                    pyautogui.press('enter')
                    pyautogui.typewrite(f'For details contact: {phone}')
                    print("Waiting for User to insert any images or make any changes (You have 1 min )....\n")
                    time.sleep(60)
                    
                    for _ in range(8):
                        pyautogui.press('tab')
                        time.sleep(0.5)
                    
                    # Press Enter to click the "Post" button
                    pyautogui.press('enter')

                    print("Posted!!")

                    print("Taking a break please dont leave the page")
                    time.sleep(30)
                    
                    # Move to the address bar and enter the next URL
                    pyautogui.hotkey('ctrl', 'l')
                    time.sleep(1)
                
            count += 1
        approve = input("Do you wish to continue (yes/no):")
        if approve == "no":
            approval = False

    except Exception as e:
        print(f"An error occurred : {e}\n","Please Try Restarting the application\nif the error still exists please contact us")