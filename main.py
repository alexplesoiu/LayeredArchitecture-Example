from repository.memory import MemoryRepository
from service import Service
from console import Console


def main():
    repo = MemoryRepository()
    service = Service(repo)
    ui = Console(service)
    ui.run()


if __name__ == "__main__":
    main()
