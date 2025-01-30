import subprocess

def get_staged_diff():
    """Return the staged diff as a string."""
    # Alternatively, you can use GitPython
    result = subprocess.run(["git", "diff", "--staged"], capture_output=True, text=True)
    return result.stdout

def clean_diff(diff_text):
    """Clean up git diff output to a minimal format for LLM processing."""
    # First replace escaped newlines with actual newlines
    lines = diff_text.replace('\\n', '\n').split('\n')
    
    # Keep only the actual code changes
    cleaned_lines = []
    for line in lines:
        # Skip all git metadata and function definitions
        if any(line.startswith(x) for x in ['diff --git', 'index ', '@@', '--- ', '+++ ', 'def ']):
            continue
        # Keep actual changes
        if line.strip():
            # Replace any remaining escaped characters
            line = (line
                   .replace('\\t', '\t')
                   .replace('\\"', '"')
                   .replace("\\'", "'"))
            cleaned_lines.append(line)
            
    result = '\n'.join(cleaned_lines).strip()
    
    # Remove function definition if it exists
    if result.startswith('def '):
        result = '\n'.join(result.split('\n')[1:]).strip()
    return result

def calculate_radius_of_planet(planet):
    if planet == "Earth":
        return 6371
    elif planet == "Mars":
        return 3389
    else:
        return 0