# coding=utf-8
import os
import click
from configparser import ConfigParser
from tool import DockerTool

cfg = ConfigParser()
cfg.read(os.getcwd() + r'/cfg')


@click.group()
def cmd_group():
    pass


@click.command()
@click.option('-w', '--workspace', prompt=True)
@click.option('-e', '--environment', prompt=True)
@click.option('-u', '--username', prompt=True)
@click.option('-p', '--password', prompt=True, hide_input=True)
def init(workspace, environment, username, password):
    if not workspace and not environment:
        cfg.set('path', 'local_workspace', workspace)
        cfg.set('image', 'default_image', environment)
    with open(os.getcwd() + r'/cfg', 'w+') as fp:
        cfg.write(fp)
    docker = DockerTool()
    docker.d_login(username, password)


@click.command()
@click.option('-p', '--path', default=cfg.get('path', 'dockerfile_path') + r'/python3',
              help='build a image from the directory')
@click.option('-i', '--image', default=cfg.get('image', 'default_image'), help='Choose the type of installation image')
def build(image, path):
    "build the image selected"""
    path = cfg.get('path', 'dockerfile_path') + path
    docker = DockerTool()
    docker.d_create(image, path)


@click.command()
@click.option('--user', prompt=True, help='username')
@click.option('--password', prompt=True, help='password', hide_input=True)
def login(user, password):
    docker = DockerTool()
    docker.d_login(user, password)


@click.command()
@click.option('-i', '--image', default=cfg.get('image', 'default_image'), help='local image')
def push(image):
    "push image to the hub"""
    docker = DockerTool()
    docker.d_push_image(image)


@click.command()
@click.option('-i', '--image', default=cfg.get('image', 'default_image'), help='Choose the type of image')
def pull(image):
    "get image from the hub"""
    docker = DockerTool()
    docker.d_pull(image)


@click.command()
@click.option('-c', '--code_path', default=cfg.get("path", "local_workspace"),
              help='bind your local code to the container')
@click.option('-i', '--image', default=cfg.get('image', 'default_image'), help='Choose the type of image')
def start(image, code_path):
    "start a container from the selected image"""
    code_path += r':/workspace'
    docker = DockerTool()
    docker.d_start_container(image, code_path)


@click.command()
@click.option('--ask', prompt="are you sure update the container now?[y/n]")
def shutdown(ask):
    "close the container"""
    if ask.lower() == 'y':
        docker = DockerTool()
        docker.d_shutdown_container()


@click.command()
@click.option('-i', '--image', default=cfg.get('image', 'default_image'), help='choose the image you want to update')
@click.option('--ask', prompt="are you sure update the container now?[y/n]")
def update(image, ask):
    "update the image"""
    if ask.lower() == 'y':
        docker = DockerTool()
        docker.d_update_image(image)


cmd_group.add_command(init)
cmd_group.add_command(build)
cmd_group.add_command(login)
cmd_group.add_command(push)
cmd_group.add_command(pull)
cmd_group.add_command(start)
cmd_group.add_command(shutdown)
cmd_group.add_command(update)

if __name__ == '__main__':
    cmd_group()
