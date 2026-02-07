
import os
import re
import collections

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
            if stripped and not stripped.startswith(('#', '-', '*', '>', '`', '[', '---')):
                title = stripped
                break
    
    if not title:
        # Fallback to filename
        base = os.path.basename(filename)
        title = os.path.splitext(base)[0].replace('-', ' ').replace('_', ' ').title()

    # Truncate title to ~60 chars if extrunally long
    if len(title) > 65:
         title = title[:60] + "..."

    # 2. Description: First 150 chars of text (skipping headers/code)
    text_content = []
    for line in lines:
        stripped = line.strip()
        # skip headers, empty lines, code blocks markers, horizontal rules, liquid tags
        if not stripped or stripped.startswith(('#', '```', '---', '{%')):
            continue
        # simple cleanup
        clean_line = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', stripped) # links
        clean_line = re.sub(r'[*_]{1,2}([^*_]+)[*_]{1,2}', r'\1', clean_line) # bold/ital
        clean_line = re.sub(r'`([^`]+)`', r'\1', clean_line) # code spans
        text_content.append(clean_line)
    
    full_text = " ".join(text_content)
    description = full_text[:150].strip()
    if len(full_text) > 150:
        description += "..."
    if not description:
        description = f"Learn about {title} with this comprehensive guide."

    # 3. Keywords
    source_text = (title + " " + full_text).lower()
    words = re.findall(r'\b[a-z]{3,}\b', source_text)
    stop_words = get_stop_words()
    filtered_words = [w for w in words if w not in stop_words]
    counter = collections.Counter(filtered_words)
    top_keywords = [w for w, c in counter.most_common(8)]
    
    # Generic fill
    if len(top_keywords) < 5:
        path_parts = filename.replace('\\', '/').split('/')
        for part in reversed(path_parts[:-1]): 
            if part not in top_keywords and part not in stop_words and len(part) > 2:
                top_keywords.append(part)
                if len(top_keywords) >= 5:
                    break
    
    keywords_str = ", ".join(top_keywords)
    return title, description, keywords_str

def parse_front_matter(content):
    if not content.startswith('---'):
        # Just to be safe, check for BOM
        if content.startswith('\ufeff---'):
            content = content[1:]
        else:
            return None, content

    # Find end of front matter
    # We look for \n--- followed by whitespace/newline
    # Check for \n---\n or \n---$
    
    # Try finding the closing fence
    # We search from index 3 to skip the opening ---
    pos = 3
    while True:
        end_idx = content.find('\n---', pos)
        if end_idx == -1:
            return None, content
            
        # Check what follows the ---
        # It must be end of line or EOF
        # Check char after \n---
        after_fence = end_idx + 4
        if after_fence >= len(content):
            # EOF right after ---
            body_start = after_fence
            break
        
        char_after = content[after_fence]
        if char_after == '\n' or char_after == '\r':
             body_start = after_fence
             # consume newline if present to get to body
             if content[body_start] == '\r': body_start += 1
             if body_start < len(content) and content[body_start] == '\n': body_start += 1
             break
        elif char_after == ' ':
             # Spaces allowed? '--- '
             # Check if rest of line is space
             next_nl = content.find('\n', after_fence)
             if next_nl == -1: next_nl = len(content)
             line_rest = content[after_fence:next_nl]
             if not line_rest.strip():
                 body_start = next_nl
                 if body_start < len(content) and content[body_start] == '\n': body_start += 1
                 break
        
        # False alarm, maybe a horizontal rule in content? Keep searching
        pos = end_idx + 1

    fm_text = content[3:end_idx]
    body = content[body_start:]
    
    metadata = {}
    try:
        for line in fm_text.split('\n'):
            line = line.strip()
            if not line or line.startswith('#'): continue
            if ':' in line:
                key, val = line.split(':', 1)
                metadata[key.strip()] = val.strip()
    except Exception as e:
        print(f"Warning: YAML parse error: {e}")
        return None, content
        
    return metadata, body

def process_file(filepath):
    #print(f"DEBUG: Processing {filepath}")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        existing_metadata, body = parse_front_matter(content)
        
        if existing_metadata is None:
            # Create new
            existing_metadata = {}
        
        # Extract heuristic metadata
        h_title, h_desc, h_kw = extract_metadata(body, filepath)

        # Merge
        existing_metadata['layout'] = 'page'
        
        # Title logic: Preserve if exists, else use heuristic
        if 'title' not in existing_metadata or not existing_metadata['title']:
            existing_metadata['title'] = f'"{h_title}"'
        else:
             # Clean up quotes if needed?
             pass

        if 'description' not in existing_metadata or not existing_metadata['description']:
            existing_metadata['description'] = f'"{h_desc}"'
        
        if 'keywords' not in existing_metadata or not existing_metadata['keywords']:
            existing_metadata['keywords'] = f'"{h_kw}"'

        # Reconstruct
        fm_lines = ["---"]
        order = ['layout', 'title', 'description', 'keywords']
        for k in order:
            if k in existing_metadata:
                fm_lines.append(f"{k}: {existing_metadata[k]}")
        
        for k, v in existing_metadata.items():
            if k not in order:
                fm_lines.append(f"{k}: {v}")
        
        fm_lines.append("---")
        fm_lines.append("")
        
        new_content = "\n".join(fm_lines) + body # Body already parsed clean
        
        # Detect if change is needed? (Optional, but good for speed)
        # Just write it
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Processed: {filepath}")
        return True

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    root_dir = os.getcwd()
    print(f"Scanning directory: {root_dir}")
    
    count = 0
    for root, dirs, files in os.walk(root_dir):
        # Simplistic skip
        if '\\.git' in root or '/.git' in root or '\\_site' in root: 
             continue
        
        for file in files:
            if file.lower().endswith('.md'):
                filepath = os.path.join(root, file)
                # Only print first few to avoid log spam if many
                if count < 5: print(f"DEBUG: Found {file}")
                if process_file(filepath):
                    count += 1
    
    print(f"Total files processed: {count}")

if __name__ == "__main__":
    main()
