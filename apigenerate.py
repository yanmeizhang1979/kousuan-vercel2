def generate_questions(start, end, count, op_type):
    questions = []
    attempts = 0
    max_attempts = count * 20

    if op_type == "add":
        # 加法逻辑不变
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
        # 减法逻辑不变
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
        # 乘法逻辑不变
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
        # 除法逻辑不变
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
        # 加减混合
        add_ratio = 0.5  # 50% 加法，50% 减法
        for _ in range(count):
            if random.random() < add_ratio:
                # 加法
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
                # 减法
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
        # 乘除混合
        mul_ratio = 0.5  # 50% 乘法，50% 除法
        for _ in range(count):
            if random.random() < mul_ratio:
                # 乘法
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
                # 除法
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
