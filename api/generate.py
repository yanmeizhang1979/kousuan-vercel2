import random
import json
from urllib.parse import parse_qs

def generate_questions(start, end, count, op_type):
    questions = []
    attempts = 0
    max_attempts = count * 20

    if op_type == "add":
        while len(questions) < count and attempts < max_attempts:
            a = random.randint(start, end)
            b = random.randint(start, end)
            s = a + b
            if s <= end:
                if random.random() < 0.3:
                    if random.choice([True, False]):
                        questions.append(f"（ ）＋ {b} = {s}")
                    else:
                        questions.append(f"{a} ＋（ ）= {s}")
                else:
                    questions.append(f"{a} ＋ {b} = _____")
            attempts += 1

    elif op_type == "sub":
        while len(questions) < count and attempts < max_attempts:
            a = random.randint(start, end)
            b = random.randint(start, a)
            diff = a - b
            if diff >= start:
                if random.random() < 0.3:
                    if random.choice([True, False]):
                        questions.append(f"（ ）－ {b} = {diff}")
                    else:
                        questions.append(f"{a} －（ ）= {diff}")
                else:
                    questions.append(f"{a} － {b} = _____")
            attempts += 1

    elif op_type == "mul":
        for _ in range(count):
            a = random.randint(max(1, start), end)
            b = random.randint(max(1, start), end)
            p = a * b
            if random.random() < 0.3:
                if random.choice([True, False]):
                    questions.append(f"（ ）× {b} = {p}")
                else:
                    questions.append(f"{a} ×（ ）= {p}")
            else:
                questions.append(f"{a} × {b} = _____")

    elif op_type == "div":
        for _ in range(count):
            divisor = random.randint(max(1, start), end)
            quotient = random.randint(1, max(1, end))
            dividend = divisor * quotient
            if random.random() < 0.3:
                if random.choice([True, False]):
                    questions.append(f"（ ）÷ {divisor} = {quotient}")
                else:
                    questions.append(f"{dividend} ÷（ ）= {quotient}")
            else:
                questions.append(f"{dividend} ÷ {divisor} = _____")

    elif op_type == "add_sub_mixed":
        add_ratio = 0.5
        for _ in range(count):
            if random.random() < add_ratio:
                a = random.randint(start, end)
                b = random.randint(start, end)
                s = a + b
                if s <= end:
                    if random.random() < 0.3:
                        if random.choice([True, False]):
                            questions.append(f"（ ）＋ {b} = {s}")
                        else:
                            questions.append(f"{a} ＋（ ）= {s}")
                    else:
                        questions.append(f"{a} ＋ {b} = _____")
            else:
                a = random.randint(start, end)
                b = random.randint(start, a)
                diff = a - b
                if diff >= start:
                    if random.random() < 0.3:
                        if random.choice([True, False]):
                            questions.append(f"（ ）－ {b} = {diff}")
                        else:
                            questions.append(f"{a} －（ ）= {diff}")
                    else:
                        questions.append(f"{a} － {b} = _____")

    elif op_type == "mul_div_mixed":
        mul_ratio = 0.5
        for _ in range(count):
            if random.random() < mul_ratio:
                a = random.randint(max(1, start), end)
                b = random.randint(max(1, start), end)
                p = a * b
                if random.random() < 0.3:
                    if random.choice([True, False]):
                        questions.append(f"（ ）× {b} = {p}")
                    else:
                        questions.append(f"{a} ×（ ）= {p}")
                else:
                    questions.append(f"{a} × {b} = _____")
            else:
                divisor = random.randint(max(1, start), end)
                quotient = random.randint(1, max(1, end))
                dividend = divisor * quotient
                if random.random() < 0.3:
                    if random.choice([True, False]):
                        questions.append(f"（ ）÷ {divisor} = {quotient}")
                    else:
                        questions.append(f"{dividend} ÷（ ）= {quotient}")
                else:
                    questions.append(f"{dividend} ÷ {divisor} = _____")

    # 补足数量
    while len(questions) < count:
        questions.append("1 ＋ 1 = _____")
    return questions[:count]

def handler(request):
    query = request.url.query or ""
    params = parse_qs(query)
    
    try:
        start = int(params.get('start', ['1'])[0])
        end = int(params.get('end', ['10'])[0])
        count = min(100, max(1, int(params.get('count', ['20'])[0])))
        op_type = params.get('op', ['add'])[0]
        
        questions = generate_questions(start, end, count, op_type)
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(questions, ensure_ascii=False)
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": f'["❌ 输入错误: {str(e)}"]'
        }
