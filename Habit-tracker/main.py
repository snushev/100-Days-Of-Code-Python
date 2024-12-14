import requests
import datetime

current_date = datetime.datetime.now().strftime("%Y%m%d")
USERNAME = input("Enter username: ").strip()
TOKEN = input("Enter token: ").strip()

headers = {
    "X-USER-TOKEN": TOKEN,
}

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
selected_graph_id = None
selected_graph_unit = None


def register_user():
    agreement = input("Do you agree to the terms of service (yes/no): ").strip().lower()
    if agreement != "yes":
        print("You must agree to the terms of service to register.")
        exit()

    minor = input("Are you not a minor (yes/no): ").strip().lower()
    if minor != "yes":
        print("You must confirm that you are not a minor to register.")
        exit()

    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": agreement,
        "notMinor": minor,
    }

    response = requests.post(pixela_endpoint, json=user_params)
    if response.status_code == 200:
        print("User registered successfully!")
    else:
        print(f"Failed to register user: {response.text}")
        exit()


def check_user_and_graphs():
    response = requests.get(f"{pixela_endpoint}/{USERNAME}", headers=headers)
    if response.status_code != 200:
        print("User does not exist or token is invalid.")
        register_user()

    print("User exists. Checking graphs...")
    response = requests.get(graph_endpoint, headers=headers)
    if response.status_code == 200:
        graphs = response.json()["graphs"]
        if graphs:
            print("Available graphs:")
            for graph in graphs:
                print(f"ID: {graph['id']}, Name: {graph['name']}")
            return graphs
        else:
            print("No graphs found.")
    else:
        print(f"Failed to retrieve graphs: {response.text}")



def create_graph():
    global selected_graph_id, selected_graph_unit

    graph_id = input("Enter graph ID: ")
    name = input("Enter graph name: ")
    unit = input("Enter unit: ")
    type_ = input("Enter type (int/float): ")
    color = input("Enter color (shibafu, momiji, sora, ichou, ajisai, kuro): ")

    graph_params = {
        "id": graph_id,
        "name": name,
        "unit": unit,
        "type": type_,
        "color": color,
    }
    response = requests.post(graph_endpoint, json=graph_params, headers=headers)
    print(response.text)
    if response.status_code == 200:
        selected_graph_id = graph_id
        selected_graph_unit = unit


def add_pixel_info():
    if not selected_graph_id:
        print("No graph selected.")
        return

    date = input("Enter the date (format: yyyyMMdd) or type 'today': ").strip()
    if date.lower() == "today":
        date = current_date

    quantity = input(f"Enter the {selected_graph_unit} for {date}: ")

    pixel_endpoint = f"{graph_endpoint}/{selected_graph_id}"
    pixel_params = {
        "date": date,
        "quantity": quantity,
    }
    response = requests.post(pixel_endpoint, json=pixel_params, headers=headers)
    print(response.text)


def edit_pixel_info():
    if not selected_graph_id:
        print("No graph selected.")
        return

    date = input("Enter the date to edit (format: yyyyMMdd): ")
    edit_pixel_endpoint = f"{graph_endpoint}/{selected_graph_id}/{date}"

    quantity = input(f"Enter the new {selected_graph_unit} for {date}: ")
    edit_pixel_params = {
        "quantity": quantity,
    }
    response = requests.put(edit_pixel_endpoint, json=edit_pixel_params, headers=headers)
    print(response.text)


def delete_pixel_info():
    if not selected_graph_id:
        print("No graph selected.")
        return

    date = input("Enter the date to delete (format: yyyyMMdd): ")
    delete_pixel_endpoint = f"{graph_endpoint}/{selected_graph_id}/{date}"

    response = requests.delete(delete_pixel_endpoint, headers=headers)
    print(response.text)


check_user_and_graphs()

while True:
    print("\nChoose one of the following:")
    print("1. Create new graph")
    print("2. Add pixel information")
    print("3. Edit pixel information")
    print("4. Delete pixel information")
    print("5. Change graph")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()
    if choice == "1":
        create_graph()
    elif choice == "2":
        add_pixel_info()
    elif choice == "3":
        edit_pixel_info()
    elif choice == "4":
        delete_pixel_info()
    elif choice == "5":
        check_user_and_graphs()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
