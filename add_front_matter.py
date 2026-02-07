
import os
import re
import collections

# Path to the audit list
AUDIT_FILE = r"d:\OneDrive - Higher Education Commission\Documents\GitHub\yasirbhutta.github.io\audit_missing_front_matter.md"

def get_stop_words():
    return set([
        "a", "an", "the", "and", "or", "but", "is", "are", "was", "were", "be", "been", "being",
        "in", "on", "at", "to", "for", "from", "with", "by", "about", "of", "this", "that", "these", "those",
        "it", "i", "you", "he", "she", "we", "they", "me", "him", "her", "us", "them",
        "what", "which", "who", "whom", "whose", "where", "when", "why", "how",
        "can", "could", "will", "would", "shallow", "may", "might", "must", "should",
        "d", "s", "t", "m", "re", "ve", "ll", "not", "no", "yes"
    ])

def extract_metadata(content, filename):
    lines = content.split('\n')
    
    # 1. Title: First H1 or first non-empty line
    title = ""
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('# '):
            title = stripped[2:].strip()
            break
    
    if not title:
        for line in lines:
            stripped = line.strip()
            if stripped and not stripped.startswith(('#', '-', '*', '>', '`', '[')):
                title = stripped
                break
    
    if not title:
        # Fallback to filename without extension and replacing dashes/underscores
        base = os.path.basename(filename)
        title = os.path.splitext(base)[0].replace('-', ' ').replace('_', ' ').title()

    # 2. Description: First 150 chars of text (skipping headers/code)
    text_content = []
    for line in lines:
        stripped = line.strip()
        # skip headers, empty lines, code blocks markers, horizontal rules
        if not stripped or stripped.startswith(('#', '```', '---')):
            continue
        # simple cleanup of markdown links [text](url) -> text
        clean_line = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', stripped)
        # cleanup bold/italic
        clean_line = re.sub(r'[*_]{1,2}([^*_]+)[*_]{1,2}', r'\1', clean_line)
        text_content.append(clean_line)
    
    full_text = " ".join(text_content)
    description = full_text[:150].strip()
    if len(full_text) > 150:
        description += "..."
    if not description:
        description = f"Documentation and resources for {title}."

    # 3. Keywords: Extract 5 relevant words
    # Combine title and text for source
    source_text = (title + " " + full_text).lower()
    # Remove non-alphanumeric
    words = re.findall(r'\b[a-z]{3,}\b', source_text)
    stop_words = get_stop_words()
    
    filtered_words = [w for w in words if w not in stop_words]
    
    # Use simple frequency
    counter = collections.Counter(filtered_words)
    # Get top 5 common, preserving order somewhat by frequency
    top_keywords = [w for w, c in counter.most_common(5)]
    
    # If not enough, fill with generic terms based on path
    if len(top_keywords) < 5:
        path_parts = filename.replace('\\', '/').split('/')
        for part in reversed(path_parts[:-1]): # exclude filename, look at folders
            if part not in top_keywords and part not in stop_words and len(part) > 2:
                top_keywords.append(part)
                if len(top_keywords) >= 5:
                    break
    
    keywords_str = ", ".join(top_keywords)

    return title, description, keywords_str

def process_file(filepath):
    try:
        if not os.path.exists(filepath):
            print(f"Skipping (not found): {filepath}")
            return False
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if content.startswith('---'):
            print(f"Skipping (already has front matter): {filepath}")
            return False

        title, description, keywords = extract_metadata(content, filepath)

        front_matter = (
            "---\n"
            "layout: default\n"
            f"title: {title}\n"
            f"description: {description}\n"
            f"keywords: {keywords}\n"
            "---\n"
        )

        new_content = front_matter + content
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Updated: {filepath}")
        return True

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    if not os.path.exists(AUDIT_FILE):
        print("Audit file not found.")
        return

    with open(AUDIT_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        line = line.strip()
        if line.startswith('- '):
            filepath = line[2:].strip()
            if process_file(filepath):
                count += 1
    
    print(f"Total files updated: {count}")

if __name__ == "__main__":
    main()
