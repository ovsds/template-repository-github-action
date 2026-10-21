import os
import tempfile

import tests.utils.replay as replay_utils
import tests.utils.cli as cli_utils

MANIFEST_PATH = "tests/replays.json"
ADDITIONAL_FILES_PATH = "tests/additional_files"


def test_replay(replay: replay_utils.Replay, results_path: str):
    replay_utils.clean_replay(replay, results_path)
    replay_utils.build_replay(replay, results_path)

    cwd = f"{results_path}/{replay.parameters['project_slug']}"
    replay_utils.copy_additional_files(replay, ADDITIONAL_FILES_PATH, cwd)

    cli_utils.run_command("git init", cwd=cwd)
    cli_utils.run_command("git add --all", cwd=cwd)
    cli_utils.run_command("git -c user.name=test -c user.email=test@example.com -c commit.gpgsign=false commit --quiet --no-verify -m init", cwd=cwd)
    # a worktree under artifacts/, so a tool that walks into it fails init, lint, test or package
    cli_utils.run_command("git worktree add --quiet --detach artifacts/worktrees/test", cwd=cwd)
    cli_utils.run_command("mise run init", cwd=cwd)
    cli_utils.run_command("mise run lint", cwd=cwd)
    cli_utils.run_command("mise run lint-fix", cwd=cwd)
    if replay.parameters.get("action_type") == "node":
        # mise run hands vitest a TTY, so it watches for changes and never exits unless CI is set
        cli_utils.run_command("CI=true mise run test", cwd=cwd)
        cli_utils.run_command("mise run package", cwd=cwd)
    cli_utils.run_command("mise run clean", cwd=cwd)
    assert not os.path.exists(f"{cwd}/artifacts"), "mise run clean left artifacts/"
    assert not os.path.exists(f"{cwd}/.git/worktrees"), "mise run clean left the worktree registered"

    replay_utils.clean_replay(replay, results_path)


def test_replays():
    # outside the repository, so its own mise tools and node_modules/.bin cannot hide a tool the generated mise.toml misses
    with tempfile.TemporaryDirectory(prefix="replays-") as temp_path:
        results_path = os.path.join(os.path.realpath(temp_path), "results")
        # mise refuses [env] and [settings] of an untrusted config; trust the throwaway results only for this run
        trusted_paths = [os.environ.get("MISE_TRUSTED_CONFIG_PATHS"), results_path]
        os.environ["MISE_TRUSTED_CONFIG_PATHS"] = os.pathsep.join(filter(None, trusted_paths))
        for replay in replay_utils.read_replays(MANIFEST_PATH):
            test_replay(replay, results_path)


__all__ = [
    "test_replays",
]
