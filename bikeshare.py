import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
            print('Select the name of the city to analyze: Chicago, New York City, Washington')
            city=input().lower()
            if city == 'chicago' or city == 'new york city' or city == 'washington' :
                break
            else:
                print('Please enter a valid city\n')

    # Get user input for month (all, january, february, ... , june)
    while True:
            print('Select the name of the month to filter by (January to June), or "all" to apply no month filter')
            month=input().lower()
            if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june':
                break
            elif month == 'all':
                break
            else:
                print('\nPlease enter a valid month. Remember, write the month with letters')

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
            print('Select the name of the day to filter by, or "all" to apply no month filter')
            day=input().lower()
            if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday':
                break
            elif day == 'all':
                break
            else:
                print('\nPlease enter a valid day. Remember, write the day with letters')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df



def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    popular_month = df['month'].mode()[0]
    f_popular_month=df['month'].value_counts().tolist()
    f_popular_month=f_popular_month[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    popular_month = months[popular_month-1]
    if month == 'all':
        print('The most common month:', popular_month, '// Count:', f_popular_month)
    else:
        print('Filtered month:', popular_month, '// Count:', f_popular_month)
    # Display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    f_popular_day=df['day_of_week'].value_counts().tolist()
    f_popular_day=f_popular_day[0]
    if day == 'all':
        print('The most common day of week:', popular_day, '// Count:', f_popular_day)
    else:
        print('Filtered day:', popular_day, '// Count:', f_popular_day)

    # Display the most common start hour
    popular_start_hour = df['start_hour'].mode()[0]
    f_popular_start_hour=df['start_hour'].value_counts().tolist()
    f_popular_start_hour=f_popular_start_hour[0]
    print('The most common start hour:', popular_start_hour, '// Count:', f_popular_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    #Calculate the most popular start station
    p_s_s = df['Start Station'].mode()[0]
    f_p_s_s = df['Start Station'].value_counts().tolist()
    #Count the frequency of the most popular start station
    f_p_s_s = f_p_s_s[0]
    print('The most most commonly used start station:', p_s_s, '// Count:', f_p_s_s)

    # Display most commonly used end station
    #Calculate the most popular end station
    p_e_s = df['End Station'].mode()[0]
    #Count the frequency of the most popular end station
    f_p_e_s = df['End Station'].value_counts().tolist()
    f_p_e_s = f_p_e_s[0]
    print('The most most commonly used end station:', p_e_s, '// Count:', f_p_e_s)

    # Display most frequent combination of start station and end station trip
    #Calculate the most popular combination
    df['station_combination'] = df['Start Station'] + '-' + df['End Station']
    p_c =df['station_combination'].mode()[0]
    f_p_c = df['station_combination'].value_counts().tolist()
    #Count the frequency of the most popular combination
    f_p_c = f_popular_combination[0]
    print('The most frequent combination of start station and end station trip:', p_c, '// Count:', f_p_c)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel = df['Trip Duration'].sum()
    total_travel_d = total_travel // (3600 * 24)
    total_travel = total_travel % (3600 * 24)
    total_travel_h = total_travel // 3600
    total_travel %= 3600
    total_travel_m = total_travel // 60
    total_travel %= 60
    total_travel_s = total_travel
    print('The total travel time: Days:{} Hours:{} Minutes:{} Seconds:{}'.format(total_travel_d,total_travel_h,total_travel_m,total_travel_s))
    #print(total_travel)

    # Display mean travel time
    mean_travel = df['Trip Duration'].mean()
    mean_travel_h = mean_travel // 3600
    mean_travel %= 3600
    mean_travel_m = mean_travel // 60
    mean_travel %= 60
    mean_travel_s = mean_travel
    print('The mean travel time: Hours:{} Minutes:{} Seconds:{}'.format(int(mean_travel_h),int(mean_travel_m),int(mean_travel_s)))
    #print(mean_travel)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:')
    print (user_types.to_string())
    # Display counts of gender
    if city == 'new york city' or city == 'chicago':
        gender_types = df['Gender'].value_counts()
        print('\nCounts of gender types:')
        print(gender_types.to_string())
        # Display earliest, most recent, and most common year of birth
        e_year = int(df['Birth Year'].min())
        f_e_year = df[df['Birth Year'] == e_year].count()
        f_e_year = f_e_year[0]
        print('\nEarliest year of birth:', e_year, '// Count:', f_e_year)
        mr_year = int(df['Birth Year'].max())
        f_mr_year = df[df['Birth Year'] == mr_year].count()
        f_mr_year = f_mr_year[0]
        print('Most recent year of birth:', mr_year, '// Count:', f_mr_year)
        mc_year = df['Birth Year'].mode()[0]
        f_mc_year = df['Birth Year'].value_counts().tolist()
        f_mc_year = f_mc_year[0]
        print('Most common year of birth:', int(mc_year),'// Count:', f_mc_year)
    else:
        print('\nNo gender data available for {}'.format(city.title()))
        print('No birth data available for {}'.format(city.title()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(city):
    """Shows raw data if the user wants to."""
    raw = input('\nWould you like to see 5 lines of raw data? Enter "yes" or "no".\n')
    rd = pd.read_csv(CITY_DATA[city]) #raw data
    count = 0
    index = rd.index
    n_rows = len(index)
    print(n_rows)
    while True:
        if raw.lower() == 'yes':
            count += 5
            if count <= n_rows:
                rd_five=rd.loc[(count-5):count,'Start Time':]
                print(rd_five)
                raw = input('\nWould you like to see the next 5 lines of raw data? Enter "yes" or "no".\n')
            else:
                print('\nNo more data available.\n')
                break
        elif raw.lower() == 'no':
            break
        else:
            print('Please, introduce a correct answer')
            raw = input()
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(city)

        restart = input('\nWould you like to restart? Enter "yes" to restart.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
