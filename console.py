from service import Service
from domain.client import Client


class Console:
    def __init__(self, service: Service):
        self._service = service
        self._menu_options = {
            "1": ("Add Client", self._add_client),
            "2": ("View Client", self._view_client),
            "3": ("View All Clients", self._view_all_clients),
            "4": ("Update Client", self._update_client),
            "5": ("Delete Client", self._delete_client),
            "6": ("Filter Clients by Name", self._filter_by_name),
            "7": ("Generate Report", self._generate_report),
            "0": ("Exit", None)
        }

    def _print_menu(self):
        for key, (description, _) in self._menu_options.items():
            print(f"{key}. {description}")

    def _add_client(self):
        client_id = int(input("Enter Client ID: "))
        name = input("Enter Client Name: ")
        email = input("Enter Client Email: ")
        phone_number = input("Enter Client Phone Number: ")

        client = Client(client_id, name, email, phone_number)
        self._service.add_client(client)

        print(f"Client {name} added successfully!")

    def _view_client(self):
        client_id = int(input("Enter Client ID to view: "))
        client = self._service.get_client(client_id)

        if client:
            print(client.name, client.email, client.phone_number)
        else:
            print("Client not found!")

    def _view_all_clients(self):
        clients = self._service.get_all_clients()

        for client in clients:
            print(
                client.client_id,
                client.name,
                client.email,
                client.phone_number
            )

    def _update_client(self):
        client_id = int(input("Enter Client ID to update: "))
        client = self._service.get_client(client_id)

        if client:
            name = input(f"Enter new name ({client.name}): ")
            email = input(f"Enter new email ({client.email}): ")
            phone_number = input(
                f"Enter new phone number ({client.phone_number}): "
            )

            client.name = name or client.name
            client.email = email or client.email
            client.phone_number = phone_number or client.phone_number

            self._service.update_client(client_id, client)
            print("Client updated successfully!")
        else:
            print("Client not found!")

    def _delete_client(self):
        client_id = int(input("Enter Client ID to delete: "))
        self._service.remove_client(client_id)

        print("Client removed successfully!")

    def _filter_by_name(self):
        name_substring = input("Enter substring to filter by name: ")
        filtered_clients = self._service.filter_by_name(name_substring)

        for client in filtered_clients:
            print(client.client_id, client.name)

    def _generate_report(self):
        report = self._service.generate_report()

        print(report)

    def run(self):
        while True:
            self._print_menu()

            choice = input("Choose an option: ")

            if choice in self._menu_options:
                _, action = self._menu_options[choice]

                if action:
                    action()
                else:
                    break
            else:
                print("Invalid choice!")

            input("Press Enter to continue...")
