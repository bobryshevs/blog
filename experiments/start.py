import click
import os
from flask import Flask
from collections import namedtuple
from loggers_factory import loggers_factory


EnvironmentFiles = namedtuple("EnvironmentFiles", ["docker_env", "local_env"])


class Starter:
    dotenv_template = '.env'
    DOCKER_ENV = 1
    LOCAL_ENV = 2

    def __init__(self, is_docker: bool) -> None:
        self.logger = loggers_factory.get()
        self.env_files = EnvironmentFiles("docker_env", "local_env")

        self.rename_env_for_start(is_docker)

        self.current_env = self.DOCKER_ENV if is_docker else self.LOCAL_ENV

    def rename_env_for_start(self, is_docker: bool):
        if is_docker:
            os.rename(self.env_files.docker_env, self.dotenv_template)
            self.logger.info("[+] Docker environment")
        else:
            os.rename(self.env_files.local_env, self.dotenv_template)
            self.logger.info("[+] Local environment")

    def rename_env_after_finish(self):
        if self.current_env == self.DOCKER_ENV:
            os.rename(self.dotenv_template, self.env_files.docker_env)
            self.logger.info("[-] Docker environment")
            self.logger.info("[+] Default settings")
        else:
            os.rename(self.dotenv_template, self.env_files.local_env)
            self.logger.info("[-] Local environment")
            self.logger.info("[+] Default settings")

    def start(self, debug: bool, host: str, port: str):
        try:
            from app import app as flask_app
            flask_app.run(debug=debug, host=host, port=port)
        except Exception as err:
            self.logger.error(str(err))
        finally:
            self.rename_env_after_finish()


@click.command()
@click.option("--docker", default=False, help="Use it if start in Docker")
@click.option("--debug", default=False, help="Set true if need debug mode")
@click.option("--host", default="0.0.0.0")
@click.option('--port', default='9003')
def main(docker: bool, debug: bool, host: str, port: str):
    starter = Starter(is_docker=docker)
    starter.start(debug=debug, host=host, port=port)


if __name__ == "__main__":
    main()
