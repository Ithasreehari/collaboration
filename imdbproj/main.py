from db_utils import (
    create_and_load_table, view_all_movies, search_movie_by_name, delete_movie_by_title
)
from data_analysis import (
    show_top_10_movies, plot_top_10_movies, plot_revenue_distribution,
    plot_budget_vs_revenue, plot_runtime_by_vote, export_to_csv
)

def menu():
    create_and_load_table()

    while True:
        print("\n TMDB Movie Dataset CLI Menu")
        print("1. View All Movies")
        print("2. Search by Movie Name")
        print("3. Delete Movie by Title")
        print("4. Show Top 10 Movies by Rating")
        print("5. Plot: Top 10 Movies by Rating")
        print("6. Plot: Revenue Distribution")
        print("7. Plot: Budget vs Revenue")
        print("8. Plot: Average Runtime by Vote Bucket")
        print("9. Export Data to CSV")
        print("10. Exit")

        choice = input("Enter Your Choice: ")

        if choice == '1':
            print(view_all_movies())
        elif choice == '2':
            name = input("Enter Movie Name: ")
            print(search_movie_by_name(name))
        elif choice == '3':
            title = input("Enter Movie Title to Delete: ")
            delete_movie_by_title(title)
            print(f"✅ Movie '{title}' deleted successfully!")
        elif choice == '4':
            show_top_10_movies()
        elif choice == '5':
            plot_top_10_movies()
        elif choice == '6':
            plot_revenue_distribution()
        elif choice == '7':
            plot_budget_vs_revenue()
        elif choice == '8':
            plot_runtime_by_vote()
        elif choice == '9':
            export_to_csv()
        elif choice == '10':
            print("👋 Exiting... Bye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
