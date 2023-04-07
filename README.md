As of March 2023, the [Codex](https://platform.openai.com/docs/guides/code) models are now deprecated. Please check out OpenAI's newer Chat models which are able to do many coding tasks with similar capability

# Creating Problem Jsonl as intended

This repo is about creating HumanEval.jsonl dataset easily.

HumanEval dataset are handwritten programming problems described in `2.2. HumanEval: Hand-Written Evaluation Set` section on the following paper.

Paper: "[Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374)".

## How to Create Json
1. Renew the parameter of fetch_id function before executing `printing.py`.

2. Write texts based on the format of `HumanEval.jsonl`. 

3. Execute `printing.py`
    then you could see changes in `problems.json` and `samples.json`.
    
4. Add `problem.json` to `HumanEval.jsonl`.

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
After executing `printing.py`, it is recommended to modify the part corresponding to importing modules or functions in `input.txt` in terms of unity as follows:

    from module_name import function_name\n\n
    import function_name as alias_name\n\n
    \ndef

## Cautions
1. Be sure the directory where the files, `input.txt` and `printing.py` are located in.

2. It might occur errors if the docstrings include in some escape sequences like '\n\n'.

## Reference
https://github.com/openai/human-eval
