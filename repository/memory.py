from typing import List
from .interface import IRepository
from domain.client import Client


class MemoryRepository(IRepository):
    def __init__(self):
        self._clients = {}  # The actual memory database is a dictionary

    def get(self, client_id: str) -> Client:
        """ Get a specific client """

        return self._clients.get(client_id)

    def get_all(self) -> List[Client]:
        """ Get all clients """

        return list(self._clients.values())

    def save(self, client: Client) -> None:
        """ Save client """

        if client.client_id in self._clients:
            raise ValueError(
                f"Client with ID {client.client_id} already exists!"
            )

        self._clients[client.client_id] = client

    def update(self, client_id: str, client: Client) -> Client:
        """ Update client """

        if client_id not in self._clients:
            raise ValueError(
                f"Client with ID {client_id} does not exist!"
            )

        self._clients[client_id] = client

        return self._clients[client_id]

    def delete(self, client_id: str) -> Client:
        """ Delete client """

        if client_id not in self._clients:
            raise ValueError(
                f"Client with ID {client_id} does not exist!"
            )

        removed_client = self._clients[client_id]
        del self._clients[client_id]

        return removed_client
