from urllib.parse import urlparse

# Original project: https://github.com/mazen160/bfac/tree/master

def url_handler(url):
# Scheme: http
    default_protocol = 'http'
    if ('://' not in url):
        url = str(default_protocol) + str('://') + str(url)
    scheme = urlparse(url).scheme

    # Domain: example.com
    domain = urlparse(url).netloc

    # Site: http://example.com
    site = scheme + '://' + domain

    # FilePath: /uploads/test.php
    file_path = urlparse(url).path
    if (file_path == ''):
        file_path = '/'

    # Filename: test.php
    try:
        filename = url.split('/')[-1]
    except IndexError:
        filename = ''

    # File Dir: /uploads/
    file_dir = file_path.rstrip(filename)
    if (file_dir == ''):
        file_dir = '/'

    # FullPath: http://example.com/uploads/
    full_path = site + file_dir

    # File Extension: php
    try:
        filename_ext = filename.split('.')
        filename_ext.pop(0)
        filename_ext = '.'.join(filename_ext)
    except IndexError:
        filename_ext = ''

    # File without Extension: test
    try:
        filename_without_ext = filename.split('.')[0]
    except IndexError:
        filename_without_ext = ''

    output = {"scheme": scheme, "domain": domain,
              "site": site, "file_path": file_path,
              "filename": filename, "file_dir": file_dir,
              "full_path": full_path, "filename_ext": filename_ext,
              "filename_without_ext": filename_without_ext}
    return(output)

