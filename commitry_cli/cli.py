import argparse
from .git_utils import get_staged_diff
from .test_deepseek import generate_commit_message

def main():
    parser = argparse.ArgumentParser(description="Suggest commit messages using a local LLM.")
    parser.add_argument("--model", default="bigscience/starcoder-base", help="Model name or path")
    parser.add_argument("--device", default="cpu", help="Device to run inference on")
    args = parser.parse_args()

    # 1. Get the diff
    diff = get_staged_diff()
    if not diff.strip():
        print("No staged changes found.")
        return

    # 2. (Optional) Summarize or reduce the diff if it's very large
    # For a naive approach, let’s just limit the diff to some chunk
    # or implement your own summarization approach.
    truncated_diff = diff[:5000]  # naive truncation to 5000 chars

    # 3. Load the model
    commit_message = generate_commit_message(truncated_diff)

    print("\nSuggested commit message:\n")
    print(commit_message)
    print("\n")
