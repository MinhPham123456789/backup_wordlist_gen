import argparse
from engines.bfac_engine import generate_bfa_urls
from engines.backup_gen_engine import get_extensions, parse_url
from urllib.parse import urlparse

def get_bfac_path(bfac_urls, target_url):
    bfac_paths = []
    domain_name = urlparse(target_url).netloc
    domain_name_with_underscore = domain_name.replace(".", "_") # Add alternative to domain name or file name 
    domain_name_with_dash = domain_name.replace(".", "-") # Add alternative to domain name or file name
    target_url = target_url + "/"
    for u in bfac_urls:
        path = u.split(target_url)[-1]
        if u != target_url + path:
            print(f"[ERROR]: Path split is incorrect with {u}, split path: {path}")
        else:
            bfac_paths.append(path)
            if domain_name in path: # Add alternative to domain name or file name in the backup file names or paths
                bfac_paths.append(path.replace(domain_name, domain_name_with_underscore))
                bfac_paths.append(path.replace(domain_name, domain_name_with_dash))
    return bfac_paths


def main():
    # Create the parser
    parser = argparse.ArgumentParser(description='Generate wordlist for backup file paths')
    # Add the URL argument
    parser.add_argument('--url', type=str, required=True, help='Target\'s URL e.g: https://example.com')
    parser.add_argument('--registered_domain', type=str, required=True, help='Target\'s registered domain e.g: https://test.example.com then registered domain is example.com, test is a subdomain')
    parser.add_argument('--output', type=str, default="./backup_wordlist.txt", help='Backup wordlist output (default: ./backup_wordlist.txt)')
    # Parse the arguments
    args = parser.parse_args()
    target_url = args.url.strip()
    if target_url[-1] == '/':
        target_url = target_url[0:-1]
    print(f"Generating backup file names and paths for {target_url}")
    bfac_urls = generate_bfa_urls(target_url, 5)
    bfac_paths = get_bfac_path(bfac_urls, target_url)
    extensions = get_extensions()
    backup_gen_paths = parse_url(target_url, args.registered_domain.strip(), extensions)
    result = bfac_paths + backup_gen_paths
    result = sorted(list(set(result)))
    # for i in result:
    #     print(i)
    with open(args.output, 'w', encoding='utf-8') as file:
        file.write('\n'.join(map(str, result)) + '\n')
    print(f'Generated {len(result)} file names and paths')


if __name__ == "__main__":
    main()
    # DEBUG
    # DEBUG_url = "https://test.example.com"
    # DEBUG_registered_domain = "example.com"
    # ## bfac engine
    # bfac_urls = generate_bfa_urls(DEBUG_url, 5)
    # bfac_paths = get_bfac_path(bfac_urls, DEBUG_url)
    # with open("./test_bfac_engine.txt", 'w', encoding='utf-8') as file:
    #     file.write('\n'.join(map(str, sorted(bfac_paths))) + '\n')
    # ## backup gen engine
    # extensions = get_extensions()
    # backup_gen_paths = parse_url(DEBUG_url, DEBUG_registered_domain, extensions)
    # with open("./test_backup_gen_engine.txt", 'w', encoding='utf-8') as file:
    #     file.write('\n'.join(map(str, sorted(backup_gen_paths))) + '\n')
    # print(f'Result length {len(backup_gen_paths)}')
    # for i in backup_gen_paths:
    #     print(i)