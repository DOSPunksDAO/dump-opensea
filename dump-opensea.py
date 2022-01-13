# Import necessary libraries
import requests, argparse, json, sys, time
import math
from colorama import Fore, Back, Style, init as coloramaInit
from alive_progress import alive_bar as progressBar

# Initialize main vars
offset = 0
num = 0
totalOwned = 0
totalNfts = 0 
owners = {}
filteredOwners = {}

# Header
def showHeader():
    print(f'''{Fore.LIGHTBLUE_EX}
 ██████████   █████  █████ ██████   ██████ ███████████                     
░░███░░░░███ ░░███  ░░███ ░░██████ ██████ ░░███░░░░░███                    
 ░███   ░░███ ░███   ░███  ░███░█████░███  ░███    ░███                    
 ░███    ░███ ░███   ░███  ░███░░███ ░███  ░██████████                     
 ░███    ░███ ░███   ░███  ░███ ░░░  ░███  ░███░░░░░░                      
 ░███    ███  ░███   ░███  ░███      ░███  ░███                            
 ██████████   ░░████████   █████     █████ █████                           
░░░░░░░░░░     ░░░░░░░░   ░░░░░     ░░░░░ ░░░░░                            
                                                                           
                                                                           
                                                                           
    ███████                                   █████████                    
  ███░░░░░███                                ███░░░░░███                   
 ███     ░░███ ████████   ██████  ████████  ░███    ░░░   ██████   ██████  
░███      ░███░░███░░███ ███░░███░░███░░███ ░░█████████  ███░░███ ░░░░░███ 
░███      ░███ ░███ ░███░███████  ░███ ░███  ░░░░░░░░███░███████   ███████ 
░░███     ███  ░███ ░███░███░░░   ░███ ░███  ███    ░███░███░░░   ███░░███ 
 ░░░███████░   ░███████ ░░██████  ████ █████░░█████████ ░░██████ ░░████████
   ░░░░░░░     ░███░░░   ░░░░░░  ░░░░ ░░░░░  ░░░░░░░░░   ░░░░░░   ░░░░░░░░ 
               ░███                                                        
               █████                                                       
              ░░░░░                      - BROUGHT TO YOU BY DOS PUNKS DAO                         

                {Fore.WHITE}Created by: {Fore.LIGHTRED_EX}GBE#0001{Fore.WHITE} for DOS PUNKS DAO
    ''')
    
# Init with flags
def flagInit():
    # Parse Flags
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--slug", help="Slug Name")
    parser.add_argument("-c", "--contract", help="Contract Address")
    parser.add_argument("-m", "--minted", help="Total Minted")
    parser.add_argument("-k", "--apikey", help="API Key")
    parser.add_argument("-f", "--filter", help="Filter by Tokens (2 If you want to filter by holders with 2 or more tokens)")
    args = parser.parse_args()

    # Check if flags exists
    slug = args.slug
    contract = args.contract
    totalMinted = int(args.minted)
    apiKey = args.apikey
    tokenFilter = args.filter
    print("[] Slug: {}{}{}\n[] Contract Address: {}{}{}\n[] Total Minted: {}{}{}\n[] API Key: {}{}{} \n[] Filter: {}{}{}\n".format(
        Fore.YELLOW, args.slug, Fore.WHITE,
        Fore.YELLOW, args.contract, Fore.WHITE,
        Fore.YELLOW, args.minted, Fore.WHITE,
        Fore.YELLOW, args.apikey, Fore.WHITE,
        Fore.YELLOW, args.filter, Fore.WHITE)
    )
    return slug, contract, totalMinted, apiKey, tokenFilter    

