# 사용방법  
1. input.txt에 Humaneval.json의 형식에 맞춰 텍스트를 입력합니다.  
2. fetch_id function의 start를 갱신합니다.  
3. printing.py를 실행합니다.  
4. example.json 파일을 HumanEval.jsonl에 붙여 넣습니다.  
Tip!  
start 수정 안 하고 example.json에서 따로 수정해도 됩니다. 
# 주의사항  
1. input.txt와 printing.py가 같은 디렉토리 상에 위치해야 합니다.  
2. input.txt의 annotation에서 '\n\n' 있으면 에러 뜹니다.    
3. 간혹가다 Indexerror 나오면 '\n' 혹은 '\t'때문에 발생한 에러일 수 있으니, 지웠다가 다시 만들어보세요.  
# 출처
https://github.com/openai/human-eval
