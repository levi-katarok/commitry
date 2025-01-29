import openai

# Connect to your local Ollama instance
client = openai.Client(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # Authentication-free private access
)

# response = client.chat.completions.create(
#     model="deepseek-r1:1.5b", # change the "XX" by the distilled model you choose
#     messages=[{"role": "user", "content": "Explain blockchain security"}],
#     stream=True
# )

# for chunk in response:
#     print(chunk.choices[0].delta.content, end="", flush=True)


def clean_response(text):
    """Remove any thinking sections from the LLM response."""
    # Remove any content between <think> tags
    while '<think>' in text and '</think>' in text:
        start = text.find('<think>')
        end = text.find('</think>') + len('</think>')
        text = text[:start] + text[end:]
    return text.strip()

def generate_commit_message(diff):
    system_prompt = "You are a helpful assistant that generates concise user git commit messages for git commits. You will recieve git diffs and you will outut a once sentence commit message. Your job is to summarize the changes in the diff into a bullet point list of changes. The commit message should be a bullet point list of changes that summarizes the changes in the diff."
    response = client.chat.completions.create(
        model="deepseek-r1:7b",
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