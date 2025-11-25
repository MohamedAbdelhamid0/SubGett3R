def display_banner():
    banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ███████╗██╗   ██╗██████╗  ██████╗ ███████╗████████╗████████╗██████╗ ██████╗║
║   ██╔════╝██║   ██║██╔══██╗██╔════╝ ██╔════╝╚══██╔══╝╚══██╔══╝╚════██╗██╔══██║
║   ███████╗██║   ██║██████╔╝██║  ███╗█████╗     ██║      ██║    █████╔╝██████╔╝
║   ╚════██║██║   ██║██╔══██╗██║   ██║██╔══╝     ██║      ██║    ╚═══██╗██╔══██║
║   ███████║╚██████╔╝██████╔╝╚██████╔╝███████╗   ██║      ██║   ██████╔╝██║  ██║
║   ╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝      ╚═╝   ╚═════╝ ╚═╝  ╚═╝
║                                                                              ║
║                            Made by: @0xtkmo on Twitter                       ║
║                          MohamedAbdelhamid0 on Github                        ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

"""
    print(banner)

def run_passive_enumeration(requested_domain):
    print("")

def run_active_enumeration(requested_domain):
    print("")


if __name__ == "__main__":
    display_banner() 

    print("Welcome to Subgett3r! This tool is designed to help you enumerate subdomains efficiently.")
    print("Please follow the prompts to get started with your subdomain enumeration.")
    print("For more information, visit the project's GitHub repository. Remember to use this tool responsibly and ethically.\n")
    requested_domain= input("Enter your target domain to begin: ")
    # Further code for subdomain enumeration would go here
    print("Choose from the following options:")
    print("1. Basic Enumeration (passive)")
    print("2. Advanced Enumeration (active) **NOTE THAT ACTIVE ENUMERATION MAY TAKE LONGER AND MAY GENERATE MORE TRAFFIC**")
    while(True):
        user_selection = input("Enter 1 or 2 based on your preference: ")
        if user_selection == '1' or user_selection == '2':
            print("")
            break

        else:
            print("Invalid selection. Please choose either 1 or 2.")

    print(f"Starting enumeration for domain: {requested_domain} with option {user_selection}")

    if user_selection == '1':
        run_passive_enumeration(requested_domain)
    elif user_selection == '2':
        run_active_enumeration(requested_domain)




   