def generate_bfa_urls(url,
                      testing_level=5,
                      dvcs_test=False):
    """
    Generates BFA testing URLs.
    Returns a list of BFA testing URLs of given URL.
    """

    url_parsed = url_handler(url)

    (scheme, domain, site, file_path, filename,
     file_dir, full_path, filename_ext,
     filename_without_ext) = (url_parsed["scheme"],
                              url_parsed["domain"],
                              url_parsed["site"],
                              url_parsed["file_path"],
                              url_parsed["filename"],
                              url_parsed["file_dir"],
                              url_parsed["full_path"],
                              url_parsed["filename_ext"],
                              url_parsed["filename_without_ext"])

    # LEVEL 1
    backup_testing_level1 = [
        site + file_path + '~',
        site + file_path + '%23',
        site + file_path + '.save',
        site + file_path + '.swp',
        site + file_path + '.swo',
        full_path + '%23' + filename + '%23',
        site + file_path + '.bak'
    ]

    # LEVEL 2
    backup_testing_level2 = [
        site + file_path + '1',
        site + file_path + 'bak',
        site + file_path + 'inc',
        site + file_path + 'old',
        site + file_path + '_',
        site + file_path + '~~',
        site + file_path + '_backup',
        site + file_path + '_bak',
        site + file_path + '-bak',
        site + file_path + '.bk',
        site + file_path + '.bkp',
        full_path + filename + '.bac',
        site + file_path + '.old',
        site + file_path + '_old',
        site + file_path + '.copy',
        site + file_path + '.original',
        site + file_path + '.orig',
        site + file_path + '.org',
        site + file_path + '.txt',
        site + file_path + '.default',
        full_path + filename + '.tpl',
        full_path + filename + '.tmp',
        full_path + filename + '.temp',
        full_path + '.' + filename + ".swp",
        full_path + '.' + filename + ".swo",
        full_path + '_' + filename + '.swp',
        full_path + '_' + filename + '.swo',
        full_path + filename + '.sav',
        full_path + filename + '.conf',
        full_path + filename_without_ext +
        '%20%28copy%29.' + filename_ext,
        full_path + 'Copy%20of%20' + filename,
        full_path + 'copy%20of%20' + filename,
        full_path + 'Copy_' + filename,
        full_path + 'Copy%20' + filename,
        full_path + 'Copy_of_' + filename,
        full_path + 'Copy_(1)_of_' + filename,
        full_path + 'Copy_(2)_of_' + filename,
        full_path + filename_without_ext +
        '%20-%20Copy.' + filename_ext,
        full_path + filename_without_ext + '%20copy.' + filename_ext
    ]

    # LEVEL 3
    backup_testing_level3 = [
        full_path + filename_without_ext + '.txt',
        full_path + filename_without_ext + '.backup',
        full_path + filename_without_ext + '.bak',
        full_path + filename_without_ext + '.bak1',
        full_path + filename_without_ext + '.bakup',
        full_path + filename_without_ext + '.bakup1',
        full_path + filename_without_ext + '.bkp',
        full_path + filename_without_ext + '.save',
        full_path + filename_without_ext + '.old',
        full_path + filename_without_ext + '.orig',
        full_path + filename_without_ext + '.original',
        full_path + filename_without_ext + '.sql',
        full_path + filename_without_ext + '.war',
        full_path + filename_without_ext + '.wim',
        full_path + filename_without_ext + '.xz',
        site + file_path + '%00',
        site + file_path + '%01',
        full_path + '~' + filename,
        full_path + filename_without_ext + '.tpl',
        full_path + filename_without_ext + '.tmp',
        full_path + filename_without_ext + '.temp',
        full_path + filename + '.saved',
        full_path + filename + '.back',
        full_path + filename + '.backup',
        full_path + filename + '.bck',
        full_path + filename + '.bakup',
        full_path + filename_without_ext + '.saved',
        full_path + filename_without_ext + '.bac',
        full_path + filename_without_ext + '.back',
        full_path + filename_without_ext + '.bck',
        full_path + filename_without_ext + '.bakup',
        full_path + '_' + filename,
        full_path + '%20' + filename,
        full_path + filename + '.nsx',
        full_path + filename + '.cs',
        full_path + filename + '.csproj',
        full_path + filename + '.vb',
        full_path + filename + '.0',
        full_path + filename + '.1',
        full_path + filename + '.2',
        full_path + filename + '.7z',
        full_path + filename + '.ar',
        full_path + filename + '.arc',
        full_path + filename + '.bz2',
        full_path + filename + '.cbz',
        full_path + filename + '.ear',
        full_path + filename + '.exe',
        full_path + filename + '.gz',
        full_path + filename + '.inc',
        full_path + filename + '.jar',
        full_path + filename + '.lst',
        full_path + filename + '.lzma',
        full_path + filename + '.war',
        full_path + filename + '.wim',
        full_path + filename + '.xz',
        full_path + '.~lock.' + filename + '%23',
        full_path + '.~' + filename,
        full_path + '~%24' + filename,
        full_path + filename_without_ext + '.1',
        full_path + filename_without_ext + '.7z',
        full_path + filename_without_ext + '.ar',
        full_path + filename_without_ext + '.bz2',
        full_path + filename_without_ext + '.cbz',
        full_path + filename_without_ext + '.ear',
        full_path + filename_without_ext + '.exe',
        full_path + filename_without_ext + '.gz',
        full_path + filename_without_ext + '.inc',
        full_path + filename_without_ext + '.include',
        full_path + filename_without_ext + '.jar',
        full_path + filename_without_ext + '.lzma',
    ]

    # LEVEL 4
    backup_testing_level4 = [
        site + file_path + '.tar',
        site + file_path + '.rar',
        site + file_path + '.zip',
        full_path + '~' + filename_without_ext + '.tmp',
        site + file_path + '.tar.7z',
        site + file_path + '.tar.bz2',
        site + file_path + '.tar.gz',
        site + file_path + '.tar.lzma',
        site + file_path + '.tar.xz',
        full_path + 'backup-' + filename,
        full_path + 'backup_' + filename,
        full_path + 'bak-' + filename,
        full_path + 'bak_' + filename,
        full_path + filename_without_ext + '-backup.' + filename_ext,
        full_path + filename_without_ext + '-bkp.' + filename_ext,
        full_path + filename_without_ext + '.tar',
        full_path + filename_without_ext + '.rar',
        full_path + filename_without_ext + '.zip',
        full_path + filename_without_ext + '.tar.7z',
        full_path + filename_without_ext + '.tar.bz2',
        full_path + filename_without_ext + '.tar.gz',
        full_path + filename_without_ext + '.tar.lzma',
        full_path + filename_without_ext + '.tar.xz',
        full_path + filename_without_ext + '.sql.gz',
        full_path + filename_without_ext + '.bak.sql',
        full_path + filename_without_ext + '.bak.sql.gz',
        full_path + filename_without_ext + '.bak.sql.bz2',
        full_path + filename_without_ext + '.bak.sql.tar.gz',
        site + file_path + '.',  # CVE-2017-12616
        site + file_path + '::$DATA',  # CVE-2017-12616
        full_path + filename_without_ext + '1',
        full_path + filename_without_ext + '1.' + filename_ext,
        full_path + filename_without_ext + '_backup',
        full_path + filename_without_ext + '_backup' + filename_ext,
        full_path + filename_without_ext + '_bak',
        full_path + filename_without_ext + '_bak' + filename_ext,
        full_path + filename_without_ext + '_old',
        full_path + filename_without_ext + '_old' + filename_ext,
        full_path + filename_without_ext + 'bak',
        full_path + filename_without_ext + 'inc',
        full_path + filename_without_ext + 'old',
    ]

    # LEVEL 5
    backup_testing_level5 = [
        site + '/.git/HEAD',
        full_path + '.git/HEAD',
        site + '/.git/index',
        full_path + '.git/index',
        site + '/.git/config',
        full_path + '.git/config',
        site + '/.gitignore',
        full_path + '.gitignore',
        site + '/.git-credentials',
        full_path + '.git-credentials',
        site + '/.bzr/README',
        full_path + '.bzr/README',
        site + '/.bzr/checkout/dirstate',
        full_path + '.bzr/checkout/dirstate',
        site + '/.hg/requires',
        full_path + '.hg/requires',
        site + '/.hg/store/fncache',
        full_path + '.hg/store/fncache',
        site + '/.svn/entries',
        full_path + '.svn/entries',
        site + '/.svn/all-wcprops',
        full_path + '.svn/all-wcprops',
        full_path + '.svn/wc.db',
        site + '/.svn/wc.db',
        site + '/.svnignore',
        full_path + '.svnignore',
        site + '/CVS/Entries',
        full_path + 'CVS/Entries',
        site + '/.cvsignore',
        full_path + '.cvsignore',
        site + '/.idea/misc.xml',
        full_path + '.idea/misc.xml',
        site + '/.idea/workspace.xml',
        full_path + '.idea/workspace.xml',
        site + '/.DS_Store',
        full_path + '.DS_Store',
        site + '/composer.lock',
        full_path + 'composer.lock'
    ]

    testing_level = str(testing_level)

    available_levels = ['1', '2', '3', '4', '5']
    # Check is requested testing_level is within available levels.
    # If not within available levels, choose highest level.
    if (testing_level not in available_levels):
        testing_level = '5'

    if (testing_level == '1'):
        backup_testing_checks = backup_testing_level1
    if (testing_level == '2'):
        backup_testing_checks = backup_testing_level1 + \
            backup_testing_level2
    if (testing_level == '3'):
        backup_testing_checks = backup_testing_level1 + \
            backup_testing_level2 + \
            backup_testing_level3
    if (testing_level == '4'):
        backup_testing_checks = backup_testing_level1 + \
            backup_testing_level2 + \
            backup_testing_level3 + \
            backup_testing_level4
    if (testing_level == '5'):
        backup_testing_checks = backup_testing_level1 + \
            backup_testing_level2 + \
            backup_testing_level3 + \
            backup_testing_level4 + \
            backup_testing_level5
    if (dvcs_test is True):
        backup_testing_checks = backup_testing_level5

    backup_testing_checks = sorted(list(set(backup_testing_checks)))
    return(backup_testing_checks)