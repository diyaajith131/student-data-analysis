import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Load the dataset
    print("Loading dataset...")
    try:
        df = pd.read_csv('students.csv')
    except FileNotFoundError:
        print("Error: 'students.csv' not found.")
        return

    # Display the first few rows of data
    print("\n--- First Few Rows ---")
    print(df.head())
    
    # Generate statistical summaries of the dataset
    print("\n--- Statistical Summaries ---")
    print(df.describe())
    
    # Calculate the average marks for each student
    df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)
    print("\n--- Data with Average Marks ---")
    print(df[['Name', 'Math', 'Science', 'English', 'Average']])
    
    # Identify the top-performing student
    top_student = df.loc[df['Average'].idxmax()]
    print("\n--- Top Performing Student ---")
    print(f"Name: {top_student['Name']}, Average Mark: {top_student['Average']:.2f}")
    
    # Find subject-wise toppers
    print("\n--- Subject-wise Toppers ---")
    math_topper = df.loc[df['Math'].idxmax()]
    science_topper = df.loc[df['Science'].idxmax()]
    english_topper = df.loc[df['English'].idxmax()]
    
    print(f"Math:    {math_topper['Name']} ({math_topper['Math']})")
    print(f"Science: {science_topper['Name']} ({science_topper['Science']})")
    print(f"English: {english_topper['Name']} ({english_topper['English']})")
    
    # Setting seaborn style
    sns.set_theme(style="whitegrid")
    
    # Visualize student marks using bar charts
    print("\nGenerating visualizations...")
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Name', y='Average', hue='Name', data=df, palette='viridis', legend=False)
    plt.title('Average Marks of Students')
    plt.ylabel('Average Mark')
    plt.xlabel('Student Name')
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig('student_marks_bar.png')
    plt.close()
    print(" -> Saved 'student_marks_bar.png'")
    
    # Create a correlation heatmap for subject scores
    plt.figure(figsize=(6, 5))
    corr_matrix = df[['Math', 'Science', 'English']].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt=".2f")
    plt.title('Correlation Heatmap of Subject Scores')
    plt.tight_layout()
    plt.savefig('correlation_heatmap.png')
    plt.close()
    print(" -> Saved 'correlation_heatmap.png'")
    
    # Compare performance by gender
    plt.figure(figsize=(8, 6))
    sns.barplot(x='Gender', y='Average', hue='Gender', data=df, palette='Set2', errorbar='sd', capsize=0.1)
    
    # Add individual points to show distribution
    sns.stripplot(x='Gender', y='Average', data=df, color='black', alpha=0.5, jitter=True)
    
    plt.title('Average Performance Comparison by Gender')
    plt.ylabel('Average Mark')
    plt.xlabel('Gender')
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig('gender_comparison.png')
    plt.close()
    print(" -> Saved 'gender_comparison.png'")
    
    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()
