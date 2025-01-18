# Phony targets
.PHONY: all clean

# Compiler
CXX = g++

# Compiler flags
CXXFLAGS = -std=c++17 -Wall -Wextra -g

# Target executable name
TARGET = stopping_time

# Build target
all: $(TARGET)

$(TARGET): stopping_time.cpp stopping_time_visualisation.py
	$(CXX) $(CXXFLAGS) -o $(TARGET) stopping_time.cpp
	./$(TARGET)
	python stopping_time_visualisation.py

# Clean up build files
clean:
	rm -f $(TARGET)