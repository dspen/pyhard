from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.");
print("If you don't want that, hit CTRL-C (^C).");
print("If you do want that hit RETURN");

input("?");

print("Opening the file...");
target = open(filename, 'w');

print("Truncating the file. Goodbye!");
target.truncate();

print("Input 3 lines.");
line1 = input("line1: ");
line2 = input("line2: ");
line3 = input("line3: ");

print("Writing these lines to file");
target.write(f"{line1}\n{line2}\n{line3}");
# target.write("\n");
# target.write(line2);
# target.write("\n");
# target.write(line3);
# target.write("\n");

print("Now closing");
target.close();
