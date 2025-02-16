import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. 读取 CSV 文件
def load_csv(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在: {file_path}")
    return pd.read_csv(file_path)

# 2. 数据清洗
def clean_data(df):
    # 去除重复行
    df = df.drop_duplicates()
    # 填充缺失值
    df = df.fillna("")
    # 转换日期列为 datetime 类型
    df["date"] = pd.to_datetime(df["date"])
    return df

# 3. 数据筛选
def filter_data(df, year=None, author=None):
    if year:
        df = df[df["date"].dt.year == year]
    if author:
        df = df[df["author"] == author]
    return df

# 4. 数据统计
def analyze_data(df):
    # 每个作者的提交次数
    author_counts = df["author"].value_counts()
    # 每日提交数量
    daily_commits = df.groupby(df["date"].dt.date).size()
    # 每个作者的代码变更量
    author_stats = df.groupby("author")[["insertions", "deletions"]].sum()
    return author_counts, daily_commits, author_stats

# 5. 数据可视化
def visualize_data(author_counts, daily_commits):
    # 绘制每日提交数量图
    plt.figure(figsize=(12, 6))
    daily_commits.plot(kind="line", marker="o")
    plt.title("Daily Commit Frequency")
    plt.xlabel("Date")
    plt.ylabel("Number of Commits")
    plt.grid(True)
    plt.show()

    # 绘制作者提交数量柱状图
    author_counts.plot(kind="bar")
    plt.title("Commits per Author")
    plt.xlabel("Author")
    plt.ylabel("Number of Commits")
    plt.show()

# 6. 导出处理后的数据
def save_cleaned_data(df, output_file):
    df.to_csv(output_file, index=False)
    print(f"处理后的数据已保存到 {output_file}")

# 主程序
if __name__ == "__main__":
    # 指定输入和输出文件路径
    input_csv = r"C:\Users\93718\Desktop\flask_commits.csv"
    output_csv = r"C:\Users\93718\Desktop\flask_commits_cleaned.csv"

    # 1. 加载数据
    print("加载 CSV 文件...")
    df = load_csv(input_csv)

    # 2. 数据清洗
    print("清洗数据...")
    df = clean_data(df)

    # 3. 数据筛选（可选）
    print("筛选数据...")
    df = filter_data(df, year=2024)  # 例如筛选 2024 年的提交

    # 4. 数据统计
    print("分析数据...")
    author_counts, daily_commits, author_stats = analyze_data(df)

    # 5. 数据可视化
    print("生成可视化图表...")
    visualize_data(author_counts, daily_commits)

    # 6. 导出处理后的数据
    print("保存处理后的数据...")
    save_cleaned_data(df, output_csv)

    # 打印统计结果
    print("\n作者提交次数统计：")
    print(author_counts)
    print("\n每日提交数量统计：")
    print(daily_commits)
    print("\n作者代码变更量统计：")
    print(author_stats)