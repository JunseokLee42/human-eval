# Introduction
This repo is about creating a json file based on the format of `HumanEval.jsonl` developed by members in openai.

## How to Create Json
1. Write texts based on the format of `HumanEval.jsonl`. 

2. Renew the parameter of fetch_id function before executing `printing.py`.

3. Execute `printing.py`
    then you could see a change in `example.json`.
    
4. Add `example.json` to `HumanEval.jsonl`.  

### Tip
It would be convenient to make the change to `example.json` rather than the start parameter.

After executing `printing.py`, it is recommended to modify the part corresponding to importing modules or functions in `input.txt` like the below:

    from module_name import function_name\n\n
    import function_name as alias_name\n\n
    \ndef.

## Cautions
1. The files, `input.txt` and `printing.py` should be located on the same directory.

2. It might occur errors if the annotation includes in some escape sequences like '\n\n'.

## Reference
https://github.com/openai/human-eval
