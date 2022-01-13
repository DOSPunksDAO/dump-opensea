# Dump-OpenSea
<pre>
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
</pre>

A simple Python script to **retrieve Owners/Holders of a whole NFT collection on ETH (OpenSea)**.

Coded by [GBE](https://github.com/gbe3hunna/) for the [DOS PUNKS DAO](https://github.com/DOSPunksDAO) to thank [@maxcapacity](https://twitter.com/maxcapacity) and [@greencrosslive](https://twitter.com/greencrosslive) for all their effort in buidling such a strong #DOSLIFE.

This script can be useful for any NFT project staff to Snapshot the actual holders

_
                                              
Developed by DOS Punks DAO for the NFT Community.   

-

This software is distributed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)

- 


# Installation

#### 1)  ```git clone https://github.com/DOSPunksDAO/dump-opensea.git```

#### 2)  ```cd dump-opensea```

#### 3)  ```pip install -r requirements.txt -U```

# Other requirements

- OpenSea Collection Path/Slug 
  - `Example: https://opensea.io/collection/dos-punks` --> `dos-punks`
- Contract Address
  - `Example: https://opensea.io/collection/dos-punks` --> `0x495f947276749ce646f68ac8c248420045cb7b5e`
- Total Minted / Total Collection Tokens
  - `Example: https://opensea.io/collection/dos-punks` --> `497`
- Moralis Web3 API Key (FREE)
  - https://admin.moralis.io/web3Api


# Usage

#### Running with user input
```
python os-snapshots.py
```
- Fill the inputs with your data
- Filter is `OPTIONAL` (Example: 2 If you want to filter by holders with 2 or more tokens...)


#### Running with flags
```
-s, --slug / Slug
-c, --contract / Contract Address
-m, --minted / Total Minted - Total Collection Tokens
-k, --apikey / Moralis Web3 API Key
-f, --filter (OPTIONAL) / Filter by Tokens (2 If you want to filter by holders with 2 or more tokens...)
```
- Type ```python os-snapshots -h``` to get the available flags

# Results

- It will generate a JSON file inside `./snapshots` directory.
- Will follow the next Schema:
  - Wallet Address: Number of tokens

