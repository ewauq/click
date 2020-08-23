import os
import click


@click.group()
def cli():
    pass


for service in os.listdir("services"):

    if service != "__pycache__":
        try:
            path = f"services.{service}.main"
            module = __import__(path, fromlist=[service])
            cli.add_command(getattr(module, service))
        except ModuleNotFoundError:
            print(f"Unable to find the {service} service ({path})")


if __name__ == "__main__":
    cli()
