import click


@click.group()
def tvdb():
    """
    TVDB products management service.
    """
    pass


@click.command()
@click.option('--id', type=int, help="The TVDB series ID")
def update(id):
    """
    Updating series
    """
    if id:
        click.echo(f"Updating series {id}...")
    else:
        click.echo(f"Updating all series...")


@click.command()
@click.argument('id')
def delete(id):
    """
    Deleting series
    """
    click.echo(f"Deleting series {id}...")


tvdb.add_command(update)
tvdb.add_command(delete)
