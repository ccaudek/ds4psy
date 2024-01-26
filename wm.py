from colorama import Fore
def print_import(import_line):
    if len(import_line.strip()) > 1:
        parts = [p for p in import_line.split(" ") if p]
        if parts[0] == 'import':
            module = parts[1]
            alias = parts[3]
            msg = Fore.GREEN + 'import' \
                + Fore.BLUE + f" {module} " \
                + Fore.GREEN + "as" \
                + Fore.BLUE + f" {alias}"
        elif parts[0] == 'from':
            module = parts[1]
            submodule = parts[3]
            alias = parts[5]
            msg = Fore.GREEN + 'from' \
                + Fore.BLUE + f" {module} "\
                + Fore.GREEN + 'import' \
                + Fore.BLUE + f" {submodule} " \
                + Fore.GREEN + "as" \
                + Fore.BLUE + f" {alias}"
        print(msg)

from watermark import watermark
print(Fore.RED + f"Watermark:\n{'-'* 10}")
print(Fore.BLUE + watermark())
print(Fore.BLUE + watermark(iversions=True, globals_=globals()))
