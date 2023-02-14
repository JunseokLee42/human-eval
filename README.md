# 코드로 어떤 일을 하고 싶은지, 혹은 코드를 실행하면 어떤 일이 일어나는지에 대한 설명이 없음
# 사용방법  
1. input.txt에 Humaneval.json의 형식에 맞춰 텍스트를 입력합니다.  
2. fetch_id function의 start를 갱신합니다.  
3. printing.py를 실행합니다.  
4. example.json 파일을 HumanEval.jsonl에 붙여 넣습니다.  
Tip!  
start 수정 안 하고 example.json에서 따로 수정해도 됩니다. 
printing.py 실행 후 통일성을 위해 from module_name import function_name\n\n, import function_name as alias_name\n\n, \ndef으로 수정하는 걸 추천드립니다.
# 주의사항  
1. input.txt와 printing.py가 같은 디렉토리 상에 위치해야 합니다.  
2. input.txt의 annotation에서 '\n\n' 있으면 에러 뜹니다.    
3. 간혹가다 Indexerror 나오면 '\n' 혹은 '\t'때문에 발생한 에러일 수 있으니, 지웠다가 다시 만들어보세요.  
# 출처
https://github.com/openai/human-eval
