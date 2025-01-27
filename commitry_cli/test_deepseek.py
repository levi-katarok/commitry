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


def generate_commit_message(diff):
    system_prompt = "You are a helpful assistant that generates concise user git commit messages for git commits. You will recieve git diffs and you will return a concise commit message. Your job is to summarize the changes in the diff into a concise commit message."
    import pdb; pdb.set_trace()
    response = client.chat.completions.create(
        model="deepseek-r1:1.5b",
        messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": diff}],
        stream=True
    )
    for chunk in response:
        print(chunk.choices[0].delta.content, end="", flush=True)
