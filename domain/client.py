class Client:
    def __init__(
        self,
        client_id: str,
        name: str,
        email: str,
        phone_number: str
    ):
        self._client_id = client_id
        self._name = name
        self._email = email
        self._phone_number = phone_number
        self._address = None

    @property
    def client_id(self):
        return self._client_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        self._email = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        self._phone_number = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value: str):
        self._address = value
