import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load data
    df = pd.read_csv("adult.data.csv")

    # 1. Count of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with a Bachelor's degree
    total_people = df.shape[0]
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round((bachelors_count / total_people) * 100, 1)

    # 4. Percentage with advanced education earning >50K
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    adv_edu_df = df[df['education'].isin(advanced_education)]
    high_edu_rich = adv_edu_df[adv_edu_df['salary'] == '>50K']
    higher_education_rich = round((high_edu_rich.shape[0] / adv_edu_df.shape[0]) * 100, 1)

    # 5. Percentage without advanced education earning >50K
    low_edu_df = df[~df['education'].isin(advanced_education)]
    low_edu_rich = low_edu_df[low_edu_df['salary'] == '>50K']
    lower_education_rich = round((low_edu_rich.shape[0] / low_edu_df.shape[0]) * 100, 1)

    # 6. Minimum hours per week
    min_work_hours = df['hours-per-week'].min()

    # 7. % of people who work min hours and earn >50K
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = min_workers[min_workers['salary'] == '>50K']
    rich_percentage = round((rich_min_workers.shape[0] / min_workers.shape[0]) * 100, 1)

    # 8. Country with highest % of >50K earners
    country_counts = df['native-country'].value_counts()
    country_rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    rich_country_percentages = (country_rich_counts / country_counts) * 100
    highest_earning_country = rich_country_percentages.idxmax()
    highest_earning_country_percentage = round(rich_country_percentages.max(), 1)

    # 9. Most common occupation for those >50K in India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # Output (optional for debugging or display)
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours, "hours/week")
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India for >50K earners:", top_IN_occupation)

    # Return all results for testing
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
