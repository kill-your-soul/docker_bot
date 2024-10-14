from docker import DockerClient
from docker.models.containers import Container


def get_containers(client: DockerClient) -> list[Container]:
    return client.containers.list()


def get_container(client: DockerClient, container_id: str) -> Container:
    return client.containers.get(container_id)


def delete_container(client: DockerClient, container_id: str) -> None:
    container = get_container(client, container_id)
    container.remove()

def get_logs(client: DockerClient, container_id: str, lines: int = 10) -> str:
    container = get_container(client, container_id)
    return container.logs(tail=lines).decode("utf-8")


def restart_container(client: DockerClient, container_id: str) -> None:
    container = get_container(client, container_id)
    container.restart()

def stop_container(client: DockerClient, container_id: str) -> None:
    container = get_container(client, container_id)
    container.stop()
