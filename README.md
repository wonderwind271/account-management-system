# account-management-system
An account management system written in python.



## environment setup

1. Install python
2. A full list of the python package required is listed in "requirements.txt". Run command

```shell
pip install -r requirements.txt
```

​	in terminal to install these packages, then 

```shell
python main.py
```

​	to start the account management system.




## release message
### alpha release(version 0.3)

- Complete the basic function of this account management system, i.e., add, delete, query(list), and sum. 
- has a built-in manual with command `help`
- query or sum a given range's data, for example, on certain days or methods.
  - `sum item shopping lunch` : sum the price of all records whose field of "item" is "shopping" or "lunch"
  - `list 2 4` : list records with index 2 and 4
  - `list` : list all records
  - `sum` : sum the price of all records
  - `add/del` : add/delete a record. You'll be prompted to give informations
- in `sum` and `list` command, you need to use "_" to replace space.
- the index start from 0



## features

- [ ] visualize a given part of records within all records
- [ ] auto-correct for slight input mistake
- [ ] regular expression support for some of the commands
