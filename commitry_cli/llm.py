import openai

# Connect to your local Ollama instance
client = openai.Client(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # Authentication-free private access
)


def clean_response(text):
    """Remove any thinking sections from the LLM response."""
    # Remove any content between <think> tags
    while '<think>' in text and '</think>' in text:
        start = text.find('<think>')
        end = text.find('</think>') + len('</think>')
        text = text[:start] + text[end:]
    return text.strip()

def generate_commit_message(diff, model="deepseek-r1:7b"):
    system_prompt = "You are a helpful assistant that generates concise summaries of git diffs. You will recieve git diffs and you will outut a once sentence summary of the changes made by the user. Your job is to summarize the changes made by the user into one sentence such that the user can post it as a commit message."
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": diff}],
        stream=True
    )
    commit_message = ""
    for chunk in response:
        content = chunk.choices[0].delta.content
        commit_message += content
        print(content, end="", flush=True)
    # Clean up the response before returning
    return clean_response(commit_message)