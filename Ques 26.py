def check_string_prefix_suffix(string, prefix, suffix):
    starts_with_prefix = string.startswith(prefix)
    
    ends_with_suffix = string.endswith(suffix)
    
    return starts_with_prefix or ends_with_suffix

if __name__ == "__main__":
    string = "Hello, world!"
    prefix = "Hello"
    suffix = "world!"

    result = check_string_prefix_suffix(string, prefix, suffix)
    
    print(f"Does the string start with '{prefix}' or end with '{suffix}'? {result}")