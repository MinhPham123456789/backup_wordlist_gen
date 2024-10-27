from urllib.parse import urlparse

def combinations(words, symbol):
    words_split = words.split(symbol)
    # exclude the first combination when split words length is equal to 1
    results = [symbol.join(words_split[:i + 1]) for i in range(len(words_split)) if not(i == 0 and len(words_split) == 1)]
    return [result for result in results if result]

def concat_extensions(results, extensions):
    # filtering out any results that start with "." or "-" or are empty strings
    results = [result for result in results if not result.startswith(("-",".")) and result] 
    extended_results = [''.join([result, extension]) for result in results for extension in extensions]
    return extended_results

def parse_url(url, registered_domain, extensions, full_url=False):
    url_parts = urlparse(url)
    scheme = url_parts.scheme
    fqdn = url_parts.netloc
    subdomain = fqdn.split("." + registered_domain)[0]

    subdomain_Z = subdomain
    subdomain_Y = fqdn
    subdomain_Y1 = "OLD." + fqdn
    subdomain_Z1 = "OLD-" + subdomain
    subdomain_Y12 = "OLD." + subdomain
    subdomain_Z12 = "OLD-" + fqdn
    domain_Y = registered_domain

    results_dot = combinations(subdomain_Z.replace("-", "."), '.')
    results_dash = combinations(subdomain_Z.replace(".", "-"), '-')
    results_dot1 = combinations(subdomain_Y.replace("-", "."), '.')
    results_dash1 = combinations(subdomain_Y.replace(".", "-"), '-')
    results_dot2 = combinations(subdomain_Y1.replace("-", "."), '.')
    results_dash2 = combinations(subdomain_Z1.replace(".", "-"), '-')
    results_dot21 = combinations(subdomain_Y12.replace("-", "."), '.')
    results_dash21 = combinations(subdomain_Z12.replace(".", "-"), '-')
    results_Y = [domain_Y.split(".")[0], domain_Y, domain_Y.replace(".", "-")]

    results = []
    results.extend(results_dot1)
    results.extend(results_dash1)
    results.extend(results_dot2)
    results.extend(results_dash2)
    results.extend(results_dot21)
    results.extend(results_dash21)
    results.extend(results_dot)
    results.extend(results_dash)
    results.extend(results_Y)

    if full_url and scheme:
        results = [f'{url}/{i}' for i in results]

    results = concat_extensions(results, extensions)
    results = sorted(list(set(results)))
    return results

def get_extensions(ext_filepath_list=['./wordlists/backup_gen_extensions.txt', 'wordlists/backup_gen_wordlists.txt']):
    for ext_filepath in ext_filepath_list:       
        with open(ext_filepath, 'r') as ext_file:
            extensions = ext_file.read().splitlines()
            # Check if extensions start with ".", else add one
            extensions = ['.' + ext if ext[0] != '.' else ext for ext in extensions]
            return extensions