import json

class HumanEval:
    def __init__(self, lines):
        self.lines = lines
        self.humaneval = {
            "task_id": "dummy",
            "prompt": "dummy",
            "entry_point": "dummy",
            "canonical_solution": "dummy",
            "test": "dummy"
        }
        self.idx = 0

    def fetch_id(self, start: int):
        self.humaneval["task_id"] = 'HumanEval/{start}'.format(start=start)
    
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
        self.humaneval["prompt"] = prompt

    def fetch_entry(self):
        entry_point = ''
        temp = list(self.lines[self.idx])[:-1]

        for item in temp:
            entry_point += item
        temp.clear
        self.humaneval["entry_point"] = entry_point
        self.idx += 1
    
    def fetch_canonical(self):
        canonical = ''
        while (self.lines[self.idx] != '\n'):
            canonical += self.lines[self.idx]
            self.idx += 1
        canonical += '\n'
        self.idx += 1
        self.humaneval["canonical_solution"] = canonical
    
    def fetch_test(self):
        test = ''
        while (self.idx != len(self.lines)):
            test += self.lines[self.idx]
            self.idx += 1
        self.humaneval["test"] = test
    
    def make_json(self, file_path: str):
        with open(file_path, 'w') as f:
            json.dump(self.humaneval, f, ensure_ascii=False)

def main(lines: list):
    a = HumanEval(lines)
    # 숫자값을 갱신해줘야 합니다.
    a.fetch_id(start=280)
    a.fetch_prompt()
    a.fetch_entry()
    a.fetch_canonical()
    a.fetch_test()
    file_path = './data/example.json'
    a.make_json(file_path)

if __name__ == "__main__":
    # 전처리 
    file = open('./input.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    # "를 \" 으로 수정
    for idx, line in enumerate(lines):
        temp = line
        lines[idx] = temp
    
    # 마지막 줄 \n\n 추가
    lines[-1] += '\n\n'

    main(lines)