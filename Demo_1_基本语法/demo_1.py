#基础语法与数据结构
def analyze_scores(scores):
    if not scores:
        return {
            "average": 0, "max": 0, "min": 0, "passed": 0
        }
    
    average = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)
    # 列表推导式
    passed=len([score for score in scores if score>=60])

    return {
        "average": round(average, 2),
        "max": max_score,
        "min": min_score,
        "passed": passed
    }

def main():
    students = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 58]
    # 字典推导式
    student_scores={
        name:score for name,score in zip(students,scores)
    }
    # 去重
    unique_scores=set(scores)

    stats=analyze_scores(scores)

    print("学生成绩字典:", student_scores)
    print("唯一成绩集合:", unique_scores)
    print("成绩统计:", stats)
    print("--------------------------------")
    print(student_scores.items())
    for name,score in student_scores.items():
        print(f"{name}的成绩是{score}")
        # 条件语句 xx if else xx if  else
        grade="优秀" if score>90 else "及格" if score>60 else "不及格"
        print(f"{name} 的成绩: {score}, 等级: {grade}")


if __name__ == "__main__":
    main()