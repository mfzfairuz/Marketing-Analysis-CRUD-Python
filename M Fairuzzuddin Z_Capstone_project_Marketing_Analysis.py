#Display Main Menu
from tabulate import tabulate

def display_main_menu():
    """Function to Present Menu Option in Main Menu

    Returns:
        _type_: _description_
    """
    title = "===== Marketing Data Analysis Program ====="
    width = 100
    centered_title = title.center(width)
    print(centered_title)
    print("\nThis program use for marketing team to gather the data and calculate descriptive statistic in simple.\nUser could compare every metrics that perform through the campaign ads")
    print("\nThe metrics that we used are ad views, ad click, ad conversion, conversion value, cost per conversion \n")

    print("List Menu:")
    print("1. Menampilkan Data Report Marketing Campaign")
    print("2. Menambah Data Report Marketing Campaign")
    print("3. Mengupdate Data Report Marketing Campaign")
    print("4. Mencari Data Report Marketing Campaign")
    print("5. Menghapus Data Report Marketing Campaign")
    print("6. Menghitung KPI Marketing Campaign")
    print("7. Exit Program")

def create_campaign():
    """
    Prompts the user for campaign data and returns a dictionary.
    Data to Input: amount spent, reach, total click, lp view, total conversion, conv value
    """
    global campaign_data 

    # Get input for the number of campaigns from the user
    while True:  
        try:
            num_entries = int(input("Enter the number of campaigns you want to create: "))
            if num_entries > 0:
                break
            else:
                print("Please enter a positive number of campaigns.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    for i in range(num_entries):
        print(f"\nData Campaign {i + 1}:\n")
        while True:
            try:
                adset_id = input("Enter ad set ID (Target Audience): ")
                amount_spent = int(input("Enter amount spent: "))
                reach = int(input("Enter reach: "))
                total_click = float(input("Enter Total Click (all): "))
                landing_page_views = int(input("Enter landing page views: "))
                total_conversions = int(input("Enter total conversions: "))
                conversion_value = float(input("Enter conversion value: "))
                break  # Exit the inner loop if input is valid
            except ValueError:
                print("Input tidak valid, Harap masukkan data yang tepat dan benar")
        
        # Create the dictionary from the data entry
        new_campaign = {
            "adset_id": adset_id,
            "amount_spent": amount_spent,
            "reach": reach,
            "total_click": total_click,
            "landing_page_views": landing_page_views,
            "total_conversions": total_conversions,
            "conversion_value": conversion_value
        }
        campaign_data.append(new_campaign)
        
    print("\nAll Campaign Data:")
    
    from tabulate import tabulate
    # Data to display in the table
    table_data = []
    for campaign in campaign_data:
        table_data.append([
            campaign["adset_id"],
            campaign["amount_spent"],
            campaign["reach"],
            campaign["total_click"],
            campaign["landing_page_views"],
            campaign["total_conversions"],
            campaign["conversion_value"]])
    # Define headers for the table
    headers = ["AdSet ID", "Amount Spent", "Reach", "All Clicks", "Landing Page Views", "Conversions", "Value"]
    # Print the table using tabulate
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

    return campaign_data

def read_campaign(campaign_data):
    """Displays all campaign data in a tabular format."""
    if len(campaign_data)==0:
        input_no_campaign = input("There is no campaign data yet, You need to add your campaign data first, Types Yes/No = ")
        if input_no_campaign.lower() == "yes":
            create_campaign()

    else:
        print("\nData Report Marketing Campaign:")

        # Prepare table data
        table_data = []
        for campaign in campaign_data:
            # Append data to table_data
            table_data.append([
                campaign["adset_id"],
                campaign["amount_spent"],
                campaign["reach"],
                campaign["total_click"],
                campaign["landing_page_views"],
                campaign["total_conversions"],
                campaign["conversion_value"]
            ])

        # Define headers
        headers = ["Ad Set ID", "Amount Spent", "Reach", "Total Clicks", 
                "Landing Page Views", "Conversions", "Value", "CTR", "CPC", "ROAS"]

        # Print the table using tabulate
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

def update_campaign(campaign_data):
    adset_id = input("Masukkan Ad Set ID yang ingin diupdate: ")
    for campaign in campaign_data:
        if campaign['adset_id'] == adset_id:
            try:
                while True:
                    print("\n1. Adset ID")
                    print("2. Amount Spent")
                    print("3. Reach")
                    print("4. Total Click")
                    print("5. Landing Page Views")
                    print("6. Conversions")
                    print("7. Conversion Value")
                    print("8. Selesai Update")
                    update_choice = int(input("Masukkan angka menu yang ingin diupdate: "))
                    
                    if update_choice == 1:
                        campaign['adset_id'] = input("Enter ad set ID (Target Audience): ")
                    elif update_choice == 2:
                        campaign['amount_spent'] = int(input("Input your Amount Spent: "))
                    elif update_choice == 3:
                        campaign['reach'] = int(input("Input new total reach: "))
                    elif update_choice == 4:
                        campaign['total_click'] = int(input("Input Total Click: "))
                    elif update_choice == 5:
                        campaign['landing_page_views'] = int(input("Input Total Landing Page View: "))
                    elif update_choice == 6:
                        campaign['total_conversions'] = int(input("Input Total Conversions: "))
                    elif update_choice == 7:
                        campaign['conversion_value'] = int(input("Input your Conversion Value: "))
                    elif update_choice == 8:
                        break
                    else:
                        print("Your Input is not valid.")
            except ValueError:
                print("Invalid Input. Please fill with Number.")

            print("Campaign data updated successfully!")
            return

    print(f"Campaign with Ad Set ID '{adset_id}' not found.")


def search_campaign(campaign_data):
    """Search campaign data by Ad Set ID."""
    adset_id = input("Enter Ad Set ID to search: ")
    found = False
    table_data = []
    for campaign in campaign_data:
        if campaign["adset_id"] == adset_id:
            table_data.append([
                campaign["adset_id"],
                campaign["amount_spent"],
                campaign["reach"],
                campaign["total_click"],
                campaign["landing_page_views"],
                campaign["total_conversions"],
                campaign["conversion_value"]])
            # Define headers for the table
            headers = ["AdSet ID", "Amount Spent", "Reach", "All Clicks", "Landing Page Views", "Conversions", "Value"]
            # Print the table using tabulate
            print(tabulate(table_data, headers=headers, tablefmt="grid"))

            found = True
            break
    if not found:
        print(f"Campaign with Ad Set ID '{adset_id}' not found.")


def delete_campaign(campaign_data):
    """Deletes a campaign by Ad Set ID."""
    adset_id = input("Enter Ad Set ID to delete: ")
    for i, campaign in enumerate(campaign_data):
        if campaign["adset_id"] == adset_id:
            del campaign_data[i]
            print(f"Campaign with Ad Set ID '{adset_id}' deleted successfully.")
            return  # Exit function after deletion
    print(f"Campaign with Ad Set ID '{adset_id}' not found.")

def kpi_campaign():
    """Displays all campaign data in a tabular format."""
    if len(campaign_data)==0:
        input_no_campaign = input("There is no campaign data yet, You need to add your campaign data first, Types Yes/No = ")
        if input_no_campaign.lower() == "yes":
            return create_campaign()

    print("\nData KPI Marketing Campaign:")

    table_data_kpi = []
    for campaign in campaign_data:
        # Calculate KPIs (if applicable)
        ctr = round((campaign["total_click"] / campaign["reach"]) * 100, 2)
        cpc = (round(campaign["amount_spent"] / campaign["total_click"], 2)
                if campaign["total_click"] != 0
                else 0)
        roas = (round(campaign["conversion_value"] / campaign["amount_spent"], 2)
                if campaign["amount_spent"] != 0
                else 0)
        conversion_rate = (round((campaign["total_conversions"] / campaign["landing_page_views"]) * 100,2,)
                if campaign["landing_page_views"] != 0
                else 0)
        
        # add the calculated values to the campaign dictionary
        campaign["ctr"] = ctr
        campaign["cpc"] = cpc
        campaign["roas"] = roas
        campaign["conversion_rate"] = conversion_rate

        # Determine Recommendation
        recommendation = ""
        if roas > 4 :
            if conversion_rate > 5 and ctr > 5:
                recommendation = "Your campaign is Great, Increase your budget"
            else:
                recommendation = "Good ROAS, but check conversion rate and CTR"
        elif roas < 4 and conversion_rate < 5:
            recommendation = "Check offer & bottom sales funnel"
        elif roas < 4 and ctr < 5:
            recommendation = "Check ad relevance to landing page"
        elif roas < 4 and cpc > 5000:
            recommendation = "Change ad creative & landing page"
        else:
            recommendation = "Analyze further to optimize"

        # Append data to table_data
        table_data_kpi.append([
            campaign["adset_id"],
            f"{ctr:.2f}%",
            f"{cpc:.2f}",
            f"{conversion_rate:.2f}",
            f"{roas:.2f}",
            recommendation
        ])
    
    # Define headers
    headers = ["Ad Set ID", "CTR", "CPC","Conversion Rate","ROAS","Recommendation"]

    # Print the table using tabulate
    print(tabulate(table_data_kpi, headers=headers, tablefmt="grid"))
    print("\n")

    while True:
        sort_by = input("Enter KPI to sort by (CTR, CPC, Conversion Rate, ROAS, or leave empty for no sorting): ")
        if sort_by.lower() in ["ctr", "cpc", "conversion rate", "roas", ""]:
            break
        else:
            print("Invalid KPI. Please choose from the list or leave empty.")
    ascending = input("Sort in ascending order? (yes/no, default is no): ").lower() == "yes"
    sorted_campaign_data = sort_campaign_data(campaign_data, sort_by, ascending)
    table_data_kpi = []
    for campaign in sorted_campaign_data:
        # Calculate KPIs (if applicable)
        ctr = round((campaign["total_click"] / campaign["reach"]) * 100, 2)
        cpc = (round(campaign["amount_spent"] / campaign["total_click"], 2)
                if campaign["total_click"] != 0
                else 0)
        roas = (round(campaign["conversion_value"] / campaign["amount_spent"], 2)
                if campaign["amount_spent"] != 0
                else 0)
        conversion_rate = (round((campaign["total_conversions"] / campaign["landing_page_views"]) * 100,2,)
                if campaign["landing_page_views"] != 0
                else 0)

        # Determine Recommendation
        recommendation = ""
        if roas > 4 :
            if conversion_rate > 5 and ctr > 5:
                recommendation = "Your campaign is Great, Increase your budget"
            else:
                recommendation = "Good ROAS, but check conversion rate and CTR"
        elif roas < 4 and conversion_rate < 5:
            recommendation = "Check offer & bottom sales funnel"
        elif roas < 4 and ctr < 5:
            recommendation = "Check ad relevance to landing page"
        elif roas < 4 and cpc > 5000:
            recommendation = "Change ad creative & landing page"
        else:
            recommendation = "Analyze further to optimize"

        # Append data to table_data
        table_data_kpi.append([
            campaign["adset_id"],
            f"{ctr:.2f}%",
            f"{cpc:.2f}",
            f"{conversion_rate:.2f}",
            f"{roas:.2f}",
            recommendation
        ])
    
    # Define headers
    headers = ["Ad Set ID", "CTR", "CPC","Conversion Rate","ROAS","Recommendation"]

    # Print the table using tabulate
    print(tabulate(table_data_kpi, headers=headers, tablefmt="grid"))
    print("\n")
    return

def sort_campaign_data(campaign_data, sort_by="ROAS", ascending=False):
    """Sorts campaign data based on a chosen KPI."""
    # Ensure valid sorting key
    valid_keys = ["CTR", "CPC", "Conversion Rate", "ROAS"]
    if sort_by.upper() not in valid_keys:
        print("Invalid sorting key, please choose from:", valid_keys)
        return campaign_data
    sorted_data = sorted(campaign_data, key=lambda x: x[sort_by.lower()], reverse=not ascending)
    return sorted_data

campaign_data = []
while True:
    display_main_menu()
    try:
        pilihan_menu = int(input("\nWhat menu that you would to choose? "))
        if pilihan_menu == 1:
            read_campaign(campaign_data)
        elif pilihan_menu == 2:
            campaign_data = create_campaign() 
        elif pilihan_menu == 3:  
            update_campaign(campaign_data)
        elif pilihan_menu == 4:  
            search_campaign(campaign_data)
        elif pilihan_menu == 5:  
            delete_campaign(campaign_data)
        elif pilihan_menu == 6:  
            kpi_campaign() 
        elif pilihan_menu == 7:  
            print("Good Job Team, all greats !")
            break  
    except ValueError:
        print("Your input is not valid, Input a number")

