# Creating Problem Jsonl as intended

This repo is about creating HumanEval.jsonl dataset easily.

HumanEval dataset are handwritten programming problems.

## How to Create Json
1. Renew the parameter of fetch_id function before executing `printing.py`.

2. Write texts based on the format of `HumanEval.jsonl`. 

3. Execute `printing.py`
    then you could see changes in `problem.json` and `samples.json`.
    
4. Add them to `HumanEval.jsonl`.

## `input.txt` Example

    def add(a,b):
        """
        make a program which returns a plus b.
        """
    
    add
        return a+b
    
    def check(candidate):
        # Check some simple cases
        assert candidate(3,4) == 7
        assert candidate(10,11) == 21

### Tip
After executing `printing.py`, it is recommended to modify the part corresponding to importing modules or functions in `input.txt` in terms of unity on the following:

    from module_name import function_name\n\n
    import function_name as alias_name\n\n
    \ndef

## Cautions
1. Be sure the directory where the files, `input.txt` and `printing.py` are located in.

2. It might occur errors if the docstrings include in some escape sequences like '\n\n'.

## Reference
https://github.com/openai/human-eval
