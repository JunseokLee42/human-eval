import json

class HumanEval:
    def __init__(self, lines):
        self.lines = lines
        self.problems = {
            "task_id": "dummy",
            "prompt": "dummy",
            "entry_point": "dummy",
            "canonical_solution": "dummy",
            "test": "dummy",
        }
        self.samples = {
            "task_id": "dummy",
            "completion": "dummy"
        }
        self.idx = 0

    def fetch_id(self, start: int):
        self.problems["task_id"] = 'HumanEval/{start}'.format(start=start)
    
    def fetch_prompt(self):
        prompt = ''
        for i, line in enumerate(self.lines):
            if (line != '\n'):
                prompt += line
                self.idx += 1
            else:
                prompt += '\n'
                self.idx += 1
                break
        self.problems["prompt"] = prompt

    def fetch_entry(self):
        entry_point = ''
        temp = list(self.lines[self.idx])[:-1]

        for item in temp:
            entry_point += item
        temp.clear
        self.problems["entry_point"] = entry_point
        self.idx += 1
    
    def fetch_canonical(self):
        canonical = ''
        while (self.lines[self.idx] != '\n'):
            canonical += self.lines[self.idx]
            self.idx += 1
        canonical += '\n'
        self.idx += 1
        self.problems["canonical_solution"] = canonical
    
    def fetch_test(self):
        test = ''
        while (self.idx != len(self.lines)):
            test += self.lines[self.idx]
            self.idx += 1
        self.problems["test"] = test
    
    def fetch_samples(self):
        self.samples["task_id"] = self.problems["task_id"]
        self.samples["completion"] = self.problems["canonical_solution"]

    def make_problems(self, file_path: str):
        with open(file_path, 'w') as f:
            json.dump(self.problems, f, ensure_ascii=False)

    def make_samples(self, file_path: str):
        with open(file_path, 'w') as f:
            json.dump(self.samples, f, ensure_ascii=False)


def main(lines: list):
    a = HumanEval(lines)
    # renew start parameter
    a.fetch_id(start=164)
    a.fetch_prompt()
    a.fetch_entry()
    a.fetch_canonical()
    a.fetch_test()
    a.fetch_samples()
    problems = './data/problems.json'
    samples = './data/samples.json'
    a.make_problems(problems)
    a.make_samples(samples)

if __name__ == "__main__":
    # preprocessing
    file = open('./input.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    # convert " into \"
    for idx, line in enumerate(lines):
        temp = line
        lines[idx] = temp
    
    # add \n\n to last line
    lines[-1] += '\n\n'

    main(lines)
