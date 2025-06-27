import pandas as pd

def process():
    data={
        "name": ["Alice", "Bob", "Charlie", "David"],
        "age": [25, 30, None, 28],
        "salary": [50000, 60000, 55000, None]
    }
    
    df=pd.DataFrame(data)
    print(df)
#      name   age   salary
# 0    Alice  25.0  50000.0
# 1      Bob  30.0  60000.0
# 2  Charlie   NaN  55000.0
# 3    David  28.0      NaN

# 数据清洗
    df['age'].fillna(df['age'].mean(),inplace=True)
    df['salary'].fillna(df['salary'].median(),inplace=True)
    print(df)
    # 过滤：年龄大于 25 的员工
    filtered_df = df[df["age"] > 25]
    
    # 聚合：计算平均薪资
    avg_salary = df["salary"].mean()
    return filtered_df, avg_salary
def main():
    # 处理数据
    filtered_df, avg_salary = process()
    
    # 输出结果
    print("年龄大于 25 的员工:")
    print(filtered_df)
    print(f"\n平均薪资: {avg_salary:.2f}")

if __name__ == "__main__":
    main()