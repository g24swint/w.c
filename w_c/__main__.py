

print("W.C version 201606")


import click

@click.group()
def workcard():
    pass


@workcard.command()
def clean(**kwargs):
    print("clean card")

@workcard.command()
def add(**kwargs):
    print("add task")

@workcard.command()
def add_goal(**kwargs):
    print("add goal")


if __name__ == "__main__":
    workcard()
