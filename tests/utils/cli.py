import subprocess
import typing


class CommandError(Exception):
    def __init__(self, exit_code: int, command: str):
        self.exit_code = exit_code
        self.command = command


def run_command(command: str, cwd: typing.Optional[str] = None) -> None:
    print(f"Running command {command}...")
    try:
        subprocess.run(command, cwd=cwd, check=True, shell=True)
    except subprocess.CalledProcessError as exc:
        raise CommandError(
            exit_code=exc.returncode,
            command=command,
        ) from exc


__all__ = [
    "CommandError",
    "run_command",
]
