from typing import Protocol
from typing import List
from domain.client import Client


class IRepository(Protocol):
    """ Repository for Client CRUD operations """

    def get(self) -> Client:
        """ Get a specific client """
        raise NotImplementedError("get not implemented")

    def get_all(self) -> List[Client]:
        """ Get all clients """
        raise NotImplementedError("get_all not implemented")

    def save(self, client: Client) -> None:
        """ Save client """
        raise NotImplementedError("save not implemented")

    def update(self, client_id: str, client: Client) -> Client:
        """ Update client """
        raise NotImplementedError("update not implemented")

    def delete(self, client_id: str) -> Client:
        """ Delete client """
        raise NotImplementedError("delete not implemented")
