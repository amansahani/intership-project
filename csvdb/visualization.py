import pandas as pd
import matplotlib.pyplot as plt
import os
# https://www.kaggle.com/datasets/rohithmahadevan/students-marksheet-dataset


def visualize(filename):
    data = pd.read_csv(os.path.join(f"{os.path.dirname(__file__)}", os.pardir, f"{filename}"))

    data['Average_Score'] = data[['Science', 'English', 'History', 'Maths']].mean(axis=1)

    overall_average = data['Average_Score'].mean()

    plt.figure(figsize=(10, 6))
    plt.bar(data['Name'], data['Average_Score'], color='skyblue', label='Average Score')
    plt.axhline(y=overall_average, color='r', linestyle='--', label=f'Overall Average: {overall_average:.2f}')
    plt.xlabel('Student Name')
    plt.ylabel('Average Score')
    plt.title('Average Scores for Students')
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()

    plt.show()


    gender_average = data.groupby('Gender')['Average_Score'].mean()


    age_average = data.groupby('Age')['Average_Score'].mean()


    subject_average = data[['Science', 'English', 'History', 'Maths']].mean()

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Gender-wise pie chart
    axes[0].pie(gender_average, labels=gender_average.index, autopct=lambda p: f'{p:.0f}', startangle=0)
    axes[0].set_title('Gender-wise Average Score')

    # Age-wise pie chart
    axes[1].pie(age_average, labels=age_average.index,autopct=lambda p: f'{p:.0f}', startangle=0)
    axes[1].set_title('Age-wise Average Score')

    # Subject-wise pie chart
    axes[2].pie(subject_average, labels=subject_average.index, autopct=lambda p: f'{p:.0f}', startangle=0)
    axes[2].set_title('Subject-wise Average Score')

    # Display the pie charts
    plt.tight_layout()
    plt.show()





