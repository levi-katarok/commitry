import argparse
from .git_utils import get_staged_diff, clean_diff
from .llm import generate_commit_message

def main():
    parser = argparse.ArgumentParser(description="Suggest commit messages using a local LLM.")
    parser.add_argument("--model", default="deepseek-r1:7b", help="Model name or path")
    args = parser.parse_args()


    # Get the diff
    raw_diff = get_staged_diff()
    diff = clean_diff(raw_diff)
    if not diff.strip():
        print("No staged changes found.")
        return

    # Load the model
    commit_message = generate_commit_message(diff, args.model)

    print("\nSuggested commit message:\n")
    print(commit_message)
    print("\n")
