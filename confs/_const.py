
# https://github.com/tsuyoshicho/vim-efm-langserver-settings
TOOLS = {
    'buf': {'buf.yaml'},
    'eslint': {'.eslintrc.js', '.eslintrc.yaml', '.eslintrc.yml', '.eslintrc.json'},
    'flake8': {'.flake8'},
    'htmllint': {'.htmllintrc'},
    'isort': {'.isort.cfg'},
    'markdownlint': {'.markdownlint.json', '.markdownlint.yaml', '.markdownlint.yml', '.markdownlintrc'},
    'mypy': {'.mypy.ini', 'mypy.ini'},
    'nvcheck': {'dict.yml'},
    'prettier': {'.prettierrc.js'},
    'pydocstyle': {'pydocstyle', 'pydocstyle.ini', 'pydocstylerc', 'pydocstylerc.ini'},
    'pylint': {'pylintrc', '.pylintrc'},
    'redpen': {'redpen-conf.xml'},
    'rstcheck': {'.rstcheck.cfg', '.rstcheck.ini'},
    'rubocop': {'.rubocop.yml'},
    'rufo': {'.rufo'},
    'shellcheck': {'.shellcheckrc'},
    'stylelint': {'.stylelintrc.json'},
    'textlint': {'.textlintrc', '.textlintrc.js', '.textlintrc.json', '.textlintrc.yaml', '.textlintrc.yml'},
    'vale': {'.vale.ini'},
    'yamllint': {'.yamllint', '.yamllint.yaml', '.yamllint.yml'},
}

FILES = {}
for tool, files in TOOLS.items():
    for file in files:
        FILES[file] = tool
