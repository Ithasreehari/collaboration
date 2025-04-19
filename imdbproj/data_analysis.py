import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from db_utils import view_all_movies

# Top 10 movies
def show_top_10_movies():
    df = view_all_movies()
    top_10 = df.sort_values(by='vote_average', ascending=False).head(10)
    print("\n🎬 Top 10 Movies by Rating:\n")
    print(top_10[['title', 'vote_average']])
    return top_10

def plot_top_10_movies():
    top_10 = show_top_10_movies()
    plt.figure(figsize=(10,6))
    sns.barplot(x='vote_average', y='title', data=top_10, palette='rocket')
    plt.title('Top 10 Movies by Vote Average')
    plt.xlabel('Vote Average')
    plt.ylabel('Movie Title')
    plt.tight_layout()
    plt.show()

# Revenue distribution
def plot_revenue_distribution():
    df = view_all_movies()
    plt.figure(figsize=(10,6))
    sns.histplot(df['revenue'], bins=30, kde=True)
    plt.title('Revenue Distribution')
    plt.xlabel('Revenue')
    plt.tight_layout()
    plt.show()

# Budget vs Revenue
def plot_budget_vs_revenue():
    df = view_all_movies()
    plt.figure(figsize=(10,6))
    sns.scatterplot(data=df, x='budget', y='revenue')
    plt.title('Budget vs Revenue')
    plt.xlabel('Budget')
    plt.ylabel('Revenue')
    plt.tight_layout()
    plt.show()

# Average Runtime by Vote Bucket
def plot_runtime_by_vote():
    df = view_all_movies()
    df['vote_bucket'] = pd.cut(df['vote_average'], bins=[0,4,6,8,10], labels=['Low','Average','Good','Excellent'])
    plt.figure(figsize=(10,6))
    sns.barplot(data=df, x='vote_bucket', y='runtime', ci=None)
    plt.title('Average Runtime by Vote Bucket')
    plt.xlabel('Vote Category')
    plt.ylabel('Average Runtime')
    plt.tight_layout()
    plt.show()

# Export to CSV
def export_to_csv():
    df = view_all_movies()
    df.to_csv('movies_export.csv', index=False)
    print("\n✅ Data exported to 'movies_export.csv' successfully!")
