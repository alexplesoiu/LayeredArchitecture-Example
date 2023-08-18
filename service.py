from typing import List
from domain.client import Client
from repository.memory import MemoryRepository


class Service:
    def __init__(self, repository: MemoryRepository):
        self._repository = repository

    def add_client(self, client: Client) -> None:
        """ Add a new client """

        self._repository.save(client)

    def get_client(self, client_id: str) -> Client:
        """ Retrieve a client by ID """

        return self._repository.get(client_id)

    def get_all_clients(self) -> List[Client]:
        """ Retrieve all clients """

        return self._repository.get_all()

    def update_client(self, client_id: str, client: Client) -> Client:
        """ Update a client's details """

        return self._repository.update(client_id, client)

    def remove_client(self, client_id: str) -> None:
        """ Remove a client by ID """

        self._repository.delete(client_id)

    def filter_by_name(self, name_substring: str) -> List[Client]:
        """ Filter clients by a substring of their name """

        return [
            client for client in self._repository.get_all()
            if name_substring.lower() in client.name.lower()
        ]

    def generate_report(self) -> str:
        """ Generate a simple report about the clients """

        total_clients = len(self._repository.get_all())
        report = f"Total clients: {total_clients}\n\n"

        for client in self._repository.get_all():
            report += f"{client.client_id}. {client.name} - {client.email}\n"
        return report
