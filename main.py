from demographic_data_analyzer import calculate_demographic_data

if __name__ == "__main__":
    results = calculate_demographic_data(print_data=True)

    print("\nResultados devueltos para testeo automático:")
    for key, value in results.items():
        print(f"{key}:\n{value}\n")
