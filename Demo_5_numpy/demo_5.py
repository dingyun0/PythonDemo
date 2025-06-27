# NumPy 数据处理 Demo
import numpy as np

def analyze_sales_data(sales):
    # 将列表转换为 NumPy 数组
    sales_array = np.array(sales)
    
    # 基本统计
    mean_sales = np.mean(sales_array)
    max_sales = np.max(sales_array)
    min_sales = np.min(sales_array)
    
    # 增长率计算
    growth_rates = np.diff(sales_array) / sales_array[:-1] * 100
    
    # 返回结果
    return {
        "mean": mean_sales,
        "max": max_sales,
        "min": min_sales,
        "growth_rates": growth_rates.tolist()
    }

def main():
    # 模拟月度销售数据
    monthly_sales = [1200, 1500, 1300, 1800, 2000]
    
    # 分析数据
    stats = analyze_sales_data(monthly_sales)
    
    # 输出结果
    print("销售数据分析:")
    print(f"平均销售额: {stats['mean']:.2f}")
    print(f"最高销售额: {stats['max']:.2f}")
    print(f"最低销售额: {stats['min']:.2f}")
    print("月度增长率 (%):", [f"{rate:.2f}" for rate in stats['growth_rates']])

if __name__ == "__main__":
    main()