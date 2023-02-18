# Creating Problem Json as intended

## How to Create Json
1. Renew the parameter of fetch_id function before executing `printing.py`.

2. Write texts based on the format of `HumanEval.jsonl`. 

3. Execute `printing.py`
    then you could see changes in `problems.json` and `samples.json`.
    
4. Add them to `HumanEval.jsonl`.  

### Tip
After executing `printing.py`, it is recommended to modify the part corresponding to importing modules or functions in `input.txt` like the below:

    from module_name import function_name\n\n
    import function_name as alias_name\n\n
    \ndef

## Cautions
1. The files, `input.txt` and `printing.py` should be located in the same directory.

2. It might occur errors if the annotation includes in some escape sequences like '\n\n'.

## Reference
https://github.com/openai/human-eval
