import matplotlib.pyplot as plt
def plot_data(my_file):
    scatter_plot = None
    x = []
    y = []

    # Opening the file and read the coordinates
    with open(my_file, 'r') as file:
        # Skip the first line (header- x and y)
        next(file)

        for line in file:
            # Strip
            # whitespace(any character or series of characters that represent horizontal or vertical space in text)
            # and split the line by comma
            values = line.strip().split(',')

            if len(values) == 2:  # Ensure there are exactly 2 values
                try:
                    x_val = float(values[0])
                    y_val = float(values[1])
                    x.append(x_val)
                    y.append(y_val)
                except ValueError:
                    print(f"Could not convert values to float: {values}")
            else:
                print(f"Unexpected number of values: {values}")

    # Create the scatterplot
    scatter_plot = plt.figure()
    plt.scatter(x, y)

    # Add labels  to the plot and the title
    plt.xlabel('X Coordinates')
    plt.ylabel('Y Coordinates')
    plt.title('Scatterplot of X and Y Coordinates')

    # Style the plot style to grid (Optional)
    plt.grid()

    # Show the plot
    plt.show()

    return scatter_plot


# Render the plot data, thus x and y coordinates file
plot_data('C:/Users/MY PC/Downloads/x_y_coordinates.txt')