# Init with user input
def inputInit():
    print(f"{Fore.YELLOW}[] Project Slug: {Style.RESET_ALL}", end="")
    slug = input().strip()
    print(f"{Fore.YELLOW}[] Contract Address: {Style.RESET_ALL}", end="")
    contract = input().strip()
    print(f"{Fore.YELLOW}[] Collection Total Tokens: {Style.RESET_ALL}", end="")
    totalMinted = input().strip()
    print(f"{Fore.YELLOW}[] Moralis API Key: {Style.RESET_ALL}", end="")
    apiKey = input().strip()
    print(f"{Fore.YELLOW}[] Filter owners ? (Y/N): {Style.RESET_ALL}", end="")
    tokenResponse = input().strip()
    if ((tokenResponse.lower()) == "y"):
        print(f"{Fore.YELLOW}[] Minimum number of tokens holding: {Style.RESET_ALL}", end="")
        tokenFilter = input().strip()
    else: tokenFilter = None
    return slug, contract, totalMinted, apiKey, tokenFilter

# Fatal Error --> Exit
def fatalError():
    print(f"\n{Fore.RED}An error has occurred. Please try again.\n")
    sys.exit()

# Retrieving owners from API's
def getOwners(slug, contract, pagination, tokenFilter, apiKey):
    # Iterate trough the pagination
    print(f'''\n{Fore.YELLOW}
        +------------------------------------------------------------+
        |              CHECKING HOLDERS. PLEASE WAIT...              |
        +------------------------------------------------------------+{Fore.WHITE}\n'''
    )
    try:
        with progressBar(int(pagination), bar='filling') as bar:
            for i in range(0,int(pagination)):
                offset = (i * 50)
                response = requests.get(f"https://api.opensea.io/api/v1/assets?order_direction=desc&offset={offset}&limit=50&collection={slug}").json()
                for asset in response['assets']:
                    global totalNfts, totalOwned, owners, num
                    totalNfts += 1
                    try: web3response = requests.get(f"https://deep-index.moralis.io/api/v2/nft/{contract}/{asset['token_id']}/owners?chain=eth&format=decimal", headers={'X-API-Key': apiKey}).json()
                    except: web3response = requests.get(f"https://deep-index.moralis.io/api/v2/nft/{contract}/{asset['token_id']}/owners?chain=eth&format=decimal", headers={'X-API-Key': apiKey}).json()
                    totalOwned += web3response['total']
                    for r in web3response['result']: 
                        if r['owner_of'] in owners: owners[r['owner_of']] += 1
                        else: owners[r['owner_of']] = 1
                    num += 1
                bar()
        if (tokenFilter not in (None, 0)): 
            print(f'\n\n{Fore.WHITE}[+] Filtered by holders with: {Fore.GREEN}{tokenFilter} or + Tokens{Fore.WHITE}')
            for _o in owners:
                if (int(owners[_o]) >= int(tokenFilter)): filteredOwners[_o] = owners[_o]
            owners = filteredOwners
    except: fatalError()

# Export to JSON
def exportJSON(slug):
    global totalNfts, totalOwned, owners
    outputFile = open(f'./snapshots/{slug}-owners.json', 'w')
    json.dump(owners, outputFile)
    time.sleep(1.5)
    print(f'''\n{Fore.YELLOW}
        +------------------------------------------------------------+
        |                  SNAPSHOT HAS BEEN TAKEN                   |
        +------------------------------------------------------------+\n
        {Fore.GREEN}     [+] Total NFTS: {Fore.WHITE}{totalNfts}{Fore.YELLOW}
        {Fore.GREEN}     [+] Total Owned: {Fore.WHITE}{totalOwned}{Fore.YELLOW}
        {Fore.GREEN}     [+] Total Owners: {Fore.WHITE}{len(owners)}{Fore.YELLOW}
        {Fore.GREEN}     [+] Exported File: {Fore.WHITE}./snapshots/{slug}-owners.json{Fore.YELLOW}\n\n'''
    )

# Main handle
def main():
    coloramaInit()
    showHeader()
    try: slug, contract, totalMinted, apiKey, tokenFilter = flagInit() #Init with flags
    except: slug, contract, totalMinted, apiKey, tokenFilter = inputInit() #Init with user input
    pagination = int(math.ceil((int(totalMinted)) / 50)) #Get pagination
    getOwners(slug, contract, pagination, tokenFilter, apiKey) #Main method
    exportJSON(slug) #Export results

#Start
main()